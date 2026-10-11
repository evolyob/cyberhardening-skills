# AI System Impact Assessment (AIA) & Risk Classification Guide

## 1. Global AI Risk Tiering Framework (EU AI Act & NIST, Aligned with CNS 42001 A.5)

Evaluate AI systems prior to production deployment against global risk severity tiers (derived from EU AI Act / NIST AI RMF, aligned with CNS 42001 Annex A.5 & Executive Yuan Guidelines):

| Risk Tier | Criteria & System Archetypes | Mandatory Compliance & Governance Controls |
| :--- | :--- | :--- |
| **Tier 1: Prohibited (Unacceptable)** | Social scoring, real-time biometric mass surveillance, deceptive subliminal manipulation. | **Absolute Rejection**: Project termination; prohibited from public/enterprise deployment. |
| **Tier 2: High Impact / High Risk** | Autonomous administrative decision-making, critical infrastructure control, recruitment/credit scoring, healthcare CADx. | **Full AIA Mandate**: Quantitative bias testing, independent human-in-the-loop fallback, continuous drift monitoring, formal executive sign-off. |
| **Tier 3: Limited / Moderate Risk** | Customer service chatbots, generative content drafting, internal document translation/summarization. | **Transparency Mandate**: Mandatory user disclosure banner (`A.8.2`), output watermarking, prompt injection guardrails. |
| **Tier 4: Minimal / Low Risk** | Spam filters, internal code syntax linters, mathematical optimization without personal data. | **Baseline InfoSec**: Standard ISO 27002 operational controls; no formal AIA documentation required. |

---

## 2. 4-Dimension AIA Evaluation Matrix & Recommended Metrics

> *Note: Numerical thresholds below represent industry best-practice heuristics (e.g., NIST AI RMF, IEEE 7000) rather than rigid ISO 42001 statutory clauses.*

| Assessment Dimension | Concrete Threat / Negative Harm | Recommended Engineering Metric (Heuristic) | Actionable Engineering Defense |
| :--- | :--- | :--- | :--- |
| **1. Individual Rights & Privacy** | Unauthorized PII ingestion, automated denial of public services | Tokenized PII scan error rate = 0; Zero citizen identity records in training corpus | Inbound DLP proxy; differential privacy ($\epsilon \le 3.0$ recommended); synthetic data substitution. |
| **2. Group Fairness & Non-Discrimination** | Algorithmic disparate impact on protected demographic cohorts | Disparate Impact Ratio (DIR) guideline: $0.80 \le \text{DIR} \le 1.25$ | Re-weight training samples; apply adversarial debiasing layers during model training. |
| **3. Human Autonomy & Safety** | Unchecked automated execution without human oversight | Human override latency $\le 500\text{ms}$; 100% of high-impact actions require explicit confirmation | Hard Human-in-the-loop (HITL) approval gate; immutable dual-operator sign-off. |
| **4. Societal & Systemic Impact** | Mass disinformation generation, critical utility service disruption | Target benchmark hallucination rate $\le 3\%$; Ragas groundedness score $\ge 0.85$ | Grounding verification via verified vector embeddings; automated circuit breaker on model failure. |

---

## 3. Event-Driven Re-Assessment Triggers

An existing AIA becomes invalid and MUST be re-executed under any of the following events:

1. **Scope Expansion**: Model deployed to new demographic groups or unvetted operational domains.
2. **Corpus Shift**: Ingestion of new data classes, external scrapings, or third-party foundation model version upgrades.
3. **Telemetry Anomaly**: Significant drift in production Population Stability Index ($\text{PSI} > 0.20$ recommended threshold) or accuracy decay.

---

## 4. Fast CLI Query for AIA Controls

```bash
# Query Annex A.5 Impact Assessment controls
python3 scripts/query.py --filter "A.5" --format markdown

# Query Bias & Data Quality controls (A.7.3)
python3 scripts/query.py --filter "A.7.3" --format markdown
```
