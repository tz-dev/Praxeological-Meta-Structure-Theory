"""
PMS Example Script 02 – Validate an Operator Chain
File: 02_validate_operator_chain.py

Description:
    Loads the PMS model and uses the dependency_table to validate whether
    a given operator chain (e.g. Δ → □ → Θ) is structurally allowed.
    This demonstrates how PMS can be used to formally check operator
    compositions against the axiomatic dependency graph.

Model:
    - PMS schema_version: PMS_1.1
    - Canonical model file: ../model/PMS.yaml

PMS structures used:
    - pms_model_reference.dependency_table
    - pms_model_reference.meta_axioms (for reference, if needed)

Usage:
    python 02_validate_operator_chain.py

Dependencies:
    - PyYAML (yaml)

Notes:
    - PMS works on structural operators, not mental states.
    - Validity here is purely formal (dependency-based), not ethical or empirical.
    - This script must NOT be used to evaluate persons, only operator chains.
"""

import yaml

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

dependency_table = {
    ax["axiom"]: ax["depends_on"]
    for ax in pms["pms_model_reference"]["dependency_table"]
}

def validate_chain(chain):
    """Check whether each operator is allowed to follow given prior operators."""
    seen = set()
    for op in chain:
        required = set(dependency_table[op])
        if not required.issubset(seen):
            return False, f"Operator {op} requires {required}, but only {seen} are available."
        seen.add(op)
    return True, "Valid chain."

# Example: Awareness = ["Θ", "□", "Δ"]  (in reverse generative order)
chain = ["Δ", "□", "Θ"]
ok, msg = validate_chain(chain)

print("Chain:", chain)
print("Valid?", ok)
print("Message:", msg)
