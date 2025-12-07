"""
PMS Example Script 03 – Project a Praxis Scene to Derived Axes
File: 03_project_scene_to_axes.py

Description:
    Shows how to interpret a simple praxis scene in terms of PMS operators
    and then project these operators onto the derived axes
    (Awareness A, Coherence C, Responsibility R, Action E, Dignity D).
    The example remains strictly structural and does not make psychological
    claims about persons.

Model:
    - PMS schema_version: PMS_1.1
    - Canonical model file: ../model/PMS.yaml

PMS structures used:
    - derived_structures.derived_axes (A, C, R, E, D)
    - Optional: pms_model_reference.meta_axioms for operator inspection

Usage:
    python 03_project_scene_to_axes.py

Dependencies:
    - PyYAML (yaml)

Notes:
    - The “scene” is a praxeological vignette, not a diagnosis.
    - Projection onto A/C/R/E/D is structural and approximate, for theory
      and model exploration only.
    - Do NOT use this pattern to assess individuals in clinical, forensic
      or HR contexts.
"""

import yaml

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

axes = pms["derived_structures"]["derived_axes"]

scene = {
    "description": "A colleague notices tension in a meeting but waits before speaking.",
    "operators_detected": ["Δ", "□", "Θ", "Χ"]  # difference, frame, time, distance
}

def infer_axes(ops):
    active = []
    for axis_name, axis in axes.items():
        if all(op in ops for op in axis["formula"]):
            active.append(axis_name)
    return active

result = infer_axes(scene["operators_detected"])

print("Scene:", scene["description"])
print("Operators:", scene["operators_detected"])
print("Projected axes:", result)
