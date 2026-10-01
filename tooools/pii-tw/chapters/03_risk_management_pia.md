# Chapter 03: Risk Assessment, Threat Modeling & Privacy Impact Assessment (PIA)

## 1. Statutory Baseline & Risk Engineering Framework
- **PDPA Enforcement Rules Art 12 Para 2 Item 3**: Mandatory establishment of risk assessment and management mechanisms for personal data assets.
- **Privacy & Risk Engineering Framework**: Risk Governance Domain 2 (IT Risk Assessment) & Privacy Engineering Domain 3 (Privacy Risk Management / PIA).

### 1.1 Standard 3-Stage Risk Assessment Methodology
```
┌─────────────────────────┐     ┌───────────────────────┐     ┌────────────────────────┐
│ 1. Risk Identification  │ ──> │   2. Risk Analysis    │ ──> │   3. Risk Evaluation   │
│ (DFD / Assets / Threats)│     │(Quantitative/Qual)    │     │ (Appetite Comparison)  │
└─────────────────────────┘     └───────────────────────┘     └───────────┬────────────┘
                                                                          │
                                                              ┌───────────▼────────────┐
                                                              │ 4. Risk Treatment Plan │
                                                              │(Mitigate/Transfer/...) │
                                                              └────────────────────────┘
```

1. **Risk Identification**: Systematically identify personal data assets, processing operations, legal grounds, and threat vectors across Data Flow Diagrams (DFD).
2. **Risk Analysis**: Quantify likelihood ($L$) and impact severity ($I$) to compute overall risk score: $Risk = L \times I$. Evaluates financial, reputational, operational, and data subject harm dimensions.
3. **Risk Evaluation**: Compare analyzed risk scores directly against Board-approved Risk Appetite thresholds to determine whether risk acceptance is permissible or treatment is mandatory.

### 1.2 Risk State Classification Matrix
- **Inherent Risk (Raw Risk)**: The baseline risk level existing in the absence of any technical or operational security controls.
- **Residual Risk (Post-Control Risk)**: The remaining risk level after deploying security and privacy controls ($Residual\ Risk = Inherent\ Risk - Control\ Effectiveness$).
- **Current Risk (Operational Risk Snapshot)**: The actual risk level at a specific point in time, accounting for active control degradation, patch latency, and operational anomalies.

### 1.3 LINDDUN Privacy Threat Modeling Framework
| Threat Dimension | Privacy Concern & Attack Vector | Engineering Countermeasure |
| :--- | :--- | :--- |
| **Linkability** | An attacker links two separate data items to infer they relate to the same data subject. | Ephemeral pseudonymization, K-Anonymity ($k \ge 5$), differential noise injection. |
| **Identifiability** | An attacker identifies a single individual from quasi-identifiers within a dataset. | Suppression of direct identifiers, coarse generalization (e.g. year of birth instead of full date). |
| **Non-Repudiation** | An individual cannot deny having performed an action when plausible deniability was expected. | Zero-Knowledge Proofs (ZKP), blinded signatures, ephemeral transaction identifiers. |
| **Detectability** | An attacker detects the presence or absence of an entity's data record in a database. | Dummy record padding, Differential Privacy ($\epsilon, \delta$), oblivious RAM protocols. |
| **Disclosure** | Unauthorized disclosure of sensitive attributes through query side-channels. | Application-layer envelope encryption, Dynamic Data Masking (DDM), Purpose-Based Access Control. |
| **Unawareness** | The user remains unaware of invisible background tracking or secondary data usage. | Granular Consent Management Platform (CMP), contextual just-in-time privacy notices. |
| **Non-Compliance** | System processing violates statutory regulations, consent scopes, or DPA contracts. | Automated CI/CD compliance gating, continuous audit logging to immutable WORM storage. |

### 1.4 4 Risk Treatment Strategies
| Treatment Option | Operational Definition | Production Architecture Example |
| :--- | :--- | :--- |
| **Mitigate** | Implement technical or architectural controls to reduce risk likelihood or impact. | Enforce AES-256 field-level encryption, multi-tenant Row-Level Security, FIDO2 MFA. |
| **Transfer** | Shift financial or operational loss exposure to an external third party or underwriter. | Procure cyber liability insurance, outsource payment card processing to PCI-DSS Level 1 vendors. |
| **Avoid** | Terminate the high-risk activity, pipeline, or architectural dependency entirely. | Eliminate non-essential sensitive PII collection, terminate risky third-party marketing SDKs. |
| **Accept** | Formally retain the residual risk when within Board-approved risk appetite limits. | Low-impact non-sensitive metadata, formally documented and signed off by executive leadership. |

