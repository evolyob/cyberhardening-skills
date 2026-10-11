# AI Threat Defense Playbook (Operational Detection & Mitigation)

## 1. Core Threat Matrix & Mitigation Recipes

| Threat Vector | Root Cause & Legal Risk | Telemetry & Detection Method | Actionable Engineering Defense |
| :--- | :--- | :--- | :--- |
| **Confidential Record Leakage** | Executive Yuan GenAI Guidelines Art. 5 (PII / State secrets in prompt) | Outbound proxy DLP regex scanner + tokenized PII classifier | Input firewall blocks prompts with citizen ID, tax, or medical records; substitutes with synthetic tokens. |
| **Prompt Injection & Jailbreak** | Untrusted user input overriding system instructions | AST prompt containment filter + SemGrep pattern scanner | Isolate system instructions in immutable system roles; strip user `<system>` delimiters. |
| **Training Corpus Poisoning** | Malicious injection into fine-tuning datasets | Cryptographic SHA-256 dataset hash verification | Pin dataset hashes in DVC/Git LFS; reject unverified web scrapes without digital signatures. |
| **Model Hallucination & Drift** | Stochastic token generation; production feature shifts | EvidentlyAI / Prometheus tracking PSI (> 0.2) and Ragas confidence | Enforce RAG with verified vector embeddings; reject outputs with confidence < 0.85. |
| **Third-Party API Dependency** | Upstream provider outage or rate-limiting | Endpoint health probes tracking HTTP 429/503 error rates | Configure automated fallback to secondary on-premise model with circuit breakers. |

---

## 2. CLI Fast Verification Shortcuts

```bash
# Query verification controls in Annex A.9
python3 scripts/query.py --filter "A.9" --format markdown

# Query data sanitization controls in Annex A.7
python3 scripts/query.py --filter "A.7" --format markdown
```

---

## 3. Incident Response SOP for AI Failures

1. **Containment**: Isolate affected endpoint; route inference traffic to fallback deterministic rule engine.
2. **Telemetry Dump**: Extract raw prompt, model output hash, temperature, and timestamp into `incident/ai_postmortem.json`.
3. **Retraining / Policy Patch**: Patch prompt fence or roll back model weights to last validated checkpoint.
