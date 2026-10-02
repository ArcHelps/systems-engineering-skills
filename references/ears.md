# EARS requirement writing

Toolkit-authored practical guidance based on [Alistair Mavin's EARS overview](https://alistairmavin.com/ears/).
Use the simplest pattern that represents the actual intent:

| Pattern | Shape | Use |
|---|---|---|
| Ubiquitous | The system shall [response]. | Obligation holds without a trigger/state qualifier |
| Event-driven | When trigger, the system shall [response]. | Discrete triggering event |
| State-driven | While state, the system shall [response]. | Continuous obligation during a state |
| Unwanted behaviour | If unwanted condition, then the system shall [response]. | Defined abnormal condition |
| Optional feature | Where feature is included, the system shall [response]. | Applicability depends on product feature |
| Combined | While state, when event, the system shall [response]. | Both qualifiers materially constrain the response |

Preserve actor, obligation, conditions, quantities, units, tolerances and modality. “Shall”
does not cure missing intent. “May” and “should” are not interchangeable with “shall.”
Do not replace an event with a persistent state or treat a state as a one-time event.
Optional feature “where” concerns configuration, not physical location.

Example: “The receiver shall warn quickly when messages stop” can become “When no valid
message has been received for [approved timeout], the receiver shall assert the
communication-loss warning within [approved warning latency].” The bracketed quantities
are unresolved engineering decisions, not invented numbers. Keep the original beside it.
“The enclosure shall have a mass no greater than 2 kg” already fits a simple ubiquitous
statement; do not add arbitrary triggers or rewrite for cosmetic uniformity.

Atomicity means a coherent verifiable obligation. Several closely coupled responses can
be one obligation if their coupling is intentional; sentence length alone does not
justify splitting. Deriving child requirements additionally requires a rationale,
allocation and preservation of parent intent; EARS rewriting alone does not do this.
