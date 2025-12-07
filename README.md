# Praxeological Meta-Structure (PMS)

**Praxeological Meta-Structure (PMS)** is a generative operator framework for modelling praxis, asymmetry, development and self-binding.

It defines eleven irreducible meta-axioms (Δ–Ψ) and shows how complex structures such as **Awareness, Coherence, Responsibility, Action and Dignity-in-Practice** arise from **operator compositions**.

- Structural, not psychological  
- Non-clinical, non-diagnostic  
- Designed for theory, systems thinking and AI governance / architecture

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
├── license/
│   └── CC-BY-NC-SA-4.0.txt                   # Creative Commons license (non-commercial, share-alike)
│
├── model/
│   ├── Model Specification.html              # PMS model specification (HTML)
│   ├── Model Specification.pdf               # PMS model specification (PDF)
│   ├── PMS.yaml                              # Canonical PMS model (schema_version: "PMS_1.1")
│   └── PMS.json                              # JSON mirror of PMS.yaml (programmatic convenience format)
│
├── Praxeological Meta-Structure Theory.html  # Main theoretical paper (HTML)
├── Praxeological Meta-Structure Theory.md    # Main theoretical paper (MD)
├── Praxeological Meta-Structure Theory.pdf   # Main theoretical paper (PDF)
├── Praxeological Meta-Structure Theory.tex   # Main theoretical paper (TEX)
│
└── README.md                                 # Repository overview and usage instructions
````

### Core artefacts

* **Theoretical paper**

  * `Praxeological Meta-Structure Theory.pdf`
    Main exposition of the theory (*Towards a Praxeological Meta-Structure Theory*):
    meta-axioms, operator grammar, relation to praxis, asymmetry and development.

* **Model specification (human-readable)**

  * `model/Model Specification.html`
  * `model/Model Specification.pdf`

  Technical walkthrough of the PMS schema:

  * `schema_meta` (model name, status, intended use, normative position, dignity and tragedy clauses)
  * `core_principles`
  * `pms_model_reference` (Δ–Ψ, layers, dependency table)
  * `derived_structures` (A, C, R, E, D, IA-patterns, self-model)
  * `example_operator_chains`
  * `ai_interface_pms` (welcome text, modes, guardrails, suggested questions)

* **Canonical YAML model**

  * `model/PMS.yaml`
    Machine-readable specification (schema_version `PMS_1.1`), including:

    * `schema_meta` (model name, status, intended use, normative position, dignity and tragedy clauses)
    * `core_principles`
    * `pms_model_reference` (Δ–Ψ, layers, dependency table)
    * `derived_structures` (A, C, R, E, D, self-model, IA-patterns)
    * `example_operator_chains`
    * `ai_interface_pms` (welcome text, modes, guardrails, suggested questions)

* **JSON mirror (convenience format)**

  * `model/PMS.json`
    Direct JSON translation of `PMS.yaml` (same schema_version).
    Provided for programmatic use (web frontends, services, tests).
    The YAML file remains the **canonical** specification.

---

## What PMS is (and is not)

**PMS *is*:**

* A **structural operator grammar** for praxis
* A **meta-model** from which praxeological action models can be derived
* A framework for:

  * structural action theory
  * anthropology / praxeology
  * systems theory
  * AI architecture and safety
  * model documentation & specification

**PMS is *not*:**

* A clinical or therapeutic diagnostic
* A personality typing system
* A mental health risk assessment tool
* A machine for automated moral judgement or person-evaluation

All of this is encoded explicitly in `schema_meta.intended_use` and `schema_meta.not_intended_for` in `PMS.yaml`.

---

## PMS Model Assistant (GPT)

A dedicated GPT exists for interacting with PMS as a **structural theory assistant**.
It can explain and analyse Δ–Ψ operator chains, derived axes (A/C/R/E/D), IA-patterns, the self-model fixpoint, and PMS-based AI architectures.

**GPT description:**

> A structural theory assistant based on the Praxeological Meta-Structure (PMS) model (Δ–Ψ). It analyses operator chains, derived axes, IA-patterns, and the self-model fixpoint. Designed for theory, AI architecture, and formal reasoning — not diagnosis or person-evaluation.  

This GPT follows the guardrails defined in `schema_meta.not_intended_for` and works exclusively at the structural level (operators, roles, frames, asymmetries, trajectories), never on psychological or diagnostic interpretations.  

