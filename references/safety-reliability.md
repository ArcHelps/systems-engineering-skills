# Safety, dependability and assurance reasoning

Toolkit-authored analysis guidance. Use the controlled safety and dependability plans and
the sources in standards.md for applicable definitions, classifications and objectives.

## Analysis boundaries

A hazard is a condition with potential harm, a failure mode describes how a function
or item fails, an effect describes the consequence at a defined level, and a cause
explains a mechanism. Preserve these distinctions. Start with mission phases, normal
and off-nominal modes, architecture boundaries and people exposed. Missing controls
are not assumed absent; mark evidence unavailable and ask for the mechanism.

FMEA traces each credible mode through local, next-higher and end effects. Fault trees
work backward from a precisely stated top event using justified AND/OR logic. Review
latent failures, common supplies, shared environments, common software, maintenance
errors, diagnostic coverage, recovery and exposure duration. Identically repeated
channels are not proof of independence. Do not model dependence as independent simply
because component failure rates are available.

## Quantification

For independent series components R_system = product(R_i). For independent parallel
success paths R_system = 1 - product(1 - R_i). State mission duration and assumptions;
simple formulas do not represent repair, switching faults, common causes, degraded
criteria or dependent failures. Constant-rate exponential R(t)=exp(-lambda*t) requires
a defensible constant-rate, no-repair model and consistent units. MTBF, reliability,
availability and failure probability are not interchangeable. Never invent failure
rates, coverage factors, probability allocations or acceptance thresholds.

If an ordinal severity/likelihood scale is supplied, use its definitions. Do not
multiply its code numbers into a quantitative risk estimate or create a universal RPN.
Rank and explain within the project's approved scheme. Formal risk acceptance and
hazard closure require authorized decisions and configuration-specific evidence.

## Assurance

Safety arguments connect a claim, context/assumptions, reasoning and evidence. Evidence
quantity is not adequacy. Identify scope mismatches, circular reasoning, stale versions,
unsupported independence and defeaters. Hazard mitigations need implementation and
verification evidence; a linked requirement is only a planned control.

FDAL, IDAL, software level and hardware DAL each have specific allocation scope and
process. Verify the applicable standard edition/objectives and independence requirements
from controlled text. This library cannot qualify a tool, allocate final assurance levels,
accept residual risk, certify software/hardware or approve a safety argument.
