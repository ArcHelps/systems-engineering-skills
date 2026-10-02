# README decisions

Reviewed 2 October 2026. These are popular examples, not an exhaustive GitHub ranking.
Stars are rounded counts shown by GitHub at review time, not quality evidence.

| Repository | Stars | Pattern worth using |
|---|---:|---|
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | 95.8k | A browseable menu grouped by task/category |
| [MCP reference servers](https://github.com/modelcontextprotocol/servers) | 90.9k | Concise capability descriptions and executable setup examples |
| [Context7](https://github.com/upstash/context7) | 62.6k | Concrete prompt examples and a short explanation of the result |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 37.7k | A standard connection example before detailed options |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | 33.3k | Recognizable use cases and explicit client prerequisites |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | 28.0k | Separate user entry points from framework documentation |

Our README follows: one sentence → ten input/task/output examples → one adaptive
setup prompt → client support → four useful prompts → short privacy/free-use note.
The complete 100-skill menu remains CATALOG.md. Technical instructions and evidence
live under docs/. Existing skill folders and Python package layout stay intact.

One README plus a catalogue is the lowest-maintenance public surface. Putting all
100 skills and every client's config into the README would avoid clicking, but would
bury setup and increase scrolling. Keeping supporting documents preserves detail
without asking a new user to learn the internals. No new website, installer framework,
generated catalogue or hosted service is needed.

The setup prompt must not imply that ChatGPT web can install a local MCP. The
[official MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
distinguishes local Codex configuration from remote tools in ChatGPT web. Attached
skill instructions are an explicit conversation-scoped fallback. We have not
verified ChatGPT ZIP execution or every client UI. The supported local MCP is checked
through its protocol rather than inferred from a successful config write.

The new checkout has its own Git root and no remote. Before publishing: choose the
public repository URL, review the MIT license/publisher identity and publish a release
if a dedicated downloadable plugin ZIP is wanted. No public URL or directory approval
is assumed in the README, and no private application history or customer artifacts were copied.
