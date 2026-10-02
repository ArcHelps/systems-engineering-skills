# Validation record — 1 October 2026

## Repository separation and setup check — 2 October 2026

Moved the toolkit to its own local Git root, rebuilt its locked environment and
kept its skills, runtime and synthetic examples together. No private application history
or customer artifacts were copied into the new repository. No remote is configured.

Package structure checks found 100 skills, 8 references and 108 evaluation cases with
no errors. A real stdio client launched from the new location, discovered 100 prompts
and 11 tools, found the cleanup skill and mapped all four synthetic example records
with one parent link. README/catalogue/document links were checked. The rebuilt plugin
ZIP contains current setup documents and the MIT license, all 100 skills and their
references, without a virtual environment, Git history or customer artifacts.

Ruff and Python distribution builds passed. No tests were created or edited and no
unit-test suite was run for these documentation/packaging changes. This setup check
does not establish client UI installation or ChatGPT ZIP-analysis availability.

This is a working local MCP toolkit and portable plugin package. It has no public
deployment, directory approval, external application write integration, or custom interactive UI.

## Public distribution wording and exclusions — 2 October 2026

The exchange definitions, endpoint rules and baseline review checks are retained.
Guidance describes the toolkit’s exchange model without identifying private source
files or attributing its rules to another application’s implementation. The shared
model reference is now engineering-model.md. Raw development outputs and scores
are archived outside the public repository; synthetic cases remain included.
Packaging excludes evaluations/results even if later recreated locally.

## Deterministic checks

- 100 skill files passed the skill-creator validator and the package's naming,
  reference, local-link, schema and acceptance-case coverage checks.
- 27 toolkit tests passed. They exercise real stdio MCP discovery and file tools,
  a 5,000-record file-backed import, path confinement, no-overwrite export, unsafe
  XML rejection, spreadsheet formula handling, malformed CSV/ZIP/PDF, and model
  endpoints, cycles, diffs and recorded trace paths. No external application suite ran.
- Ruff lint and formatting passed for the server, scripts and tests.
- plugin.json and mcp.json passed the published Agent Plugins 1.0.0 JSON schemas.
- A real loopback Streamable HTTP client exercised all 11 tools and listed all
  100 prompts. The temporary server was stopped afterward.
- The five-skill extension was exercised through real skills/list and skills/get
  RPCs. Every advertised resource was retrieved and its SHA-256 digest verified.
- Built a wheel, source archive and portable plugin ZIP. The wheel installed in a
  fresh temporary environment and ran outside the checkout. Both the wheel server
  and unpacked plugin launcher exposed 100 prompts, rendered shared references,
  served the five-skill RPC bundle with correct digests and read a synthetic source.
  Generated Codex TOML and Claude JSON configurations parsed successfully and used
  the actual interpreter/workspace paths. All 100 exact task-title searches returned
  their intended skill in the first five results.

The independent code review exposed defects that were corrected before packaging:
stale XLSX dimensions hiding rows, missing formula-cache warnings growing beyond
response limits, multiline CSV source lines, unmatched quotes merging requirements,
ReqIF block text running together, ancillary ReqIF record bounds, ambiguous IDs
appearing stable across imports, XLSX cell truncation and silent sheet renaming,
nonfinite numeric export, missing bundled prompt references, and package symlink
reads. Meaningful regression checks were written before each implementation fix.

## Engineering behavior

The 108 synthetic scenarios in evaluations/*.jsonl cover all 100 skills. Development
runs reported 108 passing cases after informed repairs and eight passing synthetic
transfer cases. Raw development outputs, scores and repair history are retained
privately outside this repository and are not included in public downloads.

These are author-run development evaluations, with some self-scoring and informed
repairs. Several original cases resemble worked examples. They are not independent
blind qualification, statistical reliability evidence, or proof of performance in
every host/model. Validate the workflows against your controlled project data and
intended client before taking formal engineering credit.

## Limits and distribution

The exchange schema defines this toolkit’s local proposal format. Validity is
structural and endpoint validation; units, formulas and constraint literals still
need engineering review. It does not implement external application permissions,
change-control workflows or evidence acceptance. The host assistant provides AI reasoning, so local parsing does not mean
offline inference or prevent host/provider processing.

Readers are bounded to 50 MiB input, 200 MiB expanded archive, 100,000 records per
reader collection, 10,000 imported records and 1,000 records per read. Tool responses
have a 2 MiB cap. Large imports can save the full proposal to new JSON and return a
bounded summary. An individual oversized record/text line requires an explicit split
or authorized host tool. OCR, XLS/XLSM and compressed ReqIF are not implemented.

Installation support is documented and MCP transport was tested; no live browser or
client UI verification was performed. Visual QA is left to Josh if UI is added.
OpenAI's current static MCP skill import accepts five skills; all 100 are exposed
through standard MCP prompts/resources/tools and the portable package. Public
submission requires its supported distribution route and review; nothing was submitted.

Sources: [OpenAI MCP skill import and endpoint requirements](https://developers.openai.com/plugins/build/mcp-server),
[plugin packaging](https://developers.openai.com/plugins/build/plugins),
[Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json),
[MCP configuration schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json).
