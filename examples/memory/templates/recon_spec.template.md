# Reverse Reconstruction & Verification Contract: [Feature Name]

> **Status**: `DRAFT` | `VERIFIED` | `FROZEN`  
> **Laws**:  
> 1. **Inherits `spec_template.md`**: Enforces *No-Spec-No-Code*, *Measure-Not-Assert*, and *Empirical Verification*.  
> 2. **No-Guessing-No-Assumption**: Every structural claim must cite an observed `Evidence ID` or be explicitly quarantined in Section 2.2 `Unknowns Registry`.  
> 3. **Clean-Room Boundary**: Extract architecture skeletons (state machines, schemas, boundaries) only. Implementation stage reads Sections 3 & 4 only; never copy proprietary raw source or binary blobs.  
> 4. **Behavioral Parity Gate**: Reconstruction is complete only when measured outputs match target baseline fixtures.

---

## 1. Target Metadata & Boundary Perimeter
- **Target Identifier**: [Application name, binary, or package version]
- **Analysis Engine**: [e.g. REA / Hopper / Ghidra / AST Parser / Runtime Trace]
- **Target Boundaries**:
  - Ingress: [API / IPC Channel / UI Event]
  - Egress: [File Write / Network Request / IPC Response]

---

## 2. Evidence Trace & Unknowns Registry

### 2.1 Verified Evidence Ledger
| Evidence ID | Source Artifact / Symbol | Observed Fact / Behavior |
| :--- | :--- | :--- |
| `EVD-001` | [artifact:location or symbol] | [Observed factual behavior] |
| `EVD-002` | [artifact:location or symbol] | [Observed factual behavior] |

### 2.2 Unknowns Registry (Quarantined Assumptions)
*Unresolved questions that must NOT be guessed. Must remain abstract interfaces until evidenced.*
- [ ] `UNK-001`: [Unverified edge-case or internal policy] -> *Design Fallback: [Declared fallback rule]*

---

## 3. Abstract Architecture Skeleton

### 3.1 Data Contract & Interface (Protocol / Types Only)
```
// Language-neutral or target-language interface (Input/Output contract)
Interface TargetPayload:
  field_a: string
  field_b: number

Interface TargetResponse:
  status: enum
  data: list[item]
```

### 3.2 State Machine & Transition Topology
```
[State: Idle] ──(Trigger Event)──► [State: Processing]
                                          │
                   ┌──────────────────────┴──────────────────────┐
                   ▼                                             ▼
          [State: Success]                              [State: Error]
```

---

## 4. Behavioral Parity Verification Matrix

- **Deterministic Verification Command**:
  ```bash
  [command to run parity test suite, e.g., pytest tests/test_parity.py]
  ```

| Case ID | Input Fixture | Target Baseline (Observed) | Reconstructed (Measured Output) | Parity Status |
| :--- | :--- | :--- | :--- | :--- |
| `TC-01` | `[Input payload 1]` | `[Observed baseline 1]` | `[Measured output 1]` | `PENDING` |
| `TC-02` | `[Input payload 2]` | `[Observed baseline 2]` | `[Measured output 2]` | `PENDING` |
| `TC-03` | `[Edge case input]` | `[Observed edge behavior]` | `[Measured edge behavior]` | `PENDING` |

---

## 5. Implementation Gates (Applying `senior_coding_laws.md`)
- [ ] **Pure Core**: Core transformation isolated as pure deterministic functions without side effects.
- [ ] **Boundary Isolation**: Third-party SDKs, native I/O, or IPC decoupled behind structural protocols / interfaces.
- [ ] **Zero Wrapper Bloat**: Zero unnecessary single-caller wrappers; flat control flow (nesting depth <= 2).
- [ ] **100% Parity Verified**: All test cases in Section 4 pass with deterministic commands (`OK`).
