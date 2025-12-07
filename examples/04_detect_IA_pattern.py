"""
PMS Example Script 04 – Detect an IA Pattern (IA_A>>E)
File: 04_detect_IA_pattern.py

Description:
    Demonstrates how to use the PMS IA-pattern definitions to check whether
    a given scene structurally resembles the pattern IA_A>>E
    (Excessive distance between Awareness and Enactment).
    The detection is based solely on the presence of specified operators
    in the scene, not on any psychological or moral evaluation of persons.

Model:
    - PMS schema_version: PMS_1.1
    - Canonical model file: ../model/PMS.yaml

PMS structures used:
    - derived_structures.ia_patterns.IA_A_much_greater_E
        - structural_basis.formula (["Ω", "Α", "Φ"])
        - generative_mechanism / axis_effects (for interpretation, if needed)

Usage:
    python 04_detect_IA_pattern.py

Dependencies:
    - PyYAML (yaml)

Notes:
    - IA-patterns describe structural praxeological constellations, not
      personality types or clinical categories.
    - This script is intended for theoretical, educational and model-testing
      scenarios only.
    - Do NOT use IA-pattern detection as a diagnostic or sanctioning tool
      for real individuals.
"""

import yaml

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

ia = pms["derived_structures"]["ia_patterns"]["IA_A_much_greater_E"]
required_ops = set(ia["structural_basis"]["formula"])

scene = {
    "description": "Person continually evaluates and reframes a problem but never acts.",
    "operators_detected": ["Ω", "Α", "Φ", "Δ", "□", "Θ"]  # contains required Ω, Α, Φ
}

if required_ops.issubset(scene["operators_detected"]):
    print("Scene likely fits IA_A>>E:")
    print("→ Excessive expansion of evaluative space; suppressed enactment (E).")
else:
    print("Scene does not match IA_A>>E.")