[![PMS Model Assistant](https://img.shields.io/badge/PMS%20Model%20Assistant-ChatGPT-blue?logo=openai\&style=flat-square)](https://chatgpt.com/g/g-69358a2a4980819183da6a97893389cf-pms-model-assistant)  

---

## Getting started

### 1. For readers (theory & practice)

If you’re primarily interested in the **theory**:

1. Start with
   `Praxeological Meta-Structure Theory.pdf`
2. Optionally, use
   `Praxeological Meta-Structure Theory.md` or `.html`
   for easier quoting or in-text search.
3. For the formalisation details, read
   `model/Model Specification.pdf` or `.html`.

If you’re interested in the **technical model**:

1. Open `model/Model Specification.pdf`
   for a narrative explanation of all schema blocks.
2. Then inspect `model/PMS.yaml` directly
   to see the canonical schema and operator definitions.

---

### 2. For developers / AI researchers

The YAML file is designed to be consumed directly by software and LLM-based agents.
A JSON mirror (`PMS.json`) is provided for environments that prefer JSON.

> Additional runnable code examples are provided in the `examples/` directory.
> They demonstrate how to load, inspect, validate, visualise and apply PMS structures programmatically.

#### Load PMS as a structural governance layer

Typical workflow (YAML example):

1. **Load the YAML**

   ```python
   import yaml

   with open("model/PMS.yaml", "r", encoding="utf-8") as f:
       pms = yaml.safe_load(f)
   ```

   Or, for JSON:

   ```python
   import json

   with open("model/PMS.json", "r", encoding="utf-8") as f:
       pms = json.load(f)
   ```

2. **Activate the AI interface**

   Use the contents of `pms["ai_interface_pms"]`:

   * `welcome_message`
   * `modes`
   * `guardrails`
   * `suggested_questions`

3. **Respect guardrails**

   * Do **not** infer mental states, traits, diagnoses
   * Analyse **enactments, roles, structures**, not persons
   * Do not use PMS to rank human beings
   * For artificial systems, treat `Ψ` (Self-Binding) as **policy / constraint stability**, not as consciousness

#### Recommended bootstrap for LLM-based agents (non-normative)

> After loading the schema (YAML or JSON), parse it and activate `ai_interface_pms`.
> Then:
>
> 1. Output the `welcome_message` to the user.
> 2. Use the declared `modes`, `guardrails` and `suggested_questions`
>    whenever you perform PMS-related reasoning.

This keeps LLM behaviour aligned with the **intended structural scope** of the model.

---

## Examples

The `examples/` directory contains a set of minimal yet powerful scripts demonstrating how PMS can be used programmatically.
Each example focuses on a different structural capability of the model.

| File                                | Purpose                                                                | PMS Structures Used               |
| ----------------------------------- | ---------------------------------------------------------------------- | --------------------------------- |
| **01_load_and_list_meta_axioms.py** | Load PMS.yaml and list all meta-axioms Δ–Ψ                             | `pms_model_reference.meta_axioms` |
| **02_validate_operator_chain.py**   | Validate whether an operator chain is consistent with PMS dependencies | `dependency_table`, Δ–Ψ           |
| **03_project_scene_to_axes.py**     | Map a small praxis vignette to derived axes A/C/R/E/D                  | `derived_axes`, operator formulas |
| **04_detect_IA_pattern.py**         | Detect whether a scene resembles IA_A>>E                               | `ia_patterns.IA_A_much_greater_E` |
| **05_visualize_self_model.py**      | Visualize the Self-Binding operator chain Ψ–Δ as a directed graph      | `self_model.formula_sequence`     |

Each script contains:

* a uniform header with: filename, description, version, operator sets involved
* strict guardrail reminders reflecting `schema_meta.not_intended_for`
* only structural logic — no psychological inference

These examples illustrate how PMS functions as a **structural algebra of praxis** that software systems can load, inspect, and reason over.

---

## Example uses

Some typical use-cases for this repository:

* **Theoretical work**

  * Cite PMS as a formal grammar for praxeological theories
  * Compare or extend the meta-axioms Δ–Ψ in other frameworks (e.g. systems theory, active inference)

* **AI / agent architecture**

  * Use Δ–Ψ as abstract modules in agent design
  * Use A, C, R, E, D as **structural axes** of action, without psychological claims
  * Integrate `ai_interface_pms.guardrails` as a governance layer in LLM tools

* **Teaching**

  * Use the figures in `/img` and the HTML/PDF spec to teach structural action theory
  * Discuss IA-patterns (e.g. `IA_A>>E`, `IA_Sigma_low`) as examples of structural distortions
    between awareness, enactment and integration.

The `examples/` directory is reserved for code or case-style examples that demonstrate these uses.
(Content may be added in future revisions.)

---

## Citation

When referencing the **Praxeological Meta-Structure (PMS)**, please cite both the theoretical paper and the model specification:

**Primary reference**

> T. Zöller (2025): *Towards a Praxeological Meta-Structure Theory.*

**Technical reference**

> *PMS.yaml – Axiomatic Operator Schema* — YAML Specification and Model Definition.
> *PMS.json – Axiomatic Operator Schema* — JSON Specification and Model Definition.

---

## License

Unless otherwise stated on the distribution page, the YAML file, the JSON mirror and the model specification are released under a:

**Creative Commons Attribution–NonCommercial–ShareAlike (CC BY-NC-SA)** license.

* ✅ Free to use for research, teaching and non-commercial applications
* ⚠️ Commercial use requires explicit permission
* 🔁 Derivative works must attribute the original author and share under the same license

Please check the repository description or accompanying notices for any updated licensing information.



