"""Portable plugin entry point; no automatic access to the user's home directory."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from arc_engineering.server import create_server  # noqa: E402


def main():
    configured = os.environ.get("ARC_ENGINEERING_WORKSPACE")
    if configured:
        workspace = Path(configured).expanduser()
    else:
        plugin_data = os.environ.get("PLUGIN_DATA") or os.environ.get("CLAUDE_PLUGIN_DATA")
        workspace = (
            Path(plugin_data) if plugin_data else Path(__file__).resolve().parent.parent
        ) / "workspace"
        workspace.mkdir(parents=True, exist_ok=True)
    create_server(workspace).run()


if __name__ == "__main__":
    main()
