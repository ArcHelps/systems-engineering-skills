"""Packaging checks are distinct from evaluating engineering judgment."""

import json
import re

from jsonschema import Draft202012Validator

from .catalog import Catalog, data_root


def check_package() -> dict:
    catalog = Catalog()
    errors = []
    root = data_root()
    schema = json.loads((root / "schemas/model.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    cases = []
    for path in sorted((root / "evaluations").glob("*.jsonl")):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            try:
                case = json.loads(line)
                if (
                    not {"skill_id", "request", "input", "expected", "must_not", "negative_request"}
                    <= case.keys()
                ):
                    errors.append(f"{path.name}:{number}: incomplete evaluation")
                elif case["skill_id"] not in catalog.skills:
                    errors.append(f"{path.name}:{number}: unknown skill")
                else:
                    cases.append(case)
            except (ValueError, TypeError) as error:
                errors.append(f"{path.name}:{number}: {error}")
    for skill in catalog.skills.values():
        text = skill["instructions"]
        if not skill["category"] or not skill["title"]:
            errors.append(f"{skill['id']}: missing discovery metadata")
        if re.search(r"\b(?:TODO|FIXME|PLACEHOLDER)\b", text):
            errors.append(f"{skill['id']}: unfinished scaffold")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith("http"):
                continue
            resolved = (root / "skills" / skill["id"] / link).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                errors.append(f"{skill['id']}: unsafe or missing link {link}")
    # Installed wheels omit evaluation fixtures; source/distribution checks require them.
    if (root / "evaluations").is_dir():
        missing = catalog.skills.keys() - {case["skill_id"] for case in cases}
        errors.extend(f"{name}: no evaluation case" for name in sorted(missing))
    if len(catalog.skills) != 100:
        errors.append(f"Expected 100 skills, found {len(catalog.skills)}")
    return {
        "skills": len(catalog.skills),
        "references": len(catalog.references),
        "evaluation_cases": len(cases),
        "errors": errors,
        "scope": "Structure and coverage only; does not prove model judgment quality",
    }
