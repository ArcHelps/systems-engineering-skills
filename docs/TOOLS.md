# Local tools

Your assistant supplies the AI reasoning. The server loads skills and performs local
file operations. It does not call a model, update an external application or approve engineering decisions.

| Tool | Purpose |
|---|---|
| search_skills / get_skill | Find a task and load its instructions |
| read_reference | Load shared guidance |
| inspect_file / read_file | Inspect inputs and read bounded pages with source hashes |
| import_requirements | Explicitly map columns into a source-preserving proposal |
| validate_model / load_model | Validate/read the local exchange format |
| compare_models | Compare exact record changes |
| trace_relationships | Follow recorded links, with visible limits |
| export_artifact | Create new JSON, CSV, XLSX, Markdown or text files |

Inputs: UTF-8 CSV/TSV, XLSX, uncompressed ReqIF, JSON, TXT/Markdown, searchable PDF and
DOCX body text/tables. PDF figures and image tables need separate inspection. OCR,
XLS/XLSM and compressed ReqIF are not built in. [Limits](VALIDATION.md).

The workspace must exist. Relative paths resolve inside it; outside paths are rejected.
Exports never overwrite. The [exchange format](../schemas/model.schema.json) defines
this toolkit’s engineering proposals; it is not an external application API schema.

For manual server startup:

```sh
uv --no-config run --locked arc-engineering serve --workspace /absolute/path/to/project
```

This waits for a stdio MCP client; it is not a browser application. Loopback HTTP is
available with `--transport streamable-http --port 8765` at `http://127.0.0.1:8765/mcp`.
It is a local service without public authentication; no public hosting is provided.

For portable plugin clients, `plugin.json` and `mcp.json` launch the same server. Set
`ARC_ENGINEERING_WORKSPACE` to select a folder; otherwise the launcher creates a
dedicated `workspace` under `PLUGIN_DATA`, or under the plugin folder as a fallback.
It requires uv. OpenAI's Scan Tools bundle advertises five skills; all 100 remain
available through standard MCP prompts/resources/tools and the ZIP.

## Maintain the package

```sh
uv --no-config run --locked arc-engineering check
uv --no-config run --locked ruff check arc_engineering scripts tests
uv --no-config run --locked ruff format --check arc_engineering scripts tests
uv --no-config build
uv --no-config run --locked python scripts/package_plugin.py
```

Run only affected tests during local edits. For an explicitly requested full toolkit
verification: `uv --no-config run --locked python -m unittest discover -s tests`.

[Authoring](AUTHORING.md) · [Evaluation evidence](VALIDATION.md) · [Privacy](PRIVACY.md)
