# Privacy and local processing

The server has no outbound HTTP client, telemetry, analytics, model API
client, or customer database. Reads and exports are confined to the workspace selected
by the operator. stdio is the default transport; HTTP binds only to 127.0.0.1. Do not
expose this unauthenticated local server publicly or through a tunnel.

When a connected assistant calls a file tool, the returned content reaches the MCP host
and may reach that host's AI provider. Prompts and engineering reasoning are performed
by the host. Local parsing therefore does not mean offline AI. Host retention, logging,
permissions and connector policies remain relevant. This package never instructs an
assistant to upload files to the publisher's servers.

Installing dependencies may contact the configured Python package registry. After
installation the Python server can run directly without network access. `uv` may also
check or download dependencies at startup unless run with offline mode. An operator can
install the locked environment first, then use its Python executable directly.

Inputs are never modified. Export creates a new file and refuses an existing filename.
Atomic publication leaves either a complete new file or no new file on ordinary
failure. Source IDs and file SHA-256 hashes are retained in import proposals. User text
is not executed as spreadsheet formulas, macros, shell commands or XML external entities.

The workspace guard is a path boundary, not an operating-system sandbox. Another local
process running as the same user can modify files or race path checks; use normal OS
permissions and isolation where the threat model requires it. A user deliberately
selecting a broad workspace authorizes broad reads within that folder. Select a dedicated
project folder rather than your home directory.

The library does not bundle licensed standards. Provide controlled authorized copies
or inspect permitted publisher sources. Standards summaries are guidance, not evidence
of project compliance. Human authorities own formal approval and acceptance.
