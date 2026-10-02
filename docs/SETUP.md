# Setup

Use the [README setup prompt](../README.md#-get-started) for assisted setup.
Start from an unzipped download or checkout. No public package-registry installation
or approved directory listing is currently available.

## Codex on your computer

From the Arc Skills folder, on macOS or Linux:

```sh
uv --no-config sync --locked
uv --no-config run --locked arc-engineering check
mkdir -p "$HOME/Documents/arc-engineering-work"
codex mcp add arc-engineering --env "PYTHONPATH=$PWD" -- "$PWD/.venv/bin/python" -m arc_engineering serve --workspace "$HOME/Documents/arc-engineering-work"
codex mcp list
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if missing.
It can provide Python if an appropriate version is not installed. These commands
download dependencies and add one local MCP entry to Codex configuration. Inspect an
existing `arc-engineering` entry before replacing it. They do not enable broader access
or change approval settings. The prepared Python environment runs without startup downloads.

On Windows, use PowerShell from the downloaded folder:

```powershell
uv --no-config sync --locked
uv --no-config run --locked arc-engineering check
$arcWork = Join-Path $HOME 'Documents/arc-engineering-work'
New-Item -ItemType Directory -Force -Path $arcWork | Out-Null
$arcPython = Join-Path (Get-Location).Path '.venv/Scripts/python.exe'
codex mcp add arc-engineering --env "PYTHONPATH=$((Get-Location).Path)" -- $arcPython -m arc_engineering serve --workspace $arcWork
codex mcp list
```

If the CLI is unavailable, generate the configuration instead:

```sh
uv --no-config run --locked arc-engineering config --workspace /absolute/path/to/arc-engineering-work --client codex
```

Merge its output into your Codex MCP configuration, preserving existing entries.
Alternatively, enter the generated command, arguments and environment in the desktop
app's MCP settings. Restart the client if the server is not yet visible. In a fresh
conversation, ask: `Use Arc Skills to list five requirement-review skills.`
Configuration listing alone does not prove the server connected; confirm tool discovery.

Copy only the files you want processed into `arc-engineering-work`. For a safe first
run, copy `examples/customer-requirements.csv` there and ask:

```text
Use Arc Skills to clean and map customer-requirements.csv.
Show all four requirements, source columns and the proposed parent links.
Review REQ-004 for verifiability. Export new files without overwriting inputs.
```

If a file is outside the configured folder, copy it into that folder or explicitly
reconfigure the workspace. Don't use your entire home directory as the workspace.

## ChatGPT web

ChatGPT web cannot start this local Python server or read your Codex configuration.
Attach the plugin ZIP, paste the README setup prompt, then upload the source material
you want reviewed. In a conversation with ZIP/file-analysis support, the assistant
can inspect the catalogue, read the selected `SKILL.md` and its bundled references,
and carry out the task using the file tools available in that conversation.

This is conversation-scoped use of the instructions, not an installed MCP or persistent
plugin. If ZIP reading is unavailable, paste the selected skill instructions and needed
reference text instead. Do not claim local file processing for this route. Actual plugin
installation requires a supported marketplace/directory route; none has been published.

## Other MCP clients

After `uv --no-config sync --locked`, generate Claude Desktop configuration:

```sh
uv --no-config run --locked arc-engineering config --workspace /absolute/path/to/arc-engineering-work --client claude
```

Merge the generated `mcpServers` entry into the client's existing configuration and
restart it. Other stdio-capable clients use the same command, arguments and environment.
Client UI installation has not been verified across every client.

## Downloads and updates

The plugin ZIP includes skills, their supporting references and the local server.
It does not install Python or uv. For a checkout, pull the selected update and run
`uv --no-config sync --locked` again. For a ZIP, download the replacement, unpack it
separately and update the configured path. Keep work files outside the installation.
Restart the client to load changes. Updating files is not a public-directory submission.

[Official MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) ·
[Plugin distribution](https://developers.openai.com/plugins/build/plugins)
