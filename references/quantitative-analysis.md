# Budgets, margins and quantitative analysis

Treat every engineering quantity as value, unit, basis, configuration, conditions,
source and uncertainty/maturity. A budget allocation is a proposed decision, not a
measured value. Keep requirement limits, allocations, estimates, measured values,
reserves and margins separate so reserves are not counted twice.

## Aggregation

Mass normally sums non-overlapping contributions. Identify assemblies that include
their children so a rolled-up value is not added again. Power requires operating modes,
duty cycles, simultaneity, conversion losses and peaks. Averaged power cannot prove
peak adequacy. Latency requires defined endpoints, sampling/jitter, processing, queues
and communication; parallel operations and overlapping intervals cannot simply be
added. Performance allocations need a justified combination rule, not equal division.

Root-sum-square uncertainty requires applicable independent error terms and a stated
statistical interpretation. Use worst-case sums for bounded quantities when appropriate;
do not convert between bounds, sigma and confidence intervals without justification.
Correlation and systematic bias can defeat naive RSS. Avoid false precision.

## Limits and margins

Convert compatible units before comparison and retain authored values. For a maximum
limit L and actual A, signed headroom L-A is positive when below the limit. A fractional
margin needs an explicit denominator and convention; division by zero is unresolved.
For a minimum limit use A-L. Strict < or > excludes equality; <= or >= includes it.
Equality requirements need the approved tolerance/decision rule rather than an invented
epsilon. Offset temperatures and temperature differences have different conversion
rules. Dimensionless count, ratio, percentages and logarithmic values need explicit
interpretation. The local model validator does not evaluate units or formulas.

## Trade studies

Start with alternatives that meet mandatory feasibility constraints. Keep those
constraints separate from preference scores. Weighted scores require agreed criteria,
scales, weights and evidence; show sensitivity to weights and uncertain inputs. A
best nominal score need not be a robust recommendation. Make/buy additionally needs
integration, assurance, supplier evidence, maintainability and lifecycle cost context.

## Output

Deliver inputs and provenance, transparent equations, assumptions, numerical result
with units, unmet or unresolved constraints and sensitivity where decision-relevant.
In the exchange model, quantities use Property Items, System `has_property` and Requirement
`constrains` relationships. Do not create Budget, Port or Calculation Item Types.
Use an existing host calculation tool for arithmetic; the assistant must not claim
`validate_model` has checked engineering arithmetic, unit conversions or formulas.
