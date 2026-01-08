# Global Overview: PMS Layers, Focus, Reach, and Position in the Stack

This document provides a single, navigable map of the PMS ecosystem: what each repository is for, what it ships, how it relates to the canonical PMS grammar, and where it sits in the overall stack.

If you are new to PMS, the key idea is simple:

* **PMS** defines a **canonical operator grammar** (Δ–Ψ) for structural praxeological analysis.
* The **domain repositories** (ANTICIPATION, CRITIQUE, CONFLICT, EDEN, SEX, LOGIC) apply that grammar to specific regimes without modifying it.
* **MIP / IA** is a **downstream governance layer**: it evaluates whether an analysis artifact is responsible, scoped, and misuse-resistant.
* **PMS–QC** is a **specialized bridge**: a structural mapping layer for quantum computing (not governance, not moral discourse).

This overview is designed to prevent two common confusions:

1. Mixing up **PMS as a theory object** (“PMS Base”) with **PMS as a repository** (“PMS Theory / Repo”).
2. Treating domain applications as if they were allowed to redefine operators or dependencies (they are not).

---

## 1) Macro Overview Table (Stack-Level) — with Primary Deliverables

| Model / Repo              | Primary Deliverables                                                                                                                                                 | Artifact Type                                   | Stack Position                                          | Central Question                                                                    | Structural Focus                                                                                                                                                                                                                                                        | Operators Under Load (typical)                                    | Typical Transition / Docking                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **PMS (Theory / Repo)**   | **Paper (MD/HTML/PDF/TEX)** · **Canonical YAML (`PMS.yaml`)** · **Spec (HTML/PDF)** · **JSON mirror** · **Diagrams (Mermaid/PlantUML)** · **Code examples (Python)** | **Canonical Core** (source-of-truth repository) | **Root / Source of Truth**                              | *What is PMS exactly—formally and implementably?*                                   | Publishes the operator grammar **Δ–Ψ**, dependency hygiene, derived axes (**A/C/R/E/D**), IA patterns, self-model, and explicit guardrails (“what PMS is not”).                                                                                                         | all (Δ–Ψ)                                                         | → every downstream repo docks to this grammar and its guardrails                      |
| **PMS (Base)**            | **(Conceptual layer, not a separate repo deliverable)** · “Δ–Ψ as an axiomatic object”                                                                               | **Axiomatic layer**                             | **Axiomatic**                                           | *What is praxis structurally?*                                                      | The minimal, irreducible operator set and composition rules; negative space: what is not modeled (values, persons, diagnostics).                                                                                                                                        | all (Δ–Ψ)                                                         | → all applications inherit constraints from here                                      |
| **PMS–ANTICIPATION**      | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)** · **Diagrams (if present)**                                                                                    | Domain Layer                                    | **Upstream**                                            | *How does praxis remain viable before event and before binding?*                    | “Future as a structural field” (not prediction): carrying **non-event (Λ)** under **temporality (Θ)** and **asymmetry (Ω)** while preserving **distance (Χ)** and **self-binding (Ψ)** as restraint.                                                                    | Λ Θ Ω Χ Ψ                                                         | ANTICIPATION → CRITIQUE (openness becomes interruptible)                              |
| **PMS–CRITIQUE**          | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)** · **Addon spec (`PMS-CRITIQUE.yaml`)** · **Model spec (HTML/PDF)**                                             | Domain Layer + Application Profile              | **Transition / Hinge**                                  | *When does irritation become interruptible—and when does it drift?*                 | Critique as **χ-stabilized interruption**: how mismatch (Δ) becomes interruptible, how critique mutates (reaction, judgment, narrative reset, silence, exposure), and what is required for correction (**Φ/Σ/Ψ**) under **Ω/Θ** and optional publicness overlay **P**.  | Δ □ Χ Φ Σ Ψ (plus Λ/Α/Ω/Θ under P)                                | CRITIQUE → CONFLICT (integration collisions)                                          |
| **PMS–CONFLICT**          | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)** · *(optional: addon profile YAML later)*                                                                       | Domain Layer                                    | **Major Knot**                                          | *What happens when bindings become structurally incompatible?*                      | Conflict as **stabilized incompatibility of praxis trajectories**: competing **Σ/Ψ** under shared **Θ**, with **Ω** cost gradients and **Χ** becoming costly or unavailable. Not “resolution,” but legibility of tragic collision and attractor formation.              | Σ Ψ Ω Θ Χ                                                         | CONFLICT → tragedy / downstream (governance, evaluation, institutionalization)        |
| **PMS–EDEN**              | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)** · **Diagrams (PNG)**                                                                                           | Domain Layer                                    | **Drift / Cross-axis**                                  | *How does praxis drift into comparison and pseudo-symmetry without “fault”?*        | Drift trace: frame drift (□) into value/comparison relation, asymmetry becoming status-legible (Ω), **non-event residue (Λ)** and **attractors (Α)** stabilizing pseudo-symmetry while **Σ/Ψ** carriage fails under **Θ**.                                              | Δ □ Ω Λ Α Θ (Φ/Σ/Ψ as exit corridors)                             | runs in parallel; often parasitizes CRITIQUE/CONFLICT dynamics                        |
| **PMS–SEX**               | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)** · *(optional: diagrams)*                                                                                       | Domain Layer                                    | **Intimacy / High Ω**                                   | *How do impulse and repetition bind under maximal asymmetry and exposure?*          | Sexual praxis as a consequence system: scripts (**Α**), cost gradients (**Ω**), trajectory effects (**Θ**), non-events (**Λ**) as steering, and binding thresholds (**Ψ**) under the decisive limiter **Χ** (stop-capability).                                          | ∇ Ω Θ Λ Α Ψ Χ                                                     | cross-couples heavily into CONFLICT (binding desync, exit realism)                    |
| **PMS–LOGIC**             | **Paper (MD/HTML/PDF)** · **Example suite (MD/HTML)**                                                                                                                | Domain Layer                                    | **Boundary / Limit Case**                               | *What remains when justification reaches its structural limit?*                     | Post-moral effects: responsibility as attributable residue under **Ω/Θ/Λ/Ψ** without generating norms. Logic is treated as indispensable but bounded by non-closure (Λ).                                                                                                | Λ Ω Θ Ψ (Σ/Φ as boundary probes)                                  | LOGIC → MIP (from description to governance/evaluation)                               |
| **PMS–QC**                | **Paper (MD/HTML/PDF)** · **Base spec (`PMS-QC.yaml`)** · **Optional ext (`PMS-QC-EXT.yaml`)** · *(potential code later)*                                            | Domain Bridge / Exploratory Spec Layer          | **Specialized Application (not downstream governance)** | *How can PMS function as a structural/context layer for quantum computing?*         | Structural correspondence mapping: **□** as workspace/subspace boundary, **Φ** as basis/context change, **Χ** as isolation discipline, **Σ** as commit boundary, **Ω** as control/measurement asymmetry, **Θ** as scheduling/iteration—without replacing QC formalisms. | □ Φ Χ Σ Ω Θ (Δ/Λ/Α/Ψ as motifs)                                   | PMS → QC mapping; QC-EXT remains optional and non-normative                           |
| **MIP / IA (MIPractice)** | **Canonical YAML (case + model reference)** · **Addon YAML (AH Precision)** · **Human specs (HTML/PDF)** · **Examples (YAML/HTML/PDF)** · **Template (HTML)**        | Downstream Application Spec                     | **Downstream (Evaluation / Governance)**                | *How do we apply structural analysis responsibly and harden the analysis artifact?* | Second-order evaluation: ACRPD profiling, IA box, trajectory tracking, zones/guardrails, misuse resistance, and meta-analysis of the analysis artifact (AH). Uses PMS outputs; introduces no new PMS operators.                                                         | consumes PMS-derived axes + constraints (A/C/R/E/D; Ω/Θ/Χ/Ψ etc.) | Application / audit / governance; feeds back into better upstream analysis discipline |

