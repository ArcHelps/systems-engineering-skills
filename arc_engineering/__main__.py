"""Local stdio is the default; loopback HTTP is available for local clients."""

import argparse
import json
import os
from pathlib import Path

from .catalog import Catalog


def main():
    parser = argparse.ArgumentParser(description="Arc systems-engineering skills and local MCP")
    subcommands = parser.add_subparsers(dest="command", required=True)
    serve = subcommands.add_parser("serve", help="Start the MCP server")
    serve.add_argument("--workspace", default=os.environ.get("ARC_ENGINEERING_WORKSPACE"))
    serve.add_argument("--transport", choices=["stdio", "streamable-http"], default="stdio")
    serve.add_argument("--port", type=int, default=8765)
    listing = subcommands.add_parser("list", help="List or search the skills")
    listing.add_argument("query", nargs="?", default="")
    listing.add_argument("--category", default="")
    config = subcommands.add_parser(
        "config", help="Print a client configuration without editing it"
    )
    config.add_argument("--workspace", required=True)
    config.add_argument("--client", choices=["codex", "claude"], default="codex")
    subcommands.add_parser("check", help="Validate catalog, links, schemas and evaluation coverage")
    args = parser.parse_args()
    if args.command == "serve":
        if not args.workspace:
            parser.error(
                "Provide --workspace or ARC_ENGINEERING_WORKSPACE; no broad filesystem default"
            )
        from .server import create_server

        server = create_server(Path(args.workspace))
        if args.transport == "stdio":
            server.run()
        else:
            if not 1 <= args.port <= 65535:
                parser.error("port must be 1..65535")
            # No public bind until deployment, authentication and tenant scoping are designed.
            server.run(transport="streamable-http", host="127.0.0.1", port=args.port)
    elif args.command == "list":
        print(
            json.dumps(
                Catalog().search(args.query, args.category, 100), ensure_ascii=False, indent=2
            )
        )
    elif args.command == "config":
        import sys
        from .files import Workspace

        workspace = Workspace(args.workspace)
        command = str(Path(sys.executable).absolute())
        arguments = ["-m", "arc_engineering", "serve", "--workspace", str(workspace.root)]
        source_root = str(Path(__file__).resolve().parent.parent)
        # Source checkouts need PYTHONPATH; installed packages ignore this harmless extra path.
        if args.client == "claude":
            print(
                json.dumps(
                    {
                        "mcpServers": {
                            "arc-engineering": {
                                "command": command,
                                "args": arguments,
                                "env": {"PYTHONPATH": source_root},
                            }
                        }
                    },
                    indent=2,
                )
            )
        else:
            print("[mcp_servers.arc-engineering]")
            print("command = " + json.dumps(command))
            print("args = " + json.dumps(arguments))
            print("[mcp_servers.arc-engineering.env]")
            print("PYTHONPATH = " + json.dumps(source_root))
    else:
        from .validation import check_package

        result = check_package()
        print(json.dumps(result, indent=2))
        if result["errors"]:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
