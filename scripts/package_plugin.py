"""Create a self-contained plugin ZIP without customer data or local environments."""

import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from arc_engineering.catalog import Catalog  # noqa: E402
from arc_engineering.validation import check_package  # noqa: E402


def main():
    root = Path(__file__).resolve().parent.parent
    result = check_package()
    if result["errors"]:
        raise SystemExit(json.dumps(result))
    catalog = Catalog(root)
    output = root / "dist" / "arc-engineering-plugin-0.1.0.zip"
    output.parent.mkdir(exist_ok=True)
    excluded = {".venv", "__pycache__", ".ruff_cache", "dist", "workspace", ".git"}
    included = {
        "arc_engineering",
        "references",
        "schemas",
        "evaluations",
        "examples",
        "scripts",
        "tests",
        "docs",
    }
    root_files = {
        "plugin.json",
        "mcp.json",
        "pyproject.toml",
        "uv.lock",
        "README.md",
        "CATALOG.md",
        "LICENSE",
    }
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            relative = path.relative_to(root)
            if (
                not path.is_file()
                or path.is_symlink()
                or relative.parts[:2] == ("evaluations", "results")
                or path.suffix == ".pyc"
                or any(part in excluded for part in relative.parts)
            ):
                continue
            if relative.parts[0] in included or str(relative) in root_files:
                archive.write(path, str(relative))
        # Each skill in the ZIP works even if an installer copies only that directory.
        for skill in catalog.skills.values():
            base = f"skills/{skill['id']}"
            archive.writestr(
                f"{base}/SKILL.md",
                skill["instructions"].replace("../../references/", "references/"),
            )
            for reference_id in skill["references"]:
                archive.writestr(
                    f"{base}/references/{reference_id}.md", catalog.reference(reference_id)
                )
    print(output)


if __name__ == "__main__":
    main()
