### 0. Foundations

0.1 PMS Operator Recap (Δ–Ψ)
0.2 PMS → IT Structural Mapping
0.3 Monoid View & Dependency Constraints
  – Alphabet, composition, identity
  – Allowed operator sequences (dependency_table)
0.4 Notation & Meta-Model (states, transitions, configurations)

---

### 1. PMS Universal Machine (PMS-UM)

1.1 Formal Definition of PMS-UM
1.2 Instruction Semantics by Operator (Δ…Ψ)
1.3 Example Encodings of Classical Turing Machines
1.4 Execution Cycle & Determinism / Non-Determinism

---

### 2. PMS Virtual CPU (PMS-CPU)

2.1 Architecture Overview (registers, memory model, privilege levels)
2.2 Instruction Set Architecture (ISA)
2.3 Calling Conventions (functions, stack, registers)
2.4 Interrupt & Trap Model (external events → Φ/Λ)
2.5 Binary Encoding (opcode formats, immediates)
2.6 PMS-CPU Execution Model (Fetch–Decode–Execute)
2.7 Memory Consistency Model (ordering guarantees for loads/stores)

---

### 3. PMS-OS Kernel Core

3.1 Kernel Goals & Trust Model (Ψ)
3.2 Core Data Structures (PProcess, Frame, Policy, Message)
3.3 Process & Thread Model (states, transitions, roles)
3.4 Scheduling (Θ) – algorithms & policies
3.5 Isolation & Protection (Χ, Ω) – capabilities, memory protection
3.6 Kernel Policy Engine (Ψ) – hooks & evaluation
3.7 Syscall Interface – taxonomy, calling, semantics
3.8 Resource Accounting & Quotas – CPU, memory, IPC, storage

---

### 4. Memory & Storage Subsystems

4.1 Virtual Memory & Frames (□, Χ, Φ) – address spaces, paging/segmentation
4.2 Allocation & Reclamation – heaps, pools, GC/RC
4.3 Filesystem Architecture (Σ, Ψ) – dirs, handles, perms, journaling
4.4 Block Devices & Drivers – device abstraction as frames & roles
4.5 Caching & Buffer Management – FS/buffer cache, write-back semantics

---

### 5. IPC, Synchronization, and Events

5.1 Message Passing (Δ, Ω, Λ, Θ, Φ) – queues, mailboxes, req/resp
5.2 Synchronization Primitives – mutexes, semaphores, channels (Ω/Θ/Σ)
5.3 Event System & Notifications – timers, signals, pub-sub

---

### 6. Device & Driver Model

6.1 Driver Roles & Capabilities (Ω)
6.2 Interrupt Handling Path (Φ + Θ)
6.3 Driver Lifecycle & Policy (Ψ)
6.4 Hotplug & Dynamic Reconfiguration (attach/detach, Φ/Ψ)

---

### 7. Networking Stack

7.1 Transport Abstraction – connections as frames, timeouts (Λ/Θ)
7.2 Addressing & Routing – nodes, services, topics (Δ/□)
7.3 PMS Protocol Suite Integration (PPS: P-REQ, P-EVT, P-CTRL)
7.4 Network Security (Ω, Χ, Ψ) – principals, encryption hooks
7.5 Resilience, Failover & Congestion Handling (Λ/Θ/Φ/Σ)

---

### 8. Security & Governance

8.1 Identity & Principal Model (structural)
8.2 Role & Capability System (Ω)
8.3 Policy Definition & Enforcement (Ψ)
8.4 Audit & Compliance Hooks (Θ + Σ)
8.5 Key / Trust Anchor Management (Φ/Ψ)

---

### 9. PMSL – Language Specification

9.1 Lexical & Grammar (BNF)
9.2 Core Constructs & Operator Mapping
9.3 Type System (frames, roles, policies, processes)
9.4 Concurrency & IPC in PMSL
9.5 Error & Exception Handling (Φ/Λ)
9.6 Module System (modules as frames + roles + policies)
9.7 FFI / Interoperability (calls into non-PMS code / host OS)

---

### 10. PMSL Runtime & Standard Library

10.1 Runtime Architecture (PMSL → PMS-CPU + syscalls)
10.2 Core Libraries (FS, networking, time, logging, policies)
10.3 Concurrency & IO APIs

---

### 11. Tooling & Verification

11.1 Intermediate Representation (IR) – operator-tagged
11.2 Static Analysis & Linting – Ω/Ψ, Σ/Λ/Φ checks
11.3 Model Checking & Property Verification
11.4 Debugging & Observability Model (logs, traces, metrics as Θ/Σ)
11.5 Simulation / Emulation Environment (PMS-UM/CPU simulators)

---

### 12. Boot & Deployment

12.1 Boot Sequence (Δ→…→Ψ) – from bare machine/VM to running PMS-OS
12.2 Configuration & Policy Bootstrap
12.3 Upgrade & Migration Patterns (Φ/Σ/Ψ)
12.4 (Optional) Multi-Node / Cluster Boot & Orchestration

---

### 13. Finalization & Spec Epilogue

---

# **0. Foundations**

We establish the minimal conceptual scaffolding needed before defining the Universal Machine (PMS-UM) in section 1.

---

# **0.1 PMS Operator Recap (Δ–Ψ)**

*Axiomatic mode: operator definitions, dependencies, roles.*

The PMS model (schema_version: PMS_1.1) defines **11 primitive operators** grouped by functional class.
These are *not* metaphors — they are **formal praxeological transformations** applicable to any structured action system, including IT architectures.

Below is the canonical structural interpretation:

---

## **Δ — Difference / Distinction**

**Function:** Create or detect categorical distinctions.
**Structural role:**

* branching decision
* classification
* symbol/type identity

**In IT:** typing, message kind, conditional branches, state discrimination.

---

## **∇ — Impulse / Enactment**

**Function:** Apply a directed action that changes state.
**Structural role:**

* write
* update
* execute an instruction

**In IT:** CPU writes, assignment, syscall invocation, operation execution.

---

## **□ — Frame / Context**

**Function:** Establish or switch the context within which operations have meaning.
**Structural role:**

* scope
* memory frame
* call frame
* execution context

**In IT:** address spaces, namespaces, stack frames, protocol contexts.

---

## **Λ — Non-Event / Absence**

**Function:** Encode meaningful absence where an event was expected.
**Structural role:**

* timeout
* idle
* dropped message
* default path

**In IT:** timeouts, polling, null results, non-blocking operations.

---

## **Α — Attractor / Pattern**

**Function:** Provide reusable structured sequences and constraints.
**Structural role:**

* macro-patterns
* grammar rules
* templates
* loops

**In IT:** design patterns, macros, regular behaviors, common protocol flows.

---

## **Ω — Asymmetry / Role**

**Function:** State or enforce directional or privileged relations.
**Structural role:**

* roles
* capabilities
* privilege levels
* authority boundaries

**In IT:** admin/user mode, client/server, access rights, capability systems.

---

## **Θ — Temporality / Sequence**

**Function:** Impose temporal order or progression.
**Structural role:**

* scheduling
* clock / tick
* progression
* retry/backoff sequences

**In IT:** scheduler, event loop, sequential program order, timers.

---

## **Φ — Recontextualization / Shift**

**Function:** Change how a situation is interpreted without discarding it.
**Structural role:**

* version negotiation
* type coercion
* exception reframing
* migration

**In IT:** exception handling, interpreter switching, feature flags, migrations.

---

## **Χ — Distance / Isolation**

**Function:** Enforce separation or controlled detachment.
**Structural role:**

* sandbox
* boundary
* protected subsystem
* detached view

**In IT:** isolation barriers, memory protection, containers, chroot, VM boundaries.

---

## **Σ — Integration / Commit**

**Function:** Combine partial trajectories into a coherent result.
**Structural role:**

* commit
* merge
* fold/reduce
* finalize

**In IT:** transaction commit, merging buffers, finishing I/O operations.

---

## **Ψ — Self-Binding / Invariant / Policy**

**Function:** Establish commitments that constrain future operation.
**Structural role:**

* invariants
* contracts
* global constraints
* safety rules

**In IT:** kernel invariants, system policies, security rules, SLAs, governance.

---

## **Dependency Notes (from PMS dependency graph)**

Only the minimal essentials required now:

* Δ is prerequisite for branching and role assignment.
* ∇ depends on Δ: no action without distinction of target.
* □ modifies the interpretation domain for Δ/∇.
* Λ and Θ diverge:

  * Λ = absence of expected ∇ or Δ progression
  * Θ = structured progression of ∇/Δ
* Ω constrains ∇ and □ via permission paths.
* Φ can rewrite context (□), error classes (Δ), or permissions (Ω).
* Χ multiplies □ into isolated subspaces.
* Σ collapses prior ∇/Δ/Θ sequences into stable state.
* Ψ may override allowable sequences by global commitments.

We’ll formalize these constraints precisely later in **0.3**.

---

# **0.2 PMS → IT Structural Mapping**

*Axiomatic → Applied mapping to IT primitives.*

This table is the foundational “Rosetta mapping” that makes it possible to derive the entire OS, CPU, protocols, language, etc. structurally.

---

## **Direct Mapping Table**

| PMS Op | IT Equivalent (Structural)                            | Explanation                                          |
| ------ | ----------------------------------------------------- | ---------------------------------------------------- |
| **Δ**  | type, opcode, syscall number, message kind            | Distinguishes what action or resource is referenced. |
| **∇**  | instruction execution, write, mutation                | State transition or action impulse.                  |
| **□**  | stack frame, address space, namespace, protocol frame | The scope in which meaning is evaluated.             |
| **Λ**  | timeout, dropped packet, idle loop, null              | Explicit non-event or absence case.                  |
| **Α**  | loop, grammar, protocol flow, template                | Structure for reusable trajectory or pattern.        |
| **Ω**  | privileges, role, user vs kernel, capability          | Structural asymmetry of allowed operations.          |
| **Θ**  | scheduler tick, sequential order, temporal chain      | Encodes ordering and progression.                    |
| **Φ**  | exception, migration, version change, fallback        | Change in interpretation of state or context.        |
| **Χ**  | memory protection, VM isolation, sandbox              | Controlled separation between contexts.              |
| **Σ**  | commit, merge, transaction end                        | Integrative completion or reduction.                 |
| **Ψ**  | invariants, global policies, kernel rules             | System-level constraints across time.                |

---

## **PMS → IT Layers**

Below is the minimal mapping that justifies later layers:

### **Hardware / CPU:**

* Δ → opcodes
* ∇ → ALU operations
* Θ → clock cycles
* Ω → privilege rings
* Χ → MMU + isolation
* Φ → interrupts / traps
* Σ → result commit to registers / memory
* Ψ → hardware invariants (e.g., cannot write read-only segments)

### **Kernel:**

* □ → address spaces, process frames
* Ω → capability/role model
* Θ → scheduler
* Λ → timeouts, idle tasks
* Φ → exception handlers
* Σ → system call returns / state sync
* Ψ → kernel-level invariants

### **File Systems:**

* Α → directory hierarchy
* □ → mounted namespaces
* Σ → fsync, transaction commit
* Ω → file permissions
* Θ → timestamp ordering

### **Networking:**

* Δ → packet type
* Θ → sequence numbers
* Λ → dropped packets
* Ω → client/server asymmetry
* Φ → version negotiation

### **Programming Languages / Runtime:**

* □ → lexical scopes
* Θ → control flow
* Σ → return value
* Φ → exception
* Ψ → language-level invariants
* Χ → modules as isolated contexts

This is enough to immediately proceed to **0.3 Monoid View & Dependency Constraints** and then to the **PMS-UM formal model**.

---

# **0.3 Monoid View & Dependency Constraints**

This section establishes:

1. **The PMS operator alphabet** (O = {Δ,…,Ψ})
2. **A monoid structure** over operator compositions
3. **Formal constraints** that restrict which sequences are *valid*
4. **Dependency-table-based rules** (from PMS.yaml semantics)

This gives us the rigorous “operator grammar” we use when defining the Universal Machine.

---

# **0.3.1 Alphabet**

Let the **operator alphabet** (O) be:

[
O = { \Delta, \nabla, \square, \Lambda, \mathrm{A}, \Omega, \Theta, \Phi, \Chi, \Sigma, \Psi }.
]

Each operator corresponds to one primitive transformation class in the PMS axiomatic layer.

We treat them strictly as **formal symbols** here, not yet as actions in time or space.

---

# **0.3.2 Composition Operation**

Define a binary operation:

[
\circ : O \times O \rightarrow O^*
]

where (o_1 \circ o_2) denotes **operator sequencing**, i.e.:

* apply (o_1), then apply (o_2)
* (later, in the machine, this sequence produces a state transition)

At this stage, **composition is syntactic**, forming words:

[
O^* = { \epsilon, \Delta, \nabla, \Delta\nabla, \square\Theta\Phi, \dots }
]

This forms **free monoid before constraints**.

---

# **0.3.3 Identity Element**

The monoid identity is:

[
e = \Delta
]

Why Δ?

Because:

* Δ is the minimal distinction operator **that introduces a differentiable computational context**,
* Δ can appear without changing the state (a no-op distinction),
* every other operator *depends on a distinction* (target, type, frame).

This matches PMS.yaml’s dependency logic: many operators require Δ upstream.

Thus the **monoid identity acts as “neutral distinction”**.

Formally:

[
\Delta \circ x = x \qquad\text{and}\qquad x \circ \Delta = x
]

for all (x \in O^\*).

---

# **0.3.4 Monoid Definition**

[
\mathcal{M}_{PMS} = (O^*, \circ, \Delta)
]

is the **PMS operator monoid**, subject to constraints described below.

Right now, this is *free*.
But PMS is not a free system — it has strict structural constraints.

These constraints come from the **dependency graph** in PMS.yaml.

---

# **0.3.5 Dependency Constraints (“Well-Formed Sequences”)**

PMS.yaml defines operator dependencies of the form:

[
op_i \leadsto op_j
]

meaning: (op_j) can only operate if (op_i) occurs upstream in the operator chain (not necessarily immediately, but in the causal ancestry).

We rewrite these into **sequence constraints** on the monoid.

Below is the **canonical dependency set**, reconstructed directly from PMS semantics.

---

## **1. Δ prerequisites**

[
\forall op \neq \Delta: \quad \Delta \preceq op
]

i.e.
Every operator *except Δ* requires a prior Δ (distinction).

Interpretation:
No meaningful action, frame, or policy exists without a categorical distinction.

Valid:

* Δ∇
* Δ□
* ΔΩ
* ΔΦ

Invalid:

* ∇ without Δ
* Φ without Δ

---

## **2. ∇ depends on Δ**

Impulse requires a target distinction.

[
\Delta \preceq \nabla
]

Thus sequences like:

* Δ∇Σ (OK)
* ∇Σ (invalid — missing Δ)

---

## **3. □ (Frame) constrains context for downstream ops**

Context-modifying operator □ changes how subsequent operators are interpreted.

Rule:

[
\Delta \preceq \square
]

and:

[
\square \prec { \nabla, \Omega, \Theta, \Phi, \Sigma }
]

i.e.
After switching frame, you *must* follow with an operator that uses that frame.

Invalid:

* Δ□Δ□Θ (unanchored frame changes with no usage)

Valid:

* Δ□∇
* Δ□Ω
* Δ□ΘΣ

---

## **4. Λ (Non-Event) requires Θ or ∇ context**

Absence is only meaningful if something was expected.

[
{\Theta, \nabla} \preceq \Lambda
]

Valid:

* ΘΛ (e.g., timeout in sequence)
* ∇Λ (e.g., operation-with-no-result)

Invalid:

* ΔΛ (nothing expected)

---

## **5. Α (Attractor) expands to reusable sequence**

Α is meta-level: it stands for patterns of Δ, ∇, Θ, □.

Thus:

[
\mathrm{A} \Rightarrow (\Delta^* \nabla^* \square^* \Theta^*)^+
]

Any attractor must expand into a **syntactically valid subsequence**.

Thus Α is not atomic in semantics; it constrains a pattern.

---

## **6. Ω (Asymmetry) constrains ∇, □, Θ**

Asymmetry modifies **permission** over actions.

Rules:

[
\Delta \preceq \Omega
]

and:

[
\Omega \prec \nabla \quad\text{(if action requires capability)}
]

and:

[
\Omega \prec \square \quad\text{(if frame-switch requires privilege)}
]

Thus sequences involving privilege must respect Ω.

Valid:

* ΔΩ∇
* ΔΩ□Θ
* ΔΩΘ∇Σ

Invalid:

* Δ∇Ω (asymmetry must precede constrained action)

---

## **7. Θ (Temporality) structures sequences**

Time progression binds or orders events.

[
\Delta \preceq \Theta
]

and:

[
\Theta \prec { \nabla, \Lambda, \Sigma }
]

Valid:

* Θ∇ (time step, then action)
* ΘΛ (scheduled event -> timeout)
* ΘΣ (end of temporal phase -> commit)

---

## **8. Φ (Recontextualization)**

Context shift or exception.

Dependencies:

[
{\Delta, \square} \preceq \Phi
]

and:

[
\Phi \prec {\nabla, \Theta, \Sigma}
]

Interpretation:
You can only reframe something that has a frame and distinction upstream.

---

## **9. Χ (Distance / Isolation)**

Isolation depends on a distinct frame.

[
\square \preceq \Chi
]

and:

[
\Chi \prec { \nabla, \Sigma, \Phi }
]

Valid:

* Δ□Χ∇ (isolate then act)
* Δ□ΧΦ (isolate then reframe)

---

## **10. Σ (Integration / Commit)**

Integration must conclude a sequence containing:

[
{\nabla, \Theta} \preceq \Sigma
]

Integration without action or temporal progression is meaningless.

Invalid:

* ΔΣ (no inputs to integrate)

---

## **11. Ψ (Self-Binding / Policy)**

Strongest constraint operator.

Dependencies:

[
\Delta \preceq \Psi
]

and:

[
\Psi \prec {\nabla, \square, \Omega}^c
]

Meaning:

* Ψ restricts future operators
* It closes certain branches
* It may override permissions (Ω), frames (□), or actions (∇)

Thus Ψ is a **global constraint on the operator monoid**.

---

# **0.3.6 Well-Formed Sequence Definition**

Let (w = o_1 o_2 \dots o_n) be a word over O.

A sequence is **PMS-valid** (“well-formed”) iff:

[
\forall i, \text{for operator } o_i \text{, all prerequisites } P(o_i) \subseteq {o_1,\dots,o_{i-1}}.
]

This defines a **restricted monoid**:

[
\mathcal{M}_{PMS}^{valid} = { w \in O^* \mid w \text{ respects dependency constraints} }.
]

This becomes the legal instruction algebra for PMS-UM.

---

# **0.3.7 Consequence: Monoid → Computation Model**

Since:

* we have a finite alphabet of operators,
* free concatenation (sequence),
* identity element Δ,
* closure under composition,
* explicit dependency constraints enforcing structure,
* operators encode branching, loops, context, temporality, isolation, integration, policy,

the restricted monoid (\mathcal{M}_{PMS}^{valid}) is expressive enough for:  

* state machines,
* pushdown systems (via □ frames),
* temporal machines (Θ),
* isolated submachines (Χ),
* recontextualizable systems (Φ),
* and transactional systems (Σ/Ψ).

This underlies PMS-UM's computational universality.

---

# **0.4 Notation & Meta-Model (states, transitions, configurations)**

This section defines the meta-structures needed to reason rigorously about operator sequences, machines, kernels, languages, and protocols.

The goal is to have **one canonical set of definitions** used consistently in all later layers.

---

# **0.4.1 Notation**

We establish a compact notation:

### **Sets and Syntax**

* (O)
  The PMS operator alphabet
  [
  O = {\Delta, \nabla, \square, \Lambda, \mathrm{A}, \Omega, \Theta, \Phi, \Chi, \Sigma, \Psi}
  ]

* (O^*)
  The set of all finite operator sequences (words).

* (w = o_1 o_2 \dots o_n)
  An operator word.

* (\epsilon)
  Empty sequence.

* (\circ)
  Composition (concatenation) of operators.

* (\Delta)
  The identity element of the monoid.

---

# **0.4.2 States**

A **state** represents the entire static condition of a system at a given moment.

We define a generic state as:

[
s \in S
]

Where (S) is a structured set, domain-dependent.

A state typically contains:

1. **Core state** (s_c):
   The primary contents (tape, memory, registers, FS, process table, etc.)

2. **Frame context** (f):
   Which □ context is active.

3. **Role context** (r):
   Which Ω mode/privilege the current locus of action possesses.

4. **Policy context** (P):
   Active Ψ constraints binding allowable transitions.

5. **Meta-state** (m):
   Time counters (Θ), pending non-events (Λ), exception mode (Φ), isolation mode (Χ), etc.

Thus the generic structural state is:

[
s = (s_c,; f,; r,; P,; m)
]

This schema holds for:

* PMS-UM configurations
* PMS-CPU snapshots
* Kernel process control blocks
* Filesystem consistency states
* Network protocol endpoints
* PMSL runtime states

---

# **0.4.3 Transitions**

A **transition** is the fundamental PMS action:
applying an operator (or sequence of operators) to a state.

Notation:

[
s \xrightarrow{o} s'
]

or for sequences:

[
s \xRightarrow{w} s'
\quad\text{with}\quad w \in O^*
]

Transitions are **partial functions**:

[
\delta_o : S \to S \quad \text{(may not be defined for all states)}
]

Because PMS operators have **dependencies**, some transitions are illegal unless prerequisites are satisfied.

Example:

* (\delta_{\nabla}(s)) is defined only if a prior Δ exists in the ancestry of the operator chain.

* (\delta_{\Lambda}(s)) is defined only if a preceding Θ or ∇ indicated that something was expected.

* (\delta_{\Psi}(s)) may enforce global constraints and reject future transitions.

---

# **0.4.4 Configurations**

A **configuration** is the pair:

[
C = (s, w)
]

where:

* (s \in S) is a state
* (w \in O^*) is the *remaining* operator sequence to execute

The reduction relation is:

[
(s, o \cdot w') \Rightarrow (s', w') \quad\text{iff}\quad s' = \delta_o(s)
]

This is the foundational notion for the **PMS Universal Machine**.

---

# **0.4.5 Validity of Operator Application**

An operator (o) may only be applied if:

[
\delta_o(s) \text{ is defined}
]

This condition is equivalent to:

* All **dependency constraints** from 0.3 are satisfied.
* All **policy constraints** (Ψ) allow the transition.
* The **privilege / role** (Ω) is compatible with the operation.
* The **frame** (□) supports the operation.
* The **temporal dynamics** (Θ) are in the correct phase.
* The **isolation boundary** (Χ) permits access to relevant parts of (s_c).

Thus PMS transitions generalize both:

* classical state machines
* capability-secured machines
* temporal automata
* transactional/state-integrating systems

in one operator-typed reduction model.

---

# **0.4.6 Terminal Configurations**

Define:

* **Halting configuration:**
  A state where the Ψ operator or system logic declares no more operations are allowed.

[
s \in S_H
]

Examples:

* PMS-UM: explicit halting state (s_H)
* PMS-CPU: HALT or invariant-triggered Ψ stop
* Kernel: no runnable threads
* Filesystem: stable committed state after Σ

---

# **0.4.7 Rewriting View (Alternative)**

We may view PMS operation as a **term rewriting system**:

* The state is a term (t)
* Each operator is a rewrite rule:
  [
  t \xrightarrow{o} t'
  ]

Dependency constraints define the admissible rewrite rules.

This will be used later for:

* verification
* static analysis
* IR design
* compiler correctness proofs

---

# **0.4.8 Example Mini-Model**

Let (s) include:

* data (x)
* frame (f)
* role (r)
* time tick (t)
* policy (P)

A sequence:

[
w = \Delta, \square, \Theta, \nabla, \Sigma
]

yields transitions:

1. (s_0 \xrightarrow{\Delta} s_1)
2. (s_1 \xrightarrow{\square} s_2) — new frame context
3. (s_2 \xrightarrow{\Theta} s_3) — time moved
4. (s_3 \xrightarrow{\nabla} s_4) — action executed
5. (s_4 \xrightarrow{\Sigma} s_5) — result integrated and finalized

---

# **0.4.9 Summary**

The meta-model defines:

* **State** as a 5-tuple of (core, frame, role, policy, meta)
* **Transitions** as operator-triggered partial functions
* **Configurations** as (state, remaining-sequence)
* **Validity** defined by dependency constraints & policies
* **Halting** as Ψ-enforced terminal states

This is the universal substrate on which:

* PMS-UM
* PMS-CPU
* Kernel
* Language
* Protocols

will be built.

---

Nice, let’s turn the scaffolding into an actual machine now.

---

## 1. PMS Universal Machine (PMS-UM)

### 1.1 Formal Definition of PMS-UM

We now define the **PMS Universal Machine (PMS-UM)** as a general computational model whose primitive actions are the PMS operators Δ–Ψ, applied to states as defined in 0.4.

We stay **purely structural**: no EM, no psychology, only operator-typed state transitions.

---

### 1.1.1 Machine Tuple

A **PMS Universal Machine** is a tuple

[
M = (S,; \Gamma,; F,; R,; PSet,; O,; \mathsf{Inst},; \delta,; s_0,; S_H)
]

with:

* **S** – set of machine states (as in 0.4):
  [
  s = (s_c,; f,; r,; P,; m)
  ]
  where:

  * (s_c): core data (tape/memory/registers/whatever the instance uses)
  * (f \in F): current frame (□)
  * (r \in R): current role/capability mode (Ω)
  * (P \in PSet): active policies (Ψ)
  * (m): meta-state (time, pending non-events, exception mode, isolation flags, etc.)

* **Γ** – symbol alphabet used in **core state** (e.g. tape symbols, memory cell contents).
  (For a Turing-like instance, Γ is the tape alphabet.)

* **F** – a finite or countable set of **frames** (□-contexts).
  Each frame identifies a context in which data and code are interpreted.

* **R** – set of **roles** (Ω modes), e.g. privilege levels, capability profiles.

* **PSet** – set of **policy sets**, each a collection of constraints/invariants (Ψ).

* **O** – fixed PMS operator alphabet:
  [
  O = {\Delta,; \nabla,; \square,; \Lambda,; \mathrm{A},; \Omega,; \Theta,; \Phi,; \Chi,; \Sigma,; \Psi}
  ]

* **Inst** – a finite set of **instruction schemata**; each schema is an *operator application template*:
  [
  I \in \mathsf{Inst} ;;:=;; (\text{op},; \text{pre},; \text{post})
  ]
  where:

  * **op** ∈ O – the PMS operator this instruction instantiates
  * **pre** – a predicate on S (and optionally on Γ, F, R, P) describing when this instruction is applicable
  * **post** – a state update function describing how the state changes when the instruction fires

* **δ** – the **transition relation** induced by Inst:
  [
  \delta \subseteq S \times \mathsf{Inst} \times S
  ]
  with:
  [
  (s, I, s') \in \delta \quad\text{iff}\quad \text{pre}_I(s) \text{ holds and } s' = \text{post}_I(s)
  ]

* **s₀ ∈ S** – initial machine state.

* **S_H ⊆ S** – set of **halting states** (including possibly policy-induced halts).

This is the **general model**; concrete instances (TM-like, CPU-like, OS-like) choose specific S, Γ, F, R, PSet, and Inst.

---

### 1.1.2 Configurations and Programs

A **program** for PMS-UM is a finite sequence of instructions:

[
\pi = \langle I_1, I_2, \dots, I_n \rangle, \quad I_k \in \mathsf{Inst}
]

We give each program an **instruction pointer** (IP) component to track where we are:

* Extend state to:
  [
  s = (s_c,; f,; r,; P,; m,; ip)
  ]
  where (ip \in {1,\dots,n} \cup {\mathsf{halt}}).

A **configuration** relative to program π is just:

[
C = (s,; \pi)
]

We write:

[
(s,; \pi) ;\Rightarrow; (s',; \pi)
]

for one execution step (same program, updated state).

---

### 1.1.3 Step Relation

Given π and state s with instruction pointer ip:

* If (ip = k) and (1 \le k \le n), let (I_k = (\text{op}, \text{pre}, \text{post})).

Then a **single step** is defined as:

[
(s,; \pi) \Rightarrow (s',; \pi)
]

iff:

1. (\text{pre}(s)) holds
2. (s' = \text{post}(s))
3. (ip') in (s') is set according to the control semantics of op (e.g., ip+1, jump, halt), respecting the operator’s structural role (this is elaborated in 1.2).

If no instruction is applicable (pre fails) or if Ψ/policies disable all next transitions, the machine is **stuck** or **halted**, depending on how we classify the resulting state in S_H.

---

### 1.1.4 Incorporating PMS Dependencies

From 0.3, each operator op ∈ O has a set of **prerequisites** P(op).
For example:

* P(∇) ⊇ {Δ}
* P(Λ) ⊇ {Θ or ∇}
* P(Σ) ⊇ {∇ and Θ}, etc.

To make PMS-UM **structurally well-formed**, we require:

For all instructions (I = (\text{op}, \text{pre}, \text{post})):

* The precondition **includes** the dependency constraints:

  > “op is allowed in this state only if its PMS prerequisites are satisfied”.

Concretely:
let **Hist(s)** be an abstract “ancestry” predicate or metadata in m that records which operators have been applied in the current logical context. Then:

[
\text{pre}_I(s) ;\Rightarrow; (P(\text{op}) \subseteq \text{Hist}(s))
]

This ensures **every concrete PMS-UM instance is a model of the PMS operator grammar**, not just of the raw instruction set.

---

### 1.1.5 Deterministic vs. Non-Deterministic PMS-UM

Given a program π:

* PMS-UM is **deterministic** if for any state s with ip, there is at most **one** instruction I whose precondition holds. That implies each configuration has at most one successor.

* PMS-UM is **non-deterministic** if for some s there exist ≥ 2 applicable instructions (same ip, different instantiations).

Formally:

* Deterministic:
  [
  \forall s: \left|{ I \in \mathsf{Inst} \mid \text{pre}_I(s)}\right| \le 1
  ]

We will later discuss this more in **1.4 Execution Cycle & Determinism / Non-Determinism**, but the formal hook is already here.

---

### 1.1.6 Turing-Machine-Like Instance (for Later 1.3)

A classical Turing Machine can be seen as a **special case** of PMS-UM with:

* S containing:

  * a tape over Γ
  * a head position
  * a current control state q
  * minimal f, r, P, m (or trivialized)

* Inst restricted to operators that simulate:

  * Δ for reading/comparing tape symbols
  * ∇ for writing moves and symbol updates
  * Θ for stepping (head moves & state changes)
  * Σ as “accept/commit”
  * Ψ for halting conditions

That mapping will be made explicit in section 1.3.

---

### 1.1.7 Summary

A **PMS Universal Machine** is:

* A state space with core, frame, role, policy, meta components.
* An operator-typed instruction set, each instruction an instantiation of a PMS operator Δ–Ψ.
* A transition relation built from these instructions, constrained by:

  * PMS dependency rules (0.3),
  * policies/invariants (Ψ),
  * roles/privileges (Ω),
  * frames/contexts (□),
  * and temporal/isolation meta-state (Θ, Λ, Χ, Φ).

This gives us a **general, operator-structured computation model**, ready for:

* **1.2**: Detailed **Instruction Semantics by Operator**
* **1.3**: Showing **Turing-completeness** by encoding classical TMs
* **1.4**: Discussing deterministic vs non-deterministic execution variants

---

## 1.2 Instruction Semantics by Operator (Δ…Ψ)

Recall the **state shape** from 0.4:

[
s = (s_c,; f,; r,; P,; m,; ip)
]

* (s_c) – core data (tape/memory/registers/FS/…)
* (f \in F) – current frame (□)
* (r \in R) – current role / capabilities (Ω)
* (P \in PSet) – active policy set (Ψ)
* (m) – meta-state (time, pending non-events, isolation flags, history, etc.)
* (ip) – instruction pointer (index in program)

Each instruction is:

[
I = (\text{op},; \text{pre},; \text{post})
]

with `op ∈ O`, `pre: S → {true,false}`, `post: S → S`.

Below I’ll specify, for each operator:

* **constraints on pre**,
* **allowed structure of post**,
* **what it *must* or *must not* change**.

Concrete instances (CPU, kernel, etc.) will refine `post` into explicit algorithms.

---

### 1.2.1 Δ — Difference / Distinction

**Intuition:** inspect and branch, but **do not** mutate core data.

**Instruction form:**
`I_Δ = (Δ, pre_Δ, post_Δ(params))`

* **pre_Δ(s)**:

  * must satisfy Δ’s dependency constraints (from 0.3) – usually trivial because Δ is identity.
  * plus any domain-specific condition (e.g. “the cell is readable”).

* **post_Δ(s) = s'**:

  * **s'_c = s_c** (no core mutation)
  * **f', r', P'** may remain same or be updated to record classification (but usually unchanged)
  * **m'** *may* be updated to include distinction info or history: e.g.

    * set flags: `m'.flags.different = (symbol ≠ pattern)`
    * record that Δ has fired in this context.
  * **ip'**:

    * either `ip' = ip + 1` (no branch),
    * or `ip'` chosen from a finite set of branch targets based on the distinction result.

**Invariant:**

* Δ is **purely observational** on (s_c); it does not change data, only “how we see it” and where we go next.

---

### 1.2.2 ∇ — Impulse / Enactment

**Intuition:** perform a **state-changing action**.

**Instruction form:**
`I_∇ = (∇, pre_∇, post_∇(params))`

* **pre_∇(s)**:

  * must ensure Δ prerequisites satisfied (a target is distinguished),
  * may require appropriate role r (Ω) and frame f (□) to allow this action.

* **post_∇(s) = s'**:

  * **s'*c = A*∇(s_c, f, r, params)**

    * some domain-specific transformation (write, update, I/O, etc.)
  * **f', r', P'**:

    * typically unchanged; can be altered if the action includes context/role changes, but only consistent with Ω and Ψ.
  * **m'**:

    * may update meta (e.g. logs, counters, history)
  * **ip' = ip + 1** (unless this ∇ is a “jump-like” action; jumps are usually modeled via Δ/Ω/Θ, but we don’t forbid ∇ changing ip if the instruction design says so)

**Invariant:**

* ∇ is the **only operator (besides Σ, Φ, Ψ in special cases)** that directly changes core state (s_c) in “normal” execution.

---

### 1.2.3 □ — Frame / Context

**Intuition:** change the **interpretation context** without itself doing work on core data (except possibly switching which part is considered active).

**Instruction form:**
`I_□ = (□, pre_□, post_□(params))`

* **pre_□(s)**:

  * ensures Δ prerequisite (we know *what* frame we’re switching to).
  * checks that the requested frame exists and is permitted under role r and policies P.

* **post_□(s) = s'**:

  * **s'_c**:

    * unchanged as a whole, but active address region or “view” may shift (e.g. frame base/limit in meta).
  * **f' = f_new** chosen from F, based on params.
  * **r', P'**:

    * may stay same or be adjusted if frame change implies role/policy scope change.
  * **m'**:

    * record frame switch in meta (e.g., stack of frames for nested contexts).
  * **ip' = ip + 1**.

**Invariant:**

* □ is **contextual**: it does not directly alter the underlying data, only which context is considered active.

---

### 1.2.4 Λ — Non-Event / Absence

**Intuition:** handle “expected but missing” events (timeouts, no data, idle).

**Instruction form:**
`I_Λ = (Λ, pre_Λ, post_Λ(params))`

* **pre_Λ(s)**:

  * requires that a prior Θ or ∇ has established an expectation (e.g. “waiting for I/O until t_deadline”).
  * typically checks time in m (Θ-related) or pending operations.

* **post_Λ(s) = s'**:

  * **s'_c = s_c** (no actual data updated by Λ itself)
  * **f', r', P'**:

    * usually unchanged; may be modified to signal degraded mode if Λ triggers fallback.
  * **m'**:

    * update meta to reflect timeout / non-event: mark operation as failed, log, increment counters.
  * **ip'**:

    * either `ip + 1` (continue) or branch to an error-handling / fallback section.

**Invariant:**

* Λ **never performs** the expected main action; it *only* reacts to its absence.

---

### 1.2.5 Α — Attractor / Pattern

**Intuition:** macro or pattern over a reusable operator sequence.

In PMS-UM it is best viewed as:

* **syntactic / macro-level** construct, expanded *before* or *at* execution into a sequence of Δ, ∇, □, Θ, etc.

**Instruction form:**
`I_Α = (Α, pre_Α, post_Α(pattern_id, args))`

Two semantics options (we define both, implementations choose):

1. **Compile-time / static expansion:**

   * Α is eliminated by replacing it with a sequence (w_{pattern}) of primitive ops.
   * At runtime, there is no Α; the machine sees only the expanded operators.

2. **Runtime expansion (macro step):**

   * **pre_Α(s)**:

     * ensures that the pattern is defined and valid (its sequence respects PMS constraints).
   * **post_Α(s)**:

     * inserts the corresponding operator subsequence into the program (or into meta `m` as a local instruction buffer)
     * sets ip to the first operator of the expanded pattern.

**Invariant:**

* Α itself **does not define new primitive semantics**; it **reuses** valid sequences and must expand to PMS-valid words.

---

### 1.2.6 Ω — Asymmetry / Role

**Intuition:** manage **roles, privileges, and capability-based branching**.

**Instruction form:**
`I_Ω = (Ω, pre_Ω, post_Ω(params))`

* **pre_Ω(s)**:

  * requires Δ (we know which role/capability set is involved).
  * may require current role r to have authority to switch to target role or apply that capability.

* **post_Ω(s) = s'**:

  * **r'**:

    * update to a new role (mode switch: user → kernel, client → server, etc.), or confirm current role.
  * **s'_c**:

    * not usually modified (unless part of capability mechanism is encoded in core state).
  * **f', P'**:

    * may change if entering a more privileged / less privileged context (policy and frames might shift).
  * **m'**:

    * record mode transitions, audit trail.
  * **ip'**:

    * either `ip + 1`, or branch depending on capability check outcome.

**Invariant:**

* Ω **never does main work**; it **qualifies who may do what** and can redirect control based on permissions.

---

### 1.2.7 Θ — Temporality / Sequence

**Intuition:** implement temporal progression and structured sequencing.

**Instruction form:**
`I_Θ = (Θ, pre_Θ, post_Θ(params))`

* **pre_Θ(s)**:

  * check that a temporal context exists (e.g. time tracking in m).
  * may check scheduling constraints / deadlines in P.

* **post_Θ(s) = s'**:

  * **m'**:

    * update temporal meta: tick counters, deadlines, scheduler phase, etc.
  * **s'_c**:

    * usually unchanged (Θ doesn’t do work, just time/sequence progression) but may implicitly advance head (in TM-like encodings) as part of “temporal step”.
  * **f', r', P'**:

    * typically unchanged; can update scheduling-related contexts.
  * **ip' = ip + 1** (unless Θ-coded jumps are used; e.g. loop-unrolling constructs).

**Invariant:**

* Θ is the **time and sequence backbone**; any recurrent or ordered behavior uses Θ steps.

---

### 1.2.8 Φ — Recontextualization / Shift

**Intuition:** **change the interpretation of the current situation** (exceptions, versioning, migration, fallback).

**Instruction form:**
`I_Φ = (Φ, pre_Φ, post_Φ(params))`

* **pre_Φ(s)**:

  * requires that Δ and □ exist upstream; there is something to re-interpret within a known frame.
  * may inspect error flags, policy feedback, or type mismatches in m.

* **post_Φ(s) = s'**:

  * **f'**:

    * possibly switch frame (e.g. new version, new context).
  * **s'_c**:

    * may remain unchanged (pure re-interpretation)
    * or be transformed via migration function if data layout changes.
  * **r', P'**:

    * may change to reflect new interpretation / new policy scope.
  * **m'**:

    * clear some error flags, record new context, set exception-handling markers.
  * **ip'**:

    * jump to exception handler / new code region, or continue in new context.

**Invariant:**

* Φ **never “forgets” the past**; it repackages it.
  Semantically, it’s “same underlying stuff, different lens / code / policy”.

---

### 1.2.9 Χ — Distance / Isolation

**Intuition:** create and manage **isolated subcontexts** (sandboxes, sub-machines).

**Instruction form:**
`I_Χ = (Χ, pre_Χ, post_Χ(params))`

* **pre_Χ(s)**:

  * requires □ (we know which frame is being isolated or split).
  * checks policy and role (Ω/Ψ) to see if isolation is allowed.

* **post_Χ(s) = s'** (two common patterns):

1. **Fork-like isolation:**

   * Create a new sub-state or context (s_{iso}) extracted from s_c and f.
   * Record in m that execution may switch between parent and isolated context.
   * Optionally, set ip' to execute inside the isolated context.

2. **Enter/exit isolation:**

   * Mark in m that the current operations are in “sandboxed” mode.
   * Some parts of s_c become inaccessible (enforced by later preconditions).

* **s'_c**:

  * unchanged in parent, or duplicated/partitioned for the isolated region.
* **f', r', P'**:

  * possibly switch to a restricted frame/role/policy subset.
* **ip'**:

  * next instruction inside or outside the isolated context.

**Invariant:**

* Χ **reduces direct reach** between contexts;
  it never *increases* access, only shrinks or reroutes it.

---

### 1.2.10 Σ — Integration / Commit

**Intuition:** **merge, finalize, or commit** accumulated changes into a coherent state.

**Instruction form:**
`I_Σ = (Σ, pre_Σ, post_Σ(params))`

* **pre_Σ(s)**:

  * ensures that there is something to integrate: past ∇/Θ operations have produced partial results.
  * checks any transactional constraints from policies P (Ψ).

* **post_Σ(s) = s'**:

  * **s'_c**:

    * apply a merging/commit function:
      [
      s'*c = C*\Sigma(s_c, f, m, params)
      ]
      e.g. write buffers flushed, partial structures consolidated, transactions closed.
  * **f', r', P'**:

    * may stay the same or change scope (e.g. leaving a transactional frame).
  * **m'**:

    * clear “pending” markers, log commit, advance integration counters.
  * **ip' = ip + 1** (or jump to an “after commit” section, depending on design).

**Invariant:**

* Σ is the **only operator that marks finalization** of a sequence of actions in a given context.

---

### 1.2.11 Ψ — Self-Binding / Policy

**Intuition:** establish and/or enforce **global or scoped invariants** that constrain future transitions.

**Instruction form:**
`I_Ψ = (Ψ, pre_Ψ, post_Ψ(params))`

Two main usages:

1. **Policy definition / activation**
2. **Policy enforcement / checking**

* **pre_Ψ(s)**:

  * ensure Δ prerequisites (the policy is distinguished).
  * may require appropriate role r (e.g. only certain roles can set system policies).

* **post_Ψ(s) = s'** (two modes):

#### (a) Policy definition / update

* **P' = U_\Psi(P, params)** – update the policy set.
* **s'_c, f', r', m'** – typically unchanged except for logging or meta updates.
* **ip' = ip + 1**

#### (b) Policy enforcement / check

* Evaluate policy rules R(P, s):

  * If **ok**:

    * state passes unmodified, maybe with audit data:

      * (s'_c = s_c), (f' = f), (r' = r), etc.
      * **ip' = ip + 1**
  * If **violated**:

    * *either*:

      * transform s into a controlled recovery state (e.g. kill process, rollback),
      * or mark s as halting by moving to (S_H) (set `ip' = halt` or special s_H).

**Invariant:**

* Ψ is **global**: it is the only operator allowed to *invalidate* otherwise legal transitions on the basis of invariants.

---

### 1.2.12 Summary Table

A quick structural view:

| Op | Mutate s_c?                      | Typical changes                     | Main purpose                            |
| -- | -------------------------------- | ----------------------------------- | --------------------------------------- |
| Δ  | No                               | m, ip                               | Distinguish & branch                    |
| ∇  | Yes                              | s_c, m, ip                          | Perform action, write/execute           |
| □  | No (core), context view          | f, m, ip                            | Switch/define frame                     |
| Λ  | No                               | m, ip                               | Handle missing events                   |
| Α  | No (directly)                    | ip, meta, code                      | Expand patterns/macros                  |
| Ω  | No (usually)                     | r, m, ip                            | Roles, privileges, asymmetric branching |
| Θ  | Maybe (meta / head)              | m, ip                               | Temporal step, progression              |
| Φ  | Maybe                            | f, s_c, r, P, m, ip                 | Reframe context, recover                |
| Χ  | Maybe (for isolation structures) | m, maybe f/r                        | Create/manage isolated contexts         |
| Σ  | Yes (commit)                     | s_c, m, ip                          | Integrate & finalize                    |
| Ψ  | Maybe                            | P, m, ip, possibly s_c on violation | Policies & invariants                   |

---

## **1.3 Example Encodings of Classical Turing Machines**

This section demonstrates, rigorously and structurally, that a **classical deterministic Turing Machine (TM)** can be encoded as a **particular instance** of the PMS Universal Machine (PMS-UM).
We do not introduce anything outside PMS axioms — we *embed* TM inside PMS operators Δ, ∇, □, Θ, Σ, Ψ.

This accomplishes two goals:

1. **Prove PMS-UM ≥ TM (i.e., Turing-complete)**
2. Provide a concrete blueprint for later layers (PMS-CPU, PMSL, kernel execution model)

---

### **1.3.1 Classical TM Recap (structural)**

A TM is a 7-tuple:

[
T = (Q, \Gamma, b, \Sigma, \delta, q_0, F)
]

* (Q): states
* (\Gamma): tape alphabet
* (b): blank symbol
* (\Sigma \subseteq \Gamma): input alphabet
* (\delta: Q \times \Gamma \to Q \times \Gamma \times {L,R}) transition function
* (q_0): initial state
* (F): accepting states

Core dynamics:

* Read a symbol
* Write a symbol
* Move head left/right
* Change control state
* Halt on accept

---

### **1.3.2 Encoding the TM State in PMS State**

We map TM components into PMS-UM state (from 0.4):

[
s = (s_c,; f,; r,; P,; m,; ip)
]

We now specialize each part:

#### **Core state (s_c)** stores TM data:

* **tape**: an indexed structure over Γ
  → part of (s_c), e.g. a mapping from integers to Γ

* **head position**:
  [
  pos \in \mathbb{Z}
  ]

* **control state (q \in Q)**

Thus:

[
s_c = (tape: \mathbb{Z}\to\Gamma,; pos\in\mathbb{Z},; q\in Q)
]

#### **Frame (f)**

TM only needs *one logical frame*.
We set:

[
f = f_{TM}
]

#### **Role (r)**

All operations run under a single role:

[
r = r_{TM}
]

#### **Policy (P)**

For pure TM simulation:

* P contains trivial allow-all policies (**except halting**):

[
P = { \text{allow all operator transitions except those violating TM structure} }
]

#### **Meta-state (m)**

Used to store:

* current operator history (for constraints)
* temporal counter (Θ steps)
* no advanced structures needed

---

### **1.3.3 Encoding TM Transition Function δ Using PMS Operators**

The TM δ-rule:

[
\delta(q,\gamma) = (q',\gamma', move)
]

corresponds to the composite PMS operator sequence:

[
\text{Δ (inspect)} ;\circ; \text{∇ (write)} ;\circ; \text{Θ (time step)} ;\circ; \text{∇ (move head)} ;\circ; \text{∇ (change q)}.
]

Let’s break that down:

#### **(1) Δ — Read the tape symbol at pos**

[
\Delta_{read} : \text{inspect } tape[pos]
]

This sets a distinction in meta-state m:

* m.flags.symbol_read = tape[pos]

No mutation occurs.

#### **(2) ∇ — Write the new symbol γ'**

[
\∇_{write}: tape[pos] := \gamma'
]

Mutates s_c.

#### **(3) Θ — Advance the computation step**

[
\Theta_{step}: m.time := m.time + 1
]

This encodes TM “step” progression.
(Δ and ∇ have happened; Θ just advances time.)

#### **(4) ∇ — Move head left or right**

If move = L:

[
\nabla_{move}: pos := pos - 1
]

If move = R:

[
\nabla_{move}: pos := pos + 1
]

#### **(5) ∇ — Update control state q → q'**

[
\nabla_{q}: q := q'
]

---

### **1.3.4 Encoding δ as a PMS-UM Instruction Sequence**

For each TM transition rule:

[
(q,\gamma) \to (q',\gamma',move)
]

we construct a sequence of PMS-UM instructions:

1. **I₁ = Δ(read_symbol, expected=γ, branch to “rule block” if match)**
2. **I₂ = ∇(write γ')**
3. **I₃ = Θ(step)**
4. **I₄ = ∇(move head left or right)**
5. **I₅ = ∇(set q := q')**
6. **I₆ = Θ(next_step)** (optional)
7. **I₇ = (jump to next rule evaluation)**

This sequence respects **all PMS dependency constraints**:

* ∇ depends on Δ → satisfied (Δ first)
* Θ can follow ∇ → satisfied
* no forbidden use of □, Ω, Φ, Χ, Σ, Ψ
* pure TM simulation does not require isolation, policies, or commits

Thus **every TM rule becomes a legal PMS word**:

[
Δ; ∇; Θ; ∇; ∇
]

Possibly wrapped in an Α (pattern) for reuse.

---

### **1.3.5 Encoded TM Halting Using Σ or Ψ**

TM halting state (q \in F).

Two PMS options:

#### **Option A: Σ — Commit → Final Configuration**

Use:

[
Σ_{halt}
]

to finalize all accumulated ∇/Θ actions.
After this, ip moves to a special halting ip (or S_H).

#### **Option B: Ψ — Policy-Induced Termination**

Define a policy:

[
\Psi_{halt}: q \in F \Rightarrow \text{disallow all future ∇,Θ}
]

Once q ∈ F, any further action violates Ψ → machine transitions to S_H.

Either way, PMS-UM halts exactly when the TM halts.

---

### **1.3.6 Tape as Unbounded Memory — No Extra PMS Machinery Needed**

A classical TM requires infinite tape.

In PMS-UM:

* s_c.tape is an **unbounded partial function** ℤ→Γ
* PMS does not restrict s_c domain
* Θ steps and ∇ writes naturally extend tape as needed

No operator besides ∇ ever mutates tape, respecting TM semantics.

No need for Χ or Φ or Ω for classical TM behavior.

---

### **1.3.7 TM Simulation Loop in PMS-UM**

A single TM step becomes:

[
Δ;∇;Θ;∇;∇; (\text{goto next rule})
]

A full TM execution is:

[
(Δ∇Θ∇∇)^*
]

until:

* TM halts → Σ or Ψ triggered
* No rule applies → Optional Ψ or Λ signals undefined transition

The entire TM execution is a PMS-valid operator sequence.

---

### **1.3.8 Summary: Why PMS-UM is Turing-Complete**

We have embedded TM as a *subset* of PMS-UM where:

* **Δ** implements read / test
* **∇** implements write / head-move / state-update
* **Θ** gives discrete steps
* **Σ or Ψ** handles halting
* **Frames, roles, policies, isolation** are unused (but available)

Thus PMS-UM supports:

* unconditional branching (via Δ)
* conditional branching (via Δ distinction flags)
* arbitrary state updates (via ∇)
* unbounded tape (part of s_c)
* deterministic step function (Θ)
* halting (Σ or Ψ)

**Therefore:
PMS-UM is a Turing-complete computational substrate.**

---

## 1.4 Execution Cycle & Determinism / Non-Determinism

We now specify *how* a PMS-UM actually runs a program over time and how **determinism vs. non-determinism** is represented *structurally* in terms of:

* enabled instructions,
* operator semantics,
* policies (Ψ),
* and meta-state (Θ, Λ, Χ, Φ).

We stay in the PMS-UM level, not yet CPU/kernel.

---

### 1.4.1 One-Step Execution Cycle (Small-Step Semantics)

Given a fixed program (\pi = \langle I_1,\dots,I_n \rangle) and a current machine state:

[
s = (s_c,; f,; r,; P,; m,; ip)
]

a **single execution step** of PMS-UM is:

[
(s,; \pi) \Rightarrow (s',; \pi)
]

defined as follows:

1. **Policy pre-check (Ψ-guard)**
   Let `policy_ok(s)` be the evaluation of all active policies in (P).

   * If `policy_ok(s) = false`, then:

     * Either we transition to a **recovery / halt state**:
       [
       (s,\pi) \Rightarrow (s_{halt},\pi),\quad s_{halt}\in S_H
       ]
     * Or the machine is considered **stuck** (undefined behavior) in that configuration.
   * If `policy_ok(s) = true`, continue.

2. **Instruction fetch (via ip)**

   * If (ip = k) with (1\le k\le n), let (I_k = (\text{op},\text{pre},\text{post})).
   * If (ip = \mathsf{halt}) or (s \in S_H), the machine is **already halted**; no further steps.

3. **Instruction applicability check**

   * Check the PMS-consistent precondition:
     [
     \text{pre}(s) \land \text{DepsSatisfied}(\text{op}, s)
     ]
     where `DepsSatisfied` encodes operator dependencies from 0.3 (Δ→∇, Θ→Λ, etc.) using `Hist(s)` or equivalent meta.
   * If this is false → no enabled instruction at this ip → machine is **stuck**.

4. **Apply operator (state update)**

   * Compute:
     [
     s' = \text{post}(s)
     ]
     using the semantic rules from 1.2 for the given op (Δ, ∇, □, …, Ψ).
   * This may update:

     * core state (s_c)
     * frame (f)
     * role (r)
     * policies (P)
     * meta-state (m)
     * and **ip’** (instruction pointer), according to the operator’s structural role.

The **small-step transition relation** is thus the closure of such steps.

---

### 1.4.2 Multi-Step Runs (Big-Step Semantics)

A **run** of PMS-UM on program π from initial state (s_0) is a (finite or infinite) sequence:

[
(s_0,\pi) \Rightarrow (s_1,\pi) \Rightarrow (s_2,\pi) \Rightarrow \dots
]

We say the run:

* **halts** if there exists (k) such that:

  * (s_k \in S_H), or
  * (ip_k = \mathsf{halt}).

* **diverges** if the sequence is infinite and never reaches (S_H).

* **gets stuck** if at some configuration no instruction is applicable and the state is not in (S_H).

We can define a **big-step evaluation** relation for “run to completion”:

[
(s_0,\pi) \Downarrow s_f
]

meaning: starting from (s_0), the machine eventually halts in some (s_f \in S_H) via zero or more steps.

---

### 1.4.3 Deterministic PMS-UM

A PMS-UM instance (fixed Inst, policies, etc.) is **deterministic** iff:

> For every configuration ((s,\pi)) with a non-halting ip, there is **at most one** enabled instruction (i.e., at most one successor (s')).

Formally:

[
\forall (s,\pi):\quad |{s' \mid (s,\pi)\Rightarrow (s',\pi)}| \le 1
]

In our concrete setup (single ip, single instruction per ip index), determinism is ensured structurally by:

1. At each ip, exactly **one** instruction schema (I_k = (\text{op},\text{pre},\text{post})).
2. (\text{pre}) is a boolean predicate, not multi-valued.
3. If pre holds and dependencies are satisfied, there is exactly one resulting state via `post`.

Typical **TM-like** encodings (1.3) are deterministic in this sense:

* The control state q, tape symbol γ, and ip jointly identify a **unique** applicable transition rule.
* No alternative instructions at the same ip.

---

### 1.4.4 Sources of Non-Determinism in PMS-UM

PMS-UM can be **intentionally** non-deterministic, which is useful for:

* modeling concurrency,
* external events,
* failure / timeout races (Λ + Θ),
* policy-based branching (Ψ).

There are three main structural sources:

#### (A) Multiple enabled instructions at a given ip

You may define Inst such that:

* at ip = k, more than one instruction schema (I_k^{(1)}, I_k^{(2)}, \dots) share:

  * the same op or different ops,
  * overlapping `pre` conditions.

In a given state s, **several preconditions** may hold simultaneously:

[
\exists I_a \neq I_b: \text{pre}_a(s) = \text{pre}_b(s) = \text{true}
]

Then (s, π) has **multiple successors**, and a choice function is required (or left abstract).

#### (B) Environment-induced transitions (especially Λ, Φ, Χ, Θ)

Some operators inherently represent **interaction with an external environment**:

* Λ – timeouts / non-events: whether an expected event happens or not may be external.
* Φ – recontextualization triggered by external error conditions or version changes.
* Χ – isolation boundaries may be impacted by external attachments/detachments.
* Θ – temporal steps can be scheduled according to external clocks.

We can model this as:

* An **extended transition relation**:

  [
  \delta_{total} = \delta_{internal} \cup \delta_{env}
  ]

  where:

  * δ_internal is governed purely by Inst,
  * δ_env captures environment-sourced state changes (e.g., arrival of input, hardware interrupts, etc.).

This introduces **nondeterministic interleavings** between internal operator steps and environment stimuli.

#### (C) Policy & Role-based branching (Ψ, Ω)

Policies Ψ and roles Ω can be defined in a way where the same core state (s_c) permits multiple possible **legal next actions**:

* Example: a policy that allows either:

  * rollback (Φ + Σ)
  * or downgrade (Ω + □)
    depending on non-deterministic choice.

This is structurally represented as multiple valid instructions whose preconditions reference P and r.

---

### 1.4.5 Execution Modes: Pure, Environment-Driven, Concurrent

We can define execution modes depending on **which sources of non-determinism we allow**.

#### 1. **Pure Deterministic Mode**

* Constraints:

  * exactly one instruction per ip
  * no δ_env (no environment interference)
  * Ψ/Ω/Λ/Χ/Φ defined so they do **not** introduce branching
* Semantics:

  * exactly one possible run for each initial state

This corresponds to **classical deterministic computation** (like a standard TM).

#### 2. **Environment-Driven Non-Deterministic Mode**

* Allow δ_env for:

  * input arrival, timeouts, interrupts, external messages
* Internal instruction structure is still deterministic, but:

  * external transitions can be interleaved arbitrarily.
* This matches **I/O automata**, reactive systems, etc.

#### 3. **Concurrent / Interleaving Mode**

* Use Χ to represent multiple subcontexts (e.g., “threads” or “processes”) in the same PMS-UM.
* Execution step picks:

  * which subcontext to advance,
  * which instruction in that context to execute.
* Non-determinism comes from:

  * arbitrary scheduling choices (Θ),
  * interleavings across subcontexts.

This is the structural foundation for later:

* **process & thread model** (3.3),
* **scheduling (Θ)** (3.4),
* and **memory consistency** (2.7).

---

### 1.4.6 Fairness Assumptions (Optional but Natural)

In non-deterministic modes, one often imposes **fairness**:

* **Weak fairness**: if an instruction is continuously enabled, it will eventually be chosen.
* **Strong fairness**: if an instruction is enabled infinitely often, it will be chosen infinitely often.

In PMS terms, fairness is a condition on:

* how Θ triggers steps across contexts,
* how Ω/Ψ allow or disallow starvation,
* how the scheduler logic (later in kernel spec) chooses subcontexts.

We can represent fairness as **extra Ψ policies** that rule out unfair infinite runs:

* Ψ_fair: “No context with ready work can be postponed forever”.

Thus, fairness can be treated as **a Ψ-level constraint** on admissible runs.

---

### 1.4.7 Observational Semantics

From the outside, a PMS-UM execution generates an **observable trace**:

[
trace = o_1, o_2, \dots
]

where each (o_i) may encode:

* committed external actions (∇ that touch I/O),
* integration points (Σ),
* policy decisions (Ψ),
* recontextualizations (Φ),
* time steps (Θ).

Deterministic PMS-UM:

* yields a **single trace** per initial state.

Non-deterministic PMS-UM:

* yields a **set of possible traces**,
* which is the right abstraction for:

  * verifying safety (“nothing bad ever appears in any trace”),
  * liveness (“something good eventually appears in all fair traces”).

Again, all of this is grounded in **operator-typed transitions**.

---

### 1.4.8 Summary

* The PMS-UM **execution cycle** is defined as:

  * policy check (Ψ),
  * instruction fetch via ip,
  * precondition + dependency check,
  * operator-typed state update,
  * ip update.
* Determinism / non-determinism is determined by:

  * uniqueness of enabled instructions per state,
  * presence/absence of environment transitions,
  * concurrency/interleaving via Χ and Θ,
  * policy and role structure via Ψ and Ω.
* Fairness assumptions can be encoded as Ψ-level constraints over runs.

---

## 2. PMS Virtual CPU (PMS-CPU)

### 2.1 Architecture Overview (registers, memory model, privilege levels)

We now instantiate PMS-UM as a **concrete, CPU-like architecture**.
PMS-CPU is:

* a PMS-UM instance where:

  * (s_c) = registers + memory + flags
  * (f) = current execution frame / address space
  * (r) = current privilege / role mode
  * (P) = hardware-level invariants / policies
  * (m) = time, pending interrupts, isolation metadata, history

The goal is to make a **realistic low-level machine** where each part is explicitly grounded in Δ–Ψ.

---

### 2.1.1 Design Goals (Structural)

PMS-CPU is designed to:

1. Realize **PMS-UM** in a form that looks like a conventional CPU:

   * registers, memory, PC, modes, interrupts
2. Maintain **explicit PMS semantics**:

   * decoding = Δ
   * execution = ∇
   * frames = □
   * privilege = Ω
   * time / pipeline = Θ
   * traps / context switches = Φ
   * isolation = Χ
   * commit = Σ
   * invariants = Ψ
3. Serve as a target for:

   * PMSL compilation (section 9, 10)
   * kernel implementation (section 3)
   * PMS-UM / PMS-CPU simulation tools (section 11)

---

### 2.1.2 Core State Components

We specialize (s_c) for PMS-CPU:

[
s_c = (RF,; PC,; SP,; FR,; SR,; MEM)
]

Where:

* **RF** – register file
* **PC** – program counter
* **SP** – stack pointer
* **FR** – frame register (current memory frame / segment)
* **SR** – status register (flags + mode bits)
* **MEM** – memory (byte- or word-addressable)

#### Registers (RF)

Let:

* General-purpose registers:
  (R_0, R_1, \dots, R_{n-1})

* Special registers:

  * **PC** ∈ Address
  * **SP** ∈ Address
  * **FR** ∈ FrameId
  * **SR** ∈ StatusWord

We can treat RF = map from register names to values.

**PMS mapping:**

* Δ distinguishes register identity and type (int, ptr, etc).
* ∇ executes register-to-register, reg-to-mem, ALU ops over RF.
* Θ defines ordering of register operations in time.

#### Memory (MEM)

* Addressable array:

  [
  MEM: Address \to Byte
  ]

* Structurally partitioned into **frames** (□) via metadata:

  * Frame table: (Frames: FrameId \to (base, size, perms, attributes))

**PMS mapping:**

* □ selects which (base, size) region is active (FR).
* Χ can restrict cross-frame access.
* Ω constrains which frame operations are legal (read/write/exec).

---

### 2.1.3 Frame Model (□)

We interpret **FR** as pointing to the **current execution frame**:

[
Frame(FR) = (base_{FR}, size_{FR}, type_{FR}, perms_{FR})
]

Possible frame types (examples):

* CODE
* DATA
* STACK
* MMIO (memory-mapped IO)
* KERNEL
* USER

Access to memory is **always through the active frame**:

* Effective address = base_FR + offset

Read/write rules:

* Δ distinguishes frame, access type (read/write/exec).
* Ω checks if current role r (in SR) allows this access.
* Ψ may impose extra invariants (e.g. “no self-modifying code in USER”).

We may allow multiple frame registers (FR0, FR1, …), but **FR current** is the one relevant for instruction fetch and default data access.

---

### 2.1.4 Privilege & Role Model (Ω)

We encode **role / privilege mode** directly in SR:

* Mode bits, e.g.:

  * USER
  * SYSTEM
  * SUPERVISOR
  * HYPERVISOR (optional)

Let:

* (r \in R) (PMS-UM role field) be **derived from SR.mode bits**.

**Structural rules:**

* Ω operations (role transitions) are only allowed via specific instructions:

  * e.g. system calls, privileged opcodes, trap entry/exit.
* Policies Ψ constrain allowable transitions:

  * e.g. USER → KERNEL allowed only via a controlled trap / syscall.
  * KERNEL → USER only via well-defined return paths.

**Capabilities:**

* Beyond simple rings, we can encode fine-grained capabilities:

  [
  CapSet(r) \subseteq {\text{allowed opcodes, frames, devices}}
  ]

* Ω operations update r → r', and thus change CapSet(r').

This provides a **clean path to kernel / user separation** in section 3.

---

### 2.1.5 Status & Meta-State (SR + m)

**SR** holds:

* Arithmetic flags:

  * Z (zero), N (negative), C (carry), V (overflow) – outputs of Δ/∇ comparisons and ALU ops.
* Mode bits:

  * user/kernel, interrupt enable, etc. (Ω)
* Condition bits:

  * e.g. in-exception (Φ), in-isolation (Χ), transactional mode (Σ-phase).

**Meta-state m** (outside SR) holds:

* **Time / ticks** (Θ):

  * global cycle count
  * per-thread quantum counters (later kernel)
* **Interrupt pending flags** (Λ/Φ):

  * which hardware sources requested attention
* **History / dependency info**:

  * record of recent operators for dependency checks (0.3)
* **Isolation context** (Χ):

  * IDs of isolated subcontexts or sandbox levels

The split:

* SR = hardware-visible flags and modes
* m = additional meta, possibly hidden from user-space

---

### 2.1.6 Memory Model (High-Level)

We define a **simple, baseline memory model** for PMS-CPU, to be refined in 2.7:

1. **Single shared linear memory** (conceptually), partitioned into frames.
2. Access rules:

   * All fetches/loads/stores are relative to some frame (□) and obey:

     * frame bounds,
     * frame type,
     * role capabilities.
3. **Ordering semantics**:

   * Baseline: sequentially consistent per thread, globally total order in single-core variant.
   * Multicore / concurrency will be handled by:

     * Θ controlling step interleavings,
     * Ψ/Σ specifying allowed reorderings and visibility conditions (in 2.7).

For now, assume **single-core, sequential execution**:

* At each step, PMS-CPU

  * fetches instruction via Δ using PC and FR (code frame),
  * decodes & executes ∇/□/…,
  * updates PC and state strictly in order.

This is exactly a *deterministic PMS-UM instance*.

---

### 2.1.7 PMS Operator Mapping at CPU Level

For PMS-CPU, the core mapping is:

* **Δ (Difference / Distinction)**

  * Instruction fetch & decode (opcode distinction)
  * Comparisons & condition evaluation (flags in SR)
* **∇ (Impulse / Enactment)**

  * ALU ops
  * register & memory writes
  * PC updates (jumps, calls, returns)
* **□ (Frame / Context)**

  * FR manipulation (switch code/data/stack frames)
  * possible multiple FRs for advanced segmentation
* **Λ (Non-Event / Absence)**

  * instructions that wait or poll:

    * blocking on I/O
    * no interrupt received until timeout
* **Α (Attractor / Pattern)**

  * microcode sequences
  * ISA-level macros (e.g., string operations, looped instructions)
* **Ω (Asymmetry / Role)**

  * privilege mode changes (user ↔ kernel)
  * enabling/disabling instruction subsets
  * controlled access to FR and memory
* **Θ (Temporality / Sequence)**

  * clock ticks
  * instruction step count
  * pipeline/retire progression
* **Φ (Recontextualization)**

  * interrupts
  * traps and exceptions
  * context switch into handlers
* **Χ (Distance / Isolation)**

  * hardware-enforced isolation:

    * MMU boundaries
    * virtualization layers
    * sandboxed execution modes
* **Σ (Integration / Commit)**

  * atomic memory updates
  * transaction commit (if supported)
  * pipeline retirement points
* **Ψ (Self-Binding / Policy)**

  * hardware invariants:

    * no write to read-only frames
    * no execution of non-executable frames
  * architectural policies enforced before/after each instruction

This ensures PMS-CPU is literally a **Δ–Ψ-shaped hardware abstraction**.

---

### 2.1.8 PMS-CPU as a PMS-UM Instance

To tie it back to 1.x:

* **S**:

  * (s = (s_c,; f,; r,; P,; m))
  * with (s_c) specialized to registers + memory.
* **Γ**:

  * bytes/words (instruction + data alphabet).
* **F**:

  * frame table identifiers (code, data, stack, kernel, etc.).
* **R**:

  * role/privilege modes encoded via SR.
* **PSet**:

  * architectural policies (e.g. memory safety, privilege constraints).
* **Inst**:

  * PMS-CPU ISA instruction set (to be defined in 2.2), each tagged with an op ∈ O.

Execution:

* **Fetch–Decode–Execute** = one small-step of PMS-UM, with:

  * Δ dominating fetch/decode,
  * ∇, □, Ω, Θ, … implementing the actual behavior,
  * Ψ gating allowed transitions.

---

### 2.1.9 Summary

In 2.1 we have:

* Specialized PMS-UM state into a **CPU-like** structure (registers, memory, PC, frames, roles).
* Aligned each **PMS operator** with explicit CPU-level semantics.
* Defined a high-level **memory and privilege model** that naturally supports:

  * an OS kernel on top (section 3),
  * a type-safe runtime and language compilation target (9, 10),
  * and formal reasoning via PMS-UM semantics.

Next, we can detail the actual **Instruction Set Architecture**:

> **2.2 Instruction Set Architecture (ISA)**
> – define concrete instructions grouped by Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ.

---

## 2.2 Instruction Set Architecture (ISA)

We now define a **PMS-CPU instruction set** where **every instruction is explicitly tagged by one PMS operator**:

[
\text{Instr} = (\text{mnemonic},; \text{op} \in O,; \text{operands},; \text{constraints})
]

Semantics of each instruction are inherited from **1.2 Instruction Semantics by Operator**; here we give the **syntactic families** and how they map to Δ…Ψ.

We’ll structure this as:

* 2.2.1 General conventions (addresses, registers)
* 2.2.2 Δ-family (distinction / compare / branch)
* 2.2.3 ∇-family (ALU, moves, memory, IO)
* 2.2.4 □-family (frames / context)
* 2.2.5 Λ-family (timeouts / non-events)
* 2.2.6 Α-family (patterns / macros)
* 2.2.7 Ω-family (roles / privilege)
* 2.2.8 Θ-family (time / sequencing)
* 2.2.9 Φ-family (exceptions / traps / reframe)
* 2.2.10 Χ-family (isolation / sandbox)
* 2.2.11 Σ-family (commit / integration)
* 2.2.12 Ψ-family (policy / invariants)

This is a **minimal but expressive** ISA; we can extend with variants later.

---

### 2.2.1 General Conventions

**Operands:**

* `Rn` – general-purpose register (R0..R7, say)
* `[addr]` – memory at effective address `addr`
* `FR` – frame register
* `SP` – stack pointer
* `PC` – program counter
* `SR` – status register
* `imm` – immediate (small constant)
* `fid` – frame id
* `role` – role identifier
* `cap` – capability identifier
* `pol` – policy id
* `ctx` – context id (for isolation or traps)
* `label` – code label (PC-relative target)

**Addressing:**

* `Rn` – register direct
* `[Rn]` – memory at address in Rn
* `[FR+Rn]` – frame-relative access (base from FR, offset via Rn)
* `[FR+imm]` – frame-relative immediate offset

We won’t define bit-level encoding yet (that’s 2.5), just the abstract op families.

---

### 2.2.2 Δ-Family — Distinction / Compare / Branch

**Operator tag:** Δ

Δ instructions **inspect** state and set flags or change PC based on distinctions, without changing core data (except flags).

1. **Compare registers**

```asm
CMP   Rdst, Rsrc      ; Δ – compare Rdst with Rsrc, set SR flags (Z,N,…) 
```

2. **Compare register with immediate**

```asm
CMPI  Rdst, imm       ; Δ – compare Rdst with imm
```

3. **Test bits / mask**

```asm
TST   Rdst, Rsrc      ; Δ – bitwise test, set flags
TSTI  Rdst, imm       ; Δ
```

4. **Conditional branches (using SR flags set by previous Δ)**

```asm
BEQ   label           ; Δ – branch if Z=1
BNE   label           ; Δ – branch if Z=0
BGT   label           ; Δ – branch if >  (signed)
BLT   label           ; Δ – branch if <  (signed)
BGE   label           ; Δ – branch if ≥
BLE   label           ; Δ – branch if ≤
```

5. **Unconditional branch (as degenerate Δ)**

```asm
JMP   label           ; Δ – pure control distinction: next PC = label
```

6. **No-op distinction**

```asm
NDIF                  ; Δ – “neutral distinction”; does nothing but counts as Δ for deps/history
```

All of these:

* Mutate only SR (flags) and PC.
* Provide the **decision backbone** for the machine.

---

### 2.2.3 ∇-Family — Impulse / ALU / Moves / Memory / IO

**Operator tag:** ∇

∇ instructions **change state**: registers, memory, PC (for calls/returns), and optionally external IO.

#### (A) Data movement

```asm
MOV   Rdst, Rsrc      ; ∇ – move register to register
MOVI  Rdst, imm       ; ∇ – load immediate
LOAD  Rdst, [FR+Rn]   ; ∇ – load from frame-relative addr
STORE [FR+Rn], Rsrc   ; ∇ – store to frame-relative addr
```

#### (B) Arithmetic & logical ops

```asm
ADD   Rdst, Rsrc      ; ∇ – Rdst := Rdst + Rsrc
ADDI  Rdst, imm       ; ∇
SUB   Rdst, Rsrc      ; ∇
MUL   Rdst, Rsrc      ; ∇
DIV   Rdst, Rsrc      ; ∇ (or fault via Φ on div-by-zero)

AND   Rdst, Rsrc      ; ∇
OR    Rdst, Rsrc      ; ∇
XOR   Rdst, Rsrc      ; ∇
NOT   Rdst            ; ∇
SHL   Rdst, imm       ; ∇
SHR   Rdst, imm       ; ∇
```

(Flags updated via Δ-typed semantics internally; but op-tag remains ∇ because main effect is mutation.)

#### (C) Stack & control transfers

```asm
PUSH  Rsrc            ; ∇ – SP := SP - sz; MEM[SP] := Rsrc
POP   Rdst            ; ∇ – Rdst := MEM[SP]; SP := SP + sz

CALL  label           ; ∇ – push return addr, set PC := label
RET                   ; ∇ – pop return addr into PC
```

#### (D) IO operations

```asm
IN    Rdst, port      ; ∇ – read from IO port
OUT   port, Rsrc      ; ∇ – write to IO port
```

All ∇ instructions:

* Must have a Δ ancestor (dependency): they act on something distinguished.
* Are the **only normal way** to modify core state.

---

### 2.2.4 □-Family — Frame / Context Instructions

**Operator tag:** □

These change **which frame / context** is active, not the underlying memory contents.

1. **Enter frame**

```asm
FRM_ENTER  fid        ; □ – set FR := fid, switch memory/exec frame
```

2. **Leave frame (restore)**

```asm
FRM_LEAVE             ; □ – restore previous FR from frame stack in meta m
```

3. **Set frame base from register**

```asm
FRM_SET   FR, Rsrc    ; □ – associate FR with base address in Rsrc (plus metadata)
```

4. **Frame-local call/return (optional sugar)**

```asm
FRM_CALL  fid, label  ; □ – switch to frame fid, then CALL label
FRM_RET                ; □ – return + restore previous frame
```

All □ ops:

* Must be preceded by Δ (which frame?).
* Constrain subsequent ∇, Ω, Θ, Φ, Σ to the new frame.

---

### 2.2.5 Λ-Family — Non-Event / Timeouts / Idle

**Operator tag:** Λ

These are **semantically meaningful no-events**, like timeouts or blocking waits.

1. **Wait with timeout**

```asm
WAIT  cond_reg, timeout_reg    ; Λ – block until cond met or timeout
```

* Uses Θ to advance time.
* If condition not met by timeout: Λ path taken (non-event).

2. **Poll**

```asm
POLL  cond_reg                  ; Λ – check once, if not ready, branch or set flag
```

3. **Semantic no-op**

```asm
NOP_SEM code                    ; Λ – no-op with semantic tag (idle, backoff, etc.)
```

Λ instructions:

* Don’t alter core data.
* Only meta-state (time, pending flags, traces) and possibly PC (branch).

---

### 2.2.6 Α-Family — Attractor / Pattern, Macro Instructions

**Operator tag:** Α

Attractor instructions represent **macro-patterns** of primitive ops.

1. **Pattern call**

```asm
PATTERN   pid                ; Α – invoke pre-defined pattern with id pid
```

2. **Parameterized pattern**

```asm
PATTERN   pid, Rarg0, Rarg1  ; Α – pattern with arguments
```

3. **Looped pattern**

```asm
LOOP_P    pid, count_reg     ; Α – repeat pattern pid count_reg times
```

Semantically:

* At **compile-time**, PATTERN/LOOP_P may be expanded into Δ/∇/□/Θ sequences.
* Or at runtime, Α expands into an instruction micro-sequence (in meta m).

Constraints:

* The expanded pattern must be a **valid PMS word** (respect 0.3 deps).

---

### 2.2.7 Ω-Family — Role / Privilege / Capability Instructions

**Operator tag:** Ω

These govern **who can do what**, not the work itself.

1. **Set role / mode**

```asm
SET_ROLE  role          ; Ω – change SR.mode / r to new role (if allowed)
```

2. **Check capability**

```asm
CHK_CAP   cap, label_fail  ; Ω – if capability cap not in CapSet(r), Δ-branch to fail
```

3. **Enter privileged section**

```asm
ENTER_PRIV  level       ; Ω – elevate to privileged level (e.g. on syscall/trap entry)
EXIT_PRIV                ; Ω – drop back to previous level
```

These:

* Don’t (normally) modify user-visible core data.
* Gate access to frames, devices, special instructions.
* Are heavily constrained by Ψ (architecture invariants).

---

### 2.2.8 Θ-Family — Temporality / Time / Ordering

**Operator tag:** Θ

These encode **time and ordering** beyond simple sequential semantics.

1. **Tick**

```asm
TICK                    ; Θ – increment time counters in meta m
```

2. **Sleep**

```asm
SLEEP   ticks           ; Θ – advance time, skip execution until ticks elapsed (may combine with Λ)
```

3. **Barrier / fence (temporal ordering)**

```asm
FENCE                   ; Θ – ordering point: no reordering of loads/stores across this
```

4. **Yield (cooperative scheduling hint)**

```asm
YIELD                   ; Θ – give scheduler hint to switch context (later kernel will bind semantics)
```

Θ instructions:

* Provide the **explicit temporal backbone** used later by scheduling and memory consistency.

---

### 2.2.9 Φ-Family — Recontextualization / Exceptions / Traps

**Operator tag:** Φ

These instructions trigger or manage **context shifts** due to errors, interrupts, or deliberate re-interpretation.

1. **Raise exception**

```asm
EXC_RAISE   code           ; Φ – signal exception with code, jump to handler context
```

2. **Install exception handler**

```asm
EXC_SET     table_ptr      ; Φ – set exception handler table (frame, role dependent)
```

3. **Trap (explicit context switch into system space)**

```asm
TRAP        code           ; Φ – synchronous trap; typically user → kernel
```

4. **Return from exception / trap**

```asm
EXC_RET                      ; Φ – restore frame, role, PC, SR from handler context 
```

5. **Reframe execution context (e.g. version / mode shift)**

```asm
REFRAME    ctx              ; Φ – change interpretation (e.g. new ABI, version)
```

Φ ops:

* Operate on frames, roles, policies, meta.
* Reinterpret or transfer control, but preserve underlying state (possibly after structured transformation).

---

### 2.2.10 Χ-Family — Isolation / Sandbox / Subcontexts

**Operator tag:** Χ

Χ instructions enforce or manipulate **isolation boundaries**.

1. **Fork isolated context**

```asm
ISO_FORK   ctx              ; Χ – create isolated context ctx from current state subset
```

2. **Enter isolated context**

```asm
ISO_ENTER  ctx              ; Χ – switch execution into isolated context
```

3. **Exit isolated context**

```asm
ISO_EXIT                    ; Χ – return to parent context
```

4. **Restrict access**

```asm
ISO_RESTRICT  mask          ; Χ – narrow visible frames/devices according to mask
```

Internally:

* Use □ (frames) + Ω (roles) + Ψ (policies) to enforce **“you can’t touch that”**.
* Are foundational for OS-level processes, containers, VMs.

---

### 2.2.11 Σ-Family — Integration / Commit / Atomicity

**Operator tag:** Σ

Σ instructions mark **integration points**: commit partial changes into a coherent state.

1. **Transaction begin/end** (optional advanced feature)

```asm
TX_BEGIN                  ; Σ – mark start of transactional region
TX_COMMIT                 ; Σ – attempt commit; on success, make all writes visible
TX_ABORT                  ; Σ – rollback to pre-begin state
```

2. **Atomic read-modify-write**

```asm
ATOMIC_ADD [FR+Rn], Rsrc  ; Σ – atomic integration of Rsrc into memory cell
ATOMIC_CAS [FR+Rn], Rcmp, Rnew  ; Σ – compare-and-swap
```

3. **Barrier with commit semantics**

```asm
COMMIT_BARRIER            ; Σ – flush pending writes, ensure consistency
```

These are crucial for:

* concurrency correctness,
* filesystem and transactional semantics later (4.3),
* and for proving invariants (Ψ) about consistent states.

---

### 2.2.12 Ψ-Family — Policy / Invariant / Governance Instructions

**Operator tag:** Ψ

These instructions are the **architectural “governance” interface**: they define and check invariants.

1. **Set policy**

```asm
SET_POL   pol_id, Rcfg      ; Ψ – install/update policy pol_id with config from Rcfg
```

2. **Check policy**

```asm
CHK_POL   pol_id, label_fail  ; Ψ – if policy violated in current state, branch or trap
```

3. **Global policy check (implicit or explicit)**

```asm
CHK_ALL_POL                  ; Ψ – evaluate all policies; may trap/EXC_RAISE on violation
```

4. **Policy-induced halt**

```asm
HALT_IF_POL  pol_id          ; Ψ – halt machine if policy pol_id says “unsafe to continue”
```

Ψ ops:

* Must not be bypassable by user-level code where they protect critical invariants.
* Are the link between **architecture** and **safety model** (and later, kernel & governance, sections 3 and 8).

---

### 2.2.13 ISA Summary (by PMS Operator)

Quick table:

| PMS Op | Example ISA families                            | Main structural role               |
| ------ | ----------------------------------------------- | ---------------------------------- |
| Δ      | CMP, TST, BEQ/BNE/…, JMP, NDIF                  | Distinction & branching            |
| ∇      | MOV, LOAD/STORE, ALU ops, CALL/RET, IN/OUT      | State-changing actions             |
| □      | FRM_ENTER/LEAVE/SET, FRM_CALL/RET               | Frame/context management           |
| Λ      | WAIT, POLL, NOP_SEM                             | Non-events, timeouts, idle         |
| Α      | PATTERN, LOOP_P                                 | Pattern/macro expansion            |
| Ω      | SET_ROLE, CHK_CAP, ENTER_PRIV, EXIT_PRIV        | Roles, privilege, asymmetry        |
| Θ      | TICK, SLEEP, FENCE, YIELD                       | Time, ordering, scheduling hook    |
| Φ      | EXC_RAISE, EXC_SET, TRAP, EXC_RET, REFRAME      | Exceptions, traps, recontextualize |
| Χ      | ISO_FORK, ISO_ENTER, ISO_EXIT, ISO_RESTRICT     | Isolation/sandbox control          |
| Σ      | TX_BEGIN/COMMIT/ABORT, ATOMIC_*, COMMIT_BARRIER | Integration, atomicity, commit     |
| Ψ      | SET_POL, CHK_POL, CHK_ALL_POL, HALT_IF_POL      | Policies, invariants, governance   |

This ISA is:

* **rich enough** to implement a full kernel, OS, language runtime,
* still **PMS-clean**: every instruction lives in exactly one operator class,
* and fits directly into the PMS-UM semantics from section 1.

---

## 2.3 Calling Conventions (functions, stack, registers)

We now define a **canonical PMS-CPU calling convention** – how functions, syscalls, and traps:

* pass arguments & return values
* use registers vs stack
* create & destroy stack frames (□)
* interact with privilege (Ω) and policy (Ψ)

Everything is **PMS-typed**: each step is a small sequence of Δ, ∇, □, Θ, Φ, Σ operations at the ISA level defined in 2.2.

We’ll cover:

1. 2.3.1 Design goals (Δ–Ψ view)
2. 2.3.2 Register classification
3. 2.3.3 Stack frame layout
4. 2.3.4 Normal function call/return protocol
5. 2.3.5 Tail calls & leaf functions
6. 2.3.6 System call / trap calling convention
7. 2.3.7 Reentrancy, recursion & Ψ invariants
8. 2.3.8 Summary

---

### 2.3.1 Design Goals (Δ–Ψ view)

The calling convention is designed to:

* Be **PMS-aligned**:

  * Frames (□) = stack frames + address spaces
  * Roles (Ω) = user vs kernel vs other modes
  * Policies (Ψ) = enforce safe calling & returning
  * Integration (Σ) = commit return values at call boundaries
* Support:

  * recursion
  * reentrancy
  * tail calls
  * clean user ↔ kernel transitions (Φ+Ω+Χ)
* Be **simple enough** to reason about at PMS-UM level, but realistic enough for OS/runtime.

We’ll assume:

* 8 general-purpose registers: `R0..R7`
* Special regs: `PC, SP, FR, SR` as in 2.1

(Exact counts can be tuned later; convention scales.)

---

### 2.3.2 Register Classification

We partition registers structurally:

#### General-purpose GPRs

* **Argument / return registers (caller-visible)**

  * `R0` – primary return value
  * `R1` – secondary return (optional; e.g. hi part or errno)
  * `R0..R3` – argument registers (ARG0..ARG3)

* **Caller-saved**

  * `R0..R3` are **caller-saved**:

    * If the caller cares about their values across a call, it must save them.

* **Callee-saved**

  * `R4..R7` are **callee-saved**:

    * A function must preserve them:

      * either not touch them,
      * or save/restore them in its frame.

This division supports:

* fast calls for up to 4 small arguments
* predictable save/restore rules.

#### Special registers

* `PC` – program counter
* `SP` – stack pointer, always points to **top of current stack frame** area in current frame (□).
* `FR` – current memory frame (address space / segment)
* `SR` – status & mode bits (flags, role, etc.)

PMS mapping:

* Δ distinguishes register roles.
* □ uses `FR` + `SP` to define call frame context.
* Ω uses mode bits in `SR` to encode privilege/role.

---

### 2.3.3 Stack Frame Layout (□ = function frame)

Each call allocates a **stack frame** in the current stack frame (□). We assume a downward-growing stack (addresses decrease as we push).

Conceptual layout (higher addresses at top):

```text
+-------------------------+  high addresses
| Caller’s frame          |
| ...                     |
+-------------------------+
| Arg spill area (caller) |  optional, outgoing args beyond R0..R3
+-------------------------+
| Return address (PC)     |
| Saved SR (optional)     |
| Saved FR (optional)     |
| Saved R4..R7 (callee-saved regs)
+-------------------------+  <-- SP after prolog
| Local variables / temps |
| Spill slots             |
+-------------------------+  low addresses
```

**Key invariants:**

* At any call boundary, there is a **well-defined frame** (□):

  * `FR` selects the stack’s memory region
  * `SP` marks the current frame top
* Callee treats its frame as **private**; caller only touches its own frame + outgoing arg area (for the callee).

This directly realizes □: each function call **creates a new sub-frame**, and `SP` bounds that frame.

---

### 2.3.4 Normal Function Call/Return Protocol

We define a **canonical calling sequence** in PMS-ISA terms.

#### 2.3.4.1 Call-site (caller) sequence

To call `foo(a, b, c, d, e, ...)`:

1. **Prepare arguments in registers** (∇)

   ```asm
   ; assume a,b,c,d in R0..R3, e in R4
   MOV   R0, Ra     ; ∇
   MOV   R1, Rb     ; ∇
   MOV   R2, Rc     ; ∇
   MOV   R3, Rd     ; ∇
   ```

2. **Spill extra arguments to stack if needed** (∇)

   ```asm
   PUSH  Re         ; ∇ – extra arg
   ; further extras: PUSH Rf, ...
   ```

3. **Optional capability / policy checks before calling** (Δ + Ω + Ψ)

   ```asm
   ; e.g., ensure we’re allowed to call foo
   CHK_CAP  CAP_CALL_FOO, label_fail   ; Ω + Δ
   ```

4. **Call the function** (∇ with underlying Δ to set return address)

   ```asm
   CALL  foo_label  ; ∇ – pushes return PC, jumps
   ```

5. **Post-call cleanup** (caller’s responsibility for outgoing stack args)

   ```asm
   ADDI  SP, SP, n_args_extra*WORD_SIZE  ; ∇ – pop extra args
   ```

6. **Read return value(s)** from `R0` (and `R1` if applicable).

Operator view:

* Argument setup: ∇
* Distinctions/capability: Δ/Ω
* Transfer: ∇ (with underlying Δ for target PC)
* Return value: integrated at call boundary (Σ conceptually; see below).

#### 2.3.4.2 Callee prolog

At label `foo_label`:

1. **Establish new call frame (□ + ∇)**

   ```asm
   PUSH  R4         ; ∇
   PUSH  R5         ; ∇
   PUSH  R6         ; ∇
   PUSH  R7         ; ∇
   ; optional: PUSH SR, FR if they must be preserved

   ; allocate locals
   SUBI  SP, SP, frame_size_locals   ; ∇ – create space for locals
   ```

   This sequence:

   * transforms the stack into a new □ frame for this function.
   * saves callee-saved registers to keep caller’s context intact.

2. **(Optional) Set a dedicated frame register for locals** (□)

   ```asm
   FRM_SET  FR, SP   ; □ – treat current SP region as this function’s frame
   ```

   This offers a structural mapping:

   * `FR` selects **this function’s lexical frame**; locals/temps accessed as `[FR+offset]`.

3. **Initialize locals / spill args as needed** (∇)

   ```asm
   STORE [FR+0], R0    ; ∇ – save arg0 as local, etc.
   ```

#### 2.3.4.3 Callee body

* Use `R0..R3` for arguments/temps.
* Use `R4..R7` for long-lived locals (since they are callee-saved).
* Use stack frame locals at `[FR+offset]` or via `SP` relative.

All internal computations are **plain ∇/Δ/Θ** operations.

#### 2.3.4.4 Callee epilog

Before returning:

1. **Place return value in `R0` (and `R1` if needed)**

   ```asm
   MOV  R0, Rresult   ; ∇
   ```

2. **Deallocate locals & restore callee-saved registers** (∇)

   ```asm
   ADDI SP, SP, frame_size_locals  ; ∇ – drop locals

   POP  R7        ; ∇
   POP  R6        ; ∇
   POP  R5        ; ∇
   POP  R4        ; ∇
   ; optional: POP FR, POP SR if they were saved
   ```

3. **Return to caller** (∇ + Σ-ish integration)

   ```asm
   RET             ; ∇ – pop PC from stack, jump
   ```

Semantically, we can view **RET** as having a Σ-flavor:

* it **integrates** the callee’s work into the caller’s state:

  * core data (globals, heap, memory updates) remain visible
  * register and stack contexts are restored to the caller’s frame
  * return registers (R0, R1) are the *committed result* of the call

You could model this more formally as:

* ∇ for PC restoration
* Σ for “commit return value + restore caller frame”

but at ISA level we keep a single mnemonic.

---

### 2.3.5 Tail Calls & Leaf Functions

To support efficient functional & systems code, we define tail call and leaf optimizations structurally.

#### 2.3.5.1 Leaf functions

A **leaf function** does not call other functions (no nested calls). For these:

* It may **skip saving/restoring callee-saved registers** entirely if it doesn’t use `R4..R7`.
* It can treat `R0..R3` as its only working set and use stack only for large locals.

Simplified prolog/epilog:

```asm
; prolog: maybe allocate locals only
SUBI SP, SP, frame_size_locals     ; ∇

; ... body ...

ADDI SP, SP, frame_size_locals     ; ∇
RET                                ; ∇
```

#### 2.3.5.2 Tail calls (call in tail position)

When a function ends with `return g(args...)` and does not need its own frame afterward, we can:

* **reuse the current frame**:

  * don’t restore callee-saved regs (we’re not returning to original caller)
  * don’t emit RET
  * just prepare args and JMP to `g`:

```asm
; tail position inside f
MOV   R0, Rarg0    ; ∇   ; prep args for g
...
JMP   g_label      ; Δ   ; jump, do not change stack frame
```

PMS structuring:

* This is a **Φ-like recontextualization** if you think of “this activation is now g”.
* But at ISA level it’s pure Δ + ∇: we merely branch and reuse □ and Ω context.

---

### 2.3.6 System Call / Trap Calling Convention

Syscalls are calls that cross a **role boundary**: from USER → KERNEL (Ω) via a **trap** (Φ).

We define:

* `TRAP code` (Φ) instruction as the canonical syscall entry.
* Kernel side adheres to a parallel calling convention.

#### 2.3.6.1 User-side syscall ABI

To perform a syscall:

1. **Place syscall number and arguments into registers**:

   * `R0` – syscall number
   * `R1..R3` – syscall arguments 0..2
   * additional args on stack (like normal calls)

   ```asm
   MOVI  R0, SYS_WRITE       ; ∇ – syscall number
   MOV   R1, Rfd             ; ∇ – arg0
   MOV   R2, Rbuf            ; ∇ – arg1
   MOV   R3, Rlen            ; ∇ – arg2
   ```

2. **Issue trap**:

   ```asm
   TRAP  #0                  ; Φ – enter kernel, code 0 = syscall vector
   ```

3. **On return**, result is in `R0` (and `R1` maybe for errno etc.).

The user-space sees this as a function that:

* takes arguments in `R1..R3` (+ stack),
* returns a value in `R0`,
* but actually goes through Ω+Φ+Χ/Ψ boundaries.

#### 2.3.6.2 Kernel trap handler convention

Inside kernel trap handler for syscall:

* It runs under **KERNEL role** (Ω).

Typical entry sequence (in kernel’s Φ handler):

1. **Save pre-trap context** (□ + Χ)

   ```asm
   ; in trap entry stub (privileged)
   PUSH  R4..R7          ; ∇
   PUSH  FR, SR, PC      ; ∇
   ; switch to kernel stack frame / FR_K
   FRM_ENTER  FR_K       ; □
   ; switch role to KERNEL
   SET_ROLE  ROLE_KERNEL ; Ω
   ```

2. **Interpret syscall arguments**:

   * `R0` = syscall number, `R1..R3` = args.

3. **Dispatch to syscall implementation**:

   ```asm
   ; Δ – distinguish syscall number
   CMPI  R0, SYS_WRITE   ; Δ
   BEQ   sys_write       ; Δ
   ...
   ```

4. **Syscall implementation** uses **same calling convention** internally:

   * arguments still in `R1..R3`, etc.
   * returns value in `R0`.

5. **On kernel exit**:

   * restore user context
   * drop role back to USER
   * return via `EXC_RET` (Φ):

   ```asm
   SET_ROLE  ROLE_USER       ; Ω
   FRM_LEAVE                  ; □ – restore user frame/stack
   EXC_RET                    ; Φ – restore PC, SR, etc. to user context
   ```

This cleanly:

* uses Ω to encode role asymmetry,
* uses Φ for trap/return recontextualization,
* uses Χ/□ for isolation of kernel memory and stack.

From PMS-UM viewpoint:

* A syscall is a Δ-identified function call that triggers a Φ-context shift and Ω-role escalation, then Σ-commits results on EXC_RET.

---

### 2.3.7 Reentrancy, Recursion & Ψ Invariants

The calling convention must support:

* **Recursion**:

  * Each call allocates its own □ stack frame via `SP` adjustments.
  * PMS ensures there’s no structural limit besides memory & Ψ policies (e.g. max stack depth).
* **Reentrancy**:

  * Interrupts (Φ) or signals may cause **nested entries** into handlers.
  * Handler uses **its own frame** (□), possibly its own kernel stack (Χ) and role (Ω).

We define **core invariants (Ψ)** for calling conventions:

1. **Frame well-formedness**:

   * For any active function:

     * its frame is contiguous
     * SP and FR are consistent
     * saved registers are restored exactly once

2. **Register preservation rules**:

   * Callee must restore all callee-saved registers (`R4..R7`, SR bits that must be preserved).
   * Caller must not assume any particular values of caller-saved registers after call.

3. **Cross-role safety** (for traps/syscalls):

   * Kernel must never return with:

     * user role still having kernel capabilities
     * user frames pointing into kernel memory

   Enforced via Ψ policies on `SET_ROLE`, `FRM_ENTER/LEAVE`, `EXC_RET`.

4. **Non-interference between frames** (Χ + Ψ):

   * A function’s private stack frame cannot be accessed by other concurrent contexts except via explicit sharing mechanisms later defined.

These Ψ invariants are checked:

* statically by tools (section 11),
* dynamically by minimal runtime checks in privileged context (e.g. debug builds, safe modes).

---

### 2.3.8 Summary

We’ve defined a **PMS-native calling convention** where:

* Functions use:

  * `R0..R3` for arguments and returns,
  * `R4..R7` as callee-saved,
  * `SP` + `FR` to define stacked frames (□),
  * `CALL` / `RET` as ∇-typed control transfers with Σ-commit flavor for results.

* Syscalls use:

  * `TRAP` (Φ) + `SET_ROLE` (Ω) to cross user/kernel boundaries,
  * `EXC_RET` (Φ) to recontextualize back to user-land.

* Ψ invariants ensure:

  * stack/frame integrity,
  * privilege safety,
  * clean integration of recursive, re-entrant, and tail-call semantics.

  ---

## **2.4 Interrupt & Trap Model (external events → Φ/Λ)**

This section formalizes *all* asynchronous and synchronous event-handling in PMS-CPU using the PMS operator algebra.
It covers:

* **Interrupts** → asynchronous external events
* **Traps** → synchronous control transfers into privileged mode
* **Faults / exceptions** → errors in execution
* **Timeouts / non-events** → Λ
* **Recontextualization** → Φ (core mechanism)
* **Stack / frame transitions** → □
* **Role switching** → Ω
* **Policy gates** → Ψ
* **Isolation boundaries** → Χ

This gives the complete PMS semantics of low-level event delivery, handler dispatch, and return paths.

---

# **2.4.1 Structural Overview (Φ + Λ + Ω + □)**

Every event in PMS-CPU enters execution through one of two operators:

### **Φ (Recontextualization)**

Used for:

* hardware interrupts
* traps (syscalls, privileged instructions, breakpoints)
* faults/exceptions
* context-frame reinterpretation

Φ *always* implies:

1. Change of execution context (□)
2. Potential role elevation (Ω)
3. New interpretation of the state (Φ semantics)
4. Policy checks (Ψ) to validate the transition

### **Λ (Non-event / absence / timeout)**

Used for:

* timer expiry
* expected event not occurring
* wait timeouts
* idle loop handling

Λ does **not** change core context by itself — it signals “something that should have happened did *not* happen”.

Together, Φ and Λ define the entire event model of PMS-CPU.

---

# **2.4.2 Event Sources**

We classify events structurally:

## **(A) Asynchronous events → Φ**

External hardware stimuli:

* IRQ lines (timer, network, disk, devices)
* Inter-processor interrupts (if multicore introduced later)
* External signals (debugger attach, suspend, power events)

Represented as Φ because:

* They *recontextualize* execution: “stop what you were doing; do *this* now”.

## **(B) Synchronous traps → Φ**

Generated by the CPU while executing an instruction:

* `TRAP` instruction (syscall entry)
* privileged instruction in user mode
* breakpoints (`BRK`)
* explicit `EXC_RAISE`

## **(C) Faults / exceptions → Φ**

CPU-detected errors:

* page faults (□ violation)
* capability/privilege violations (Ω violation)
* arithmetic faults (divide-by-zero)
* misaligned access
* illegal opcode (Δ fails to classify decode)

These are Φ because they require reinterpretation of the current state (exception context).

## **(D) Non-events → Λ**

Timeout or missing events:

* waiting for message / I/O
* timer expires without expected event
* scheduler idle/no runnable threads

These produce Λ but may subsequently cause a Φ (e.g., timeout → trap to scheduler).

---

# **2.4.3 Interrupt Vector Table (IVT) — a Δ-indexed Φ dispatch**

We define a **vector table** stored in a privileged frame:

```
IVT[0]  = address of reset handler
IVT[1]  = address of timer interrupt handler
IVT[2]  = address of device 0 interrupt
IVT[3]  = address of device 1 interrupt
...
IVT[n]  = syscall trap handler
```

Mechanically:

1. Hardware interrupt provides an **interrupt number** `irq`.
2. A Δ distinction is performed:

```asm
CMPI R_irq, irq      ; Δ
JMP  [IVT + irq]     ; Δ – branch into handler
```

**Vectoring = pure Δ**, handler entry = Φ.

---

# **2.4.4 Φ Entry Protocol (General Handler Entry)**

All Φ-type events (interrupts, traps, faults) use *one* structural pattern:

### **Steps of Φ entry**

#### **(1) Save interrupted context (∇ + □)**

PMS-CPU must preserve user-space or lower-privilege execution:

```asm
PUSH PC         ; ∇
PUSH SR         ; ∇
PUSH FR         ; ∇
PUSH R4..R7     ; ∇   ; callee-saved
```

This implicitly creates a new **exception frame** (□).

#### **(2) Switch role/mode (Ω)**

```asm
SET_ROLE ROLE_KERNEL       ; Ω
```

This enforces:

* capability rules for privileged execution
* isolation of kernel state

If a trap from kernel occurs, Ω may keep or change role according to Ψ.

#### **(3) Switch to kernel stack / frame (□)**

```asm
FRM_ENTER FR_KERNEL_STACK  ; □
```

This isolates kernel from user stack:

* user stack cannot be trusted (Χ)
* kernel must run with stable frame

#### **(4) Install exception context metadata (Φ + m)**

Meta-state gets:

* cause code (irq number, trap code, fault code)
* saved PC/SR
* exception depth level

#### **(5) Transfer control to handler (Δ)**

```asm
JMP handler_address   ; Δ
```

Handler executes with full CPU privileges.

---

# **2.4.5 Handler Execution Semantics**

Handlers run in a **privileged □ frame** with:

* Ω = kernel role
* FR = kernel frame
* Unrestricted access to privileged instructions
* Policies Ψ checked continuously

Handlers may:

* acknowledge interrupt sources
* perform I/O
* schedule next processes (Θ)
* modify system state

Handlers may **not** violate Ψ invariants:

Examples:

* must not re-enter user mode with inconsistent SP or FR
* must restore caller context in a balanced way
* must respect isolation (Χ)

---

# **2.4.6 Return-from-Interrupt / Trap (Φ Exit)**

Exiting handler uses:

```asm
EXC_RET    ; Φ
```

### **EXC_RET does:**

1. Check Ψ policies

   * role must be downgraded if returning to user
   * stack frame validity
   * no kernel state leaked

2. Restore frame (□):

```asm
FRM_LEAVE
```

3. Restore role (Ω):

```asm
SET_ROLE ROLE_USER
```

4. Restore registers & PC (∇):

```asm
POP R7..R4
POP FR
POP SR
POP PC
```

### **Result:**

Execution resumes *exactly* where interrupted unless handler requested modification (e.g. PC rewrite for signal injection).

---

# **2.4.7 Nested Interrupts (Multi-level Φ)**

Because Φ is compositional, PMS-CPU supports nested exceptions.

Rules:

1. **SR.flags.interrupt_enable** determines if other interrupts may preempt this handler.
2. If allowed:

   * New Φ entry occurs
   * A new exception frame (□) is pushed
   * Exception depth in `m` increments
3. Ψ may restrict max nesting depth to avoid stack exhaustion.

This is structurally identical to:

```
Φ( Φ( Φ( state ) ) )
```

Each layer is its own □ frame + Ω context.

---

# **2.4.8 Faults, Traps, and Syscalls (Φ variants)**

### **Synchronous trap (syscall)**

Triggered by:

```asm
TRAP #code     ; Φ
```

Call sequence described in 2.3:

* Arguments in registers
* Kernel receives them in handler
* Uses EXC_RET to return

### **Faults / exceptions**

Examples:

| Fault condition            | PMS operator | Handler type |
| -------------------------- | ------------ | ------------ |
| page fault / invalid frame | □ violation  | Φ            |
| privilege violation        | Ω violation  | Φ            |
| division by zero           | ∇ error      | Φ            |
| illegal opcode             | Δ failure    | Φ            |

Handler may:

* terminate offending process
* reframe the context (Φ)
* apply policies (Ψ)
* restore or retry instruction

### **Breakpoints/debug traps**

Generated via:

```asm
BRK     ; Φ
```

Handled similarly to trap.

---

# **2.4.9 Timeouts and Non-Events (Λ)**

Λ is used when *expected* event does **not** occur in time.

Typical use:

### Example: waiting for I/O

```asm
WAIT R_status, R_timeout    ; Λ
```

Semantics:

* Θ increments time counters
* If device ready: return normally
* If timeout expires → Λ triggered

Λ may propagate into a Φ-based scheduler trap:

```
Λ → Φ_scheduler
```

Where scheduler evaluates runnable tasks and may switch context.

This gives PMS-CPU:

* Polling-free asynchronous I/O
* Reactive time-based execution
* Unified timeout behavior across kernel and user contexts

---

# **2.4.10 Isolation (Χ) and Interrupts**

Interrupts must respect isolation boundaries:

### Rule:

If CPU is executing inside an isolated context:

```
Χ = active
```

Then Φ entry semantics are restricted:

1. Interrupt handler may **not** access isolated state unless explicitly allowed by Ψ
2. Isolation metadata is preserved across Φ entry
3. A return path (`EXC_RET`) must not violate the isolation constraints

This is the basis for:

* sandboxed execution
* secure enclaves
* process isolation in kernel (later in section 3)

---

# **2.4.11 Interrupt Priorities and Θ (Temporal Ordering)**

We incorporate priorities into Θ:

* Θ defines scheduling and ordering
* Interrupt priority determines handler ordering if multiple Φ are pending
* Higher-priority interrupts preempt lower-priority ones if:

```
SR.flags.interrupt_enable && priority(high) > priority(current)
```

Handler execution timing is tracked in `m.time` (Θ).

This means:

* time progresses explicitly
* order of Φ events is a partial order controlled by Θ + Ψ

---

# **2.4.12 Summary of PMS Interrupt/Trap Semantics**

| Phenomenon          | PMS Operator(s) | Meaning                           |
| ------------------- | --------------- | --------------------------------- |
| Interrupt           | Φ               | Asynchronous context switch       |
| Trap (syscall)      | Φ + Ω           | Controlled role elevation         |
| Fault/exception     | Φ               | Reinterpretation of invalid state |
| Timeout / non-event | Λ               | Expected event absent             |
| Return from handler | Φ + Σ           | Merge state + restore context     |
| Isolation rules     | Χ + Ψ           | Restrict access during/after Φ    |
| Priority / timing   | Θ               | Temporal ordering of events       |

The Φ/Λ model gives PMS-CPU a **complete and unified** event architecture.

---

## 2.5 Binary Encoding (opcode formats, immediates)

We now give a **concrete binary encoding** for PMS-CPU instructions — a mapping from the abstract ISA (2.2) to fixed-width bit patterns.

Design goals:

* Keep it **simple & orthogonal** enough to reason about.
* Make **PMS operator tags (Δ…Ψ) explicit** in the encoding.
* Allow enough space for:

  * opcodes
  * registers
  * immediates
  * PMS metadata (frame/role/policy hints where needed).

Think of this as a “reference encoding”; actual hardware can extend or tweak it as long as the **Δ–Ψ labeling and structural semantics** stay intact.

---

### 2.5.1 Word Size & Endianness

We choose:

* **Instruction width:** fixed **32-bit** words.
* **Address granularity:** byte-addressed memory.
* **Endianness for data:** **little-endian** (LSB at lowest address) — but this is *convention*, not structurally essential.

Instruction fetch uses FR (code frame) and PC:

* PC increments in units of 4 bytes per instruction (unless branch / jump).

---

### 2.5.2 Top-Level Instruction Layout

We reserve **4 bits** for the **PMS operator tag**, so the decoder can directly see which Δ…Ψ class an instruction belongs to.

Generic 32-bit layout:

```text
31           28 27          22 21      16 15       10  9        0
+---------------+--------------+----------+----------+-----------+
| PMS_OP (4)    | OPCODE (6)   | RD (6)   | RS1 (6)  | PAYLOAD   |
+---------------+--------------+----------+----------+-----------+
```

* `PMS_OP` (4 bits): encodes which Δ…Ψ operator class (0..10 used, rest reserved).
* `OPCODE` (6 bits): subopcode within that operator family.
* `RD` / `RS1` (6 bits each): register specifiers or special IDs.
* `PAYLOAD` (10 bits): interpreted per format:

  * second source register
  * small immediate
  * part of larger immediate / offset
  * control flags, etc.

Because we have different needs per instruction type, we define **formats** that reuse and reinterpret these fields.

---

### 2.5.3 PMS Operator Tag Encoding

We assign each PMS operator a **tag ID**:

```text
PMS_OP (4 bits)
0000  Δ  (Difference / Distinction)
0001  ∇  (Impulse / Enactment)
0010  □  (Frame / Context)
0011  Λ  (Non-Event / Absence)
0100  Α  (Attractor / Pattern)
0101  Ω  (Asymmetry / Role)
0110  Θ  (Temporality / Sequence)
0111  Φ  (Recontextualization)
1000  Χ  (Distance / Isolation)
1001  Σ  (Integration / Commit)
1010  Ψ  (Self-Binding / Policy)
1011–1111  reserved
```

**Invariant:**

* Every valid instruction word has exactly one PMS_OP tag.
* The **decoder’s first action (Δ)** is to read PMS_OP and dispatch to the appropriate semantic family.

---

### 2.5.4 Register Encoding

We use **5 bits** for registers (`0..31`), but earlier we conceptually used 8 GPRs. This gives us headroom:

* `R0–R7`   – general-purpose registers (as in 2.3).
* `R8–R15`  – reserved / future GPR expansion.
* `R16–R23` – system / special registers (PC, SP, FR, SR, etc.), or alias fields.
* `R24–R31` – reserved for future or implementation-specific uses.

For simplicity in this spec:

* We **logically** treat PC, SP, FR, SR as *special registers*, not addressed via the 5-bit GPR namespace in the high-level ISA.
* In the binary encoding, some instructions may encode operations on PC/SP/FR/SR using reserved register codes or implicit behavior (e.g. CALL/RET).

We’ll call the register fields:

* `rd` – destination register (5 bits).
* `rs1`, `rs2` – source registers (5 bits each).

We’ll adjust the generic layout to 32 bits accordingly.

---

### 2.5.5 Concrete Instruction Formats

We define **4 canonical formats** that cover all PMS-CPU instructions:

* **R-type** — register + register (ALU etc.)
* **I-type** — register + small immediate
* **B-type** — branch/jump with offset
* **S-type** — system / special (Φ, Χ, Ψ, etc.)

#### 2.5.5.1 R-type (Register–Register)

For ALU, basic moves, some compare ops:

```text
31     28 27   22 21   17 16   12 11   7 6   0
+---------+-------+-------+-------+------+-----+
| PMS_OP  | OPC   |  rd   |  rs1  | rs2  |fun2|
+---------+-------+-------+-------+------+-----+
```

* `PMS_OP` (4): Δ, ∇, etc.
* `OPC` (6): subopcode within operator class.
* `rd` (5), `rs1` (5), `rs2` (5).
* `fun2` (7): minor function bits (e.g. shift type, flags).

Example (∇ ADD):

* PMS_OP = `0001` (∇)
* OPC = `000001` (ADD)
* rd = dest register
* rs1, rs2 = sources
* fun2 = 0

#### 2.5.5.2 I-type (Register–Immediate)

For small immediates (e.g., ADDI, MOVI, LOAD spilled, etc.):

```text
31     28 27   22 21   17 16   12 11           0
+---------+-------+-------+-------+-------------+
| PMS_OP  | OPC   |  rd   |  rs1  |  imm12      |
+---------+-------+-------+-------+-------------+
```

* `imm12` – **12-bit immediate**, sign-extended or zero-extended depending on `OPC`.

Example (∇ ADDI):

* PMS_OP = `0001` (∇)
* OPC = `000010` (ADDI)
* rd = dest
* rs1 = base
* imm12 = constant

#### 2.5.5.3 B-type (Branch / Jump)

For control transfers with PC-relative offsets:

```text
31     28 27   22 21   17 16                        0
+---------+-------+-------+--------------------------+
| PMS_OP  | OPC   |  rs1  |       off17             |
+---------+-------+-------+--------------------------+
```

* `rs1` – register used for condition (or zero if not used).
* `off17` – **17-bit signed offset**, multiplied by 4 (word-aligned).
* For unconditional `JMP`, rs1 is ignored.

Example (Δ BEQ):

* PMS_OP = `0000` (Δ)
* OPC = `000101` (BEQ)
* rs1 = condition flag or register index
* off17 = branch displacement

We can also use **two registers** for comparisons by encoding the compare as a preceding Δ (CMP) and BEQ/NE etc. look at SR flags.

#### 2.5.5.4 S-type (System / Φ/Χ/Ψ/Ω/□/Σ)

For system-level instructions with small codes, roles, frame IDs, etc.:

```text
31     28 27   22 21   17 16   12 11           0
+---------+-------+-------+-------+-------------+
| PMS_OP  | OPC   |  rs1  |  rs2  |  sys12      |
+---------+-------+-------+-------+-------------+
```

* `sys12` – 12-bit subfield encoding:

  * trap/exception code (`TRAP`, `EXC_RAISE`),
  * role ID (`SET_ROLE`),
  * frame ID (`FRM_ENTER`, `FRM_SET`),
  * capability ID (`CHK_CAP`, etc.),
  * policy ID (`SET_POL`, `CHK_POL`).

`rs1` and `rs2` can:

* be real registers (e.g., pointer to handler table, policy config),
* or be special register selectors (e.g., 31 = SP, 30 = FR, etc.) in an extended encoding.

---

### 2.5.6 Encoding by PMS Operator Family

Now we map the abstract ISA (2.2) into these formats and opcodes.

I’ll sketch the key representatives; the full table is conceptually straightforward.

---

#### 2.5.6.1 Δ — Distinction / Comparisons / Branches

**PMS_OP = 0000**

Representative opcodes:

* `OPC = 000000` → `CMP rd, rs1, rs2` (R-type)
* `OPC = 000001` → `CMPI rd, rs1, imm12` (I-type)
* `OPC = 000010` → `TST rd, rs1, rs2` (R-type)
* `OPC = 000011` → `TSTI rd, rs1, imm12` (I-type)
* `OPC = 000100` → `JMP off17` (B-type, rs1 ignored)
* `OPC = 000101` → `BEQ off17` (B-type, uses SR.Z)
* `OPC = 000110` → `BNE off17`
* `OPC = 000111` → `BGT off17` (uses SR flags)
* … etc.
* `OPC = 001111` → `NDIF` (S-type; no effect beyond history/trace).

Semantics: as in 2.2; only SR and PC change.

---

#### 2.5.6.2 ∇ — ALU / Moves / Memory / Control

**PMS_OP = 0001**

Examples:

* ALU (R-type):

  * `OPC = 000000` → `ADD rd, rs1, rs2`
  * `OPC = 000001` → `SUB rd, rs1, rs2`
  * `OPC = 000010` → `MUL rd, rs1, rs2`
  * `OPC = 000011` → `DIV rd, rs1, rs2`
  * `OPC = 000100` → `AND rd, rs1, rs2`
  * `OPC = 000101` → `OR  rd, rs1, rs2`
  * `OPC = 000110` → `XOR rd, rs1, rs2`
  * `OPC = 000111` → `NOT rd, rs1` (rs2 ignored)

* Immediate variants (I-type):

  * `OPC = 001000` → `ADDI rd, rs1, imm12`
  * `OPC = 001001` → `MOVI rd, imm12` (rs1 ignored)

* Memory (I-type):

  * `OPC = 010000` → `LOAD rd, [FR + rs1 + imm12]`
  * `OPC = 010001` → `STORE [FR + rs1 + imm12], rs2` (rd unused)

* Stack & control (S-type with implicit SP/PC):

  * `OPC = 011000` → `PUSH rs1` (rd ignored; sys12 encodes size)
  * `OPC = 011001` → `POP rd`
  * `OPC = 011010` → `CALL off17` (B-like; pushes return PC; PC += off17)
  * `OPC = 011011` → `RET` (S-type, sys12=0; pops PC)

* IO:

  * `OPC = 100000` → `IN rd, port` (`port` from imm12)
  * `OPC = 100001` → `OUT port, rs1`

All with PMS semantics from 1.2.

---

#### 2.5.6.3 □ — Frames / Context

**PMS_OP = 0010**

Mostly S-type:

* `OPC = 000000` → `FRM_ENTER fid`:

  * `sys12` = frame ID.
  * rs1, rs2 ignored.

* `OPC = 000001` → `FRM_LEAVE`:

  * use frame stack in meta-state `m`.

* `OPC = 000010` → `FRM_SET FR, rs1`:

  * FR base address in `rs1`.
  * `sys12` may include permissions/type code.

* `OPC = 000011` → `FRM_CALL fid, off17` (optional sugar):

  * combine `FRM_ENTER` + `CALL`.

All these **don’t mutate data**, only frame context and PC.

---

#### 2.5.6.4 Λ — Non-Events / Wait / Idle

**PMS_OP = 0011**

Typical encodings (I- or S-type):

* `OPC = 000000` → `WAIT rs1, rs2`:

  * `rs1` – condition/status register.
  * `rs2` – timeout register index (or special encoding).
  * `sys12` – wait mode (blocking/non-blocking).

* `OPC = 000001` → `POLL rs1`:

  * quick check; sets SR.Z if ready, else not.

* `OPC = 000010` → `NOP_SEM code`:

  * `sys12` = semantic code (idle, backoff, etc.).

These only update meta (`m`, time) and possibly PC for fallback branch.

---

#### 2.5.6.5 Α — Patterns / Macros

**PMS_OP = 0100**

Encoded as S-type with pattern ID:

* `OPC = 000000` → `PATTERN pid`:

  * `sys12` = pattern ID.

* `OPC = 000001` → `PATTERN pid, rs1, rs2`:

  * pattern receives register arguments.

* `OPC = 000010` → `LOOP_P pid, rs1`:

  * repeat pattern `pid` `rs1` times.

At decode time, an implementation can:

* **expand** Α into internal micro-ops (Δ/∇/□/…), or
* treat Α as a macro step with its own micro-sequence.

---

#### 2.5.6.6 Ω — Role / Privilege / Capability

**PMS_OP = 0101**

S-type:

* `OPC = 000000` → `SET_ROLE role`:

  * `sys12` = role ID.
  * modifies SR.mode / r.

* `OPC = 000001` → `CHK_CAP cap, off17`:

  * `sys12` = capability ID.
  * If capability missing → branch by `off17` (B-like or trap).
  * Or trap via Φ depending on design (e.g., `CHK_CAP` mismatches raise Φ).

* `OPC = 000010` → `ENTER_PRIV level`

* `OPC = 000011` → `EXIT_PRIV`

These modify SR.mode / CapSet(r) but not core data.

---

#### 2.5.6.7 Θ — Time / Ordering

**PMS_OP = 0110**

Examples:

* `OPC = 000000` → `TICK`:

  * increments time in meta `m`.

* `OPC = 000001` → `SLEEP imm12`:

  * param = number of ticks.

* `OPC = 000010` → `FENCE`:

  * memory ordering barrier; may involve Σ-like micro operations.

* `OPC = 000011` → `YIELD`:

  * hint to scheduler (Θ+Ψ at kernel level).

Encoding uses I- or S-type; data fields minimal.

---

#### 2.5.6.8 Φ — Exceptions / Traps / Reframe

**PMS_OP = 0111**

All S-type:

* `OPC = 000000` → `TRAP syscode`:

  * `sys12` = syscall/trap code (e.g., syscall vector).
  * triggers Φ entry protocol (2.4) in hardware/kernel.

* `OPC = 000001` → `EXC_RAISE code`:

  * `sys12` = exception code; similar to TRAP but semantically “error”.

* `OPC = 000010` → `EXC_SET table_ptr`:

  * `rs1` = register with pointer to exception handler table.

* `OPC = 000011` → `EXC_RET`:

  * no operands; returns from handler (Φ exit).

* `OPC = 000100` → `REFRAME ctx`:

  * `sys12` = context ID (e.g. new ABI version); updates f/r/P meta.

---

#### 2.5.6.9 Χ — Isolation / Sandbox

**PMS_OP = 1000**

S-type:

* `OPC = 000000` → `ISO_FORK ctx`:

  * `sys12` = isolated context ID.

* `OPC = 000001` → `ISO_ENTER ctx`

* `OPC = 000010` → `ISO_EXIT`

* `OPC = 000011` → `ISO_RESTRICT mask`:

  * `sys12` = bitmask of allowed frames/devices.

Internally these update isolation metadata in `m` and related frame/role restrictions.

---

#### 2.5.6.10 Σ — Integration / Commit

**PMS_OP = 1001**

R- or S-type:

* `OPC = 000000` → `TX_BEGIN`:

  * marks transactional region in `m`.

* `OPC = 000001` → `TX_COMMIT`:

  * merges speculative writes into visible state.

* `OPC = 000010` → `TX_ABORT`:

  * rolls back to pre-TX state.

* `OPC = 000011` → `ATOMIC_ADD [FR+rs1+imm12], rs2`:

  * I-type variant; Σ semantics at memory cell.

* `OPC = 000100` → `ATOMIC_CAS [FR+rs1+imm12], rs2, rd`:

  * R+I hybrid but encoded with I-type plus function bits.

* `OPC = 000101` → `COMMIT_BARRIER`:

  * full commit barrier.

---

#### 2.5.6.11 Ψ — Policy / Invariants / Governance

**PMS_OP = 1010**

S-type:

* `OPC = 000000` → `SET_POL pol_id, rs1`:

  * `sys12` = policy id,
  * `rs1` = register containing pointer/config blob.

* `OPC = 000001` → `CHK_POL pol_id, off17`:

  * branch / trap if policy violated.

* `OPC = 000010` → `CHK_ALL_POL`:

  * evaluate all active policies.

* `OPC = 000011` → `HALT_IF_POL pol_id`:

  * induces Ψ-based halting state if policy demands.

Ψ instructions often only affect:

* P (policy set),
* m (audit logs, counters),
* and potentially ip if they cause trap/halt.

---

### 2.5.7 Encoding of Special Registers & System State

There are two main options:

1. **Implicit semantics** for some instructions:

   * `CALL`/`RET` use PC and SP implicitly.
   * `PUSH`/`POP` always operate on SP.
   * `EXC_RET` uses hidden exception frame stack.

2. **Explicit encoding** via reserved register IDs:

   * e.g. `rs1 = 31` means “SP”, `rs1 = 30` means “PC”, etc.

For this spec, we choose:

* **Implicit** for core control / stack instructions (CALL, RET, PUSH, POP, EXC_*).
* **Explicit** for FR and SR when needed via dedicated instructions:

  * `FRM_SET` uses a normal GPR as pointer/base.
  * `SET_ROLE` modifies SR.mode implicitly.

This keeps code size down and preserves structural clarity.

---

### 2.5.8 Invalid Encodings & Ψ/Δ Guards

Not every 32-bit pattern is valid:

* Some combinations of `PMS_OP + OPC` are unused → **illegal instruction**.
* Even valid opcodes may be **disallowed** by:

  * current role (Ω),
  * active policies (Ψ),
  * frame constraints (□).

We define:

* Illegal opcode detection as a Δ failure:

  * “cannot classify this 32-bit word as a valid instruction”.

This yields a **Φ fault**:

* EXC: illegal instruction,
* trapped into kernel handler.

Policy Ψ can further forbid certain encodings (e.g. use of TX instructions in user mode) and trigger traps/halt.

---

### 2.5.9 Example Encodings (Concrete Bitstrings)

Just to make it tangible, here’s a small example assuming:

* `R1 = 00001`, `R2 = 00010`, `R3 = 00011`, `R0 = 00000`.

1. `ADD R1, R2, R3`:

* PMS_OP = ∇ = 0001
* OPC (ADD) = 000000
* rd = 00001
* rs1 = 00010
* rs2 = 00011
* fun2 = 0000000

Binary:

```text
0001 000000 00001 00010 00011 0000000
```

2. `TRAP #2`:

* PMS_OP = Φ = 0111
* OPC = 000000 (TRAP)
* rs1, rs2 = 00000
* sys12 = 000000000010 (2)

Binary:

```text
0111 000000 00000 00000 000000000010
```

3. `SET_ROLE ROLE_KERNEL (id 1)`:

* PMS_OP = Ω = 0101
* OPC = 000000
* sys12 = 000000000001

```text
0101 000000 00000 00000 000000000001
```

These are not meant to be final encodings, but they show the shape: **PMS operator tag at top, then subopcode, then operands/payload.**

---

### 2.5.10 Summary

Section 2.5 gave:

* A **32-bit fixed encoding** for PMS-CPU instructions.
* A **4-bit PMS_OP tag** that makes Δ…Ψ semantics explicit at decode time.
* A set of **instruction formats (R/I/B/S)** mapped to each operator family.
* Concrete **OPC conventions** for major instructions (ALU, branches, traps, frames, roles, policies, transactions, isolation).

This lets us:

* Write real machine code for PMS-CPU.
* Feed PMS-CPU binaries into simulators and verification tools (section 11).
* Cleanly relate binary programs back to operator-typed PMS-UM semantics.

---

## **2.6 PMS-CPU Execution Model (Fetch–Decode–Execute)**

The purpose of 2.6 is to show **how the PMS-CPU actually runs machine code** under Δ–Ψ rules, integrating:

* the **monoid constraints** (0.3)
* the **operator-typed ISA** (2.2)
* the **binary encoding** (2.5)
* the **interrupt/trap model** (2.4)

This is the PMS-CPU’s analogue of the classical *FDE cycle*, except here the decode phase produces a *PMS operator-typed control decision*.

---

# **2.6.1 High-Level Cycle**

Every hardware time step `Θ` drives a *bounded deterministic transition*:

[
(s, PC) ;\xrightarrow{\Theta + \Delta + \text{op}} (s', PC')
]

The full PMS-CPU cycle is:

1. **Θ-Step (Temporal progress)**
2. **Δ-Fetch (Load instruction word under frame FR)**
3. **Δ-Decode (Classify PMS_OP, OPC)**
4. **Ω/Ψ Pre-Check (Capabilities + Policies)**
5. **□ Context Binding (Frame apply)**
6. **Execute operator-specific transition (∇, Λ, Φ, Χ, Σ, etc.)**
7. **Σ / Commit (if operator requires)**
8. **PC update (Δ, Θ, Φ rules)**
9. **Interrupt/Trap check → Φ branch**

Each step has formally defined partial transition functions.

---

# **2.6.2 Step 1 — Θ: Hardware Temporal Step**

The CPU’s global temporal driver is Θ.

At the beginning of each cycle:

[
m \gets T_\Theta(m)
]

Typical updates in meta-state `m`:

* tick counters
* deadline counters
* pipeline timers
* pending Λ signals (if some channel expired)

This step creates the **temporal expectation context** used later by Λ (timeouts) and scheduling logic.

---

# **2.6.3 Step 2 — Δ-Fetch**

The PMS-CPU loads the next 32-bit instruction word from memory, under frame FR:

[
\text{instr} = \text{Mem}[FR.code_base + PC]
]

The action belongs to **Δ**, because it is a *distinction-producing read*:

* Does not alter `s_c`.
* Sets classification flags in `SR` (status register):

  * illegal/valid bit
  * alignment bit
  * exception / trap flags

If fetch fails (address violation → Χ, no-permission → Ω, or illegal frame m), control immediately shifts to **Φ: trap path** (2.4).

---

# **2.6.4 Step 3 — Δ-Decode**

Δ identifies:

* `PMS_OP` = top 4 bits
* `OPC` = subopcode
* format = R/I/B/S

This sets an internal decoded instruction object:

[
I = (\text{op}, \text{opcode}, \text{format}, \text{operands}, \text{payload})
]

This decouples binary representation from PMS semantics.

If PMS_OP does not map to Δ…Ψ → illegal → **Φ trap**.

No state mutation except:

* update meta m.hist to record Δ.
* register SR.decode_ok.

---

# **2.6.5 Step 4 — Ω / Ψ Pre-Check**

Before executing operator op, PMS-CPU performs a composite structural validation:

## **A. Ω-role/capability validation**

[
\Omega(s, I) = \text{true} \quad\text{iff role } r \text{ permits op}
]

Examples:

* ∇ STORE is forbidden in user mode → trap via Φ.
* Φ TRAP may be allowed in user mode.
* Σ TX_COMMIT allowed only in privileged role.
* Χ ISO_FORK only allowed in isolated-creator role.

## **B. Ψ-policy validation**

[
\Psi(s, I) = \text{true} \quad\text{iff active policies P allow op}
]

Examples:

* Policies can ban certain syscalls.
* Policies can enforce memory bounds stricter than Ω.
* Policies can forbid isolated contexts to change frame FR.

If validation fails → **Φ(exception)**.

---

# **2.6.6 Step 5 — □ Frame Binding**

Before the operator executes, the CPU binds effective frame(s):

* code frame (FR_code)
* data frame (FR_data)
* stack frame (SP frame)
* isolation frame (Χ mask)
* transactional frame (Σ overlays)

This produces a *context bundle*:

[
f^* = \mathit{BindFrame}(f, m, r)
]

which is then passed to the operator’s post-function.

Key property: **□ never mutates core data**, only the interpretation domain.

---

# **2.6.7 Step 6 — Execute Operator Semantics (∇…Ψ)**

Now the instruction family executes according to its op tag.

---

## **Case Δ (Distinction)**

* Reads but does not write.
* Updates SR.flags (Z, N, C, V, type bits).
* Produces branch decision for B-type instructions.
* PC may change (cond. branches).

---

## **Case ∇ (Impulse)**

* Primary state mutation:

[
s_c' = A_\nabla(s_c, f^*, r, \text{operands})
]


Examples:

* ALU write
* LOAD / STORE
* PUSH / POP
* CALL / RET
* IO operations

If STORE, roles/policies may require capability checks → possibly branch to Φ.

---

## **Case □ (Frame)**

* Updates f and/or frame stack.
* Does not mutate s_c.
* E.g., FRM_ENTER, FRM_LEAVE.
* PC = PC + 1 normally.

---

## **Case Λ (Non-Event)**

* Evaluates whether expected event occurred (based on m).
* If not, executes fallback or sets flags.
* Does not mutate s_c.
* Often branches based on timeout conditions.

---

## **Case Α (Attractor)**

Two strategies:

### **Static expansion (preferred for hardware):**

Α is expanded at decode time into micro-ops Δ/∇/□/Θ.

### **Dynamic runtime expansion:**

Inject mini-instruction-sequence into pipeline from pattern memory.

Either way, Α itself is not a primitive state transition — it triggers **execution of a valid PMS sub-word**.

---

## **Case Ω (Asymmetry)**

* Mutates r (role).
* Possibly sets capability bits.
* Must always be allowed by Ψ and Ω (higher role can restrict itself).
* Never mutates s_c directly.

---

## **Case Θ (Temporality)**

* Increments local counters, deadlines.
* Possibly issues memory FENCE.
* Does not mutate s_c except through memory-order synchronization.

---

## **Case Φ (Recontextualization / Trap)**

Two paths:

1. **From normal instructions (explicit TRAP, EXC_RAISE)**
2. **From failure of Ω/Ψ/Χ/Δ checks (implicit trap)**

Φ saves a *trap frame*:

* old PC
* registers
* frame context
* meta-state

Then:

* switches frame f to handler frame
* sets PC = handler_addr
* updates role r if privileged handler
* sets exception code in SR

Φ **does not lose the past**; it reframes it structurally.

---

## **Case Χ (Isolation)**

* Create or enter isolated context.
* Restrict accessible frames.
* Change meta-state to “isolated” mode.
* Possibly map/duplicate memory segments (copy-on-write behavior).

---

## **Case Σ (Integration / Commit)**

* Merge buffered/transactional writes into visible memory.
* Conclude isolation or transactional frames.
* Clear pending write logs.
* Update m to mark integrated state.

---

## **Case Ψ (Policy)**

Either:

* defines/updates policy set P, or
* enforces policy check (may halt).

Ψ is the only operator that may **transition into a halting configuration** based on invariant rules.

---

# **2.6.8 Step 7 — Σ Commit Phase (If Required)**

Many instructions produce:

* temporary ALU results
* deferred writes
* speculative values (in transactions)
* isolation overlays

A Σ micro-phase may be inserted automatically when needed.

Examples:

* After ∇ STORE (if in transactional mode)
* After frame migration
* After exception handler exit (Φ→Σ)

Σ ensures the machine always moves forward through a **consistent state**.

---

# **2.6.9 Step 8 — PC Update**

PC is updated according to op class:

* Normal: `PC = PC + 4`
* Branch (Δ B-type):
  `PC = PC + (off << 2)`
* CALL:
  pushes return PC; sets PC = target
* RET:
  pops PC
* EXC_RAISE / TRAP:
  PC = handler address (from Φ preconfigured table)
* EXC_RET:
  PC restored from trap frame
* HALT (Ψ):
  PC = HALT; CPU enters S_H

---

# **2.6.10 Step 9 — Interrupt/Trap Check (Deferred Φ)**

At the *end* of the cycle, the CPU checks:

* pending external interrupts
* pending internal faults
* timer interrupts
* isolation violations
* transactional abort signals
* policy violations detected asynchronously

If any are pending and enabled:

→ **Φ trap entry** executed *before* next instruction fetch.

Thus interrupts behave as **asynchronous Φ events**.

---

# **2.6.11 Pipelined (“Out-of-Order”) View (Optional)**

If PMS-CPU is superscalar:

* Δ-fetch and Δ-decode proceed in separate stages.
* Ω/Ψ checks may occur early (during decode).
* Χ/Σ may enforce reorder barriers (Θ FENCE).
* Policy Ψ can globally restrict reordering (e.g. no speculative loads across certain boundaries).

Still, the architectural semantics remain exactly the same as the sequential version.

---

# **2.6.12 Formal Execution Relation**

The PMS-CPU defines a deterministic transition relation:

[
(s, PC) \xrightarrow{\text{CPU}} (s', PC')
]

where the CPU-step is:

[
\Theta ;\circ; \Delta_{fetch} ;\circ; \Delta_{decode} ;\circ;
(\Omega \land \Psi)*{check} ;\circ; \square*{bind} ;\circ;
op_{execute} ;\circ; \Sigma_{auto} ;\circ; PC_{update} ;\circ; \Phi_{interrupt}
]

All operators are composed in the PMS-valid order, matching dependency constraints from section 0.3:

* Δ precedes any ∇ or control
* Ψ/Ω constrain ∇
* Φ can wrap any operator
* Σ occurs after ∇/Θ
* Χ constrains access
* and so on.

---

# **2.6.13 Summary**

The PMS-CPU execution model is not a classical FDE cycle — it is a **PMS-typed operator pipeline**, where each instruction’s behavior is determined by its **operator tag** (Δ…Ψ) and the structural constraints of PMS.

This model yields:

* explicit semantics for privilege, isolation, and policy,
* structural time (Θ) integrated into execution,
* recontextualization (Φ) as first-class trap semantics,
* integration (Σ) as mandatory commit semantics,
* and full compatibility with PMS-UM semantics.

---

## **2.7 PMS Memory Consistency Model**

This section defines how the PMS-CPU orders **LOAD/STORE** and other memory-affecting operations **under the PMS operator algebra**, not under ad-hoc hardware rules.
Because the ISA is operator-typed, each PMS operator produces **structural ordering guarantees** that combine to form a full consistency model.

The result is a memory model that is:

* simple to define,
* extremely expressive,
* equivalent in power to TSO/RC11/etc when instantiated,
* but fundamentally grounded in Δ–Ψ.

---

# **2.7.1 Memory Operations in PMS Terms**

Memory reads and writes are modeled as:

* **Δ (Difference)**
  → reads from memory; classification; branch conditions.
  → never mutates memory.

* **∇ (Impulse)**
  → writes to memory or registers; causes mutation of core state.
  → also includes LOAD (read from memory into register)
  *because LOAD mutates the register file*, it is ∇.

* **Σ (Integration)**
  → commit/writeback/finalization of buffered, speculative, or transactional writes.

* **□ (Frame)**
  → modifies address space, memory view, isolation domain.
  → does not modify memory itself but changes interpretation.

* **Θ (Temporality)**
  → provides ordering steps; fences; sequencing constraints.

* **Χ (Isolation)**
  → restrict or re-scope memory visibility; create isolated regions.

* **Ψ (Policy)**
  → forbid / constrain ordering relationships; impose invariants.

This is enough to fully define memory consistency without any architecture-specific special rules.

---

# **2.7.2 Fundamental Ordering Dimensions**

The PMS consistency model is defined by **three orthogonal structural axes**:

### **Axis A — Operator Intrinsic Ordering (Δ→∇→Σ)**

This ordering is forced by dependency constraints:

* Δ must precede ∇
  *You cannot write or interpret a write target without Δ somewhere upstream*

* ∇ must precede Σ
  *Σ integrates only after ∇ has produced intermediate states*

Thus the fundamental micro-order is:

[
\Delta \prec \nabla \prec \Sigma
]

This is **unbreakable** and defines the minimal consistency skeleton.

---

### **Axis B — Temporal Ordering (Θ)**

Θ enforces:

[
\Theta \prec { \nabla, \Delta, \Lambda, \Sigma }
]

and can also act as:

* a **barrier** (Θ_FENCE)
* a **clock-step**
* a **synchronization tick**

Thus Θ defines a **happens-before** relation:

[
\Theta \Rightarrow HB(\text{next cycle})
]

Equivalent to “cycle boundaries” in classical CPUs — except here it is operator-defined.

---

### **Axis C — Isolation & Frame Ordering (Χ, □)**

Χ produces **visibility domains**:

* what memory writes can be seen by which contexts
* when isolation enters or leaves

Frames (□) structure this further:

* Σ may commit into only *some* frames
* Δ/∇ may see either the isolated or global view

So:

[
\Chi \Rightarrow \text{visibility-scope boundary}
]

This is like MESI/VM isolation/NUMA boundaries — unified in one operator.

---

# **2.7.3 Baseline Consistency Guarantees (PMS-SC)**

**Sequential Consistency** in PMS means:

> *All operators appear to execute in a total order consistent with each thread’s program order, respecting Δ/∇/Σ/Θ/□/Χ/Ψ constraints.*

This is the simplest and strongest model.

Program order is exactly the PMS operator monoid ordering.

[
(\Delta \prec \nabla \prec \Sigma \prec \Theta \prec \Phi)
]

---

# **2.7.4 Relaxed Consistency — Structural Relaxations**

The key insight:
**PMS does not need to “invent” relaxations — relaxations follow from relaxing operator dependencies.**

For example:

### **Relaxation Type R1: Out-of-Order Δ (Speculative Reads)**

If Ψ allows Δ to be evaluated **before** earlier ∇ is finalized, Δ can “speculate”.

This mimics:

* TSO speculative loads
* ARM/POWER early loads
* weak memory models

### **Relaxation Type R2: Delayed Σ (Write Buffering)**

Σ may be delayed due to Θ or Ψ constraints:

* represent store buffers
* reorder stores w.r.t later Δ

Equivalent to:

* x86 store buffer
* TSO store→load reordering
* release/acquire-split semantics

### **Relaxation Type R3: Frame-based Reordering (□-switch)**

If two regions reside in **separate frames** and no Ψ forbids reordering, ordering constraints may be relaxed:

* per-object consistency
* per-region consistency
* NUMA-like models

### **Relaxation Type R4: Isolation-based Reordering (Χ)**

If an isolated context owns its own view:

* writes inside isolation aren’t visible until Σ release
* loads don’t see global writes until merge
* isolation boundaries provide natural atomic sections

Equivalent to:

* transactions
* memory protection domains
* process-level isolation

---

# **2.7.5 Memory Barrier / Fence Semantics (Θ_FENCE)**

Θ can be instantiated as:

* **full memory fence**
* **acquire**
* **release**
* **acq_rel**
* **seq_cst fence**
* **I/O fence**

This is architecturally defined by:

[
\Theta_{\text{FENCE}} :
\text{forbid reordering across boundary}
]

This operator-level definition is strictly simpler than ad-hoc hardware rules.

---

# **2.7.6 Happens-Before (HB) Relation in PMS**

Define HB as the minimal transitive closure of:

1. **Program Order** (monoid sequence):
   [
   op_i \prec op_j
   ]

2. **Temporal Order** (Θ steps):
   [
   \Theta_i \Rightarrow HB(\text{next cycle})
   ]

3. **Commit Visibility** (Σ):
   [
   \nabla_i \prec \Sigma_i \Rightarrow \text{visible after } \Sigma_i
   ]

4. **Isolation Boundaries** (Χ):

   * Writes inside Χ-subcontext only become globally visible after:
     [
     \Chi\text{-exit} ;\circ; \Sigma
     ]

5. **Policy Constraints** (Ψ):

   * Ψ may enforce extra HB edges (e.g., seq_cst mode).
   * Ψ may forbid some reorderings (e.g., memory safety invariants).

---

# **2.7.7 Example: Implementing Hardware TSO in PMS**

TSO = *writes appear in program order; loads may bypass pending stores; load-load ordered; store-store ordered; store-load reordered.*

In PMS:

* **Write buffering** = delayed Σ
* **Load bypass** = speculative Δ
* **Acquire/Release fences** = Θ_FENCE
* **Store→Load reorder** permitted when Δ is allowed before Σ by Ψ policy
* **Store-store order** guaranteed because:
  [
  \Sigma\text{ pipeline flush preserves store order}
  ]

This is purely operator-driven — no special memory model machinery.

---

# **2.7.8 Example: Implementing ARMv8 Weak Model**

ARM allows:

* Load→Load reorder
* Load→Store reorder
* Store→Load reorder
* Store→Store reorder (except dependencies)

Use PMS configuration:

* Δ may occur before prior Δ/∇ unless forbidden by Θ_FENCE
* Σ commit delayed aggressively
* Data dependencies forced by Ψ policies
* Release/acquire barriers = Θ_FENCE(REL) and Θ_FENCE(ACQ)

Again, PMS operators reproduce ARM’s model exactly.

---

# **2.7.9 Example: Strong Transactional Memory**

Χ (isolation) + Σ (commit) + Ψ (atomicity policy):

* writes inside Χ-subcontext are uncommitted until Σ
* if a conflict is detected, Φ abort → rollback via Ψ
* visibility atomicity encoded by HB(Σ_exit)

This naturally implements HTM (Intel TSX), STM, and database-style ACID semantics.

---

# **2.7.10 Example: Language-Level Memory Models (C++/Java)**

PMS provides operator-level primitives that match language-level memory constructs:

| Language Concept   | PMS Operator(s)                   |
| ------------------ | --------------------------------- |
| seq_cst            | Ψ + Θ_FENCE(full)                 |
| acquire            | Θ_FENCE(acquire)                  |
| release            | Θ_FENCE(release)                  |
| relaxed            | Δ/∇ without fences, governed by Ψ |
| atomic read/write  | ∇ under Ω capability restrictions |
| atomic RMW         | ∇ + Σ commit region               |
| publication safety | Σ + Ψ ordering                    |

Thus PMS-CPU can implement a safe runtime for PMSL and foreign languages.

---

# **2.7.11 Summary**

The PMS memory consistency model is:

* **not bolt-on** but **a direct consequence** of operator algebra.
* Δ/∇/Σ give the minimal ordering.
* Θ enforces cycle barriers, fences, sequencing.
* Χ and □ define visibility scopes and isolation.
* Ψ defines invariant-based ordering constraints.

This yields a **single unified model** covering:

* classical SC
* TSO
* ARM / POWER
* transactional memory
* capability-based access
* process-level isolation
* language-level atomics

with no contradictions and no extra machinery.

---

# **3. PMS-OS Kernel Core**

## **3.1 Kernel Goals & Trust Model (Ψ)**

The PMS-OS Kernel is the **minimal privileged subsystem** defined over PMS-CPU that:

1. Mediates *all* transitions involving
   **Ω (roles)**, **□ (frames)**, **Χ (isolation)**, **Φ (traps)**, and **Ψ (policies)**.
2. Enforces in-kernel **global invariants** (Ψ-level rules).
3. Provides **safe, isolated, predictable execution contexts** for user processes.
4. Defines system services (IPC, scheduling, memory, I/O) using PMS operators.

Everything the kernel does is reducible to:

* **Ω**: controlling *who* is allowed to execute which operations,
* **□**: controlling *where* (context/frame) operations occur,
* **Χ**: controlling *which memory / resources* are visible or isolated,
* **Φ**: controlling *how* traps, faults, and syscalls recontextualize control,
* **Ψ**: enforcing *global commitments* that must hold across time.

We now formalize that as a **trust model**.

---

# **3.1.1 Kernel Trust Boundary (Χ + Ω + □)**

The kernel is the **root context** in which:

* role = `KERNEL` or `SUPERVISOR`
* frame = kernel frame KF
* isolation = none or minimal (Χ = “global domain”)

Define:

[
Context_{kernel} = (f = KF,, r \in {KERNEL,SUPERVISOR},, Χ = global)
]

From this context, the kernel may:

* create / destroy isolated user frames (□ + Χ)
* set role transitions (Ω)
* install or update Ψ policies
* handle Φ traps
* perform Σ commits over global state

**User processes** must *never* enter Context_{kernel} except via Φ trap (“syscall”) or via Ψ-controlled transitions, and must leave via Φ return.

This is the kernel trust boundary.

---

# **3.1.2 Kernel Global Invariants (Ψ)**

These are the **Ψ-level commitments** that the PMS-OS kernel guarantees to enforce.
They are expressed as operator constraints, not English rules.

Let (P_{kernel}) be the kernel’s global policy set.

### **Invariant Ψ₁ — Capability correctness (Ω-consistency)**

For any state s:

[
\Psi_{1}(s):\quad
\forall \nabla\text{-instruction } I,\quad
requires_cap(I) \subseteq CapSet(r_s)
]

Meaning:

* no ∇ (write, ALU, memory action) may be executed by a role lacking capability.

### **Invariant Ψ₂ — Frame isolation (□/Χ consistency)**

For all memory operations:

[
\Psi_{2}(s):\quad
Addr \in VisibleFrames(f_s)
]

Ensures frames obey visibility rules — processes cannot exceed their sandbox.

### **Invariant Ψ₃ — No uncontrolled privilege escalation (Ω monotonicity)**

Privilege transitions must follow:

[
USER \rightarrow KERNEL \text{ only via } Φ_{trap}
]
[
KERNEL \rightarrow USER \text{ only via } Φ_{return}
]

Ψ enforces monotonicity of role transitions except on authorized paths.

### **Invariant Ψ₄ — Policy integrity (Σ + Ψ)**

Updates to the policy set are allowed only in kernel context:

[
Ψ\text{-mutating ops allowed iff } r_s = KERNEL
]

### **Invariant Ψ₅ — Temporal fairness (optional)**

If enabled, fairness is also expressed as a Ψ condition:

[
\Psi_{5}(s):\quad
\forall\text{ runnable process } p,;\text{p must be scheduled eventually}
]

This will tie into the Θ-based scheduler.

### **Invariant Ψ₆ — Safe recontextualization (Φ correctness)**

Φ transitions (traps, exceptions, context shifts) must preserve:

* caller isolation (Χ)
* privilege boundaries (Ω)
* correct frame layouts (□)

Formally:

[
Φ(s) \Rightarrow s' \text{ satisfies } \Psi_{1\ldots5}
]

Φ cannot break Ψ invariants.

---

# **3.1.3 Kernel Rights & Obligations (Operator-Level)**

### **Rights: What kernel *may* do**

* **Ω-rights:**
  Assign, modify, or revoke roles/capabilities.

* **□-rights:**
  Create/manage frames (process address spaces, kernel segments).

* **Χ-rights:**
  Create isolate domains (processes, containers, VMs).

* **Φ-rights:**
  Enter and leave any context; handle traps; define trap tables.

* **Σ-rights:**
  Commit global state (scheduler decisions, resource accounting, process tables).

* **Ψ-rights:**
  Define system-wide invariants; halt system on violation.

### **Obligations: What kernel *must* do**

Every kernel action must satisfy:

[
\Psi(s_{before}) \Rightarrow \Psi(s_{after})
]

meaning kernel cannot violate global invariants even temporarily
(except in isolated rollback paths defined by Φ/Σ).

Additionally:

* Kernel must maintain **monotonic isolation**:

[
Χ_{user} \preceq Χ_{kernel}
]

User isolation cannot shrink kernel visibility.

* Kernel must ensure **correct frame/role meta integrity**:

[
(f_{user}, r_{user}) \text{ never gain access to kernel frames}
]

* Kernel must perform **Θ-scheduling** deterministically or plastically (policy-defined).

---

# **3.1.4 Relation to PMS-CPU**

**PMS-CPU** defines:

* registers, memory, frames, roles
* trap/interrupt infrastructure (Φ)
* isolation primitives (Χ)
* policy checks (Ψ)
* commit rules (Σ)

**PMS-OS Kernel** installs:

* process table
* scheduling rules over Θ
* memory allocator over □
* privilege architecture over Ω
* system call interface over Φ
* isolation semantics over Χ
* global policies (Ψ) that bind all components

Thus kernel = “privileged PMS program” that configures the CPU’s operator algebra into multi-process semantics.

---

# **3.1.5 Kernel as a Persistent Φ-Handler**

The kernel is entered via:

* system calls (user → kernel)
* interrupts (device → kernel)
* exceptions (faults → kernel)

These are **Φ transitions** that:

1. Switch frame (□), role (Ω), and isolation domain (Χ → global)
2. Execute kernel routines as ∇ / □ / Ω / Θ / Σ
3. Return to user-space via Φ-return

Formally:

[
Φ_{enter}: (f_{user}, r_{user}, Χ_{user}) \rightarrow (KF, KERNEL, Χ_{global})
]
[
Φ_{exit}: (KF, KERNEL, Χ_{global}) \rightarrow (f_{user}, r_{user}, Χ_{user})
]

Kernel is effectively the **Φ-domain master**.

---

# **3.1.6 Kernel Process Model: Trust Structure (Preview)**

(Actual details in 3.3; here is the trust perspective.)

Each user process has:

* its own frame (□)
* its own isolation domain (Χ)
* a restricted role (Ω)
* per-process policies (Ψ_local), subject to Ψ_global

The kernel:

* creates/destroys processes
* assigns frames to them
* switches Θ execution
* applies Σ commits (context switches, accounting)

Processes can never:

* modify their frames outside allowed regions
* change their roles (Ω)
* break isolation (Χ)
* bypass kernel policy (Ψ)
* enter kernel context except through Φ(t) traps

---

# **3.1.7 Summary**

The PMS-OS kernel’s **trust model** is fully defined by PMS operators:

* **Ψ**: defines global invariants the kernel guarantees
* **Ω**: establishes privilege roles and permissions
* **□**: defines execution frames and memory contexts
* **Χ**: establishes process isolation boundaries
* **Φ**: defines legitimate entry/exit paths into kernel mode
* **Σ**: defines global commit/integration points
* **Θ**: defines controlled temporal scheduling
* **Δ/∇**: provide the low-level logic/ action backbone

This model unifies:

* process isolation
* privilege rings
* memory protection
* trap/interrupt handling
* system calls
* scheduling
* resource control
* transactional safety

in one consistent operator-theoretic framework.

---

# **3.2 Core Data Structures (PProcess, Frame, Policy, Message)**

These are the **canonical kernel-level data structures**, each directly aligned with PMS operators.
They are *not* implementation artifacts — they form the kernel’s formal state space.

We define them as **algebraic records**, with explicit PMS semantics attached.

---

# **3.2.1 PProcess (Praxeological Process Control Block)**

A **PProcess** is the kernel’s representation of a running or runnable computational locus — conceptually similar to a PCB/TCB, but **operator-typed**.

### **Definition**

[
PProcess =
(id,; f,; r,; Χ,; P_{local},; regs,; meta)
]

Where:

### **• `id`**

Unique process identifier.
Created via **Δ→∇** during `PROC_CREATE`.

### **• `f : FrameId`**

The **current address/context frame** of this process.
(□ semantics)

### **• `r : Role`**

The role / privilege level (Ω).
Atomic transitions only via Φ(syscall/trap) or Ω-ops inside kernel.

### **• `Χ : IsolationContext`**

Defines the boundaries of visibility:
Which frames, devices, channels are visible to this process.

### **• `P_local : PolicySet`**

Per-process policies (Ψ).
Always subordinate to global kernel policies:

[
P_{local} \preceq P_{global}
]

Examples:

* memory quota limit
* open file count limit
* IPC rate limit
* CPU usage constraints

### **• `regs : RegisterFileSnapshot`**

Snapshot of PMS-CPU registers (RF, PC, SP, FR, SR) when process is not currently executing.
Necessary for context switching (Θ+Φ).

### **• `meta`**

Process meta-state:

* scheduling data (Θ counters: runtime_used, quantum_remaining)
* exception / trap state flags (Φ)
* pending signals or events (Λ)
* accounting counters (Σ)

---

# **3.2.2 Frame**

Frames (□) are the kernel’s first-class abstraction for **execution and memory contexts**.

A **Frame** is:

[
Frame = (id,; base,; size,; type,; perms,; owner,; links)
]

Where:

### **• `id : FrameId`**

Kernel-unique frame identifier.

### **• `base, size`**

Memory region bounds.
These define the frame’s projection onto physical or virtual memory.

### **• `type ∈ {CODE, DATA, STACK, MMIO, DEVICE, KERNEL, USER, …}`**

### **• `perms`**

Permissions over this frame:

[
perms = {read, write, exec, share, map, …}
]

Controlled by Ω and checked by Ψ on every ∇ or Δ-branch involving memory.

### **• `owner : PProcessID`**

Which process “owns” the frame.
Kernel frames have owner = `KERNEL`.

### **• `links` (optional)**

Relationships to other frames:

* parent/child frames (for isolation χ)
* copy-on-write links
* shared frames for IPC or mapped I/O
* mounted subframes (filesystem layers)

**Frame = the □ data structure**.

---

# **3.2.3 Policy**

Policies implement Ψ semantics at kernel level.

A **Policy** is one of:

[
Policy ::=
(ResourceLimit);|;
(CapabilityRule);|;
(AccessRule);|;
(SchedulingRule);|;
(GlobalInvariant);|;
(Custom)
]

### **Generic form:**

[
Policy = (id,; scope,; predicate,; action)
]

Where:

### **• `id`**

Identifier.

### **• `scope ∈ {global, per_process, per_frame, per_role}`**

Defines whether Ψ applies to:

* global system state
* each process
* each frame
* each role/capability set

### **• `predicate : State → {true,false}`**

Checks invariant or constraint.
Examples:

* memory usage ≤ quota
* attempts to write to read-only frame
* no role escalation except via Φ
* scheduling fairness conditions

### **• `action`**

Executed if predicate fails.
A **Φ/Σ combination**, e.g.:

* **Φ**: trap to kernel recovery handler
* **Σ**: rollback memory to last consistent state
* **Σ + HALT**: terminate offending process
* **Φ + adjust_P**: apply fallback policy

Policies are entirely operator-based.

---

# **3.2.4 Message (IPC primitive)**

The PMS kernel has **message-passing as first-class** (Δ, Ω, Λ, Θ, Φ, Σ).
Messages define kernel-level IPC.

### **Definition**

[
Message = (id,; sender,; receiver,; type,; payload,; meta)
]

Where:

### **• `id`**

Unique message ID.

### **• `sender : PID`**,

### **• `receiver : PID`**

Endpoints must be valid processes, or kernel/system endpoints.

### **• `type`**

Δ-distinction type:

* `REQ` (request)
* `RESP` (response)
* `EVT` (event)
* `CTRL` (control)
* `SIG` (signal-like)
* `TIMEOUT`
* etc.

### **• `payload`**

Opaque bytes or structured data.
May reside in a dedicated message frame or shared IPC region.

### **• `meta`**

Data relevant to PMS operators:

* whether message is blocking or async (Θ/Λ)
* capabilities carried (Ω)
* isolation scope for payload (Χ)
* deadlines (Θ)
* delivery guarantees (Σ)

The kernel’s IPC subsystem (chapter 5) uses these fields directly.

---

# **3.2.5 Summary Table**

| Structure    | PMS Operators       | Purpose                                                |
| ------------ | ------------------- | ------------------------------------------------------ |
| **PProcess** | Ω, □, Χ, Θ, Φ, Σ, Ψ | Process identity, isolation, scheduling, policies      |
| **Frame**    | □, Ω, Χ             | Memory/execution context with permissions              |
| **Policy**   | Ψ, Ω, Φ, Σ          | Global or local invariants; violation handlers         |
| **Message**  | Δ, Ω, Λ, Θ, Φ, Σ    | Kernel-level IPC with distinction, roles, time, events |

These are the **core kernel objects**.
Every upcoming kernel subsystem (scheduler, memory manager, syscall layer, IPC, etc.) operates on these.

---

# **3.3 Process & Thread Model(states, transitions, roles)**

This section defines how **processes and threads exist, transition, and interact** inside a PMS-OS kernel.
No psychology, no behavior modelling — purely **praxeological structures** (operators, roles, frames, temporal arcs, isolation).

We use:

* PMS-CPU (chapter 2) as the execution substrate
* Kernel data structures (3.2) as the state space
* PMS operators Δ–Ψ as the **ONLY** allowed model-building primitives

---

# **3.3.1 Conceptual Overview**

In PMS, a **process** is a **Χ-isolated, Ω-scoped, □-contextual locus of ∇-capable execution**, governed by Ψ policies and advanced in Θ temporal steps.

A **thread** is a **Θ-scheduled execution strand** within a process, sharing the same:

* frames (□),
* role/capabilities (Ω),
* isolation boundary (Χ),
* policies (Ψ),
* but with its own **register snapshot** and temporal arc in `meta`.

Thus:

### **Process = structural container (Χ / Ω / □ / Ψ) and Thread = temporal actuator (Θ / Δ / ∇ / Φ / Σ)**

They form a nested praxeological hierarchy.

---

# **3.3.2 Kernel-Level Representation**

### **Process Representation**

(Using PProcess from 3.2)

[
PProcess = (id,; f,; r,; Χ,; P_{local},; regs,; meta)
]

### **Thread Representation**

A **Thread** is:

[
Thread = (tid,; parentPID,; regs,; state,; Θ_{budget},; meta)
]

Where:

* `regs` = register snapshot (including PC, SP, FR, SR)
* `state` = thread scheduling state (see below)
* `Θ_budget` = time quantum or eligibility counter
* `meta` = exception flags (Φ), wait conditions (Λ), last-run time, etc.

Multiple threads share:

* process frames (□)
* process role (Ω)
* process isolation scope (Χ)
* process local policies (Ψ)
* process-owned messages / IPC channels

---

# **3.3.3 Thread States (PMS-Aligned)**

We define **kernel thread states** strictly using PMS operators:

| Thread State   | PMS Operators | Meaning                                                 |
| -------------- | ------------- | ------------------------------------------------------- |
| **READY**      | Δ, Θ          | Distinctively ready for next Θ scheduling step          |
| **RUNNING**    | ∇, Θ          | Actively executing ∇ instructions                       |
| **BLOCKED**    | Λ, Φ          | Waiting on event, timeout, I/O, or exception            |
| **SUSPENDED**  | Χ, Ω          | Suspended via role or isolation constraint              |
| **ZOMBIE**     | Σ             | Completed execution but not integrated (not reaped)     |
| **TERMINATED** | Σ + Ψ         | Fully integrated into system state; resources reclaimed |

Let’s define each formally:

---

### **READY**

A thread is considered **READY** if:

1. Its next instruction is legal (dependency constraints satisfied)
2. Policies (Ψ) do not block it
3. No pending Λ or Φ requiring special handling

Symbolically:

[
ready(t) := Δ(t) ∧ ¬Λ(t) ∧ ¬Φ(t) ∧ Ψ_{allow}(t)
]

---

### **RUNNING**

During execution:

[
RUNNING := (t.state = RUNNING) \land \Theta_step
]

This is the Θ→∇ phase transition.

A RUNNING thread repeatedly performs:

[
\Delta \rightarrow \nabla \rightarrow (\Theta) \rightarrow ...
]

As defined in PMS-CPU (2.6).

---

### **BLOCKED**

A thread is **BLOCKED** when it is in a Λ-context:

* waiting for IPC message
* waiting for I/O
* sleeping
* waiting for condition variable
* waiting for event/timer
* waiting for kernel service

Formal:

[
BLOCKED := Λ_{pending}(t) \lor Φ_{pending}(t)
]

Because:

* Λ = non-event
* Φ = recontextualization (e.g., waiting for handler)

---

### **SUSPENDED**

Suspension is **Χ / Ω driven**:

* restricted by isolation boundary
* prevented by privilege roles
* or manually suspended via kernel control

[
SUSPENDED := Χ_{restriction}(t) \lor Ω_{deny}(t)
]

---

### **ZOMBIE**

A thread that finished execution (PC reached end), but not yet reclaimed.

This is:

[
ZOMBIE := Σ_{pending}(t)
]

Integration not yet performed.

---

### **TERMINATED**

A thread is terminated when:

1. Its Σ integration is complete
2. Policies Ψ declare its lifecycle ended

Formal:

[
TERMINATED := Σ_{done}(t) \land Ψ_{close}(t)
]

---

# **3.3.4 Process States**

Process states derive from their constituent threads:

| Process State  | Condition                                       |
| -------------- | ----------------------------------------------- |
| **RUNNING**    | at least one RUNNING thread                     |
| **READY**      | at least one READY thread and none RUNNING      |
| **BLOCKED**    | all threads BLOCKED                             |
| **SUSPENDED**  | all threads SUSPENDED or isolated by Χ/Ω        |
| **ZOMBIE**     | no runnable threads, but resources uncollected  |
| **TERMINATED** | all threads TERMINATED and process Σ/Ψ complete |

Formally:

[
state(P) = Σ({state(t) \mid t \in Threads(P)})
]

Integration Σ chooses the resulting process state by collapsing thread states.

---

# **3.3.5 State Transition Rules**

The kernel defines **operator-typed transitions**:

### **1. READY → RUNNING (Θ scheduling)**

[
(READY, Θ) \rightarrow RUNNING
]

### **2. RUNNING → READY (Θ quantum expiry)**

[
RUNNING \xrightarrow{Θ_{expire}} READY
]

### **3. RUNNING → BLOCKED (Λ or Φ)**

[
RUNNING \xrightarrow{Λ} BLOCKED
]
[
RUNNING \xrightarrow{Φ} BLOCKED
]

### **4. BLOCKED → READY (event arrival)**

[
BLOCKED \xrightarrow{\neg Λ} READY
]

### **5. RUNNING → SUSPENDED (Ω or Χ)**

[
RUNNING \xrightarrow{Ω_{restrict}} SUSPENDED
]
[
RUNNING \xrightarrow{Χ_{enter}} SUSPENDED
]

### **6. SUSPENDED → READY (Ω or Χ release)**

[
SUSPENDED \xrightarrow{Ω_{allow}} READY
]

### **7. RUNNING → ZOMBIE (PC reached end)**

[
RUNNING \xrightarrow{Σ_{pending}} ZOMBIE
]

### **8. ZOMBIE → TERMINATED (Σ+Ψ)**

[
ZOMBIE \xrightarrow{Σ_{complete} \land Ψ_{close}} TERMINATED
]

These transitions constitute the thread/process-level automaton.

---

# **3.3.6 Role and Capability Semantics (Ω)**

Ω defines the **role track** of a process and its threads:

* USER
* SYSTEM
* SUPERVISOR
* HYPERVISOR

Transitions:

[
Ω: r \rightarrow r'
]

are only allowed via Φ (trap) or kernel-controlled Ω instructions.

Ω also determines:

* allowed syscalls
* allowed frames (□)
* allowed isolation scopes (Χ)
* allowed policy modifications (Ψ)

Thus Ω provides **the role lattice** governing process/thread behavior.

---

# **3.3.7 Isolation Semantics (Χ)**

Χ defines how threads and processes are separated:

* memory isolation
* namespace isolation
* device visibility
* IPC boundary definitions

Operations:

[
Χ_{enter}(ctx) \quad ; \quad Χ_{exit}
]

Transitions impose or remove visibility restrictions.

Threads inherit Χ from their parent process unless a Φ operation creates a nested context (e.g. entering a sandbox or VM).

---

# **3.3.8 Temporal Semantics (Θ)**

Θ governs:

* scheduling quantum
* fairness
* preemption
* wait timeouts
* temporal constraints in Ψ (e.g., max latency)

Each step in thread execution is:

[
\Delta \rightarrow \nabla \rightarrow Θ
]

and scheduling itself is implemented as a **Θ-rooted operator sequence**:

[
Θ_{schedule}: select(t) → context_switch → RUNNING
]

This is the subject of section 3.4 (scheduler).

---

# **3.3.9 Exception & Trap Semantics (Φ)**

Threads encountering:

* errors,
* illegal instructions,
* privilege violations,
* page faults,
* explicit TRAP instructions,

transition via Φ into handler contexts, preserving their state in `meta`.

Φ never discards state; it **recontextualizes** it.

Example:

[
RUNNING \xrightarrow{Φ_{pagefault}} BLOCKED
]

Later:

[
BLOCKED \xrightarrow{Φ_{resume}} READY
]

---

# **3.3.10 Integration Semantics (Σ + Ψ)**

When threads end, Σ cleans up:

* open frames
* file descriptors
* IPC endpoints
* memory regions
* temporary states

Ψ finalizes:

* accounting logs
* last-used capabilities
* applied policies
* termination conditions

A process ends when:

[
\forall t \in Threads(P): TERMINATED(t)
]

and Σ merges all remaining resources into global kernel state.

---

# **3.3.11 Summary**

### **Processes:**

* □ execution contexts
* Ω privilege roles
* Χ isolation boundaries
* Ψ local/global policies
* Host multiple Θ-scheduled threads

### **Threads:**

* Δ-driven distinction
* ∇-driven execution
* Θ temporal arcs
* Λ/Φ wait and exception
* Σ/Ψ finalization

### **Transitions:**

Operator-typed and fully PMS-valid.

---
# **3.4 Scheduling (Θ) – algorithms & policies**

In the PMS-OS kernel, **Θ is the temporal operator** responsible for *progression, ordering, cadence, selection, fairness*, and all scheduling semantics.

A scheduler is therefore **not an algorithmic trick** —
it is the **Θ-governed praxeological structure** controlling when and how processes/threads are allowed to perform ∇ actions inside their □-contexts under Ω/Ψ constraints.

We proceed strictly structurally.

---

# **3.4.1 Core Idea: Scheduling = Θ-mediated selection of ∇-capable loci**

At its most formal:

A scheduler is a **Θ-rooted operator chain** that maps:

[
Θ : \text{ReadySet} ;\rightarrow; \text{SelectedThread}
]

subject to **Ψ policies**, **Ω roles**, **Χ isolation**, and **Λ wait states**.

Execution then proceeds:

[
Θ_{schedule} ;\circ; \Delta ;\circ; \nabla ;\circ; Θ ;\circ; \dots
]

until preemption or blocking.

---

# **3.4.2 Scheduler State**

Scheduler metadata sits inside the kernel’s **m** (meta-state):

[
m_{sched} = \left(
rq,;
rq_prio,;
clocks,;
Θ_{quantum},;
deadlines,;
history,;
fairness_tokens
\right)
]

Where:

* **rq** – ready queue (Θ-schedulable threads)
* **rq_prio** – optionally priority-indexed queues (Ω constraints may alter priority)
* **clocks** – kernel time sources for Θ progression
* **Θ_quantum** – time slice per thread (or dynamic)
* **deadlines** – for real-time scheduling
* **history** – records Δ/∇ patterns for fairness Ψ
* **fairness_tokens** – quotas to avoid starvation (Ψ_fair)

---

# **3.4.3 Scheduler Interface as Operators**

The scheduler exposes a small set of **operator-level primitives**:

### **Θ.enqueue(t)**

Register thread t as READY.

Requires:

* Ω permits scheduling
* Ψ does not forbid running t
* No Λ or Φ pending that force BLOCKED

### **Θ.dequeue(t)**

Remove t from scheduling context (BLOCKED, SUSPENDED, ZOMBIE transitions).

### **Θ.select() → t**

Selects one READY thread.

This is where scheduling *algorithmics* happen, but always as **Θ-expressions**, not imperative semantics.

### **Θ.dispatch(t)**

Perform a controlled **context switch**:

1. Save current thread state (Σ-partial)
2. Switch frames (□)
3. Switch roles (Ω) if necessary
4. Update ip
5. Transition thread t → RUNNING

### **Θ.tick()**

Advance the scheduler’s notion of time, update deadlines, check preemption, generate Λ events if timeouts occur.

---

# **3.4.4 Context Switch (Θ + Σ + □ + Ω)**

A context switch is fundamentally a **Θ-triggered Σ integration of the old thread’s transient ∇ actions**, followed by **reassignment of □ and Ω** to the new thread.

Formally:

[
Θ_{switch}(t_{old}, t_{new}) =
Σ_{save}(t_{old})
;\circ;
□*{set}(frame(t*{new}))
;\circ;
Ω_{set}(role(t_{new}))
;\circ;
Θ_{start}(t_{new})
]

This emphasizes:

* Θ orchestrates sequencing
* Σ commits and freezes the outgoing thread’s partial execution
* □ changes context
* Ω changes privilege track
* No ∇ occurs except in **Σ-save / frame setup** operations

---

# **3.4.5 Scheduling as a PMS Automaton**

We model scheduling transitions with the following structural automaton:

[
(RQ,;t,;m_{sched})
\xrightarrow{Θ_{select}}
(t,;RUNNING)
\xrightarrow{Θ_{quantum_expire}}
READY
]

[
RUNNING \xrightarrow{Λ} BLOCKED
]

[
BLOCKED \xrightarrow{\neg Λ} READY
]

[
RUNNING \xrightarrow{Ω_{restrict}} SUSPENDED
]

[
SUSPENDED \xrightarrow{Ω_{allow}} READY
]

This matches exactly the thread state transitions in 3.3, but **Θ is the causal driver**.

---

# **3.4.6 Scheduling Algorithms in Θ-Form**

We now show how classical scheduling styles appear **purely structurally** in Θ terms.

## **(A) Round-Robin**

Θ.select picks next thread in rq cyclically:

[
Θ_{select} := Θ_{rr}(rq, ptr)
]

Where `ptr` is a meta pointer in m, rotated on Θ.tick.

Preemption occurs when:

[
Θ_{quantum}(t) = 0 \quad \Rightarrow \quad Θ_{switch}
]

This is a pure Θ-machine.

---

## **(B) Priority Scheduling (Ω + Θ)**

Priority is a **Ω-asymmetry**.
Thus rq_prio is structured by Ω roles.

Selection rule:

[
Θ_{select}(rq_prio) :=
\text{pick highest Ω-level queue with READY threads}
]

Preemption rule:

[
Ω(t') > Ω(t) \Rightarrow Θ_{switch}(t \rightarrow t')
]

Ω forms a strict partial order defining preference.

---

## **(C) Weighted Fairness (Ψ_fair + Θ)**

Fairness is encoded as a **Ψ-level invariant**:

[
Ψ_{fair}: \forall t,; \text{if } ready(t) \text{ infinitely often} \Rightarrow scheduled(t) \text{ infinitely often}
]

Θ implements this via:

* fairness_tokens
* historical counters in m.history
* rotating deficits (DRR-like)

Selection:

[
Θ_{select}(rq) := \arg\max_t; fairness_tokens(t)
]

Each dispatch decrements tokens; Θ.tick increments them.

---

## **(D) Real-Time Scheduling (deadlines in meta + Θ)**

Deadlines live in meta:

[
deadline(t) \in m.deadlines
]

Selection policy:

Earliest Deadline First:

[
Θ_{select}(rq) := \arg\min_t; deadline(t)
]

Rate Monotonic (RM):

[
Ω_{RM}(t) := \frac{1}{period(t)}
]
[
Θ_{select} := \arg\max_t; Ω_{RM}(t)
]

---

## **(E) Mixed Hierarchical Schedulers (Ω + Ψ + Θ)**

Because Ω defines hierarchies and Ψ defines branch constraints, a PMS scheduler may enforce multi-level constraints:

Example:

* Ω separates kernel threads, service threads, user threads
* Ψ ensures minimum fairness for user threads
* Θ chooses actual dispatch order

Formally:

[
Θ_{select} = Θ(Ω\text{-groups} \rightarrow Ψ\text{-constraints} \rightarrow rq)
]

---

# **3.4.7 Handling Timeouts & Missing Events (Λ)**

Λ is triggered when an expected event (I/O, IPC, lock) **does not** occur.

In scheduling:

[
RUNNING \xrightarrow{∇(wait)} BLOCKED
]

Then:

### If timeout elapses:

[
BLOCKED \xrightarrow{Λ_{timeout}} READY
]

### If event arrives:

[
BLOCKED \xrightarrow{\neg Λ} READY
]

Λ is always coupled with Θ.tick:

[
Λ_{timeout} := (Θ.now \ge m.wait_deadline)
]

---

# **3.4.8 Hyper-scheduling and Isolation (Χ)**

Χ allows the scheduler to run **multiple isolated scheduling domains**:

[
Χ: domain_i ;\perp; domain_j
]

Each domain has its **own Θ-instance**:

[
Θ_i,; Θ_j : distinct scheduling automata
]

This models:

* VM guest schedulers
* container schedulers
* per-core runqueues
* scheduling classes (RT vs normal)

Χ governs whether Θ_i may inspect or influence Θ_j.

---

# **3.4.9 Scheduler Policy Engine (Ψ_s)**

Ω defines priority and role constraints.
Ψ defines **policy-level invariants** such as:

* no starvation
* max latency L_max
* max CPU share
* mandatory isolation between classes
* guaranteed service constraints

These are enforced by the scheduler as:

[
Ψ_s(sched_state,; t) = \text{true/false}
]

If Ψ_s forbids scheduling t:

* t stays READY but unselectable
* or t is demoted to SUSPENDED
* or t triggers Φ → recontextualized handling

Ψ_s may also enforce **termination** if constraints are violated:

[
Ψ_s(t) = \text{violation} ;\Rightarrow; t \rightarrow TERMINATED
]

---

# **3.4.10 Preemption Model (Θ + Φ)**

A preemption event is:

[
RUNNING(t) \xrightarrow{Θ_preempt} READY(t)
]

Triggers:

* save registers (Σ-save)
* run Φ_recontext if preemption needs reframing (e.g., kernel trap)
* scheduler chooses next t'

Formally:

[
Θ_preempt :=
\begin{cases}
Θ_{quantum_expire},\
Ω_{priority_intrusion},\
Φ_{interrupt},\
Ψ_{policy_trigger}
\end{cases}
]

Thus **preemption results from Θ, Ω, Φ, Ψ interactions**.

---

# **3.4.11 Putting It All Together: The PMS Scheduling Equation**

A full Θ-driven scheduling cycle is:

[
Θ_{tick}
;\circ;
Θ_{update_queues}
;\circ;
Θ_{select}
;\circ;
Θ_{dispatch}
;\circ;
(\Delta ; \nabla)^*
;\circ;
Θ_{yield/preempt}
]

Subject to:

[
Ψ(whole_system) = true
]

This is the **minimal praxeological structure of a scheduler**.

---

# **3.4.12 Summary**

**Scheduling (Θ) controls:**

* which threads run
* when they run
* for how long they run
* under which privileges (Ω)
* inside which frame (□)
* under which invariants (Ψ)
* respecting isolation (Χ)
* reacting to missing events (Λ)
* handling recontextualizations (Φ)
* integrating progress (Σ)

Θ is the **formal backbone** of kernel execution.

---

# **3.5 Isolation & Protection (Χ, Ω) – capabilities, memory protection**

Χ and Ω are the **kernel’s structural security substrate**.
Together they define:

* **who may act** (Ω)
* **where action is allowed** (Χ + □)
* **under what constraints** (Ψ)

Isolation is never a heuristic — it is an **operator-enforced structural transformation**.

We build the model bottom-up.

---

# **3.5.1 Core Idea: Isolation = Χ applied to □-contexts**

A process is *not* a bundle of resources; it is a **frame (□)** with:

* a register/memory view
* a namespace
* an access graph

**Χ creates *distance* between frames**, meaning:

[
χ: \square_i ;\rightarrow; (\square_i,;\square_j)_{isolated}
]

Χ partitions the world into **accessible** and **non-accessible** regions.

---

# **3.5.2 Role of Ω (Asymmetry)**

Ω defines structured **access asymmetries**, i.e., who may interact with what.

In PMS terms:

[
Ω(f_i, r) = \text{allowed action set in frame } f_i
]

Ω is the operator that:

* assigns **privilege levels** (kernel vs user)
* assigns **capabilities**
* governs **directionality** of access (e.g. parent→child allowed, child→parent denied)

Isolation (Χ) defines boundaries.
Ω defines **one-way doors** across boundaries.

Together they define **capability machines**, memory protection, syscall permissions.

---

# **3.5.3 Structural Model of Kernel Isolation**

Kernel processes (system frames) live in a privileged domain:

[
Ω(kernel) > Ω(user)
]

Χ enforces that **user □-frames cannot see or mutate kernel □ frames**:

[
χ(\square_{user},\square_{kernel}) = \text{strict separation}
]

This yields classical kernel→user asymmetries:

* kernel may inspect user memory (Ω high → has permission)
* user may not inspect kernel memory (Ω low → forbidden by dependency rules)

---

# **3.5.4 Memory Protection Rules in PMS Terms**

Define memory regions:

[
Mem = { R_1, R_2, \dots }
]

Each region belongs to a **frame**:

[
owner(R_k) = f_i
]

Each process p runs under role r_p and frame f_p.

The core rule:

[
\text{Access allowed}(p, R_k)
\quad\Leftrightarrow\quad
Ω(r_p) \triangleright owner(R_k)
]

Where **Ω(r_p) \triangleright owner(R_k)** means:

* The role r_p has capability to access owner frame f_i
* No Ψ policies prohibit this
* No Χ isolation boundary forbids this

Access occurs only through **∇**:

[
\nabla_{read/write}(p, R_k) \quad \text{requires Ω-permission + no χ-barrier}
]

Thus **all memory I/O is Ω+Χ-gated ∇ actions**.

---

# **3.5.5 Χ as the Kernel’s Isolation Graph**

We define a directed graph:

[
G_{iso} = (F, E)
]

Where:

* **F** = set of frames (process address spaces, kernel subsystems, device contexts)
* **E** = edges permitted by Ω and Ψ

Χ enforces **absence of edges**:

[
χ(f_i,f_j) = \neg ( (f_i,f_j)\in E )
]

Thus Χ literally *cuts edges* in the resource graph.

Isolation is not an emergent property — it is the **explicit result of applying Χ to □-nodes**.

---

# **3.5.6 Address Spaces as □-Frames**

Each process owns a **virtual address space**:

[
VAS(p) = \square_p
]

A mapping:

[
map_p : VAS(p) \rightarrow PhysicalMem
]

Permission enforcement is:

[
\nabla_{read/write}(addr) \text{ valid iff } Ω(r_p)\triangleright map_p(addr)
]

If Χ applies:

[
χ(\square_p, region) \Rightarrow \text{block precondition of ∇}
]

Thus ∇ fails **structurally**, not with an ad-hoc check.

---

# **3.5.7 Capability System (Ω)**

Capabilities are **structured asymmetries**:

A capability C is a triple:

[
C := (target_frame,; allowed_ops,; scope)
]

Ω grants a thread t the role:

[
r_t = r_{base} \cup {C_1, \dots, C_n}
]

Thus access is **role-driven**, not ACL-driven.

### Operators:

* **Ω.grant(C)**
  Adds capability C to r_t.

* **Ω.revoke(C)**
  Removes capability C from r_t.

* **Ω.check(op, f_j)**
  Returns whether ∇/Δ/etc. is allowed inside frame f_j.

All role changes must obey dependency rules:

* must follow Δ (distinction of capability)
* may be restricted by Ψ
* must respect isolation graphs (Χ cannot be overridden)

---

# **3.5.8 Memory Isolation Example**

Suppose:

* p_user has VAS_user
* kernel has VAS_kernel
* device driver has VAS_driver

Isolation graph:

[
G_{iso} :
\quad
\square_{user} ;\perp; \square_{kernel}
\quad
\square_{user} ;\perp; \square_{driver}
]

Ω privileges:

* r_user cannot access kernel frames
* r_kernel can access user frames (for copy_from_user)
* r_driver can access MMIO frames for devices

Thus access rules:

### Valid:

[
\text{kernel} : \nabla_{read}(VAS_{user})
]

### Invalid:

[
\text{user} : \nabla_{write}(VAS_{kernel})
]

Invalid operations fail because:

* χ enforces separation
* Ω denies privilege
* Ψ asserts security invariants (optional)

---

# **3.5.9 System Call Entry: a Χ → Ω reconfiguration**

When a user process makes a syscall:

1. **Δ** identifies syscall type
2. **Φ** recontextualizes to kernel frame
3. **Ω** changes role: user → kernel mode
4. **□** switches frame (VAS_user → VAS_kernel)
5. Kernel verifies arguments using Δ + Ψ
6. Kernel executes ∇ actions
7. **□ + Ω** restored to user mode
8. **Σ** finalizes return

This is a **structured operator sequence**, not a CPU trick:

[
Δ ; Φ ; Ω ; □ ; ∇^* ; Σ ; □^{-1} ; Ω^{-1}
]

---

# **3.5.10 Cross-Process Isolation (Χ) + IPC Gates**

Inter-process communication occurs via **explicit bridges**:

[
Bridge(f_i,f_j)
]

A bridge is a controlled exception in the isolation graph.

A process cannot spontaneously reach another frame:

[
χ(f_i,f_j) \Rightarrow \text{no direct Δ/∇/□ permitted}
]

So IPC requires **explicitly authorized structures**:

* message queues
* channels
* shared memory segments (only via Ω-granted capabilities)

Creating a shared memory region requires:

1. Δ: distinguish region
2. Ω: assign capability
3. Σ: commit region creation
4. Update isolation graph **locally** (one-directional edges unless Ψ forbids)

---

# **3.5.11 File System Isolation via Χ**

Directory trees map naturally to frames (□):

* each mount = frame
* each directory subtree = sub-frame

Isolation rules:

[
χ(\square_{container_1}, \square_{container_2})
]

removes visibility or writeability across namespaces.

Ω attaches read/write/exec capabilities relative to these frames.

---

# **3.5.12 Device Driver Protection (Ω + Χ)**

Drivers operate in semi-privileged domains.

Χ isolates:

* driver addressing domains
* DMA regions
* device registers

Ω restricts driver privileges:

* access only MMIO frames
* forbidden from arbitrary kernel memory
* forbidden from user memory unless mediated

This models **IOMMU** and driver sandboxing cleanly.

---

# **3.5.13 Ψ (Policy) Tightens All Isolation Rules**

Ψ governs:

* mandatory access control
* namespace normalization
* forbidden cross-domain flows
* invariants like “kernel memory must not be writable by user processes”
* memory safety / no-exec regions
* sandbox confinement

Ξ enforces these invariants at run time:

If an operation violates the policy:

[
Ψ(s) = \text{violation} \Rightarrow
s \rightarrow S_H \text{ (halt/kill transition)}
]

Thus isolation violations are **structurally fatal**.

---

# **3.5.14 Summary**

**Isolation is Χ**:

* creates disconnected or selectively connected contexts
* enforces address space separation
* forms the memory protection graph

**Protection is Ω**:

* assigns capabilities
* directs allowed/forbidden access
* controls privilege levels

**Ψ** reinforces both as invariants.
**□** frames provide the spatial substrate.
**∇** is allowed only when permitted by Χ+Ω+Ψ.

This yields a fully general, praxeologically grounded **capability-based security architecture**.

---

## **3.6 Kernel Policy Engine (Ψ) – hooks & evaluation**

Ψ is the **kernel’s self-binding operator**: once a policy is declared, Ψ constrains every future Δ, ∇, □, Ω, Θ, Φ, Χ, Σ.

So far we’ve used Ψ abstractly as “policies/invariants”.
Here we define **the actual kernel subsystem** that:

* stores policies,
* exposes hook points,
* evaluates them in real time,
* and decides whether transitions are allowed, transformed, or killed.

Think: *“the kernel’s conscience”*, but structurally: a Ψ-typed state machine.

We’ll do:

1. 3.6.1 Goals and structural role of Ψ in the kernel
2. 3.6.2 Policy objects and policy state
3. 3.6.3 Policy hooks (where Ψ sees the world)
4. 3.6.4 Policy evaluation pipeline
5. 3.6.5 Enforcement actions (what Ψ can do)
6. 3.6.6 Policy lifecycle (load, update, revoke)
7. 3.6.7 Performance & caching
8. 3.6.8 Compositional policies (stacking Ψ)
9. 3.6.9 Interaction with PMSL, tooling, and verification

---

### **3.6.1 Kernel Ψ: Goals & Structural Role**

We treat the **Kernel Policy Engine (KPE)** as a distinguished kernel subsystem:

[
KPE := (PSet_k,; Eval_\Psi,; Hooks,; Actions)
]

Where:

* **PSet_k** – the kernel’s current set of active policies (Ψ-state)
* **Eval_Ψ** – evaluation functions that decide “allowed / modified / denied / deferred”
* **Hooks** – the surfaces where kernel operations consult Ψ
* **Actions** – what Ψ is allowed to do when a rule fires

Goals:

1. Make **every security / governance rule** a Ψ policy, not a hard-coded special case.

2. Represent these rules as **constraints on operator transitions**:

   * e.g. “no ∇(write) to this frame from this role”,
   * “no Χ-exit from this sandbox without going through this Δ check”.

3. Keep Ψ **orthogonal** to functional behavior:

   * The system would *functionally* run with Ψ = ∅,
   * but we *never* actually run it that way outside controlled contexts.

---

### **3.6.2 Policy Objects and Policy State**

We introduce a first-class kernel object:

```text
struct Policy {
    PolicyId        id;
    PolicyScope     scope;       // global, per-frame, per-process, per-role, per-object
    PolicyMode      mode;        // enforce, monitor-only, disabled
    PolicyPriority  priority;
    PolicyExpr      expr;        // predicate or rule set
    PolicyActions   actions;     // allow/deny/modify/log/escalate
}
```

#### **3.6.2.1 Policy scope (where it applies)**

**PolicyScope** is structurally tied to PMS entities:

* `GLOBAL` – covers every operator in the kernel (Ψ_global)
* `FRAME(f)` – applies to all operations scoped to □-frame f
* `PROCESS(pid)` – applies to all transitions involving PProcess(pid)
* `ROLE(r)` – applies whenever Ω says `r` is active
* `OBJECT(obj_id)` – specific kernel objects (file, socket, IPC channel, etc.)

Each scope corresponds to a **region in PMS state**:

* global policies → P in global kernel state (`P_global`)
* frame policies → part of the frame metadata (□ + Ψ)
* role policies → attached to Ω roles
* object policies → tied to Σ-managed objects in memory/FS

#### **3.6.2.2 Policy expressions (Ψ formulas)**

**PolicyExpr** is a (restricted) logic over:

* actors: process, thread, role
* target: frame, object, address range
* operator: Δ, ∇, □, Ω, Θ, Φ, Χ, Σ type
* context: time, call stack, labels, tags
* history: simplified abstraction of `Hist(s)` (from 0.3)

We can think of a rule as:

[
\text{if } condition(actor, target, op, context) \text{ then } action
]

The Policy Engine never executes arbitrary code; it runs **declarative predicates**.

---

### **3.6.3 Policy Hooks (Ψ seeing the kernel)**

Hooks are where **kernel operations consult Ψ**.

We very explicitly tie them to PMS operators:

#### **3.6.3.1 Δ-hooks (distinction / decision)**

Places where the system chooses among branches:

* syscall dispatch
* IPC routing decisions
* scheduling decisions (pick next thread)
* FS decisions (follow symlink? mount namespace crossing?)

Δ-hooks allow policies like:

* “deny any syscall from ROLE_GUEST to open() / exec()”
* “for this process, rewrite open(path) to chrooted path”

#### **3.6.3.2 ∇-hooks (state-changing actions)**

Before a **mutating operation** executes:

* write to memory / file / socket
* change role / capabilities
* launch a process or clone a thread
* change frame mappings (VM operations)

Ψ can veto or rewrite ∇:

* “deny writes to /etc/* from non-privileged processes”
* “log any ∇ creating network connections with dest outside domain X”

#### **3.6.3.3 □ / Χ hooks (frame/isolation changes)**

Important logic when:

* switching address spaces (context switch)
* creating new frames (fork, container, VM)
* entering / exiting isolation (sandbox, chroot, namespace)

Policies:

* “this role cannot join any frame other than these whitelisted frames”
* “containers of type A must never mount B”

#### **3.6.3.4 Ω hooks (role / capability changes)**

Any change to **who you are**:

* acquiring or dropping capabilities
* switching from user to kernel mode (trap)
* assuming a new principal identity

Policies:

* “unprivileged processes cannot gain network capability”
* “service X may only impersonate users with label Y”

#### **3.6.3.5 Θ / Λ hooks (time, timeouts)**

Scheduling & timing:

* when Θ advances time (timer tick)
* when Λ signals a timeout or idle

Policies:

* “this process must not exceed N CPU ticks in interval T”
* “idle tasks must not starve runnable policy-critical tasks”

#### **3.6.3.6 Φ hooks (exceptions, traps, context shifts)**

When:

* trap into kernel (syscalls)
* faults occur
* returns to user-space happen

Policies:

* “on fault F from process with label X, kill process”
* “for debugging session, redirect exceptions to monitor”

#### **3.6.3.7 Σ hooks (commit / integration)**

At transaction boundaries:

* end of filesystem transactions
* commit of network packet transmission
* commit of process state (e.g., after exec)

Policies:

* “only commit transactions touching these objects if integrity tags match”
* “log every Σ on high-value resources”

---

### **3.6.4 Policy Evaluation Pipeline**

At every hook, we conceptually run the same pipeline:

[
( state\ s,\ operation\ op,\ context\ c ) \xrightarrow{Eval_\Psi} decision
]

Steps:

#### **(1) Collect context** (Δ over state)

Gather minimal necessary info:

* actor: `pid`, `tid`, `role`, `labels`
* target: object id, frame, path, address, etc.
* op type: which PMS operator class, plus concrete kind (e.g. `∇/WRITE` vs `∇/EXEC`)
* current time, system mode
* call stack tags (e.g. which subsystem invoked this)

This is conceptually a big Δ: we distinguish “this attempted action” as a structured event.

#### **(2) Select relevant policies** (Δ over PSet_k)

Filter PSet_k by scope:

* global policies always included
* plus policies scoped to actor, role, frame, target, etc.

We now have an ordered list:

[
P_{relevant} = { policy_1, \dots, policy_n }
]

ordered by **PolicyPriority**.

#### **(3) Evaluate predicates** (Ψ)

For each policy:

[
result_i = Eval(policy_i.expr, s, op, c)
]

Possible results:

* `ALLOW` – rule accepts and doesn’t override others
* `DENY` – rule denies operation
* `MODIFY` – rule transforms the operation or its parameters
* `DEFER` – rule says “ask another policy” (no opinion)
* `LOGONLY` – rule logs but does not influence decision
* `ESCALATE` – rule triggers higher-level escalation (e.g. send event to security framework)

#### **(4) Combine results (resolution)**

Using a configurable **policy combiner** (Ψ meta-policy):

Examples:

* “deny overrides allow” (classic)
* “first matching policy wins by priority”
* “policies can independently modify; final op is intersection of modifications”

We define an abstract combiner:

[
Combine: [result_i] \rightarrow decision
]

Where decision ∈:

* `FINAL_ALLOW(op')` – proceed, possibly with modified op'
* `FINAL_DENY(reason)` – block operation
* `FINAL_ESCALATE(dest)` – send to another handler / kill process / etc.

#### **(5) Act on decision (enforcement)**

See next section.

---

### **3.6.5 Enforcement Actions (What Ψ Can Do)**

Ψ must be powerful enough to control behavior, but not so powerful that it becomes a second kernel.

Allowed actions:

1. **Allow**
   Do nothing; let op proceed as requested.

2. **Modify**
   Transform the operation before it happens:

   * change path (`/secret` → `/dev/null` in a dummy sandbox)
   * downgrade permissions (open read-only instead of read-write)
   * redirect to a different frame (□ remap)

   Mechanically: Ψ can rewrite the op’s arguments, within a predefined transformation language.

3. **Deny / Block**

   * return an error to caller
   * for privileged operations, may trigger Φ (exception) instead of silent failure

4. **Kill / Isolate**

   * terminate the current process
   * or seal it further inside Χ (reduce its capabilities / frames) as a “quarantined” entity

   That is structurally:

   [
   χ' : \square_p \rightarrow \square_p^{quarantined}
   ]

5. **Log / Audit (Θ + Σ)**

   * append structured event to audit log
   * optionally integrate metrics: number of violations, near misses, etc.
   * logs are Σ-actions: they commit a record into a durable structure

6. **Escalate**

   * send message to governance layer (see section 8)
   * raise higher-level policy evaluations (e.g. human approval, remote validator)

Ψ **never bypasses** other operators: it mediates them.
Enforcement is always “as part of a transition”, not as a separate second computation.

---

### **3.6.6 Policy Lifecycle (Load, Update, Revoke)**

Ψ itself is subject to Ψ — the system’s governance is self-binding.

#### **3.6.6.1 Policy creation**

A privileged entity (kernel module, governance agent, boot configuration) can:

```text
Ψ_CREATE(policy_spec) → PolicyId
```

This is a Σ-typed operation: it integrates a new policy into `PSet_k`.

Constraints:

* Must run under a role with `CAP_POLICY_ADMIN` (Ω)
* Must pass meta-policy Ψ checks (e.g. “no policy may grant unrestricted access to these frames”)

#### **3.6.6.2 Policy update**

Policies can be updated:

```text
Ψ_UPDATE(PolicyId, new_spec)
```

This is structurally a **Φ + Σ combo**:

* Φ: reinterpret the meaning of the policy
* Σ: integrate new definition

Invariants:

* policy updates must not break core safety invariants
* constant “baseline” policies may be immutable (kernel trust base)

#### **3.6.6.3 Policy disable / remove**

Controlled via:

```text
Ψ_SET_MODE(PolicyId, mode)   // enforce / monitor-only / disabled
Ψ_DELETE(PolicyId)
```

Meta-policy (higher Ψ) may disallow the removal of foundational policies:

* e.g. you cannot disable “kernel memory non-writable by user processes”

#### **3.6.6.4 Boot-time Ψ**

At boot, a minimal set of policies is loaded:

* hardware invariants (no user writes to kernel frames)
* stack/heap sanity
* base resource quotas

Then additional policies (e.g. site-specific security rules) are loaded.

The **boot sequence** itself is a Δ→…→Ψ script, described later in 12.1.

---

### **3.6.7 Performance & Caching**

We don’t want Ψ to become a giant mutex on every syscall.

Structural techniques to make Ψ fast:

#### **3.6.7.1 Policy indexing**

Policies in `PSet_k` are indexed by scope and op type:

* per-syscall lists
* per-object-type lists
* per-role lists

Selecting relevant policies is a series of cheap Δ steps, not a linear scan of all policies.

#### **3.6.7.2 Decision caching**

For high-frequency operations, we can cache decisions:

```text
CacheKey = (actor_id, role, op_type, object_id, coarse_context)
CacheVal = decision_summary
```

Under constraints:

* Cache is invalidated/reduced when capabilities change (Ω) or policies change (Ψ).
* Cache entries are optional: if not present, Ψ evaluates from scratch.

#### **3.6.7.3 Fastpaths**

For operations that are obviously safe (common case):

* trivial policies quickly approve without scanning more complex rules.
* Example: read-only files in a public directory with only global, non-restrictive policies.

This is basically:

[
\text{If } \text{FastPathPre}(s,op) \text{ then allow immediately}
]

Fast path conditions must be proven sound (no false-allow), only occasionally over-conservative (false-deny leads to slow path).

---

### **3.6.8 Compositional Policies (Stacking Ψ)**

We want to allow:

* global policies (e.g. “no kernel memory writes from user mode”)
* domain policies (e.g. “all webserver processes must not read /home")
* process-specific policies (“this sandbox can only see dirs X, Y”)
* runtime policies (e.g. temporary restrictions after suspicious behavior)

We compose them as:

[
P_{eff}(subject) = Combine(P_{global}, P_{role}, P_{frame}, P_{process}, P_{object})
]

Where `Combine` is itself governed by a **meta-policy** (a Ψ-of-Ψ):

* express “deny overrides allow” vs “first match” vs “strict conjunction”
* disallow policies that attempt to weaken the global baseline

You can think of this as a **layered binding**:

* Ψ₀ – immutable kernel safety invariants
* Ψ₁ – site / deployment baseline
* Ψ₂ – per-role and per-domain policies
* Ψ₃ – dynamic policies (sandbox, runtime limits)

Hierarchically:

[
Ψ_{total} = Ψ_0 \land Ψ_1 \land Ψ_2 \land Ψ_3
]

No layer can contradict higher layers; at best, it can refine them further.

---

### **3.6.9 Interaction with PMSL, Tooling & Verification**

Everything about Ψ is **operator-visible** and **toolable**.

* PMSL (sections 9–10) can expose a **policy DSL** that compiles down to PolicyExpr.

* The IR (11.1) tags potentially security-relevant operations so static tools can check:

  * “does this PMSL module ever request capabilities it shouldn’t?”
  * “can this code path violate a given Ψ policy in principle?”

* Model checking (11.3) can be applied to:

  * subsets of the kernel state + policy rules
  * verifying properties like “no user process can escalate to ROLE_ADMIN under these policies”

* Debugging / observability (11.4):

  * Ψ contributes events to logs, metrics (“policy hit count”), traces (“policy X denied op Y”).

Ψ thus becomes:

* a **formally structured, PMS-native policy layer**,
* not a patchwork of ad-hoc checks.

---

**Net result:**

The **Kernel Policy Engine** is a concrete incarnation of Ψ:

* policies are objects with explicit scope and logic,
* hooks exist at each significant operator surface (Δ, ∇, □, Ω, Θ, Φ, Χ, Σ),
* decisions integrate with the rest of the PMS model,
* and invariants are expressible, enforceable, and analysable as part of the same formal system.

---

# **3.7 Syscall Interface – Taxonomy, Calling, Semantics**

*(The kernel’s Δ/∇/Φ/Ω/Ψ boundary)*

The **syscall interface** is the first **explicit and controlled meeting point** between:

* **User-space PMSL programs**
* The **kernel’s privileged PMS-CPU environment**

Structurally, every syscall is a **Φ–Ω–Δ–Ψ composite**:

1. **Φ** — context shift into kernel mode (trap)
2. **Ω** — privilege upgrade into a restricted kernel role
3. **Δ** — distinction: identify syscall number, validate arguments
4. **Ψ** — run policy rules
5. **∇ / □ / Χ / Σ** — actually perform the requested kernel operation
6. **Σ / Φ** — commit and re-contextualize when returning to user mode

A syscall is thus not a primitive, but a **composed PMS operator trajectory**.

---

# **3.7.1 Syscall Taxonomy (What kinds of syscalls exist?)**

We divide syscalls structurally by their dominant operator class.

### **A. Δ-class syscalls**

(*Distinction-heavy: resolve, lookup, classify, inspect*)

Examples:

* `stat(path)` – identify metadata of an object
* `getpid()` – return identity
* `resolve(service)` – service discovery

Dominant operators:

* Δ (testing / comparing identifiers)
* □ (interpreting path / namespace)
* mostly read-only, minimal ∇

---

### **B. ∇-class syscalls**

(*Actions: mutate kernel-managed state*)

Examples:

* `write(fd, buf, len)`
* `sendmsg(socket, msg)`
* `chmod`, `chown`
* `create`, `unlink`

Dominant operators:

* ∇ (actual mutation)
* Σ (integration)
* Ψ (policy constraints)
* Χ/Ω (permission checks)

These are the most policy-sensitive syscalls.

---

### **C. □-class syscalls**

(*Frame / address-space management*)

Examples:

* `mmap`, `munmap`, `mprotect`
* `clone`, `exec`, `chroot`
* namespace enter/exit

Dominant operators:

* □ (switching frames)
* Χ (for creating isolated frames)
* Ω (permission)
* Ψ (policy gating)

---

### **D. Ω-class syscalls**

(*Role or capability operations*)

Examples:

* `setuid`, `setgid`
* `capset` (capability manipulation)
* `sudo-like elevation primitives`

Dominant operators:

* Ω (role)
* Δ (checking target role/capability)
* Ψ (govern which transitions are allowed)

---

### **E. Θ-class syscalls**

(*Time, scheduling, timers*)

Examples:

* `nanosleep`
* `setitimer`
* real-time scheduling commands

Dominant operators:

* Θ (time abstraction)
* Λ (timeout conditions)
* Ψ (resource exhaustion constraints)

---

### **F. Φ-class syscalls**

(*Explicit traps / exec / context change*)

Examples:

* `syscall()` itself
* domain-crossing syscalls (vmcalls, seccomp notifiers)
* `execve` (context—reframing)

Dominant operators:

* Φ (context shift)
* □ (new frame)
* Ω (switch to kernel)
* Σ (commit process image)
* Ψ (enforce safety on entry)

---

### **G. Χ-class syscalls**

(*Isolation / sandbox / container control*)

Examples:

* `unshare()`
* `clone(CLONE_NEWUSER | …)`
* VM or container creation
* seccomp installation

Dominant operators:

* Χ (isolate)
* □ (install new namespace frames)
* Ψ (limit privileges)

---

### **H. Σ-class syscalls**

(*Integration, commit, transactional*)

Examples:

* `fsync`
* `sync`
* `commit journal`
* `checkpoint`
* `atomicfs / dependable write sets`

Dominant operators:

* Σ (integration)
* Ψ (commit-time invariants)
* Θ (ordering)

---

### **I. Ψ-class syscalls**

(*Governance, policy control*)

Examples:

* audit configuration
* system policy loader
* kernel-level rule definition

Dominant operators:

* Ψ (policy)
* Ω (role-checking)
* Σ (commit policy to global state)
* Φ (reframe policy scope)

---

# **3.7.2 Syscall Calling Convention (How syscalls are invoked)**

We define a PMS-native calling convention.
A syscall is invoked using a **Φ-tagged instruction**:

```asm
TRAP  syscall_id
```

Semantically:

1. **Φ**: enter kernel context

   * save user frame
   * switch to kernel frame
   * elevate Ω role to KERNEL
   * record trap reason in m.trap_info

2. **Δ**: identify syscall_id

3. **Δ**: validate argument registers

4. **Ψ**: run syscall-specific + global policies

5. Dispatch to **handler(syscall_id)**

Arguments are passed by registers:

* R0 = syscall_id
* R1–R5 = syscall arguments
* return value in R0

Stack usage is controlled by □ (frame switching).

---

# **3.7.3 Syscall Semantics (Detailed Execution Model)**

A kernel syscall handler is structurally:

[
Φ ;→; Ω ;→; Δ ;→; Ψ ;→; (\nabla,\square,\chi,\Theta,\Sigma) ;→; Φ
]

Breaking into phases:

---

## **Phase 1: Trap Entry (Φ)**

Triggered by:

```asm
TRAP syscall_id
```

Kernel performs:

* Save user PC, user SR
* Switch to kernel frame:
  [
  □: f := f_{kernel}
  ]
* Switch to kernel role:
  [
  Ω: r := ROLE_KERNEL
  ]
* Mark m.trap_context with syscall metadata (for policies)

---

## **Phase 2: Validate syscall identity (Δ)**

The handler stub checks:

[
Δ(syscall_id)
]

If invalid →
Φ: raise exception → return error, or kill.

---

## **Phase 3: Load & check arguments (Δ + Ω + Ψ)**

Argument validation is expressed as:

* Δ – check distinction (types, ranges, permissions)
* Ω – ensure role process has capability
* Ψ – ensure no global or object policy forbids the requested op

If policies disallow:

[
Ψ: \text{FINAL_DENY}
]

---

## **Phase 4: Execute core operation (∇ / □ / Χ / Θ / Σ)**

Depending on syscall type:

* ∇ ― modify kernel state (write, create, send, set attribute)
* □ ― change frames (mmap, exec, switch namespace)
* Χ ― isolate or restrict (containers, jails)
* Θ ― schedule-related operations
* Σ ― commit integration (fsync, checkpoint)

All these transitions must pass:

* Ω: privilege checks
* Ψ: post-operation safety constraints

---

## **Phase 5: Build return state & exit (Φ + Σ)**

The syscall returns using:

```asm
EXC_RET
```

which semantically:

* Σ: commit core changes relevant to the syscall
* Φ: reframe back to user context
* Ω: downgrade role from kernel → user

Result placed in R0.

---

# **3.7.4 Canonical Syscall Structure (Template)**

All syscalls can be specified with the following formal template:

```
Syscall S:
    Pre:
        Δ: identify target and arguments
        Ω: verify actor role/capabilities
        Ψ: check all policies
    Body:
        □: frame operations
        ∇: mutation operations
        Χ: isolation if needed
        Θ: scheduling/time semantics
        Σ: commit if required
    Post:
        Ψ: post-conditions (invariants)
        Φ: reframe to user-mode
```

This template is useful for:

* kernel code generation
* formal verification (section 11)
* syscall documentation
* static checking from PMSL

---

# **3.7.5 Example Syscall Semantics**

Let’s define a few canonical examples.

---

## **Example 1 — write(fd, buf, len)**

*(∇-class)*

### Pre:

* Δ: classify fd target (file/socket/pipe)
* Ω: check write capability
* Ψ: check file policies (read-only? audit-only?)

### Body:

* ∇: write to kernel buffer
* Θ: update timestamps
* Σ: commit the write if buffering disabled (or defer for fs journaling)

### Post:

* Ψ: verify post-conditions (no forbidden data leakage)
* Φ: return to user

---

## **Example 2 — mmap(addr, size, flags)**

*(□-class)*

### Pre:

* Δ: classify flags
* Ω: check memory map capability
* Ψ: enforce limits on mapping (no executable writable regions)

### Body:

* □: create new memory frame
* Χ: apply isolation if mapping belongs to a sandbox
* Σ: finalize mapping in process page table

### Post:

* Φ: return

---

## **Example 3 — execve(path, argv)**

*(Φ-class)*

### Pre:

* Δ: check file
* Ψ: enforce execution policies (no exec from forbidden frames)

### Body:

* Σ: commit process state flush
* □: install new executable frame (new FR)
* ∇: load program
* Φ: full reframe → new userspace context

### Post:

* Ψ: validate new context invariants

---

# **3.7.6 Syscall Table Structure**

Kernel maintains a table:

```
struct SyscallEntry {
    SyscallId id;
    SyscallHandler handler;
    PolicyMask   policy_requirements;
    RoleMask     allowed_roles;
    FrameMask    allowed_frames;
    OperatorClass op_class;    // Δ, ∇, □, … Ψ
}
```

The syscall table is a **manifest of PMS structure**.
Every entry tells the kernel:

* which operator class is dominant
* which policies must run
* which contexts are legal
* which roles can invoke it

This makes formal verification extremely straightforward.

---

# **3.7.7 The Syscall Interface as a PMS Contract**

The syscall layer is a **PMS sublanguage** with the grammar:

[
\Phi ; \Omega ; Δ ; Ψ ; (\nabla \mid \square \mid \chi \mid \Theta \mid \Sigma) ; Ψ ; Φ
]

Every syscall conforms to this pattern.

That gives us:

* **Predictable effects**
* **Verifiable invariants**
* **Well-defined privilege boundaries**
* **A clean separation** between user and kernel frames

---

# **3.8 Resource Accounting & Quotas**

*(CPU, memory, IPC, storage — all via Ω/Θ/Σ/Ψ, governed by process roles and kernel policy)*

PMS-XOS (the kernel we are specifying) must maintain **first-class, operator-structured resource accounting**, where every kernel-mediated resource consumption is explicitly represented as:

* **Δ** — identify resource and actor
* **Ω** — verify role/capability to consume
* **Θ** — measure temporal consumption
* **Σ** — commit usage increments
* **Ψ** — enforce policies/limits
* **Λ** — represent exhaustion or timeouts

This gives us a resource model with *machine-checkable invariants* and *fine-grained isolation*.

---

# **3.8.1 Goals of PMS Resource Accounting**

A PMS-designed kernel must guarantee:

1. **Deterministic accountability**
   All resource usage is attributed to a **frame + role (Ω)** combination.

2. **Policy-governed allocation (Ψ)**
   Resources must obey global and local invariants.

3. **Isolation (Χ)**
   One actor’s consumption cannot corrupt another’s.

4. **Temporal fairness (Θ)**
   Scheduling and rate-limits implemented by explicit time operators.

5. **Graceful degradation (Λ + Φ)**
   Quotas reached → soft failure → recontextualization or fallback.

6. **Auditability (Σ + Ψ)**
   All resource transitions are integrated into a stable accounting ledger.

---

# **3.8.2 Accounting Framework: The Resource Frame (RF)**

Every process/thread has an associated **Resource Frame**:

[
RF = (cpu, mem, ipc, storage, net, policy, limits)
]

RF is itself a **□-frame**: a context for interpreting resource actions.

Inside kernel state, we store:

```
struct ResourceFrame {
    CPUUsage      cpu;
    MemUsage      mem;
    IPCUsage      ipc;
    StorageUsage  storage;
    NetUsage      net;
    RoleMask      owner_roles;       // Ω
    PolicyMask    active_policies;   // Ψ
    ResourceLimits limits;           // quotas
}
```

This attaches resource accounting to operator semantics.

---

# **3.8.3 CPU Accounting (Θ + Σ + Ψ)**

CPU time is inherently **temporal**, so Θ is central here.

### **Mechanism**

On each scheduler tick (Θ):

1. **Θ:** measure elapsed time slice
2. **∇:** increment `RF.cpu.used += quantum`
3. **Σ:** commit usage
4. **Ψ:** verify limits

If limit violated:

* Ψ triggers either:

  * downgrade priority (Ω change),
  * throttle (Θ extension),
  * SIGXCPU-like trap (Φ),
  * suspension or kill (transition to exit state).

### **CPU Quota Models**

We support both **hard** and **soft** limits:

| Type       | Operator Interpretation                                             |
| ---------- | ------------------------------------------------------------------- |
| Soft limit | Θ can continue; Ψ triggers warnings or lowered priority (Ω shift).  |
| Hard limit | Ψ forbids further Θ and ∇ execution; Φ transitions to fail context. |

### **Per-Frame + Per-Role Attribution**

If a process switches role (Ω), CPU usage *in RF* is partitioned by role.

This supports kernel-level billing (“who consumed what in which privilege mode”).

---

# **3.8.4 Memory Accounting (∇ + Σ + Ψ + Χ)**

Memory actions use:

* **∇** — for actual allocation/deallocation
* **□** — switching address spaces
* **Χ** — isolation boundaries (protection domains)
* **Ψ** — limit + policy enforcement

### **Memory Allocation Workflow**

When user calls `mmap`, `brk`, or allocation occurs inside runtime:

1. **Δ:** classify the region request
2. **Ω:** verify capability to allocate
3. **Ψ:** check limits (RF.mem.used < RF.mem.max)
4. **∇:** perform allocation
5. **Σ:** commit accounting update

### **Memory Quota Violations**

If RF.mem.used > RF.mem.max:

* **Φ:** throw exception (OOM-like recontextualization)
* **Ψ:** optional kill/restart policy
* **Λ:** represent “allocation failure” (no event: allocation could not complete)

### **Isolation Guarantees (Χ)**

Memory of different frames never overlaps unless policy permits.

Isolation enforced via:

* Per-frame page tables
* Ω-driven capability sets
* Ψ rules: “user code cannot map kernel pages”, “no execute on writable pages”, etc.

---

# **3.8.5 IPC Accounting (Δ + Ω + Σ + Ψ)**

IPC (queues, channels, ports, sockets) is resource-consuming because:

* buffers occupy memory
* message sends/receives consume kernel operations
* flows may be rate-limited

### **IPC Send Operation Accounting**

Sending a message triggers:

1. **Δ:** classify destination port/channel
2. **Ω:** verify send capability
3. **Δ:** measure message size
4. **Ψ:** check message-size and message-rate limits
5. **∇:** enqueue into IPC buffer
6. **Σ:** commit size/time counters

### **IPC Receive Accounting**

Receiving a message:

* Δ: inspect availability
* Λ: if none available (non-blocking receive)
* Θ: if blocking, timeout
* Σ: count receive operations

### **IPC Quotas**

RF.ipc contains:

* max_message_bytes
* max_queue_bytes
* max_messages_per_second
* max_outstanding_requests

Violation → Ψ triggers:

* temporary blocking (Θ delay)
* forced backoff (Φ)
* capability downgrade (Ω)
* send/recv denial (Λ outcome)

---

# **3.8.6 Storage Accounting (∇ + Σ + Δ + Ψ)**

Storage usage is accounted structurally like a transactional resource.

### **Allocation / Write Operation**

1. **Δ:** resolve inode / file / block
2. **Ω:** verify write permission
3. **Ψ:** check quota (RF.storage.used + delta < max)
4. **∇:** perform write or block allocation
5. **Σ:** commit update to storage usage
6. **Ψ:** enforce consistency rules

### **Deletion / Freeing**

1. **Δ:** identify object
2. **Ω:** verify capability
3. **∇:** free blocks
4. **Σ:** decrement RF.storage.used

### **Storage Quota Events**

When additional storage cannot be allocated:

* Λ: soft failure (write returns ENOSPC)
* Φ: transaction may roll back
* Ψ: kernel may also suspend or kill the offender

---

# **3.8.7 Multi-Level Quotas (Process / Role / Group / System)**

PMS allows quotas at **multiple hierarchical levels**, each a frame:

* **Process RF**
* **User RF**
* **Role RF**
* **Container / Namespace RF**
* **System RF**

Hierarchy is implemented via **frame stacking (□)**.

During accounting:

* Increment at **local RF**
* Also increment at **all ancestor RFs**

Ψ ensures the strictest limit governs behavior.

Example:

If a container RF is near quota, even if a process RF has headroom, Ψ denies allocations.

---

# **3.8.8 Auditing & Observability (Δ + Σ + Θ + Ψ)**

For every resource-affecting event:

* Δ writes an audit record for:

  * who (role r)
  * what (resource id)
  * how much (delta)
  * when (Θ timestamp)
* Σ commits audit log entry
* Ψ ensures retention and consistency rules

Audit logs themselves may be isolated via Χ and subject to storage quotas.

---

# **3.8.9 Policy Integration (Ψ): Resource Governance**

Policies express invariants like:

* “No process may allocate > 2GB total memory.”
* “Containers cannot exceed 10% of system CPU.”
* “IPC send rate must not exceed 10k msgs/sec.”
* “Write operations cannot exceed storage class guarantee.”

A Ψ-rule activates:

[
Ψ_{resource_limit} : RF.x.used > RF.x.max \Rightarrow \text{deny or reframe}
]

Possible reactions:

### Soft reaction:

* Θ: delay
* Ω: reduce priority
* Φ: notify process

### Hard reaction:

* Λ: return failure
* Φ: abort syscall
* Kill: place process in exit state

We explicitly encode actions as operator transitions, so the model is machine-verifiable.

---

# **3.8.10 Summary**

PMS resource accounting is:

| Resource | Dominant Ops | Notes                                          |
| -------- | ------------ | ---------------------------------------------- |
| CPU      | Θ, Σ, Ψ      | Temporal; fairness and quotas encoded by Θ + Ψ |
| Memory   | ∇, Σ, Ψ, Χ   | Frames (□), isolation (Χ), OOM handling (Φ/Λ)  |
| IPC      | Δ, Ω, Σ, Ψ   | Sends/receives, queue length, rate limits      |
| Storage  | ∇, Σ, Ψ      | Journaling, quota enforcement, Δ resolution    |

All accounting flows reduce to:

[
Δ ;→; Ω ;→; Ψ ;→; ∇/□/Χ ;→; Σ ;→; Ψ
]

This prepares us for Section **4: Memory & Storage Subsystems**, since the quota system and accounting model feed directly into:

* VM architecture (4.1)
* Allocation & reclamation (4.2)
* Filesystem consistency (4.3)

---

# **4. Memory & Storage Subsystems**

## **4.1 Virtual Memory & Frames (□, Χ, Φ)**

**address spaces, paging, segmentation**

This section defines the PMS-native virtual memory model.
It unifies *address spaces*, *memory protection*, *segmentation/paging*, *isolation*, and *context switching* under the operator triad:

* **□ — Frame** → defines addressable context (segments, page tables, stack frames, code/data frames)
* **Χ — Distance / Isolation** → process boundaries, sandboxing, read/write/exec protection
* **Φ — Recontextualization** → context switches, page faults, mapping changes, versioned memory views

This forms the kernel’s full VM abstraction.

---

# **4.1.1 Conceptual Model: Memory as a Set of Frames (□)**

In PMS, **memory is not a flat array**.
It is a *hierarchy of frames*, each representing a bounded region of interpretable state.

### **Definition: Memory Frame (□)**

A frame is:

[
\text{Frame} = (base, size, type, perms, meta)
]

Where:

* **base** – physical or virtual base address
* **size** – extent
* **type** – CODE, DATA, STACK, HEAP, MMIO, KERNEL, USER, SHARED, etc.
* **perms** – {r, w, x, u, k, …} capabilities
* **meta** – policy hooks, cacheability, page size, NUMA domain, etc.

The CPU-level **FR register** selects the **current execution context**, but OS-level memory management tracks *many* frames per process:

```
PAddr Space → [Physical Frames]
VAddr Space → [Virtual Frames / Mappings]
Process     → [FrameSet_p = {code, data, heap, stack, shared, ipc, …}]
```

A **process address space** is simply a *set of frames* plus a *resolution mechanism* (page tables / segmentation), all mediated by □.

---

# **4.1.2 Virtual Address Resolution (□ + Φ)**

A virtual address VA is interpreted under the current frame context (□):

[
PhysAddr = Resolve(VA, FrameSet_p)
]

Resolution performs:

1. **Δ** — classify VA: which segment/page does it belong to?
2. **□** — select the corresponding frame
3. **Φ** — if mapping is missing or invalid → page fault → recontextualize context
4. **Ω** — check privilege and capability constraints
5. **Σ** — integrate write results into stable memory state when applicable

### **Two structural strategies are permitted:**

---

## **(A) Segmentation-style resolution (pure □)**

A set of contiguous frames:

```
[ code_frame | data_frame | heap_frame | stack_frame ]
```

VA → pick frame by interval membership.

Good for:

* small OS
* embedded systems
* simpler reasoning

---

## **(B) Paging-style resolution (□ + Δ classification per page)**

Virtual space divided into pages; each page references a frame:

```
VA → page_index → PageTable[p] = FrameId → physically mapped frame
```

Δ identifies the page; □ supplies the frame; Φ handles faults.

Paging advantages:

* external fragmentation eliminated
* dynamic memory allocation simpler
* copy-on-write (COW) natural
* isolation and sharing are easier

---

# **4.1.3 Process Address Space Construction (□, Χ, Ψ)**

A process is assigned a **FrameSet_p** by the kernel:

```
FrameSet_p = {
    CodeFrame,
    DataFrame,
    HeapFrame,
    StackFrame,
    IPCFrames[],
    SharedFrames[],
    KernelGatewayFrame
}
```

### **Χ ensures isolation:**

* A process can only access frames explicitly in its FrameSet_p.
* All cross-frame accesses must pass:

  * capability checks (Ω)
  * policy gates (Ψ)
  * optional sandbox filters (Χ-restriction masks)

### **Ψ enforces invariants:**

* read-only code
* stack non-executable
* heap non-executable
* user cannot map kernel frames
* cannot escape sandbox or current namespace

If any invariant is violated → **Φ fault (recontextualization) → kernel handler**.

---

# **4.1.4 Frame Transitions & Context Switching (Φ + □ + Ω)**

A context switch is **not primarily “switch registers”**.
It is: **change which frames define the meaning of memory accesses**.

### **User → Kernel (syscall/trap)**

Sequence:

1. Φ — trap/exception entry (as defined in 2.4)
2. Ω — switch role to kernel
3. □ — switch FR to kernel frame set
4. Χ — isolate kernel from user memory
5. Execute handler
6. Φ — return via EXC_RET → restore frames
7. Ω — role → user
8. □ — restore user frameset

### **Kernel → User (return)** is symmetric.

This is a *frame recontextualization* governed by Φ.

---

# **4.1.5 Paging/PTE Structure (□ + Ω + Ψ)**

Each page table entry (PTE) is a frame descriptor:

[
PTE = (FrameId, perms, flags, meta)
]

**perms** enforce Ω capabilities:

* r: load
* w: store (∇)
* x: instruction fetch (Δ decode)

**flags** can include:

* user / kernel domain
* copy-on-write
* dirty, accessed
* present / not-present
* shared / private

**meta** supports:

* versioned views (Φ)
* isolation scopes (Χ)
* NUMA locality
* encryption metadata

### **Page faults = Φ events**

Triggered on:

* accessing unmapped page
* write to COW page
* write to read-only page
* execute on non-exec page
* user touching kernel frame

Flow:

1. Δ — CPU detects violation
2. Φ — trap
3. kernel handler resolves frame (e.g., map, fault, kill)
4. □ — updates page table
5. return via Φ-exit

---

# **4.1.6 Copy-on-Write (Σ + Φ + Χ)**

COW frames give efficient fork & snapshot semantics.

### **Process fork():**

1. Duplicate address space metadata, not memory
2. All writable pages → marked **COW**
3. Frames shared between parent and child → Χ enforced
4. On write (∇) to shared page:

   * Δ — detect COW violation
   * Φ — COW fault
   * □ — allocate new frame
   * Σ — commit new frame, update mapping
   * continue execution

This sequence is *structurally perfect*:

```
Δ (detect) → Φ (recontextualize) → □ (new mapping) → ∇ (apply write) → Σ (commit)
```

---

# **4.1.7 Memory Protection Model (Χ, Ω, Ψ)**

Protection is enforced through:

### **Χ — Isolation domains**

* Process-level
* Thread-level sandbox
* VM / container boundary
* Shared memory visibility rules

### **Ω — Capabilities**

* Which frames can be mapped
* Which perms allowed (r/w/x)
* Which syscalls may change mappings

### **Ψ — Global invariants**

Examples:

* “Kernel frames must not be executable in user mode.”
* “W^X policy: no frame may be writable and executable simultaneously.”
* “All shared frames must have stable permissions across processes.”

Violations → Φ fault → handler → either resolve or kill process.

---

# **4.1.8 Segmentation as a Structured □-Hierarchy**

Segmentation becomes natural in PMS:

### **Nested Frames**

```
Process Frame (□)
 ├── CodeFrame
 ├── DataFrame
 ├── HeapFrame
 └── StackFrame
```

Operations like:

* changing stack frame → □
* entering function frame → □
* switching privilege domain → Ω + □
* returning to previous context → Φ + □

This aligns with the *frame algebra* used earlier for calling conventions.

---

# **4.1.9 Shared Memory & IPC Frames (□ + Χ + Ω)**

Processes may share frames explicitly:

```
SharedFrame[fid] → mapped into multiple FrameSet_p
```

Χ ensures:

* sharing is opt-in
* permissions must match
* Ψ prohibits conflicting usage (e.g., both writable unless controlled)

Use cases:

* zero-copy IPC
* shared ring buffers
* graphics buffers
* shared libraries (x-only)

---

# **4.1.10 Dynamic Memory Management (Heap) (∇ + Σ + Ψ)**

Heap operations:

* `malloc` → allocate slice within HeapFrame
* `free` → mark slice free
* potential GC integration (future section 4.2)

Allocator’s duties:

* track free lists / trees
* obey boundaries of HeapFrame
* ensure fragmentation stays within policy limits (Ψ)
* issue Σ commits when blocks become globally visible or shared

---

# **4.1.11 Advanced: Versioned Memory Contexts (Φ)**

Φ allows the OS to reinterpret memory under new rules:

### Examples:

* Live process migration
* Hot-patching code pages
* Switching ABI modes
* Rebinding shared libraries
* Transactional memory snapshots

Memory versioning flow:

1. Φ — reframe memory context
2. □ — switch to new frame set
3. Update mappings
4. Resume execution in new version

All this without changing the logical program state (s_c), just its **interpretation frame**.

---

# **4.1.12 Summary**

The PMS-driven virtual memory model rethinks addresses and mappings as **structured context operations**, not raw integer dereferences.

### **Core conceptual triad**

| PMS Operator              | Role in VM                                      | Examples                                           |
| ------------------------- | ----------------------------------------------- | -------------------------------------------------- |
| **□ Frame**               | defines memory context & address interpretation | segments, pages, stack frames, kernel/user frames  |
| **Χ Isolation**           | prohibits illegal cross-context access          | process isolation, sandboxing, shared-memory rules |
| **Φ Recontextualization** | handles faults, traps, frame changes            | page faults, syscalls, migration, ABI switch       |

### **Outcomes**

* Unified segmentation and paging
* Clean representation of syscall transitions
* Natural modeling of COW, shared memory, and reentrancy
* Isolation and permissions encoded via Χ and Ω
* All protection via Ψ invariants
* Page faults and context switches elegantly represented as Φ

---

# **4.2 Allocation & Reclamation – Heaps, Pools, GC/RC**

*(∇, Σ, □, Ω, Χ, Ψ, Φ)*

This section formalizes **dynamic memory management** in PMS-OS using PMS operators as the governing mechanisms.
It covers:

* Heap structure
* Allocation and free
* Pools and slab allocators
* Reference counting & Garbage Collection
* Safety rules (Ω, Χ, Ψ)
* Failure semantics (Λ, Φ)

Everything is expressed in the same structural form used for the CPU, kernel, and virtual memory.

---

# **4.2.1 Heap as a Structured Frame (□)**

Each process contains a **HeapFrame** within its FrameSetₚ:

[
HeapFrame = (base, size, perms={r,w}, type=HEAP, meta)
]

The heap is **not** an undifferentiated region.
It is a hierarchical set of *allocation subframes*:

```
HeapFrame (□)
 ├── BlockFrame[0]
 ├── BlockFrame[1]
 ├── …
 └── BlockFrame[N]
```

Each **BlockFrame**:

[
BlockFrame = (addr, size, state ∈ {free, used}, meta)
]

Allocators manipulate these subframes through ∇, Σ, and occasionally Φ.

---

# **4.2.2 Allocation Semantics (∇ + Σ)**

An allocation request of size *n* is:

[
ptr = alloc(n)
]

### Allocation algorithm in PMS operator terms:

1. **Δ — classify request**
   Determine size class, alignment, pool, etc.

2. **□ — select candidate frame(s)**
   Choose appropriate free BlockFrame or pool frame.

3. **Ω — privilege check**
   Ensure the caller is allowed to expand heap or use shared pools.

4. **∇ — allocate**
   Update the BlockFrame:

   * mark as used
   * split if necessary
   * update free lists / trees

5. **Σ — commit allocation**
   The updated allocator metadata becomes globally visible inside the process.

6. Return pointer.

### Invalid Case → Λ or Φ

If no block is large enough:

* **Λ** if heap expansion is optional (try other alloc strategies)
* **Φ** if expansion requires recontextualization (e.g., map new page)

---

# **4.2.3 Free / Reclamation Semantics (∇ + Σ)**

Freeing memory:

[
free(ptr)
]

Steps:

1. **Δ — validate ptr**
   If invalid → Φ fault (use-after-free or foreign pointer).

2. **∇ — mark block as free**
   Update BlockFrame.state = free.

3. **∇ — coalesce adjacent free blocks**
   Optional, depends on allocator.

4. **Σ — commit free**
   Make block available for new allocations.

### Safety Enforcement (Ψ)

Policies ensure:

* double-free detection
* pointer validity
* free only inside HeapFrame
* prevention of freeing kernel/shared frames

Violation → Φ → kernel terminates process or applies recovery.

---

# **4.2.4 Pool / Slab Allocators (Α + □ + Σ)**

Pools and slabs are expressed naturally using **Α patterns**:

```
Α_slab(size_class):
    pre-allocated FrameSet:
        SlabFrame
        ObjectFrame[i]
```

Allocation from a slab:

* Δ classify object size
* □ select appropriate slab
* ∇ toggle object state “free → used”
* Σ finalize

Advantages:

* constant-time alloc/free
* reduced fragmentation
* fits well with PMS’s structured frame model

Shared kernel pools (e.g., for IPC messages) require Ω/Ψ enforcement since cross-process allocation is involved.

---

# **4.2.5 Reference Counting (RC) (∇ + Σ + Ω + Ψ)**

Reference counting is a first GC model expressible purely in PMS operators.

For each allocated object:

[
refcount(o) ∈ s_c
]

### Increment (retain):

* Ω check capability to share object
* ∇ increment counter
* Σ commit update

### Decrement (release):

* ∇ decrement counter
* if result = 0 → **trigger free sequence**
* Σ finalize

Ψ forbids:

* overflow
* RC underflow
* cross-process sharing without appropriate permissions

Χ constraints isolate which processes may access the object.

---

# **4.2.6 Mark & Sweep GC (Θ + Δ + ∇ + Σ + Χ)**

Garbage collection can be described as a **Θ-sequenced traversal** of reachable frames:

### **Mark phase**:

1. Θ — enter GC cycle
2. Δ — identify roots
3. Δ — inspect pointers in each reachable object
4. ∇ — mark reachable objects
5. Χ — prevent concurrent mutation (stop-the-world) or use barriers

### **Sweep phase**:

1. Θ — sweep init
2. Δ — classify blocks: marked vs unmarked
3. ∇ — free unmarked blocks
4. Σ — commit new heap state

Policies (Ψ) determine:

* GC triggers
* max heap size
* behavior under memory pressure
* fairness across processes

---

# **4.2.7 Copying / Generational GC (Φ + □ + Σ)**

Copying GC uses **Φ recontextualization** of heap frames:

### Steps:

1. Φ — move to “new heap frame”
2. □ — allocate to-space frame
3. Δ — scan objects
4. ∇ — copy live objects into to-space
5. Σ — integrate new heap and discard old frame
6. Update block pointers

Χ ensures no other thread sees intermediate garbage.

---

# **4.2.8 Memory Pressure, OOM Handling (Λ + Φ + Ψ)**

When memory is low:

* **Λ** triggers (“non-event”: allocation expected but cannot be fulfilled yet)
* Kernel reacts:

  * reclaim pages
  * run GC
  * shrink caches
* If still failing → **Φ OOM recontextualization**

  * kill process
  * send signal
  * enter low-memory mode

Ψ enforces system-wide invariants, such as:

* kernel must not run out of memory
* certain system processes cannot be OOM-killed

---

# **4.2.9 Concurrency Safety (Χ + Ω + Ψ + Θ)**

Concurrent allocation & free across threads:

* Χ defines heap isolation or shared heap subcontexts
* Ω controls who may allocate on shared heaps
* Θ defines ordering of allocator structures
* Ψ ensures:

  * ABA prevention
  * lock-free correctness rules
  * memory model constraints (ties into 2.7)

---

# **4.2.10 Summary**

| Concern     | PMS Operator Backbone | Notes                                       |
| ----------- | --------------------- | ------------------------------------------- |
| allocation  | Δ, □, ∇, Σ            | classify → choose frame → allocate → commit |
| free        | Δ, ∇, Σ               | validate → free → integrate                 |
| GC          | Θ, Δ, ∇, Σ            | traversal, marking, sweeping                |
| isolation   | Χ                     | per-process heaps, safe sharing             |
| permissions | Ω                     | who may allocate/free                       |
| invariants  | Ψ                     | memory safety rules                         |
| faults      | Λ, Φ                  | out-of-memory, invalid ptr                  |

The heap becomes a consistent PMS-structured subsystem: allocations are ∇ actions inside a □ region governed by Ω/Ψ and finalized via Σ.

---

# **4.3 Filesystem Architecture (Σ, Ψ) — directories, handles, permissions, journaling**

*(Operators: Δ, ∇, □, Α, Ω, Χ, Θ, Φ, Λ, Σ, Ψ)*

The PMS filesystem (PMS-FS) is a **frame-structured storage system**.
Every file, directory, mount, transaction, capability, or journal entry is a **Frame (□)**; every filesystem operation is a **PMS operator sequence**.
This makes the FS a *first-class PMS subsystem*, fully consistent with the compute/memory models.

---

# **4.3.1 Core Data Model: The Filesystem as a Frame Tree (□ + Α + Ω + Ψ)**

The filesystem is a **tree (or DAG with hardlinks) of frames**:

```
FSRoot (□)
 ├── DirFrame("/etc")
 │     ├── FileFrame("config")
 │     └── FileFrame("policy")
 ├── DirFrame("/usr")
 └── DirFrame("/var")
       └── DirFrame("log")
```

Each frame has:

[
FileFrame = (id, name, type, perms, owner, data, meta)
]
[
DirFrame = (id, name, perms, owner, entries, meta)
]

Where:

* **perms / owner** use Ω (roles, capabilities)
* **entries** is a mapping `name → FrameID`
* **meta** includes timestamps (Θ), journaling info (Σ), policy hooks (Ψ)

**Σ** governs all *persistent integration*: writes become visible only when a Σ commit occurs.

**Ψ** enforces FS-level invariants such as:

* no crossing isolation boundaries (Χ)
* correct permission enforcement (Ω)
* quota limits
* consistency requirements

---

# **4.3.2 Directory Semantics (Δ, ∇, Σ, Ψ)**

### **Lookup (Δ)**

A directory is a classification frame. Looking up a name is:

[
DirFrame \xrightarrow{\Delta(name)} entry
]

Δ returns:

* exists → branch to file/directory handler
* missing → Λ (non-event) or Φ (error recontextualization)

### **Create Entry (∇ + Σ)**

Creating a new file:

1. Δ: check name not present
2. Ω: permission to create in this dir
3. ∇: create FileFrame, add to directory entries
4. Σ: commit update to directory structure

### **Remove Entry (∇ + Σ + Ψ)**

Deletion:

1. Δ: find entry
2. Ψ: check constraints (e.g., cannot delete non-empty dir)
3. ∇: unlink entry
4. Σ: commit change
5. optional: GC or reclamation for underlying blocks

---

# **4.3.3 File Handles & Open File Tables (□, Ω, Χ)**

Opening a file creates a **HandleFrame**:

[
HandleFrame = (file_id, mode, offset, perms, isolation)
]

Process Open File Table = a set of HandleFrames indexed by FD numbers.

### Open:

1. Δ: locate file
2. Ω: check read/write/exec permission
3. □: create a new HandleFrame for this process
4. Χ: isolate based on namespace/container
5. Σ: return handle ID

Handles allow access without re-checking directory path each time, but Ψ may enforce per-op checks.

---

# **4.3.4 File I/O Semantics (Δ, ∇, Θ, Σ, Ψ)**

### **Read (Δ + Θ)**

```
read(fd, n):
    Δ: check handle validity
    Θ: advance read offset
    return data
```

No write occurs → no Σ required.
Ψ may enforce:

* no reads past EOF
* isolation constraints (Χ)

### **Write (∇ + Σ)**

```
write(fd, data):
    Δ: classify size, location
    Ω: check write permission
    ∇: modify underlying storage blocks
    Σ: commit write according to journaling mode
```

### Write Strategies:

* **Σ(write-through)**: synchronous commit
* **Θ-buffered + Σ-later**: delayed commit
* **Transactional (Α-pattern)**: group multiple writes → single Σ

---

# **4.3.5 Permissions & Role System (Ω + Ψ)**

Permissions (Ω) determine what operations are allowed.
Policies (Ψ) define global or directory-level rules:

Examples:

* Ψ: no world-writable dirs
* Ψ: user may only write within its home subtree
* Ψ: append-only logs
* Ψ: immutability windows (cannot modify for X seconds → Θ + Ψ)

Ω permissions can be granular:

```
r   read
w   write
x   execute
c   create
d   delete
p   privilege escalate (CAP-like)
```

Each checked at Δ or ∇ entry points.

---

# **4.3.6 Mounts & Namespaces (□ + Χ + Φ + Ψ)**

A mount is a **Frame recontextualization (Φ)**:

```
Φ: rebind directory-frame pointer → new root or sub-tree
```

Used for:

* process namespaces
* container isolation
* per-thread or per-process view of FS
* overlay filesystems (union mounts)

Isolation (Χ) enforces view boundaries.

Ψ ensures:

* mount points do not violate system policies
* read-only mounts remain immutable
* overlay merges follow consistent Σ rules

---

# **4.3.7 Journaling / Transactions (Σ + Α + Θ + Φ)**

The FS journal is explicitly Σ-centric.
A journal entry is:

[
JournalEntryFrame = (op_seq, timestamp, state)
]

### **Write-ahead logging (WAL)**:

1. **Α-pattern** expands fs operations into a canonical ordered sequence.
2. **Σ(journal-write)** records intended updates.
3. **Θ** orders log entries by commit time.
4. **Σ(final)** applies updates to FS structures.
5. **Φ(recovery)** recontextualizes state after crash.

This provides:

* crash consistency
* atomic directory updates
* transactional file ops

### Transaction Example:

```
begin_tx:
    Α: open transactional frame
write(file):
    ∇ modify buffers
commit:
    Σ(journal)
    Σ(apply changes)
abort:
    Φ rollback
```

Multi-operation transactions become first-class PMS patterns.

---

# **4.3.8 Crash Recovery (Φ + Σ + Θ)**

Upon reboot:

1. Θ: replay journal in timestamp order
2. Δ: identify completed vs incomplete transactions
3. Φ: recontextualize filesystem state
4. Σ: integrate all valid updates

Any incomplete α-transaction is rolled back (Φ recovery path).

---

# **4.3.9 Quotas & Limits (Ω + Ψ + Σ)**

System-wide or per-user quotas enforced structurally:

* Ω: capability to allocate disk space
* Ψ: policies restricting max blocks, max inodes
* Σ: applied after each allocation

Quota violation leads to:

* Λ (write deferred)
* Φ (error)

---

# **4.3.10 Summary Table**

| Operation      | Operators     | Structural Meaning                 |
| -------------- | ------------- | ---------------------------------- |
| lookup         | Δ             | distinction in directory frame     |
| open           | Δ, Ω, □, Χ, Σ | permission + handle frame creation |
| read           | Δ, Θ          | classify + move offset             |
| write          | Δ, Ω, ∇, Σ    | update & commit                    |
| mkdir/rmdir    | Δ, ∇, Σ, Ψ    | create/remove frames               |
| mount          | Φ, □, Χ, Ψ    | recontextualize FS tree            |
| fsync          | Σ             | integrate pending writes           |
| journaling     | Α, Σ, Θ, Φ    | transactional write discipline     |
| crash recovery | Θ, Δ, Φ, Σ    | ordered reconstruction             |

Filesystem behaviour is now fully grounded in the PMS axioms.

---

# **4.4 Block Devices & Drivers — device abstraction as frames & roles**

*(Operators: □, Ω, Χ, Φ, Σ, Δ, ∇, Θ)*

This section defines the PMS model of block devices, drivers, and I/O pipelines.
The goal is to make device access **structurally identical** to all other subsystems:
devices are **frames (□)**, access is governed by **roles (Ω)** and **isolation (Χ)**, driver transitions use **Φ**, and durable updates use **Σ**.

This forms the unified basis for both traditional OS block drivers **and** PMS-native virtual devices (network-backed, memory-backed, or distributed).

---

# **4.4.1 Block Devices as Frames (□)**

Every block device is represented as a **DeviceFrame**:

[
DeviceFrame = (id,; type,; blocksize,; capacity,; perms,; owner,; ops,; state)
]

Where:

* **type** ∈ {DISK, SSD, NVMe, RAMDISK, VDEV, LOOP, NET-BLOCK, …}
* **blocksize** and **capacity** define logical geometry
* **perms, owner** handled via Ω (capabilities)
* **ops** is a driver-defined map of (Δ, ∇, Σ)-typed operations
* **state** includes queues, caches, pending I/O, etc.

In PMS, a block device is **just another frame** whose “data” is a sequence of fixed-size blocks:

[
blocks: \mathbb{N} \to Byte^{blocksize}
]

Accessing a device requires entering its frame context:

```
FRM_ENTER dev_id   ; □ — enter device context
```

Device reads/writes are then ∇ operations interpreted relative to this frame.

---

# **4.4.2 Driver Architecture (Δ, ∇, Θ, Φ, Ω)**

A **driver** in PMS is not a monolithic privileged blob — it is a structured machine made of operators:

### DriverFrame (□)

```
DriverFrame = {
    device_id,
    ops: {
        Δ_identify,
        Δ_check_bounds,
        ∇_read_blocks,
        ∇_write_blocks,
        Σ_commit,
        Φ_recover,
        Θ_dispatch,
        Ω_permission_check
    },
    queues,
    cache,
    state
}
```

### Operators in the driver:

| Operator | Driver Meaning                                                    |
| -------- | ----------------------------------------------------------------- |
| **Δ**    | identify device, classify I/O request type, check block alignment |
| **Ω**    | check role/capability for I/O (e.g., user can read but not write) |
| **Θ**    | dispatch requests over a schedule (queue processing)              |
| **∇**    | perform the actual block read/write on hardware or backing store  |
| **Σ**    | commit writes (flush buffers or guarantee ordering)               |
| **Φ**    | error handling: retries, remapping bad blocks, failover           |

Drivers therefore become **PMS-UM submachines** attached to device frames.

---

# **4.4.3 I/O Request Pipeline (Δ → Ω → Θ → ∇ → Σ → Φ)**

A block I/O request follows a canonical PMS operator sequence:

### **1. Δ — Request Classification**

```text
Δ(request):
    - identify operation (READ/WRITE)
    - extract block index + length
    - check logical bounds
```

### **2. Ω — Permission Check**

Role/capability enforcement:

* READ requires `cap_read`
* WRITE requires `cap_write`
* FLUSH requires `cap_admin` or device-specific caps

If Ω fails → driver emits Φ(error-access-denied).

### **3. Θ — Scheduling / Dispatch**

Enqueue into driver scheduling structure:

* FIFO
* Deadline
* Elevator / C-LOOK
* Priority-based

Scheduler uses Θ to serialize and order operations.

### **4. ∇ — Execute the I/O**

For each scheduled request:

* ∇ reads from underlying device frame:
  [
  blocks[i] \mapsto buffer
  ]
* ∇ writes:
  [
  buffer \mapsto blocks[i]
  ]

Optional caching inside driver state.

### **5. Σ — Commit / Ordering**

Ensures:

* write ordering constraints (barriers)
* transaction durability (for journaled filesystems)
* flushing device cache if necessary

### **6. Φ — Recontextualization for Errors or Retries**

Driver may:

* retry (after Θ backoff)
* reframe device view (mark block bad, remap)
* escalate error to filesystem or kernel

This completes the structural unified I/O lifecycle.

---

# **4.4.4 Device Isolation Model (Χ)**

Block devices are **isolation boundaries**.

Each DeviceFrame has an associated Χ-domain:

[
Χ(device) = { allowed_frames : caps }
]

When entering a device context (via FRM_ENTER):

* Χ enforces that only permitted regions of memory, buffers, descriptors may be accessed.
* Isolation prevents:

  * DMA into unauthorized memory
  * direct device → process memory writes
  * bypassing filesystem access controls

### DMA Example (structured):

If DMA is supported:

* A DMARegionFrame is created (□)
* Χ restricts DMA to that frame only
* ∇ DMA ops copy block into DMARegionFrame buffer

If DMA violates policy → Φ(exception) or Ψ(system halt).

---

# **4.4.5 Storage Stack as Composed Frames (□ + Α)**

Block device → optional layers → filesystem.

```
[Physical DeviceFrame]
        ↓ (□)
[PartitionFrame]
        ↓ (□)
[VolumeFrame / RAIDFrame / EncryptedFrame]
        ↓ (□)
[Filesystem Root Frame]
```

### Examples of α-patterns (Α) for layered devices:

* **RAID-1 mirror pattern:**

```
PATTERN RAID1:
   ∇ write block to devA
   ∇ write block to devB
   Σ commit if (both successful) else Φ(recover)
```

* **Encryption frame:**

```
READ:
    ∇ read encrypted block
    ∇ decrypt block
    return plaintext
WRITE:
    ∇ encrypt block
    ∇ write encrypted block
    Σ
```

Each layer in the stack is itself a PMS operator-based machine.

---

# **4.4.6 Interrupt Path for Block Devices (Φ + Θ + Λ)**

Block devices generate interrupts for:

* I/O completion
* I/O error
* queue empty
* device hotplug

### Interrupt handling sequence:

1. **Φ(entry)** — trap from device
2. **Δ** — driver identifies cause
3. **Θ** — driver schedules handling (dequeue next request, complete current)
4. **Σ** — optional commit of completion metadata
5. **Λ** — if device becomes idle (no pending events)

This integrates naturally with the CPU interrupt/trap model (2.4).

---

# **4.4.7 Hotplug & Dynamic Reconfiguration (Φ + Ψ + □)**

When a device is inserted/removed:

### Hotplug sequence:

1. **Φ(hotplug-event)** — OS recontextualizes I/O subsystem
2. **Δ** — driver identification
3. **□** — create or remove the DeviceFrame
4. **Ψ** — enforce policies (e.g. only root may mount new device)
5. **Σ** — integrate updated FS/device tree state

Failures produce:

* Φ(retry / fallback driver)
* Λ(timeout waiting for device presence)
* Ψ(reject unauthorized device)

---

# **4.4.8 Error Handling & Recovery (Φ, Σ, Θ)**

Driver uses Φ for:

* block remapping
* retry logic (Θ-based exponential backoff)
* transition to degraded modes (mirror half failed)
* integrity restoration

Σ ensures all recovery updates become consistent (e.g., mark block as bad).

---

# **4.4.9 Why PMS Device Model is Superior to Classical OS Models**

Traditional OSes treat drivers as opaque code running with elevated privilege.
PMS instead treats drivers as **operator-constrained machines**:

* All operations typed as Δ/∇/□/Ω/Θ/Σ/Φ
* Verifiable behavior (section 11: IR & model checking)
* Capability-bound (Ω), format-bound (□), isolation-bound (Χ)
* Structured error-handling (Φ)
* Clear transactional semantics (Σ)

Drivers cannot violate invariants unless Ψ permits it.

---

# **4.4.10 Summary Table**

| Layer                   | Operators | Structural Meaning                |
| ----------------------- | --------- | --------------------------------- |
| DeviceFrame             | □, Ω, Χ   | identity, capabilities, isolation |
| Driver ops              | Δ, ∇      | classify and execute I/O          |
| Scheduling              | Θ         | dispatch order                    |
| Timeouts                | Λ         | non-event when device silent      |
| Error handling          | Φ         | recontextualize / retry / recover |
| Write durability        | Σ         | commit to storage                 |
| Stacking (RAID, crypto) | Α, Σ, Φ   | reusable patterns                 |

Block devices now fully integrate with the PMS universal model.

---

# **4.5 Caching & Buffer Management — FS/Buffer Cache, Write-Back Semantics**

*(Operators: Δ, ∇, Θ, Λ, □, Ω, Χ, Φ, Σ, Α)*

This section defines the unified PMS caching and buffer-management model for block storage and filesystems.
It treats caches and buffers as *formal PMS frames*, with strict sequencing, isolation, commit, and policy guarantees.

Caching is **not** an afterthought—it becomes a *first-class operator-structured subsystem*.

---

# **4.5.1 The PMS Cache Model: CacheFrame (□ + Χ)**

A cache is a **Frame** with controlled visibility and isolation constraints:

[
CacheFrame = (id,; type,; mapping,; state,; perms,; owner)
]

Where:

* **type** ∈ {BLOCK_CACHE, PAGE_CACHE, FS_BUFFER_CACHE}
* **mapping:** block/page → cached data buffer
* **state:** metadata: dirty/clean bits, LRU counters, refcounts
* **perms:** access governed by Ω (filesystem, kernel, device-driver roles)
* **isolation:** Χ ensures user processes cannot see other processes’ cached data directly

CacheFrames are entered implicitly by the filesystem, explicitly by drivers or kernel routines:

```
FRM_ENTER cache_id    ; □
```

Within the CacheFrame, ∇ operates on cached buffers instead of physical storage.

---

# **4.5.2 Cache Lifecycle (Δ → Ω → ∇ → Θ → Σ / Λ / Φ)**

Every read/write request goes through the following canonical operator sequence:

### **1. Δ — Lookup / Distinction**

Determine whether the block/page is in cache:

```
Δ(cache_lookup):
    if mapping.contains(block):
        hit
    else:
        miss
```

The distinction sets flags in meta-state m (hit/miss).

### **2. Ω — Capability Check**

Does the caller have permission to access this cached item?

* Read: cap_read
* Write: cap_write
* Metadata updates: cap_fs_admin

If Ω fails → Φ(access error).

### **3. ∇ — Load Into Cache (on miss)**

If miss:

* ∇ issues block read (via driver)
* Buffer allocated and inserted into CacheFrame

```
∇ load_block -> cache[block]
```

Dirty bit = false.

### **4. Θ — Scheduling / Access Sequencing**

Cache management often interleaves multiple operations:

* LRU updates
* multi-threaded reads/writes
* lock ordering

Θ ensures sequential consistency at the cache-level.

### **5. ∇ — Modify Cached Buffer**

On writes:

```
∇ write bytes to cachebuffer
dirty = true
```

This is *purely in-cache*, not committed yet.

### **6. Σ / Λ / Φ — Finalization**

Depending on policy and state:

* **Σ (commit)**: write-back to device
* **Λ (non-event)**: delay write if sync criteria not met
* **Φ (recontextualization)**: remap, retry, fallback, handle device errors

This lifecycle is identical across FS, drivers, virtual devices, journal layers, etc., enabling rigorous reasoning.

---

# **4.5.3 Buffer States & Transitions (Σ-driven)**

Each buffer goes through a well-defined state machine:

```
CLEAN → DIRTY → FLUSHING → CLEAN
     ↘ Φ(error) → RECOVERY → CLEAN/DEAD
```

### **Transitions:**

| PMS Operator | Transition Meaning                        |
| ------------ | ----------------------------------------- |
| Δ            | Check if buffer exists / check dirty flag |
| ∇            | Modify buffer (→ DIRTY), mark metadata    |
| Θ            | Schedule flush or eviction                |
| Σ            | Commit to storage (DIRTY → CLEAN)         |
| Λ            | Not-yet-ready event (delay write)         |
| Φ            | Error during flush → recovery path        |

Buffers that fail recovery may be marked DEAD, triggering upper FS to recreate structures.

---

# **4.5.4 Write Policies: PMS-Structured**

The PMS operator set provides a *formal vocabulary* for describing all classical cache write policies.

### **1. Write-Through (Σ after every ∇)**

Sequence:

[
∇write \rightarrow Σcommit
]

No dirty state persists beyond a single operation.
Easy to reason; slow on some hardware.

### **2. Write-Back (Σ deferred)**

Sequence:

[
∇write \rightarrow Θ(delay) \rightarrow Σcommit
]

Optional Λ if device not ready:

[
Θ \rightarrow Λ (timeout) \rightarrow retry / Φ
]

### **3. Write-Around (skip cache on write)**

Sequence:

[
∇write_direct \rightarrow Σ
]

Cache unaffected unless a later read demands that block.

### **4. Log-Structured (Α-pattern)**

Expressed via Attractor pattern Α:

```
PATTERN LOG_APPEND:
    ∇ append to logbuffer
    when logbuffer_full:
        Σ flush logbuffer
```

This composes into journaling FS design (4.3).

---

# **4.5.5 Eviction Policies (Θ + Δ + Ω + Σ)**

Eviction is treated as a **temporal decision**:

### Δ — Identify candidate

Examines:

* LRU history
* access frequency
* dirty bit
* role-specific priorities (Ω)

### Ω — Permission to evict?

Some buffers belong to privileged subsystems (e.g. superblock).
Eviction may be blocked.

### Θ — Sequence / choose eviction order

Scheduler picks next buffer to evict.

### Σ — Commit if dirty

If buffer is dirty:

[
Σ(write_back)
]

### ∇ — Free buffer

After commit, buffer removed:

[
∇ delete cachebuffer
]

---

# **4.5.6 Multi-Layer Caching (Α + □ + Χ)**

Filesystems and block devices often maintain **multiple caches**:

* Block cache
* Page cache
* Directory entry cache
* Metadata cache
* Journaling intent cache

Each is a **Frame**; they can stack:

```
FRM_ENTER PageCache
FRM_ENTER BlockCache
FRM_ENTER DeviceFrame
```

The Α-pattern relations define:

* coherency rules
* ordering
* dependency (e.g. page cache depends on block cache)

Χ enforces that each layer sees only what it must; FS metadata cache is isolated from raw device blocks except via the driver.

---

# **4.5.7 Journaling & Coherency (Σ + Φ + Θ)**

The journaling model integrates tightly with the cache:

### Write sequence with intent logging:

1. ∇ modify data buffer
2. ∇ create journal entry buffer
3. Σ commit journal entry
4. Σ commit data buffer
5. Φ rollback if crash detected mid-sequence
6. Θ reorder or flush sequences in batches

This prevents torn writes and maintains FS integrity.

All journal operations are **just PMS operator sequences**.

---

# **4.5.8 Concurrency & Synchronization (Θ + Ω + Χ)**

Concurrent access to the cache requires:

* lock ordering constraints (Ω)
* temporal ordering (Θ)
* isolation rules (Χ)

### Example atomic buffer update:

```
LOCK buffer        ; Ω
Δ read state
∇ modify buffer
Σ commit (or deferred)
UNLOCK buffer      ; Ω
```

Optionally:

* Χ enforces that cross-process writes do not interfere
* Θ ensures sequential consistency

Atomicity is expressed with Σ or Σ+Ω combinations.

---

# **4.5.9 Consistency Models for Caches (Ψ)**

Ψ-layer policies define:

* when Σ must fire
* how much reordering Θ may perform
* what isolation levels Χ apply
* how metadata must be updated (Δ constraints)

Examples:

### Strong Consistency

Ψ_strong:

* writes visible immediately after Σ
* no reorder across Θ barriers
* metadata and data flushed together

### Eventual Consistency

Ψ_eventual:

* Σ deferred
* multiple ∇ modifications batched
* allow Θ to reorder non-dependent writes

### Transactional FS Consistency (Ψ_fs)

* Σ commit for journal and data
* rollback safety via Φ
* multi-buffer atomicity

The policy system makes consistency configurable and enforceable.

---

# **4.5.10 Unified Structural Summary**

| PMS Operator | Cache Meaning                                               |
| ------------ | ----------------------------------------------------------- |
| **Δ**        | lookup, metadata inspection, dirty check, eviction tests    |
| **∇**        | modify buffer, load/write data                              |
| **Θ**        | schedule flush, eviction, LRU updates                       |
| **Λ**        | delay flush, not-ready events                               |
| **Φ**        | error handling, block remapping, recovery                   |
| **□**        | frames for caches, device access, journaling layers         |
| **Ω**        | permission checks, concurrency rules, privileged buffers    |
| **Χ**        | isolation of cache layers and tenants                       |
| **Σ**        | commit to stable storage, durability                        |
| **Α**        | macro-patterns: journaling, log-structured, layered caching |

Caching becomes a **first-class, formally-typed system** within the PMS kernel, supporting:

* strong invariants
* composability
* formal verification (section 11)
* clear OS/runtime behavior
* deterministic or non-deterministic scheduling

---

# **5. IPC, Synchronization, and Events**

## **5.1 Message Passing (Δ, Ω, Λ, Θ, Φ) — queues, mailboxes, request/response**

Message passing in PMS-OS is not an “API layer”.
It is a **praxeological structure**: a rigorously operator-typed flow built from Δ, Ω, Λ, Θ, Φ (and Σ for integration, though we reserve Σ for delivery/commit semantics in 5.2).

The result is a **general, verifiable IPC substrate** that unifies:

* synchronous & asynchronous messaging
* mailboxes & queues
* request/response protocols
* interrupt-to-process delivery
* fault-tolerant remote message handing
* distributed messaging (when extended in section 7)

Everything flows directly from PMS operator grammar.

---

# **5.1.1 Conceptual Model: MessageFrame (□ + Χ)**

All messaging occurs inside **MessageFrames**, which are specialized Frame types:

[
MessageFrame = (id,; type,; queue,; perms,; owner,; meta)
]

Where:

* **type** ∈ {MAILBOX, QUEUE, CHANNEL, PIPE, PORT}
* **queue:** ordered buffer of messages
* **perms:** Ω permissions (send, receive, inspect)
* **owner:** process or kernel subsystem
* **meta:** Θ counters, Λ flags, Φ error markers

A process enters a MessageFrame to perform send/receive:

```
FRM_ENTER msg_id        ; □
```

Χ isolates each MessageFrame unless explicitly shared.

---

# **5.1.2 Message Structure**

A message is a PMS-typed object:

[
Msg = (\Delta_tag,; payload,; sender,; caps,; meta)
]

* **Δ_tag**: distinguishes message kind (REQUEST, RESPONSE, EVENT, SIGNAL, ERROR…)
* **payload**: raw data or small structured record
* **sender**: process ID, role
* **caps**: optional capabilities sent across Ω boundaries
* **meta**: timestamps (Θ), retries, hop counters

Messages are FIFO by default; additional structures (priority queues) use Θ + Ω patterns.

---

# **5.1.3 Send Semantics (Δ → Ω → ∇ → Θ → Σ)**

### **1. Δ — Distinguish the message type**

Sender determines what kind of message is being sent:

```
CMP tag, MSG_TYPE_REQUEST      ; Δ
```

This also selects the correct queue and permissions.

### **2. Ω — Capability check**

Before enqueueing, the OS evaluates:

* Does the sender have SEND permission on this mailbox/queue?
* Are required capabilities allowed to cross boundary?

```
CHK_CAP cap_send, fail_label   ; Ω
```

If forbidden → Φ (permission trap).

### **3. ∇ — Enqueue the message**

```
ENQ msgframe, Msg              ; ∇
```

This mutates the core queue state.

### **4. Θ — Temporal sequencing**

Sender-side Θ handles:

* scheduling dependencies
* message ordering (sequence numbers)
* potential backpressure

```
TICK                           ; Θ
```

### **5. Σ — Integration of send (optional)**

Some systems require send-commit semantics:

```
COMMIT_SEND msgframe           ; Σ
```

Meaning:
The message is *guaranteed* visible to receivers.

If Σ is omitted, send is “best-effort until buffer sync”.

---

# **5.1.4 Receive Semantics (Δ → Ω → Λ/∇ → Φ)**

Receiving messages is a dual structure.

### **1. Δ — Check for message availability**

```
CMP queue_length, 0            ; Δ
BEQ no_msg                     ; Δ
```

### **2. Ω — Capability check**

```
CHK_CAP cap_recv, fail        ; Ω
```

### **3. Λ — If empty: non-event**

If queue empty:

```
no_msg:
WAIT msgframe, timeout         ; Λ
```

Λ produces *non-event semantics*:

* return with timeout
* schedule another Θ-based attempt later
* or Φ if caller expects a synchronous message and absence implies fault

### **4. ∇ — Dequeue**

If message exists:

```
DEQ msgframe, Rmsg             ; ∇
```

Mutates queue state.

### **5. Φ — Recontextualization on malformed or policy-blocked message**

```
EXC_RAISE MSG_INVALID          ; Φ
```

Used when:

* message violates interface contract
* sender not allowed to send to receiver
* version mismatch (protocol-level Φ)

---

# **5.1.5 Request/Response Pattern (Α over Δ, Ω, Θ, ∇, Σ, Φ)**

Request/response is a reusable **Α-pattern**:

### **Pattern Α_REQRESP(client, server)**:

1. **Client → Server**

   ```
   Δ distinguish REQUEST
   Ω check send rights
   ∇ enqueue into server mailbox
   Θ schedule
   ```

2. **Server receipt**

   ```
   Δ check queue
   Ω check recv rights
   ∇ dequeue
   (process request)
   ```

3. **Server → Client response**

   ```
   Δ distinguish RESPONSE
   Ω check capability to reply
   ∇ enqueue to client mailbox
   Σ (commit)
   ```

4. **Client receipt**

   ```
   Δ check queue
   Λ wait if needed
   ∇ dequeue
   Φ reframe if response implies new context/state
   ```

### Algebraic form:

[
Α_{REQRESP} = (\Delta,\Omega,\nabla,\Theta)_; (\Delta,\Omega,\nabla)_; (\Delta,\Lambda/\nabla,\Phi)
]

This pattern is callable at kernel and userspace levels (via syscalls).

---

# **5.1.6 Mailboxes vs Queues (Role & Isolation Semantics)**

### **Mailbox (per-process)**

* Χ isolates mailbox to a single process.
* Ω typically grants only “owner receives / others send”.

### **Queue (shared)**

* Can be many-to-many.
* Ω enforces:

  * producer caps
  * consumer caps
  * ordering constraints (priority queues use Θ)

Isolation controlled via:

```
ISO_RESTRICT mask      ; Χ
```

allowing only specific processes to see queue contents.

---

# **5.1.7 Synchronous Messaging via Λ/Θ**

Synchronous IPC = “wait until response arrives”, implemented structurally:

```
SEND request
WAIT reply, timeout     ; Λ
IF timeout → Φ error
```

The presence of Λ in the receive path distinguishes:

* *event* (message arrives)
* *non-event* (timeout triggers fallback Φ)

Θ controls fairness and scheduling:

```
YIELD                    ; Θ – allow server to run
```

---

# **5.1.8 Interrupt → Message Unification (Φ → Δ → ∇)**

The interrupt subsystem (2.4) is structurally identical to message passing:

### Hardware interrupt → Φ trap

Φ captures the external event.

### Kernel interrupt handler constructs Msg

Δ distinguishes interrupt type
Ω checks whether delivery is allowed to this process
∇ enqueues message into process’s event mailbox

### Process later receives it via normal IPC

This gives a unified model:

* hardware events
* software messages
* timer events
* signals

all share the same Δ–Ω–Λ–Θ–Φ machinery.

---

# **5.1.9 Reliability & Delivery Semantics (Ψ + Σ + Λ)**

Ψ policies define delivery guarantees:

### **At-most-once delivery**

* Σ commits dequeue
* message discarded after read
* Ψ forbids re-delivery

### **At-least-once delivery**

* Sender keeps copy
* Σ_commit only when receiver acknowledges
* If Λ timeout → retry (∇ enqueue again)
* Controlled by Θ for backoff

### **Exactly-once delivery**

Requires:

* message IDs (Δ)
* commit protocol (Σ)
* consistency policy (Ψ_eonce)
* Φ on duplicate detection

---

# **5.1.10 Structural Summary Table**

| PMS Operator | IPC Role                                               |
| ------------ | ------------------------------------------------------ |
| **Δ**        | message type, queue state checks, branching            |
| **Ω**        | send/receive permissions, capability-passing           |
| **Λ**        | timeouts, non-event on empty queue                     |
| **Θ**        | ordering, scheduling, fairness, retries                |
| **Φ**        | message validation errors, fallback, interrupt arrival |
| **□**        | MessageFrames for queues/mailboxes/channels            |
| **Χ**        | isolate endpoints, control visibility                  |
| **∇**        | enqueue/dequeue, modify queue state                    |
| **Σ**        | commit delivery, enforce reliability                   |
| **Ψ**        | delivery policies, interface contracts                 |
| **Α**        | reusable messaging patterns (req/resp, streaming, RPC) |

Message passing in PMS-OS is therefore:

* unified
* verifiable
* policy-controllable
* compatible with concurrency
* and extensible to distributed systems (section 7)

---

# **5.2 Synchronization Primitives (Ω, Θ, Σ, Χ, Δ)**

**mutexes, semaphores, channels — structural PMS model**

In PMS-OS, synchronization **is not ad-hoc**: all primitives are strictly constructed from PMS operators and their dependency grammar.

This yields synchronization mechanisms that are:

* capability-secured (**Ω**)
* temporally ordered (**Θ**)
* isolation-preserving (**Χ**)
* distinction-driven (**Δ**)
* commit-consistent (**Σ**)
* policy-verifiable (**Ψ**)

Below is the full structural specification.

---

# **5.2.1 Core Idea: A SyncPrimitive is a Frame (□) + Role Gate (Ω) + Temporal Sequencer (Θ)**

Every synchronization construct is a specialized **□-Frame**:

[
SyncFrame = (id,; type,; state,; waiters,; perms,; meta)
]

Where:

* **type**: MUTEX, SEMAPHORE, CHANNEL, RWLOCK, FUTEX-like, EVENT-FD-like
* **state**: primitive-specific data (e.g., locked/unlocked, count, buffer)
* **waiters**: queue of threads waiting (Θ-ordered)
* **perms**: Ω roles/capabilities for lock/unlock/wait/signal
* **meta**: Θ counters, fairness markers, Λ flags, Φ exception markers

Χ isolates each SyncFrame unless explicitly shared.

---

# **5.2.2 Distinction First: Δ Guards Every Sync Operation**

Before any lock, unlock, wait, signal, or send/recv:

```
CMP SyncFrame.type, MUTEX     ; Δ
```

Or:

```
CMP state.locked, 0           ; Δ
```

**Δ establishes the precondition** for any ∇-mutation.
This enforces PMS dependency constraints (no ∇ without Δ).

---

# **5.2.3 Mutex Semantics (Ω + ∇ + Θ + Σ)**

A **mutex** is a SyncFrame with:

[
state = (locked \in {0,1},; owner)
]

### **Lock (attempt)**

Sequence:

1. **Δ** – check locked/unlocked

2. **Ω** – capability check (does caller have LOCK rights?)

3. If unlocked:

   ```
   state.locked := 1             ; ∇
   state.owner := current_tid    ; ∇
   Σ commit_lock                  ; Σ
   ```

4. If locked:

   → **Θ enqueue thread** in waiter queue
   → thread enters **blocked** state
   → scheduler context switches
   → Λ may signal timeout if waiting is bounded

### **Unlock**

1. **Δ** verify ownership
2. **Ω** check UNLOCK capability (Ω ensures correctness even in kernel bypass cases)
3. **∇** unlock mutex: `state.locked := 0; state.owner := null`
4. **Θ** pick next waiter deterministically or via fair ordering policy
5. **Σ** commit unlock + wake

In PMS, **Σ makes mutex unlocking atomic and visible** across contexts.

---

# **5.2.4 Semaphores (Ω, Θ, ∇, Σ, Λ)**

A semaphore has:

[
state = (count \in \mathbb{N},; max)
]

### **wait(P) / down():**

1. **Δ** compare `count`

2. If `count > 0`:

   ```
   count := count - 1          ; ∇
   Σ commit_wait                ; Σ
   ```

3. Else:

   ```
   ENQUEUE waiters, tid        ; Θ
   BLOCK tid                   ; Θ
   WAIT timeout → Λ            ; Λ
   ```

### **signal(V) / up():**

1. **Δ** verify `count < max`
2. **Ω** check SIGNAL capability
3. **∇** increment count
4. **Θ** wake one or more waiters
5. **Σ** commit increment & wake

### Reliability policy

Ψ can enforce:

* strong fairness (every waiting thread eventually gets the semaphore)
* bounded waiting
* FIFO order via Θ

---

# **5.2.5 Channels (Δ, Ω, Θ, ∇, Λ, Φ, Σ)**

Channels unify:

* pipe semantics
* synchronous/async send-receive
* bounded/unbounded queues
* rendezvous channels (CSP style)

Channel state:

[
state = (buffer,; capacity,; closed,; wait_send,; wait_recv)
]

### **send(channel, msg)**

1. **Δ** check if buffer full or closed
2. **Ω** check SEND permission
3. Case analysis:

#### **Case A — buffer NOT full**

```
ENQ buffer, msg              ; ∇
Σ commit_send                ; Σ
Θ wake receiver if waiting
```

#### **Case B — buffer full**

Either:

* **blocking send**:

  ```
  ENQUEUE wait_send, tid     ; Θ
  BLOCK tid                  ; Θ
  WAIT timeout → Λ           ; Λ
  ```

* **non-blocking send**:

  → return Λ (no-space non-event)

### **receive(channel)**

1. **Δ** check if buffer empty
2. **Ω** check RECV permission
3. If message available:

```
msg := DEQ buffer            ; ∇
Σ commit_recv                ; Σ
Θ wake sender if waiting
```

4. If empty:

* blocking:

  ```
  ENQUEUE wait_recv          ; Θ
  BLOCK tid                  ; Θ
  WAIT timeout → Λ           ; Λ
  ```

* non-blocking → Λ return

### **Channel close**

1. **Δ** classify channel as open/closed
2. **Ω** check CLOSE capability
3. **∇** set `state.closed := 1`
4. **Θ** wake all waiters
5. **Φ** mark messages after close as invalid
6. **Σ** commit close

---

# **5.2.6 RW-Locks (Ω, Θ, Δ, ∇, Σ)**

Work exactly like mutex + semaphore hybrid.

RWLock state:

[
state = (readers,; writer_active,; writer_waiters,; reader_waiters)
]

### **read-lock**

* Δ check `writer_active == 0`
* Ω check read perms
* Θ manage waiters
* ∇ increment `readers`
* Σ commit

### **write-lock**

* Δ check `readers == 0 and writer_active == 0`
* Ω check write perms
* Θ enqueue or wake
* ∇ set writer_active := 1
* Σ commit

Fairness policies are Ψ-level.

---

# **5.2.7 Futex-Like Primitives (Fast-Path ∇, Slow-Path Θ/Λ)**

A **futex** (fast userspace lock) maps cleanly to PMS:

### Fast path (no kernel):

* Δ compare memory word
* Ω ensure access rights
* ∇ attempt atomic modification (CAS-like)
* Success → Σ commit
* Failure → slow path

### Slow path (kernel):

* Θ enqueue thread
* Λ wait with timeout
* Φ wake on error or recontextualization (e.g., mutex owner died)

This is the default primitive for PMS userland threading.

---

# **5.2.8 Condition Variables (Λ, Θ, Ω, Φ)**

CondVar state:

[
state = (waiters)
]

### **wait(cv, mutex)**:

1. Δ assert mutex owned
2. Ω check WAIT permission
3. ∇ release mutex
4. Θ enqueue thread
5. WAIT (timeout → Λ)
6. Once signaled → Θ resume
7. Re-acquire mutex via ∇

### **signal / broadcast:**

1. Δ check waiter list
2. Ω verify SIGNAL
3. Θ select waiter(s)
4. ∇ wake
5. Σ commit signal

Φ handles:

* mutex death
* policy violations
* invalid wake-ups

---

# **5.2.9 Synchronization as Operator Algebra**

Each primitive corresponds to a **legal PMS operator word**, e.g.:

### Mutex lock attempt (success path)

[
Δ;;Ω;;∇;;Σ
]

### Mutex lock (blocking path)

[
Δ;;Ω;;Θ;;Λ;;Θ;;∇;;Σ
]

### Semaphore V

[
Δ;;Ω;;∇;;Θ;;Σ
]

### Channel synchronous receive

[
Δ;;Ω;;Λ/∇;;Φ;;Σ
]

These sequences fully respect dependency constraints from **0.3**.

---

# **5.2.10 Policy-Level Guarantees (Ψ)**

Ψ governs:

* fairness
* ordering
* maximum hold-time
* priority inheritance
* deadlock detection
* capability bounds
* starvation prevention
* distributed consistency of lock semantics

Ψ can enforce scheduling invariants:

```
Ψ: NO_THREAD_WAITING_FOREVER
Ψ: WRITER_PRIORITY
Ψ: FIFO_SEMAPHORE
Ψ: NONBLOCKING_CHANNELS_ONLY
```

Ψ is the *regulator* and can override or cancel transitions.

---

# **5.2.11 Summary**

Synchronization in PMS-OS is built on:

| Operator | Structural Function                                           |
| -------- | ------------------------------------------------------------- |
| **Δ**    | inspect resource state (lock free? count?)                    |
| **Ω**    | ensure correct privilege and capability use                   |
| **Θ**    | manage wait queues, order, scheduling                         |
| **Λ**    | timeouts, empty buffer semantics                              |
| **∇**    | atomic updates (lock, unlock, count, enqueue)                 |
| **Σ**    | commit updates, wake operations, finalize consistency         |
| **Φ**    | handle misinterpretation, invalid states, recontextualization |
| **Χ**    | isolate sync objects between processes                        |
| **□**    | sync primitives as frames                                     |
| **Ψ**    | global policies for fairness & correctness                    |

This yields a **uniform, axiomatic, verifiable** synchronization subsystem.

---

# **5.3 Event System & Notifications (Θ, Λ, Φ, Ω, Δ, Σ)**

**timers, signals, pub-sub — PMS-OS structural definition**

Event handling in PMS-OS is *not* a bolt-on mechanism:
it emerges naturally from the PMS operators for **temporality (Θ), absence (Λ), recontextualization (Φ), asymmetry (Ω), isolation (Χ), distinction (Δ), and commit (Σ)**.

Events are simply **operator-triggerable transitions** that may originate:

* internally (Θ-driven timers, scheduler ticks)
* externally (interrupts, device signals)
* cross-process (IPC, signals)
* system-wide (policy notifications, recontextualization events)

We define all of them uniformly.

---

# **5.3.1 Event Model Overview**

A PMS Event is a PMS-typed transition trigger:

[
Event = (\Delta_{kind},; payload,; source,; target,; meta)
]

with:

* **Δ_kind** — operator-level distinction of event type
* **payload** — arbitrary data
* **source** — process, device, timer, kernel, etc.
* **target** — process, sync primitive, channel, or global handler
* **meta** — Θ timestamp, Λ absence flags, Φ error states, Ω required roles

Events do *not* mutate anything directly:
they request that some **event handler** run a PMS operator sequence.

---

# **5.3.2 Component: EventFrames (□ + Χ)**

All events exist inside an **EventFrame**:

[
EventFrame = (queue,; routing,; filters,; perms,; meta)
]

* **queue**: Θ-ordered event list
* **routing**: mapping Δ_kind → handler function
* **filters**: optional Ψ policies, e.g. throttling, priority
* **perms**: Ω capability matrix (who may send/receive)
* **meta**: time, error counters, last-Φ states

Χ can isolate EventFrames by process or security domain.

---

# **5.3.3 Timers (Θ, Λ, Σ)**

Timers are a **pure Θ construct**.

### **Structures**

[
Timer = (deadline,; mode,; callback,; active)
]

### Timer Operation

#### (1) Registration

```
Δ: classify timer parameters
Ω: capability check (create timer)
∇: insert Timer into TimerWheel
Σ: commit registration
```

#### (2) Tick-driven activation

Each **Θ tick** checks:

```
Δ compare now >= deadline
if false: continue
if true: Θ schedule callback event
```

#### (3) Timer Miss / Expiry → Λ

If execution cannot occur in time due to:

* CPU starvation
* isolation blocking
* policy throttling

then a **Λ-event** is triggered:

```
Λ: timer_missed
Φ: optional recontextualization (defer, reschedule)
```

Timers are therefore **Θ → Δ → Λ/Φ → Σ** event machines.

---

# **5.3.4 Signals (Δ, Ω, Θ, Φ, Σ)**

Signals are lightweight, asynchronous notifications.

Examples:
`SIGIO`, `SIGCHLD`, `SIGTERM` (abstract PMS analogues)

### **SignalFrame**

[
SignalFrame = (pending, handlers, perms, meta)
]

### Sending a signal

```
Δ classify signal kind
Ω check SEND_SIGNAL capability
Θ enqueue into target.pending
Σ commit enqueue
```

### Delivering a signal

On each scheduling boundary (**Θ**), a process checks:

```
Δ if pending ≠ ∅
Ω ensure process can receive signals
Θ dequeue one signal
Φ enter signal-handler frame
execute handler
Σ return to main frame
```

### Failed delivery → Λ

```
Λ: signal_dropped (blocked, dead task, invalid handler)
Φ: recover (redirect, default handler, escalate)
```

Signal delivery therefore uses:

[
Δ;;Ω;;Θ;;Φ;;Σ
]

the minimal operator chain for asynchronous forcing of control flow.

---

# **5.3.5 Pub-Sub System (Δ, Ω, Θ, Χ, Σ, Λ, Φ)**

PMS pub-sub is *structurally native*: it is built from EventFrames arranged into **topic frames**.

### **TopicFrame**

[
TopicFrame = (topic_id,; subscribers,; backlog,; perms,; meta)
]

### Publish(message)

1. **Δ**: classify topic
2. **Ω**: verify PUBLISH permission
3. **Θ**: append message to topic backlog
4. **Σ**: make message visible
5. **Θ**: enqueue deliver events for each subscriber

### Subscribe(process)

1. **Δ**: topic exists?
2. **Ω**: SUBSCRIBE perms
3. **∇**: add subscriber to list
4. **Σ**: commit

### Delivery

Each subscriber receives events through its EventFrame:

```
Δ classify message
Θ schedule delivery
Ω check RECEIVE perms
∇ deliver into mailbox or channel
Σ commit
```

### When subscriber is not ready → Λ

```
Λ: subscriber_unavailable
Φ: drop, retry, buffer, or reroute depending on Ψ policy
```

### Isolation: Χ

TopicFrames can be isolated per namespace or security class:

* tenants
* containers
* user sessions
* privilege domains

Χ ensures no cross-talk without explicit Ω permission.

---

# **5.3.6 Timers, Signals, Pub-Sub in Unison (Event Algebra)**

All event mechanisms reduce to operator chains of the following forms:

### **Timer event**

[
Θ;;Δ;;Θ;;Σ
]

### **Signal**

[
Δ;;Ω;;Θ;;Φ?;;Σ
]

### **Pub-sub publish**

[
Δ;;Ω;;Θ;;Σ
]

### **Delivery failure**

[
Δ;;Λ;;Φ;;Σ?
]

### **Recontextualized event handling**

[
Δ;;Φ;;Θ;;Σ
]

Thus all events are algebraically expressible as PMS-valid sequences.

---

# **5.3.7 Event Routing Engine (Kernel)**

Kernel has an EventRouter:

[
EventRouter = (routing_table,; filters,; perms,; backlog,; meta)
]

Processing loop:

1. Θ tick increments time
2. Δ check incoming event queues
3. Ω verify that event is allowed
4. Θ route to destination EventFrame
5. Φ recontextualize if target unavailable
6. Σ commit routing

---

# **5.3.8 Policy (Ψ) Over Events**

Ψ governs:

* event rate limits
* masking rules
* signal default actions
* timer reliability constraints
* pub-sub topic visibility
* global ordering guarantees (Θ policies)

Ψ can cancel or redirect events by overriding valid transitions:

```
Ψ: deny_signal(SIGKILL) in sandboxed process
Ψ: enforce FIFO delivery on topic “orders”
Ψ: prohibit real-time timers in low-privilege domains
```

Ψ is the *ultimate arbiter* of event behavior.

---

# **5.3.9 Summary**

| Mechanism   | Δ | Ω | Θ | Λ | Φ | Σ | Χ | Function              |
| ----------- | - | - | - | - | - | - | - | --------------------- |
| **Timers**  | ✓ | – | ✓ | ✓ | ✓ | ✓ | – | time-driven events    |
| **Signals** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | – | async notifications   |
| **Pub-Sub** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | topic-based messaging |

All event behavior emerges from PMS operators, respecting structural grammar and dependency constraints.

---

# **6. Device & Driver Model**

## **6.1 Driver Roles & Capabilities (Ω)**

*Axiomatic grounding: Ω = asymmetric access structure, privilege gradients, directional capability relations.*

In PMS-IT, a **driver** is not an ad-hoc piece of software.
It is a **role-bound execution locus** with **Ω-typed capability edges** that define:

1. **what** parts of the hardware abstraction it may act on (Δ-bound referents),
2. **how** it may act (∇ privileges),
3. **under which frame** its operations are interpreted (□ context),
4. **what policies** constrain it (Ψ),
5. and **which asymmetries** it introduces relative to the kernel and device (Ω edges).

Thus, the driver model is entirely derivable from the structure:

[
\Omega : \text{Role/Capability Operator enforcing directional asymmetries.}
]

---

# **6.1.1 Drivers as Ω-Structured Roles**

A driver is defined as a **triple**:

[
D = (f_D,; r_D,; C_D)
]

where:

* **f_D ∈ F** — the *driver frame*: contextual namespace for device registers, MMIO regions, protocol semantics.
  (Grounded in □.)

* **r_D ∈ R** — the *driver role*: a specific Ω-mode that grants exactly the capabilities required to operate the device.

* **C_D ⊆ Capabilities** — the *capability set*: a finite set of Ω edges describing directed permissions:

  * read-capability: Ω(read → device-register-X)
  * write-capability: Ω(write → device-register-Y)
  * interrupt-ack capability: Ω(ack → IRQ-n)
  * DMA grant capability: Ω(dma-map → region)
  * isolation-entry capability: Ω(enter → Χ-subcontext)

These are all **Ω-typed relations**:

[
\Omega(r_D,, action_type,, target)
]

The Ω constraints ensure:

* a driver cannot operate outside its declared domain,
* the kernel can formally prove safety properties by checking Ω edges,
* capability elevation / reduction is a **structurally typed** operation.

---

# **6.1.2 Capability Classes (Ω-Families)**

All driver capabilities fall into five **structural Ω families**, each corresponding to PMS operator interplay:

### **(A) Access Capabilities** (Δ→∇ restricted by Ω)

What hardware objects the driver may distinguish or act on.

Examples:

* Ω(read, register)
* Ω(write, register)
* Ω(read, config-space)
* Ω(write, MMIO-range)

These restrict ∇ to only the permitted Δ-distinguished objects.

---

### **(B) Temporal Capabilities** (Ω→Θ)

Permissions affecting when or how the driver participates in scheduling:

* Ω(allow-interrupt-handler)
* Ω(allow-deferred-work)
* Ω(timer-arm)
* Ω(timeout-register)

These define which Θ transitions the driver can initiate.

---

### **(C) Contextual Capabilities** (Ω→□)

Permissions to enter or manipulate frames:

* Ω(enter-driver-frame)
* Ω(map-device-frame)
* Ω(switch-to-config-frame)

Without these, the driver cannot perform □ operations affecting device context.

---

### **(D) Isolation Capabilities** (Ω→Χ)

Permissions to create, enter, or exit isolation domains for safe operation:

* Ω(spawn-iosandbox)
* Ω(access-ringbuffer-subset)
* Ω(allow-DMA-scope)

These define which Χ transformations are legal for the driver.

---

### **(E) Policy Capabilities** (Ω→Ψ)

Permissions to apply or modify policies affecting the device domain:

* Ω(apply-power-policy)
* Ω(change-error-policy)
* Ω(register-policy-hooks)

These control how Ψ changes influence the driver’s future actions.

---

# **6.1.3 Driver–Kernel Asymmetry Graph (Ω-Graph)**

Every PMS-OS defines an **Ω-asymmetry graph**:

Nodes:

* Kernel role (r_K)
* Driver roles (r_D1, r_D2, …)
* Optional device-domain roles (r_dev_low, r_dev_high)

Edges:

* directional Ω-edges defining legal capability flows

Graph invariant:

[
\Omega(r_K) \supseteq \Omega(r_D) \supseteq \Omega(r_{dev})
]

Drivers may have **strictly less** capability than the kernel but **more** than raw device roles.
This encodes the standard “kernel > driver > device” trust hierarchy *without hardcoding it* — it is generated structurally.

---

# **6.1.4 Driver Execution Model Under Ω Constraints**

At runtime, the driver executes PMS-CPU instructions, but each instruction prefixed by ∇ or □ must pass an Ω-check:

[
\text{Allowed}(op, target, s) \Leftrightarrow \Omega(r_D) \models (op, target)
]

Examples:

* ∇(write MMIO[x]) requires Ω(write, MMIO[x])
* □(enter dma-frame) requires Ω(enter-dma-frame)
* Θ(interrupt-ack) requires Ω(ack IRQ)

If an instruction lacks a supporting Ω edge:

* Ψ may block it,
* the kernel may reframe via Φ (e.g., fallback mode),
* or an isolation fallback may occur via Χ.

Thus **Ω defines the admissible operator-space** for the driver.

---

# **6.1.5 Capability Elevation / Reduction (Ω-Transitions)**

Ω itself is an operator with dependencies:

[
Δ \preceq Ω \prec ∇, □, Θ
]

A capability transition occurs through an instruction:

[
I_{\Omega\text{-update}} = (Ω,; pre,; post)
]

Two forms:

### **(A) Elevation (controlled)**

Allowed only if:

* kernel role r_K authorizes elevation via Ψ(policy), and
* Δ distinguishes correct device + operation type.

Effect:

[
r_D' = r_D \oplus C
]

where C is a capability subset.

### **(B) Reduction (always safe)**

[
r_D' = r_D \setminus C
]

Used for:

* entering restricted modes,
* fault conditions,
* device reset states.

All changes to capabilities flow through **Ω-typed transitions**.

---

# **6.1.6 Driver Modularity via Ω-Framed Capability Sets**

Drivers are decomposed into Ω-modules, each with its own capability subset:

* init-module (Ω_init)
* irq-handler (Ω_irq)
* config-module (Ω_cfg)
* data-path module (Ω_dp)
* control-plane module (Ω_ctl)

Each module is framed:

[
M = (□*{module},; Ω*{module},; Ψ_{module})
]

This provides:

* strict scoping of what each module may do,
* minimal crossing points,
* predictable reasoning for runtime verification.

The kernel loads modules and composes their frames using □ and Σ.

---

# **6.1.7 Driver–Device Binding (Δ→Ω→□)**

Attaching a driver to a device is a structural sequence:

1. **Δ(device-id)**
   Distinguish the device type.

2. **Ω(assign driver-role)**
   Install the capability profile for that device type.

3. **□(enter driver frame)**
   Switch to driver context where its MMIO mappings, protocol semantics, and policies apply.

This ensures that *no driver can attach itself to a device*—the kernel must initiate Δ and Ω.

---

# **6.1.8 Summary of 6.1**

Let’s summarize the full structure of drivers under PMS:

| Structural Element        | PMS Operator | Meaning                                              |
| ------------------------- | ------------ | ---------------------------------------------------- |
| Driver identity           | Δ            | Device-type distinctions used to select driver logic |
| Driver action permissions | Ω            | Capability edges restricting ∇,□,Θ                   |
| Driver execution context  | □            | Frame for device registers, protocols                |
| Driver scheduling & time  | Θ            | Placement in IRQ/deferred queues                     |
| Driver isolation          | Χ            | DMA sandboxes, memory protection                     |
| Driver policy domain      | Ψ            | Power/error policy, safety constraints               |

**Drivers are Ω-structured entities.**
Their behaviors are legal only if Ω edges allow the operator sequences they attempt.
This gives a *formal, verifiable, capability-secured driver model*.

---

# **6. Device & Driver Model**

## **6.2 Interrupt Handling Path (Φ + Θ)**

*Structural mode: interrupts as Φ-driven recontextualization; timing and ordering via Θ; privileges by Ω; isolation by Χ.*

At this point we already have:

* CPU-level **Φ semantics** (2.4) – how the PMS-CPU enters/exits handlers.
* Ω-based **driver roles and capabilities** (6.1).
* Θ-based **scheduling and time** in the kernel (3.4).
* Χ-based **isolation** and □-based **frames** (3.5, 4.1).

Now we assemble these into a **full interrupt path** from **wire → CPU → kernel → driver → scheduler → process**, using Φ + Θ as the backbone.

---

## **6.2.1 Goals & Structural View**

The PMS interrupt path is designed to:

1. Treat **every interrupt** as a **Φ event**:

   * recontextualization of execution
   * change of role (Ω) and frame (□)
   * optional isolation changes (Χ)
2. Use **Θ** for:

   * ordering and priority
   * time-based control (tick/timer interrupts)
   * safe integration with scheduling (3.4)
3. Use **Ψ** to enforce invariants:

   * bounded handler time
   * no illegal capability use
   * safe exit back to pre-interrupt context or safe fallback on failure.

We will split the path into:

* **Hardware → CPU Φ-entry** (low-level)
* **CPU → Kernel interrupt core** (dispatcher)
* **Kernel core → Driver top half** (hard IRQ)
* **Deferred bottom half / softirq / workqueue** (Θ-mediated)
* **Return path** (Φ-exit + Σ integration)

---

## **6.2.2 Interrupt Lifecycle Phases**

An interrupt’s life is structurally:

[
\text{Device event} \xrightarrow{Δ} \text{IRQ line} \xrightarrow{Φ_{CPU}} \text{Kernel IRQ context} \xrightarrow{Δ/Ω/Θ} \text{Driver handler} \xrightarrow{Σ/Θ} \text{Completion + Return}
]

We can enumerate the **canonical phases**:

1. **Signal generation (device → IRQ)** — device asserts an interrupt line, distinguished by Δ.
2. **CPU recognition & Φ-entry** — PMS-CPU performs Φ: saves context, switches role/frame.
3. **Kernel interrupt dispatch** — kernel Δ-selects handler, uses Ω to check driver capabilities.
4. **Driver “top half” handler** — runs in interrupt context with strict Ψ limits.
5. **Deferred “bottom half” / softirq** — Θ-scheduled work in process or soft-interrupt context.
6. **Completion & wakeups** — Σ integrates results, Θ awakens sleepers, Λ / timeouts handled.
7. **Φ-exit & return to pre-interrupt context** — EXC_RET-style recontextualization back to user or kernel code.

Each step is a PMS-valid sequence: **Δ → Ω/□ → Φ → Θ → Σ/Ψ** respecting dependency constraints.

---

## **6.2.3 CPU-Level Interrupt Entry (Φ-core recap)**

When an IRQ `irq` fires while some context was executing (user or kernel):

1. **Asynchronous event arrives (external Π, modeled via Δ)**
   The CPU’s interrupt controller distinguishes an IRQ number:

   [
   Δ_{irq}: \text{classify line} \rightarrow irq_id
   ]

2. **Φ-entry microsequence** (from 2.4, specialized for drivers):

   Conceptually:

   ```asm
   ; auto-generated by hardware/µcode (Φ)
   PUSH  PC              ; ∇
   PUSH  SR              ; ∇
   PUSH  FR              ; ∇
   ; optionally PUSH R4..R7, etc.

   SET_ROLE  ROLE_KERNEL ; Ω
   FRM_ENTER  FR_KSTACK  ; □
   ; record cause in meta m: m.exc.cause = irq_id
   JMP  IVT[irq_id]      ; Δ
   ```

   Structural operators:

   * Φ — “we are not executing in the old context anymore”
   * Ω — move to kernel role
   * □ — move to kernel stack/frame
   * Θ — time progression continues; we may update interrupt-related counters in `m.time`
   * Χ — implicit: isolation boundaries reinterpreted under kernel frame

The **IVT entry** (Interrupt Vector Table) for `irq_id` points into **kernel interrupt core**, not directly into driver code.

---

## **6.2.4 Kernel Interrupt Core: Dispatch Layer (Δ + Ω + Θ)**

### **6.2.4.1 IRQ Controller Abstraction Frame**

The kernel exposes an **IRQ controller frame**:

[
□_{IRQ} = (\text{IRQ descriptors}, \text{priority}, \text{routing}, \text{mask state})
]

Each IRQ is represented by:

```text
struct IRQDesc {
    int          irq_id;
    Priority     prio;
    DriverID     owner;       // which driver (if any) handles this
    HandlerFn    top_half;    // hard-irq handler entry
    HandlerFn    bottom_half; // deferred handler (optional)
    PolicyID     pol;         // Ψ constraints for this irq
    CapSet       caps;        // Ω capabilities bound to this IRQ
}
```

(We’re not fixing exact C-ism; this is structural.)

### **6.2.4.2 Core dispatch sequence**

In the **kernel IRQ entry stub** (running under Φ/Ω/□ from 6.2.3):

1. **Lookup descriptor (Δ)**

   ```asm
   ; irq_id in some register R_irq
   ; Δ-distinguish the descriptor
   ; conceptually:
   desc = IRQDesc[irq_id]          ; Δ – classification
   ```

2. **Policy gate (Ψ)**

   * Check if this IRQ is enabled, not masked, and allowed under current state:

     * power state
     * CPU affinity
     * rate-limiting, etc.

   If policy denies:

   * either ignore (Λ path: non-event for software),
   * or route to a special policy handler.

3. **Priority & nesting control (Θ + Ψ)**

   * Compare `desc.prio` with `m.current_irq_prio` (in meta m).
   * If lower priority and nesting not allowed, mark as **pending** and return (Θ will process later).
   * Otherwise, update `m.current_irq_prio` and `m.irq_nesting++`.

4. **Ω Capability check**

   * Verify that the driver associated with `desc.owner` has capability:

     [
     Ω(r_{D},; handle_irq,; irq_id)
     ]

   * If not, Ψ can route to a fallback handler or treat as security violation.

5. **Invoke top-half handler**

   * Jump to `desc.top_half` with appropriate calling convention:

     ```asm
     CALL  desc.top_half   ; ∇ – driver’s top-half
     ```

   This call runs under:

   * role `r_K` (kernel role) or a driver-specific privileged role `r_D^K`
   * kernel stack frame (□)
   * with interrupt state (e.g., nested interrupts) tracked in `m`.

---

## **6.2.5 Driver Top Half: Hard IRQ Handler (Φ-domain)**

The **top half** is the driver’s time-critical handler executed in interrupt context.

### **6.2.5.1 Contract & Constraints**

* Must be **bounded** in execution time (Ψ bound).
* Operates under privileged role (Ω) but with **limited capabilities** `C_D`.
* Executes in a **non-schedulable** context:

  * cannot block,
  * cannot perform unbounded allocations,
  * cannot call heavy APIs that might sleep or wait.

PMS view:

* This is a **Φ sub-context** overlaid on top of the victim context.
* Θ is available but restricted (e.g., no long-running loops violating time bounds).

### **6.2.5.2 Typical handler structure**

In pseudo-ISA:

```asm
; R_irq, current IRQ descriptor available
driver_irq_top:
    ; Acknowledge interrupt at device level (∇ + Ω + □)
    ; e.g. read status register, write ack bit:
    LOAD   Rstatus, [FRdev + STATUS_REG]    ; ∇
    ; Δ-distinguish cause bits:
    TSTI   Rstatus, MASK_RX                 ; Δ
    BEQ    no_rx                            ; Δ

    ; Clear interrupt flag:
    STORE  [FRdev + STATUS_REG], Rclear     ; ∇

    ; Enqueue work item for bottom half (Θ + Σ)
    CALL   schedule_bottom_half             ; ∇

no_rx:
    ; Possibly handle TX complete, errors, etc.
    ; Minimal core work here

    RET                                     ; ∇
```

Operators involved:

* □ – device frame `FRdev` maps MMIO/registers
* Ω – permissions enforced on register access and scheduling calls
* Θ – scheduling API used to queue deferred work
* Σ – integration of “event occurred” into system state (e.g., queued I/O completion)

Top half’s main job:

1. **Confirm the interrupt** (Δ)
2. **Acknowledge/clear hardware state** (∇ under Ω/□)
3. **Schedule deferred work** (Θ)
4. Exit as fast as possible to keep latency low.

---

## **6.2.6 Bottom Half / Deferred Work (Θ + Σ)**

Heavy or blocking work is deferred from Φ-context to **normal schedulable contexts** using Θ.

We provide three structural patterns (the implementation can choose or mix):

1. **Soft IRQ context** (still “interrupt-ish”, but schedulable slices)
2. **Dedicated kernel threads / work queues**
3. **Process-level callbacks / completions**

All share the same pattern:

[
\text{top-half} \xrightarrow{Θ_schedule} \text{deferred-context} \xrightarrow{Σ} \text{completion}
]

### **6.2.6.1 Soft IRQ (interrupt bottom-half)**

* Implemented as **kernel-managed queue** of pending work items.
* Each work item is a small function pointer + argument frame.

Pseudocode structure:

```text
struct SoftIRQTask {
    HandlerFn fn;
    void*     arg;
    Priority  prio;
    PolicyID  pol;
}
```

Top half schedules:

```asm
; In top half:
MOV   R0, &softirq_rx_task   ; ∇
CALL  softirq_enqueue        ; ∇ – Θ scheduling primitive
```

Later, in **softirq processing context**:

* Kernel scheduler (Θ) periodically runs:

```asm
softirq_loop:
    TASK = dequeue_next_softirq()   ; ∇ + Θ
    IF TASK != NULL:
        CALL TASK.fn(TASK.arg)      ; ∇ – run bottom-half handler
        GOTO softirq_loop
    ELSE:
        RETURN                      ; ∇
```

Here:

* Θ defines when softirq processing runs (post-IRQ, idle, etc.).
* Ψ ensures no starvation (fairness) and bounds on execution.

### **6.2.6.2 Work queues / kernel threads**

For long-running tasks, the driver can offload to **work queues**:

* Work queue is a pool of kernel threads.
* Each work item is processed in a **normal thread context**, with ability to:

  * block,
  * allocate,
  * call any safe API.

Pattern:

```asm
; In top half:
MOV  R0, &work_item      ; ∇
CALL workqueue_schedule  ; ∇ (Θ)

; In worker thread (normal kernel context, Ω = ROLE_KERNEL_THREAD):
CALL driver_bottom       ; ∇
```

Θ is responsible for:

* mapping pending work onto worker threads,
* ordering by priority or fairness rules.

### **6.2.6.3 Process-level completion**

For user-visible operations (read/write, async I/O), bottom halves typically:

1. Complete kernel bookkeeping (Σ on in-kernel state).
2. Wake tasks waiting on events (Θ – scheduling signals result).
3. Deliver signals or completion notifications via IPC (Δ/Ω/Λ/Θ/Φ interplay; see section 5).

---

## **6.2.7 Scheduling, Priorities, and Ordering (Θ + Ψ)**

### **6.2.7.1 IRQ priority model**

Each IRQ has an integer priority `prio` and a class (e.g., timer, I/O, critical, best-effort).

Θ and Ψ combine to enforce:

* **preemption rules**:

  * higher-priority IRQ can preempt lower-priority handlers if `SR.interrupt_enable` is set and Ψ allows.
* **masking / affinity**:

  * masks determined by policy (Ψ) and cores (Θ-scheduling across CPUs if multicore).

### **6.2.7.2 Non-preemptive vs preemptive interrupt handling**

Two modes structurally:

1. **Non-preemptive IRQ handling**:

   * Once in an IRQ handler, other interrupts are masked except critical ones.
   * This is just a Ψ rule:

     [
     \Psi_{nonpreempt}: \forall irq',\ priority(irq') \le priority(irq) \Rightarrow masked
     ]

2. **Preemptive IRQ handling**:

   * Higher-priority IRQs can nest.

     * `m.irq_nesting` and `m.current_irq_prio` track this.
     * Ψ ensures **bounded nesting** to avoid stack overflow.

### **6.2.7.3 Interaction with process scheduler**

The scheduler (Θ, section 3.4) is integrated via:

* **timer interrupts**:

  * dedicated IRQs that periodically trigger scheduler tick handlers.
  * these run in kernel IRQ context and can:

    * account CPU time (3.8),
    * reevaluate run queues,
    * possibly trigger rescheduling.

* **wakeups**:

  * Bottom halves or softirqs call into the scheduler to wake blocked tasks.
  * This is structurally Θ: moving a task from **blocked** to **runnable**.

---

## **6.2.8 Driver-Facing Interrupt Contract**

From the point of view of a driver author, PMS-OS offers a **structured contract**:

### **Registration**

Drivers register interest in interrupts via a call like:

```c
int register_irq_handler(int irq, HandlerFn top, HandlerFn bottom, CapSet caps, PolicyID pol);
```

Structural meaning:

1. Δ: distinguish `irq` and driver identity.
2. Ω: ensure driver has needed capabilities in `caps`.
3. Ψ: attach policy `pol` governing rate limits, nesting rules, CPU affinity.
4. □: bind handler into IRQ frame (update IRQDesc).

### **Top-half API constraints**

* Must not:

  * block,
  * allocate unboundedly,
  * call APIs marked “sleepable”.
* Should:

  * acknowledge device,
  * queue bottom-half,
  * return quickly.

These rules are enforced by:

* Ω (only specific APIs exposed in top-half context),
* Ψ (runtime checks or static analysis),
* tools in section 11 (static proof).

### **Bottom-half API**

* May block and use full kernel interfaces,
* Must still obey policy `pol`:

  * e.g., max latency to complete I/O,
  * fairness to other tasks.

Bottom halves also must not directly violate isolation (Χ) or capability boundaries (Ω); they still run under a role `r_D` but typically in a thread context.

---

## **6.2.9 Faults During Interrupt Handling (Φ-of-Φ)**

If a fault occurs **inside** an interrupt handler:

* e.g., illegal access, capability violation, unexpected null, etc.

This triggers a **nested Φ**:

1. **Φ_fault entry**:

   * save current (already-in-Φ) context,
   * possibly switch to an even more privileged debug/error handler role.

2. **Error policy (Ψ_fault)** decides:

   * terminate the offending driver,
   * mask the IRQ,
   * quarantine the device (Χ: drop from visible frame),
   * panic / halt if fatal.

3. **Recovery**:

   * either attempt to **reframe** state (Φ) to a safe mode,
   * or **rollback** partial work (Σ/Ψ cooperation),
   * then `EXC_RET` back to pre-interrupt or to a safe stop state.

This explicitly avoids “undefined behavior inside interrupts”:
**every misbehavior is a structural Φ + Ψ event with defined resolution paths**.

---

## **6.2.10 Summary**

The PMS interrupt path is:

* **Φ-centric**: every interrupt, trap, and exception is a structured recontextualization.
* **Θ-backed**: timing, ordering, and scheduling of top/bottom halves and softtasks.
* **Ω-governed**: drivers can only act according to their capability sets.
* **Χ-isolated**: device and kernel states are protected by frames and isolation domains.
* **Ψ-guarded**: policies ensure bounded, safe, and fair handling, even under nesting and faults.
* **Σ-integrated**: results of interrupt handling (I/O completions, wakeups, state transitions) are explicitly committed at bottom halves and scheduler hooks.

This gives us a **precise, compositional model** for interrupt handling that we’ll reuse in:

* 6.3 Driver Lifecycle & Policy (Ψ)
* 6.4 Hotplug & Dynamic Reconfiguration (Φ/Ψ + Χ/□)

# **6.3 Driver Lifecycle & Policy (Ψ)**

*Structural mode: drivers as governed agents; policies Ψ define admissible trajectories across their lifecycles.*

We already have:

* Ω: driver roles & capabilities (6.1)
* Φ + Θ: interrupt & trap model (6.2)
* Χ: isolation domains (3.5, 4.1)
* Σ: integration / commit (FS, memory, IPC)
* Ψ: global invariants & policies (0.x, 3.x, 8.x)

Now we define a **driver lifecycle model** where:

* A *driver* is a **role-bearing, policy-bound agent** attached to devices.
* Its lifecycle is a **state machine** constrained by Ψ.
* All transitions are explicit PMS operator sequences (Δ, Ω, Θ, Φ, Χ, Σ, Ψ).

---

## **6.3.1 Entities & Policy Layers**

We distinguish four main entities:

1. **Driver module (D)** – code + metadata + policies.
2. **Device (Dev)** – hardware or virtual endpoint (PCI device, network iface, block device, etc.).
3. **Binding (B)** – relation `(D, Dev)` meaning *driver D handles device Dev*.
4. **Driver context (C_D)** – runtime execution context(s) of D:

   * IRQ handlers, bottom halves, workqueues, threads, control ops.

### **Policy layers (Ψ)**

Policies apply at multiple levels:

1. **Ψ_K** – kernel-global policy:

   * Which driver classes are allowed at all.
   * Signing / attestation / trust domain constraints.
   * Global resource budgets and safety constraints.

2. **Ψ_class** – device-class policies:

   * e.g. “network drivers must use sandbox X”,
   * “storage drivers require journaling hooks”,
   * “USB drivers must be hotplug-aware.”

3. **Ψ_D** – per-driver policy:

   * capacities, time bounds, isolation mode, allowed syscalls, logging/audit requirements.

4. **Ψ_dev** – per-device policy:

   * per-port, per-device config (which drivers may bind, which modes allowed).

The effective policy at runtime is:

[
Ψ_{eff}(D, Dev) = Ψ_K \land Ψ_{class(Dev)} \land Ψ_D \land Ψ_{dev}
]

All driver lifecycle transitions must satisfy `Ψ_eff`.

---

## **6.3.2 Driver Lifecycle States**

We model each driver module `D` with a lifecycle state:

* **S₀: Uninstalled** – not present in system.
* **S₁: Installed** – code + metadata present (on disk / image), registered with kernel.
* **S₂: Loaded** – code mapped into memory, symbols resolved.
* **S₃: Probed** – candidate devices have been tested for compatibility.
* **S₄: Bound / Active** – driver has one or more live `(D, Dev)` bindings.
* **S₅: Suspended** – driver/devices quiesced (power mgmt, sleep).
* **S₆: Error / Degraded** – policy violation or runtime failure detected, but not yet fully unloaded.
* **S₇: Quarantined** – isolated via Χ; only limited recovery/introspection allowed.
* **S₈: Unloaded** – code detached; no active bindings; resources reclaimed.

Each `(D, Dev)` binding also has its own binding-state subgraph, but we’ll talk primarily at the driver-module level and refer to per-device binding when needed.

---

## **6.3.3 Lifecycle State Machine (Operators on Transitions)**

We describe core transitions and the dominant PMS operators involved. Each transition is governed by Ψ and Ω, and often uses Φ, Χ, Σ, Θ, Δ.

### **T1: Install → Load (S₁ → S₂)**

**Operators:** Δ, Σ, Ψ, □

1. **Δ**: kernel distinguishes driver artifact (name, version, class, signature).

2. **Ψ_K/Ψ_class**: check:

   * allowed driver class?
   * signature / attestation valid?
   * not explicitly blacklisted?

3. **Σ**: integrate driver into **driver registry**:

   * add D to `DriverTable`
   * record class, supported IDs, policy handle Ψ_D, capabilities Ω_D.

4. **□**: map driver code into kernel frame:

   * allocate code/data frames,
   * set `FR_D_code`, `FR_D_data`.

The result is `S₂: Loaded`.

If Ψ fails, installation is rejected (stay in S₁ or back to S₀) and may trigger audit logs.

---

### **T2: Load → Probe (S₂ → S₃)**

**Operators:** Δ, Ω, Ψ, Θ

**Probe** = testing which devices this driver can handle.

Steps:

1. **Δ**: enumerate candidate devices `Dev_i` whose IDs match D’s declared match table.

2. **Ψ_class/Ψ_dev**: filter by policy:

   * e.g. some devices may require only trusted drivers, or only signed.

3. **Ω**: verify driver’s capability to access the device’s bus/frame:

   * `Ω(r_D, access_bus, Dev)` must hold.

4. **Θ**: run hardware/software probes in **finite time**:

   * e.g., read device registers, send probe commands.
   * bounded by Ψ (no unbounded loops; timeouts enforced via Λ/Θ).

If a probe succeeds for a device, we move along a **binding transition** (T3). If all probes fail, driver remains Loaded (S₂) but unbound; or policy may allow auto-unload.

---

### **T3: Probe → Bound/Active (S₃ → S₄)**

**Operators:** Φ, Χ, Σ, Ω, Ψ

Binding `(D, Dev)`:

1. **Φ (recontextualization)**:

   * interpret Dev as now “owned” (or co-owned) by D.
   * switch device’s MMIO or command frame into **driver’s isolation domain**:

     * set `FR_dev_D` or attach Dev to a driver-specific Χ compartment.

2. **Ω**:

   * assign driver context role `r_D^K` (kernel driver role).
   * capabilities `C_D` for:

     * bus access,
     * interrupts registration,
     * DMA (if allowed),
     * control operations.

3. **Σ**:

   * commit binding into:

     ```text
     DriverBindings: (D, Dev) → Bound
     ```

   * set up IRQ handlers (register top/bottom halves with 6.2’s model).

   * allocate internal queues, buffers, and control structures.

4. **Ψ**:

   * activate `Ψ_eff(D, Dev)` for this binding.
   * this may include:

     * rate limits (interrupt rate, I/O rate),
     * maximum memory for buffers,
     * isolation level (Χ mode),
     * audit level (logging hooks, etc.).

Driver is now **Bound / Active** (S₄) for that device.

---

### **T4: Active ↔ Suspended (S₄ ⇄ S₅)**

**Operators:** Θ, Ψ, Φ, Σ, Λ

Suspension handles **power management / sleep / device quiescing**.

#### S₄ → S₅ (Suspend)

From Active to Suspended:

1. **Θ**: enter a suspend sequence (time-ordered steps).

2. **Ψ**: check if driver/device is in a suspendable state:

   * no critical I/O in flight,
   * no unsynced data (Σ not pending),
   * power constraints satisfied.

3. **Φ**: recontextualization:

   * device moves into low-power / inactive frame,
   * some operations become prohibited by Ψ.

4. **Σ**:

   * flush buffers,
   * finalize outstanding I/O,
   * update FS/network/system state so no invariants are violated.

5. **Λ**:

   * mark outstanding expectations as “suspended” non-events
   * e.g., operations that would have happened but are now postponed.

#### S₅ → S₄ (Resume)

1. **Θ**: resume sequence.

2. **Ψ**:

   * ensure environment conditions allow resume
   * e.g., bus still present, security context still valid.

3. **Φ**: recontextualize to active frame:

   * restore FR_dev_D,
   * re-enable interrupts (Ω + SR flags),
   * re-open queues, restart timers.

4. **Σ**:

   * commit to “device is now live” state,
   * wake any waiting users/processes.

If resume fails (lost device, policy change, error), go to **Error/Degraded** (S₆) or **Quarantined** (S₇).

---

### **T5: Active/Suspended → Error/Degraded (S₄/S₅ → S₆)**

**Operators:** Ψ, Φ, Χ, Σ

This happens when:

* driver violates a policy,
* device misbehaves,
* repeated faults, timeouts (Λ + Θ),
* hardware errors detected.

Steps:

1. **Ψ_detect** observes violation:

   * e.g., driver exceeds interrupt budget,
   * tries forbidden frame access,
   * misuses capabilities,
   * too many retries / timeouts.

2. **Φ_error**:

   * reframe the driver context as “degraded mode”.
   * mark `(D, Dev)` binding as “error-state” in metadata.

3. **Χ strengthening**:

   * increase isolation:

     * restrict accessible frames / MMIO ranges,
     * block certain syscalls or kernel APIs,
     * optionally disconnect the device from user-visible namespace.

4. **Σ**:

   * commit error state to logs/audit,
   * mark operations as failed,
   * propagate appropriate error codes to userspace (via IPC, FS, etc.).

The driver is in S₆: still *present*, but not fully functional.

---

### **T6: Error/Degraded → Quarantined (S₆ → S₇)**

**Operators:** Χ, Ψ, Φ

Some violations require **hard quarantine**:

1. **Ψ_escalation** decides:

   * repeated faults,
   * critical security violation,
   * driver from untrusted domain.

2. **Χ_quarantine**:

   * move driver + associated devices into an isolated context:

     * no live user-visible handles,
     * interrupts may be left disabled,
     * I/O paths cut.

3. **Φ**:

   * reframe any existing user requests to **failure** or “device disappeared”.

4. **Ψ_quarantine**:

   * restrict allowed operations on D to:

     * introspection,
     * logs,
     * controlled debugging,
     * eventual replacement.

Quarantined drivers cannot be reactivated without explicit administrator/Ψ_K decision (or auto-recovery path defined by policy).

---

### **T7: Active / Error / Suspended → Unloaded (S₄/S₅/S₆ → S₈)**

**Operators:** Θ, Σ, Φ, Χ, Ψ

When the system decides to **remove a driver** (manual unload, upgrade, or fatal error):

1. **Θ**: ensure all contexts have quiesced:

   * no threads executing in D’s code,
   * no IRQ handlers pending,
   * no bottom halves queued,
   * no open handles (or all forcibly closed).

2. **Φ_unbind**:

   * unbind `(D, Dev)` for all devices:

     * disable IRQs,
     * tear down MMIO mappings,
     * disconnect from FS/network namespaces.

3. **Χ_teardown**:

   * remove isolation compartments for D and its devices,
   * release frames and resources.

4. **Σ**:

   * commit removal to kernel state:

     * update driver table,
     * update device-state (mark unhandled/not_present).

5. **Ψ**:

   * verify post-conditions:

     * no reachable references to D’s frames,
     * no capabilities or handles referencing D remain,
     * resource counters (3.8) balanced.

If Ψ fails (e.g., leak detected), system may move to S₇ (quarantine) or take stronger action (e.g., partial restart).

---

## **6.3.4 Policy Attachments & Governance (Ψ in Practice)**

We now make Ψ more concrete.

### **6.3.4.1 Policy “attachments” to drivers**

For each driver `D`, kernel stores:

```text
DriverPolicy {
    TrustLevel   trust;      // e.g., core, signed, vendor, third-party, experimental
    CapSet       caps;       // Ω: allowed capabilities
    Isolation    iso_mode;   // Χ: isolation domain type (none, container, VM, enclave)
    TimeBudget   irq_budget; // max IRQ run-time per interval
    TimeBudget   work_budget;// max bottom-half / workqueue time
    MemBudget    mem_limit;  // max memory for driver internal structures
    DeviceClass  class;      // net, block, char, usb, gpu, etc.
    AuditLevel   audit;      // logging intensity
    RecoveryMode recovery;   // restart, quarantine, disable, panic, etc.
}
```

Ψ is a **set of constraints** referencing these.

### **6.3.4.2 Enforcement points**

Key enforcement points for Ψ:

1. Install / Load (T1):

   * trust level, signatures, class allowlist/denylist.

2. Probe / Bind (T2/T3):

   * whether D may touch the bus or device,
   * whether class + trust level match device policy.

3. IRQ / bottom-half / workqueue execution:

   * time budgets via Θ + Λ (timeouts, scheduling).
   * memory budgets on allocations via Σ + 3.8 resource accounting.
   * API calling patterns (e.g., no blocking from top half).

4. Error / Fault handling:

   * escalation rules: when to restart, when to quarantine, when to panic.

5. Unload / Upgrade:

   * safe removal conditions,
   * optional auto-migration of device to new driver (Φ rebind).

---

## **6.3.5 Driver Upgrade / Replacement (Φ + Σ + Χ)**

When upgrading or swapping drivers while devices are live:

### **Scenario:** D_old → D_new for device Dev

We follow a structured Φ sequence:

1. **Δ**: distinguish D_old, D_new, and Dev.

2. **Ψ_compat**: check upgrade policy:

   * version compatibility,
   * driver class invariants,
   * trust levels,
   * migration support.

3. **Φ_migrate**:

   * create a **migration frame** for Dev:

     * old state (queues, configuration, hardware state)
     * new driver’s view of that state.

   * recontextualize Dev from `(D_old, Dev)` to `(D_new, Dev)`:

     * may require transformation of internal data structures (Φ on s_c).

4. **Σ_migrate**:

   * commit new binding `(D_new, Dev)`,
   * mark old binding as “replaced”.

5. **Χ**:

   * isolate old driver `D_old` (S₇) or unload it (S₈) if no other devices use it.

6. **Ψ_post**:

   * check that no invariants are broken:

     * no lost outstanding I/O,
     * no resource leaks,
     * Dev accessible and consistent.

If migration fails, Ψ may revert:

* roll back to D_old (if still functional),
* quarantine Dev and D_new,
* escalate to admin/policy.

---

## **6.3.6 Error Handling, Recovery, and Quarantine (Ψ + Φ + Χ)**

We define a small taxonomy of **driver fault policies** (RecoveryMode):

1. **Recover / Restart in-place**:

   * Try resetting the device,
   * Reinitializing driver state,
   * Re-establishing bindings.

   Operators: Φ_reset, Σ_reset, Θ_backoff.

2. **Restart driver once**:

   * Unbind, unload, reload D, re-probe and re-bind.

   Operators: T7 (Unload) → T1–T3 (Install/Load/Probe/Bind).

3. **Quarantine driver / device**:

   * Isolate both from user-space and most of the kernel.

   Operators: Χ_quarantine, Ψ_quarantine.

4. **Panic / Stop system**:

   * For critical subsystems (e.g. root FS, memory controller) with no safe recovery.

   Operators: Ψ_panic → transition system into global halting state.

Policies can differentiate:

* by trust level (core driver vs third-party),
* by device criticality (boot disk vs optional USB),
* by configured system mode (production vs debug).

---

## **6.3.7 Interaction with Resource Accounting (3.8 Ψ + Σ)**

Drivers are **heavy users of resources**; their lifecycle hooks tie into 3.8:

1. **Memory**:

   * driver allocations charged to `ResourceAccount(D, Dev)` buckets.
   * limits enforced by Ψ:

     * `mem_limit` per driver and per device class.

2. **CPU**:

   * IRQ and bottom-half time tracked via Θ and Σ.

     * `irq_budget` and `work_budget` ensure no runaway drivers.

3. **IPC & queues**:

   * per-driver/public IPC channels accounted for:

     * max queue depths,
     * rate limits.

4. **Storage & network**:

   * drivers for block / network devices report throughput and utilization to accounting.

Policy:

* If a driver exceeds resource budgets:

  * initial soft warnings (logs),
  * throttling (Θ – reduce scheduling slice),
  * eventual escalation to S₆/S₇ (Error/Quarantine).

---

## **6.3.8 Summary**

In PMS terms, a **driver** is:

* A **role-bearing agent** (Ω) operating within a **frame** (□),
* With **isolation constraints** (Χ),
* Subject to **global and local policies** (Ψ),
* Interacting with hardware via **Δ, ∇, Φ** and time via **Θ**,
* Committing effects via **Σ**, and handling absences/timeouts via **Λ**.

The **driver lifecycle** is a Ψ-governed state machine:

* **Install → Load → Probe → Bind/Active → Suspend/Resume → Error → Quarantine → Unload**,
* with clear PMS operators driving each transition and enforcing invariants.

This lifecycle plugs cleanly into:

* 6.2’s interrupt path,
* 4.x memory & storage (frames, mapping, FS),
* 3.x kernel core (scheduling, isolation, syscalls, accounting),
* and 8.x governance (trust, identity, policy).

---

# **6.4 Hotplug & Dynamic Reconfiguration (Φ/Ψ)**

*Structural perspective: hotplug as recontextualization events governed by invariants.*

Hotplug means:

* **New devices appear**, requiring recognition, classification, policy checks, enumeration, driver binding.
* **Existing devices disappear**, requiring unbinding, teardown, isolation, graceful degradation or quarantine.
* **Device topology or configuration changes** (multi-function devices, network links, PCIe bridges, USB trees).
* **Driver stacks reconfigure live** (driver replacement, fallback, multipath, link renegotiation).

All of this is expressed in PMS through **Φ**, **Ψ**, **Χ**, **Θ**, **Δ**, **Σ**.

---

# **6.4.1 Types of Hotplug Events**

We categorize all hotplug events in PMS terms:

### **A. Physical attach/detach events (Φ_ext)**

External source triggers Φ:

* device connected/disconnected,
* bus reports presence change,
* port power change,
* cable insertion/removal,
* function-level resets.

This is structurally:
[
\Phi_{\text{ext}} : s \rightarrow s'
]
Reinterpret the system topology.

### **B. Logical reconfiguration events (Φ_logic)**

No physical event — system context changes:

* virtualization guest attaches a virtual device,
* kernel loads new bus handler,
* device renames or reassigns functions,
* new capabilities advertised at runtime.

### **C. Discovery/Enumeration events (Δ_enum + Θ)**

System distinguishes new device identities:

* topology scanning,
* reading device descriptors,
* generating identity Δ-distinction records (ID, class, vendor, version).

### **D. Policy events (Ψ_hotplug)**

Policies that constrain whether attach/detach are allowed:

* “Only trusted drivers may handle hotplug USB devices”
* “PCIe hotplug allowed only in zones A/B”
* “Storage hotplug allowed but must enter write-quiescent state first”

### **E. Absence/non-event recognition (Λ_hotplug)**

Expected attach/detach does *not* occur:

* delayed device response,
* half-attached states,
* transient enumeration failures.

---

# **6.4.2 Core Hotplug Pipeline (Attach)**

When a device **appears**, the kernel undergoes the following Φ-driven transformation sequence:

## **Step 1. Signal → Φ_ext**

Hardware/bus triggers interrupt or polled event:

```
Φ_ext: Bus reports new device D_new present
```

Φ_ext updates meta-state:

* new topology snapshot in m.topology,
* pending attach job queued for the hotplug subsystem.

## **Step 2. Δ_distinguish: Identify device**

Kernel performs systematic distinction:

```
Δ_identify(D_new):
    read IDs
    classify bus type
    read descriptors
```

Result → creation of a **device frame**:

```
□_dev(D_new)
```

## **Step 3. Ψ_policy: Check attach permissions**

Apply effective policy:

[
Ψ_{eff}(D_{new}) = Ψ_K \land Ψ_{class} \land Ψ_{bus} \land Ψ_{zone} \land Ψ_{dev}
]

Examples:

* Disallow hotplug in secure mode.
* Allow only signed drivers for this bus.
* Require xen/VM-level mediation.
* Require isolation for USB-storage class.

If Ψ denies attach → go directly to ** quarantine path (Φ_reject + Χ)**.

## **Step 4. Φ_enumerate: Recontextualize bus**

Bus driver performs enumeration:

```
Φ_enumerate:
    update device tree / topology
    create ephemeral enumeration frame
    reconcile with existing bus state
```

In complex buses (PCIe, USB), enumeration itself is a whole Δ–Φ–Θ sequence.

## **Step 5. Probe driver candidates (Δ + Ω + Ψ)**

For each driver module D:

```
Δ_match(D, D_new)
Ω_cap_check(D, bus_access)
Ψ_D_class(D, D_new)
```

Only drivers satisfying **Ψ** and **Ω** remain as candidates.

## **Step 6. Bind (T3 equivalent)**

Binding uses Φ + Σ:

```
Φ_bind(D, D_new):
    assign driver context
    map device MMIO frames (□)
    install IRQ handlers
    register capabilities (Ω)
Σ_commit_binding(D, D_new)
```

The device is now **active**.

## **Step 7. Notify dependent subsystems (Θ + Σ)**

Integration steps:

* filesystem mounts,
* network interface creation,
* block device registration,
* Wacom/keyboard input nodes.

[
Σ_{\text{system}}: \text{commit new device to global namespace}
]

---

# **6.4.3 Core Hotplug Pipeline (Detach)**

When a device **disappears**, the system follows analogous but inverse transitions:

## **Step 1. Φ_ext_detach: topology recontextualization**

Bus signals removal:

```
Φ_ext_detach(D_lost)
```

m.topology updated to “device missing”.

## **Step 2. Λ_absence: detect non-event**

If device fails to respond within Ψ-bounded Θ intervals:

```
Λ_timeout(D_lost)
```

This distinguishes physical removal from transient error.

## **Step 3. Ψ_detach_policy**

Policies decide what kind of teardown is allowed:

Examples:

* "Storage devices must not be detached if writes pending unless force-detach flag set."
* "Network interfaces may be hot-removed if routing allows failover."

## **Step 4. Φ_unbind: Recontextualize driver → remove binding**

Driver transitions:

* Active → Suspended,
* Suspended → Unbound.

Sequence:

```
Φ_unbind(D, D_lost)
   disable IRQs
   flush pending DMA
   freeze queues
   mark device frame invalid
```

## **Step 5. Σ: Commit unbind**

Integration of removal:

* remove from `/dev`,
* update kernel resource tables,
* notify IPC channels.

## **Step 6. Χ_isolate residue**

If any part of the driver still refers to the now-missing device, policy can enforce:

```
Χ: isolate driver context
```

This protects kernel from invalid memory/hardware access.

## **Step 7. Ψ_post_detach**

Final consistency check:

* no outstanding references,
* no leaked capabilities,
* no dangling buffers.

---

# **6.4.4 Topology Reconfiguration (Bridges, Multi-function, etc.)**

Some buses allow **dynamic topology**, not just simple add/remove.
PMS models this via *composite Φ recontextualizations*.

### **Φ_topology_change**

Applied when:

* PCIe switch appears/disappears,
* USB hub resets or changes port states,
* Thunderbolt daisy chain reconfigures,
* Network topology changes (link up/down, aggregated bonds).

Φ transforms:

* parent/child device frames (□),
* bus role hierarchy (Ω_asymmetry),
* device ID mapping,
* capabilities exposed.

### Integration:

[
Σ_{\text{topology}} : \text{commit new topology}
]

Policies Ψ then validate:

* no device aliasing,
* no cycles in topology graph,
* no unauthorized path (e.g., TBolt allowed only for certain trust levels).

---

# **6.4.5 Driver Stack Reconfiguration (Φ_replace, Φ_upgrade)**

This includes runtime driver replacement, multipath failover, alternate mode negotiation.

## **Φ_replace: change driver D_old → D_new**

Steps mirror 6.3.5:

* Δ: detect incompatible/updated driver.
* Ψ_check: ensure replacement allowed.
* Φ_migrate: translate state.
* Σ_commit: activate new driver.
* Χ_isolate: retire old driver.

## **Φ_fallback: driver failover**

Triggered by Ψ when error budgets exceeded.

Sequence:

* Φ_migrate device state,
* rebind to fallback driver D_fallback,
* update network/storage namespaces via Σ.

---

# **6.4.6 Policy Model for Hotplug (Ψ_hotplug)**

Ψ_hotplug encodes all invariants for attach/detach:

### **Categories:**

1. **Security constraints:**

   * USB class restrictions,
   * thunderbolt authorization,
   * PCI hotplug zones,
   * signed driver requirement.

2. **Safety constraints:**

   * storage hotplug only when FS consistent,
   * disallow NVMe detach under load unless forced.

3. **Resource constraints:**

   * prevent attach when memory overcommit,
   * disallow new devices if IRQ budget exceeded.

4. **System-governance constraints:**

   * certain networks allowed only by policy,
   * virtualization mediation required (hypervisor policy).

### **Policy shape:**

A policy might specify:

```
Ψ_hotplug(dev_class=X):
    require signs(dev)
    require isolation(Χ_mode = container)
    require driver ∈ approved_driver_list
    forbid attach if loadavg > threshold
    forbid detach if pending_IO(dev) > 0
```

Ψ is evaluated at each step of the attach/detach pipeline.

---

# **6.4.7 Hotplug Failure Modes (Λ + Φ + Ψ)**

Failure in any step triggers one of structured responses:

### **A. Reject & isolate**

If attach fails early:

```
Φ_reject
Χ_isolate(device)
```

### **B. Retry**

If enumeration nondeterministic (e.g. USB flakiness):

```
Λ_timeout
Θ_backoff
repeat Δ_identify
```

### **C. Partial bind, then rollback**

If driver fails to initialize fully:

```
Φ_partial
Σ_partial_rollback
戻 (return to previous state)
```

### **D. Escalation to quarantine**

If repeated attach attempts violate policy:

```
Ψ_escalate → Χ_quarantine(driver)
```

---

# **6.4.8 Concurrency, Ordering, and Interleavings (Θ)**

Hotplug events interleave with other kernel activity.
Ξ concurrency patterns:

1. **Multiple devices attach simultaneously:**
   Θ schedules attach jobs; dependencies expressed by bus ordering.

2. **Attach during detach:**
   Φ resolution ensures consistent topology.

3. **Ongoing IO during detach:**
   Requires Σ-mediated quiesce and commit before final detach.

4. **Driver upgrade concurrent with hotplug:**
   Policies Ψ restrict reconfiguration windows.

---

# **6.4.9 Integration with Resource Accounting (3.8)**

Attach increases:

* IRQ budget,
* memory allocation per driver,
* bus bandwidth,
* possible multipath usage.

Detach decreases these resources.

Metrics go through Σ + Ψ audit:

```
Σ_account_update(D, Dev)
Ψ_budget_check()
```

If attach would violate system-level quotas → Ψ blocks it.

---

# **6.4.10 Summary**

Hotplug in PMS is a **governed recontextualization pipeline**:

* **Φ** drives context shifts (attach, detach, topology change, driver replacement).
* **Ψ** enforces system policies: security, safety, resource, governance.
* **Χ** isolates misbehaving states and maintains integrity during transitions.
* **Δ** performs identification and classification.
* **Θ** orders the attach/detach processes and resolves concurrency.
* **Σ** finalizes new or removed states into the global namespace.
* **Λ** handles absences, failed attempts, and degraded events.

This yields a unified, formally structured hotplug framework that works for:

* PCIe, USB, Thunderbolt
* network link negotiation
* multipath storage
* virtual devices
* dynamic driver stacks
* clustered or distributed system reconfiguration

---

# **7. Networking Stack**

# **7.1 Transport Abstraction – connections as frames, timeouts (Λ/Θ)**

**Operators:** □ (frame), Δ (distinction), Θ (temporality), Λ (non-event), Ω (asymmetry), Χ (isolation), Φ (recontextualization), Σ (integration), Ψ (policy).

Transport is the lowest-level networking substrate in PMS-OS: the level *beneath* protocols, above device drivers.
Its job is to provide a consistent **connection abstraction**, which in PMS is framed as:

**“A connection is a dynamic □-frame, temporally organized by Θ, subject to timeouts Λ, and governed by Ω/Ψ.”**

Everything else — routing, protocol logic, congestion control — is layered on top of these primitives.

---

# **7.1.1 Transport as a Frame (□_conn)**

A *connection* is represented as a **context frame**:

[
□_{\text{conn}}(cid) =
(base,, state,, role,, policy,, meta)
]

Where:

### **1. base**

The underlying transport device/driver frame (e.g., NIC queue pair, virtual port, loopback).

### **2. state**

The local connection state machine:

* sequence numbers
* connection flags
* negotiated parameters
* send/receive windows
* device/driver handles

### **3. role (Ω)**

Asymmetric relation between peers:

* client/server
* initiator/responder
* control/data channel
* privileged/unprivileged send rights

Ω determines what transitions are legal.

### **4. policy (Ψ)**

Connection-level invariants:

* encryption required?
* authentication required?
* max RTT, min throughput?
* congestion fairness constraints?
* isolation level?

### **5. meta (Θ/Λ/Φ/Χ)**

Temporal counters, last-seen timestamps, timeout budget, isolation markers, fallback state.

---

# **7.1.2 Transport Timeline (Θ)**

Every connection progresses along a **temporal arc (Θ)**:

### **Θ_connect**

Initiation sequence:

```
Θ: send SYN-equivalent
Θ: receive ACK-equivalent
```

But in PMS we don’t prescribe packets — *only* operator structure:

[
Θ_{\text{open}} = Δ_{\text{id}} ; Ω_{\text{role_set}} ; Σ_{\text{commit_open}}
]

Where:

* Δ distinguishes connection request
* Ω sets role: initiator/responder
* Σ commits connection into active tables

### **Θ_active**

Main data-transfer temporal loop:

[
(Δ_{\text{window}} ; ∇*{\text{send}} ; ∇*{\text{recv}} ; Σ_{\text{ack}})^*
]

This is the structural skeleton behind any sliding-window mechanism (TCP, QUIC, RDMA, etc.).

### **Θ_close**

Connection teardown sequence:

[
Θ_{\text{close}} : Δ ; Ω ; Σ ; Φ
]

* Δ distinguishes closure signal
* Ω may apply role-specific “who may close” rules
* Σ commits last bytes, flushes buffers
* Φ recontextualizes the transport frame back to idle

---

# **7.1.3 Non-Events & Timeouts (Λ)**

Λ models all network absence conditions:

* delayed ACK → Λ_acktimeout
* missing keepalive → Λ_ka
* peer not responding → Λ_noreply
* link-down → Λ_linkfail
* partial delivery → Λ_partial
* flow-control stall → Λ_fc

### Structural form:

[
Λ_{\text{timeout}} : \text{expected event not observed within Θ-window}
]

Λ transitions **do not mutate core state** directly; they:

1. update `m.timeout_flags`
2. schedule a **fallback transition** via Φ or Θ_backoff
3. trigger policy checks Ψ

E.g.:

```
Λ_acktimeout:
    m.flags.ack_missing = true
    Φ_recover(conn)
```

Λ is essential for liveness: it encodes loss, silence, jitter, and transient failures as *structured events* rather than errors.

---

# **7.1.4 Transport States as PMS Operator Graphs**

A transport connection is a **PMS-operator state machine**, not a single variable.

Let C be a connection frame.

The transition structure:

### **OPENING:**

[
C_0 \xrightarrow{Δ_{\text{syn}}} C_1 \xrightarrow{Θ} C_2 \xrightarrow{Σ_{\text{open}}} C_3
]

### **ACTIVE:**

Repeated loop:

[
C \xrightarrow{Δ_{\text{ready}}}
\xrightarrow{∇*{\text{send}}}
\xrightarrow{∇*{\text{recv}}}
\xrightarrow{Λ_{\text{loss?}} / Θ_{\text{success}}}
\xrightarrow{Σ_{\text{update}}}
\rightarrow C'
]

### **CLOSING:**

[
C_N \xrightarrow{Δ_{\text{finish}}} \xrightarrow{Σ} \xrightarrow{Φ_{\text{teardown}}} C_{\text{free}}
]

This structuring allows multiple advanced behaviors:

* retransmission (Θ + Λ + Φ)
* congestion control (Θ + Σ)
* backpressure (Ω + Θ)
* out-of-order handling (Δ + Σ)
* half-open states (Λ + Φ)

---

# **7.1.5 Connection Frames and Namespaces (□ + Χ)**

Each connection is isolated via:

### **1. Its own frame (□_conn)**

Contains:

* send buffer
* receive buffer
* state variables
* per-connection policies

### **2. Isolation boundaries (Χ)**

Prevents cross-talk between connections:

* Χ_per_conn: each connection in its own sandbox
* Χ_per_flow: hardware queues separated
* Χ_per_security_zone: inter-tenant isolation in virtualized setups
* Χ_shielding: drop all IO when connection is quarantined

Χ ensures “one connection cannot corrupt another”.

### **3. Namespaces**

Connections belong to:

* process namespace
* network namespace
* security namespace
* bus/interface namespace

Switching between namespaces → **Φ_recontextualize**.

---

# **7.1.6 Order, Delay, and Scheduling (Θ)**

Network transport is fundamentally temporal, so Θ is key:

### **Θ_seq — sequence maintenance**

Assigns ordering to outbound or inbound segments.

### **Θ_retrans — retry timer**

If Λ_detect(timeout):

```
Θ_backoff
Θ_retransmit
```

### **Θ_sched — connection scheduling**

Kernel can interleave connections based on Θ policies:

* fair queueing
* weighted priorities
* real-time guarantees
* latency-sensitivity

### **Θ_flow — pacing**

Transport may pace packets in time to avoid bursts:

```
Θ_pace:
    delay sending until pacing interval expires
```

---

# **7.1.7 Transport-Level Φ (Recontextualization)**

Φ handles all major interpretational shifts:

### **A. Φ_migrate**

Switch transport to a different underlying device or queue (e.g., NIC migration).

### **B. Φ_fallback**

Change transport mode:

* fast-path → slow-path
* offload → software stack
* encrypted → unencrypted (if allowed by Ψ)

### **C. Φ_resync**

Used when sequence numbers or windows diverge.

### **D. Φ_quarantine**

Isolate connection due to security violation or protocol error.

Φ always preserves the past but changes the *lens* of interpretation.

---

# **7.1.8 Transport Policies (Ψ)**

Ψ overlays general invariants:

### **1. Security policies**

* encryption mandatory?
* authentication required?
* cross-namespace transports allowed?
* allowed peers / subnets?
* anomaly detection (rate limits, malformed sequences)?

### **2. Flow policies**

* max bandwidth
* min throughput
* RTT constraints
* head-of-line blocking limits
* pacing rules

### **3. Resource policies**

* per-process connection limits
* per-user bandwidth quotas
* kernel-global transport budget

Ψ determines **what transitions are legal** in the transport state machine.

---

# **7.1.9 Transport Integration (Σ)**

Σ commits transport-level changes:

### **Σ_send_done**

Move sent data to “ack-pending”.

### **Σ_ack_merge**

Integrate acked bytes into completion queues.

### **Σ_state_commit**

Apply state updates:

* updated windows
* updated sequence numbers
* cleared timeout flags
* merged retransmission status

### **Σ_teardown**

Final teardown state integrated into global namespaces:

* free connection ID
* free buffers
* release isolation context
* update routing tables if needed

Σ ensures global consistency.

---

# **7.1.10 Summary (7.1)**

Transport abstraction in PMS is expressed as:

* **Connection = □ (frame)**
* **Events & transitions = Δ**
* **Action & I/O = ∇**
* **Temporal flow = Θ**
* **Timeouts & absence = Λ**
* **Recontextualization = Φ**
* **Isolation = Χ**
* **Asymmetry = Ω**
* **Commit/merge = Σ**
* **Policies = Ψ**

This gives a transport layer that is:

* deterministic or non-deterministic depending on Ψ/Θ/Λ
* fully isolated per-connection
* fully policy-governed
* time-aware (Θ)
* absence-aware (Λ)
* capable of fallback, migration, multi-path, congestion control
* abstract enough to implement TCP, QUIC, RDMA, Unix sockets, or custom protocols with the same PMS substrate

---

# **7.2 Addressing & Routing – nodes, services, topics (Δ/□)**

**Operators:**
Δ (distinction), □ (frame), Θ (temporal progression), Φ (recontextualization), Ω (asymmetry), Χ (isolation), Λ (non-event), Σ (integration), Ψ (policy).

Addressing & routing in PMS networking follows the same structural pattern as all PMS subsystems:

**Address = Δ (identity) inside □ (namespace) under Ω/Ψ constraints.
Routing = Δ + Θ + Φ transitions of frames (□_route), producing Σ-committed next-hop decisions.**

This gives a unified substrate for:

* local IPC,
* host networking,
* container & VM networking,
* overlay & cluster networking,
* service-mesh addressing,
* topic-based (pub/sub) addressing,
* identity-based networking (actors, principals).

All implemented using the same operator algebra.

---

# **7.2.1 Structural Address Model (Δ inside □)**

In PMS, an **address** is not a number — it is a **distinguished symbol inside a frame**:

[
Addr ::= Δ_{id} \in □_{\text{namespace}}
]

Where:

* **Δ_id** → the distinguishing element (node ID, service ID, topic ID, path element, queue identifier)
* **□_namespace** → the scope that gives the identifier meaning

Examples:

| Address Type           | Δ (distinction) | □ (namespace)   |
| ---------------------- | --------------- | --------------- |
| IP address             | Δ_IP            | □_internet      |
| MAC                    | Δ_mac           | □_link_layer    |
| Unix socket            | Δ_path          | □_filesystem    |
| Actor/service          | Δ_serviceID     | □_service_space |
| Topic (pub-sub)        | Δ_topic         | □_topic_space   |
| VM/Container interface | Δ_vnic          | □_tenant_space  |

**Key principle:**
*Δ without □ has no meaning; □ without Δ has no identity.*
This two-operator basis replaces ad-hoc address systems.

---

# **7.2.2 Node Identity Frames (□_node)**

Each node in a PMS-based network has a **node frame**:

[
□_{\text{node}} = (id,, credentials,, roles,, routing_table,, policies)
]

Containing:

### **1. id (Δ_node)**

Node identity inside the cluster or network.

### **2. credentials (Ω)**

Roles & capabilities:

* allowed to send?
* allowed to accept?
* allowed to administer routing?

### **3. routing_table (Δ→□ mappings)**

Maps:

* destination distinctions (Δ_dest)
* to routing frames (□_next)

### **4. policies (Ψ)**

Enforce allowable routing:

* no routing between certain zones
* encryption required
* multi-tenancy boundaries
* max hops
* no hairpin routing, etc.

Node frames combine all these into a single PMS structure.

---

# **7.2.3 Address Resolution (Δ → Δ inside new □)**

Address resolution transforms an identity Δ in one frame into a Δ in another.

Examples structurally:

### **DNS-like resolution:**

```
Δ_hostname  --(Φ_resolve)-->  Δ_ip  in  □_internet
```

### **Service discovery:**

```
Δ_serviceID  --(Φ_lookup)-->  Δ_instanceID  in  □_service_space
```

### **Topic routing:**

```
Δ_topic  --(Φ_expand)-->  {Δ_subscriber_i}  in  □_subscription_graph
```

The operator is **Φ** because resolution changes *interpretation context* while preserving the original semantic object:

“a name becomes an address becomes a next-hop”.

---

# **7.2.4 Routing as Frame Transition (□_route)**

Routing is treated as a **sequence of frame transitions**:

[
□*{\text{node}*A}
\xrightarrow{\text{Δ_dest}}
□*{\text{route}}
\xrightarrow{\Theta*{\text{select}}}
□_{\text{node}_B}
]

### **□_route** contains:

* the resolved next-hop
* the path metrics
* temporal state (Θ counters for TTL, deadlines, RTT estimates)
* policy context (Ψ_route)
* isolation markers (Χ)

This allows routing to be:

* deterministic
* probabilistic
* policy-driven
* multi-path
* isolated per-tenant
* context-sensitive

All using the same PMS operators.

---

# **7.2.5 Temporal Routing (Θ)**

Routing always has a temporal component:

### **1. Θ_forward**

Increment hop count, update TTL or lifetime budget.

### **2. Θ_select**

Choose next-hop based on current temporal information:

* load
* congestion window
* time-sensitive routing (deadline-aware)
* real-time constraints

### **3. Θ_refresh**

Periodic refresh of routing tables or link metrics.

### **4. Θ_reroute**

Triggered when:

* Λ (absence) = missing heartbeat, missing ACK
* Φ (recontextualization) = link changes
* Χ (isolation change) = tenant migration or segmentation

Routing becomes a **temporal flow**, not a static function.

---

# **7.2.6 Λ in Routing (Non-Events)**

Non-events handle:

* link failure
* interface down
* node disappearance
* heartbeat loss
* route expiration
* missing ARP/NDP response
* missing DNS response
* stale metrics

Structural form:

[
Λ_{\text{route-timeout}}: \text{expected Δ-response not observed within Θ-window}
]

Effect:

1. mark route degraded
2. trigger Φ_reroute (context shift)
3. possibly update policies (Ψ)
4. schedule retry (Θ_backoff)

Λ is essential to resilience; no networking stack is complete without absence-handling.

---

# **7.2.7 Hierarchical Frames for Multi-Level Routing**

Because □ denotes context, we can model *any* hierarchy:

### **1. Global network frame**

[
□_{\text{internet}}
]

### **2. Region frame**

[
□_{\text{region}}
]

### **3. Cluster frame**

[
□_{\text{cluster}}
]

### **4. Node frame**

[
□_{\text{node}}
]

### **5. Process/service frame**

[
□_{\text{service}}
]

Hierarchical routing becomes:

[
□*{A} \to □*{B} \to □*{C} \to □*{D}
]

Each step is a **Φ** recontextualization plus a **Θ** temporal step.

This works for:

* classic IP routing
* SDN
* service meshes
* overlay networks
* P2P
* RPC
* actor systems
* topic-based routing

All using the same operator structure.

---

# **7.2.8 Topic-Based (Pub/Sub) Addressing**

A topic is simply:

[
Δ_{topic} \in □_{topicspace}
]

A publish event:

[
\text{Δ_topic} ; \Theta ; ∇_{\text{send}}
]

Routing a publish means:

[
Φ_{\text{expand-subs}}
]

Which yields:

[
{Δ_{\text{sub}*i}} \in □*{\text{subscribers}}
]

Then message delivery proceeds normally (Θ forwarding, Λ timeouts, Σ acknowledgement).

Topics require **no special machinery** beyond Δ+□+Θ+Φ.

---

# **7.2.9 Capability-Restricted Routing (Ω)**

Ω enforces that not all nodes/roles can route to all others.

Examples:

* tenant A cannot route into tenant B (Χ + Ω)
* privileged nodes may use privileged backplane links
* “service-only” nodes can’t perform general routing
* nodes with low-trust role cannot forward encrypted flows

Ω acts at routing time as:

[
Δ_{dest} \xrightarrow{Ω_{check}}
\begin{cases}
\text{allowed} \
\text{blocked} \
\text{rerouted via Φ} \
\end{cases}
]

Ω produces:

* branch decisions
* upgrade/downgrade in routing role
* alternative paths
* quarantine (route suppressed via Χ)

---

# **7.2.10 Isolation Boundaries (Χ)**

Routing respects isolation:

### **Tenant isolation**

[
Χ_{\text{tenant}}
]

Preventing cross-tenant addressing.

### **Namespace isolation**

[
Χ_{\text{ns}}
]

Network namespaces for containers/VMs.

### **Security zones**

[
Χ_{\text{sec-zone}}
]

DMZ, backend, control plane, management plane, etc.

Routing attempts crossing a Χ boundary force:

* Φ_reinterpret (different address mapping)
* or Ψ_deny (halt routing attempt)
* or encapsulation into isolated transport (tunnels)

---

# **7.2.11 Policy-Governed Routing (Ψ)**

Ψ establishes invariants such as:

* routing only allowed if encrypted
* routing blocked from low-trust zones
* rate limits
* must avoid certain nodes
* no single point may see all traffic (privacy-preserving routing)
* maximum hop count
* congestion fairness rules

Ψ acts as:

[
Ψ_{\text{route}}(state) =
\begin{cases}
\text{allow} \
\text{redirect via Φ} \
\text{require Ω-upgrade} \
\text{deny (halt)} \
\end{cases}
]

Thus policies directly shape the routing graph.

---

# **7.2.12 Routing Commit (Σ)**

When a routing decision is finalized:

[
Σ_{\text{route-commit}}
]

Actions include:

* update next-hop cache
* update metrics (RTT, congestion, reliability)
* record successful route in logs
* clear timeout flags
* confirm address-to-path mapping
* update route lifetime counters
* merge cost metrics

Σ ensures routing tables and metrics stay coherent globally.

---

# **7.2.13 Summary (7.2)**

Addressing & routing in PMS are unified under:

* **Δ** — identity elements (node, service, topic)
* **□** — namespaces and routing frames
* **Θ** — temporal routing (hops, scheduling, TTL, pacing)
* **Λ** — absence (timeouts, failures, stale routes)
* **Φ** — context shifts (resolution, reroute, fallback, re-interpret)
* **Χ** — isolation boundaries
* **Ω** — capability-based routing permissions
* **Ψ** — routing policies and invariants
* **Σ** — commit of routing decisions, metrics, state

This gives a routing substrate capable of implementing:

* IP
* UDP
* TCP/QUIC
* SDN
* service discovery
* mesh routing
* actor-based addressing
* topic-based pub/sub routing
* virtual networking
* cluster routing
* multi-tenant segmentation
* privacy-preserving routing

All from the same minimal operator algebra.

---

# **7.3 PMS Protocol Suite Integration (PPS: P-REQ, P-EVT, P-CTRL)**

The **PMS Protocol Suite (PPS)** defines a minimal, operator-typed meta-protocol layer that sits above transport (7.1) and addressing/routing (7.2), but below application semantics and PMSL.

PPS uses the PMS operator algebra directly to define **three universal message forms**:

1. **P-REQ** — *request–response*
   (Δ → Ω → Θ → Σ)
2. **P-EVT** — *event / notification*
   (Δ → Θ → (Λ or Σ))
3. **P-CTRL** — *policy, capability, or frame control*
   (Δ → Φ → Ω → Ψ → Σ)

These three patterns cover all IT protocol behavior structurally — RPC, REST, gRPC, pub/sub, actor messages, system events, control plane signals, capability negotiation, versioning, routing changes, isolation mode toggles, etc.

PPS is therefore a **meta-protocol grammar**, not a concrete wire format.

---

# **7.3.1 PPS Message Structure (Δ inside □_transport)**

A PPS message is:

[
Msg = (Δ_{kind},; Δ_{id},; payload,; □*{transport},; Ω*{src→dst},; Ψ_{policy},; Θ_{ts},; m_{meta})
]

**Fields:**

### **Δ_kind**

The protocol distinction:

* P-REQ
* P-EVT
* P-CTRL

### **Δ_id**

Message identity (UUID or sequence number).

### **payload**

Arbitrary binary or structured data (can contain PMSL values).

### **□_transport**

Connection frame:

* stream frame
* datagram frame
* channel frame
* topic frame

### **Ω_{src→dst}**

Permissions/capabilities attached to the message flow.

### **Ψ_policy**

Active policies constraining handling of the message:

* authenticity required
* replay protection
* routing restrictions
* decryption scope
* isolation boundary

### **Θ_ts**

Temporal metadata:

* creation timestamp
* lifetime/TTL
* retry budget
* sequence counters

### **m_meta**

Additional meta:

* version tags
* routing hints
* diagnostics

---

# **7.3.2 P-REQ (Request/Response Protocol)**

**Operators:** Δ, Ω, Θ, Φ, Λ, Σ

P-REQ is the general form of **RPC-like interactions**.

Structurally:

[
P\text{-}REQ \equiv Δ_{\text{req}} ; Ω_{\text{caps}} ; Θ_{\text{progress}} ; { ∇, Φ, Λ }^* ; Σ_{\text{response}}
]

This models:

* request message (Δ_req)
* permission check at destination (Ω)
* sequential processing (Θ)
* internal actions (∇)
* optional exception/migration (Φ)
* timeouts or missed responses (Λ)
* response commit (Σ)

### **Core semantics**

1. **Δ_req**
   Distinguish request type and call target.

2. **Ω_check**
   Verify caller capabilities for function/service.

3. **Θ_dispatch**
   Enter the service handler in proper temporal frame.

4. Handler body
   Structured sequence of ∇, □, Φ, and Θ (application-layer logic).

5. **Σ_reply**
   Integrate results and emit reply message.

### **Non-event path (timeouts)**

If no reply is produced within the Θ window:

[
Θ_{deadline} \to Λ_{\text{no-response}} \to Φ_{\text{error-frame}}
]

Which may:

* retry
* escalate
* return error
* reroute
* downgrade capability

P-REQ thus supports synchronous and async request–response uniformly.

---

# **7.3.3 P-EVT (Event / Notification Protocol)**

**Operators:** Δ, Θ, Λ, Σ, Φ, Χ

P-EVT is used for **pub-sub messages, notifications, asynchronous signals, state change events**.

Structure:

[
P\text{-}EVT \equiv Δ_{\text{evt}} ; Θ_{\text{emit}} ; { Φ, Λ }^* ; Σ_{\text{deliver}}
]

### **Core semantics**

1. **Δ_evt**
   Declare the event kind.

2. **Θ_emit**
   Timestamp, sequencing, rate-governing.

3. Delivery flow:

   * **Normal**: directo delivery to subscribers
     [
     Σ_{\text{deliver}}
     ]
   * **Transform** (Φ):
     reframe event (e.g., from raw → cooked → filtered)
   * **Drop** (Λ):
     backpressure, event queue full, subscriber offline

4. **Χ boundaries**
   Some events may not be deliverable across security or tenant boundaries.

5. **No required Ω**
   Events often don’t require capability checks, unless crossing protected domains.

### **Examples of P-EVT mappings**

| Type                | Structural form                            |
| ------------------- | ------------------------------------------ |
| Pub/sub topic event | Δ_topic ; Θ ; Σ_deliver                    |
| Timer event         | Δ_timer ; Θ_tick ; Σ_trigger               |
| Signal to process   | Δ_signal ; Θ ; Φ_contextswitch             |
| Kernel event        | Δ_kmsg ; Θ ; Λ_drop-on-overflow ; Σ_commit |

---

# **7.3.4 P-CTRL (Control Plane Protocol)**

**Operators:** Δ, Φ, Ω, Ψ, Θ, Σ, Χ

P-CTRL is the most powerful PPS form: it manipulates **context, roles, policies, routes, capabilities, versions, isolation boundaries**.

Structure:

[
P\text{-}CTRL \equiv Δ_{\text{ctrl}} ; Φ_{\text{recontext}} ; Ω_{\text{role-change}} ; Ψ_{\text{policy-update}} ; Θ_{\text{apply}} ; Σ_{\text{commit}}
]

This covers:

* control-plane protocols
* configuration updates
* capability negotiation
* dynamic isolation (hotplug, attach/detach)
* version/feature negotiation
* routing updates
* doorbell/control messages
* service-side admin commands
* container/VM lifecycle commands
* driver reconfiguration
* network stack policy changes

### **Core operator structure**

1. **Δ_ctrl**
   Distinguish what control plane operation is being attempted.

2. **Φ_recontextualize**
   Re-interpret local context:

   * switch protocol version
   * enter new mode
   * negotiate features
   * rebind frame mappings

3. **Ω_role-change**
   Enforce capability elevation or demotion:

   * admin → user
   * user → restricted
   * node → gateway
   * control-plane → data-plane

4. **Ψ_policy-update**
   Install/update/invalidate policies governing:

   * routing
   * security
   * quotas
   * protocol behavior
   * message validation

5. **Θ_apply**
   Apply changes in a temporally controlled manner:

   * phased rollout
   * atomic switch
   * quiescence window
   * rollback scheduling

6. **Σ_commit**
   Commit the new state atomically and propagate to subsystems.

### **Examples of real protocols mapped to P-CTRL**

| System | Example                   | PMS operators |
| ------ | ------------------------- | ------------- |
| TCP    | window update, mode shift | Δ;Φ;Θ;Σ       |
| QUIC   | version negotiation       | Δ;Φ;Ω;Ψ;Σ     |
| k8s    | control-plane updates     | Δ;Φ;Ψ;Θ;Σ     |
| SDN    | flow rule install         | Δ;Φ;Ψ;Σ       |
| AMQP   | credit flow control       | Δ;Φ;Ω;Θ;Σ     |
| Actors | capability rebinding      | Δ;Ω;Φ;Σ       |
| iSCSI  | mode transitions          | Δ;Φ;Ψ;Σ       |

Everything becomes a structural instance of P-CTRL.

---

# **7.3.5 PPS as Universal Protocol Grammar**

The three PPS message classes are **minimal and complete**:

### **P-REQ**

→ transactional, directed, symmetric or asymmetric requests

### **P-EVT**

→ asynchronous publish/notify signals

### **P-CTRL**

→ recontextualizing / role-changing / policy-carrying control plane messages

Together, they cover all protocol families:

* RPC
* REST
* streaming RPC
* pub-sub
* signals
* events / webhooks
* distributed locks
* leader election
* control plane signals
* version negotiation
* capability-based systems
* orchestration (containers, VMs, services)
* SDN control
* cluster coordination
* distributed transactions

All of these decompose cleanly into Δ–Ψ operator sequences.

---

# **7.3.6 Interactions Between PPS and Networking (7.1, 7.2)**

PPS messages use the underlying transport and routing abstractions:

* **Δ** identifies message type, sender, destination
* **□_transport** defines the connection frame
* **Θ** sequences the flow (send → ack → retry)
* **Λ** handles missing responses or events
* **Ω** restricts permitted interactions
* **Φ** rewrites protocol context (version, mode, fallback)
* **Χ** enforces isolation
* **Ψ** enforces packet-level policy
* **Σ** commits protocol actions (ACK, final state)

Because PPS is built on the operator algebra, all higher-level protocols can be expressed in a unified execution model.

---

# **7.3.7 Summary (7.3)**

The **PMS Protocol Suite (PPS)** provides a universal, operator-typed grammar for all network protocols:

| PPS class  | Structural meaning             | Operators        |
| ---------- | ------------------------------ | ---------------- |
| **P-REQ**  | request–response               | Δ, Ω, Θ, ∇, Λ, Σ |
| **P-EVT**  | async event/signals            | Δ, Θ, Λ, Φ, Σ, Χ |
| **P-CTRL** | control-plane & policy updates | Δ, Φ, Ω, Ψ, Θ, Σ |

Every existing protocol family fits as a specialization of one of these three operator patterns.

---

# **7.4 Network Security (Ω, Χ, Ψ)**

**Operators:** Ω (asymmetry/capabilities), Χ (isolation), Ψ (policy), plus Δ, Θ, Φ, Λ, Σ where required.

PMS treats security not as an “add-on” but as a **first-class structural consequence** of the operator algebra.
Network security emerges from the interplay of three dominant operators:

* **Ω — Asymmetry / Role / Capability**
  Defines *who may do what* over the network.
* **Χ — Distance / Isolation**
  Defines *which contexts are mutually reachable*.
* **Ψ — Self-binding / Policy / Invariant**
  Defines *what must always hold across time and across all nodes*.

Together they create a **composable security substrate** that governs:

* identity and authentication
* authorization and capabilities
* segmentation and isolation
* trust boundaries
* encryption mandates
* packet filtering
* multi-tenant separation
* control-plane protections
* safety invariants
* policy-driven routing and traffic shaping

This layer is not ad-hoc; it is the consequence of PMS operator dependencies.

---

# **7.4.1 Structural Identity and Principal Model (Δ + Ω)**

Every communicating principal is distinguished by:

[
Δ_{\text{id}} \in □_{\text{principal-space}}
]

Principals include:

* nodes
* services
* processes
* containers/VMs
* users (structural, not psychological)
* actors
* system modules

Identity is **structural**, not personal.
Capabilities are attached via Ω:

[
Ω(Δ_{\text{id}}) = {cap_1, cap_2, \dots}
]

These capabilities govern:

* which PPS messages a principal may send or receive
* which transport frames (□_transport) they may enter
* which routing domains they may traverse
* which control-plane operations (P-CTRL) they may perform

### **Identity + Capability = Network Role**

Network roles emerge implicitly:

* client, server, admin, router, orchestrator
* producer/consumer
* pub/sub subscriber
* control-plane authority
* observer/debug role
* confined/minimal-cap role

No separate concept of “role model” is needed; Ω *is* the role model.

---

# **7.4.2 Trust Boundaries and Segmentation (Χ)**

Χ creates **isolation boundaries** between network contexts:

[
□*{A} \xrightarrow{Χ} □*{B}
]

meaning: *the contexts exist, but direct communication is restricted or reinterpreted*.

Χ boundaries define:

* network namespaces
* VLANs / VRFs
* tenant segmentation
* DMZs and zones
* private vs public networks
* control-plane vs data-plane separation
* sandboxed subsystems
* microservice trust domains
* confidential compute enclaves
* cross-node capability limits

### Χ enforces structural distance

* A principal in □₁ *cannot* directly observe or modify state in □₂
* Communication must traverse a permitted corridor (P-CTRL message or broker)
* Address mapping uses Φ to reinterpret Δ identities across boundaries
* Policies (Ψ) apply invariants to crossings (encryption, auditing, allowed protocols)

Thus Χ is the core of **zero-trust network architecture** in PMS.

---

# **7.4.3 Policy-Enforced Guarantees (Ψ)**

Ψ provides global or scoped invariants:

[
Ψ = { rule_1, rule_2, \dots }
]

Each rule constrains future actions involving:

* sending or receiving packets
* routing decisions
* encryption requirements
* capability transitions
* entry into or exit from isolation frames
* control-plane operations
* traffic shaping and quota boundaries
* cluster-wide safety conditions

### Examples of Ψ-level network invariants

* “All traffic crossing χ-boundary X must be encrypted.”
* “Only nodes with Ω_admin may issue P-CTRL updates.”
* “Max hop count = 15 for tenant A.”
* “Topology changes must be serialized (Θ) and committed (Σ).”
* “Rate limit actor messages to N per Θ-window.”
* “No routing through untrusted roles.”
* “Control-plane must never transit the data-plane frame.”

Ψ is enforced **at every step**: if a transition violates a policy, the machine:

1. **rejects** (halt or drop), or
2. **reframes** via Φ (fallback, downgrade), or
3. **moves into containment** via Χ, or
4. **logs and continues** under a reduced capability set (Ω-downgrade).

---

# **7.4.4 Message-Level Security (Ω, Ψ on PPS Messages)**

Each PPS message carries:

* Ω_src → sender’s capabilities
* Ω_dst → required capabilities for receiver
* Ψ_message → constraints governing delivery or processing
* Χ_boundary tags → which isolation domain(s) the message belongs to

This allows:

### **Authentication**

Using capability claims:

[
Δ_{\text{id}} + Ω_{\text{proof}} \Rightarrow \text{identity verified}
]

Ω_proof may include:

* cryptographic signatures
* MACs
* token-bound capabilities
* ephemeral session capabilities

### **Authorization**

Receiver checks:

[
Ω_{\text{src}} \subseteq Ω_{\text{allowed}}
]

Under Ψ-enforced constraints.

### **Confidentiality**

Ψ may enforce encryption:

* per tenant
* per message type
* per χ-boundary crossing
* per protocol family (P-REQ, P-CTRL)

### **Integrity**

Σ_commit rules require:

* checksums/hashes
* signatures
* replay protection
* sequence constraints (Θ-order)

Everything is operator-grounded; nothing is bolted on afterward.

---

# **7.4.5 Secure Routing (Ω, Χ, Ψ + Δ, Θ, Φ)**

Routing in PMS already depends on Δ, □, Θ, Φ, Λ, Σ (7.2).
Security adds Ω, Χ, Ψ to constrain routing.

### **Ω-based routing constraints**

Roles define:

* who may route packets
* which prefixes/domains may be reached
* who may install routing rules (P-CTRL)
* gateway/border router roles
* privileged administrative paths

### **Χ-based segmentation**

Routing graph is segmented:

[
Graph = \bigcup_i □^{(i)} \quad\text{with crossings guarded by } Χ^{(i,j)}
]

Routing attempts that violate Χ:

* are denied by Ψ
* or require encapsulation & transformation by Φ
* or trigger isolation downgrade/update

### **Ψ-based routing policies**

Examples:

* “Tenant A cannot route into Tenant B.”
* “Admin-only networks require Ω_admin.”
* “Traffic between zones must satisfy encryption=on.”
* “Must avoid certain intermediate nodes (privacy).”
* “No routing loops: detect via Θ-order + Σ consistency checks.”

---

# **7.4.6 Secure Transport Frames (□_transport + Ω + Ψ)**

Transport frames (from 7.1) include:

* stream (TCP/QUIC-like)
* datagram (UDP-like)
* channel (actor/mailbox-like)
* topic (pub-sub)

Security is applied structurally:

### **Frame entry (□_transport)**

[
enter_frame: \square_{\text{transport}} \quad\text{requires } Ω_{\text{perm}} \land Ψ_{\text{rules}}
]

Violations lead to:

* **Φ** reinterpretation (fallback, downgrade)
* **Λ** denial (non-event)
* **Χ** containment
* **Ψ** enforcement halt

### **Frame lifetime**

Ω & Ψ may impose:

* session expiration
* key rotation windows
* permissible payload sizes
* fragmentation rules
* backpressure behavior
* allowed P-CTRL operations inside the frame

---

# **7.4.7 Control Plane Security (P-CTRL with Ω → Ψ → Σ)**

P-CTRL messages (7.3) require the strongest security.

Control plane operations include:

* routing updates
* link-state changes
* capability grants/revocations
* identity provisioning
* cluster membership updates
* driver/device reconfiguration
* version negotiation
* policy distribution

**Operator sequence:**

[
Δ_{\text{ctrl}} ; Ω_{\text{auth}} ; Ψ_{\text{validate}} ; Φ_{\text{recontext}} ; Θ_{\text{apply}} ; Σ_{\text{commit}}
]

Notable constraints:

* Ω_admin (or domain-specific capabilities) required
* Ψ ensures safety invariants during upgrade/migration
* Χ restricts which nodes may receive or forward control-plane messages
* Θ controls rollout timing
* Σ commits state transitions atomically

This yields a **provably safe control plane** — structurally enforced.

---

# **7.4.8 Failure, Absence, and Attack Handling (Λ + Φ + Ψ)**

Network anomalies are modeled explicitly using Λ:

### **Absence conditions**

* missing ACK
* missing heartbeat
* missing P-CTRL confirmation
* timeout during routing update
* incomplete handshake
* unreachable node
* link down

Λ triggers **Φ-recontextualization**:

* failover
* reroute
* downgrade
* quarantine frame
* version fallback
* policy reinforcement

Followed by **Ψ checks** which determine:

* whether to continue
* whether to isolate (Χ)
* whether to escalate
* whether to reject and halt

When a pattern of Λ events matches a Ψ-defined signature:

* An intrusion or anomaly is detected structurally.
* No behavioural inferences about “attackers” are needed.

---

# **7.4.9 End-to-End Invariants (Ψ across nodes and frames)**

Ψ invariants propagate across entire routing chains:

[
Ψ_{\text{e2e}} = \bigcap_i Ψ_{\text{node}*i} \cap Ψ*{\text{route}}
]

Ensuring:

* end-to-end encryption
* hop-limit enforcement
* traffic-class consistency
* QoS guarantees
* multi-tenant separation
* monotonic capability restrictions
* no downgrade attacks
* no frame confusion (□-isolation)

Each hop checks Ψ before forwarding.
Every Σ_commit is subject to Ψ constraints.

---

# **7.4.10 Summary (7.4)**

Network security in PMS is not a subsystem — it is a **native structural phenomenon**:

| Operator | Security Function                                 |
| -------- | ------------------------------------------------- |
| **Ω**    | capability, identity, authorization               |
| **Χ**    | segmentation, isolation, zero-trust boundaries    |
| **Ψ**    | global and local security policies, invariants    |
| **Δ**    | identity of principals, domains, message kinds    |
| **Θ**    | timing windows, expiration, sequencing            |
| **Λ**    | failure detection, anomaly patterns               |
| **Φ**    | recontextualization on error, fallback, migration |
| **Σ**    | commit of secure state transitions                |

This yields:

* zero-trust architecture
* segmented routing
* capability-aware communication
* secure control plane
* safe protocol evolution
* attack-surface minimization
* deterministic security guarantees via operator constraints

All encoded at the operator level, with no external assumptions.

---

# **7.5 Resilience, Failover & Congestion Handling (Λ/Θ/Φ/Σ)**

Resilience in PMS networking is **not** implemented through ad-hoc error handlers or protocol-specific hacks.
Instead, it emerges from the *interaction* of four operators:

* **Λ — Non-event / absence / failure**
* **Θ — Temporality / retry windows / ordering / pacing**
* **Φ — Recontextualization / fallback / migration**
* **Σ — Integration / commit / stabilization**

These four form a canonical pattern:

[
\Lambda ;\rightarrow; \Theta ;\rightarrow; \Phi ;\rightarrow; \Sigma
]

This is the structural “resilience pipeline.”
Every network anomaly, congestion event, or link failure flows through this sequence (possibly multiple times).

---

# **7.5.1 Failure & Absence Detection (Λ)**

Λ encodes **meaningful absence** in a context where something *was expected*.
Network-level Λ events include:

### Missing or delayed transport events

* missing ACK
* missing heartbeat
* no P-REQ response
* request timed out
* TCP/QUIC-like retransmission timeout
* DNS-style missing answer
* failed handshake

### Routing and topology absence

* silent node disappearance
* missing link-state update
* neighbor-not-seen condition
* unreachable destination

### Control-plane absence

* no confirmation for P-CTRL
* no policy-distribution acknowledgment

Λ is always generated **structurally**, never heuristically:

[
\text{Expected event} \land \neg\text{observed} ;\Rightarrow; \Lambda
]

This makes Λ robust, predictable, and operator-consistent.

---

# **7.5.2 Temporal Recovery Dynamics (Θ)**

Once a Λ occurs, Θ determines **how time advances and when actions should be retried**.

Typical Θ-driven behaviors:

### Backoff patterns (explicit attractors or Θ sequences)

* exponential backoff
* linear retry
* jitter-inserted retry
* scheduled retransmission windows

These become attractors (Α-patterns) over Θ that can be composed:

[
Α_{\text{retry}} = (\Theta_{\text{wait}} \circ Δ_{\text{check}})^k
]

### Timeout windows

Θ defines the timing logic for:

* connection-timeout
* handshake windows
* routing propagation deadlines
* flow-control or congestion windows

### Heartbeats & liveness

Θ periodically triggers Δ-liveness checks, which may again generate Λ if the peer is silent.

**Key structural rule:**
Θ does *not* resolve the failure; it *shapes* the temporal conditions under which recovery attempts may proceed.

---

# **7.5.3 Adaptive Fallback & Recontextualization (Φ)**

Φ applies when the meaning or context of a connection, route, or session must change.

### Uses of Φ in resilience:

#### **(A) Failover to alternate routes**

[
Φ_{\text{route}}: \square_{\text{route}} \Rightarrow \square_{\text{alt-route}}
]

Triggered when repeated Λ events and Θ timeouts occur.

#### **(B) Protocol-level fallback**

* switch from QUIC→TCP-like semantics
* switch to degraded mode (reduced QoS)
* revert to version N-1 after handshake fail

This is pure Φ:
“same intention, new interpretation frame.”

#### **(C) Multi-path recontextualization**

If path A is congested or failing:

[
Φ_{\text{mpath}}: \text{session} \Rightarrow \text{multipath mode}
]

#### **(D) Service-level migration**

When a node becomes unreachable:

[
Φ_{\text{service}}: \text{endpoint} \Rightarrow \text{new endpoint}
]

This is part of the structural reliability model — not a special RPC mechanism.

#### **(E) Isolation downgrade (Χ + Φ)**

If failure is suspicious or matches a Ψ-defined risk pattern:

[
Φ_{\text{risk}} : \square \Rightarrow \square_{\text{sandbox}}
]

Used for:

* quarantining misbehaving nodes
* isolating a flooding endpoint
* preventing denial-of-service propagation

---

# **7.5.4 Congestion Handling (Θ, Λ, Σ, Ψ)**

Congestion is a **temporal mismatch** between offered load and available capacity.
PMS expresses congestion via:

* Λ — missing acknowledgments or delayed events
* Θ — adjusting rate windows
* Σ — committing congestion-control state
* Ψ — enforcing global fairness and safety

### **Congestion signals (Λ)**

Congestion typically manifests as:

* delayed ACKs
* queue overflows
* flow-control blocks
* missing heartbeats
* timeouts in P-REQ / P-CTRL

All of these are Λ events.

### **Rate adjustment (Θ)**

Θ governs:

* slow start (Θ doubling window)
* congestion avoidance (Θ linear increments)
* multiplicative decrease schedules
* pacing logic

### **Recontextualization under congestion (Φ)**

Φ may shift communication modes:

* from high-throughput → low-throughput mode
* switch encodings or compression
* split a stream into multiple substreams
* migrate traffic to alternate paths

### **Committing stable congestion state (Σ)**

When rate adjustments stabilize:

[
Σ_{\text{cc}} : \text{pending window updates} \Rightarrow \text{committed state}
]

Σ ensures:

* consistent congestion window
* consistent routing tables
* consistent flow-control parameters
* atomic updates across nodes (if coordinated)

### **Policy constraints (Ψ)**

Ψ enforces safety invariants:

* “No flow may exceed rate X across tenant boundary.”
* “Control-plane traffic must never be throttled.”
* “Encrypted traffic must not be dropped unless mandatory.”
* “Congestion control changes must be monotonic under conditions.”

Thus congestion handling is **governed**, not accidental.

---

# **7.5.5 High-Availability Links & Multi-Path Resilience (Φ + Σ + Ψ)**

High-availability networking is encoded through:

### **Redundant paths**

Φ chooses alternate frames:

[
Φ: \square_{path_1} \Rightarrow \square_{path_2}
]

### **Atomic failover state commit**

Σ commits the routing/connection-state change once stable.

### **Policies ensuring monotonic health**

Ψ prevents oscillations:

* forbid flapping between routes
* require minimum stability window before Φ is applied
* enforce bounds on retry behavior (Θ)

---

# **7.5.6 Session & Stream Resilience (Λ/Θ/Φ/Σ across PPS)**

PMS Protocol Suite (7.3) gains resilience automatically:

### **P-REQ (request/response)**

*Λ*: missing response
*Θ*: retry
*Φ*: alternate target, fallback version
*Σ*: commit final response or fallback result

### **P-EVT (event / notification)**

*Λ*: subscriber silent
*Θ*: retry with increasing intervals
*Φ*: degrade to offline buffer mode
*Σ*: finalize event delivery or discard based on Ψ

### **P-CTRL (control plane)**

Strong constraints:

* Ψ disallows loss of essential control-plane messages
* Φ recontextualizes during partition
* Σ ensures consistent routing state across all nodes

---

# **7.5.7 Partition Tolerance & Cluster Resilience**

Partition handling is unified via the Λ→Θ→Φ→Σ chain:

### **Detection (Λ)**

No messages from a region = partition suspected.

### **Temporal heuristics (Θ)**

Wait windows, confirmation attempts, stabilizing timers.

### **Recontextualization (Φ)**

Two sides reinterpret themselves as:

* partitioned‐primary
* partitioned‐secondary
* read‐only mode
* congestion-mode
* degraded cluster

### **Commit (Σ)**

Once conditions stabilize, cluster commits:

* new membership view
* new authority node
* new routing graph
* new isolation boundaries

Cluster-level Ψ invariants ensure safety:

* no two primaries
* no uncontested authority split
* no cross-partition write violations

---

# **7.5.8 Graceful Recovery & Reintegration (Σ + Φ)**

When a previously failed or isolated node reappears:

1. **Δ** identifies the re-joining principal
2. **Ω** validates capability (may have been revoked)
3. **Φ** recontextualizes:

   * version negotiation
   * resync
   * role reassignment
4. **Θ** drives step-by-step resync
5. **Σ** commits:

   * routing tables
   * membership view
   * flow-control params
   * node state alignment

Ψ ensures recovery does not violate consistency or security invariants.

---

# **7.5.9 End-to-End Structural Pattern**

All resilience mechanisms reduce to the canonical PMS pattern:

[
\Lambda \quad \text{(failure)}
;\rightarrow;
\Theta \quad \text{(temporal recovery logic)}
;\rightarrow;
\Phi \quad \text{(fallback / recontextualize)}
;\rightarrow;
\Sigma \quad \text{(commit stable new state)}
]

This is *universal* for:

* congestion control
* routing failover
* session recovery
* partition tolerance
* control-plane stabilization
* service migration
* transport fallback
* multi-path redundancy
* buffering and offline delivery
* handshake retries
* role/capability escalation or downgrade

This structural pattern is what makes PMS networking **predictable, analyzable, and composable**.

---

# **8. Security & Governance**

## **8.1 Identity & Principal Model (structural)**

This section defines the **foundational identity substrate** used across PMS-CPU, PMS-OS, PMSL, the networking stack, drivers, IPC, and governance systems.
Principals exist because the system must decide *who may perform which transformations* (Ω, Ψ, Χ).

Identity is therefore a **first-class operator-level construct** that binds:

* **Δ** – distinction: who/what is acting
* **Ω** – role/capability: what asymmetries and permissions apply
* **Χ** – isolation boundaries: which contexts the principal may access
* **Ψ** – invariants/policies governing identities
* **Σ** – integration: long-term bindings (keys, attributes, capabilities)
* **Φ** – recontextualization: delegation, impersonation, sandbox transitions

---

# **8.1.1 Goals of the Principal Model**

The PMS identity framework must satisfy:

1. **Global uniqueness within a domain**
   Each principal is uniquely distinguishable by Δ.

2. **Role-binding and capability constraints**
   Principal attributes map into Ω — capabilities, privilege tiers, device permissions, network roles, etc.

3. **Frame-scoped identity**
   Identity must follow context (□):
   *per-frame identities*, *per-process identities*, *per-connection identities*.

4. **Isolation mapping (Χ)**
   Principals have *isolation domains* that determine accessible memory, IPC channels, and devices.

5. **Policy-controllability (Ψ)**
   Policies can restrict principal actions, revoke privileges, impose quotas, or reframe identity (Φ).

6. **Composable across nodes**
   Same structural definition works for:

   * local OS kernels
   * distributed systems
   * network connections
   * driver ecosystems
   * multi-node orchestration

---

# **8.1.2 What is a Principal in PMS?**

A **Principal** is the **atomic “actor identity” unit** in the system.

Formally:

```
Principal ::= {
    pid: PrincipalID,
    attrs: PrincipalAttributes,
    caps: CapabilitySet,   ; Ω
    frames: FrameScope,    ; □
    iso: IsolationDomain,  ; Χ
    pol: PolicyLinks       ; Ψ
}
```

### **pid — PrincipalID**

A globally unique identifier in the domain.
May be hierarchical:

* NodeID:LocalPID
* Cluster:Node:Service:Thread
* UserID:ProcessID
* DeviceClass:DeviceID

Generated via Δ (distinction).

### **attrs — PrincipalAttributes**

Metadata such as:

* type: user, service, kernel, driver, device, VM, container
* cryptographic materials (public keys)
* creation timestamps
* provenance
* resource limits (overridden by Ψ)

### **caps — CapabilitySet (Ω)**

The principal’s capabilities determine:

* memory access
* syscall subset
* device access
* IPC rights
* scheduling modes
* network roles
* privilege level transitions

### **frames — FrameScope (□)**

Defines:

* active address space
* namespace
* call-stack frame lineage
* mapping of identity into frame-specific roles

Identity can *change permissions depending on frame*.

### **iso — IsolationDomain (Χ)**

Defines boundaries:

* which processes can this principal access?
* which memory frames?
* what IPC channels?
* which namespaces?
* is this principal confined to a sandbox?

A principal’s isolation domain is enforced by both Ω and Χ.

### **pol — PolicyLinks (Ψ)**

Policies that constrain or extend the principal’s behavior:

* auditing rules
* mandatory access control
* invariants (e.g., cannot escalate without justification)
* key rotation rules
* quota policies
* revocation conditions

---

# **8.1.3 Principal Classes (Static Typology)**

PMS defines broad categories of principals:

### **1. User Principals**

Human-facing identity holders (conceptually):
UID-like or account-like identifiers.

### **2. Service Principals**

Long-lived internal identities:

* system daemons
* background tasks
* database service
* network broker

### **3. Process Principals (per execution context)**

Every process gets a principal identity:

* pid = (Node, ProcessID)
* inherits from user/service principal
* can be further restricted by isolation domain (Χ)

### **4. Thread Principals**

Optional, but permitted:

* each thread may hold its own derived principal
* used in highly secure systems with per-thread roles

### **5. Device Principals**

Each device/driver is a principal:

* allows fine-grained driver security (6.x)
* driver cannot exceed its capability domain

### **6. External Principals (Network)**

Remote identities:

* certificates
* public keys
* negotiated identities from 7.x (transport and PPS)

These interact with local principals via Φ (recontextualization) and Ψ (authorization logic).

---

# **8.1.4 Identity Binding Mechanisms (Δ, Σ, Ω)**

Binding identity happens through **integrative** operator chains:

### **(A) Creation Binding (Δ → Σ)**

When a process, service, device, or connection is created:

1. Δ distinguishes the new entity
2. Σ binds attributes + capabilities
3. Ω configures role
4. Χ establishes isolation
5. Ψ sets policy constraints

### **(B) Delegation Binding (Φ → Ω → Σ)**

A principal can delegate capabilities:

```
delegate(P_src, P_dst, cap):
    Φ – change interpretation of P_dst's context
    Ω – append cap to P_dst.capabilitySet
    Σ – commit delegation event to system log
```

Used for:

* privileged subprocess creation
* driver delegation
* network handshake identity passing
* IPC authority transfer

### **(C) Revocation Binding (Ψ → Σ)**

Ψ policies revoke:

* capabilities
* access
* identity validity
* isolation permissions

Σ commits the revocation.

---

# **8.1.5 Identity Across Frames (□)**

Principals must map across multiple frames:

### **(1) Execution Frames**

Each nested call stack frame may temporarily alter identity interpretation:

```
call foo():
    □ – new frame
    Ω – restrict/add capabilities
    Ψ – enforce contract
end frame – capabilities revert
```

### **(2) Memory Frames**

Access rights map directly to frame metadata:

* read/write/exec bits
* shared/mapped frames
* per-frame principal roles

### **(3) Network Frames**

Each connection (7.x) is a □ frame:

* has its own security context
* principal identity may be transformed via Φ (e.g., TLS handshake)
* mapped into local principal via Σ

---

# **8.1.6 Identity Across Isolation Boundaries (Χ)**

Isolation domains define:

* principals allowed inside a sandbox
* transitions permitted between parent and child domains
* rules for data exchange
* syscall whitelisting

Χ + Ψ = **Mandatory Isolation Invariants**

Example:

```
Process P1 → ISO_FORK → Child C1
Χ: C1 inherits minimal capabilities only
Ψ: C1 cannot escalate beyond parent’s domain
Ω: C1 may have additional internal roles
```

Isolation transitions are always mediated by Φ to recontextualize identity.

---

# **8.1.7 Identity in Distributed Contexts (Δ–Φ–Ψ)**

When a principal interacts across nodes:

### **Step 1: Distinguish remote principal (Δ)**

* parse credentials
* verify certificate/public key
* classify principal type

### **Step 2: Apply recontextualization (Φ)**

* map remote identity to local representation
* adjust role or capability set
* map remote isolation requirements into local ones

### **Step 3: Enforce policies (Ψ)**

* apply trust rules
* audit rules
* quota and usage policies
* forwarding constraints

### **Step 4: Commit final identity view (Σ)**

Identity becomes stable for the duration of the connection/session.

---

# **8.1.8 Identity Lifecycle**

A principal’s identity moves through:

1. **Creation (Δ→Σ)**
2. **Contextual refinement (□, Ω, Φ)**
3. **Active operation (∇ governed by Ω/Ψ)**
4. **Delegation or capability changes (Φ→Ω)**
5. **Isolation modifications (Χ)**
6. **Policy updates or revocations (Ψ)**
7. **Destruction / garbage collection (Σ final)**

---

# **8.1.9 Identity as a First-Class Security Primitive**

Identity is not a label — it is an **active structural participant** in the PMS transition system.

Principals:

* constrain allowable transitions
* carry policies forward through frames
* define the scope of isolation domains
* govern device/driver authority
* enforce network security
* harmonize distributed system semantics

Identity informs:

* which Δ distinctions are legal
* what ∇ impulses are allowed
* which □ frames can be entered
* when Λ timeouts apply
* who may initiate Φ/Ω transitions
* what Σ integrations are permissible
* how Ψ invariants constrain behavior

Identity is therefore the **anchor** of security and governance across the entire PMS architecture.

---

# **8.1.10 Identity Examples / Formal Identity Algebra**

To make PMS identities operational in kernels, distributed systems, drivers, and languages, we now define:

1. **A formal algebra of principal identities**
2. **Operator-induced transformations over identities**
3. **Worked examples**
4. **Invariants required for system security**

This algebra is minimal, closed, and directly aligned with PMS operators (Δ, Ω, Χ, Φ, Σ, Ψ).

---

# **8.1.10.1 Identity Algebra: Core Objects**

We define the algebraic structure:

[
\mathcal{I} = (ID, \circ, \sqsubseteq, \otimes, \triangleright, \uplus)
]

where:

### **1. ID — Set of identities**

Each identity is:

[
id = (pid, attrs, caps, frames, iso, pol)
]

as established in **8.1.2**.

### **2. Composition (∘)**

Identity composition represents **derivation**:

* new process from user
* thread from process
* device-instance from device-principal
* connection-context identity from remote principal

Formally:

[
id_{child} = id_{parent} \circ ctx
]

where **ctx** is a minimal context descriptor:

[
ctx = (\Delta_{\text{create}}, \Omega_{\text{adjust}}, \Chi_{\text{assign}}, \Psi_{\text{bind}})
]

Composition applies the context transformation to the parent principal.

### **3. Partial Order (⊑)**

A structural **subprincipal** relation:

[
id_a \sqsubseteq id_b
]

meaning:

* every capability of (id_a) is a subset of (id_b)’s
* every isolation domain of (id_a) is equal or more restrictive
* policies of (id_b) encompass those of (id_a)

Thus:

[
id_{thread} \sqsubseteq id_{process} \sqsubseteq id_{user}
]

and:

[
id_{sandbox} \sqsubseteq id_{process}
]

### **4. Capability Tensor (⊗)**

Binary operation combining capability sets:

[
caps(id_a \otimes id_b) = caps(id_a) \cup caps(id_b)
]

Used for:

* delegation
* merged identities in IPC
* driver-role augmentation

### **5. Action Authorization (⊳)**

A relation:

[
id \triangleright op
]

meaning:
**identity id is permitted (by Ω + Ψ) to execute operator op**.

This is determined by:

* capability set (Ω)
* policy constraints (Ψ)
* frame scope (□)
* isolation domain (Χ)

It defines the **admissible transition set** in PMS-UM (section 1.x).

### **6. Policy Union (⊎ or ⊎_Ψ)**

Combination of identity’s policies with global/system policies:

[
pol(id_1 \uplus id_2) = \Psi(id_1) \cup \Psi(id_2)
]

Used for:

* cluster-wide identity propagation
* merging network-derived policies
* applying capability inheritance with constraints

---

# **8.1.10.2 Operator-Induced Identity Transformations**

Each PMS operator affects identities in a formally definable way.

### **Δ — Identity Differentiation**

Produces a new unique principal ID:

[
id' = Δ(id) = (new_pid, attrs, caps, frames, iso, pol)
]

Used for:

* process creation
* device instantiation
* network session establishment
* driver subcontext creation

### **Ω — Role/Capability Adjustment**

Capability modification:

[
id' = Ω(id, C_{\pm})
]

where (C_{\pm}) adds or removes capabilities.

Must preserve:

[
id' \sqsubseteq id \otimes C_+
]

### **Χ — Isolation Refinement**

Defines a more restrictive isolation domain:

[
id' = \Chi(id, iso')
]

with:

[
iso' \subseteq iso(id)
]

Used for:

* sandbox entry
* per-connection isolation
* driver protection domains
* VM/container operations

### **Φ — Recontextualization**

Identity reinterpretation across boundaries:

[
id' = \Phi(id, frame_target, role_target)
]

Examples:

* entering kernel mode
* mapping remote identity to local
* applying new version semantics
* driver identity mapping inside bus controllers

### **Σ — Commit / Integration**

Identity fixation:

[
id' = \Sigma(id)
]

which freezes:

* certain attributes
* policies
* isolation domains

Used for:

* post-authentication identity lock
* committed cluster node identities
* stable driver identities once initialized

### **Ψ — Policy Enforcement**

Identity restriction or invariance:

[
id' = \Psi(id, rules)
]

Rules can:

* cap capabilities
* forbid specific operators
* limit time or resource consumption
* require audit even if allowed

Ψ can also render identity invalid (revocation).

---

# **8.1.10.3 Identity Algebra Laws**

To ensure global consistency, identities must obey:

### **(1) Composition Associativity**

[
(id \circ ctx1) \circ ctx2 = id \circ (ctx1 \circ ctx2)
]

Frame and policy scopes must compose in a well-defined way.

### **(2) Monotonicity of Capabilities**

If:

[
id_a \sqsubseteq id_b
]

then:

[
caps(id_a) \subseteq caps(id_b)
]

### **(3) Isolation Contraction Law**

Isolation can decrease but never increase without a privileged transition:

[
id' = \Chi(id, iso') \Rightarrow iso' \subseteq iso
]

and reverse expansion requires Ω or Ψ permission.

### **(4) Policy Expansion Monotonicity**

[
pol(id_a \uplus id_b) \supseteq pol(id_a)\cup pol(id_b)
]

### **(5) Action Authorization Consistency**

If:

[
id \triangleright ∇
]

then it must also be true that:

* Δ-preconditions can be met
* Ω grants capability
* Ψ does not forbid the action
* Χ does not block relevant access
* □ supports the frame

Thus authorization is **multi-factor valid**.

---

# **8.1.10.4 Worked Examples**

## **Example 1 — Process Creation from a User**

User identity:

```
id_u = {
  pid = U123,
  caps = {start_process, access_home},
  iso  = full_user_space,
  pol  = {...}
}
```

Process creation:

```
id_p = id_u ∘ ctx_proc
```

Where:

```
ctx_proc = (
   Δ_create,           ; new PID
   Ω_adjust={drop:system_caps}, 
   Χ_assign={proc_isolation},
   Ψ_bind={audit_on_syscalls}
)
```

Yields:

```
id_p = {
  pid = P8842,
  caps = {read, write, IPC},    ; reduced
  iso  = proc_isolation,
  pol  = combined-policies
}
```

## **Example 2 — Driver Identity Mapping (kernel ↔ driver)**

```
id_kern = {caps={manage_devices}, iso=kernel_space}
id_drv0 = id_kern ∘ ctx_driver
```

Context:

```
ctx_driver = (
   Δ_driver_instance,
   Ω_adjust={drop:kernel_memory_access, add:device_io},
   Χ_assign={driver_sandbox},
   Ψ_bind={device_policy}
)
```

Driver identity is:

* isolated
* capability-limited
* governed by device policies
* unable to escalate unless Ω/Ψ permit

## **Example 3 — Network Principal Mapping**

Remote identity:

```
id_remote = {
  pid = cert:CN=serviceA,
  caps = {net_client},
  pol  = {signed_by_CA}
}
```

Recontextualization via Φ:

```
id_conn = Φ(id_remote, frame=connection_frame, role=network_service)
```

Then Σ commits it:

```
id_conn_fixed = Σ(id_conn)
```

This becomes the identity used for:

* IPC
* service calls
* resource quotas
* audit logs

## **Example 4 — Impersonation with Delegation**

Delegation:

```
id_child = Φ(id_parent, frame_child, role_child)
id_child2 = Ω(id_child, add={subset_capabilities})
id_final  = Σ(id_child2)
```

This models:

* sudo-like operations
* service-to-service delegation
* privilege-limited subprocess creation

---

# **8.1.10.5 Minimal Identity Normal Forms**

To support efficient kernel and runtime implementation, define two **normal forms**:

### **(1) Local Normal Form (LNF)**

[
id = (pid, caps, frame, iso)
]

Policies and attributes baked into caps + iso.
Used inside:

* threads
* processes
* scheduling
* syscalls

### **(2) Distributed Normal Form (DNF)**

[
id = (pid, caps, frame, iso, pol, provenance)
]

Used for:

* cross-node identities
* network security
* remote services
* multi-node orchestration

---

# **8.1.10.6 Identity Validity Conditions**

An identity is **valid** iff:

1. pid is unique in domain
2. caps authorized by Ω
3. iso enforced by Χ
4. policies consistent under Ψ
5. identity stands in a valid frame □
6. any recontextualizations (Φ) preserve invariants
7. Σ integrations do not break constraints

These conditions prevent:

* unauthorized elevation
* frame escape
* isolation violations
* policy bypass
* impersonation
* identity confusion attacks

---

# **8.1.10.7 Summary**

Identity algebra provides:

* explicit identity objects
* formal transformations (Δ, Ω, Χ, Φ, Σ, Ψ)
* capability and isolation logic
* compositional derivation of principals
* strict invariants ensuring security
* normal forms for kernel + distributed scenarios

Identity is not a metadata tag — it is a **mathematically structured, operator-governed entity** that shapes every state transition in the PMS architecture.

---

# **8.2 Role & Capability System (Ω)**

*PMS-IT Architecture — Structural, Operator-Level Specification*

This section defines the **formal role and capability system** of the PMS architecture entirely in terms of **Ω**, **Ψ**, **Χ**, and **□**, consistent with all previous identity and kernel specifications.

The Ω-system governs:

* what actions can be performed,
* in which frames,
* under which invariants,
* with which isolation boundaries,
* and how these permissions evolve structurally over time.

No psychology — only structural roles, capabilities, constraints, and operator-level dynamics.

---

# **8.2.1 Purpose of Ω in the PMS Stack**

Ω is the **sole primitive operator** responsible for establishing structural asymmetries in any PMS machine.

Functions:

1. **Define allowed operator sets**
   (Which of Δ, ∇, □, Θ, Φ, Χ, Σ, Ψ an identity/process/driver may invoke)

2. **Bind capabilities to identities**
   (Ref. §8.1 Identity Model)

3. **Establish privileged pathways**
   (System calls, kernel transitions, device access, etc.)

4. **Restrict transitions**
   by excluding specific operator sequences based on identity and frame.

5. **Coordinate role changes across frames**
   (User → kernel, driver → isolated, node → cluster-service, etc.)

In short:

[
Ω : \text{identity} \rightarrow {\text{allowed operator subsets}}
]

and

[
(id \triangleright op) \Leftrightarrow op \in Ω(id) \land \Psi(id,op) \land \Chi(id)\text{-compatible}
]

---

# **8.2.2 Components of a Role**

A **role** is a structured permission descriptor:

[
role = (caps, frameScope, isoScope, policyScope)
]

Where:

### **(1) caps (capability set)**

The primitive actions enabled for this role.

[
caps \subseteq O \times \text{capabilites}
]

Capabilities specify **which operators** (O = {Δ…Ψ}) can be called under which parameters.

### **(2) frameScope (□-range)**

Which frames are visible/selectable by this role.

Example:

```
{ user_frame, process_frame }   ; user role
{ kernel_frame }                 ; kernel role
{ driver_sandbox, device_mmio }  ; driver role
```

### **(3) isoScope (Χ-domain)**

Which isolation boundaries the identity can enter/exit.

Example:

* cannot escape its container
* cannot access sibling driver sandboxes
* can move from user → process → thread, but not reverse

### **(4) policyScope (Ψ-subset)**

Which policies apply to the role and which it may modify.

Examples:

* user cannot modify system policies
* kernel can
* driver may only modify device-level policies
* network principal may have externally bound policies imported via Φ

---

# **8.2.3 Capability Definition**

A capability is defined structurally as:

[
cap = (op, domain, params)
]

Where:

* **op ∈ {Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ}**
* **domain** is a frame or resource subset
* **params** restrict invocation (resource limits, specific devices, specific pages, etc.)

Capabilities implement **fine-grained control** of permissible actions.

For example:

```
cap_write_page = (∇, domain={page_0..page_3}, params={write})
cap_switch_frame = (□, domain={user_frame → process_frame})
cap_commit_fs = (Σ, domain={fs_namespace}, params={commit})
cap_recontext = (Φ, domain={net->service}, params={version=2})
```

---

# **8.2.4 Capability Hierarchies and Lattices**

Capabilities form a **partial order**:

[
cap_a \sqsubseteq cap_b \quad \text{iff} \quad
(domain_a \subseteq domain_b) \land (params_a \subseteq params_b) \land (op_a = op_b)
]

Thus roles are **capability sets forming a join-semilattice**:

[
role = \bigvee cap_i
]

Capability union (⊗) is monotonic:

[
caps(id_a \otimes id_b) = caps(id_a) \cup caps(id_b)
]

Used for:

* delegation
* IPC identity merging
* distributed identity mapping

---

# **8.2.5 Role Transitions (Ω-transformations)**

Role transitions are performed by the operator Ω:

[
id' = Ω(id, \Delta caps, \Delta frameScope, \Delta isoScope, \Delta policyScope)
]

With constraints:

* **Capabilities can be dropped freely**, but added only if Ψ permits.
* **Isolation can only become more restrictive by default** (Χ contraction).
* **Frame scope changes must be consistent with privilege transitions**.
* **Policy scope changes must be validated by Ψ**.

Thus transitions follow:

[
id_{new} = id \circ ctx_{role}
]

where ctx includes Ω adjustments.

---

# **8.2.6 Role Types in the PMS-OS Kernel**

The system provides **canonical roles** built directly from Ω:

### **(1) User Role**

* Minimal capabilities
* Visible frames: user, home namespace
* Cannot modify policies
* Cannot access hardware frames directly
* Restricted isolation boundaries

### **(2) Process Role**

* Derived from user via Δ creation
* Gains action capabilities (∇ on memory pages)
* Gets isolated sandbox via Χ
* Frame scope includes process frames

### **(3) Kernel Role**

* Superset of capabilities
* Access to hardware frames (□)
* Can escalate or de-escalate other roles
* May modify system policies (Ψ)
* Root of isolation tree

### **(4) Driver Role**

* Specialized capability subset:

  * ∇ only on device-specific MMIO/register pages
  * No access to general kernel memory
* Frame scope includes only driver_sandbox and device I/O frame
* Policy-enforced boundaries via Ψ_driver
* Runtime transitions allowed under Φ (device reset/reprobe)

### **(5) Network Principal Role**

* Frame scope: connection_frame
* Capabilities limited to IPC, address resolution, protocol operations
* Imported policies via Φ during session establishment
* Restricted isolation to prevent state contamination

These are not “user categories”—they are purely **structural permission sets** defined by Ω and Ψ.

---

# **8.2.7 Ω as Enforcement: Authorization Semantics**

Authorization predicate for any operator invocation:

[
id \triangleright op(params)
]

is true iff *all* hold:

### **(1) Capability Check**

[
(op, domain, params) \in caps(id)
]

### **(2) Frame Check (□)**

The operator targets must lie within frameScope(id).

### **(3) Isolation Check (Χ)**

The action must not cross forbidden isolation boundaries.

### **(4) Policy Check (Ψ)**

No policy forbids this operator for this identity under current conditions.

### **(5) Operator Dependency Check**

Structure must be valid:

[
P(op) \subseteq Hist(s)
]

---

# **8.2.8 Role Refinement and Decomposition**

Roles can be decomposed into **micro-roles** or **subroles**:

[
role = \bigcup_i role_i
]

Example: a network service process may have:

* role_net_recv
* role_net_send
* role_fs_read
* role_tls_handshake

This decomposition enables:

* least-privilege isolation
* fine-grained auditing
* capability-scoped processes
* multi-frame execution limits

---

# **8.2.9 Temporal Roles (Θ + Ω)**

Roles can be time-bound:

[
Ω(id, \text{grant:cap}, expiry=t)
]

Encoded via Θ in meta-state.
Used for:

* temporary delegation
* session-scoped permissions
* ephemeral elevated capabilities
* driver update windows
* cluster maintenance modes

---

# **8.2.10 Summary**

Ω provides a **unified structural system** for:

* role definition
* capability composition
* permission enforcement
* operator-level authorization
* isolation and policy integration
* role transitions across frames and contexts
* distributed identity consistency

It is the foundation of **kernel privilege separation**, **driver safety**, **network security**, **filesystem access**, and **multi-node operations**.

---

# **8.3 Policy Definition & Enforcement (Ψ)**

*PMS-IT Architecture — Structural Governance Layer*

Ψ is the **highest-order operator** in PMS.
It defines, activates, evaluates, and enforces **system-wide or scoped invariants** that restrict *all other operators* (Δ–Σ) in real time.

Ψ governs:

* safety
* correctness
* consistency
* compliance
* resource constraints
* cross-frame behavior
* role transitions
* isolation boundaries
* scheduling fairness
* network trust
* filesystem integrity
* transactional state models

Ψ is thus the **binding contract layer** across all subsystems.

No psychology; strict structural semantics.

---

# **8.3.1 Purpose of Ψ in the System**

Ψ enforces **global or scoped rules** about what transitions are allowed.
It is not itself a transition that changes data — it constrains *all* transitions.

Formally:

[
\Psi : S \rightarrow {allow, deny, transform, halt}
]

For any operator invocation:

[
(id,op,params,s) \text{ is valid } \iff \Psi(s,id,op,params) = allow
]

Ψ is the final arbiter of:

* operator admissibility
* permitted role transitions (Ω)
* frame scope changes (□)
* isolation crossing (Χ)
* transformation semantics (Φ)
* commit conditions (Σ)

---

# **8.3.2 Structure of a Policy**

A **policy** is a tuple:

[
pol = (scope, conditions, actions, priority)
]

Where:

### **(1) scope**

Defines the domain in which the policy applies:

* system-wide
* per-frame
* per-process
* per-driver
* per-device
* per-connection
* per-node
* per-distributed-trust-domain

### **(2) conditions**

Predicates over:

* identity & roles (Ω)
* frame relations (□)
* isolation boundaries (Χ)
* operator being attempted
* resource usage
* time windows (Θ)
* prior operator history (dependency graph)
* external trust assertions (for network identities)

### **(3) actions**

What Ψ does when the conditions match:

* allow
* deny
* transform (redirect via Φ)
* isolate (Χ tighten)
* escalate (Ω restricted → fallback role)
* trigger commit/rollback (Σ)
* trap (Φ)
* halt (to S_H)

### **(4) priority**

Policies form a **priority-sorted set**, defining a deterministic evaluation order.

---

# **8.3.3 Policy Layers: Hierarchical Composition**

Policies are structured into layers:

1. **Ψ₀ — Machine Core Policies**
   Hardware-level invariants:

   * no execution outside executable frames
   * no writes to read-only pages
   * no privilege escalation without explicit operator
   * commit/atomicity requirements

2. **Ψ₁ — Kernel Policies**

   * scheduling constraints
   * syscall safety
   * IPC message shape invariants
   * driver access correctness
   * per-process memory bounds

3. **Ψ₂ — Filesystem & Network Policies**

   * read/write/exec for FS paths
   * per-connection caps
   * encryption/integrity requirements
   * routing constraints

4. **Ψ₃ — Application / Domain Policies**

   * per-service limits
   * cross-service access constraints
   * data-shape invariants

All Ψ layers form a **policy stack**:

[
Ψ = Ψ_0 \prec Ψ_1 \prec Ψ_2 \prec Ψ_3 \prec \dots
]

Each layer can override or restrict the layer above.

---

# **8.3.4 Policy Enforcement Mechanism**

At every operator application:

[
op(s) \xrightarrow{Ψ}
\begin{cases}
s' & allow \
s_f & deny/transform/halt
\end{cases}
]

### Enforcement order:

1. **Check structural preconditions** (0.3 dependencies)
2. **Check Ω-capabilities** (role/cap permissions)
3. **Check Χ-isolation rules**
4. **Run Ψ policy chain**
5. **Execute actual state transition**

Thus Ψ sits at the **final gate** before any operator actually commits.

---

# **8.3.5 Policy-Based Transformation (Φ + Ψ)**

Ψ may instruct the system to **transform** the current operation via Φ:

Example transformations:

* convert illegal memory access into trap
* reframe context for compatibility (version mismatch)
* redirect syscall to higher-privileged implementation
* enforce fallback IPC route
* attach or detach isolation layers
* reinterpret role or frame under alternative semantics

Formally:

[
Ψ(s,op) = transform(\Phi(pattern))
]

so the operator becomes:

[
op' = \Phi(op)
]

Execution continues under the new interpretation.

---

# **8.3.6 Policy Domains and Models**

### **(A) Memory Policies**

* region access rules
* W^X enforcement
* stack guard
* driver MMIO boundaries
* DMA safety

### **(B) Process & Thread Policies**

* max memory
* file descriptor limits
* allowed capabilities
* CPU quotas
* isolation barriers

### **(C) IPC & Synchronization Policies**

* message shape
* mailbox quotas
* channel directionality
* sender/receiver authorization

### **(D) Filesystem Policies**

* path-based permissions
* transactional guarantees
* namespace boundaries

### **(E) Network Policies**

* allowed protocols
* cryptographic requirements
* incoming/outgoing address scopes
* routing constraints

### **(F) Distributed Policies**

* trust anchors
* certificate/identity constraints
* cross-node capability delegations

All of these are expressed as Ψ rules over operators Δ–Σ.

---

# **8.3.7 Policy Algebra**

Policies form a structured algebra:

### **Union**

[
Ψ_A \cup Ψ_B = Ψ_{A,B}
]

### **Intersection**

[
Ψ_A \cap Ψ_B = Ψ_{A \land B}
]

### **Override**

[
Ψ_A \prec Ψ_B \Rightarrow B \text{ has priority}
]

### **Composition**

[
Ψ = Ψ_{core} \prec Ψ_{kernel} \prec Ψ_{runtime} \prec Ψ_{app}
]

### **Monotonic tightening**

Policies may only tighten unless explicit Φ-transformation granted:

[
Ψ' \subseteq Ψ \quad \text{is safe}
]

[
Ψ' \supseteq Ψ \quad \text{requires Φ-validated recontextualization}
]

---

# **8.3.8 Policy Evaluation Semantics**

A general evaluation step:

```
function Psi_evaluate(id, op, params, s):
    for pol in sorted(policy_list):
        if pol.scope matches (id, frame(s), isolation(s)):
            if pol.conditions satisfied:
                return pol.actions
    return allow
```

Possible outcomes:

* **allow:** proceed with operator
* **deny:** operator forbidden; raise exception
* **transform:** replace op by Φ(op)
* **isolate:** apply Χ tightening
* **escalate:** controlled Ω role shift
* **rollback:** Σ-based rollback
* **halt:** transition to S_H

---

# **8.3.9 Policy Installation & Modification**

Ψ is modified only via Ψ-typed instructions:

```
SET_POL pol_id, cfg         ; Ψ
DEL_POL pol_id              ; Ψ
UPDATE_POL pol_id, cfg      ; Ψ
CHK_POL pol_id              ; Ψ
```

Constraints:

* only identities with capability `cap_modify_policy` may call these
* modifications may require Φ-mediated reframe
* cannot relax system-core Ψ₀ without privileged reboot path
* policies must remain internally consistent (checked by kernel Ψ validator)

---

# **8.3.10 Runtime Enforcement Examples**

### **1. Illegal Frame Write**

Process attempts:

```
STORE [kernel_frame+0x10], R1
```

Check path:

1. Ω: no capability → fail
2. Ψ: enforce trap → Φ(EXC_RAISE)

Result: exception, not crash.

---

### **2. Driver Exceeds Allowed IO Ports**

Driver tries to write outside allocated MMIO window.

Ψ yields:

```
action = isolate
```

So Χ applies:

* isolate driver context
* revoke capabilities
* notify kernel

---

### **3. Network Connection Without Required Crypto**

A network principal sends plaintext.

Policy:

```
if conn.requires_tls and packet.unencrypted:
    action = deny
```

Result: packet drop + optional event.

---

### **4. Process Exceeds Memory Quota**

Policy triggers:

```
action = transform(Φ_kill_or_oom)
```

Kernel terminates or reclaims memory.

---

# **8.3.11 Summary**

Ψ is the **governance spine** of the PMS architecture:

* defines safety and correctness rules
* restricts all operator transitions
* governs Ω role changes
* shapes □ frame functions
* enforces Χ isolation
* invokes Φ for reinterpretation or exceptions
* coordinates Σ commits and transactional consistency
* forms a multi-layer policy lattice

Everything in PMS-IT — CPU, OS, FS, networking, IPC, concurrency — is ultimately bound by Ψ rules.

---

# **8.4 Audit & Compliance Hooks (Θ + Σ)**

*PMS-IT Architecture — Structural Observation, Logging, and Evidence Layer*

Audit & compliance in PMS are *structural runtime consequences* of the temporality operator **Θ** (time, sequencing, progression) and the integration operator **Σ** (commit, finalization, consolidation).

**Θ** gives *when* and *in which order* events occur.
**Σ** gives *what actually became durable state*.

Together they form the foundation for a **verifiable, replayable, and trustable system history**.

No psychology — only system semantics.

---

# **8.4.1 Rationale: Why Θ + Σ Enable Auditing**

Auditing requires three invariants:

1. **Temporal ordering**
   *When did something happen?*
   → Provided by Θ ticks, sequence numbers, scheduling steps.

2. **Committed reality**
   *What ultimately happened?*
   → Provided by Σ commits, atomicity, transactional reductions.

3. **Cross-context coherence**
   *Events in one frame/role must be correlated across others.*
   → Provided by PMS frame/role identity, and Σ’s integration boundaries.

Thus PMS has **first-class primitives for trace integrity**, without inventing extra mechanisms.

---

# **8.4.2 Audit Events as Structured Θ-Records**

Every operator application (Δ–Ψ) may produce a structured **Θ-event**:

[
E = (ts, op, id, frame, role, result, meta)
]

Where:

* **ts** — Θ timestamp (logical or physical)
* **op** — the PMS operator invoked
* **id** — actor identity/principal (from 8.1)
* **frame** — active □ context
* **role** — Ω privilege state
* **result** — success/denied/transformed/isolated/etc.
* **meta** — optional attributes (size, address, syscall number, message shape)

The Θ-event stream is the **raw audit log**.

Θ defines ordering:

[
E_1 \prec E_2 \iff Θ(ts_1) < Θ(ts_2)
]

This ensures that all audits have a consistent, monotonic timeline even across isolation domains.

---

# **8.4.3 Σ as Durable Evidence (Commit-Grade Records)**

Not all Θ-events matter for compliance.
Only **committed effects** matter.

Σ marks the boundary:

* Before Σ → tentative, undoable actions (partial writes, provisional states).
* At Σ → state becomes binding.
* After Σ → audit evidence becomes authoritative.

Thus **Σ produces an immutable audit checkpoint**:

[
C = Σ(s) = (hash(s_c), frame, role, policies, resource usage, …)
]

Each Σ event can include:

* hash of memory frame or affected regions
* hash of FS content after commit
* resource deltas
* isolation boundaries at time of commit
* policy set (Ψ) in effect at commit
* identity/role of committer

This forms a **cryptographically chainable audit log** (even without requiring cryptography):
Each Σ state references its predecessor by Θ ordering and content hash.

---

# **8.4.4 Audit Scopes**

Policies can specify **audit scopes** to define what is recorded.

### **System-wide (Ψ₁-level)**

* privilege transitions
* frame transitions
* traps/exceptions
* isolation entry/exit
* syscalls
* driver events
* network connection lifecycle

### **Resource-level (Ψ₂-level)**

* FS writes
* memory allocation
* IPC sends/receives
* device IO

### **Domain-level (Ψ₃-level)**

* per-service events
* workflow/state-machine transitions
* protocol compliance (network PPS events)

Scope determines how much Θ metadata is emitted and which Σ commits create durable evidence.

---

# **8.4.5 Audit Hooks (Θ)**

Audit hooks are inserted **automatically** by:

* the kernel
* drivers
* the network stack
* the filesystem
* the scheduler
* isolation manager
* policy engine

Example hook types:

### **Θ.AUDIT_OP(op, id, frame, role)**

Emitted each time an operator is attempted.

### **Θ.AUDIT_ALLOW / Θ.AUDIT_DENY**

Result of policy evaluation.

### **Θ.AUDIT_FRAME_ENTER/LEAVE**

Every □ transition.

### **Θ.AUDIT_ROLE_CHANGE(old,new)**

Every Ω transition.

### **Θ.AUDIT_ISO_ENTER/EXIT**

Every Χ isolation boundary crossing.

### **Θ.AUDIT_NET(packet_meta)**

Message sent/received, with identity & routing data.

These events accumulate into the Θ-log before any Σ commit makes them final or prunable.

---

# **8.4.6 Commit Hooks (Σ)**

Σ integrates both **state** and **audit slices**.

A Σ event creates a **commit artifact**:

[
A_k = Σ(Θ_{i…j}, state)
]

Where:

* Θ_{i…j} — ordered set of Θ events since last Σ
* state — the post-commit machine state (or subset as defined by policy)

Each commit artifact A_k is:

* durable
* optionally hashed
* linked to A_{k-1}
* optionally written to FS or external logger
* optionally transmitted for distributed audit (e.g., in clustered systems)

**Σ enforces atomicity**:
The system cannot partially commit audit data.

---

# **8.4.7 Audit Storage and Rotation**

Audit data may be:

### **(1) In-memory Θ ring buffers**

Short-term history for debugging.

### **(2) FS-backed audit journal**

Structured, Σ-committed chunks (like FS journaling).

### **(3) Network-sent audit streams**

Forwarded to trusted remote logger or compliance collector.

### **(4) Distributed audit fabric**

For cluster-level invariants, each node’s Σ artifacts include cross-signatures of others.

Rotation policies (Ψ-managed):

* maximum size
* retention time
* tamper-prevention rules
* purge-on-commit
* encrypt-before-write (if network domain demands)

---

# **8.4.8 Policy-Driven Audit Requirements (Ψ + Θ + Σ)**

A policy may state:

* what must be audited
* when it must be committed
* how audit must be stored
* what failure response occurs if audit cannot be performed

Examples:

### **Example A: “all network packets must be logged”**

Ψ-network:
[
∀send,recv: Θ.\text{AUDIT_NET}(…) \land Σ\text{ include NET events}
]

### **Example B: “failed syscall must produce durable evidence”**

Ψ-kernel:
[
fail(syscall) \Rightarrow Θ.\text{AUDIT_DENY} ; Σ
]

### **Example C: “cross-isolation boundary writes must be committed with hash”**

Ψ-iso:
[
Χ\text{ boundary-cross} \Rightarrow Σ(\text{hash-of-scope})
]

### **Example D: “all actions by role R must be logged”**

Ψ-role:
[
r=R \Rightarrow \text{audit everything}
]

---

# **8.4.9 Compliance Verification**

Compliance frameworks act on:

* the Θ-log (event stream)
* Σ-commits (durable, tamper-evident snapshots)
* identity graph (8.1)
* role/capability lattice (8.2)
* active/past policies (8.3)

A compliance verifier checks:

* invariant satisfaction across Θ timelines
* no forbidden Δ/∇ operations
* no cross-boundary actions without correct Ω+Ψ authorization
* all required audits present
* Σ commits consistent and unbroken
* no unexpected Φ exception or rollback sequences
* resource quota compliance

Compliance is a **policy-based meta-check**; it uses the same Ψ mechanism.

---

# **8.4.10 Distributed Audit & Σ-Chaining**

For multi-node systems:

* each node commits A_k
* transmits hash(A_k) to peers
* receives hashes from them
* forms a **Merkle chain or DAG of Σ-commits**

This allows:

* cluster-wide ordering
* detection of tampering
* cross-node compliance
* distributed rollback recovery
* replicated audit logs

This is structurally enabled by Θ ordering and Σ commit semantics — no extra constructs required.

---

# **8.4.11 Auditable Subsystems Overview**

| Subsystem | Θ Events                              | Σ Commits                           |
| --------- | ------------------------------------- | ----------------------------------- |
| CPU       | instruction-level trace, role changes | atomic operations, fences           |
| Kernel    | syscalls, scheduling, traps           | process state commits, IPC delivery |
| Memory    | allocation, faults                    | page-table & frame commits          |
| FS        | path ops                              | writeback, transaction commit       |
| Network   | send/recv events                      | connection/flow boundaries          |
| Drivers   | MMIO ops                              | configuration changes               |
| Isolation | boundary crossings                    | sandbox creation/destruction        |
| Policies  | evaluation                            | policy-set change commits           |

Auditing is **unified** under Θ and Σ across all layers.

---

# **8.4.12 Summary**

Audit & compliance in PMS-IT are not add-ons — they are **emergent from the execution model**:

* **Θ** provides ordering, timing, causal structure, and fine-grained event capture.
* **Σ** produces durable, atomic, tamper-evident commit points.
* **Ψ** defines what must be audited and what compliance means.
* **Ω, □, Χ, Φ** add the structural context needed for correct interpretation.
* **Identities & principals (8.1)** anchor all events to actors.

Together, PMS provides a **full structural audit trail**, suitable for:

* debugging
* compliance
* forensic reconstruction
* distributed trust
* safety-critical systems

---

# **8.5 Key / Trust Anchor Management (Φ / Ψ)**

*PMS-IT Architecture — Structural Cryptographic Rooting, Context Shifts, and Invariant Enforcement*

This section defines the PMS-native model for **trust anchors, keys, credentials, and attestation infrastructure**, entirely grounded in **Φ** (recontextualization / exception / interpretation shift) and **Ψ** (policy / invariant).

No psychology.
Only structural roles, frames, identities, and operator-level logic.

---

# **8.5.1 Why Φ + Ψ Form the Trust Infrastructure**

In PMS:

* **Ψ** governs *what is accepted*, *what must be true*, and *what transitions are allowed* → **invariant layer**
* **Φ** governs *how something is to be interpreted* → **recontextualization layer**

Trust anchors — public keys, certificates, root-of-trust objects — are **interpretation mechanisms** (Φ) backed by **policy-level invariants** (Ψ).
Thus:

[
\text{Trust} = Φ(\text{credentials}) \quad \text{subject to} \quad Ψ(\text{policies})
]

And:

* Key rotation = controlled Φ
* Key validation = Ψ-check
* Compromise handling = Φ + Ψ-triggered reframe
* Root-of-trust definition = Ψ-level hard invariant

The PMS model does **not** treat keys as magical objects; they are simply **frames containing distinguishing data** whose interpretation depends on established policy invariants.

---

# **8.5.2 Key Material as PMS Frames (□)**

A key is a **frame with structured content**:

[
keyFrame = \square(\text{material},\text{type},\text{scope},\text{metadata})
]

Where:

* **material** — raw bytes of key or certificate
* **type** — public/private/symmetric/ephemeral
* **scope** — which identities/roles may use it
* **metadata** — algorithm, key length, expiry (Θ), allowed usage (Ω), commit bindings (Σ)

Key material is always kept inside **isolated subframes** (Χ), ensuring:

* separation of private keys
* distinction between runtime secrets and persistent trust anchors
* restricted copy paths enforced by Ω + Ψ

Thus:
**keys = structured, isolated frames with explicit usage roles**.

---

# **8.5.3 Trust Anchors as Policy Constraints (Ψ)**

A **trust anchor** is defined as:

[
TA = (keyFrame, Ψ_{verify}, Ψ_{use}, Ψ_{rotate})
]

Meaning:

1. **Ψ_verify**
   Policies for validating another key or signature using this anchor.

2. **Ψ_use**
   Policies determining where this anchor’s trust can propagate (e.g., signing binaries, validating boot images, verifying network peers).

3. **Ψ_rotate**
   Policies defining when and how this anchor may be updated, replaced, revoked, or reinterpreted.

Trust anchors are **never used directly**; their effects always go through Ψ-evaluation.

Example:

```
Ψ_verify_signed_kernel :  
    TA_root ⊢ verify(kernel_image.signature)
```

If a kernel image fails verification → a **Φ-exception reframe** is triggered (boot failure, quarantine, fallback).

---

# **8.5.4 Φ for Key Interpretation, Rotation, and Revocation**

Recontextualization (Φ) handles all cases where the meaning of key material changes:

### **(A) Key Rotation**

[
Φ_{rotate}(keyFrame_{old}, keyFrame_{new})
]

Creates a new interpretation context:

* new signing/verification rules
* rebinds policies using this key
* optionally preserves lineage metadata

### **(B) Key Revocation**

[
Φ_{revoke}(keyFrame)
]

Triggers:

* removal from trust anchor list
* immediate Ψ rules forbidding signing/verification
* optional fallbacks or quarantine modes

### **(C) Rolling Interpretation Windows**

Keys with time-bound validity (Θ metadata):

[
Φ(\square_{key}, t) =
\begin{cases}
\text{valid}, & t_current < t_{expiry} \
\text{expired}, & \text{otherwise}
\end{cases}
]

Expiration is just a **time-based Φ-shift** in the meaning of the frame.

### **(D) Cross-Version Trust Conversion**

Example: OS upgrade or new protocol version:

[
Φ_{version}(keyFrame, newInterpretationRules)
]

Updates how signatures or identities are interpreted under a new code context.

---

# **8.5.5 Key Usage Bound by Ω (Role Constraints)**

The role/capability system (Ω) restricts which identities may perform:

* signing
* decryption
* verification
* key extraction
* key generation

For a given identity id:

[
id \triangleright use(keyFrame)
]

iff:

1. cap(use(keyFrame)) ∈ caps(id)
2. keyFrame.scope permits use
3. Ψ_use rules allow it
4. Χ isolation rules permit access to the key material
5. □ frameSwitch is allowed (if moving into secure key frame)

Thus **Ω determines the structural surface** of key usage, while **Ψ determines semantic correctness**.

---

# **8.5.6 Σ for Key Commit & Durable Trust State**

Key installation, removal, or rotation is always finalized via **Σ**:

[
Σ(keyFrame, Ψ_{state})
]

This produces:

* a durable record of trust configuration
* optional hash of trust anchor set
* binding to logs (Θ)
* persistence across reboots

Use-cases:

* log of all key additions/removals
* reproducible trust state after boot
* cluster-wide synchronization of trust state

Σ ensures **keys enter durable system state only through transactional integration**.

---

# **8.5.7 Boot-Time Trust Anchor Integration**

Boot process is structurally:

1. Load root-of-trust keyFrames
2. Apply Ψ_verify(policy) to check boot image
3. Φ-shift into "trusted" or "untrusted" boot context
4. Σ commit trust state

This process is **operator-complete**:

* Δ distinguishes signature types
* □ selects boot frame
* Θ orders boot stages
* Ω restricts what can modify trust anchors
* Ψ enforces invariants
* Φ handles fallback or recovery
* Χ isolates boot loaders
* Σ commits validated states

---

# **8.5.8 Network Trust Anchors (Distributed Ψ + Φ)**

Network nodes establish trust using:

### **Ψ_session**

Defines acceptable credentials, ciphers, and handshake steps.

### **Φ_negotiate**

Recontextualizes connection based on:

* remote key
* protocol version
* identity mapping
* cluster policy

### **Σ_session**

Commits established session keys, routing permissions, and identity links.

Thus network trust becomes:

[
Φ(\text{peerKey}) \land Ψ(\text{policy}) \Rightarrow \Sigma(\text{sessionState})
]

With full PMS grounding.

---

# **8.5.9 Distributed Trust Anchors & Cross-Node Ψ**

Clusters or multi-node systems synchronize trust as follows:

1. Each node maintains a trust anchor set (Σ-committed).
2. Nodes exchange Θ-signed summaries (hashes, timestamps).
3. Φ resolves conflicts or divergent trust states.
4. Ψ policies enforce consistency rules (e.g., majority, quorum, external authority).
5. Σ creates unified trust anchor commits across nodes.

This enables:

* distributed CA
* multi-node signing authorities
* consistent certificate revocation
* cluster governance (see section 12)

---

# **8.5.10 Examples of Trust Anchor Types**

### **Static Root-of-Trust Key**

* Lives in immutable frame (Χ)
* Ψ forbids rotation
* Only allowed to verify OS/kernel images

### **Rotatable Root**

* Versioned keyFrames
* Φ handles rotation-path
* Ψ controls conditions under which rotation is allowed

### **Intermediate Authorities**

* Policies define issuance rules
* Φ handles certificate signing and re-signing

### **Session Keys**

* Transient frames with Θ-expirations
* Not persisted through Σ

### **Driver Keys**

* Bound to driver_sandbox scope
* Used for authenticating firmware or device config

### **Cluster Governance Keys**

* Represent collective identities (8.1.9)
* Ψ ensures quorum-based recontextualization

---

# **8.5.11 Summary**

Key and trust management in PMS follows directly from PMS operator logic:

| Layer                              | Operator | Role                                                  |
| ---------------------------------- | -------- | ----------------------------------------------------- |
| **Interpretation of keys**         | Φ        | Recontextualize key meaning, rotation, version shifts |
| **Trust invariants**               | Ψ        | Define validity, acceptance, propagation rules        |
| **Permission to use keys**         | Ω        | Assign structural capabilities                        |
| **Isolation of key materials**     | Χ        | Secure frames, sandboxed key stores                   |
| **Key storage and commit**         | Σ        | Durable system-wide trust state                       |
| **Metadata / lifecycle**           | Θ        | Expiry, time-based transitions                        |
| **Distinctions between key types** | Δ        | Key type, algorithm, usage classification             |
| **Frame-based key organization**   | □        | Where keys live in memory/FS/VM                       |

This provides a complete, rigorous, operator-grounded trust system across:

* boot,
* kernel,
* drivers,
* networking,
* distributed systems,
* language runtime,
* and storage.

---

# **9. PMSL – Language Specification**

## **9.1 Lexical & Grammar (BNF)**

PMSL is a **statically typed, PMS-structured language** whose syntax is designed so that:

* every construct can be **annotated** with a PMS operator (Δ…Ψ), and
* the compiler can emit an **operator-tagged IR** (section 11.1) that respects the dependency monoid from 0.3.

This section is **purely syntactic**:

* characters → tokens
* tokens → grammar (BNF)
* hooks for PMS operator annotations

Types, effects, operator mapping, and concurrency semantics come in 9.2–9.5.

---

## **9.1.1 Source Text & Character Set**

* **Encoding:** UTF-8.
* **Case sensitivity:** PMSL is **case-sensitive**.
* **Line terminators:** `\n` (LF) is canonical; `\r\n` is allowed and normalized.

**Character classes (abstract):**

* `LETTER` – `A–Z`, `a–z`, plus `_` and Unicode letters.
* `DIGIT` – `0–9`.
* `WS` – whitespace: space, tab, carriage-return, newline.

---

## **9.1.2 Tokens & Lexical Rules**

Lexing rules (informal) followed by precise token definitions.

1. The source is read left-to-right and split into **tokens**.
2. `WS` and comments are **ignored**, except where they separate tokens.
3. Longest-match rule: when multiple tokens can be recognized, pick the longest.

### **Comments**

```text
LineComment  ::= "//" { any-char-except-newline } 
BlockComment ::= "/*"  { any-char } "*/"         // nesting not required by spec
```

Comments are lexically removed.

### **Identifiers**

```bnf
Identifier ::= Letter { Letter | Digit }
Letter     ::= "A"…"Z" | "a"…"z" | "_" | UnicodeLetter
Digit      ::= "0"…"9"
```

* Identifiers starting with `_` are reserved for generated / internal symbols (tooling, runtime).

### **Literals**

**Boolean:**

```bnf
BoolLit ::= "true" | "false"
```

**Integer:**

```bnf
IntLit  ::= DecInt | HexInt | BinInt

DecInt  ::= DigitNonZero { Digit }
         | "0"

DigitNonZero ::= "1"…"9"

HexInt  ::= "0x" HexDigit { HexDigit }
HexDigit ::= Digit | "a"…"f" | "A"…"F"

BinInt  ::= "0b" BinDigit { BinDigit }
BinDigit ::= "0" | "1"
```

**Float:**

```bnf
FloatLit ::= DecInt "." { Digit } [ ExpPart ]
           | "." Digit { Digit } [ ExpPart ]
           | DecInt ExpPart

ExpPart  ::= ("e" | "E") [ "+" | "-" ] DecInt
```

**String:**

```bnf
StringLit ::= "\"" { StringChar } "\""

StringChar ::= any char except '"' or '\'
             | EscapeSeq

EscapeSeq  ::= "\\" ( "\"" | "\\" | "n" | "r" | "t" | "0" | "u{" HexDigit {HexDigit} "}" )
```

**Char:**

```bnf
CharLit ::= "'" CharChar "'"

CharChar ::= any char except "'" or '\'
           | EscapeSeq
```

**Bytes (optional but useful):**

```bnf
BytesLit ::= "b\"" { ByteChar } "\""
ByteChar ::= StringChar
```

---

## **9.1.3 Keywords**

Keywords are reserved identifiers and cannot be used as user-defined names.

### **Structural / module**

```text
module, import, as, from, expose, alias
```

### **Types & declarations**

```text
type, struct, enum, union, trait, impl, fn, proc,
let, var, const
```

### **Control flow**

```text
if, then, else, match, case, of,
while, for, in, loop, break, continue, return
```

### **Concurrency / IPC / processes**

```text
spawn, async, await, send, recv, select,
process, actor, channel
```

### **Roles / policies / security**

```text
role, capability, policy, requires, ensures, with,
principal, as_role, assume, assert
```

### **Exceptions / events**

```text
try, catch, finally, raise, signal, timeout
```

### **Misc**

```text
true, false, null, unit
```

PMS-operator names (`delta`, `nabla`, `phi`, etc.) are **not** keywords; operator **annotations** use a different lexical channel (see below).

---

## **9.1.4 Operators & Punctuation**

**Arithmetic & bitwise:**

```text
+  -  *  /  %  &  |  ^  <<  >>  ~
```

**Comparison & logical:**

```text
==  !=  <  <=  >  >=
&&  ||  !
```

**Assignment & composition:**

```text
=  :=  +=  -=  *=  /=  %=  &=  |=  ^=  <<=  >>=
->  =>  ::
```

* `=` – value binding / simple assignment
* `:=` – *rebind* / mutable update (semantics in 9.2)
* `->` – function/arrow type
* `=>` – match/guard arrow, or lambda body
* `::` – path separator for modules/types

**Punctuation:**

```text
(  )  [  ]  {  }
,  ;  :  .  @  #
```

---

## **9.1.5 PMS Operator Annotations (Δ, ∇, □, …)**

PMSL allows **explicit tagging** of syntactic constructs with PMS operators, both in **Unicode** and in **ASCII**.

### **Operator tokens**

Unicode forms:

```text
Δ  ∇  □  Λ  Α  Ω  Θ  Φ  Χ  Σ  Ψ
```

ASCII aliases (case-sensitive):

```text
DELTA, NABLA, FRAME, LAMBDA0, ATTR, OMEGA, THETA,
PHI, CHI, SIGMA, PSI
```

The lexer recognizes:

* either a single Unicode symbol (e.g. `Δ`)
* or its ASCII alias (e.g. `DELTA`)

as an **OpTag** token when used in annotation position.

### **Annotation syntax**

**Statement / expression annotation:**

```bnf
OpAnnot  ::= "@" OpTag
OpTag    ::= "Δ" | "∇" | "□" | "Λ" | "Α" | "Ω" | "Θ" | "Φ" | "Χ" | "Σ" | "Ψ"
           | "DELTA" | "NABLA" | "FRAME" | "LAMBDA0" | "ATTR"
           | "OMEGA" | "THETA" | "PHI" | "CHI" | "SIGMA" | "PSI"
```

Usage examples (informal):

```pmsl
@Δ if x > 0 { ... }

@∇ let y = x + 1;

@Ω role Admin { ... }

@Σ commit_changes();
```

**Block / declaration annotation:**

```pmsl
@Φ
fn migrate(old: OldType) -> NewType { ... }

@Ψ
policy NoRawSyscalls { ... }
```

Semantically:

* At most **one** primary OpTag per syntactic node.
* Additional tags (e.g. meta-annotations) are possible via attributes (`#[…]`) but defined in 9.2.

---

## **9.1.6 High-Level Grammar Overview**

We now give a **core BNF** for PMSL, sufficient to parse full programs and attach OpTags.
Details of types and constructs will be refined in 9.2–9.4.

BNF convention:

```bnf
<nonterm> ::= production
           | alternative
{ X }     ::= zero or more repetitions
[ X ]     ::= optional
```

---

### **9.1.6.1 Program & Modules**

```bnf
Program       ::= { TopLevelDecl }

TopLevelDecl  ::= ModuleDecl
                | ImportDecl
                | TypeDecl
                | RoleDecl
                | PolicyDecl
                | ProcessDecl
                | FnDecl
                | ConstDecl

ModuleDecl    ::= "module" ModulePath "{" { TopLevelDecl } "}"

ModulePath    ::= Identifier { "::" Identifier }

ImportDecl    ::= "import" ModulePath [ "as" Identifier ]
                | "import" ModulePath "::" "{"
                      ImportItem { "," ImportItem }
                  "}"

ImportItem    ::= Identifier [ "as" Identifier ]
```

---

### **9.1.6.2 Declarations (sketch)**

```bnf
ConstDecl     ::= "const" Identifier ":" Type "=" Expr ";"

TypeDecl      ::= "type" Identifier TypeParamsOpt "=" TypeBody ";"

TypeParamsOpt ::= [ "<" TypeParam { "," TypeParam } ">" ]
TypeParam     ::= Identifier

TypeBody      ::= StructBody
                | EnumBody
                | AliasBody
                | UnionBody

StructBody    ::= "struct" "{" FieldDecl { ";" FieldDecl } [ ";" ] "}"
FieldDecl     ::= Identifier ":" Type

EnumBody      ::= "enum" "{" EnumVariant { "," EnumVariant } [ "," ] "}"
EnumVariant   ::= Identifier [ "(" Type { "," Type } ")" ]

AliasBody     ::= Type

UnionBody     ::= "union" "{" FieldDecl { ";" FieldDecl } [ ";" ] "}"

RoleDecl      ::= [ OpAnnot ] "role" Identifier
                  "{" RoleItem { ";" RoleItem } [ ";" ] "}"

RoleItem      ::= "capability" Identifier ":" CapabilitySpec

CapabilitySpec ::= Type                          // details in 8.2 / 9.3

PolicyDecl    ::= [ OpAnnot ] "policy" Identifier
                  "{" PolicyClause { ";" PolicyClause } [ ";" ] "}"

PolicyClause  ::= "requires" Expr
                | "ensures" Expr
                | "forbid" Expr

ProcessDecl   ::= [ OpAnnot ] "process" Identifier
                  "(" ParamListOpt ")"
                  ProcessBody

ProcessBody   ::= Block
```

`FnDecl` will be the main function construct:

```bnf
FnDecl        ::= [ OpAnnot ]
                  "fn" Identifier
                  "(" ParamListOpt ")"
                  [ "->" Type ]
                  FnBody

ParamListOpt  ::= [ Param { "," Param } ]
Param         ::= Identifier ":" Type

FnBody        ::= Block
                | "=>" Expr   // expression-bodied (lambda-like)
```

---

### **9.1.6.3 Blocks, Statements, and Operator Annotations**

A **block** introduces a scope (□ at the language level):

```bnf
Block         ::= "{" { Stmt } "}"
```

Every statement can optionally carry an **OpAnnot**:

```bnf
Stmt          ::= [ OpAnnot ] CoreStmt

CoreStmt      ::= LetStmt
                | VarStmt
                | ExprStmt
                | IfStmt
                | MatchStmt
                | WhileStmt
                | ForStmt
                | ReturnStmt
                | BreakStmt
                | ContinueStmt
                | SpawnStmt
                | SendStmt
                | RecvStmt
                | TryCatchStmt
```

**Bindings:**

```bnf
LetStmt       ::= "let" Pattern [ ":" Type ] "=" Expr ";"
VarStmt       ::= "var" Pattern [ ":" Type ] "=" Expr ";"

Pattern       ::= Identifier
                | "_" 
                | "(" Pattern { "," Pattern } ")"
```

**Expression statements:**

```bnf
ExprStmt      ::= Expr ";"
```

**Control flow:**

```bnf
IfStmt        ::= "if" Expr Block [ "else" BlockOrIf ]
BlockOrIf     ::= Block | IfStmt

MatchStmt     ::= "match" Expr "{"
                      MatchArm { MatchArm }
                 "}"

MatchArm      ::= "case" Pattern [ "if" Expr ] "=>" Block

WhileStmt     ::= "while" Expr Block

ForStmt       ::= "for" Pattern "in" Expr Block

ReturnStmt    ::= "return" [ Expr ] ";"
BreakStmt     ::= "break" ";"
ContinueStmt  ::= "continue" ";"
```

**Concurrency / IPC (hooks only; semantics in 9.4):**

```bnf
SpawnStmt     ::= "spawn" Expr ";"

SendStmt      ::= "send" Expr "to" Expr ";"
RecvStmt      ::= "recv" Expr "into" Pattern
                  [ "timeout" Expr ] ";"
```

**Exceptions & events:**

```bnf
TryCatchStmt  ::= "try" Block
                  "catch" "(" Pattern ")" Block
                  [ "finally" Block ]

RaiseStmt     ::= "raise" Expr ";"
SignalStmt    ::= "signal" Expr ";"
TimeoutStmt   ::= "timeout" Expr Block
```

(Last three can also be treated as `ExprStmt` with special Expr kinds.)

---

### **9.1.6.4 Expressions**

Expressions are PMSL’s core term language. We define them with familiar precedence, plus room for PMS-specific constructs.

```bnf
Expr          ::= LambdaExpr

LambdaExpr    ::= OrExpr
                | "|" ParamListOpt "|" "=>" Expr   // anonymous function

OrExpr        ::= AndExpr { "||" AndExpr }
AndExpr       ::= RelExpr { "&&" RelExpr }

RelExpr       ::= AddExpr
                | RelExpr RelOp AddExpr

RelOp         ::= "==" | "!=" | "<" | "<=" | ">" | ">="

AddExpr       ::= MulExpr { ("+" | "-") MulExpr }
MulExpr       ::= UnaryExpr { ("*" | "/" | "%") UnaryExpr }

UnaryExpr     ::= PrimaryExpr
                | ("+" | "-" | "!" | "~") UnaryExpr

PrimaryExpr   ::= Literal
                | Identifier
                | "(" Expr ")"
                | PrimaryExpr "." Identifier
                | PrimaryExpr "(" ArgListOpt ")"
                | "[" Expr { "," Expr } "]"       // list/array literal
                | BlockExpr

BlockExpr     ::= Block     // expression-valued block

Literal       ::= IntLit | FloatLit | StringLit | CharLit
                | BoolLit | BytesLit | "null" | "unit"

ArgListOpt    ::= [ Expr { "," Expr } ]
```

Operator precedence (highest to lowest):

1. Primary (`()`, `[]`, `.`, function call)
2. Unary (`+`, `-`, `!`, `~`)
3. Multiplicative (`*`, `/`, `%`)
4. Additive (`+`, `-`)
5. Relational (`<`, `>`, `<=`, `>=`)
6. Equality (`==`, `!=`)
7. Logical AND (`&&`)
8. Logical OR (`||`)

All binary infix operators are **left-associative**, except:

* comparison operators are **non-chainable** in this base grammar (i.e. `a < b < c` is not allowed syntactically; must write `(a < b) && (b < c)`),
* `=>` and `->` are right-associative where they occur.

---

### **9.1.6.5 Types (syntactic skeleton)**

Detailed type system in 9.3; here we just define syntax categories.

```bnf
Type          ::= ArrowType

ArrowType     ::= SumType [ "->" Type ]        // right-associative

SumType       ::= ProdType { "|" ProdType }    // union / variant-like

ProdType      ::= AppType { "*" AppType }      // product / tuples

AppType       ::= SimpleType { TypeArgList }   // type application

SimpleType    ::= Identifier
                | ModulePath "::" Identifier
                | "(" Type ")"
                | "[" Type "]"                 // list/array type
                | "unit"

TypeArgList   ::= "<" Type { "," Type } ">"
```

Examples (informal):

```pmsl
fn f(x: Int, y: Int) -> Int { ... }
type Maybe<T> = enum { None, Some(T) }
type Pair<A,B> = (A * B)
type Proc = process(Unit) -> Unit
```

---

## **9.1.7 Grammar Hooks for Operator-Typed IR**

To support the operator-tagged IR:

1. **Every statement and expression** admits an optional `OpAnnot`.

2. At the IR level, the compiler will:

   * decorate each node with **an effective operator tag**:

     * explicit `@Δ` etc. if present,
     * otherwise inferred from construct and context (9.2).

3. For convenience, the grammar can be seen as:

```bnf
AnnotatedNode ::= [ OpAnnot ] Node
```

where `Node` ranges over:

* `TopLevelDecl`
* `Stmt`
* `Expr` (for explicit expression-level ops)
* `TypeDecl`, `RoleDecl`, `PolicyDecl`, `ProcessDecl`, `FnDecl`

This structural hook guarantees that every executable piece of PMSL code can be traced back to a PMS operator in the monoid (0.3).

---

## **9.1.8 Minimal Example**

Illustrative PMSL snippet that type-checks under this grammar (semantics to follow later):

```pmsl
module example::counter {

    type Counter = struct {
        value: Int
    }

    @Ω
    role CounterUser {
        capability inc: Counter;
    }

    @Ψ
    policy NonNegative {
        requires self.value >= 0;
    }

    @∇
    fn inc(c: Counter) -> Counter {
        let next = c.value + 1;
        return Counter { value: next };
    }

    @Δ
    fn main() -> unit {
        let c0 = Counter { value: 0 };
        let c1 = inc(c0);
        if c1.value > 10 {
            // ...
        }
    }
}
```

This is **valid PMSL** lexically and grammatically per 9.1; the meaning of `@Ω`, `@Ψ`, `@∇` and the type `Counter` will be specified in:

* **9.2** – Core Constructs & Operator Mapping
* **9.3** – Type System
* **9.4** – Concurrency & IPC
* **9.5** – Error & Exception Handling

---

# **9.2 Core Constructs & Operator Mapping**

This section defines **how every core construct in PMSL maps to the PMS operator algebra**
(Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ).

**Goal:**
For every syntactic construct in PMSL (bindings, functions, control flow, blocks, concurrency, modules), we specify:

1. **Primary operator** (*what the construct fundamentally *is***)
2. **Secondary operators** (*implicit structural effects*)
3. **Compiler output** (operator-tagged IR form)

This is the semantic backbone that ensures PMSL → PMS-CPU → Kernel → Runtime remain **operator-consistent**.

---

# **9.2.1 Overview Table (High-Level Mapping)**

| PMSL Construct         | Primary PMS Op  | Secondary Ops      | Explanation                                                  |
| ---------------------- | --------------- | ------------------ | ------------------------------------------------------------ |
| `let` binding          | **Δ**           | Σ                  | Distinguish + integrate immutable binding                    |
| `var` binding          | **Δ**           | ∇, Σ               | Distinction + mutable state cell creation                    |
| Mutation (`x := e`)    | **∇**           | Σ                  | State-changing write, commit local update                    |
| Blocks `{ ... }`       | **□**           | Θ, Σ               | New context frame, structured sequence                       |
| Conditionals (`if`)    | **Δ**           | Θ, Φ               | Branch by distinction; Φ used in fallthrough simplifications |
| Loops (`while`, `for`) | **Α** (pattern) | Θ, Δ, ∇            | Loop attractor expands to internal Δ/Θ/∇ cycles              |
| Functions              | **□**           | Ω (roles), Σ       | Call frame = new □; return = Σ                               |
| Returns                | **Σ**           | Φ (escape context) | Integration of result + exit frame                           |
| Match/case             | **Δ**           | Θ                  | Multi-way distinction                                        |
| Try / catch / raise    | **Φ**           | Λ, Σ               | Recontextualization of error; Λ for absence of normal return |
| Async / await          | **Θ**           | Χ                  | Temporal suspension + isolated future                        |
| Channels / send / recv | **Δ / ∇**       | Λ, Θ, Ω            | Send = ∇; recv = Δ + Λ (timeout)                             |
| Spawning processes     | **Χ**           | Θ, Ω               | New isolated execution context                               |
| Modules                | **□**           | Ψ                  | Namespace frame, bound by policy                             |
| Imports                | **Δ**           | Σ                  | Distinguish & integrate symbol sets                          |

Below we go construct-by-construct.

---

# **9.2.2 Bindings (`let`, `var`, constants)**

## **1. `let` — Immutable Binding**

Semantic operator mapping:

* **Primary:** **Δ** — introduces a *new distinction* (name → value).
* **Secondary:** **Σ** — integrates the binding into the current frame.

IR form:

```
Δ(bind name)
Δ(eval expr)
Σ(install name=value)
```

Characteristics:

* No ∇ allowed on this symbol in this frame (enforced by Ψ-type rules).
* Compiled into a □-local namespace entry.

---

## **2. `var` — Mutable Binding**

Semantic operators:

* **Primary:** **Δ** — introduce variable name.
* **Secondary:** **∇** — allocate mutable cell.
* **Σ** — finalize binding into frame.

IR:

```
Δ(bind name)
Δ(eval initializer)
∇(allocate mutable cell)
Σ(install name → cell)
```

Ψ may restrict mutation privileges based on Ω (role).

---

## **3. Mutation (`x := e`)**

* **Primary:** **∇**
* **Secondary:** **Σ** — commit update to the variable’s cell

IR:

```
Δ(resolve x)
Δ(eval expr)
Ω(check write capability)
∇(write cell(x) ← value)
Σ(complete update)
```

---

# **9.2.3 Blocks & Scopes**

A block:

```pmsl
{
    statements...
}
```

maps to:

* **Primary:** **□** (new lexical frame)
* **Secondary:**

  * **Θ** — execution sequencing in the frame
  * **Σ** — integrate frame results (typically discard scope-locals except return value)

IR shape:

```
□(enter frame)
Θ(stmt1)
Θ(stmt2)
...
Σ(exit frame)
```

Return statements (below) inject **Φ+Σ** into block exit.

---

# **9.2.4 Control Flow**

## **1. `if` expression / statement**

An `if` is a **Δ-driven branching**:

```
if cond { t } else { f }
```

IR:

```
Δ(eval cond)
Ω(check branch capability if needed)
Θ(branch)
□ enter true/false frame
...
Σ(merge branch outputs)
```

Notes:

* Δ is the “type of branch path chosen”.
* Θ orders branch entry.
* Σ merges outcomes into a single continuation value.

---

## **2. `match` / `case`**

Pattern matching is **multi-way Δ**:

```
match x {
    case A(v) => ...
    case B    => ...
}
```

Mapping:

* **Δ(pattern-discriminate)** for each case arm
* **Θ** for sequential arm testing
* **Σ** at merge

---

## **3. Loops (`while`, `for`, `loop`)**

Loops are **Α – attractors**, expansions of reusable operator sequences.

Example:

```
while cond { body }
```

Expands to IR macro:

```
Α(LOOP) expands to:
LABEL start:
  Δ(cond)
  Θ(branch)
  if false → goto end
  □(enter body frame)
    body...
  Σ(exit body)
  Θ(step)
  goto start
LABEL end:
```

Operators involved:

* **Α** — loop macro/pattern
* **Δ** — check condition
* **Θ** — iteration ordering
* **□/Σ** — body frame

---

# **9.2.5 Functions and Calls**

## **Function Definition**

```
fn f(a: A, b: B) -> C { ... }
```

Maps to:

* **Primary:** **□** — function body = new evaluation frame.
* **Secondary:**

  * **Ω** — function may define required roles or capabilities.
  * **Σ** — on return, integrate return value into caller context.

IR template:

```
□(enter fn-frame)
Δ(bind parameters)
Θ(seq body statements)
Σ(return value)
```

---

## **Function Call**

* Evaluate arguments: Δ + Θ
* Create call frame: **□**
* Apply role/policy constraints: **Ω, Ψ**
* Execute body
* Return: **Σ + Φ** (exit context)

IR:

```
Δ(resolve function)
Δ(eval arg1)
...
□(enter call frame)
Θ(exec)
Σ(return integration)
Φ(pop frame context)
```

---

## **Return**

```
return e;
```

* **Σ** — integrate value as function output
* **Φ** — shift out of current frame (unwind)

IR:

```
Δ(eval e)
Σ(set return value)
Φ(exit frame)
```

---

# **9.2.6 Exceptions, Errors, Recontextualization (Φ, Λ)**

## **1. `try` / `catch` / `finally`**

```pmsl
try { ... } catch(e) { ... } finally { ... }
```

Semantic mapping:

* **Φ** — error → new interpretive context (exception)
* **Λ** — absence of normal result
* **Σ** — finalize body or handler

IR skeleton:

```
□ try-frame
Θ exec
if error:
   Φ(recontextualize → exception-frame)
   □ catch-frame
   Σ(merge)
finally:
   □ fin-frame
   Σ(merge)
```

---

## **2. `raise e`**

* **Φ** — reframe into error state
* **Λ** — suppress normal return path

IR:

```
Δ(eval e)
Φ(create exception context)
Λ(abort normal flow)
```

---

# **9.2.7 Concurrency & IPC Constructs**

## **1. `spawn expr`**

Creates a new isolated execution locus:

* **Primary:** **Χ** — new execution boundary
* **Secondary:** **Θ** — scheduler enqueues
* **Ω** — assign role/capabilities to subprocess

IR:

```
Δ(eval expr)
Χ(fork new context)
Ω(assign role)
Θ(schedule new task)
```

---

## **2. Channels: `send`, `recv`, `select`**

### **send x to ch**

* **Primary:** **∇** — mutate queue state
* Secondary:

  * **Ω** — capability to send
  * **Θ** — event sequencing

IR:

```
Δ(resolve ch)
Δ(eval x)
Ω(check send rights)
∇(enqueue x into ch)
Θ(signal receiver wakeup)
Σ(update channel state)
```

---

### **recv ch into var timeout t**

* **Primary:** **Δ** — check if message available
* **Λ** — if not and timeout fires
* **∇** — bind received value

IR:

```
Δ(resolve ch)
Δ(check queue head)
if empty:
   Θ(start timeout)
   Λ(on timeout)         // non-event
else:
   ∇(dequeue)
   Σ(bind var)
```

---

### **select { recv ch1; recv ch2; … }**

* Multi-way Δ
* Λ for timeouts
* Θ schedules readiness

---

# **9.2.8 Modules, Imports, Namespaces**

## **1. Modules**

`module X { ... }`

* **Primary:** **□** — namespace frame
* **Secondary:** **Ψ** — module-level invariants / visibility rules

IR:

```
□(enter module frame)
Ψ(apply module policy)
Σ(export module bindings)
```

---

## **2. Imports**

`import m::x as y`

* **Primary:** **Δ** — select symbol from module
* **Secondary:** **Σ** — merge into current namespace

IR:

```
Δ(resolve module path)
Δ(select symbol)
Σ(bind alias in frame)
```

---

# **9.2.9 Policies, Roles, Capabilities in PMSL Constructs**

PMSL exposes Ω/Ψ declarations directly:

### **`role`**

```
role Admin {
    capability shutdown: System;
}
```

Semantic:

* **Ω** — role definition operator
* **Ψ** — compiled rule for enforcement

IR:

```
Ω(declare role Admin)
Σ(register capabilities)
```

---

### **`policy`**

```
policy SafeFS {
    requires path.starts_with("/home");
}
```

* **Ψ** — invariants
* **Δ** — distinctions inside conditions
* **Σ** — finalize policy install

IR:

```
Ψ(define policy)
Σ(install into PSet)
```

---

# **9.2.10 Summary: PMSL → Operator-Typed IR Pipeline**

Every construct yields a well-typed sequence of operators:

```
AST node
    ↓ annotated by @OpTag or inferred tag
IR node
    ↓ expanded into primitive PMS ops (Δ…Ψ)
PMS Instruction Sequence
```

This guarantees:

* **Correct dependency structure** (0.3 monoid)
* **Operator-complete semantics**
* Direct mapping to **PMS-CPU ISA** (2.2)
* Compatibility with **Kernel policy engine** (3.6)

---

# **9.3 Type System (frames, roles, policies, processes)**

The PMSL type system is **structural**: types are *not* descriptions of data “shapes” alone, but **operator-validity constraints** over frames (□), roles (Ω), policies (Ψ), and process loci (Χ).
A PMSL type is therefore a **multi-component contract** that determines:

* What Δ/∇/Θ/Φ/Σ operations are **admissible**
* In which **frame (□)** they are evaluated
* Under which **role (Ω)**
* Under which **policy set (Ψ)**
* Inside which **execution locus/process (Χ)**

In other words:

> **A PMSL type is a *structural admissibility profile* for operator sequences.**

This is fundamentally different from classical languages (which type-check values).
PMSL types ensure **operator validity**, **context invariants**, and **safe transitions**.

---

# **9.3.1 Type System Overview**

The PMSL type system consists of four orthogonal but interacting kind-level categories:

1. **Frame Types (□-types)**
2. **Role Types (Ω-types)**
3. **Policy Types (Ψ-types)**
4. **Process Types (Χ-types)**

Additionally, PMSL still supports:

5. **Data Types** (primitive + structured) — but even these are expressed with Δ-based distinction operators and Σ-based integration.

All types ultimately reduce to constraints over operator-typed transitions.

---

# **9.3.2 Frame Types (□)**

A **Frame Type** describes:

* the **contextual domain** in which a value, computation, or module is valid
* the **operator constraints** tied to that context (e.g., allowed ∇ writes, allowed Φ migrations)

Formally:

```
FrameType F := {
    allowed_ops: O_subset,
    subframes: Set[FrameType],
    visibility: SymbolMap,
    lifetime: LifetimeSpec
}
```

### Structural Semantics:

* **□ introduces a new frame instance** of some FrameType.
* The FrameType determines which Δ/∇/Θ/Φ/Σ transitions are admissible *inside* it.

Examples of frame types:

| FrameType          | Structural Meaning                                      |
| ------------------ | ------------------------------------------------------- |
| `LexicalFrame`     | Standard scope; ∇ allowed on `var`; Σ flushes bindings  |
| `ModuleFrame`      | Named □ frame with export Σ; Ψ attaches module policies |
| `TransactionFrame` | Σ = commit; Φ = rollback; ∇ constrained until commit    |
| `IsolatedFrame`    | Used inside Χ (sandbox); restricted ∇/Φ/Ω               |

Frame subtyping:

```
F1 ≤ F2   iff   allowed_ops(F1) ⊆ allowed_ops(F2)
```

This is a *structural inclusion* relation.

---

# **9.3.3 Role Types (Ω)**

A **Role Type (Ω-type)** characterizes **capability sets** and **operator permissions**.

```
RoleType R := {
    capabilities: Set[Capability],
    allowed_ops: O_subset,
    escalation: Set[RoleType],
    downgrades: Set[RoleType]
}
```

* Capabilities correspond to structural acts (mutate FS, open socket, spawn process).
* RoleType is attached as the `r` component of the machine state.
* Ω transitions (role changes) are type-checked against this structure.

### Role Subtyping (Capabilities):

```
R1 ≤ R2   iff   capabilities(R1) ⊆ capabilities(R2)
```

### Protected Operators

Certain ops require Ω authorization:

* ∇ on privileged memory
* □ frame creation for kernel-level modules
* Χ spawning
* Φ exception-privileged reframing

This yields **operator-safety typing**:

> A term is well-typed under role R if all operators in its PMSL-expanded sequence are allowed under R.

---

# **9.3.4 Policy Types (Ψ)**

A **Policy Type** is the type-level encoding of a **Ψ invariant**, i.e., a rule constraining operator sequences.

```
PolicyType P := {
    invariants: Set[Invariant],
    scope: FrameType or Module,
    enforcement_points: Set[Op ∈ O]
}
```

Policies do *not* classify values — they classify **trajectories**.

### Policy Subtyping:

A policy P₁ is a subtype of P₂ iff:

```
invariants(P1) ⊇ invariants(P2)
```

(i.e., stronger policies are “subtypes”)

### Policy Composition:

The Σ operator defines policy merge:

```
P_combined = Σ(P1, P2)
```

Ψ instructions in IR enforce these at compile time and at runtime.

Example policy types:

| PolicyType      | Enforced Invariants             |
| --------------- | ------------------------------- |
| `SafeFS`        | path must start with /home      |
| `NoNetwork`     | forbid Δ/∇ on socket ops        |
| `ReadOnlyFrame` | forbid ∇ except on local stack  |
| `SecureModule`  | forbid Φ out of module boundary |

Policies rewrite type-checking constraints on permitted Δ/∇/Φ/Χ transitions.

---

# **9.3.5 Process Types (Χ)**

A **Process Type** describes the isolation boundary:

```
ProcessType Proc := {
    isolation_level: IsoLevel,
    allowed_syscalls: Set[Syscall],
    namespace: FrameType,
    scheduler_class: SchedType
}
```

* Χ creates a new process
* ProcessType determines which kernel ops are admissible
* Χ-type subtyping relates to containment levels:

```
Proc_sandbox ≤ Proc_user ≤ Proc_system
```

Operator restrictions follow:

* Sandbox → restricted ∇, Φ, no raw FS access
* User → normal privileges
* System → broad but policy-bound privileges

---

# **9.3.6 Data Types (Δ-derived)**

Even simple data types arise structurally from Δ distinctions.

Primitive examples:

```
Bool := Δ{true,false}
Int := Δ ℤ
String := Δ* over character alphabet
```

Composite types are Σ-integrations:

```
Tuple[T1,T2]  := Σ(T1, T2)
List[T]       := Α(pattern using Σ + Θ)
Option[T]     := Δ{none:Λ, some:T}
Result[T,E]   := Δ{ok:T, err:E via Φ}
```

This yields a uniform structural foundation:

* **Sum types = Δ**
* **Product types = Σ**
* **Sequential types = Θ**
* **Error types = Φ + Λ**
* **Patterned types = Α**
* **Isolated/linear types = Χ**

---

# **9.3.7 Putting It All Together: Typed Judgement Form**

We define the typing judgment in PMSL as:

### **Expression Typing**

```
Γ ⊢ e : T   under (F : FrameType, R : RoleType, P : PolicyType, Proc : ProcessType)
```

with Γ = binding environment (Δ/Σ-constructed).

Meaning:

> Expression e is valid if all operator sequences produced by e are admissible under the quadruple (F, R, P, Proc).

---

# **9.3.8 Type Soundness (Structural)**

Two key theorems:

### **Preservation**

If:

```
Γ ⊢ e : T
(s, e) → (s', e')
```

then:

```
Γ ⊢ e' : T
```

because transitions respect Ω/Ψ constraints and remain within allowed ops of FrameType & ProcessType.

### **Progress**

If:

```
Γ ⊢ e : T
```

then e is either:

* a value (Σ-complete), or
* a PMSL form where some Δ/∇/Θ/... rule applies, unless blocked by a Ψ policy (in which case the runtime halts legally).

---

# **9.3.9 Example: Fully Typed Fragment**

Consider:

```pmsl
module M {
    policy SafeFS;
    fn write_home(path: String, data: String) {
        let p = path;
        var f = open(p);   // requires Ω(FS.write)
        write(f, data);    // ∇ on FS
    }
}
```

Typing:

1. Module frame:

   ```
   □ : ModuleFrame
   Ψ(SafeFS)
   ```
2. Function frame:

   ```
   □ : LexicalFrame
   R : UserRole with capability FS.write
   ```
3. `open`:
   Requires Ψ(SafeFS) satisfaction → path ∈ /home.
4. `write`:
   Requires ∇ permission under RoleType.

Thus type-checking ensures:

* no ∇ outside allowed directories
* no write without capability
* frame boundaries respected

All ensured structurally by the type system.

---

# **9.3.10 Summary**

PMSL’s type system is:

* **Frame-centric (□)**
* **Role-capability-centric (Ω)**
* **Policy-centric (Ψ)**
* **Process/Isolation-centric (Χ)**
* **Operator-validity-centric (Δ…Ψ)**

It ensures that *all* programs translate into PMS operator sequences that are:

* structurally valid,
* privilege-correct,
* policy-compliant,
* context-consistent.

---

# **9.4 Concurrency & IPC in PMSL**

*(Δ–Ψ–structured concurrency, process calculus, message semantics)*

PMSL concurrency is **not bolted on** — it is the *direct programming-level projection* of the PMS concurrency substrate defined in:

* PMS-CPU: isolation (Χ), time/order (Θ), non-events (Λ), traps (Φ)
* Kernel: process model, scheduling (Θ), IPC semantics (5.x)
* Type system: process types (Χ), roles (Ω), policies (Ψ)

In PMSL, **concurrent constructs expand into operator-valid sequences** that preserve all these invariants.

This section defines:

1. **Concurrency Model**
2. **Thread / Process Creation (Χ + Θ)**
3. **Synchronization Constructs (Ω/Θ/Σ)**
4. **Message Passing Primitives (Δ, Ω, Λ, Θ, Φ)**
5. **Channel Types & Protocol Enforcement**
6. **Dispatch & Event Handling**

---

# **9.4.1 Concurrency Model — Actors + Structured Threads**

PMSL supports **two complementary concurrency layers**:

### **A. Structured Threads (χ-local execution loci)**

A thread is **a fresh execution locus** obtained via Χ:

```
spawn { expr }
```

Expands to:

```
Χ_fork(ctx)
Θ_start(ctx)
evaluate(expr in ctx)
```

Thread types are governed by **ProcessType** (9.3), which determines:

* permitted syscalls
* isolation level
* scheduler class
* allowed IPC patterns

### **B. Actor-Like Message Endpoints (Δ-typed channels)**

Actors are simply *objects with attached message queues* (5.1), typed as:

```
actor A : Channel[T] { ... }
```

Messages follow **PMS structural semantics**:

* Δ classifies message kind
* Ω checks sender’s role/capability
* Λ covers timeouts / absence
* Θ orders events
* Φ handles error paths / recontextualization
* Σ integrates message into recipient state

The PMS actor model is therefore **a strict subset of PMSL concurrency**, not a separate paradigm.

---

# **9.4.2 Thread / Process Creation (Χ + Θ)**

### **Syntax**

```
let tid = spawn expr;
```

### **Typing**

If:

```
Γ ⊢ expr : T   under ProcessType P_child
```

and parent process has permission to spawn P_child (Ω + Ψ),
then:

```
Γ ⊢ spawn expr : ThreadId
```

### **Operator Expansion**

```
Χ_fork(P_child)          ; create isolated frame + role + namespace
Θ_init(P_child)          ; establish temporal anchor for scheduler
Δ_thread_id              ; distinguish ID
∇_enqueue_run(expr)      ; schedule work
```

The new thread enters the kernel run queue via Θ.

### **Join / Await**

```
join tid
```

Expands to:

```
WAIT until (Θ_event for tid.status == finished)
Λ if timeout
Σ integrate tid result
```

---

# **9.4.3 Synchronization Constructs (Ω/Θ/Σ)**

PMSL offers high-level synchronization, all compiled to PMS operators.

## **Mutexes (Ω + Θ)**

```
mutex m;

m.lock();
m.unlock();
```

Expand to:

```
Ω_acquire(m.cap)         ; capability check
Θ_wait_queue(m)          ; scheduler-ordered wait
Λ (timeout) optional
Σ_grant_lock(m)          ; commit ownership
```

Release:

```
Ω_release
Σ_unlock
Θ_notify(waiters)
```

## **Semaphores**

```
sem.wait();
sem.post();
```

Expand into:

```
Δ(count)                 ; test
Θ_block/unblock
Σ_update count
```

## **Condition variables**

```
cond.wait(m);
cond.notify();
```

Map to kernel event queues:

```
Θ_sleep
Λ timeout
Φ wake (recontextualize into runnable)
```

All sync constructs respect:

* process role (Ω)
* isolation boundary (Χ)
* scheduling policy (Θ)
* policy constraints (Ψ)

---

# **9.4.4 Message Passing (Δ, Ω, Λ, Θ, Φ)**

Message passing is **first-class** in PMSL, typed through `Channel[T]` and `Mailbox[T]`.

### **Channel creation**

```
let c = channel<T>();
```

Expands to:

```
Δ(T)                     ; message type distinction
Χ_create_mailbox         ; isolated queue
Σ_register_object        ; commit channel object
```

---

## **Sending messages**

```
send c msg
```

Operator-level sequence:

1. **Δ_msg** — classify message (variant/tag/type T)
2. **Ω_check** — ensure sender has rights to post to `c`
3. **∇_enqueue** — insert message into mailbox
4. **Θ_signal** — notify receiver
5. **Σ_post** — finalize enqueue

Error paths:

* **Λ_timeout** if channel is full (bounded channels)
* **Φ_reframe** if message is incompatible with receiver policy or type

---

## **Receiving**

```
let m = recv c;
```

Operator expansion:

1. **Θ_wait** — wait for message arrival
2. **Λ_no_event** — handle timeout or non-blocking failure
3. **Δ_unwrap** — decode message tag
4. **Σ_dequeue** — commit removal from mailbox

This is a structural dual of send.

---

# **9.4.5 Channel Types & Protocol Enforcement**

Channels may include **protocol specifications** (PPS, section 7.3):

```
channel<P_REQ or P_EVT or P_CTRL>
```

PMSL treats protocol types as **Σ-integrated state machines**, where each send/recv must conform to allowed transitions:

```
StateMachineType Protocol :=
    { states, transitions : Δ × Σ × Θ → state }
```

Type-checking ensures:

* illegal message sequences = compilation error
* incomplete handling = warning or error
* missing timeout handling = policy violation under Ψ

Higher-level syntax:

```
protocol MyProto {
    state Init {
        on Req -> Waiting;
    }
    state Waiting {
        on Resp -> Done;
        on Timeout -> Init;
    }
}
```

PMSL will expand this into Δ/Θ/Λ/Σ operators rigorously.

---

# **9.4.6 Events & Dispatch (Φ + Θ)**

PMSL programs may define event handlers:

```
on event X from source Y { ... }
```

Compilation:

1. **Δ_event** — classify incoming event
2. **Ω_check_source** — ensure handler has authority
3. **Φ_enter_handler** — switch into handler frame/context
4. **Θ_order** — record event timestamp/order
5. **∇_exec** — perform handler code
6. **Σ_exit_handler** — commit state changes

Event loops:

```
loop {
    wait event e;
    handle e;
}
```

Expands to:

```
Θ_cycle  
Λ no-event  
Δ classify  
Φ dispatch  
Σ integrate  
```

This forms the core of actor-style reactive programs.

---

# **9.4.7 Structured Concurrency (Α patterns + Θ sequences)**

PMSL supports structured concurrency patterns:

```
async let x = f1();
async let y = f2();
await x + y;
```

Pattern Α-expand into:

```
Χ_spawn f1
Χ_spawn f2
Θ_schedule
WAIT both finished
Σ_join results
```

All expansions remain PMS-valid sequences.

---

# **9.4.8 Summary**

PMSL concurrency is **structurally guaranteed** by PMS operators:

| PMS Operator | Concurrency Role                               |
| ------------ | ---------------------------------------------- |
| Δ            | message/type distinction, event classification |
| ∇            | enqueue/dequeue, state updates                 |
| □            | per-thread frame contexts                      |
| Λ            | timeouts, non-blocking receive                 |
| Α            | structured concurrency patterns                |
| Ω            | capability checks for send/recv/spawn          |
| Θ            | scheduling, ordering, blocking/wake-up         |
| Φ            | traps, exceptions, event dispatch              |
| Χ            | thread/process creation & isolation            |
| Σ            | integration (message commit, join)             |
| Ψ            | safety policies governing IPC & concurrency    |

PMSL concurrency is thus **formally grounded**, not ad-hoc.

---

# **9.5 Error & Exception Handling (Φ / Λ)**

*(Recontextualization & Non-Event Semantics in PMSL)*

PMSL error handling is not an afterthought layered atop the runtime — it is a **direct projection of the PMS Φ/Λ operator semantics**:

* **Φ — Recontextualization:**
  errors trigger *context shifts*, handler entry, fallback frames, ABI/role changes, or recovery paths.

* **Λ — Non-Event:**
  missing results, timeouts, absent responses, & cancelled waits are *first-class semantic events*, not special return codes.

This enables a fully structural error model, suitable for OS kernels, distributed protocols, actors, and transactional subsystems.

---

# **9.5.1 Error Value vs. Error Context (Δ / Φ)**

PMSL distinguishes two categories:

### **A. Value-Level Errors (Δ)**

Errors that behave like *ordinary values*, e.g.:

```
let result = try f(x);
```

If `f(x)` returns `Err e`, PMSL interprets it via:

* **Δ_e** — classify error variant
* **branch** into local handler or propagate

These use Δ only; no context shift occurs yet.

### **B. Context-Level Errors (Φ)**

Errors that **modify the execution context**:

* exceptions
* traps
* ABI reframe
* policy violations
* type mismatch requiring migration
* privilege switch errors

These are true Φ-operations: `Φ_raise`, `Φ_enter_handler`, `Φ_restore`.

Thus PMSL supports:

* **recoverable value errors (Δ)**
* **context errors (Φ)**
  with clean separation.

---

# **9.5.2 Exception Syntax**

### **Raising exceptions**

```
raise err;
```

Expands to:

```
Δ(err)                 ; classify error
Φ_raise(err)          ; shift context
Θ_branch(handler)     ; schedule handler entry
```

### **Handling exceptions**

```
try {
    expr
} catch (E1 e) {
    handler1
} catch (E2 e) {
    handler2
}
```

Expands to:

1. Push handler table into meta-state (`Φ_set_handler_table`).
2. Evaluate `expr`.
3. If Φ occurs, use Δ to dispatch based on error type.
4. Jump into handler frame.

---

# **9.5.3 Exception Type System**

Errors are typed via PMSL’s sum types:

```
type IOError =
    | NotFound
    | Permission
    | Timeout
    | DeviceFault(code)

type Result<T> =
    | Ok T
    | Err IOError
```

**Type rules:**

If `expr : Result<T>`, then:

```
try expr : T
```

provided *all* error variants are handled or declared.

This is enforced via **Δ completeness checking**:

* Unhandled variants → compile error.
* Conditional handler missing fallback → warning or Ψ policy error.

---

# **9.5.4 Recontextualization Semantics (Φ)**

Errors that cannot be treated as local values initiate **Φ-recontextualization**:

### Examples of Φ paths:

1. **Privilege escalation errors**
   → fallback into kernel handler frame

2. **ABI mismatch**
   → shift to compatibility frame (Φ_reframe ABI_v1 → ABI_v2)

3. **Isolation boundary violation**
   → Φ_trap into sandbox supervisor

4. **Process-level faults**
   → Φ_kill or Φ_restart under policy Ψ

### Formal expansion:

```
Φ_enter_handler(ctx)
□_switch_frame(handler_frame)
Ω_set_role(handler_role)
Θ_mark_handler_entry
```

Handler execution is just evaluation inside **handler frame** until:

* **Φ_restore** returns to caller context, or
* **Σ_commit** finalizes a recovery transformation.

---

# **9.5.5 Non-Event Semantics (Λ)**

Λ captures **absence** rather than malfunction:

```
let msg = recv c timeout 100ms;
```

Expansion:

1. Θ_wait(c, deadline)
2. If message arrives → Δ_classify → Σ_dequeue
3. If not → **Λ_timeout(c)**

Λ values can be:

```
None
Timeout
Cancelled
Empty
```

Λ handlers are allowed:

```
on timeout { ... }
```

Λ never mutates core state; it updates only:

* meta-state (`m.timeout_count += 1`)
* control flow (`branch label`)

---

# **9.5.6 Combined Error Model: Δ + Λ + Φ**

PMSL integrates all error modes:

### **Δ-value error**

*Local branching*
Use for ordinary recoverable failures (parsing, file-not-found, etc.).

### **Λ non-event**

*Absence of expected event*
Networking, IPC, scheduling, I/O, timers.

### **Φ context error**

*Structural reframe*
Exceptions, traps, policy enforcement, ABI shifts.

A PMSL function can declare which modes it uses:

```
fn f(x:Int) throws (E_IO, E_Parse) yields ΛTimeout -> Int
```

Meaning:

* may raise Φ exceptions of types `E_IO`, `E_Parse`
* may return Λ-timeout as a valid value
* otherwise returns an Int

This integrates directly with the type system (9.3).

---

# **9.5.7 Try/Else/Finally (Σ integration)**

PMSL supports structured cleanup via Σ:

```
try {
    expr
} else {
    alternative
} finally {
    cleanup
}
```

Operator expansion:

1. Try-block
2. On error → Φ_enter_handler
3. Else-block (only if no Φ/Δ-error taken)
4. Finally-block is **Σ_final**:

```
Σ_enter_cleanup
evaluate cleanup
Σ_exit_cleanup
```

Σ ensures cleanup effects are **committed** even in presence of Φ/Λ.

---

# **9.5.8 Default Runtime Handlers (Ψ policies)**

Policies can require:

* **catch-all** handlers
* mandatory timeout handling
* restricted exception types
* recovery or restart decisions

Example Ψ rule:

```
Ψ: every process must handle Timeout or be terminated.
```

Runtime check:

```
CHK_POL TimeoutHandling
Φ_trap_unhandled if violated
```

Another example:

```
Ψ: forbids raw exception rethrow across isolation boundary.
```

Φ_enforcement:

```
if boundary_violation:
    Φ_redirect to boundary handler
```

---

# **9.5.9 Exception Handling & IPC**

Cross-process exceptions propagate as **structured messages**:

```
raise RemoteFault("device failed")
```

is encoded as:

* send P-EVT fault packet
* remote Φ_enter_handler
* optional return value (Σ)

Timeouts (Λ) also propagate as structural events.

---

# **9.5.10 Summary Table**

| PMS Operator | Error-Model Role                      |
| ------------ | ------------------------------------- |
| **Δ**        | classify error value; local branching |
| **Λ**        | non-event (timeout, missing input)    |
| **Φ**        | exception, trap, context shift        |
| **Ω**        | check authority for handlers          |
| **Θ**        | control wait/timeout sequencing       |
| **Χ**        | per-thread handler contexts           |
| **Σ**        | cleanup, commit recovery              |
| **Ψ**        | global error-handling policies        |

PMSL’s error system is therefore **structurally complete**, guaranteed to be consistent with the universal PMS semantics.

---

# **9.6 Module System (modules as frames + roles + policies)**

*(PMSL structural modularity via □, Ω, Ψ, Χ, Σ)*

In PMSL, a **module** is not merely a namespace—it is a **PMS-structured computational region**, defined as a *triple*:

```
Module = (Frame, RoleSet, PolicySet)
```

This directly reflects PMS operator semantics:

* **□ — Frame**
  A module *is* a frame: a context with its own symbol table, memory region, type environment, and import/export scope.

* **Ω — Roles / Capabilities**
  Each module is executed under a *module-role*, defining what its code may access or do.

* **Ψ — Policies / Invariants**
  Each module can declare invariants enforced on all code inside the module frame.

* **Χ — Isolation**
  Modules may run in isolated subcontexts (e.g., separate processes, sandboxes, capsules).

* **Σ — Integration**
  Module linking, finalization, interface commitments.

This gives PMSL modularity a **rigorous praxeological foundation**—modules are embedded directly into the operator algebra.

---

# **9.6.1 Module Declaration Syntax**

### **Basic form**

```
module M {
    export fn f(x:Int) -> Int { ... }
    let internal_data = ...
    import N { g }
}
```

Semantically expands to:

```
□_enter(M.frame)
Ω_set_role(M.role)
Ψ_activate(M.policies)
Σ_register_exports
```

### **Extended form with explicit structural constraints**

```
module M : ModuleType {
    requires role UserSpace;
    requires policy SafeFS;

    provides interface I {
        fn f(x:Int) -> Int;
    }
}
```

All of these clauses resolve to Ω- and Ψ-instructions at compile time and to frame-changing □-instructions at runtime.

---

# **9.6.2 Modules as Frames (□)**

Every module defines a **lexical and execution frame**:

```
M.frame = {
    symbols: {types, functions, values},
    memory_region: {base, size},
    imports: set of (module, symbols),
    exports: set of symbols,
}
```

Entering module scope during evaluation is:

```
□_switch_frame(M.frame)
```

This provides:

* symbol resolution
* address space for module-local data
* scoping of capabilities and policies

Nested modules create a **frame stack** encoded in meta-state m.

---

# **9.6.3 Role Assignment to Modules (Ω)**

Each module has an assigned **role**:

```
M.role : Role
```

Common examples:

* `UserSpace`
* `KernelSpace`
* `Driver`
* `TrustedModule`
* `SandboxedModule`
* `NetProtocolModule`

Role semantics:

* determine which PMSL constructs can be used
* control access to system calls
* allow or forbid memory operations
* govern imports/exports
* enforce least-privilege by default

Entering a module applies:

```
Ω_set_role(M.role)
```

The type checker ensures:

* exported symbols obey role constraints
* imported modules’ roles are compatible
* callers meet required role expectations

---

# **9.6.4 Module Policies (Ψ)**

Modules attach **policies** that constrain internal operations:

```
M.policies : PolicySet
```

Policies can specify:

### **Safety constraints**

* memory safety rules
* forbidden syscalls
* required handler coverage
* invariants over stored data

### **Security requirements**

* encryption required on channels
* all exports must be capability-checked
* only certain roles may call module functions

### **Lifecycle invariants**

* module requires Σ-finalization of state
* module must not leak resources
* version compatibility constraints

Entering module:

```
Ψ_apply(M.policies)
```

Violations cause Φ-traps or forced halts (Ψ_enforce).

---

# **9.6.5 Module Isolation (Χ)**

Modules may be declared **isolated**, spawning subcontexts:

```
module M isolated { ... }
```

This expands to:

```
Χ_enter_isolation(M.ctx)
□_switch_frame(M.frame)
Ω_set_role(M.role)
Ψ_apply(M.policies)
```

Isolation properties:

* no direct pointer sharing
* IPC-only communication
* controlled resource access
* can run in separate processes or sandboxes
* can enforce deterministic execution

Cross-isolation calls require message passing or capability tokens.

---

# **9.6.6 Module Linking & Import/Export (Δ + Σ)**

### **Import resolution (compile-time)**

```
import N { a, b, c }
```

Compile-time process:

1. **Δ_resolve(N)** – distinguish module identity
2. verify exported symbols
3. check role & policy compatibility
4. generate integration thunk

### **Export registration (runtime commit)**

When module is loaded:

```
Σ_register_exports(M.exports)
```

This operation finalizes:

* symbol table consistency
* type signatures
* role/policy annotations
* version bindings

### **Dynamic linking (Φ + Σ)**

If module loading occurs at runtime:

```
load_module("NetStack")
```

Expands to:

```
Φ_load_frame
Ω_check_privilege
Ψ_apply_policies
Σ_link_exports
```

Errors (bad ABI, incompatible policy, version mismatch) cause **Φ_reframe**.

---

# **9.6.7 Module Versioning & Reframing (Φ)**

Version changes are performed via Φ:

```
reframe M to Version2
```

Equivalent to:

```
Φ_recontextualize(M.old_frame → M.new_frame)
Ψ_reverify_policies
```

Used for:

* live upgrades
* compatibility layers
* ABI migrations
* hot-swapping subsystems

Φ ensures backward-compatibility logic is explicit and typed.

---

# **9.6.8 Module Capabilities (Ω)**

Modules may require or define **capabilities**:

```
module FS {
    capability write_file;
}
```

Callers must hold the capability:

```
require cap write_file;
```

At call time:

```
Ω_check(cap)
Δ_branch if unauthorized
```

Capabilities may be:

* value-level tokens
* structural module properties
* policy-enforced invariants

---

# **9.6.9 Module Lifecycle (Θ + Σ)**

Each module has a lifecycle aligned with PMS temporal/integration operators:

### **Initialization**

```
Θ_on_load
Σ_commit_init_state
```

### **Active state**

Operations run under module’s frame, role, policy.

### **Finalization**

```
Θ_before_unload
Σ_finalize_resources
```

### **Optional persistence**

Some modules maintain persistent state committed via Σ:

```
Σ_persist(module_state)
```

This is used in:

* storage subsystems
* network protocols
* configuration modules

---

# **9.6.10 Types of Modules**

We classify modules by structural composition (not by purpose):

| Module Type              | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| **Pure Module**          | Only □, Δ, ∇ ops; no IO, no roles.                   |
| **Isolated Module**      | Uses Χ; boundaries enforced.                         |
| **Privileged Module**    | Ω grants extended syscalls; must satisfy Ψ policies. |
| **Protocol Module**      | Exports PPS-typed channels (7.3).                    |
| **Transactional Module** | Uses Σ heavily; supports atomic state.               |
| **Reframe Module**       | Provides Φ-based version shifts.                     |
| **Resource Module**      | Manages memory, storage, IPC objects.                |

These are *not* semantic categories—they express **operator-level structure**.

---

# **9.6.11 Module-to-Module Interaction via IPC**

A module call across isolation boundaries becomes:

```
send M_inbox Request(params)
recv response
```

With structural decomposition:

1. **Δ classify request**
2. **Ω check caller capability**
3. **Χ enforce boundary**
4. **Φ dispatch into callee frame**
5. **∇ execute**
6. **Σ return**

This reproduces safe cross-module interaction automatically.

---

# **9.6.12 Summary**

PMSL modules are not files or namespaces—they are **structured PMS entities**, combining:

| PMS Operator | Module Semantics                                |
| ------------ | ----------------------------------------------- |
| **□**        | module frame, lexical & execution context       |
| **Ω**        | module role, capability requirements            |
| **Ψ**        | policy constraints & invariants                 |
| **Χ**        | isolation of module context                     |
| **Φ**        | dynamic loading, reframing, error handling      |
| **Σ**        | linking, export commit, init/finalize           |
| **Θ**        | lifecycle timing, load/unload hooks             |
| **Δ**        | symbol resolution, import/export classification |

This yields a modular system that is:

* **safe by construction** (Ψ + Ω + Χ)
* **explicitly structured** (□ frames)
* **dynamically adaptable** (Φ reframing)
* **transactionally consistent** (Σ)

PMSL modules are therefore the *canonical unit of composition* in the PMS architecture.

---

# **9.7 FFI / Interoperability (calls into non-PMS code / host OS)**

*(Structured external interoperability via Ω, □, Φ, Χ, Ψ)*

The PMS architecture treats interoperability not as an escape hatch but as a **first-class operator-typed mechanism**.
FFI is modeled as controlled entry into **foreign frames** with explicit:

* **□** — frame switching into foreign environments
* **Ω** — capability gating for safety
* **Φ** — recontextualization across ABI, type, and semantic boundaries
* **Χ** — isolation between PMS memory and foreign memory
* **Σ** — integration of returned values
* **Ψ** — policies constraining which foreign calls are allowed

This makes FFI a **formal subsystem**, not an ad-hoc feature.

---

# **9.7.1 Foreign Frame Model (□_foreign)**

Any external environment is treated as a **frame**:

```
ForeignFrame {
    abi_type: C | POSIX | WASI | JVM | custom
    call_gate: entry point
    memory_access: allowed / isolated / shared
    calling_convention: specification
}
```

Switching into a foreign context is done via an explicit operator:

```
□_enter(ForeignFrame)
```

This corresponds to:

* establishing ABI conventions,
* switching register/stack discipline (PMS-CPU),
* aligning type encodings.

Returning from the FFI call is:

```
□_exit(ForeignFrame)
```

Foreign frames are therefore **typed contexts**, not arbitrary jumps into native code.

---

# **9.7.2 FFI Call Semantics in PMSL**

General PMSL syntax:

```
foreign fn c_sin(x:Float) -> Float;
...
let y = c_sin(1.0);
```

Expands to the operator-level sequence:

1. **Δ** — resolve foreign symbol
2. **Ω_check** — verify FFI capability
3. **Χ_isolate** — isolate PMS memory region if required
4. **Φ_reframe** — convert PMS types → foreign ABI types
5. **□_enter** — switch to foreign frame
6. **∇_call** — perform actual native call
7. **Σ_integrate** — convert result back into PMS form
8. **□_exit** — return to PMS frame

This makes FFI part of the *normal operational algebra* of PMS interpretation.

---

# **9.7.3 Capability Gating (Ω)**

Foreign interaction is *never* allowed by default.
Modules must declare capabilities:

```
requires capability FFI_Calls;
requires capability HostFS;
```

At call time:

```
Ω_check(FFI_Calls)
```

If the role lacks the capability:

```
Δ ⇒ unauthorized
Ψ_enforce ⇒ deny or trap
```

This protects:

* kernel-level transitions
* system resources
* unsafe pointer operations
* filesystem/network access through foreign code

Ω turns FFI into an auditably safe boundary.

---

# **9.7.4 Memory Interaction & Isolation (Χ)**

Because foreign code may expect raw pointers, the PMS runtime mediates memory access through **isolation boundaries**.

### Three modes:

#### **(a) Fully Isolated**

PMS object graph is translated into foreign memory buffers:

```
Χ_copy_to_foreign
∇_call
Χ_copy_to_pms
```

Used for:

* C library calls
* host OS syscalls
* WASI modules
* safe default mode

#### **(b) Shared but Restricted**

Only explicitly marked buffers are shared:

```
buffer shared(pms_buf) with foreign
```

Χ ensures:

* no foreign code can access unshared regions
* linear or borrow-style aliasing rules can be enforced

#### **(c) Unsafe Raw Access (needs Ω_superuser)**

Available only to privileged modules:

```
unsafe foreign fn do_raw(ptr: *mut u8);
```

Requires:

```
Ω_check(SuperFFI)
Ψ_enforce(strict auditing)
```

This prevents accidental system compromise.

---

# **9.7.5 Foreign ABI Reframing (Φ)**

Crossing a language or OS boundary is always a **recontextualization event**:

```
Φ(PMS_type → ABI_type)
Φ(exception_model → error_code_model)
Φ(memory_model → foreign_allocation_model)
```

Examples:

* PMS `Int` → C `int64_t`
* PMS exceptions → errno or return codes
* PMS structured errors → POSIX error types
* PMS-owned memory → malloc’ed buffers

Likewise on return:

```
Φ(ABI_results → PMS_values)
```

If something fails during reframing:

```
Φ_recover
Ψ_policy_enforce
```

Example: invalid encoding, truncated string, mismatched layout → converted into PMS exception with Φ.

---

# **9.7.6 Foreign Error Handling (Λ, Φ)**

Foreign calls can produce **non-events** (Λ) or errors requiring reframing (Φ).

### **Λ: Non-Event in FFI**

Examples:

* a non-blocking POSIX read returns EAGAIN
* a socket call returns “no data yet”
* optional pointer returns NULL

Runtime treats this as:

```
Λ_foreign_non_event
Δ classify
branch -> fallback / retry / await
```

### **Φ: Foreign Exception or Error**

Errors are reframed into PMS exception structures:

```
Φ_map_errno
Φ_map_java_exception
Φ_map_wasm_trap
```

Then raised in PMSL’s error model (9.5).

---

# **9.7.7 Asynchronous Foreign Calls (Θ + Δ + Λ)**

Asynchronous host operations (I/O, timers, futures, GPU calls) integrate naturally:

1. **Submit request**
2. Θ schedules continuation
3. Λ signals timeout or no-event
4. Φ reframe completion or errors
5. Σ commit result

PMSL syntax:

```
let r = await foreign async read(fd, buf);
```

Desugars into:

```
∇ submit_request
Θ schedule
Λ or Φ depending on readiness
Σ integrate result
```

---

# **9.7.8 Host OS Interoperability Layer**

The host OS is modeled as a **super-frame**:

```
HostFrame {
    abi: POSIX | NT | WASI | native,
    capabilities: {open, read, write, ioctl, mmap, ...},
    policies: host-defined constraints
}
```

Syscalls in PMSL are just FFI calls to this frame:

```
foreign sys open(path:String, flags:Int) -> FD;
```

Enforced by:

* Ω_host_role
* Ψ_host_policy
* Χ isolation (esp. for mmap)
* Φ conversion of errno
* Σ commit as PMSL file handle

This makes “syscalls” structurally identical to any FFI call—just more privileged.

---

# **9.7.9 PMSL → Native Code Calling Convention**

The compiler generates a well-defined calling wrapper:

```
call_wrapper(M.frame, target_symbol, args...) = {
    □_enter(ForeignFrame)
    Ω_check
    Χ_setup_buffers
    Φ_prepare_abi
    ∇ call target_symbol
    Φ_wrap_return
    Σ_commit
    □_exit(ForeignFrame)
}
```

The wrapper ensures:

* no raw escape of PMS pointers
* all cross-boundary semantics are explicit
* policies are verified
* lifetimes and cleanup occur correctly

---

# **9.7.10 Example: Calling a C Function**

### PMSL code:

```
foreign fn strlen(s: &Byte) -> Int;

fn demo() {
    let buf = "hello".as_bytes();
    let n = strlen(buf);
}
```

### Operator-level expansion:

```
Δ_resolve(strlen)
Ω_check(FFI_Calls)
Χ_share(buf)
Φ_encode_pointer
□_enter(C_ABI)
∇_call(strlen)
Φ_decode_int
Σ_integrate_result
□_exit
```

Everything is explicit and enforced by the operator constraints.

---

# **9.7.11 Example: Calling Host Filesystem API**

```
foreign sys read(fd:FD, buf:&mut Byte, n:Int) -> Int;
```

Call sequence:

1. Δ resolve `read`
2. Ω check `HostFS_Read` capability
3. Χ share/mmap or isolate buffer
4. Φ convert parameters to host layout
5. □ enter HostFrame
6. ∇ perform syscall
7. Λ or Φ handle errno/timeouts
8. Σ finalize buffer state
9. □ exit

---

# **9.7.12 Summary**

PMSL FFI is a structured combination of PMS operators:

| PMS Operator | FFI Meaning                                     |
| ------------ | ----------------------------------------------- |
| **□**        | Switch into foreign ABI frame                   |
| **Ω**        | Verify capability for external call             |
| **Φ**        | Reframe values/types/exceptions                 |
| **Χ**        | Enforce isolation & safe memory sharing         |
| **Δ**        | Symbol and ABI distinction                      |
| **∇**        | Perform the actual native call                  |
| **Λ**        | Handle no-event/partial readiness               |
| **Σ**        | Commit results back into PMSL                   |
| **Ψ**        | Apply/ enforce policies on external interaction |

This yields an interoperability system that is:

* **safe by construction**
* **fully typed**
* **auditable and policy-controlled**
* **compatible with arbitrary host OS or runtime**
* **semantically uniform with the rest of PMS**

---

### 10. PMSL Runtime & Standard Library

## 10.1 Runtime Architecture (PMSL → PMS-CPU + syscalls)

The PMSL runtime is the **bridge** from high-level PMSL code to the PMS-CPU + PMS-OS world:

* It **compiles and loads** PMSL modules into PMS-CPU code (Δ → opcodes).
* It **manages process state**: heaps, stacks, module frames, tasks.
* It **mediates** all interaction with the kernel via **syscalls** (Φ + Ω + Χ).
* It **enforces language-level invariants** as Ψ on top of the kernel’s Ψ.

We describe:

1. Runtime layering (PMSL → IR → PMS-CPU → syscalls)
2. PMSL process model vs kernel processes
3. Call/return and syscall paths
4. Memory layout and frame usage
5. Concurrency & event integration
6. Policy and safety integration

---

### 10.1.1 Layering & Components

Conceptual stack for a single PMSL program:

```text
+------------------------------------+
| PMSL Program (modules, types, etc) |
+------------------------------------+
| PMSL Runtime:                      |
|  - Loader & Linker                 |
|  - Scheduler shim                  |
|  - Heap/GC & Handle tables         |
|  - Exception & signal dispatcher   |
|  - Syscall wrapper layer           |
+------------------------------------+
| PMSL IR (Δ–Ψ-tagged)               |
+------------------------------------+
| PMS-CPU ISA (Δ, ∇, □, Ω, Θ, Φ, …)  |
+------------------------------------+
| PMS-OS Kernel (processes, IPC, FS) |
+------------------------------------+
| Hardware / PMS-CPU implementation  |
+------------------------------------+
```

Operator view:

* **Δ** – IR typing, function/module IDs, syscall numbers, handle kinds
* **∇** – execution of compiled code, heap alloc/free, field updates
* **□** – module frames, activation frames, heap regions, address spaces
* **Λ** – timeouts, failed I/O, empty channels, missing events
* **Α** – runtime patterns: call sequences, common IPC flows, retry loops
* **Ω** – language roles: untrusted vs trusted module, capability-scoped APIs
* **Θ** – task scheduling hooks, timers, cooperative yields
* **Φ** – exception delivery, domain boundary moves (host FFI, kernel boundary)
* **Χ** – module isolation, sandboxed runtimes, per-tenant heaps
* **Σ** – transaction-like scopes, commit of buffered I/O, GC phases
* **Ψ** – language invariants: type safety, ownership, API contracts

---

### 10.1.2 PMSL Process Model vs Kernel Processes

At the kernel layer (section 3):

* A **PProcess** is the kernel’s unit of isolation & accounting.
* It may have multiple kernel threads (KThreads), scheduled by Θ.

The PMSL runtime runs *inside* a PProcess and defines its own lighter-weight units:

* **Runtime process** (RProc) – usually 1:1 with PProcess

  * Has a **root module frame** and **global heap**
* **Runtime threads / tasks** (RThread / Task)

  * Map to:

    * either dedicated kernel threads (1:1 or N:M),
    * or cooperative tasks multiplexed over a smaller kernel thread pool.

Mapping:

* Each RThread has:

  * **call stack** (□ activation frames)
  * **task-local context** (roles, policies, handles)
  * **scheduler metadata** (Θ: run state, priority, deadlines)

* Each RProc corresponds to:

  * one PMS-OS process with a **virtual address space** (□),
  * one or more KThreads.

This mirrors the PMS operator picture:

* OS-level Χ/□ gives the **outer isolation**
* Runtime-level □/Χ gives **intra-process structure** (modules, tasks, actors).

---

### 10.1.3 Compilation & Execution Path (PMSL → PMS-CPU)

**Compile-time pipeline (tooling + runtime loader):**

1. PMSL source → **PMSL AST** (Δ distinctions of syntax/types)
2. AST → **PMSL IR** (section 11.1):

   * operator-tagged constructs (Δ..Ψ)
   * explicit control flow, frames, roles, policies
3. IR → **PMS-CPU ISA**:

   * function bodies compiled into ISA functions
   * call sites implemented via CALL/RET conventions (2.3)
   * syscalls inserted for kernel services (3.7)
4. Linker resolves:

   * intra-module and inter-module references
   * runtime entry points (main, init hooks)
5. Loader:

   * allocates code/data frames in the process address space
   * sets up **initial module frames** (□)
   * builds the **Runtime context** (RProc, main RThread)

**Execution:**

* Kernel launches the process (PProcess) via **exec**-style syscalls.
* PMS-CPU starts at runtime entry stub:

  * sets up initial stack frame
  * initializes runtime (heap, handle tables, sched structures)
  * calls PMSL program’s `main`/entry as a normal function.

From that point:

* PMSL code runs on PMS-CPU,
* runtime intervenes only via:

  * library calls,
  * trap/syscall wrappers,
  * exception handling,
  * GC / housekeeping.

---

### 10.1.4 Call, Syscall, and FFI Paths

#### PMSL function call

At PMSL level:

```pmsl
fn f(x: Int, y: Int) -> Int { x + y }
```

Compilation:

* **Δ** – type & function distinction
* **∇** – body compiled to arithmetic ∇ + branches
* **□** – new activation frame on stack at call
* **Σ** – implicit at return (return value commit + frame restoration)

ISA sequence (simplified):

```asm
; caller
MOV   R0, arg_x     ; ∇
MOV   R1, arg_y     ; ∇
CALL  f_label       ; ∇
; result in R0

; callee prolog
PUSH  R4..R7        ; ∇
SUBI  SP, SP, frame_size  ; ∇
; body ...
ADDI  SP, SP, frame_size  ; ∇
POP   R7..R4        ; ∇
RET                 ; ∇ (Σ-flavored)
```

#### Syscall path (PMSL → kernel)

PMSL exposes safe APIs like:

```pmsl
fn write(fd: File, buf: &Bytes) -> Result<Int, IoError>
```

Runtime implementation:

1. Type-safe wrapper checks:

   * **Ψ** invariants: valid `fd`, accessible buffer, capabilities (Ω)
2. Packs raw syscall arguments into registers:

   * `R0 = syscall_number(WRITE)`
   * `R1..R3 = fd, buf_ptr, len`
3. Executes `TRAP #0` (Φ) to enter kernel (3.7).
4. Kernel executes, returns via EXC_RET (Φ).
5. Runtime maps result codes back to:

   * `Ok(n)` or `Err(IoError)`.

Operator view:

* Language call site: Δ + ∇ + □ + Σ
* Boundary crossing: Φ + Ω + Χ + Ψ
* Error mapping: Φ (recontextualization of kernel error to language exception/Result).

#### FFI path (to host libraries)

FFI functions are **special frames**:

* Declared in PMSL with `extern`-like syntax.
* Bound at load-time to:

  * host OS functions,
  * or dynamically loaded libraries.

Runtime:

* Enforces Ψ constraints around FFI:

  * type checks,
  * isolation rules (Χ),
  * capability checks (Ω).
* Uses **host-specific calling convention**, but always through a Φ-like reframe:

  * “We reinterpret this call as foreign, and trust the host to obey its own Ψ.”

---

### 10.1.5 Memory Layout & Frames in the Runtime

Inside a PMSL process:

* **Address space** (□, courtesy of kernel):

  * Code frames (modules, runtime)
  * Data frames (globals, literals)
  * Heap frames (allocation arenas)
  * Stack frames (per RThread)
  * MMIO / special kernel-mapped regions

Runtime adds **logical frames** on top:

1. **Module frames (□)**

   * Each module M has a frame:

     * constants
     * static data
     * imports/exports
   * PMSL module system (9.6) maps directly here.

2. **Activation frames (□)**

   * On each call, runtime creates a stack frame:

     * locals
     * saved registers
     * links to module frame

3. **Heap regions**

   * May be:

     * a single global heap per process
     * or multiple **region frames** per module or logical subsystem.
   * GC/allocator sees them as Σ domains:

     * allocation ∇
     * collection/compaction Σ

4. **Isolation frames (Χ)**

   * For stronger guarantees:

     * per-tenant heap/frame
     * per-plugin or untrusted module sandbox
   * Kernel’s Χ (process address spaces, VM) + runtime’s Χ (heap/handle policies) combine.

Psi-level invariants:

* “Pointers never cross address-space boundaries except via FFI/special channels.”
* “Handles track which heap/frame they belong to; no cross-region free.”

---

### 10.1.6 Concurrency, Events, and the Runtime Scheduler

PMSL concurrency (9.4) exposes constructs like:

* **tasks / async functions**
* **channels** or **mailboxes**
* **timers** and **signals**

Runtime is responsible for mapping these to:

* kernel scheduler (Θ, section 3.4),
* kernel IPC (5.x),
* PMS-CPU primitives (WAIT, YIELD, TICK, FENCE, etc.).

Typical patterns:

1. **Task spawn**

   * Runtime allocates a new activation frame + task descriptor.
   * Either:

     * binds it to a kernel thread (1:1),
     * or adds to a cooperative scheduler queue (N:M).
   * Uses Θ (`YIELD`, `TICK`) to interleave tasks.

2. **Channel send/recv**

   * Channel is implemented as a **kernel mailbox** or shared buffer with Σ/Χ semantics.
   * PMSL send → runtime call → kernel IPC send.
   * PMSL recv:

     * Waits on kernel queue or internal queue.
     * Uses Λ for timeout semantics.

3. **Timers and timeouts**

   * Runtime requests kernel timers (Φ from timer IRQs).
   * PMSL `sleep`, `timeout`, `select`:

     * map to WAIT+Λ+Φ pattern.
   * Θ/time in meta-state is updated by timer interrupts and scheduler ticks.

4. **Signals / events**

   * Kernel delivers events (signals, I/O ready, etc.) to the PMSL runtime via:

     * signal handlers,
     * event queues,
     * or registered callbacks.
   * Runtime translates these into:

     * PMSL-level events (callbacks, async wakes),
     * Φ-based exception/notification mechanisms in PMSL (9.5, 5.3).

Overall:

* Kernel does **global scheduling & isolation** (Θ, Χ).
* Runtime does **intra-process scheduling & semantics** (Θ, Ψ, Α patterns).

---

### 10.1.7 Policies, Safety & Ψ Integration

There are three Ψ layers:

1. **Hardware/CPU Ψ** (2.x)

   * architectural invariants: memory permissions, etc.

2. **Kernel Ψ** (3.x, 8.x)

   * process isolation, resource limits, security policy.

3. **Runtime Ψᵣ** (language-level)

   * type safety,
   * ownership / lifetime rules,
   * API contracts and capability use.

Runtime duties:

* Enforce **Ψᵣ** before crossing boundaries:

  * before syscalls,
  * before FFI calls,
  * before sharing references/handles with other RThreads or processes.
* Maintain logs and audits (8.4):

  * annotate Σ points (commits, e.g. file flush)
  * track Θ events (scheduling/timeout history)
* Cooperate with static analysis (11.x):

  * IR retains Δ–Ψ tags,
  * runtime-inserted checks are visible and verifiable.

In effect, the PMSL runtime is a **policy-aware conductor**:

* It turns PMSL programs into well-formed PMS-CPU traces.
* It ensures that every ∇ touching the outside world goes through the appropriate Δ, Ω, Φ, Χ, Σ, Ψ gates.

---

# **10.2 Core Libraries (FS, Networking, Time, Logging, Policies)**

*(Standard Library as Δ–Ψ–structured wrappers over kernel syscalls and runtime services)*

The PMSL standard library (PMSL-Std) is not a random assortment of functions—it is a **canonically structured layer** that:

1. Wraps all kernel services via **structured syscall wrappers** (Δ + Ω + Φ + Χ + Σ)
2. Exposes high-level abstractions consistent with PMS operators
3. Enforces Ψ-level invariants that the kernel cannot enforce alone
4. Provides reusable Α-patterns for common tasks
5. Integrates tightly with the runtime’s scheduling, event, and isolation mechanisms

PMSL-Std sits above the runtime (10.1) and provides the “programmable face” of the OS.

---

# **10.2.1 Filesystem Library (FS.Std)**

*(Α patterns, Δ distinctions, Ω capability gating, Σ commits)*

The FS library mirrors the filesystem architecture (4.3) using PMSL-safe types and abstractions.

### **Core Types**

```
type Path     = String
type File     = Handle<FileDesc>
type Dir      = Handle<DirDesc>
type OpenMode = { Read, Write, Append, Create, Truncate }
type FsError  = enum { NotFound, Permission, io:IoError, invalid }
```

All handles are **opaque**, enforcing Χ isolation between PMSL-level objects and kernel file descriptors.

### **Core Functions**

#### **open(path, mode) → Result<File, FsError>**

Operator sequence:

* Δ resolve path
* Ω_check(FS_Open) — capability
* Φ encode path
* ∇ syscall.open
* Φ map errno → FsError
* Σ return handle

#### **read(file, buf, n) → Result<Int, FsError>**

* Ω_check(FS_Read)
* Χ_isolate or share buf
* ∇ syscall.read
* Λ if non-blocking & no data
* Φ error conversion
* Σ integrate new buffer length

#### **write(file, buf) → Result<Int, FsError>**

* Same structure; Σ ensures commit semantics (matches FS journaling/flush rules).

#### **flush(file) → Result<(), FsError>**

* ∇ issue kernel flush
* Σ commit

#### **list_dir(path) → Result<[DirEntry], FsError>**

Uses repeating Δ→∇→Θ sequences for directory entry walks.

#### **fsync(file)**

Maps directly to **Σ** at FS layer.

---

### **10.2.1.1 Higher-Level FS Α-patterns**

* `copy_file(src, dst)`
* `write_all(fd, buf)`
* `read_to_end(fd)`
* directory traversal patterns

All built as reusable Α constructs expanding to sequences of Δ, ∇, Θ, Λ, Φ, Σ.

---

# **10.2.2 Networking Library (Net.Std)**

*(Structured frames, timeouts via Θ/Λ, connections as □-contexts)*

Networking follows the model defined in section 7.

### **Core Types**

```
type Socket       = Handle<SocketDesc>
type Address      = { ip:IP, port:Int }
type NetError     = enum { Timeout, Reset, Closed, Permission, io:IoError }
type Endpoint     = Frame<TransportCtx>
```

Connections are modeled as **frames (□)** representing protocol state.

### **Core Functions**

#### **socket(domain, type, proto)**

Creates a new □ frame for transport state.

#### **connect(sock, addr, timeout)**

Sequence:

* Δ classify address
* Ω_check(Net_Connect)
* Θ set timeout baseline
* ∇ syscall.connect
* Λ if timeout
* Φ map host-specific connection errors
* Σ finalize connected state

#### **send(sock, buf)**

FFI/syscall boundary:

* Ω_check(Net_Send)
* Χ isolate/validate buf
* ∇ syscall.send
* Σ commit sent bytes

#### **recv(sock, n)**

Uses Λ semantics if no data is available.
Time-based blocking waits use Θ + Λ patterns.

#### **close(sock)**

Triggers Σ on connection teardown + release of frame.

---

### **10.2.2.1 Higher-Level Networking Α-patterns**

* request-response cycle (Δ → send → Θ → recv → Σ)
* retry with backoff (Α using Θ sequences)
* non-blocking event loop pattern matching (Δ on readiness flags)
* subscription-based receiving (pub-sub, 5.3)

---

# **10.2.3 Time Library (Time.Std)**

*(Θ temporality layer + Λ timeout semantics)*

The time library wraps:

* system clock,
* timers,
* sleep operations,
* monotonic clocks,
* runtime scheduling hooks.

### **Core Types**

```
type Instant = u64      // monotonic counter
type Duration = u64     // nanoseconds or runtime-defined unit
type Timer = Handle<TimerDesc>
```

### **Functions**

#### **now() → Instant**

* Δ via syscall.time
* Φ map to PMSL Instant

#### **sleep(duration)**

Operator sequence:

* Θ schedule sleep
* Kernel timer → async wake event (Φ)
* Σ at completion

#### **timeout(duration, future)**

Compiled as:

```
spawn timer
select { future => Σ, timer => Λ(timeout) }
```

Θ, Λ, Φ work together to produce a clean timeout abstraction.

#### **interval(period)**

Generates recurring Θ-events.

---

# **10.2.4 Logging Library (Log.Std)**

*(Structured Θ/Σ events + Ψ consistency rules)*

Logging is a **structured commit mechanism**:

### **Types**

```
enum Level { Trace, Debug, Info, Warn, Error }
type LogRecord = { timestamp:Instant, level:Level, message:String, context:Map }
```

### **Functions**

#### **log(level, msg, context?)**

Sequence:

* Δ distinguish level
* Ω_check(Log_Write)
* Θ timestamp insertion
* ∇ emit record to sink (memory, console, file, syslog)
* Σ flush or batch depending on config

#### **set_log_target(target)**

Switches □ context for logging.

#### **scoped_context(k,v)**

Creates a temporary □ frame contributing fields to all nested log records.

---

# **10.2.5 Policy Library (Policy.Std)**

*(Ψ policy definition + Ω role binding + Σ activation + Φ fallback)*

PMSL-level policies govern:

* invariants for API use,
* access controls,
* safe-mode enforcement,
* module-scoped permissions.

Kernel Ψ protects system resources;
**Runtime Ψᵣ** protects program-level invariants.

### **Types**

```
type Policy = Frame<PolicyCtx>
type Rule = { condition, effect }
type PolicyError = enum { Violated, Invalid, Unauthorized }
```

### **Functions**

#### **define(policy_name, rules)**

Creates a Ψ-typed frame.

#### **activate(policy)**

Equivalent to running:

```
Ψ_add(policy)
```

updates the runtime policy stack.

#### **deactivate(policy)**

Removes from Ψ stack.

#### **check(rule, input)**

Δ + Ω_check + Φ mapping of failures.

#### **with_policy(policy) { ... }**

Sets a scoped Ψ frame (□+Ψ interplay).

---

# **10.2.6 Integration with Concurrency & Events**

The core libraries integrate tightly with the event system (5.3):

* Networking uses async readiness events
* FS async I/O uses kernel event queues
* Timers use kernel timer interrupts → runtime Θ events
* Logging can be asynchronous or batched using Θ/Σ
* Policies can be time-sensitive:

  * “no more than X ops per Θ window”
  * “forbid write after Σ commit”

The runtime scheduler coordinates all of this according to the semantics of tasks, channels, Λ, Φ, Θ introduced earlier.

---

# **10.2.7 Summary**

The Core Libraries are **structured, operator-aligned facades** over kernel services.

| Library    | Dominant Ops  | Meaning                                                     |
| ---------- | ------------- | ----------------------------------------------------------- |
| FS.Std     | Δ, ∇, Σ, Φ, Ω | path resolution, I/O, commits, error reframing, permissions |
| Net.Std    | □, Θ, Λ, Φ, Ω | connection frames, timeouts, transport events               |
| Time.Std   | Θ, Λ, Φ       | scheduling, sleep, timers                                   |
| Log.Std    | Θ, Σ, Δ       | timestamping + commit-based logging                         |
| Policy.Std | Ψ, Ω, □, Φ    | policy definition, enforcement, scoped invariants           |

Everything is **safe, capability-controlled, frame-typed, and policy-aware**.

---

# **10.3 Concurrency & IO APIs**

*(The PMSL High-Level Concurrency Layer built from Θ, Λ, Φ, Ω, Χ, Σ)*

This is the **top** of the runtime stack:
a structured, operator-aligned concurrency model built *directly* on PMS primitives and the PMS-CPU + kernel capabilities defined earlier.

Unlike ad-hoc concurrency models used in legacy languages, PMSL provides **native**, **type-safe**, **policy-aware**, and **operator-grounded** concurrency where:

* **Θ** is the temporal/scheduling backbone
* **Λ** is meaningful absence (timeouts, non-events)
* **Φ** is exception/migration/interrupt-driven recontextualization
* **Ω** ensures privilege/capability isolation
* **Χ** enforces per-task, per-channel memory/scope isolation
* **Σ** provides commit/atomicity boundaries for concurrent effects

And — crucially — **all concurrency primitives map to explicit syscalls and runtime operations**, making PMSL concurrency deterministic-by-construction or nondeterministic only where allowed by Ψ.

---

# **10.3.1 Concurrency Model Overview**

PMSL supports two concurrency modes:

## **(1) Structured Concurrency (default)**

All concurrent tasks must be spawned within a lexical “task scope,” forming a **Θ-scoped task tree**:

```
task {
    let a = spawn taskA()
    let b = spawn taskB()
    wait_all(a, b)
}
```

No orphan tasks. No hidden global threads.
Lifetime is tied to scope → Σ commit upon scope exit.
Cancellation = Φ-style recontextualization.
Timeouts = Λ events integrated into Θ scheduling.

## **(2) Unstructured Concurrency (explicit, opt-in)**

Allowed only through Ω-gated APIs:
good for daemons, server loops, background workers.

```
spawn_detached worker()
```

Cancelled only through Ψ-kill or administrative policies.

---

# **10.3.2 Kernel Execution Units → PMSL Tasks**

In the kernel (3.3), processes and threads are represented as **isolation frames** (Χ) combined with roles (Ω) and temporal state (Θ).

PMSL maps each “task” to a kernel **thread frame**, but with restrictions:

* each PMSL task has:

  * its own **□ lexical frame**
  * its own **Χ isolation context** (memory slices, locals)
  * its own **Θ timestamp / scheduler-quanta**
  * optional **policy stack Ψᵣ** (runtime-level)

This yields deterministic, safe task boundaries.

---

# **10.3.3 Task API**

### **spawn(f) → Task<T>**

Creates a child task:

**Operator expansion:**

1. Δ classify function f
2. Χ allocate isolated context for child
3. □ create new lexical frame for task
4. Ω grant task-level caps
5. Θ register task with scheduler
6. Σ return handle

### **spawn_detached(f)**

Same as spawn, except:

* no parent Σ join requirement
* Ω-check ensures caller has “DETACH” capability
* lifetime under kernel, not lexical scope

### **async/await syntax**

PMSL supports:

```
async fn foo() -> Int {
    let v = await read(socket)
    return v + 1
}
```

**await** compiles to:

* Δ check future state
* Θ suspend current task
* Λ wait for event (if unresolved)
* Φ resume upon event → new context
* Σ integrate result into local frame

---

# **10.3.4 Task Synchronization Primitives**

All synchronization abstractions are structured versions of kernel primitives (5.2), but type-safe.

---

## **Mutex<T>**

```
let m = Mutex<T>::new(val)
m.lock().with(|mut t| { ... })
```

Semantics:

1. Ω ensures locking allowed
2. Χ ensures t is isolated while locked (view from one task)
3. Θ requeues task on contention
4. Σ unlock commits new t

---

## **Semaphore(n)**

Kernel-backed, with Θ/Λ integration for timed waits.

---

## **Channel<T>** — the canonical IPC primitive

PMSL includes **typed, bounded/unbounded channels**:

```
let (tx, rx) = channel<T>(capacity=16)
tx.send(v)
let v = rx.recv()
```

Operator semantics:

* **send**:
  Δ classify message → Ω capability check → Χ copy/transfer → ∇ write → Σ commit

* **recv**:
  Δ classification → Θ wait → Λ if empty timeout → Φ on channel-close → Σ integration

Channels form the safe user-space equivalent of kernel message queues (5.1).

---

## **Select / Event-Choice**

```
select {
    msg = rx.recv()     => handle(msg),
    tick = timer.next() => handle(tick),
    timeout(50ms)       => handle_default()
}
```

This compiles to a **Θ-driven event loop** with Δ-branches and Λ timeouts.

---

# **10.3.5 Task Lifetime & Cancellation (Φ + Ψ)**

Cancellation is **structured**:

### **cancel(task)**

* Ψ-runtime verifies hierarchical relationship
* Φ transitions child into cancellation-context
* Child receives cancellation exception
* Child must Σ end state or Φ propagate up
* Parent waits for clean Σ integration

### **scope exit → Σ commit**

At the end of any:

```
task {
    ...
}
```

The runtime performs:

* Σ integration of task results
* Ψ cleanup of policy stack
* Χ release of isolated resources
* Θ update scheduler accounting

---

# **10.3.6 IO API and Asynchronous IO**

PMSL unifies all IO (FS, networking, drivers) via the **same concurrency primitives**.

### **Basic async IO skeleton**

```
let data = await fs.read(fd, n)
let msg  = await socket.recv()
let evt  = await device.wait_irq()
```

Under the hood:

* read/recv/irq → Λ (wait) + Θ (event scheduling) + Φ (wake)
* isolation of buffers via Χ
* privilege checks via Ω
* proper commits via Σ

Async IO becomes the *default* safe mechanism.

---

# **10.3.7 High-Level Concurrency Patterns (Α-patterns)**

The standard library includes reusable Α-patterns:

---

### **Task Pool**

```
task_pool(size=8).submit(job)
```

Expands to:

* Χ isolate worker contexts
* Θ schedule jobs
* Σ returns results in deterministic order

---

### **Pipeline**

```
pipeline {
    stage1 | stage2 | stage3
}
```

Each stage is a □ frame with its own Χ resource boundaries.

---

### **Supervisor Trees (like Erlang), but structured**

```
supervisor {
    child(taskA),
    child(taskB),
    on_fail restart
}
```

Φ → failure detection
Σ → restart commit
Ψ → invariant: supervisor cannot silently drop children

---

### **Async Streams**

Native operator-typed stream abstraction:

```
for await msg in stream {
    ...
}
```

Temporally grounded via Θ.

---

# **10.3.8 Memory Consistency for PMSL (User-Level)**

PMSL uses the kernel’s memory model (2.7) but strengthens it:

* All shared-memory synchronization uses **Σ barriers**
* Data races are structurally impossible unless Ω allows “unsafe” sections
* Channel+task-based concurrency has **strong SC semantics**

Thus PMSL gives:

* Deterministic messaging
* Safe structured concurrency
* Explicit escape hatches (Ω/Ψ/Σ) for low-level control

---

# **10.3.9 Summary**

PMSL Concurrency & IO APIs provide:

### **Primitive level**

| Operator | Role                                         |
| -------- | -------------------------------------------- |
| Θ        | task scheduling, suspension, timers          |
| Λ        | timeouts, waits, absence                     |
| Φ        | cancellation, exceptions, trap-based resumes |
| Ω        | task permissions, async IO gating            |
| Χ        | isolated task memory and channel boundaries  |
| Σ        | commit points for synchronization            |

### **APIs**

* spawn, spawn_detached
* async/await
* channels, select, timers
* mutexes, semaphores
* supervisor trees
* pipelines & pools
* unified structured async IO

### **Guarantees**

* Structured, safe concurrency
* Deterministic or explicitly nondeterministic
* Task-scoped invariants via Ψ
* Isolation by construction
* Built on the PMS-CPU + kernel IPC model

---

# **11. Tooling & Verification**

Tooling in PMS is not an afterthought — it is *intrinsically PMS-structured*.
Every analysis, verification, debug, or transformation tool is defined on top of:

* the **operator algebra** (Δ–Ψ),
* the **meta-model for states/transitions** (0.4),
* the **PMS-UM reduction semantics**, and
* the **PMS-CPU ISA** (2.2).

The central artifact under which these tools operate is the **PMS Intermediate Representation (PMS-IR)**.

---

# **11.1 Intermediate Representation (IR) – Operator-Tagged**

The PMS-IR is a **unified, operator-typed, analyzable representation** of all executable PMS artifacts:

* PMSL source modules
* compiled PMSL functions
* kernel policies
* syscall interface specs
* driver-state machines
* networking protocol handlers
* verification models
* offline interpretable artifacts (formal proofs, audits)

It is the **single canonical IR** for analysis, optimization, verification, simulation, and codegen.

---

# **11.1.1 Guiding Principles**

The PMS-IR is designed to:

### **(1) Preserve PMS operator semantics**

Every instruction in PMS-IR is explicitly tagged with **one operator in {Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ}**.

This tag is invariant under optimization and transformations.

Example:

```
Δ.compare r1 r2
∇.add     r3 r1 r2
□.enter   frame_id
Θ.tick
Φ.raise   exc_id
Ψ.guard   policy_id
```

### **(2) Preserve all dependency constraints**

Unlike machine IRs which treat operators generically, PMS-IR enforces that:

* ∇ cannot appear without Δ in its dominator ancestry
* Λ only appears under Θ or ∇ expectations
* Φ requires Δ and □ ancestry
* Σ requires ∇/Θ antecedents
* Ψ may block or rewrite further control paths

These constraints are **syntactically encoded** in the IR and **checked statically**.

### **(3) Be amenable to static analysis & model checking**

PMS-IR is:

* SSA-like (single-assignment for core values)
* CFG-representable (basic blocks + edges)
* Explicit about time (Θ)
* Explicit about role transitions (Ω)
* Explicit about frame/context boundaries (□)
* Explicit about isolation transitions (Χ)

### **(4) Be the input for PMS-CPU codegen**

PMS-IR → PMS-CPU ISA is a clean lowering:

* Δ → CMP/TST/JMP
* ∇ → ALU/LOAD/STORE
* □ → FRM_ENTER/LEAVE
* Ω → SET_ROLE
* … etc.

---

# **11.1.2 PMS-IR Structure**

A PMS-IR program is a tuple:

[
IR = (Defs, Types, Blocks, Policies)
]

Where:

### **(A) Defs**

Function, module, syscall, and driver-state definitions:

```
def foo(a: Int, b: Int) -> Int
def driver.usb.handle_irq(ctx: IRQContext) -> Status
def sys.read(fd: Int, buf: Ptr, len: Int) -> Int
```

### **(B) Types**

Type environment from PMSL’s type system (9.3):

* frame types
* role sets
* policy sets
* process/actor types
* structural types (records, unions, enums, sums)

### **(C) Blocks**

Basic blocks of operator-typed instructions:

```
block B0:
    Δ.test r1 r0
    BEQ B_fail
    ∇.add r2 r1 r0
    Θ.tick
    JMP B1
```

### **(D) Policies**

Inline Ψ constraints attached to:

* functions,
* modules,
* syscalls,
* blocks,
* edges.

Example:

```
Ψ.require( role == USER or CAP_IO )
Ψ.forbid_write(frame=kernel_code)
Ψ.max_time(block=B0, ticks=5)
```

---

# **11.1.3 IR Instruction Format**

Each PMS-IR instruction is a record:

```
IRInstr {
    op: PMSOperator,      // Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ
    opcode: Symbol,        // specific operation (cmp, add, enter_frame, etc.)
    operands: List<Value>, // registers, SSA names, frames, roles
    meta: MetaInfo         // loc, debug, source mapping, comments
}
```

Example:

```
IRInstr(
  op = ∇,
  opcode = "store",
  operands = [r2, frame(FR_DATA), offset(0x10)],
  meta = {src="foo.pmsl:41"}
)
```

### **PMSOperator is mandatory**

There is *no* untyped instruction in the IR.

---

# **11.1.4 Control Flow Graph (CFG) Structure**

A PMS-IR CFG edge is labeled with one of the operators:

* **Δ-edges** — conditional distinctions
* **Θ-edges** — temporal progression
* **Φ-edges** — trap/exception/recontextualization flow
* **Ψ-edges** — policy-induced constraints (may prune edges)
* **Σ-edges** — commit/transaction boundaries
* **Λ-edges** — timeout fallback paths
* **Χ-edges** — exit/enter isolation

CFG node example:

```
block B0:
    Δ.eq r1, r0
    BEQ B1
    JMP B2
```

CFG edges:

* (B0 → B1) labeled Δ
* (B0 → B2) labeled Δ

This enables **operator-aware control-flow analysis**, e.g.:

* “Can a Σ commit be reached without a preceding ∇?”
* “Can a Φ raise escape an isolation (Χ) boundary?”
* “Is this Ω privilege elevation reachable by untrusted user input?”

---

# **11.1.5 SSA Integration**

PMS-IR uses **partial SSA**:

* Register-like values (v0, v1, …) are single-assignment
* Frame pointers, roles, and policies are *not* in SSA:

  * because they are modeled structurally (□, Ω, Ψ)
  * they evolve through operator-typed transitions

Example:

```
v0 = ∇.load [FR+0]
v1 = Δ.compare v0, 10
BEQ B1
v2 = ∇.add v0, 3
Σ.commit
```

---

# **11.1.6 IR Meta-Operators for Analysis**

Some operators have **meta variants** used *only during tooling*, not during execution:

### **Δ? — symbolic distinction**

Used to ask "what if x = y?" in static analysis.

### **Φ? — symbolic recontextualization**

Used for modeling exception propagation.

### **Ψ? — symbolic policy solving**

Used to check whether a policy can ever be violated.

Meta-operators do **not** appear in executable IR but are used by:

* model checker,
* static analyzer,
* symbolic execution engine.

---

# **11.1.7 IR Validation (Static)**

Before an IR program can be accepted:

1. **Operator dependency constraints (0.3)** must hold globally.

2. **Each CFG path** must satisfy consistency:

   * ∇ dominated by Δ
   * Λ preceded by Θ/∇
   * Φ preceded by Δ and □
   * Σ dominated by ∇/Θ
   * Ψ must not be bypassed
   * Χ transitions fully bracketed

3. **Type checks** (9.3) for roles, frames, policies, processes.

4. **Policy consistency checks** (Ψ):

   * All policy preconditions resolvable
   * No policy cycle creating unsatisfiable invariants

5. **Isolation correctness** (Χ):

   * No escape from isolated subspace without explicit Χ.exit

6. **Temporal constraints**:

   * No infinite Θ-only loops without policy exception
   * No starvation of Δ / ∇ under fairness assumptions

---

# **11.1.8 IR Transformations**

PMS-IR supports several transformations, each operator-aware:

### **(A) Dead code elimination (Δ-aware)**

Eliminates blocks whose Δ distinctions can never be satisfied.

### **(B) Φ-normalization**

Rewrites nested Φ sequences into canonical form:

```
Φ.raise → Φ.save_ctx → Φ.dispatch_handler
```

### **(C) Σ-hoisting / sinking**

Move commit boundaries to reduce overhead while preserving Σ dominance relations.

### **(D) Ω-constraint narrowing**

Simplify role transitions based on static analysis:

```
if role == USER and CHK_CAP(CAP_IO) always true:
    collapse Ω→ identity
```

### **(E) □-frame flattening**

Inline frames where isolation and privilege constraints allow it.

### **(F) Δ-specialization**

Specialize branches with known distinctions → partial evaluation.

### **(G) A-expansion**

Inline or decompose attractor patterns (loops, macros).

---

# **11.1.9 IR Serialization Format**

A PMS-IR file is stored as a structured, declarative format:

```
pms-ir-version = 1.0

module mymod:
    import fs
    import net

types:
    Frame DataFrame { base:Addr, size:Size, perms:Perm }
    Role  User | Kernel | Driver

policies:
    Ψ.require( role != Kernel or CAP_K )
    Ψ.forbid_write(frame=kernel_code)

function add(a:Int, b:Int) -> Int:
block entry:
    Δ.cmp v0=a, v1=b
    BEQ block eq_path
    ∇.add v2=a, v3=b
    Σ.commit
    JMP block exit
```

Intended to be:

* machine-readable
* checkable
* stable under optimization
* embeddable into debugging and verification tools

---

# **11.1.10 Summary**

The PMS-IR is:

* **operator-tagged**, preserving Δ–Ψ semantics
* **dependency-checked** by construction
* **SSA-compatible**, **CFG-structured**, **policy-aware**
* extensible for static analysis, symbolic execution, and model checking
* the canonical lowering target from PMSL (9.x)
* and the canonical raising source for PMS-CPU codegen (10.x → 2.x)

This IR enables:

* formal verification,
* security auditing,
* debugging,
* optimization,
* and multi-target compilation

all without losing PMS structural invariants.

---

# **11.2 Static Analysis & Linting – Ω/Ψ, Σ/Λ/Φ Checks**

Static analysis in PMS is not merely “compile-time checking.”
It is a **semantic verification phase** that enforces PMS operator constraints, type rules, isolation guarantees, temporal properties, and policy consistency **before** PMS-CPU codegen or kernel integration.

Think of PMS static analysis as:

* **structural analysis** (operators Δ–Ψ)
* **role/capability analysis** (Ω)
* **policy/invariant analysis** (Ψ)
* **temporal analysis** (Θ, Λ)
* **context/isolation analysis** (□, Χ)
* **commit semantics analysis** (Σ)
* **exception/recontext analysis** (Φ)

This is much richer than typical compilers.

---

# **11.2.1 Analysis Pipeline**

Given PMS-IR (11.1):

```
PMSL → IR-gen → PMS-IR → Static Analysis → Optimizer → PMS-CPU codegen
```

Static analysis consists of eight major phases:

1. **Operator Dependency Checking (from 0.3)**
2. **Type & Frame Analysis (frames, roles, policies)**
3. **Privilege / Role Flow Analysis (Ω)**
4. **Policy Verification (Ψ)**
5. **Temporal Analysis (Θ, Λ)**
6. **Isolation Correctness Analysis (Χ)**
7. **Commit & Integration Analysis (Σ)**
8. **Exception Propagation Analysis (Φ)**

Linters implement the lightweight, user-facing, developer-friendly parts of these phases.

---

# **11.2.2 Operator Dependency Checking**

PMS requires:

* ∇ dominated by Δ
* Λ preceded by Θ or ∇
* Φ preceded by Δ and □
* Σ dominated by ∇/Θ
* Ψ dominated by Δ
* Χ dominated by □ (no isolation without an active frame)

The static analyzer walks the CFG and guarantees that **on all paths** the dependency table (0.3) is satisfied.

### Violations (examples):

**Error:**

```
∇.store r1, [F_DATA]  
↑ No Δ in dominator chain
```

**Error:**

```
Λ.timeout            // illegal
↑ no Θ expectation upstream
```

**Error:**

```
Φ.reinterpret …  
↑ must follow Δ and □ in all paths
```

**Error:**

```
Σ.commit  
↑ no ∇ or Θ upstream → empty commit
```

These are *structural violations* — they are always fatal.

---

# **11.2.3 Role / Capability Analysis (Ω)**

This phase analyzes:

* role transitions (`Ω.enter`, `Ω.elevate`, `Ω.drop`)
* privilege requirements of IR instructions
* capability sets required for syscalls, frame transitions, and isolation exit

We perform flow-sensitive analysis over the CFG:

```
role_in[B]  -> role_out[B]
```

Rules:

* Ω edges update the role context
* Δ/Θ/∇ do not (unless instruction explicitly annotated)
* Φ may change role if exception re-enters kernel mode, etc.

### Checks Performed

#### **(1) Unreachable Privilege Escalation**

```
Ω.enter(KERNEL)
↑ not reachable from user-space without explicit capability
```

#### **(2) Illegal Cross-Frame Access**

```
∇.store [kernel_frame]  
↑ only permitted in roles = {Kernel, DriverIO}  
role = User → violation
```

#### **(3) Excessive Privilege Retention**

Fail if:

* role elevated to KERNEL but never dropped back → violates Ψ safety policy.

#### **(4) Missing Role Guards**

If a block contains privileged operations but has no Ω-preconditions or Ψ guards:

```
Δ.test  
∇.write [dev_reg]
↑ write to device register requires Ω(role=Driver)
```

---

# **11.2.4 Policy Verification (Ψ)**

Policies appear as Ψ instructions and Ψ-annotations in IR.
Static analysis performs:

### **Policy Reachability**

Ensure that every path that must pass a policy check **does** pass it.

### **Policy Coverage**

Ensure all policies relevant to:

* filesystem accesses
* network flows
* isolation boundaries
* driver I/O
* syscalls
* resource usage

are reached in all valid scenarios.

### **Policy Satisfiability**

Detect contradictions:

```
Ψ.require role == USER
Ψ.require role == KERNEL
↑ Unsatisfiable combined constraints
```

Or more subtle forms:

```
Ψ.max_time(block=B0, ticks=10)
Ψ.min_time(block=B0, ticks=12)
↑ Conflicting temporal constraints
```

### **Policy Monotonicity**

Ψ may not weaken constraints once established, unless explicitly marked as “rollback/override”.

Static analysis checks:

* no unexpected weakening of invariants,
* Ψ overrides only permitted in admin privilege contexts.

### **Open Policy Violations**

Paths that **escape** from required policy enforcement:

```
entry → … → Σ.commit  
↑ never hits Ψ.guard → violation
```

---

# **11.2.5 Temporal Analysis (Θ, Λ)**

Temporal analysis enforces correct usage of:

* **Θ temporal progression**
* **Λ non-event / timeout**
* **Φ timed exceptions**
* **Ψ temporal bounds**

### Checks:

#### **(1) Illegal Timeout**

Λ must have an upstream Θ or expected ∇.

#### **(2) Deadloops**

A loop with only Θ operations and no policy guard:

```
loop B0:
    Θ
    JMP B0
↑ infinite Θ-only loop unless Ψ allows it (rare)
```

If no Ψ guard exists → static error.

#### **(3) Event-Time Inconsistency**

If Λ timeout is reachable *without* any event being expected, raise an error.

#### **(4) Temporal Bound Violations**

Policies can specify:

```
Ψ.max_time(block=B2, ticks=5)
```

Static analyzer estimates tick counts and flags potential overrun.

#### **(5) Missed Deadline Paths**

If a block has a deadline but CFG allows bypassing Θ steps leading to deadline → violation.

---

# **11.2.6 Isolation Correctness Analysis (Χ)**

Isolation (Χ) establishes boundaries akin to:

* processes
* containers
* security domains
* transactional sandboxes
* protocol/statemachine localities

Static analysis ensures:

### **(1) No Leakage Across Χ Boundaries**

If a value or pointer from an isolated region flows outward without explicit **Χ.exit**, error.

Example:

```
Χ.enter iso_f
v = ∇.load iso_frame[0]
return v        // error — returning isolated pointer/data
```

### **(2) No Implicit Capability Escalation by Isolation**

Isolation cannot be used to smuggle privileged frames.

```
User enters isolation → loads driver_frame → exits  
↑ Violation: isolation cannot bypass Ω restrictions
```

### **(3) Balanced Isolation**

Each Χ.enter must be matched with a χ.exit on all terminating paths.

### **(4) No Cross-Context Writes**

Writes from one isolation context to another must pass through authorized integrator / mediator.

---

# **11.2.7 Commit & Integration Analysis (Σ)**

Σ marks integration / commit points:

* FS writeback
* transactional commit
* IPC message finalization
* resource accounting boundaries

Static analysis checks:

### **(1) Empty Commit**

Σ must not occur without any prior ∇ or Θ that produce state to integrate.

### **(2) Commit Under Isolation**

Σ inside Χ isolation is only legal if it commits *inside* the isolated context — not to a parent context unless explicitly authorized.

### **(3) Commit Ordering**

Σ must respect frame dominance:

```
□.enter F1
∇ write
□.enter F2
Σ.commit   // must commit in F2, not bypass into F1
```

### **(4) Atomicity Consistency**

If Σ is part of a transaction boundary, static analysis ensures all required operations are included and no forbidden operations appear after Σ in the same context.

---

# **11.2.8 Exception & Recontextualization Analysis (Φ)**

Φ operations restructure execution context:

* raise exceptions
* switch protocol versions
* reframe data
* propagate context changes

Analysis verifies:

### **(1) Dominated by Δ and □**

As required by semantics:

```
Φ.raise without Δ and □ upstream → illegal
```

### **(2) Correct Isolation Escape Semantics**

Φ cannot jump out of an isolated context unless:

* explicitly permitted via policy
* a matching Χ.exit is provided

### **(3) Completely Handled Exceptions**

Every Φ.raise must have:

* Φ.handler, or
* return-to-caller policy allowing propagate upward, or
* entry into halting state.

### **(4) Balanced Reframes**

Multiple Φ transitions must not lead to “identity loss,” i.e., forgetting original frames or roles unless allowed by Ψ.

---

# **11.2.9 Linting Layer**

Linting = static analysis made developer-friendly.

Examples of lint rules:

### Δ-lints

* “Δ distinction result not used”
* “Suspicious Δ: comparison always true/false”

### ∇-lints

* “∇ write to zero-length frame”
* “∇ compute but result unused before Σ”

### Ω-lints

* “Role elevation immediately dropped — suspicious”
* “Unreachable Ω branch”

### Θ-lints

* “Θ inside tight loop without Ψ guard”
* “Unused temporal counter”

### Λ-lints

* “Timeout unreachable — remove Λ”
* “Multiple Λs without corresponding expected event”

### Φ-lints

* “Handler returns to invalid frame”
* “Φ.chain too deep — consider refactoring”

### Χ-lints

* “Isolation enters but never commits any Σ inside”
* “Potential isolation leak: value flows out of domain”

### Σ-lints

* “Σ inside high-frequency loop — performance hazard”
* “Σ commits too large a region — consider splitting”

### Ψ-lints

* “Policy always true — redundant”
* “Conflicting Ψ constraints”

---

# **11.2.10 Deliverables of the Static Analyzer**

For every PMS-IR input, the analyzer produces:

### **(A) Operator-Flow Graph**

Shows how Δ–Ψ propagate across the program.

### **(B) Role-Flow Graph (Ω)**

Visualizes privilege transitions.

### **(C) Frame-Path Analysis**

Which frames the program can enter and in what order.

### **(D) Policy Verification Report**

Satisfied/violated policy constraints.

### **(E) Isolation Audit**

All isolation contexts, entry/exit, violations.

### **(F) Temporal Model**

Tick ranges, deadlines, loops, deadlines, reachability.

### **(G) Resource Pre-Accounting**

Static estimate of commits, memory writes, IPC usage.

### **(H) Human-Friendly Lint Report**

Warnings and suggestions.

---

# **11.2.11 Summary**

Static analysis ensures **structural correctness, safety, capability discipline, policy compliance, isolation integrity, temporal soundness, and commit semantics** across PMS programs **before execution**.

It enforces the PMS operator algebra *at compile time*, not only at runtime.

---

# **11.3 Model Checking & Property Verification**

*(Operator-typed verification: Δ–Ψ as the semantic backbone)*

PMS systems have **first-class semantics** for:
branching (Δ), mutation (∇), frames (□), absence (Λ), patterns (Α), roles (Ω), time (Θ), reframing (Φ), isolation (Χ), commit (Σ), and invariants (Ψ).
This makes PMS a *well-typed transition system*—perfect for formal verification.

This section defines how to verify PMS programs, kernels, protocols, and distributed systems.

---

# **11.3.1 Formal Verification Model**

We model a PMS program (IR) as:

[
\mathcal{T} = (S, S_0, \rightarrow, P)
]

Where:

* **S**: PMS states
  *(sₙ are tuples of core/frame/role/policy/meta, 0.4)*
* **S₀**: initial states
* **→**: transition relation induced by PMS operators
* **P**: active policy set (Ψ)

Thus PMS verification = verifying properties of the labeled transition system (LTS):

[
s \xrightarrow{o} s' \quad\text{with } o \in {\Delta,\nabla,\square,\dots,\Psi}
]

---

# **11.3.2 Operator-Labeled Transition System**

Every PMS transition is labeled with exactly one operator (Δ–Ψ).
Thus a path is:

[
s_0 \xrightarrow{o_1} s_1 \xrightarrow{o_2} s_2 \xrightarrow{o_3} \cdots
]

Model checking uses these labeled paths to verify:

* **safety**
* **liveness**
* **isolation guarantees**
* **role/capability constraints**
* **resource bounds**
* **temporal correctness**
* **policy consistency**

Because every label is semantically meaningful (NOT just arbitrary opcodes), the model checker can reason about system behavior at an extremely high level.

---

# **11.3.3 Classes of Properties**

We verify properties corresponding to PMS operators:

---

## **(A) Safety Properties — “Nothing bad ever happens” (Ψ-level invariants)**

Examples:

* “Kernel memory is writable only in Ω=Kernel role”
* “No cross-domain writes violating Χ”
* “No Φ exception escapes its allowed frame”
* “No Σ commit occurs without prior ∇ mutation”
* “Timeout Λ cannot occur in frames marked ‘strict temporal’”

These are expressed as:

[
\mathbf{AG}\ \text{safe}(s)
]

Where safe(s) is a predicate over PMS state components.

---

## **(B) Liveness Properties — Θ-driven eventuality**

Examples:

* “Every request (Δ) eventually produces a response (Σ) under fair Θ scheduling”
* “Isolation contexts eventually exit via Χ.exit”
* “Every driver interrupt (Φ) eventually triggers driver handler ∇”

Expressed as:

[
\mathbf{AF}\ \text{goal}(s)
]

Under fairness constraints encoded as Ψ_fair.

---

## **(C) Temporal Boundedness — Θ/Λ constraints**

* “Operation completes within T ticks”
* “Λ timeout only occurs if expected by Θ event”

Expressed as:

[
\mathbf{AG}( \text{entered}(B) \Rightarrow \mathbf{AF}_{\le T}\ \text{exited}(B))
]

---

## **(D) Isolation Properties — Χ correctness**

* “No isolated value leaks to non-isolated context”
* “No cross-frame jump without Ω permission”

Formally:

[
\mathbf{AG}\neg\text{leak}(s)
]

---

## **(E) Policy Adherence — Ψ constraints**

Policies are invariants over:

* roles (Ω)
* frames (□)
* temporal structure (Θ)
* allowed transitions

Ψ gives us a built-in mechanism for specifying checked properties:

[
\mathbf{AG}\ \Psi_ok(s)
]

If Ψ_ok fails → halting transition into S_H.

---

## **(F) Commit Correctness — Σ**

* “Every Σ commit represents a consistent state”
* “No Σ happens inside forbidden context”

Formally:

[
\mathbf{AG}(\Sigma \Rightarrow \text{consistent}(s))
]

---

# **11.3.4 Model Checking Algorithmic Strategy**

PMS verification uses hybrid techniques:

---

## **(1) Symbolic Model Checking**

(State-space exploration using symbolic PMS-state encodings.)

Core elements:

* symbolic frame contexts (□)
* symbolic role sets (Ω)
* symbolic isolation partitions (Χ)
* symbolic policies (Ψ)
* symbolic time regions (Θ)

We use:

* BDD-like symbolic encodings
* SMT solving over operator constraints
* symbolic execution over PMS-IR

---

## **(2) Abstract Interpretation**

We abstract:

* value ranges
* frame sets
* capability flows
* temporal bounds
* policy invariants
* Σ commit regions
* Χ isolation partitions

This yields scalable approximations of reachable PMS states.

---

## **(3) Operator-Dominance Analysis**

Because PMS operators have a **partial order** (from dependency rules):

* Δ dominates ∇
* □ dominates Χ and Φ
* Θ dominates Λ and Σ
* Ω dominates most privileged ops
* Ψ dominates everything

We use this ordering to prune illegal state transitions and compress the search space.

---

## **(4) Path Pruning via Ψ Policies**

Ψ invariants eliminate many transitions from the LTS:

* halting states
* forbidden execution paths
* disallowed frame transitions
* illegal role changes
* illegal timeouts

This drastically reduces the model-checking space.

---

## **(5) Commit-Region Partitioning (Σ)**

Σ divides the LTS into logical phases.
We exploit Σ boundaries to:

* modularize the state space
* collapse many internal ∇/Θ steps
* enable local reasoning inside transaction-like regions

---

# **11.3.5 Verification of Multi-Node Systems (Distributed PMS)**

Because PMS networks (Section 7) have:

* role-based endpoints (Ω)
* frame-scoped addressing (□)
* timeouts (Λ)
* retries (Θ)
* recontextualization (Φ)

…distributed properties can be modeled cleanly.

We can check:

---

### **(A) Distributed Safety**

* “No two nodes commit conflicting Σ states”
* “Cross-node isolation holds”
* “No unauthorized role escalation across nodes”

---

### **(B) Distributed Liveness**

* “Every Δ request eventually yields Σ response”
* “Heartbeats Θ eventually reach all neighbors”

---

### **(C) Network Partition Handling (Φ)**

* correctness of recontextualization under partition/unpartition
* consistency of state after reconnection

---

### **(D) Causal Ordering (Θ + Σ)**

* ordering of messages across frames
* consistent transaction replay after isolation

---

# **11.3.6 Verification of PMS-CPU and Kernel**

Key verification tasks:

### **Correct System Call Boundaries (Ω + Ψ)**

Ensure:

* user → kernel transitions respect capabilities
* kernel → user transitions drop privileges correctly
* system-wide invariants always hold

### **Memory Protection (Χ)**

Prove:

[
\mathbf{AG}\neg\text{illegal_access}
]

### **Scheduling Liveness (Θ)**

Guarantee:

* no runnable task is starved
* fairness obligations are met

### **Policy Enforcement (Ψ)**

Show:

* every policy-relevant path hits Ψ guards
* no escape path exists

---

# **11.3.7 Toolchain Integration**

The verification system connects to:

* PMSL compiler
* PMS-IR generator
* Static analyzer
* PMS-CPU simulator
* Kernel validator
* Distributed protocol analyzer

Outputs:

* **Counterexamples**, annotated with Δ–Ψ operator traces
* **Invariant violation reports**
* **Certified proof artifacts**
* **Temporal metrics**
* **Role/Frame policy diagrams**
* **Isolation graph integrity proofs**

---

# **11.3.8 Summary**

PMS verification is possible because:

* operators encode semantic structure at the machine level
* transitions are typed (Δ–Ψ)
* policies (Ψ) and isolation (Χ) give usable invariants
* commits (Σ) give natural proof boundaries
* frames (□) segment the state space cleanly
* time (Θ) and absence (Λ) express temporal properties directly

The result is a model-checking system far more expressive and analyzable than conventional instruction sets.

---

# **11.4 Debugging & Observability Model (logs, traces, metrics as Θ / Σ)**

PMS systems are *inherently observable* because **every state transition is typed** by one of the 11 PMS operators Δ–Ψ.
This allows debugging, tracing, profiling, and runtime analysis to be expressed directly in terms of:

* **Θ** — temporal progression, sequencing, timestamps
* **Σ** — commit points, stable snapshots, integration boundaries
* **Δ** — distinctions that drive control flow
* **Φ** — context shifts (exceptions, traps)
* **Χ** — isolation boundaries
* **Ω / Ψ** — privilege and invariant enforcement events

This section defines the **Operator-Structured Observability Architecture (OSOA)**.

---

# **11.4.1 Observability Model Overview**

Observability in PMS is built around three fundamental ideas:

---

### **(1) Every transition has operator semantics**

Instead of arbitrary “instruction tracing,” we log operator-labeled transitions:

[
s \xrightarrow{o} s' \quad (o \in {\Delta, \nabla, \square, …, \Psi})
]

A debugger or tracing system sees **semantic traces**, not raw opcodes:

* Δ = branch / distinction
* ∇ = mutation
* □ = frame/context change
* Θ = time progression
* Φ = exception/trap
* Σ = commit
* Ω = privilege escalation/de-escalation
* Χ = isolation enter/exit

This alone makes introspection dramatically easier.

---

### **(2) Temporal structure is explicit (Θ)**

Θ is the built-in clock/sequencer.
So all logs and traces attach to Θ events:

* *instruction_index*
* *logical time (Θ ticks)*
* *scheduler phase*
* *transaction window*
* *isolation epoch*

---

### **(3) Commit structure is explicit (Σ)**

Σ marks durable, consistent, debuggable points:

* stable snapshots
* transaction commits
* safepoints
* state captures for rollbacks
* log-flush boundaries

This gives observability **strong structural anchors**.

---

# **11.4.2 Debugging Model**

PMS defines a generic debugger abstraction using Δ–Ψ semantics.

## **Breakpoints (Δ / Ω / Ψ)**

Breakpoints can be placed on:

* **Δ events**
  Whenever a branch-distinction is evaluated (e.g., CMP → BEQ), debugger may stop.

* **Ω role transitions**
  Break when privilege mode changes (user→kernel, sandbox enter, capability grant).

* **Ψ policy triggers**
  Stop when an invariant is evaluated or violated.

* **Operator-specific breakpoints**
  e.g., break on any Φ exception, any Σ commit, any Χ isolation entry.

**Breakpoint format:**

```
break when op ∈ {Δ, Φ, Σ} and condition(s)
```

Examples:

```
break Δ where flag.Z = 1
break Φ where exception.code = DIV_ZERO
break Σ where transaction.id = T42
break Ω where role = Kernel
```

---

## **Stepping (Θ-driven)**

Because Θ encodes temporal steps:

* **step-instruction** = advance one Θ-tick
* **step-over** = advance to next Σ boundary
* **step-through-exception** = continue through Φ transitions until normal-frame reached
* **step-frame** = continue until next □ switch

This exposes logical execution structure, not just program counter increments.

---

## **Inspection of State**

Debugger can inspect:

### Registers & memory (∇/Δ)

* internal register values
* frame-scoped memory view via □

### Frame context (□)

* active address-space
* call-frame stack
* privilege frame

### Role & policy context (Ω/Ψ)

* current role r
* enabled capabilities
* active policy set

### Isolation context (Χ)

* sandbox / VM / process scope

### Meta-state (Θ/Λ)

* timers
* pending timeouts
* last-operator history

---

## **Reverse Debugging (via Σ snapshots)**

Because Σ marks consistent commit points, PMS supports:

* checkpointing on Σ
* replay from Σ boundaries
* reverse stepping until previous Σ

This is similar to rr (Mozilla), but structural and guaranteed by the model.

---

# **11.4.3 Tracing Model**

A **trace** is a sequence of operator-labeled events:

[
(o_1, t_1, info_1),\ (o_2, t_2, info_2), \dots
]

Where:

* (o_i) ∈ {Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ}
* (t_i) = Θ-timestamp
* (info_i) = metadata depending on the operator

---

### **Trace Schema (per operator)**

#### **Δ events**

Include: branch target, comparison values, flags.

#### **∇ events**

Register/memory diffs (possibly minimized with symbolic delta).

#### **□ events**

New frame id, previous frame, reason code.

#### **Λ events**

Timeout reason, expected event, elapsed time.

#### **Α events**

Pattern id, expansion range.

#### **Ω events**

Role transitions, capability grants/denials.

#### **Θ events**

Scheduler tick, quantum switch, pipeline retirement.

#### **Φ events**

Exception class, trap vector, reframe target.

#### **Χ events**

Isolation context id, entry/exit, access filters.

#### **Σ events**

Commit id, write-set summary, transaction boundaries.

#### **Ψ events**

Policy evaluation result, violated invariant, remediation action.

---

# **11.4.4 Observability Planes**

PMS defines **four observability planes**, each tied to specific operators:

---

## **(1) Control Plane — Δ / Ω / Ψ**

Used for:

* branching logic
* security-related control flow
* policy-driven decisions
* capability enforcement

---

## **(2) Data Plane — ∇ / Σ**

Used for:

* data mutations
* commit records
* write sets
* atomic ops

---

## **(3) Context Plane — □ / Φ / Χ**

Used for:

* address-space switching
* trap/exception reasoning
* isolation transitions

---

## **(4) Temporal Plane — Θ / Λ**

Used for:

* timing, profiling
* timeouts
* scheduler activity
* event ordering guarantees

---

# **11.4.5 Metrics & Profiling Model**

Metrics derive directly from Θ/Σ/Δ counts.

---

### **Timing Metrics (Θ)**

* cycles per instruction
* stall cycles
* scheduling quanta
* latency histograms

```
metric Θ.count(op = ∇)
metric Θ.latency(Φ_exception → Σ_commit)
```

---

### **Stability Metrics (Σ)**

* commits per second
* average write-set size
* commit failure rate
* transactional consistency violations (should be 0)

---

### **Control Metrics (Δ)**

* branch predictability
* decision tree depth
* misclassification counts

---

### **Policy Metrics (Ψ)**

* policy evaluation frequency
* policy violations over time
* mode changes (Ω transitions)

---

### **Isolation Metrics (Χ)**

* cross-context calls
* isolation boundary crossings
* restricted-access traps

---

# **11.4.6 Logging Model (Operator-Tagged Logging)**

Logs in PMS are **operator-tagged events**.
Example log record:

```json
{
  "op": "Φ",
  "timestamp": 88213,
  "frame": "kernel_trap",
  "role": "kernel",
  "exception": "DIV_ZERO",
  "pc": "0x8040123",
  "detail": "division by zero at user frame"
}
```

Logs are structured and machine-parseable by design because:

* PMS-IR is operator-tagged
* PMS-CPU ISA is operator-tagged
* PMSL runtime emits operator-tagged events

---

# **11.4.7 Operator-Aware Distributed Tracing**

Across nodes, traces include:

* frame id (□ node-specific)
* role/capability (Ω)
* temporal ordering (Θ with vector clocks)
* isolation boundaries (Χ → process, container, VM, domain)
* recontextualization flows across nodes (Φ)
* commit boundaries (Σ)

This yields **perfectly structured distributed traces**.

---

# **11.4.8 Debugging & Observability for Kernel and Drivers**

Kernel debugging relies heavily on:

* Φ (trap events)
* Ω (role switches)
* Χ (process isolation)
* Δ (scheduler decisions)
* Σ (commit of scheduling or memory operations)

Driver debugging focuses on:

* interrupts (Φ)
* DMA boundaries (□)
* device isolation (Χ)
* policy checks (Ψ)

---

# **11.4.9 Developer APIs (PMSL Debugging Interface)**

PMSL offers built-in debugging primitives:

```
debug.trace(op?)        -- subscribe to specific operator events
debug.step()            -- Θ-step
debug.break(condition)  -- Δ breakpoint
debug.snapshot()        -- Σ snapshot
debug.revert(id)        -- restore Σ snapshot
debug.inspect(object)   -- inspect frame/role/policy
debug.time()            -- Θ query
debug.wait()            -- Λ wait
debug.policy()          -- Ψ policy info
```

---

# **11.4.10 Summary**

PMS debugging & observability is **not bolted on** —
it’s inherent in the semantics of Δ–Ψ:

### **Θ**

→ Time, ordering, profiling, stepping

### **Σ**

→ Commit, checkpoints, reverse debugging

### **Δ**

→ Control-flow structure & breakpoints

### **Φ**

→ Exception/trap visibility

### **Χ**

→ Isolation-introspection

### **Ω/Ψ**

→ Security-governance instrumentation

The result is a radically clean and powerful debugging architecture.

---

# **11.5 Simulation / Emulation Environment (PMS-UM/CPU Simulators)**

*A unified, operator-typed simulation stack for correctness, debugging, research, and formal verification.*

A PMS system cannot be properly developed without **first-class simulators**—because PMS is an operator-semantic architecture (Δ–Ψ), simulation becomes unusually powerful and structurally clean.

This section defines the architecture, semantics, and tooling for:

* **PMS-UM simulators** (universal machine, abstract execution)
* **PMS-CPU simulators** (ISA-level emulation)
* **Hybrid simulators** (mixed abstract/ISA)
* **Deterministic vs. nondeterministic execution modes**
* **Debug hooks (Θ/Σ), policy hooks (Ψ), and isolation semantics (Χ)**
* **Replay, time dilation, symbolic execution paths**
* **Scenario generation for verification and security**

---

# **11.5.1 Simulation Goals**

PMS simulation is designed to support:

### **(1) Correctness**

* Validate PMSL programs
* Validate kernel subsystems
* Validate device drivers
* Ensure correct execution order (Θ)
* Check that isolation (Χ) and policy (Ψ) constraints never break

### **(2) Performance Exploration**

* Test various scheduling algorithms (Θ)
* Analyze memory behaviors, caches, frame churn (□)
* Study commit frequencies and transactional behaviors (Σ)

### **(3) Security & Governance Analysis**

* Explore privilege transitions (Ω)
* Model policy violations (Ψ)
* Simulate attack / failure scenarios using synthetic Φ events

### **(4) Language Runtime Testing**

* PMSL → IR → PMS-CPU pipeline testing
* FFI integration behavior
* Module loading and recontextualization semantics (Φ)

Because PMS execution is typed at the operator level, simulation has **complete semantic fidelity**.

---

# **11.5.2 PMS-UM Simulator (Abstract Machine Simulation)**

The PMS-UM simulator is the **lowest-level semantic reference**, independent of ISA details.

A UM simulation step is exactly:

[
(s, \pi) \Rightarrow (s', \pi)
]

Where *s* is the full PMS-UM state tuple:

[
s = (s_c,\ f,\ r,\ P,\ m,\ ip)
]

### **UM Simulator Features**

#### **A. Operator-Typed Execution**

The simulator does not execute “instructions” but **operator events**:

* Δ — distinction step
* ∇ — mutation step
* □ — frame switch
* Λ — timeout / non-event
* Α — macro expansion
* Ω — role transition
* Θ — temporal progress
* Φ — reframe / trap injection
* Χ — isolate / sandbox
* Σ — commit
* Ψ — policy evaluation

Each step logs structured events (per 11.4).

#### **B. Deterministic vs. Non-Deterministic Mode**

The simulator can run in:

* **deterministic UM mode** — all nondeterminism resolved by a fixed scheduler
* **non-deterministic UM mode** — branching runs, trace trees

This allows automated exploration of valid paths.

#### **C. History Tracking**

The meta-state m stores operator history for dependency validation (Δ → ∇, Θ → Λ, etc.).

#### **D. Instrumented Frames (□)**

* reveal address-space views
* reveal isolation boundaries (Χ)
* detect illegal frame transitions based on policies (Ψ)

#### **E. Reproducible Runs**

All runs can be replayed from Σ commit checkpoints.

---

# **11.5.3 PMS-CPU Simulator (ISA-Level Execution)**

The PMS-CPU simulator emulates **full ISA semantics** from section 2:

* fetch/decode = Δ
* execution = ∇
* frame operations = □
* privilege = Ω
* traps = Φ
* time = Θ
* isolation = Χ
* commit = Σ
* policy enforcement = Ψ

Enabled features:

### **Instruction Execution Model**

For each simulated instruction:

1. Δ: decode & operand distinction
2. Ω: capability check
3. Ψ: policy pre-check
4. ∇ / □ / Φ / Χ: apply instruction semantics
5. Σ: commit point
6. Θ: increment logical time

This pipeline captures all PMS semantics structurally.

---

# **11.5.4 Hybrid Simulator (UM + CPU)**

PMS systems may be evaluated at either:

* **abstract operator level** (UM)
* **ISA level** (CPU)

A hybrid simulator integrates both:

* High-level PMSL → IR runs in UM mode
* IR → PMS-CPU mapping executed in CPU mode
* Both traces unify because they are operator-tagged
* This enables “round-trip consistency checking”:

[
\text{UM-level semantics} = \text{CPU-level semantics}
]

This is essential for language correctness proofs.

---

# **11.5.5 Configuration & Scenario Testing**

Simulation environments can define **scenario scripts** that inject external events:

### **Event Injection (Φ/Λ)**

* timer interrupts
* device interrupts
* exception triggers
* synthetic faults
* timeouts

Example:

```
inject Φ exception=IO_FAULT at t=120
inject Λ when waiting_on="net.recv"
```

### **Role/Capability Scenarios (Ω/Ψ)**

Simulate changes in privilege:

```
inject Ω role=Elevated for 3 ticks
inject Ψ policy_violation="fs.read.restricted"
```

### **Isolation Scenarios (Χ)**

Simulate sandbox enter/exit:

```
inject Χ enter context=vm1 at t=60
```

This allows systematic stress-testing of kernel, FS, network stack, etc.

---

# **11.5.6 Symbolic Execution (Optional)**

Because every operator has rigid semantic meaning, symbolic execution becomes clean:

* Δ → symbolic branch conditions
* ∇ → symbolic state updates
* □ → symbolic environments
* Ω → symbolic privilege state
* Φ → symbolic context transitions
* Ψ → symbolic invariant constraints

Symbolic execution enables:

* path exploration
* constraint solving
* security ceiling proofs (unreachability)
* formal contract verification

---

# **11.5.7 Time Dilation & Virtual Time (Θ)**

The simulator controls Θ instead of real time:

* accelerate execution
* freeze time for debugging
* replay with different temporal orderings (non-deterministic concurrency tests)
* enforce fairness constraints as Ψ-policies

This allows:

* deterministic replay of originally nondeterministic runs
* time-travel debugging
* scheduling algorithm evaluation

---

# **11.5.8 Simulation of Multiprocessing & Isolation (Χ + Θ)**

A multi-core PMS simulator is built by:

* Representing each core as a separate Θ-thread
* Using Χ to create isolated cores or partitions
* Using Θ interleaving rules to simulate concurrent execution

Isolation semantics ensure:

* No core violates memory/frame isolation
* Shared memory accesses follow Σ + Ψ memory model rules
* Scheduled interleavings obey deterministic / nondeterministic modes

---

# **11.5.9 Trace Unification for Multi-Level Observability**

All simulators produce unified operator-tagged traces:

[
trace = \langle (o_i, t_i, meta_i) \rangle
]

UM and CPU traces merge perfectly because:

* both describe Δ–Ψ transitions
* both maintain Θ timestamps
* both record Σ commit boundaries
* both record isolation/context/role/policy state

This gives a **single, coherent observability backbone** for all layers of the system.

---

# **11.5.10 Simulator API (Minimal)**

A generic API:

```
sim = Simulator(mode="UM"|"CPU"|"Hybrid")

sim.load(program)
sim.set_initial_state(state)
sim.run(max_steps=?)
sim.step()
sim.step_until(op=Σ)
sim.inject(event)
sim.snapshot()
sim.restore(id)
sim.trace(filter?)        -- Δ, Φ, Θ, Σ, …
sim.export_trace()
sim.verify(properties)    -- uses section 11.3 verifier
```

The same API is available to:

* PMSL compilers
* Kernel tests
* Driver tests
* Network stack tests
* Model checkers
* Security/governance auditors

---

# **11.5.11 Summary**

The PMS simulation environment:

### **Unifies abstract and ISA execution**

via operator-tagged semantics.

### **Supports deterministic and nondeterministic runs**

for both correctness and adversarial exploration.

### **Provides powerful introspection**

via Θ, Σ, Ψ, Χ instrumentation.

### **Is deeply tied to verification**

via symbolic execution, path exploration, and invariant checking.

This completes the Tooling & Verification chapter.

---

# **12. Boot & Deployment**

## **12.1 Boot Sequence (Δ → … → Ψ)**

### *From bare hardware/VM image to a fully running PMS-OS kernel*

The PMS boot process is not described in terms of firmware quirks or silicon details; instead, it is a **structured ascent through the PMS operator hierarchy**.
Every stage corresponds to a well-defined operator class, building an increasingly constrained action space until the kernel invariant (Ψ) takes over.

Boot becomes a *formal Δ→…→Ψ chain*:

[
\Delta ;\Longrightarrow; \square ;\Longrightarrow; \Omega ;\Longrightarrow; \Theta ;\Longrightarrow; \nabla ;\Longrightarrow; \Chi ;\Longrightarrow; \Phi ;\Longrightarrow; \Sigma ;\Longrightarrow; \Psi.
]

We walk this in exact structural order.

---

# **12.1.1 Stage 0 — Δ: Distinguish Hardware / VM Identity**

*(Platform Bring-Up)*

The bare machine, physical or virtual, exposes only raw state.
The earliest boot code performs **Δ-distinctions**:

### Hardware identity:

* CPU type, ISA level
* Frame layout capability (paging, segmentation)
* Device presence
* Memory ranges
* Boot medium (disk, network, firmware, ROM)

### PMS-CPU identity:

* Operator availability (does CPU support Χ isolation? Σ atomics? etc.)
* Privilege modes recognized (Ω mapping)

### Boot distinctions map into a **hardware capability structure**:

[
H = \Delta(\text{cpu, mem, frames, devices, features})
]

These distinctions are not operational yet; they merely classify the substrate so later stages can reason about it.

---

# **12.1.2 Stage 1 — □: Establish Initial Frame (Boot Frame)**

*(The root execution context)*

Boot firmware sets up a **boot frame**:

[
f_0 = \square(\text{boot memory segment})
]

This is the first true PMS context:

* Code frame (where bootloader lives)
* Data frame (heap/scratch)
* Device frame (memory-mapped I/O)

The OS is not yet running; we’ve simply *bounded* the region in which early code executes.

---

# **12.1.3 Stage 2 — Ω: Enter Privileged Role (Early Kernel Mode)**

*(Assign asymmetry: privileged boot context)*

Once inside the boot frame, the machine authorizes the initial role:

[
r_0 = \Omega(\text{BootSupervisor})
]

Meaning:

* Full access to memory
* Access to frame table
* Permission to install policies later
* Ability to execute privileged opcodes

Boot is impossible without Ω: the system must clearly mark who has authority.

---

# **12.1.4 Stage 3 — Θ: Activate Temporal Semantics**

*(Initialize system clocks / scheduling epoch)*

Before performing any non-trivial ∇-operations, we must establish temporal progression:

[
m.t := 0;\quad \Theta_{\text{boot_tick}}
]

Bootloader initializes:

* CPU cycle counter
* Timer interrupts (if hardware supports)
* Boot scheduling model (single-thread sequential)

From now on, memory and IO operations have temporal order — necessary for correctness.

---

# **12.1.5 Stage 4 — ∇: Load Kernel Image into Memory**

*(State-changing impulse: constructing the live system image)*

This is the first substantial mutation stage:

[
\nabla(\text{load kernel binary into kernel frame})
]

Operations include:

* Copy kernel sections from boot medium → memory
* Initialize kernel data structures
* Allocate kernel stack
* Prepare early device tree

All ∇ actions are fully privileged (Ω) and occur within the boot frame (□).

---

# **12.1.6 Stage 5 — Χ: Establish Isolation Domains**

*(Create the separation between kernel and user, devices, and virtual subsystems)*

Once the kernel is in memory, the system must formalize isolation:

[
\Chi:
\begin{cases}
\text{Kernel domain} \
\text{User domain} \
\text{Device subcontexts} \
\text{Optional: VM partitions}
\end{cases}
]

This includes:

* Setting up MMU page tables / segmentation
* Marking kernel pages executable and user pages restricted
* Creating protected address-space frames
* Installing unreachable regions for security

Isolation is a PMS-primitive — not a late addition.

---

# **12.1.7 Stage 6 — Φ: Context Switch From Boot Context → Kernel Context**

*(Reframe the world: enter the kernel proper)*

The kernel is now loaded but not yet running as **itself**.
Φ performs the recontextualization:

[
\Phi(\text{switch from boot frame } f_0 \to f_{kernel})
]

This includes:

* Dropping BootSupervisor role
* Entering KernelSupervisor role
* Switching to kernel stack
* Switching instruction pointer to kernel entry symbol
* Installing kernel exception/trap tables

Φ is the formal transition from “bootloader environment” to “kernel environment”.

---

# **12.1.8 Stage 7 — Σ: System-Wide Integration / Commit**

*(Stabilize early state into a coherent operational baseline)*

Before services start, the system must *commit* its early configuration:

[
\Sigma_{\text{kernel_init}}
]

Meaning:

* Lock kernel memory map
* Finalize device enumeration
* Seal early kernel structures
* Transition from provisional allocation → stable runtime allocation
* Flush relocation tables

After Σ, the kernel is in its first **consistent state**.

This is the formal moment where “the kernel exists.”

---

# **12.1.9 Stage 8 — Ψ: Install Global Policies (Kernel Invariants)**

*(The final and defining step of PMS boot)*

The kernel now installs the **system’s invariants**:

[
\Psi_{\text{install}}(\text{SecurityPolicy},\ \text{SchedulingPolicy},\ \text{IsolationPolicy},\ \text{FSPolicy},\dots)
]

Typical invariants:

* User-mode cannot access kernel frames.
* Interrupt handlers must run in privileged role.
* No execution from writable pages.
* Scheduling fairness is enforced.
* Isolation between processes is mandatory.
* Kernel data structures cannot be mutated except by kernel code.

Ψ binds the system:
**after activation, not all legal PMS operator sequences remain allowed.**
The OS becomes a *governed* structure.

Many systems “boot” before Φ or Σ; PMS-OS only exists **after Ψ binds**.

---

# **12.1.10 Summary of Boot as Δ→Ψ Ascent**

| Stage | PMS Operator | Meaning                                                |
| ----- | ------------ | ------------------------------------------------------ |
| 0     | Δ            | classify hardware & boot capabilities                  |
| 1     | □            | establish boot frame                                   |
| 2     | Ω            | authorize privileged boot role                         |
| 3     | Θ            | start temporal semantics                               |
| 4     | ∇            | load kernel + mutate memory                            |
| 5     | Χ            | isolate memory + create domains                        |
| 6     | Φ            | enter kernel context                                   |
| 7     | Σ            | commit initial system state                            |
| 8     | Ψ            | install global policies → kernel becomes authoritative |

This is the **formal PMS boot sequence**.

---

# **12.2 Configuration & Policy Bootstrap**

### *How the running PMS-OS kernel absorbs configuration, establishes system-wide Ψ policies, activates Ω role structures, and initializes persistent □ frames.*

**Key principle:**
Boot (12.1) produces a *minimal, policy-capable kernel state*.
**12.2 is where the system becomes *governed*** — i.e., configured by external inputs, persistent system state, and admin-level policies.

We describe the bootstrap in strict PMS operator order.

---

# **12.2.1 Overview: Post-Boot Initialization as a Ψ-Centered Pipeline**

After Σ (kernel commit), the system is coherent but *empty of configuration*.
To become a usable OS, the kernel must **integrate config → generate roles → build policy graphs → bind invariants**.

This phase uses the core trio:

* **Δ** — load/parse configuration distinctions
* **□** — assemble configuration frames
* **Ω** — instantiate role/capability model
* **Ψ** — activate full policy model
* **Σ** — commit final system configuration

This becomes a reproducible chain:

[
Δ \to □ \to Ω \to Ψ \to Σ
]

---

# **12.2.2 Step Δ — Load & Distinguish Configuration Sources**

Configuration enters the system via **distinctions** in operator space.
Typical sources:

1. **Boot config** (kernel parameters, sysctl seeds, cmdline)
2. **System config files** (e.g., `/etc/pms/system.conf`)
3. **Policy bundles** (security, memory, scheduling, IPC)
4. **User account manifests**
5. **Module or service descriptors**

Each is parsed as Δ operations:

[
Δ_{\text{cfg}} : \text{read raw config → extract key distinctions}
]

Examples:

* `scheduler = "priority"`
* `default_user_role = "Standard"`
* `filesystem.root.label = "pms-os"`
* `networking.enable = true`

Key property:
**Δ loads configuration, but does not yet act on it.**

---

# **12.2.3 Step □ — Construct Configuration Frames**

Configuration distinctions are grouped into **frames** (contexts) so later operations reason about them consistently.

The kernel produces a structured set:

[
F_{\text{cfg}} =
{ f_{\text{system}}, f_{\text{network}}, f_{\text{security}}, f_{\text{fs}}, f_{\text{process}}, f_{\text{users}}, \dots }
]

Each frame is a □-context representing:

* **system-wide settings** (time, locale, tick rate)
* **kernel behavior** (memory layout, MMU mode, scheduling mode)
* **subsystem config** (network, storage, IPC, security)
* **identity & authentication config**

Frames give **semantic locality**.
When a module or service is initialized, it enters the relevant frame.

Example:

[
□*{\text{enter}}\big(f*{\text{security}}\big)
]

means all subsequent Ω, Ψ, Σ operations interpret configuration within the “security” context.

---

# **12.2.4 Step Ω — Instantiate Role & Capability Graph**

Once configuration frames exist, the system synthesizes the **Ω-role graph**:

[
R = Ω(\text{roles from config})
]

Examples:

* `root`, `system`, `daemon`, `user`, `nobody`
* Subsystem roles: `netd`, `fsd`, `authd`, `sched`
* Hardware roles: `driver.usb`, `driver.pci`, etc.

Ω builds:

### **(1) Capability Sets**

Mapping roles → capabilities:

* FS: read/write/exec on namespaces
* Net: bind/listen/send
* Process: fork/kill/signal
* Kernel: privileged operations allowed only to system roles

### **(2) Hierarchy / Inheritance**

Ω generates directed asymmetries:

[
root > system > daemon > user > nobody
]

### **(3) Boundary Rules**

E.g.:

* user cannot write kernel frames
* daemon cannot alter policy frames
* nobody has only read to public resources

Ω is thus the *graph-building operator* for system authority.

---

# **12.2.5 Step Ψ — Activate Policies (Invariants)**

This is the decisive phase:
**once Ψ activates system policies, the kernel becomes governed.**

Policies come from:

* static kernel policy templates
* config files
* admin-policy bundles
* module/service-supplied policies

Ψ merges them:

[
Ψ_{\text{activate}}(P_{\text{kernel}},\ P_{\text{config}},\ P_{\text{services}})
]

Ψ enforces:

### **(1) Access Control Policies**

* role → capability checks
* cross-frame access restrictions
* user isolation
* process ⇆ kernel boundary invariants

### **(2) Memory & Isolation Policies**

* allowed frame transitions
* forbidden direct writes
* sandbox behavior for processes

### **(3) Scheduling Policies**

* fairness invariants
* max CPU consumption per role
* priority ceilings/floors

### **(4) Filesystem Policies**

* write restrictions
* mount options
* namespace visibility

### **(5) Network Policies**

* allowed outbound/inbound channels
* firewall-like structural constraints
* routing rules

Ψ sets **hard global invariants** that change what operator sequences are legal.

Before Ψ:
the kernel can do nearly anything (Ω determines who may).
After Ψ:
the kernel must obey the policy lattice; illegal transitions become blocked.

---

# **12.2.6 Step Σ — Commit Configuration into Live System State**

Once Ψ completes, the configuration becomes **live and persistent**:

[
Σ_{\text{cfg_commit}}
]

Σ merges:

* configuration distinctions
* configuration frames
* role/capability graphs
* policy sets
* subsystem initial states
* kernel structures

Into a **coherent operational baseline**.

Σ also:

* finalizes subsystem initialization
* notifies services that configuration is ready
* starts user-mode or service-mode runtime

Σ is the moment the OS enters **operational normal form**.

---

# **12.2.7 Post-Bootstrap: Policy Reactivity (Φ + Ψ)**

After boot, configuration isn’t static.
The system supports **Φ-recontextualization of policy** dynamically:

* updating network config
* remounting filesystems
* rotating keys
* upgrading scheduler policies
* enabling/disabling modules

Sequence:

[
Φ(\text{updated frame}) ;\to; Ψ(\text{new invariants}) ;\to; Σ(\text{commit})
]

Φ reinterprets context, Ψ imposes new constraints, Σ stabilizes.

This is how PMS-OS supports hot reconfiguration without reboot.

---

# **12.2.8 Final Result of Configuration Bootstrap**

After Δ→□→Ω→Ψ→Σ:

The system now has:

* **bound role hierarchy**
* **active global policies**
* **stable configuration frames**
* **isolation + capability model**
* **kernel and system services initialized**
* **authoritative Ψ baseline**

---

# **12.3 Upgrade & Migration Patterns (Φ / Σ / Ψ)**

### *Dynamic system evolution through controlled recontextualization, integration, and policy rebinding.*

Upgrades and migrations are *not* ad-hoc in the PMS architecture.
They follow a strict operator-level discipline:

[
\textbf{Φ (recontextualize)} ;\to; \textbf{Ψ (bind policies)} ;\to; \textbf{Σ (commit)}
]

This triplet forms the universal **system evolution pipeline**.

Upgrades are not interruptions.
They are *structured context shifts* expressed directly through the core PMS operators.

---

# **12.3.1 Upgrade/Migration as a Φ-First Process**

The essence of Φ:

> **Φ changes the interpretation of existing state without discarding it.**

This is precisely what upgrades and migrations require.

**Examples of Φ-relevant operations:**

* switching filesystem version or metadata layout
* upgrading a kernel subsystem (scheduler, MMU mode, driver model)
* changing network protocol version
* reinterpretation of configuration formats
* migrating a persistent representation (FS, DB, policy store)
* live OS patching (hotfix, microkernel module reload)

Formally:

[
Φ_{\text{upgrade}} : (s_c, f, r, P, m) ;\mapsto; (s'_c, f', r', P', m')
]

where:

*the underlying data is preserved*,
but its **meaning, structure, or constraints** change.

Φ always prepares the system for a new semantic frame before enforcing invariants.

---

# **12.3.2 Φ – Types of Recontextualization in Upgrades**

### **(1) Frame Migration (□→□′)**

Switch from one frame structure to another:

* FS metadata format v1 → v2
* memory frame model change (e.g., from segmentation to full paging)
* VM isolation-mode switch (Χ interaction)

[
Φ_{\square}: \square_{old} \to \square_{new}
]

No mutation required yet; only interpretation changes.

---

### **(2) Schema / Layout Reinterpretation**

For persistent structures:

* inode layout v3 → v4
* network packet header reinterpretation
* process control block upgrade

Φ establishes a bridge:

[
Φ_{\text{schema}}(s_c) = \text{reinterpret}(s_c)
]

Sometimes followed by actual data migration during Σ.

---

### **(3) Version Activation**

Switching active version of:

* scheduler
* network interface driver
* authentication subsystem
* PMSL runtime

Φ loads the new version, flips a context pointer, and marks old version for retirement.

---

### **(4) Fallback / Rollback Reframes**

Failures during migration trigger:

[
Φ_{\text{fallback}} : \square_{new} \to \square_{old}
]

rollback semantics integrated with Ψ (policy check) and Σ (commit rollback).

---

# **12.3.3 Ψ – Policy Rebinding After Recontextualization**

Φ alters meaning. Ψ **enforces invariants under the new meaning**.

After Φ, the system must check:

1. **compatibility of role/capability assignments**
2. **forward-compatibility of policies** (older policies may be incompatible)
3. **security posture** of the new frame
4. **resource limits/quotas** remain valid
5. **privilege boundaries** remain correct
6. **migration-specific invariants** (e.g., “must not downgrade isolation mode”)

Thus the system executes:

[
Ψ_{\text{upgrade-check}}(P, f', s'*c) \rightarrow
\begin{cases}
\text{allow upgrade} \
\text{block upgrade} \
Φ*{\text{fallback}} + Σ_{\text{rollback}}
\end{cases}
]

Ψ acts as the **governor** of upgrades.

---

# **12.3.4 Σ – Upgrade Commit (New System Baseline)**

Once Φ shifts context and Ψ approves the change:

[
Σ_{\text{commit-upgrade}} : s' \mapsto s_{\text{new}}
]

Σ responsibilities:

### **(1) Finalize Data Migration**

If φ only reinterpreted the layout, Σ actually mutates the persistent structures:

* rewrite FS metadata
* update persistent configuration
* convert policy stores
* update thread/process tables
* flush changes to disk

### **(2) Activate New Components**

Switch to new:

* kernel modules
* device drivers
* scheduler or MMU mode
* protocol implementation
* runtime libraries

### **(3) Retire Old Structures**

Cleanup of pre-upgrade frames or versions; ensure no stale references remain.

### **(4) Notify Subsystems and Services**

Events emitted (Θ) to:

* services
* daemons
* userland
* kernel subsystems
* driver frameworks

regarding the new baseline.

After Σ, the upgrade becomes *the new system truth*.

---

# **12.3.5 Bootstrapping & Fallback Guarantees**

Upgrades must always be:

1. **Atomic** (Σ ensures indivisibility)
2. **Recoverable** (Φ rollback paths)
3. **Policy-consistent** (Ψ approval required)

Sequence:

[
Φ_{\text{prepare}} \to Ψ_{\text{validate}} \to Σ_{\text{commit}}
]

Failure-safe via:

[
Ψ_{\text{fail}} \Rightarrow Φ_{\text{fallback}} \Rightarrow Σ_{\text{rollback}}
]

This makes upgrades and migrations inherently *safe*, *auditable*, and *policy-bound*.

---

# **12.3.6 Hot vs Cold Upgrades (Both Are Natural)**

### **Cold Upgrade** (reboot between versions)

* Φ reconstructs state from persistent frames
* Ψ ensures new kernel is compatible
* Σ commits new baseline
* Most components restart

### **Hot Upgrade** (in-place, live migration)

* Φ swaps live module contexts
* Ψ verifies invariants on live processes
* Σ commits incremental changes
* No reboot required
* PMS structure is particularly strong here because Φ cleanly separates meaning from data

---

# **12.3.7 Distributed / Multi-Node Migration (Optional)**

When PMS-OS runs on multiple nodes:

* Φ coordinates frame reinterpretation across nodes
* Ψ verifies cluster-wide invariants (e.g. no partitioning of capability graph)
* Σ commits consistent global state

Later, in “Optional: multi-node boot/orchestration”, this becomes a full model.

---

# **12.3.8 Summary of PMS Upgrade/Migration Logic**

### **Upgrades are Φ-Ψ-Σ sequences:**

1. **Φ** — *Recontextualize* state

   * new frame
   * new interpretation
   * new version
   * rollback path established

2. **Ψ** — *Validate and bind policies*

   * ensure safety
   * ensure compatibility
   * allow/deny transition

3. **Σ** — *Integrate & commit*

   * finalize migration
   * activate new system baseline
   * retire old context
   * issue subsystem notifications

---

# **12.4 Multi-Node / Cluster Boot & Orchestration (Optional)**

### *Distributed PMS-OS initialization through Δ → □ → Ω → Ψ → Σ across multiple nodes and shared policy domains.*

A multi-node PMS system is **not** a special case added on top of the OS.
It is simply PMS operators applied to *multiple machine-roots* whose frames, roles, and policies are synchronized.

The same operator grammar—Δ, □, Ω, Θ, Φ, Χ, Σ, Ψ—scales without modification.

---

# **12.4.1 Conceptual Model: A Cluster as a Higher-Order Frame (□ᴳ)**

A cluster is represented as a **global frame**:

[
□^{G} = \text{Frame}( \text{nodes}, \text{topology}, \text{shared policy domain}, \text{capabilities} )
]

Each node *Nᵢ* has its own:

* core state (s_cᵢ)
* role set (rᵢ)
* policy set (Pᵢ)
* meta (mᵢ)
* isolation boundaries (Χᵢ)
* local frames (□ᵢ)

Cluster orchestration adds:

* **inter-node Δ** (distinctions: node identity, readiness, capabilities)
* **global □ᴳ** (cluster config, placement, topology)
* **global Ωᴳ** (cluster-level roles/capabilities)
* **distributed Ψᴳ** (global invariants)
* **distributed Σᴳ** (cluster-wide commit/logical consistency)

This mirrors single-node boot, but *lifted* to the cluster level.

---

# **12.4.2 Δ — Distinguish Nodes, Identity, and Capabilities**

Cluster boot begins with a discovery wave:

[
Δ_{\text{discover}}(N_1, N_2, \dots, N_k)
]

Performed via:

* network beacons
* registry queries
* fixed topology lists
* out-of-band control channels

Each node self-advertises:

* **node-ID**
* hardware capabilities
* available storage
* roles it can serve (Ω)
* version information for drivers, kernel modules, PMSL runtime

All this is represented as Δ distinctions.

Δ does **not** connect nodes — it only maps them.

---

# **12.4.3 □ — Build Cluster Frames (Topology, Shards, Services)**

Next, Δ outputs are arranged into structured frames:

### **Cluster frames:**

* **□ᴳ.topology** — cluster graph (edges, latency classes, partitions)
* **□ᴳ.services** — service placement frame
* **□ᴳ.storage** — global namespace for volumes
* **□ᴳ.security** — identity domains and trust anchors
* **□ᴳ.runtime** — task distribution, scheduling domains
* **□ᴳ.failure-zones** — fault-containment groups

Each node contributes a local □ᵢ, integrated into □ᴳ through:

[
□_{\text{integrate}} : □_i \hookrightarrow □^G
]

This creates the structural *context* for distributed operation.

---

# **12.4.4 Ω — Establish Cluster Roles & Capabilities**

The cluster defines node-level and global roles.

### **Node-level roles include:**

* storage-node
* compute-node
* network-node
* controller-node
* auth-node
* gateway-node

Each has asymmetries:

[
\Omega_{node}(N_i)
]

assigning capabilities such as:

* allowed to host volumes
* allowed to route traffic
* allowed to execute distributed sched decisions
* allowed to issue distributed Ψ policies
* allowed to participate in consensus

### **Cluster-level roles (Ωᴳ):**

* **orchestrator** (global controller)
* **consensus-node** (voter, log-replicator)
* **coordination-node** (barrier, lock-service)
* **observer**

Ωᴳ ensures:

* each role is uniquely placed or sharded
* access to shared frames is asymmetrically regulated
* no node performs actions outside its capability envelope

---

# **12.4.5 Ψ — Global Policies, Invariants, and Consensus**

Ψ is the *heart* of cluster orchestration.

Cluster-wide Ψ includes:

### **(1) Membership Policy**

Defines conditions for:

* joining
* leaving
* eviction
* quarantine
* recovery

[
Ψ_{\text{membership}} : N_i \to {\text{allowed},\text{blocked}}
]

### **(2) Resource Policy**

Invariant constraints across the cluster:

* max volume replicas
* CPU/memory limits
* load distribution shape
* global quotas

### **(3) Security Policy**

Cluster trust anchors, identity domains:

* certificate binding
* allowed key-exchange modes
* isolation boundaries across nodes (Χᴳ)
* cluster-wide privilege invariants

### **(4) Consensus Policy (Ψᴳ.consensus)**

Defines:

* quorum requirements
* election rules
* log consistency guarantees
* commit semantics (Σᴳ)

Ψ enforces that **any transition that would violate global invariants is illegal**, even if locally valid.

---

# **12.4.6 Σ — Distributed Commit (Σᴳ)**

Cluster-wide Σ is a **multi-node integration step**:

[
Σ^G : (s_1,\dots,s_k) \mapsto (s_1',\dots,s_k')
]

using:

* **consensus** for logically shared state
* **barriers** for synchronization
* **two-phase (or PMS-native) commit** for distributed transactions
* **global sequence numbers (Θᴳ)** for ordering

Σᴳ ensures:

* consistent filesystem namespace
* synchronized service topology
* policy invariants persist across the cluster
* upgrades/migrations finish atomically across nodes
* no split-brain states persist

A global commit is performed only when:

[
Ψ_{\text{global}}(all\ nodes) = \text{true}
]

Σᴳ is thus the distributed version of Σ: cluster-level *finalization*.

---

# **12.4.7 Φ — Distributed Recontextualization (Upgrades, Failover, Rebalancing)**

Φ handles:

### **(1) Versioned Failover**

Node failure triggers:

[
Φ_{\text{failover}} : □^G \to □^G_{\text{degraded}}
]

This reinterprets cluster topology without modifying data.

### **(2) Rolling Upgrades**

Version transitions:

[
Φ_{\text{upgrade}}(N_i) : f_i \to f_{i,\text{new}}
]

Θ sequences orchestrate rollout order.

### **(3) Sharding / Resharding**

Move responsibilities:

[
Φ_{\text{reshard}} : (□^G.\text{services}) \to (□^G.\text{services}')
]

Then Σᴳ finalizes the reassignment.

### **(4) Network Reinterpretation / Route Migration**

Topology changes and route re-evaluation.

---

# **12.4.8 Θ — Distributed Temporal Coordination**

Cluster time is a **Θᵍ progression domain**:

* tick propagation
* drift compensation
* event ordering
* distributed timers
* heartbeat semantics
* timeouts for Λ events

Θᵍ ensures globally-consistent ordering for:

* consensus logs
* replicated state machines
* clusterwide Σ commits
* distributed scheduling
* multi-node upgrades (Φ)

---

# **12.4.9 Χ — Cross-Node Isolation Domains**

Distributed isolation types:

### **(1) Fault Domains**

Χ separates power zones, racks, AZs.

### **(2) Security Domains**

Cluster RBAC boundaries enforced across nodes.

### **(3) Workload Isolation**

Tenant separation at cluster level.

Χᵍ ensures:

* failure propagation is controlled
* security roles remain local unless explicitly exported
* workloads can be contained

---

# **12.4.10 Full Multi-Node Boot Sequence Summary**

The cluster boot pipeline:

[
Δ^G \to □^G \to Ω^G \to Ψ^G \to Σ^G
]

**Step Summary:**

1. **Δᴳ** — discover nodes, distinguish capabilities
2. **□ᴳ** — build global cluster context
3. **Ωᴳ** — assign global roles, capabilities, responsibilities
4. **Ψᴳ** — enforce cluster-wide invariants
5. **Σᴳ** — commit cluster baseline
6. (optional) **Φ** for upgrades, failure reframes, topology changes
7. **Θᵍ** — coordinate time across nodes
8. **Χᵍ** — enforce distributed isolation

After Σᴳ:
**Cluster reaches operational normal form.**

---

# **13. Finalization & Spec Epilogue**

### *Unifying Statement, Guarantees, and Canonical Closure of the PMS-IT Architecture*

The preceding sections (0–12) define a **complete, axiomatic, layered IT architecture** whose foundation is the 11 PMS operators (Δ, ∇, □, Λ, Α, Ω, Θ, Φ, Χ, Σ, Ψ).
This final section closes the specification by:

1. Unifying the layers into a single coherent architecture,
2. Stating formal guarantees achieved by the PMS model,
3. Defining completeness conditions,
4. Defining extensibility conditions,
5. Stating equivalence to classical computational, OS, and distributed models,
6. Marking the specification as internally consistent and closed.

This section is intentionally short and definitive.

---

# **13.1 Unified Stack Overview (Top-to-Bottom)**

Across sections 0–12, PMS-IT establishes a full architecture:

```
PMS Operators (Δ–Ψ)
    ↓
Monoid + Dependency System (0.3)
    ↓
PMS-UM (Universal Machine, 1.x)
    ↓
PMS-CPU (Virtual Hardware, 2.x)
    ↓
PMS-OS Kernel (3.x)
    ↓
Memory, Storage (4.x)
    ↓
IPC, Events, Devices (5–6)
    ↓
Networking Stack (7.x)
    ↓
Security & Governance (8.x)
    ↓
PMSL Language & Runtime (9–10)
    ↓
Tooling, Verification, Simulation (11.x)
    ↓
Boot & Deployment (12.x)
```

These layers are **not** independent modules but **structured projections** of the same operator algebra.

Every IT-layer behaves as a *restricted PMS-UM instance*.

---

# **13.2 What Has Been Proven / Established**

The spec establishes:

## **(1) A Universal Operational Semantics**

Every IT mechanism – CPU instruction, syscall, trap, message, filesystem operation, network exchange – is representable as a PMS operator sequence respecting the dependency grammar.

This gives the system:

* **semantic uniformity**,
* **formal analyzability**,
* **provable invariants**,
* **safe extensibility**.

## **(2) Turing-Completeness**

Section 1.3 gives a constructive embedding of deterministic Turing Machines into PMS-UM.
Therefore:

[
\text{PMS-UM is Turing-complete.}
]

## **(3) A Unified Model for Hardware, OS, Language, Network, Security**

Instead of separate conceptual frameworks (ISA, kernel design, protocol stack, RBAC, etc.), PMS-IT shows:

[
\text{All IT constructs reduce to controlled compositions of } {\Delta,\nabla,\square,\Lambda,\mathrm A, \Omega,\Theta,\Phi,\Chi,\Sigma,\Psi}.
]

Each IT-level construct is simply **a structural special case**.

## **(4) Deterministic and Non-Deterministic Execution as Structural Modes**

PMS explicitly encodes:

* deterministic machines,
* non-deterministic machines,
* environment-driven systems,
* concurrent interleavings,
* distributed consensus systems.

All follow the same reduction semantics.

## **(5) A Unified Security Model**

Identity → Roles → Capabilities → Policies → Commit
is structurally:

[
Δ \to Ω \to Ψ \to Σ
]

Security emerges as **operator ordering**, not bolted-on rules.

## **(6) A Complete Systems Architecture**

Sections 2–12 collectively define a full operating system:

* PMS-CPU (machine)
* PMS-OS Kernel (supervisor)
* Memory, storage, IPC, drivers
* Networking stack
* Security & governance
* Language and runtime
* Verification tools
* Boot and cluster orchestration

All grounded in PMS-UM.

---

# **13.3 Completeness Conditions**

The specification is **complete** when:

1. **All PMS operators have explicit ISA-level representatives**.
   (Done: 2.2)

2. **All OS-level mechanisms map to operator sequences**.
   (Done: sections 3–6)

3. **Language constructs map cleanly to CPU operations via PMSL → IR → ISA**.
   (Done: 9.1–9.7, 10.x)

4. **Global invariants Ψ are definable at all layers**.
   (Done: 3.1, 8.3, 12.x)

5. **Σ commits define clear integration semantics** for:

   * memory operations,
   * IPC,
   * filesystem,
   * transactions,
   * distributed consensus.
     (Done: 2.2.11, 3.8, 4.5, 7.5, 12.3)

6. **Boot produces a normal-form operational cluster state**.
   (Done: 12.1–12.4)

These six conditions ensure the framework is self-contained.

---

# **13.4 Extensibility Conditions**

New features can be added **only** if:

1. They reduce to sequences of the 11 operators,
2. They obey dependency constraints (section 0.3),
3. They do not require new primitive operators,
4. Any new instruction or system behavior fits cleanly into:

   * Δ for distinctions,
   * ∇ for mutations,
   * □ for contexts,
   * Λ for absence-handling,
   * Α for patterns,
   * Ω for role asymmetry,
   * Θ for ordering/time,
   * Φ for recontextualization,
   * Χ for isolation,
   * Σ for integration,
   * Ψ for invariants.

If a proposed mechanism cannot be expressed using this operator algebra, the mechanism is *not part of PMS-IT*.

This guarantees long-term stability and prevents architectural drift.

---

# **13.5 Equivalences to Classical Frameworks**

PMS-IT is sufficient to express:

### **Classical Computation**

* deterministic Turing machines
* nondeterministic Turing machines
* λ-calculus
* register machines
* pushdown automata
* actor models

### **Classical OS Theory**

* POSIX-like process model
* capabilities systems
* microkernels
* monolithic kernels
* virtualization

### **Distributed Systems**

* Paxos / Raft
* CRDTs
* state-machine replication
* eventual consistency
* strong consistency
* leader election

### **Language Theory**

* imperative
* functional
* capability-secured
* transactional languages

PMS operators are *orthogonal primitives*: these classical models appear as **specializations**, not additions.

---

# **13.6 Canonical Closure: The PMS Normal Form of Computation**

We can now define the **PMS Normal Form**:

[
w = \Delta^{*} ; \Omega^{*} ; \square^{*} ; (\Theta^{*} \nabla^{*} \Lambda^{*} \Phi^{*} \Chi^{*})^{*} ; \Sigma^{*} ; \Psi^{*}
]

with the dependency constraints from 0.3.

Every legitimate PMS-IT execution—from hardware fetch/decode to cluster-wide distributed commit—reduces to such sequences.

This is the **canonical form** of all computation in the PMS-IT system.

---

# **13.7 Epilogue Statement**

**PMS-IT is now a complete, unified, formally grounded, implementation-ready systems architecture.**

It provides:

* a universal operational semantics (PMS-UM),
* a full CPU model (PMS-CPU),
* a complete OS (PMS-OS),
* networking, IPC, FS, memory, scheduling subsystems,
* a programming language (PMSL),
* runtime and libraries,
* debugging, verification, modeling tools,
* boot and distributed orchestration models,
* a unified security and governance system,
* and a strict algebraic foundation based on PMS operators.

The specification is **closed, consistent, and internally complete**.

From here, the next steps are:

* **reference implementation**,
* **compiler pipeline**,
* **kernel prototype**,
* **distributed runtime**,
* **formal verification suite**,
* **standard library definition expansion**,
* **release and documentation generation**.

But architecturally and semantically, **the PMS-IT specification is finished**.

