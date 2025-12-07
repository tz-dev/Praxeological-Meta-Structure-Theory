graph LR
    subgraph MetaAxioms
      Delta["Δ"]
      Nabla["∇"]
      Frame["□"]
      Lambda["Λ"]
      Alpha["Α"]
      Omega["Ω"]
      Theta["Θ"]
      Phi["Φ"]
      Chi["Χ"]
      Sigma["Σ"]
      Psi["Ψ"]
    end

    subgraph Axes
      A_axis["Awareness (A) = Θ ∘ □ ∘ Δ"]
      C_axis["Coherence (C) = Θ ∘ Λ ∘ □ ∘ ∇"]
      R_axis["Responsibility (R) = Ψ ∘ Φ ∘ Θ ∘ Ω"]
      E_axis["Action (E) = Σ ∘ Θ ∘ ∇"]
      D_axis["Dignity-in-Practice (D) = Ψ ∘ Χ ∘ Ω"]
    end

    Delta --> A_axis
    Frame --> A_axis
    Theta --> A_axis

    Nabla --> C_axis
    Frame --> C_axis
    Lambda --> C_axis
    Theta --> C_axis

    Omega --> R_axis
    Theta --> R_axis
    Phi --> R_axis
    Psi --> R_axis

    Nabla --> E_axis
    Theta --> E_axis
    Sigma --> E_axis

    Omega --> D_axis
    Chi --> D_axis
    Psi --> D_axis
