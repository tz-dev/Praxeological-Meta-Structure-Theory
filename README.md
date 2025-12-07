# Praxeological Meta-Structure (PMS)

**Praxeological Meta-Structure (PMS)** is a generative operator framework for modelling praxis, asymmetry, development and self-binding.

It defines eleven irreducible meta-axioms (Δ–Ψ) and shows how complex structures such as **Awareness, Coherence, Responsibility, Action and Dignity-in-Practice** arise from **operator compositions**.

- Structural, not psychological  
- Non-clinical, non-diagnostic  
- Designed for theory, systems thinking and AI governance / architecture

---

## Repository contents

```text
├── examples/                         # (Reserved) Examples of PMS-based analyses or code
├── img/
│   ├── figure_01.png                 # Figures used in the paper / model spec
│   ├── figure_02.png
│   ├── figure_03.png
│   ├── figure_04.png
│   └── figure_05.png
├── model/
│   ├── Model Specification.html      # Human-readable PMS model specification
│   ├── Model Specification.pdf       # PDF version of the specification
│   └── PMS.yaml                      # Canonical PMS model file (schema_version: "PMS_1.1")
├── Praxeological Meta-Structure Theory.html  # HTML export of the theoretical paper
├── Praxeological Meta-Structure Theory.md    # Markdown export of the theoretical paper
├── Towards a Praxeological Meta-Structure Theory.pdf  # Main theoretical paper (PDF)
└── README.md                         # This file
````

### Core artefacts

* **Theoretical paper**

  * `Towards a Praxeological Meta-Structure Theory.pdf`
    Conceptual foundation of PMS: meta-axioms, operator grammar, relation to praxis, asymmetry and development.

* **Model specification (human-readable)**

  * `model/Model Specification.html`
  * `model/Model Specification.pdf`
    Technical walkthrough of the PMS YAML: schema_meta, meta-axioms Δ–Ψ, derived structures (A, C, R, E, D, IA-patterns, self-model), AI interface and guardrails.

* **Canonical YAML model**

  * `model/PMS.yaml`
    Machine-readable specification (schema_version `PMS_1.1`), including:

    * `schema_meta` (model name, status, intended use, normative position, dignity and tragedy clauses)
    * `core_principles`
    * `pms_model_reference` (Δ–Ψ, layers, dependency table)
    * `derived_structures` (A, C, R, E, D, self-model, IA-patterns)
    * `example_operator_chains`
    * `ai_interface_pms` (welcome text, modes, guardrails, suggested questions)

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

## Getting started

### 1. For readers (theory & practice)

If you’re primarily interested in the **theory**:

1. Start with
   `Towards a Praxeological Meta-Structure Theory.pdf`
2. Optionally, use
   `Praxeological Meta-Structure Theory.md` or `.html`
   for easier quoting or in-text search.
3. For the formalisation details, read
   `model/Model Specification.pdf` or `.html`.

If you’re interested in the **technical model**:

1. Open `model/Model Specification.pdf`
   for a narrative explanation of all YAML blocks.
2. Then inspect `model/PMS.yaml` directly
   to see the canonical schema and operator definitions.

---

### 2. For developers / AI researchers

The YAML file is designed to be consumed directly by software and LLM-based agents.

#### Load PMS as a structural governance layer

Typical workflow:

1. **Load the YAML**

   ```python
   import yaml

   with open("model/PMS.yaml", "r", encoding="utf-8") as f:
       pms = yaml.safe_load(f)
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

> After loading the YAML, parse it and activate `ai_interface_pms`.
> Then:
>
> 1. Output the `welcome_message` to the user.
> 2. Use the declared `modes`, `guardrails` and `suggested_questions`
>    whenever you perform PMS-related reasoning.

This keeps LLM behaviour aligned with the **intended structural scope** of the model.

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

The `examples/` directory is reserved for code or case-style examples that demonstrate these uses. (Content may be added in future revisions.)

---

## Citation

When referencing the **Praxeological Meta-Structure (PMS)**, please cite both the theoretical paper and the model specification:

**Primary reference**

> T. Zöller (2025): *Towards a Praxeological Meta-Structure Theory.*

**Technical reference**

> *PMS.yaml – Axiomatic Operator Schema*
> YAML Specification and Model Definition.

---

## License

Unless otherwise stated on the distribution page, the YAML file and this model specification are released under a:

**Creative Commons Attribution–NonCommercial–ShareAlike (CC BY-NC-SA)** license.

* ✅ Free to use for research, teaching and non-commercial applications
* ⚠️ Commercial use requires explicit permission
* 🔁 Derivative works must attribute the original author and share under the same license

Please check the repository description or accompanying notices for any updated licensing information.
