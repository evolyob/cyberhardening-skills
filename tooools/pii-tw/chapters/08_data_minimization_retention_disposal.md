# Chapter 08: Data Minimization, Automated Retention & Secure Disposal

## 1. Statutory Baseline & Sanitization Engineering
- **PDPA Statutory Article 11 Para 3**: Mandatory erasure or cessation of collection, processing, and use upon expiration of retention periods or fulfillment of specific purpose.
- **PDPA Enforcement Rules Art 12 Para 2 Item 2**: Mandatory definition of personal data scope and retention schedules.
- **ISACA CRISC / CDPSE Mapping**: Data Minimization, Media Sanitization (NIST SP 800-88), Crypto-Shredding & Anonymization Engineering.

### 1.1 De-Identification & Mathematical Privacy Models
| Privacy Model | Mathematical Definition & Standard | Defense Against Attack Vectors |
| :--- | :--- | :--- |
| **K-Anonymity** | In a dataset $T$, each quasi-identifier tuple occurs at least $k$ times ($k \ge 5$). | Prevents identity linkage attacks using external voter/demographic registries. |
| **L-Diversity** | Each equivalence class of size $\ge k$ contains at least $l$ well-represented distinct values ($l \ge 3$) for each sensitive attribute. | Prevents homogeneity attacks and background knowledge attribute disclosure. |
| **T-Closeness** | The distance between the distribution of a sensitive attribute in an equivalence class and the whole table is $\le t$ ($t \le 0.15$). | Prevents probabilistic skewness and semantic inference attacks. |
| **Differential Privacy** | An algorithm $\mathcal{M}$ satisfies $\epsilon$-DP if $\Pr[\mathcal{M}(D) \in S] \le e^\epsilon \Pr[\mathcal{M}(D') \in S]$ for neighboring datasets $D, D'$. | Mathematically bounds individual identification risk independent of auxiliary background data. |

### 1.2 NIST SP 800-88 Rev 1 Media Sanitization Standards
```
┌─────────────────────────────────────────────────────────────┐
│ 1. Clear: Logical overwrite with pseudo-random byte patterns │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ 2. Purge: Firmware Secure Erase / Magnetic Degaussing        │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ 3. Destroy: Physical Disintegration, Incineration, Shredding │
└─────────────────────────────────────────────────────────────┘
```

- **Crypto-Shredding Architecture**:
  1. Each tenant or dataset is encrypted with a dedicated Data Encryption Key (DEK).
  2. DEKs are managed centrally in a Hardware Security Module (KMS/HSM).
  3. Upon retention expiration, the dedicated DEK is permanently destroyed from the HSM. Ciphertext stored in backups and distributed nodes becomes mathematically irrecoverable.

---

## 2. Production Scenario: Data Lake Retention Breach & Anonymization Pipeline
- **Incident Overview**: An enterprise retail data lake stored unmasked transaction records, customer credit scores, and GPS tracking logs from accounts closed 8 years prior.
- **Control Defects**: Absence of automated Time-to-Live (TTL) retention policies; machine learning analytics pipelines trained directly on unmasked PII.
- **Remediation Architecture**:
  1. Configured cloud storage bucket lifecycle rules: automated transition to cold archive followed by cryptographic key deletion (Crypto-Shredding).
  2. Built an automated de-identification ETL pipeline enforcing K-Anonymity ($k=5$) and L-Diversity ($l=3$), generalizing timestamps to quarterly buckets.
  3. Decommissioned end-of-life magnetic drives through physical shredding certified under NIST SP 800-88 standards.

---

## 3. CRISC / CDPSE Exam Question Bank & Distractor Forensics

### Q1 `[CRISC/CDPSE - BEST]`
When publishing commercial statistical datasets, what is the BEST engineering defense against linkage attacks using external public registries?
- A. Remove only the data subject's full name and national identification number while preserving other fields intact
- B. Implement K-Anonymity ($k \ge 5$) combined with L-Diversity and quasi-identifier generalization
- C. Store the unmasked dataset on a password-protected USB flash drive
- D. Share unmasked raw data exclusively with research institutions under non-disclosure agreements

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Removing only direct identifiers leaves quasi-identifiers (e.g. ZIP code, gender, birth date) vulnerable to linkage attacks. K-Anonymity and generalization mathematically eliminate re-identification risk.
> - **Why A is Incorrect**: Direct removal (pseudonymization) fails against linkage attacks when quasi-identifiers remain.
> - **Why C is Incorrect**: Password protection provides access control during storage, not anonymization for data sharing.
> - **Why D is Incorrect**: Legal contracts provide administrative recourse rather than mathematical privacy protection.

### Q2 `[CRISC/CDPSE - EXCEPT]`
When decommissioning cloud storage volumes or end-of-life non-volatile media containing personal data, which approach is INVALID and ineffective as a secure disposal method?
- A. Permanently deleting the dedicated data encryption keys (Crypto-shredding)
- B. Executing multi-pass overwrites or firmware purge commands certified under NIST SP 800-88
- C. Relying solely on standard operating system file deletion commands (e.g. empty trash or `rm`) without overwriting blocks or destroying keys
- D. Physically shredding or degaussing physical magnetic hard drives

> **[Correct Answer] C**
> **[Distractor Forensics]**
> - **Why C is Correct**: Standard OS deletion (C) only removes directory index pointers while leaving raw data blocks intact on physical sectors, allowing trivial forensic reconstruction (EXCEPT valid disposal).
> - **Why A, B, D are Incorrect**: Crypto-shredding, NIST SP 800-88 purging, and physical destruction are industry-standard sanitization methods.

### Q3 `[CRISC/CDPSE - PRIMARY]`
What is the PRIMARY purpose of implementing automated Time-to-Live (TTL) expiration policies on databases containing customer personal data?
- A. Maximize server network bandwidth throughput
- B. Ensure compliance with data retention limits by automatically deleting personal data when retention periods expire
- C. Allow marketing teams to bypass user consent requirements
- D. Reduce the frequency of routine database index rebuild operations

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Automated TTL policies ensure systematic adherence to statutory retention limits without relying on error-prone manual deletion scripts.
> - **Why A and D are Incorrect**: Bandwidth throughput and index rebuilds are operational database maintenance considerations.
> - **Why C is Incorrect**: TTL policies enforce retention limits; they cannot override consent requirements.

### Q4 `[CRISC/CDPSE - FIRST]`
An organization is designing a new customer analytics platform. Under the Data Minimization principle, what is the architectural team's FIRST step?
- A. Provision the largest available cloud storage cluster to store all possible future data points
- B. Define the specific business purpose and determine the minimum set of data elements strictly required to achieve that purpose
- C. Procure third-party demographic data feeds to enrich existing customer profiles
- D. Disable database audit logging to accelerate analytical query speeds

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Data minimization begins with defining the specific purpose and identifying the absolute minimum necessary data schema (FIRST step).
> - **Why A and C are Incorrect**: Provisioning maximal storage to collect excessive data directly violates data minimization.
> - **Why D is Incorrect**: Disabling audit logging violates regulatory accountability requirements.
