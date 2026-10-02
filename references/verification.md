# Verification and evidence

Toolkit-authored working method informed by the [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
and ECSS verification references listed in standards.md. No clause text is reproduced.

Verification asks whether the implementation meets specified requirements. Validation
asks whether the specified/delivered system meets stakeholder needs in its intended use.
Do not infer either from the other. A requirement may need several methods across
different levels, conditions, models and stages.

## Select a method

Specify the subject, required response or property, operating conditions, measurable
criterion, observable evidence, configuration and justified method. Test actively exercises
and measures; inspection examines physical/documented attributes; analysis derives
results from justified models/data; demonstration shows behavior in defined conditions.
Project taxonomies may also name review/modeling; use the controlled verification plan
to establish how those map to accepted methods. Method selection alone is not a test plan.

Evaluate observability, safety of exercising the condition, test feasibility, measurement
uncertainty, representativeness, model validity, and required assurance independence.
An analysis result needs input provenance, assumptions, domain of validity and model
verification/validation where relevant. Simulation is not automatically qualification.

## Procedure and evidence

Record requirement revision, product configuration, setup, environmental conditions,
instrument calibration, step/action, expected result, limits, recorded measurement,
anomaly/deviation, execution identity and time. Acceptance criteria must precede results;
do not rewrite them to fit observed performance. A Run pass against obsolete criteria
does not demonstrate a changed requirement.

Example: a maximum 100 ms response measured as 98 ms with ±5 ms uncertainty cannot be
declared unambiguously compliant under a conservative worst-case criterion. Report the
nominal measurement, uncertainty, applicable decision rule and resulting uncertainty;
do not invent a statistical confidence or apply an unstated guard band.

Qualification and acceptance serve different purposes. Confirm applicable levels,
durations, models and conditions from the project-approved basis; never use generic
vibration/thermal numbers. Waived test steps require disposition evidence, not a silent
pass. A test report references its exact configuration and controlled procedure.

## Coverage and freshness

`verifies` means a Test is scoped to a Requirement. It does not establish adequate
conditions, successful execution, current evidence or accepted close-out. Separate
planned coverage, executed evidence, technical adequacy and authorized acceptance.
After a change, trace dependencies and examine whether assumptions, limits, setup,
implementation or configuration differ. Identify candidate re-verification and retained
justifications; graph proximity alone does not invalidate or preserve evidence.
