"""
PMS Example Script 05 – Visualize the Self-Model Operator Chain
File: 05_visualize_self_model.py

Description:
    Loads the PMS model and builds a directed graph of the self-model
    operator chain:
        Self = Ψ ∘ Σ ∘ Χ ∘ Φ ∘ Θ ∘ Ω ∘ Α ∘ Λ ∘ □ ∘ ∇ ∘ Δ
    The script visualizes this sequence as a left-to-right graph, showing
    how self-binding (Ψ) is structurally grounded in the preceding operators.

Model:
    - PMS schema_version: PMS_1.1
    - Canonical model file: ../model/PMS.yaml

PMS structures used:
    - derived_structures.self_model.formula_sequence
    - Optionally pms_model_reference.meta_axioms for labels / tooltips

Usage:
    python 05_visualize_self_model.py

Dependencies:
    - PyYAML (yaml)
    - networkx
    - matplotlib

Notes:
    - The self-model here is a structural fixpoint of praxis, not a claim
      about inner experience or consciousness.
    - For artificial systems, Ψ should be read as policy / constraint
      stability, not as subjective selfhood.
    - This visualization is a didactic tool for theory, teaching and
      architecture design, not a diagnostic instrument.
"""

import yaml
import networkx as nx
import matplotlib.pyplot as plt

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

seq = pms["derived_structures"]["self_model"]["formula_sequence"]

G = nx.DiGraph()
for i in range(len(seq) - 1):
    G.add_edge(seq[i], seq[i + 1])

plt.figure(figsize=(10, 3))
pos = {seq[i]: (i, 0) for i in range(len(seq))}
nx.draw(G, pos, with_labels=True, arrows=True, node_size=1500)
plt.title("Self-Model Operator Chain (Ψ ∘ … ∘ Δ)")
plt.show()
