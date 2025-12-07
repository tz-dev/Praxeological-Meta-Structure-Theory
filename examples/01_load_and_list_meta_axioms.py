import yaml

with open("../model/PMS.yaml", "r", encoding="utf-8") as f:
    pms = yaml.safe_load(f)

axioms = pms["pms_model_reference"]["meta_axioms"]

print("Meta-Axioms (Δ–Ψ):")
for ax in axioms:
    print(f"{ax['id']}: {ax['name']}  — depends on {ax['depends_on']}")
