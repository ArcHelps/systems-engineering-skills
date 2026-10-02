"""Check the distributable against local-file leaks and missing skill references."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


class PackagingTests(unittest.TestCase):
    def test_zip_excludes_symlinks_bytecode_and_contains_self_contained_skills(self):
        source = Path(__file__).resolve().parent.parent
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "plugin"
            root.mkdir()
            for name in (
                "arc_engineering",
                "skills",
                "references",
                "schemas",
                "scripts",
                "evaluations",
            ):
                shutil.copytree(
                    source / name,
                    root / name,
                    ignore=shutil.ignore_patterns("*.pyc", "__pycache__"),
                )
            (root / "examples").mkdir()
            (root / "evaluations/results").mkdir(exist_ok=True)
            (root / "evaluations/results/private-review.jsonl").write_text(
                "Private development output"
            )
            secret = Path(directory) / "private.txt"
            secret.write_text("Private customer source")
            (root / "examples/linked.txt").symlink_to(secret)
            (root / "arc_engineering/loose.pyc").write_bytes(b"local bytecode")
            subprocess.run(
                [sys.executable, str(root / "scripts/package_plugin.py")],
                cwd=root,
                env={**os.environ, "PYTHONPATH": str(root)},
                check=True,
                capture_output=True,
            )
            with zipfile.ZipFile(root / "dist/arc-engineering-plugin-0.1.0.zip") as archive:
                self.assertNotIn("examples/linked.txt", archive.namelist())
                self.assertFalse(
                    any(name.startswith("evaluations/results/") for name in archive.namelist())
                )
                self.assertIn("evaluations/requirements.jsonl", archive.namelist())
                self.assertFalse(any(name.endswith(".pyc") for name in archive.namelist()))
                prefix = "skills/review-requirement-ecss/"
                text = archive.read(prefix + "SKILL.md").decode()
                self.assertIn("references/engineering-contract.md", text)
                self.assertIn(prefix + "references/engineering-contract.md", archive.namelist())


if __name__ == "__main__":
    unittest.main()