---

## 2. Production Scenario: Open Banking Third-Party API Integration
- **Incident Overview**: A commercial bank planned an Open Banking integration allowing third-party fintech applications to pull customer financial transaction histories.
- **PIA Findings**: Inherent risk was critical due to third-party lack of MFA and potential data linkage attacks; calculated residual risk significantly exceeded the bank's approved risk appetite.
- **Remediation Architecture**:
  1. Rejected unconditional risk acceptance.
  2. Applied hybrid treatment: Avoided transmitting national IDs; Mitigated transaction linkage by issuing ephemeral pseudo-tokens via KMS.
  3. Executed legally binding Data Processing Agreements (DPA) with mandatory third-party audit rights. Residual risk fell within approved appetite.

---

## 3. Scenario Practice & Decision Forensics (Q&A) & Distractor Forensics

### Q1 `[Privacy Engineering - PRIMARY]`
Following a comprehensive Privacy Impact Assessment (PIA), what is the PRIMARY basis for determining whether additional controls must be implemented?
- A. Whether the latest commercial security software packages have been procured
- B. Whether residual risk exceeds the organization's approved risk appetite
- C. Total financial cost proposed by third-party implementation vendors
- D. Whether industry competitors have experienced recent privacy enforcement actions

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In enterprise risk governance, the fundamental decision criterion for risk treatment is comparing residual risk against approved risk appetite.
> - **Why A is Incorrect**: Control selection must be risk-driven rather than motivated by technological novelty.
> - **Why C is Incorrect**: While cost-benefit analysis informs control selection, budget alone does not determine the necessity of risk treatment.
> - **Why D is Incorrect**: Competitor actions provide threat intelligence context, not organizational risk thresholds.

### Q2 `[Privacy Engineering - BEST]`
During system architecture design, which structured methodology is BEST suited for identifying privacy threats such as linkability, identifiability, and non-repudiation in Data Flow Diagrams?
- A. STRIDE Threat Modeling
- B. LINDDUN Privacy Threat Modeling
- C. Automated Network Vulnerability Scanning
- D. Static Application Security Testing (SAST)

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: LINDDUN is the internationally recognized engineering methodology specifically formulated for privacy threat modeling on Data Flow Diagrams.
> - **Why A is Incorrect**: STRIDE targets information security threats (Spoofing, Tampering, etc.) rather than privacy properties.
> - **Why C and D are Incorrect**: Vulnerability scanning and SAST are code-level and network-level security testing tools, not architectural threat modeling methodologies.

### Q3 `[Privacy Engineering - FIRST]`
What is the FIRST step a risk engineering team must perform when conducting an information asset risk assessment?
- A. Select and deploy field-level cryptographic controls
- B. Identify and catalogue information assets along with their respective business owners
- C. Purchase cyber breach liability insurance policies
- D. Calculate annualized loss expectancy (ALE) values

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: An assessment cannot evaluate threats or vulnerabilities without first identifying and scoping the assets at risk (FIRST step).
> - **Why A is Incorrect**: Control implementation occurs during the risk treatment phase, downstream from assessment.
> - **Why C is Incorrect**: Insurance procurement represents a risk transfer decision made after risk evaluation.
> - **Why D is Incorrect**: Quantitative calculation requires asset valuation established during initial asset identification.

### Q4 `[Privacy Engineering - EXCEPT]`
Which condition makes the formal acceptance of an identified privacy risk INVALID under enterprise risk management standards?
- A. The calculated residual risk exceeds the organization's maximum risk tolerance limit
- B. The asset owner has formally signed the risk acceptance documentation
- C. The risk has been entered into the centralized enterprise risk register with a review date
- D. Compensating controls have been evaluated and determined to be cost-prohibitive

> **[Correct Answer] A**
> **[Distractor Forensics]**
> - **Why A is Correct**: An organization cannot lawfully or prudently accept a risk that breaches its maximum risk tolerance or legal capacity limits, making acceptance invalid.
> - **Why B, C, D are Incorrect**: Documented sign-off, risk register tracking, and cost-prohibitive control evaluations are standard elements of valid risk acceptance workflows.
