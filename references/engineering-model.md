# Engineering exchange model

This toolkit uses the fixed exchange definitions below for local engineering proposals.
They describe this package’s output format, not an external application’s API or storage
implementation. Records use local IDs; applying proposals to another system requires
that system’s authorized import and review process. No such integration is included.

## Fixed Item Types

| Type key | Core content |
|---|---|
| requirement | Required statement; optional rationale, priority, requirement_types, notes |
| system | Optional description and notes; hierarchy uses contains |
| test | Required method, objective, acceptance_criteria; optional procedure, steps, automation_ref, notes |
| test_plan | Required objective; optional entry_criteria, exit_criteria, notes |
| risk | Required cause, event, consequence, severity, likelihood; optional notes |
| property | Required unit; optional expression and notes; value is derived, no editable lifecycle status |

Each Item has a required name. Owners are steward assignments, not inherited permissions.
Other than Properties, lifecycle statuses are draft, active and retired. Verification
outcomes belong to Runs and evidence, not authored `verification_state` on Tests.
Verification method belongs to linked Tests, not a separate Requirement field.

Requirement Types: Functional, Performance, Interface, Design Criteria, Environmental,
Operational, Safety, Compliance, Quality, Reliability, Security, Physical, Human Factors,
Maintainability, Mission, Stakeholder, Software, Hardware, Derived. `Derived` is a
classification independent of a recorded `derives` relationship.

Test methods: test, analysis, inspection, demonstration, modeling, review. A method in
this taxonomy does not establish that a controlled ECSS edition accepts it as a primary
verification method; preserve the project's classification and explain any mapping.

Risk severity: low, medium, high, critical. Likelihood: rare, unlikely, possible, likely,
almost_certain. Analysis-specific hazards, FMEA rows, fault tree nodes, DALs, safety
arguments and action trackers are output artifacts, not additional exchange Item Types.
Do not invent a stored risk matrix or multiply ordinal scale codes.

## Fixed Relationship Types

| Key | Source → target | Meaning and constraints |
|---|---|---|
| contains | System → System | Container to contained System; no hierarchy cycles |
| derives | Requirement → Requirement | Parent/source to derived child; no hierarchy cycles |
| allocated_to | Requirement → System | Responsibility allocation |
| satisfied_by | Requirement → System | Recorded satisfaction claim |
| interface | System ↔ System | One relationship per unordered pair; name and exchange fields |
| verifies | Test → Requirement | Verification scope, not a passing result |
| includes_test | Test Plan → Test | Ordered slot with position and optional label; repeated Tests allowed |
| identifies | Requirement or System → Risk | Risk context |
| mitigated_by | Risk → Requirement or System | Mitigation claim |
| has_property | System → Property | Quantitative system attribute |
| constrains | Requirement → Property | Operator and literal limit |
| depends_on | Property → Property | Derived solely from formula references |

An Interface is a relationship, never an Item. Its fields are kind (electrical,
mechanical, thermal, software, fluid, other), direction (bidirectional, source_to_target,
target_to_source), exchanged_item, description, and linked requirement_ids. Source
protocol details may be preserved in descriptions, notes, controlled documents or
proposed custom fields; do not create Port or Message Item Types.

A Property is a scalar quantity with an explicit unit, or count/ratio
when dimensionless. Quantitative budgets use Properties and supported relationships.
Expressions remain strings. This toolkit preserves them; it does not evaluate formulas
or generate depends_on edges without inspected dependencies.

## Local exchange representation

Read `schemas/model.schema.json` through `arc://schema/model`. Top level contains
schema_version `1.0`, items, relationships, optional metadata. Each local record has
id, type, fields; Items have name, relationships have source/target. Optional import_id
retains the source identity. `metadata.source`, `original_statement`, `source_fields`,
and `imported_fields` retain provenance. These are artifact metadata, not new core fields.
Custom fields are separate proposals; their existence does not approve a model definition.

Validate before comparing or tracing models. Validation establishes exchange shape,
fixed endpoints, uniqueness and cycles; it does not establish permissions, complete
trace coverage, semantic satisfaction, formula correctness, or evidence acceptance.
Units and constraint-limit strings are preserved for engineering review; this validator
does not convert units or prove that a literal has the Property's dimension. A depends_on
edge needs supplied derivation provenance, but that marker is a claim, not verified
expression parsing. Do not treat exchange validity as acceptance by an external application.
