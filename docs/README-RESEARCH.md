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

Our README follows: one sentence → input/task/output examples → one adaptive
setup prompt → client support → useful prompts → short privacy/free-use note.
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

The checkout has its own Git root and the public repository URL is
https://github.com/ArcHelps/systems-engineering-skills. Local documentation changes
do not publish a release or confer directory approval. No private application history
or customer artifacts were copied.

## Hardware positioning and attribution — 3 October 2026

The README and package metadata explicitly name systems and hardware engineers.
The main menu includes electrical and mechanical interfaces, power and mass budgets,
environmental qualification coverage, FMEA review and DO-254 evidence checks.
These are existing capabilities; the wording does not claim PCB layout, circuit
simulation or CAD generation. Repeated publisher slogans and account references
are removed; the Arc Skills invocation remains the established trigger.

Skill author comments preserve attribution when files are copied. They are not a
proven GEO tactic and do not require branding in generated answers. Two shared
references link to inspected publisher guides where they provide relevant reading,
without treating them as engineering standards or requiring a website visit.

[Google's generative AI search guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
supports useful, readable content and ordinary SEO fundamentals; it does not establish
a ranking benefit from author comments or repeated self-links. These links serve readers
and identify supporting publisher material. No claim is made about improved AI citations.
