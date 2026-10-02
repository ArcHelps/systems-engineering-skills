"""Validation and analysis of local exchange proposals, never external database writes."""

import json
from collections import defaultdict, deque
from graphlib import CycleError, TopologicalSorter

from jsonschema import Draft202012Validator

from .catalog import data_root


SCHEMA = json.loads((data_root() / "schemas/model.schema.json").read_text())
ENDPOINTS = {
    "contains": ({"system"}, {"system"}),
    "derives": ({"requirement"}, {"requirement"}),
    "allocated_to": ({"requirement"}, {"system"}),
    "satisfied_by": ({"requirement"}, {"system"}),
    "interface": ({"system"}, {"system"}),
    "verifies": ({"test"}, {"requirement"}),
    "includes_test": ({"test_plan"}, {"test"}),
    "identifies": ({"requirement", "system"}, {"risk"}),
    "mitigated_by": ({"risk"}, {"requirement", "system"}),
    "has_property": ({"system"}, {"property"}),
    "constrains": ({"requirement"}, {"property"}),
    "depends_on": ({"property"}, {"property"}),
}


def validate_model(model: dict) -> dict:
    """Check exchange structure, fixed endpoints, uniqueness, and hierarchy cycles."""
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in Draft202012Validator(SCHEMA).iter_errors(model)
    ]
    if errors:
        return {"valid": False, "errors": errors, "warnings": []}
    items = {item["id"]: item for item in model["items"]}
    ids = [row["id"] for row in model["items"] + model["relationships"]]
    if len(set(ids)) != len(ids):
        errors.append("Every local item and relationship ID must be unique")
    interfaces = set()
    plan_positions = set()
    relationships_by_id = {row["id"]: row for row in model["relationships"]}
    graphs = {kind: defaultdict(set) for kind in ("contains", "derives", "depends_on")}
    warnings = []
    for edge in model["relationships"]:
        kind, source, target = edge["type"], edge["source"], edge["target"]
        if source not in items or target not in items:
            errors.append(f"{edge['id']}: unresolved endpoint {source} -> {target}")
            continue
        allowed_source, allowed_target = ENDPOINTS[kind]
        if (
            items[source]["type"] not in allowed_source
            or items[target]["type"] not in allowed_target
        ):
            errors.append(f"{edge['id']}: invalid {kind} endpoint types")
        if source == target:
            errors.append(f"{edge['id']}: self relationship is not permitted")
        if kind in graphs:
            graphs[kind][target].add(source)
        if kind == "interface":
            pair = frozenset((source, target))
            if pair in interfaces:
                errors.append(f"{edge['id']}: duplicate interface for unordered System pair")
            interfaces.add(pair)
            for req in edge["fields"].get("requirement_ids", []):
                if req not in items or items[req]["type"] != "requirement":
                    errors.append(f"{edge['id']}: invalid linked Requirement {req}")
        if kind == "depends_on" and not edge.get("metadata", {}).get("derived_from_expression"):
            errors.append(f"{edge['id']}: depends_on must be derived from a Property expression")
        if kind == "includes_test":
            slot = (source, edge["fields"]["position"])
            if slot in plan_positions:
                errors.append(f"{edge['id']}: Test Plan slot positions must be unique")
            plan_positions.add(slot)
    for kind, graph in graphs.items():
        try:
            TopologicalSorter(graph).prepare()
        except CycleError:
            errors.append(f"{kind}: cycle detected")
    for item in model["items"]:
        if item["type"] == "test":
            for step in item["fields"].get("steps", []):
                constraint_id = step.get("constraint_relationship_id")
                if (
                    constraint_id
                    and relationships_by_id.get(constraint_id, {}).get("type") != "constrains"
                ):
                    errors.append(
                        f"{item['id']}: Test step refers to missing or non-Constraint {constraint_id}"
                    )
        if item["type"] == "property" and item.get("status") not in (None, "active"):
            errors.append(f"{item['id']}: Properties have no editable lifecycle status")
        if item["type"] == "test_plan" and item.get("status") == "active":
            if not any(
                edge["type"] == "includes_test" and edge["source"] == item["id"]
                for edge in model["relationships"]
            ):
                warnings.append(
                    f"{item['id']}: active Test Plan has no slots; cannot start a Cycle"
                )
    return {"valid": not errors, "errors": errors, "warnings": warnings}


def require_valid(model: dict) -> None:
    result = validate_model(model)
    if not result["valid"]:
        raise ValueError("Invalid exchange model: " + "; ".join(result["errors"][:10]))


def compare_models(before: dict, after: dict) -> dict:
    """Compare exact records by stable local ID; order is not an engineering change."""
    require_valid(before)
    require_valid(after)
    if any(
        item.get("metadata", {}).get("identity_unresolved")
        for model in (before, after)
        for item in model["items"]
    ):
        raise ValueError(
            "Resolve missing or duplicate source IDs before comparing model identities"
        )
    result = {}
    for collection in ("items", "relationships"):
        old = {row["id"]: row for row in before[collection]}
        new = {row["id"]: row for row in after[collection]}
        result[collection] = {
            "added": [new[key] for key in sorted(new.keys() - old.keys())],
            "removed": [old[key] for key in sorted(old.keys() - new.keys())],
            "modified": [
                {"id": key, "before": old[key], "after": new[key]}
                for key in sorted(old.keys() & new.keys())
                if old[key] != new[key]
            ],
        }
    return result


def trace_relationships(
    model: dict,
    start_id: str,
    relationship_types: list[str] | None = None,
    direction: str = "both",
    max_depth: int = 4,
) -> dict:
    """Return bounded recorded paths. Paths do not prove semantic impact or compliance."""
    require_valid(model)
    if direction not in {"incoming", "outgoing", "both"} or not 1 <= max_depth <= 12:
        raise ValueError("direction must be incoming/outgoing/both; max_depth must be 1..12")
    if start_id not in {item["id"] for item in model["items"]}:
        raise ValueError("Unknown starting Item")
    kinds = set(relationship_types or ENDPOINTS)
    if kinds - ENDPOINTS.keys():
        raise ValueError("Unknown Relationship Type")
    adjacency = defaultdict(list)
    for edge in model["relationships"]:
        if edge["type"] not in kinds:
            continue
        if direction in {"outgoing", "both"}:
            adjacency[edge["source"]].append((edge["target"], edge["id"]))
        if direction in {"incoming", "both"}:
            adjacency[edge["target"]].append((edge["source"], edge["id"]))
    queue = deque([([start_id], [])])
    paths = []
    truncated = False
    while queue:
        item_ids, edge_ids = queue.popleft()
        for target, edge_id in adjacency[item_ids[-1]]:
            if target in item_ids:
                continue
            if len(edge_ids) >= max_depth:
                truncated = True
                continue
            path = {"item_ids": item_ids + [target], "relationship_ids": edge_ids + [edge_id]}
            paths.append(path)
            if len(paths) >= 1000:
                return {"paths": paths, "truncated": True, "reason": "1000 path limit"}
            queue.append((path["item_ids"], path["relationship_ids"]))
    return {
        "paths": paths,
        "truncated": truncated,
        "meaning": "Recorded dependencies only; engineering impact requires assessment",
    }
