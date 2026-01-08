"""
PMS Example Script 01 – Load and List Meta-Axioms
File: 01_load_and_list_meta_axioms.py

Description:
    Minimal example that loads the Praxeological Meta-Structure (PMS) model
    from the canonical YAML file and prints the list of meta-axioms Δ–Ψ with
    their basic dependency information.

Model:
    - PMS schema_version: PMS_1.1
    - Canonical model file: ../model/PMS.yaml

PMS structures used:
    - pms_model_reference.meta_axioms (Δ–Ψ)

Usage:
    python 01_load_and_list_meta_axioms.py

Dependencies:
    - PyYAML (yaml)

Notes:
    - PMS is a structural, non-psychological meta-model.
    - This script is for theoretical and technical exploration only.
    - Do NOT use PMS for clinical diagnosis, personality typing, mental health
      risk assessment, automated moral judgement or individual person evaluation.
"""

import yaml

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

axioms = pms["pms_model_reference"]["meta_axioms"]

print("Meta-Axioms (Δ–Ψ):")
for ax in axioms:
    print(f"{ax['id']}: {ax['name']}  — depends on {ax['depends_on']}")
