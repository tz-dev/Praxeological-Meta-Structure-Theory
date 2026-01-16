# Praxeological Meta-Structure (PMS)

The **Praxeological Meta-Structure (PMS)** is a generative operator framework for formally modelling **praxis, asymmetry, development, and self-binding** — a structural grammar of praxis.

It defines eleven irreducible meta-axioms (Δ–Ψ) and specifies how complex structures such as **Awareness, Coherence, Responsibility, Action, and Dignity-in-Practice** arise from ordered operator compositions.

Profile:

* structural, not psychological  
* non-clinical, non-diagnostic  
* non-normative, non-moralistic  
* designed for theory, systems thinking, and AI architecture / governance  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18188141.svg)](https://doi.org/10.5281/zenodo.18188141)

---

## What PMS is — and is not

| PMS is | PMS is not |
| ------ | ---------- |
| an **operator grammar of praxis** | a clinical or therapeutic diagnostic |
| a **meta-model** from which praxeological action models can be derived | a personality typing system |
| a framework for structural action theory | a mental health risk assessment tool |
| a framework for anthropology / praxeology | a machine for automated moral judgement or person-evaluation |
| a framework for systems theory |  |
| a framework for AI architecture and safety |  |
| a framework for model documentation and specification |  |

These boundaries are explicitly encoded in:

* `schema_meta.intended_use`  
* `schema_meta.not_intended_for`  

in the canonical file: `model/PMS.yaml`.

---

## Entry Condition and Validity Gate

Any **application** of PMS (not critique or rejection of PMS) presupposes:

* **Χ (Distance):** reflective distance; no fusion into verdict, urgency, enforcement, or person-level attribution.  
* **Reversibility:** all readings are scene-bound, revisable, and non-final.  
* **D (Dignity-in-Practice):** enacted restraint under asymmetry; no shaming, ranking, humiliation, or ontological evaluation of persons or groups.

Applications that suspend these conditions are **formally invalid as PMS applications**, even if PMS terminology is used.

---

## Dignity-in-Practice (D) — Structural, not ontological

Dignity-in-Practice is **not** a claim about inherent, metaphysical, or legal human worth.  
It is a **praxeological constraint** on how asymmetry (Ω) is handled in action.

D refers to:

* restraint under asymmetry,  
* protection of exposure and vulnerability,  
* refusal to instrumentalize asymmetry for humiliation, ranking, or degradation.

D does **not** refer to:

* human rights doctrine,  
* moral status,  
* metaphysical or ontological dignity,  
* ranking of beings.

In PMS, dignity is not something one *has*;  
it is something that is **enacted—or violated—through praxis**.

This keeps PMS:

* non-moralistic,  
* non-metaphysical,  
* strictly structural.

---

## Self-Binding Clause

Any application of PMS is itself subject to PMS.

Analyses that suspend:

* Distance (Χ),
* Self-binding discipline (Ψ),
* or Dignity-in-Practice (D),

in order to enforce truth, clarity, authority, resolution, or action are **structurally invalid** as PMS applications.

PMS can be misunderstood, misapplied, or rejected.  
It can only be structurally betrayed by adherents who keep its language while abandoning its self-binding requirements.

---

## The 11 Meta-Axioms (Δ–Ψ)

| Operator | Name                | Short definition                                                                              | Depends on | Examples (selection)                                                                                                      |
| :------: | ------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------- |
|     Δ    | Difference          | Minimal structural distinction enabling any differentiation.                                  | –          | self vs. other; inside vs. outside a role; allowed vs. forbidden action                                                   |
|     ∇    | Impulse             | Directional tension/drive arising from difference.                                            | Δ          | desire triggered by perceived lack; urge to correct an imbalance; move toward/away from a signal                          |
|     □    | Frame               | Contextual structure that constrains and shapes impulses.                                     | Δ, ∇       | institutional rules; family role expectations; conversation context                                                       |
|     Λ    | Non-Event           | Structured absence: meaningful failure or delay of an expected occurrence within a frame.     | □          | a promised reply that never arrives; silence where a response is expected; postponed decision that reshapes the situation |
|     Α    | Attractor           | Recurrent pattern/stabilization built from repeated framed interactions and non-events.       | Δ, ∇, □, Λ | repeated avoidance of conflict; reliable punctuality; stable institutional routine                                        |
|     Ω    | Asymmetry           | Structural imbalance establishing directionality of power, exposure, capacity, or obligation. | Α          | parent–child relation; mentor–apprentice dynamics; leader–follower position                                               |
|     Θ    | Temporality         | Temporal structuring enabling trajectories, commitments, and development.                     | Ω, Α       | long-term responsibility; accumulating consequences; ongoing development of a role                                        |
|     Φ    | Recontextualization | Transformation by embedding an existing structure into a new frame.                           | Θ, Ω, □    | reframing conflict as misunderstanding; seeing failure as a learning step; renegotiating role expectations                |
|     Χ    | Distance            | Reflective withdrawal that attenuates immediate impulses and patterns.                        | Φ, Θ, □    | pausing before reacting; stepping out of a role to reflect; deliberately suspending a habitual script                     |
|     Σ    | Integration         | Synthesis of disparate/conflicting elements into a coherent whole.                            | Χ, Φ       | aligning motives and roles; integrating emotional impulse and norm; forming a coherent action plan                        |
|     Ψ    | Self-Binding        | Identity formation through commitment to integrated structures over time.                     | Σ, Θ, Χ    | holding oneself accountable; owning a caregiving role; long-term identity commitments and promises                        |

Dependency chain:

```
Δ → ∇ → □ → Λ → Α → Ω → Θ → Φ → Χ → Σ → Ψ
```

---

## Repository contents

```text
├── examples/                                 # Runnable PMS example scripts (see README table)
│   ├── 01_load_and_list_meta_axioms.py       # Load PMS.yaml and list Δ–Ψ
│   ├── 02_validate_operator_chain.py         # Validate operator chains using dependency rules
│   ├── 03_project_scene_to_axes.py           # Map a praxis vignette to A/C/R/E/D
│   ├── 04_detect_IA_pattern.py               # Detect IA_A>>E structural pattern
│   └── 05_visualize_self_model.py            # Visualize the self-model operator chain (Ψ…Δ)
│
├── img/                                      # Figures used in paper
│   ├── figure_01.png
│   ├── figure_02.png
│   ├── figure_03.png
│   ├── figure_04.png
│   └── figure_05.png
│
├── doc/
│   ├── Global Overview - PMS Layers, Focus, Reach, and Position in the Stack.md
│   └── Global Overview - PMS Layers, Focus, Reach, and Position in the Stack.html
│
├── model/
│   ├── Model Specification.html              # PMS model specification (HTML)
│   ├── Model Specification.pdf               # PMS model specification (PDF)
│   ├── PMS.yaml                              # Canonical PMS model (schema_version: "PMS_1.1")
│   ├── PMS.json                              # JSON mirror of PMS.yaml (programmatic convenience format)
│   ├── PMS_mermaid_chain.md                  # Mermaid operator-chain diagram (Δ→∇→…→Ψ)
│   ├── PMS_mermaid_axes.md                   # Mermaid diagram mapping Δ–Ψ to A/C/R/E/D
│   └── PMS_plantuml_operators.uml            # PlantUML class diagram of Δ–Ψ operator hierarchy
│
├── LICENSE-CC-BY-4.0                         # CC BY 4.0 (for model content & docs)
├── MIT-LICENSE                               # MIT License (for example code/tools)
│
├── Praxeological Meta-Structure Theory.html  # Main theoretical paper (HTML)
├── Praxeological Meta-Structure Theory.md    # Main theoretical paper (MD)
├── Praxeological Meta-Structure Theory.pdf   # Main theoretical paper (PDF)
├── Praxeological Meta-Structure Theory.tex   # Main theoretical paper (TEX)
│
└── README.md                                 # Repository overview and usage instructions
```

---

## Core artefacts

### Theoretical paper

* `Praxeological Meta-Structure Theory.pdf`
  Main exposition: meta-axioms, operator grammar, praxis, asymmetry, development.

### Model specification

* `model/Model Specification.html`
* `model/Model Specification.pdf`
  Narrative explanation of all schema blocks.

### Canonical model

* `model/PMS.yaml`
  Canonical machine-readable schema (version `PMS_1.1`).

### JSON mirror

* `model/PMS.json`
  Programmatic convenience mirror of the YAML file.

### Diagrams

* Mermaid and PlantUML files in `model/` visualize operators and derived axes.

---

## Derived Structures

From the operator grammar emerge:

* Derived axes:

  * Awareness (A)
  * Coherence (C)
  * Responsibility (R)
  * Action (E)
  * Dignity-in-Practice (D)

* Self-model fixpoint:

  * `Self = Ψ ∘ Σ ∘ Χ ∘ Φ ∘ Θ ∘ Ω ∘ Α ∘ Λ ∘ □ ∘ ∇ ∘ Δ`

* IA-patterns (e.g. `IA_A>>E`, `IA_Sigma_low`) describing structural distortions between axes.

All of these are defined canonically in `model/PMS.yaml`.

For extended case-style illustrations and cross-domain pattern cartography, see
**[PMS–AXIOM](https://github.com/tz-dev/PMS-AXIOM)**.

---

## The PMS Ecosystem and Add-on Suite

PMS defines the canonical grammar.
Other repositories apply it without modifying it.

### Structural strata

1. Canonical grammar

* **PMS (Theory / Repo)**
  Source of truth for operators, dependencies, derived axes, guardrails.

2. Domain layers (operator-strict applications)

* **[PMS–ANTICIPATION](https://github.com/tz-dev/PMS-ANTICIPATION)**
  non-event, futurity, viability, restraint before binding

* **[PMS–CRITIQUE](https://github.com/tz-dev/PMS-CRITIQUE)**
  interruption, irritation, correction, drift, exposure

* **[PMS–CONFLICT](https://github.com/tz-dev/PMS-CONFLICT)**
  incompatible bindings, tragic collision, cost gradients

* **[PMS–EDEN](https://github.com/tz-dev/PMS-EDEN)**
  comparison drift, pseudo-symmetry, status regimes

* **[PMS–SEX](https://github.com/tz-dev/PMS-SEX)**
  impulse, scripts, asymmetry, binding thresholds, stop-capability

* **[PMS–LOGIC](https://github.com/tz-dev/PMS-LOGIC)**
  limits of justification, post-moral residue, non-closure

* **[PMS–QC](https://github.com/tz-dev/PMS-QC)**
  structural mapping for quantum computing (not governance)

These apply PMS to specific regimes without redefining operators.

3. Downstream governance

* **[MIP / IA (Maturity in Practice / Integrity Architecture)](https://github.com/tz-dev/Maturity-in-Practice)**  
  Evaluates whether produced analyses are responsible, scoped, and misuse-resistant.  
  It introduces no new PMS operators.

> Rule of thumb:
> PMS defines the grammar.
> Domain layers show how it behaves under specific load regimes.
> MIP / IA hardens the resulting analysis artifacts.

---

## Getting started

### For readers

* The theoretical argument and motivation for PMS are in
  `Praxeological Meta-Structure Theory.*` (PDF/HTML/MD/TEX).

* A structured walkthrough of the formal model is in
  `model/Model Specification.*`.

* The canonical, machine-readable definition lives in
  `model/PMS.yaml` (with `PMS.json` as a mirror format).

### For developers / AI researchers

PMS is primarily designed to be used as a **structural grammar for AI agents**  
(not just as a library you import).

Typical main use:

* give an AI agent:
  - `model/PMS.yaml` (or `PMS.json`) as its structural grammar,
  - plus the blocks:
    - `ai_interface_pms.welcome_message`
    - `modes`
    - `guardrails`
    - `suggested_questions`

This turns the agent into a **PMS-constrained structural analyst**:
* it reasons in operators (Δ–Ψ),
* projects to A/C/R/E/D,
* respects Distance (Χ), Reversibility, and Dignity-in-Practice (D),
* and avoids diagnosis, person-typing, or enforcement drift.

Programmatic loading (e.g. for agent tooling or validation):

```python
import yaml
with open("model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)
```

Core blocks for agent use:

* `pms["pms_model_reference"]` → operators and dependencies
* `pms["derived_structures"]` → A/C/R/E/D, IA-patterns, self-model
* `pms["ai_interface_pms"]` → welcome text, modes, guardrails

Self-binding (Ψ) in artificial systems means:

* stability of policies and constraints,
* not consciousness or subjectivity.

---

## Examples

There are two distinct ways to use the example material.

### 1) As AI-agent scaffolding (primary use)

The main intended use of PMS is through AI agents that:

* load `PMS.yaml`,
* activate `ai_interface_pms`,
* reason using operators and derived axes.

In this mode:

* the examples serve as **reference patterns** for how PMS reasoning can look,
* not as the primary interface.

For richer, cross-domain case material, see:
**[PMS–AXIOM](https://github.com/tz-dev/PMS-AXIOM)**  
which acts as a cartography of structural closure- and drift-patterns across the stack.

---

### 2) As runnable Python demos

The `examples/` folder contains small scripts that demonstrate:

* how to load the schema,
* validate operator chains,
* project scenes to derived axes,
* detect IA-patterns,
* and visualize the self-model.

Run them locally:

```bash
python examples/01_load_and_list_meta_axioms.py
python examples/02_validate_operator_chain.py
python examples/03_project_scene_to_axes.py
python examples/04_detect_IA_pattern.py
python examples/05_visualize_self_model.py
```

Files:

| File                              | Shows how to…                  |
| --------------------------------- | ------------------------------ |
| `01_load_and_list_meta_axioms.py` | load PMS.yaml and list Δ–Ψ     |
| `02_validate_operator_chain.py`   | validate operator dependencies |
| `03_project_scene_to_axes.py`     | map a scene to A/C/R/E/D       |
| `04_detect_IA_pattern.py`         | detect IA_A>>E                 |
| `05_visualize_self_model.py`      | draw the self-fixpoint chain   |

All examples:

* include guardrail reminders,
* operate structurally (operators, frames, asymmetries),
* never infer mental states or diagnoses.


---

## Links & Resources

*Maturity in Practice* is situated within a broader **praxeological ecosystem** that connects anthropological theory, formal operator models, applied analyses, and executable specifications.

The resources below are organized by **structural role** within that ecosystem.

PMS–AXIOM is part of a broader **praxeological ecosystem** spanning formal operator theory, applied anthropology, governance analysis, and executable specifications.

| Category        | Resource | Description |
| --------------- | -------- | ----------- |
| Model website   | [PMS Theory Site](https://pms-theory.netlify.app) | Canonical PMS theory reference |
| Book websites   | [Maturity in Practice (EN)](https://maturity-in-practice.netlify.app) | *Maturity in Practice* — English edition (praxeological anthropology) |
|                 | [Reife im Vollzug (DE)](https://reife-im-vollzug.netlify.app) | *Reife im Vollzug* — Deutsche Ausgabe |
|                 | [PMS Stack](https://pms-stack.netlify.app) | PMS-STACK reference architecture |
| Amazon          | [Maturity in Practice (EN)](https://www.amazon.com/dp/B0G4XBKNNR) | *Maturity in Practice: A Praxeological Anthropology* — English edition |
|                 | [Reife im Vollzug (DE)](https://www.amazon.de/dp/B0G4SPBDQD) | *Reife im Vollzug: Eine praxeologische Anthropologie* — Deutsche Ausgabe |
|                 | [PMS-STACK](https://www.amazon.com/dp/B0G6G7V38P) | *PMS-STACK — A Praxeological Operating System Architecture* |
| GitHub (papers) | [PMS Theory / Repo](https://github.com/tz-dev/Praxeological-Meta-Structure-Theory) | Canonical PMS grammar, theory & YAML definitions |
|                 | [Maturity-in-Practice](https://github.com/tz-dev/Maturity-in-Practice) | Book sources & applied praxeological anthropology |
|                 | [PMS-QC](https://github.com/tz-dev/PMS-QC) | PMS-QC — Praxeological Meta-Structure for Quantum Computing |
|                 | [PMS-LOGIC](https://github.com/tz-dev/PMS-LOGIC) | PMS-LOGIC — Structural Responsibility, Logical Limits, and Post-Moral Effects |
|                 | [PMS-ANTICIPATION](https://github.com/tz-dev/PMS-ANTICIPATION) | PMS-ANTICIPATION — Structural Conditions, Risks, and Viability of Anticipatory Praxis |
|                 | [PMS-CRITIQUE](https://github.com/tz-dev/PMS-CRITIQUE) | PMS-CRITIQUE — From Irritation to Correction: A Praxeological Grammar of Critique |
|                 | [PMS-EDEN](https://github.com/tz-dev/PMS-EDEN) | PMS-EDEN — Structural Drift from Praxis to Comparison and Reciprocity Loss |
|                 | [PMS-SEX](https://github.com/tz-dev/PMS-SEX) | PMS-SEX — From Impulse to Self-Binding: A Praxeological Grammar of Sexuality |
|                 | [PMS-CONFLICT](https://github.com/tz-dev/PMS-CONFLICT) | PMS-CONFLICT — Conflict as Stabilized Incompatibility: Cost, Binding, and Tragic Non-Integration |
|                 | **[PMS-AXIOM](https://github.com/tz-dev/PMS-AXIOM)** | PMS-AXIOM — Cartography of Classical Closure-Demands Across the PMS Stack |
| Custom GPTs     | [PMS Model Assistant](https://chatgpt.com/g/g-69358a2a4980819183da6a97893389cf-pms-model-assistant) | Interactive PMS.yaml exploration & validation |
|                 | [Maturity in Action](https://chat.openai.com/g/g-693460d3def48191ad08647301645a2e-maturity-in-action-a-praxeological-anthropology) | Applied praxeological anthropology assistant |

---

## Citation

Primary reference:

> T. Zöller (2025): *Towards a Praxeological Meta-Structure Theory.*

Technical reference:

> *PMS.yaml – Axiomatic Operator Schema — YAML Specification and Model Definition.*
> *PMS.json – Axiomatic Operator Schema — JSON Specification and Model Definition.*

---

## License

Dual license:

### Code

MIT License → `MIT-LICENSE`

### Model & docs

Creative Commons Attribution 4.0 → `LICENSE-CC-BY-4.0`

Attribution:

> “T. Zöller – Praxeological Meta-Structure (PMS) Model (Δ–Ψ, PMS.yaml v1.1)”

© 2025 T. Zöller

---

## Contributing

* clarify scope via issue
* maintain compatibility with `PMS.yaml`
* avoid breaking changes without discussion

Extensions are welcome if they:

* keep the structural, non-psychological scope
* respect CC BY 4.0 attribution