---

## 2) Practical Stack Map (for navigation and repo management)

The ecosystem is easiest to understand as **three non-mixing strata**:

### A) Canonical Grammar (one source of truth)

**PMS (Theory / Repo)** is the only place where:

* the operator set (Δ–Ψ) is defined,
* dependencies are canonical,
* derived axes (A/C/R/E/D) and guardrails are specified as a stable base.

If a question is about “what an operator means,” “which dependencies are valid,” or “what PMS explicitly does not model,” the canonical answer lives here.

### B) Domain Layers (operator-strict applications)

These repositories produce **domain legibility** without turning into advice, therapy, discourse ethics, or enforcement.

* **ANTICIPATION** (before event / before binding)
* **CRITIQUE** (interruptibility before integration; drift under load)
* **CONFLICT** (after binding; incompatibility under Θ/Ω; tragic legibility)
* **EDEN** (comparison drift / pseudo-symmetry regimes)
* **SEX** (intimacy + scripts + binding thresholds)
* **LOGIC** (limits of justification; post-moral residue fields)
* **QC** (specialized domain bridge; structural mapping, not governance)

Each domain layer is a constrained application: it uses PMS “as specified,” adds no new operators, and keeps claims reversible and scene-bound.

### C) Downstream Governance / Evaluation (artifact responsibility)

**MIP / IA** evaluates whether a produced analysis is:

* scope-clean (no drift into diagnosis or person-typing),
* misuse-resistant (explicit guardrails and “red zone” awareness),
* structurally grounded (assumptions and limits stated),
* publishable without coercive drift.

It does not replace PMS and does not compete with the domain layers—it hardens their outputs.

---

## 3) Why the “Primary Deliverables” column matters (operationally)

It prevents two recurring failure modes:

1. **Spec drift**
   When a domain repository quietly starts acting like a grammar repository (redefining operators, smuggling dependencies, inventing “new primitives”).
   The deliverables column makes “where definitions live” visible at a glance.

2. **Tooling confusion**
   People often mix “paper repositories” with “schema/spec repositories.”
   The deliverables column clarifies which repos ship YAML contracts, templates, code, or only papers and examples—so integrations stay clean.

---

## 4) Minimal repo discipline checklist (optional but useful)

A lightweight standard that keeps the ecosystem coherent:

* Every repo states: **“Depends on PMS; does not modify PMS operators.”**
* Every repo lists its deliverables explicitly (paper formats, YAML contracts, examples, specs).
* Every domain repo keeps:

  * the guardrail gate (distance + reversibility + dignity-in-practice),
  * a “What this is not” section,
  * and avoids person-typing, diagnosis, or enforcement language.
* Only **PMS (Theory / Repo)** contains canonical operator definitions and dependency tables.

---

## Conclusion (optional)

The PMS ecosystem is deliberately designed for **density over expansion**:

* **PMS** stabilizes the grammar and its negative space (what is not modeled).
* Domain layers carve out a small set of **high-leverage regimes** where structural drift and viability are repeatedly misread in moral or psychological terms.
* **MIP / IA** ensures that applying these models does not collapse into coercion, verdict production, or irreversible exposure.

If you want a single rule of thumb:

> **PMS defines the grammar.
> Domain layers show how the grammar behaves under specific load regimes.
> MIP / IA hardens the resulting analysis artifacts for responsible use.**
