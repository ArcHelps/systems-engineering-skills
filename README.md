# 🛠️ Systems Engineering Skills

**100 free AI skills for systems and hardware engineers.**

Review requirements against ECSS. Check electrical and mechanical interfaces.
Build power and mass budgets. Review environmental qualification tests, FMEA and verification evidence.

**[Browse all 100 skills →](CATALOG.md)** · [Setup](docs/SETUP.md) · [Example prompts](#-try-it)

## 🍽️ Pick a task

| What you have | Skill | What you get |
|---|---|---|
| A messy requirements spreadsheet | [Clean and map requirements](skills/clean-map-requirements-spreadsheet/SKILL.md) | A cleaned table, field mapping, import proposal and issues |
| A customer specification PDF | [Extract customer requirements](skills/extract-customer-requirements/SKILL.md) | A requirement register with IDs, page references and open questions |
| A requirement + the applicable ECSS edition | [Review a requirement against ECSS](skills/review-requirement-ecss/SKILL.md) | Findings tied to inspected criteria, with proposed corrections |
| A parent requirement | [Derive sub-requirements](skills/derive-sub-requirements/SKILL.md) | Proposed children, derivation rationale and unresolved decisions |
| Parent and child requirements | [Compare children to parents](skills/compare-child-parent-requirements/SKILL.md) | Gaps, unsupported additions and a coverage table |
| A requirements specification | [Find conflicting requirements](skills/identify-conflicting-requirements/SKILL.md) | Conflicting pairs, shared conditions and proposed resolutions |
| Requirements awaiting verification | [Build a verification matrix](skills/build-requirements-verification-matrix/SKILL.md) | Requirement-to-method mapping and missing acceptance criteria |
| Test results + acceptance criteria | [Assess test results](skills/assess-test-results/SKILL.md) | Evidence assessment, limitations and unresolved outcomes |
| A tender + your response evidence | [Build a tender compliance matrix](skills/build-tender-compliance-matrix/SKILL.md) | Clause-by-clause responses, evidence and exceptions |
| Two versions of a specification | [Compare specification versions](skills/compare-requirements-specification-versions/SKILL.md) | A change register and candidate verification impacts |
| An electrical interface specification | [Review an electrical interface](skills/review-electrical-interface/SKILL.md) | Missing or inconsistent voltage, current, signal, grounding and fault parameters |
| Mechanical interface drawings | [Review a mechanical interface](skills/review-mechanical-interface/SKILL.md) | Mating geometry, datum, tolerance, clearance and load checks; unresolved drawing details |
| Component loads and supply limits | [Build a system power budget](skills/build-system-power-budget/SKILL.md) | Power demand by operating mode, remaining margin and unresolved loads |
| Component masses and quantities | [Build a system mass budget](skills/build-system-mass-budget/SKILL.md) | Component totals, subsystem rollups, remaining allowance and missing estimates |
| Environmental requirements and test reports | [Review environmental qualification coverage](skills/review-environmental-qualification-coverage/SKILL.md) | Required conditions mapped to test evidence, with uncovered conditions identified |
| An FMEA | [Review an FMEA for missing failure modes](skills/review-fmea-missing-failure-modes/SKILL.md) | Candidate omissions, failure consequences and questions requiring engineering judgment |
| Airborne electronic hardware assurance records + applicable objectives | [Check DO-254 assurance evidence](skills/check-do254-hardware-assurance-evidence/SKILL.md) | Evidence gaps against supplied, applicable objectives |

There are also skills for **interfaces, architecture, budgets, safety, reliability,
change control and design reviews**. [See the full menu →](CATALOG.md)

## 🚀 Get started

Download this repo using **[Code → Download ZIP](https://github.com/ArcHelps/systems-engineering-skills/archive/refs/heads/main.zip)**. Open the unzipped folder in Codex,
or attach the ZIP to a ChatGPT conversation that supports file analysis.

**Copy and paste this setup prompt:**

```text
Set up Arc Skills from:
https://github.com/ArcHelps/systems-engineering-skills
Use the repository or ZIP I provided, or fetch the public repository if your tools allow it.
Read README.md and docs/SETUP.md, then choose the route this client supports.
If you can run local commands, install the locked dependencies, connect the local
MCP to Codex using the documented configuration, and check skill discovery.
Use a dedicated arc-engineering-work folder for inputs and new outputs.
Keep my existing settings and source files intact. Do not publish or upload my files.
If you cannot run a local MCP, read the attached catalogue and load only the
selected skill and its references for this conversation. Explain any unavailable tools.
Show me five relevant skills and run the synthetic requirements example if possible.
Say which route actually worked and whether I need to restart or enable anything.
```

| Where you use it | What works |
|---|---|
| **Codex on your computer** | Local MCP with all 100 skills and file tools. Recommended. |
| **ChatGPT web** | Attached skill instructions + ChatGPT's available file tools. This does not install the MCP. |
| **Claude Desktop / other local MCP clients** | The same local MCP; [connection instructions](docs/SETUP.md#other-mcp-clients). |

Local setup needs **Python 3.11+ and uv**. No model API key needed.

## 💬 Try it

Attach a file or place it in your configured work folder, then paste a prompt:

**Clean requirements**

```text
Use Arc Skills to clean and map customer-requirements.xlsx.
Preserve every source ID and original statement. Show the field mapping,
duplicate IDs, TBDs/TBCs, missing information and unresolved links.
Give me a cleaned workbook and an import proposal. Reconcile all row counts.
```

**Review a specification**

```text
Use Arc Skills to extract and review this requirements PDF.
Keep page references, notes, figures and deleted requirements visible.
Give me a requirements table and the most consequential issues first:
contradictions, broken references, unclear limits and unverifiable statements.
Separate confirmed problems from ambiguities. Don't invent missing values.
```

**Review against ECSS**

```text
Use Arc Skills to review REQ-014 against the ECSS-E-ST-10-06 edition
I attached. Cite the inspected criteria, explain each finding and propose
the smallest correction. Preserve the original wording beside the proposal.
If you cannot inspect the applicable standard, label the review advisory.
```

**Build a power budget**

```text
Use Arc Skills to build a system power budget from component-loads.xlsx.
Separate standby, nominal and peak demand by operating mode. Preserve units,
quantities, duty cycles and source values. Show demand against the supplied
power limits, conversion losses, missing loads and remaining margin.
Don't assume every peak load operates simultaneously or invent missing values.
```

**No file yet?**

```text
Use Arc Skills to review this requirement:
"The unit shall provide an appropriate warning quickly."
Explain what is missing and propose clearer wording without inventing a latency.
```

## 🔒 Your files

The local MCP processes files in your chosen folder without uploading them to an external server.
Your assistant and its AI provider still process the content used in the conversation.
ChatGPT uploads follow ChatGPT's policies. [Data flow →](docs/PRIVACY.md)

The skills and code are free under the [MIT license](LICENSE). Your AI assistant may have
its own charges. Standards are not bundled; provide authorized copies when needed.
Engineering edits are proposals for your review, with source wording preserved.

<details>
<summary>For contributors</summary>

[Write a skill](docs/AUTHORING.md) · [Validation and limits](docs/VALIDATION.md) · [MCP tools](docs/TOOLS.md)

</details>
