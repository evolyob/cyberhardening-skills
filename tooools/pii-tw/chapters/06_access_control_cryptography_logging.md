# Chapter 06: Access Control, Cryptographic Architecture & Advanced PETs

## 1. Statutory Baseline & Security Engineering
- **PDPA Enforcement Rules Art 12 Para 2 Item 6**: Mandatory data security management and personnel access controls.
- **PDPA Enforcement Rules Art 12 Para 2 Item 10**: Safety audit mechanisms and retention of access trace logs.
- **ISACA CRISC / CDPSE Mapping**: Zero Trust IAM, Envelope Encryption, Advanced PETs & Continuous Immutable Auditing.

### 1.1 Zero Trust IAM & Segregation of Duties (SoD)
```
┌─────────────────────────────────────────────────────────────┐
│ 1. Identity & Context Gating (FIDO2 MFA / Device Health)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ 2. Privileged Access Management (PAM Just-In-Time / Ephemeral)│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ 3. Policy Enforcement Point (PBAC / ABAC Context Evaluation)│
└─────────────────────────────────────────────────────────────┘
```

| Security Dimension | Technical Engineering Standard | Verification Mechanism |
| :--- | :--- | :--- |
| **Authentication** | FIDO2 / WebAuthn phishing-resistant Multi-Factor Authentication. | Prohibit SMS/email OTP for administrative access; enforce hardware security keys. |
| **Privilege Elevation** | Just-In-Time (JIT) ephemeral credentials via PAM; max duration 4 hours. | Automatic credential revocation; mandatory dual-custody approval workflows. |
| **Segregation of Duties** | Separation of Infrastructure Admins, DBAs, and Security Audit Officers. | No single role possesses concurrent data decryption keys and log deletion rights. |

### 1.2 Cryptographic Key Hierarchy & Envelope Encryption
- **Data Encryption Key (DEK)**: Generated via CSPRNG (AES-256-GCM); encrypts plaintext PII fields at application layer before database commit.
- **Key Encryption Key (KEK)**: Asymmetric or symmetric master keys residing exclusively inside certified Hardware Security Modules (Cloud HSM / KMS, FIPS 140-3 Level 3). KEK encrypts DEKs.
- **Key Rotation**: Automated annual KEK rotation with cryptographic re-wrapping of DEK envelopes without re-encrypting underlying database rows.

### 1.3 Advanced Privacy-Enhancing Technologies (PETs) Matrix
| PET Category | Mathematical Foundation | Enterprise Production Use Case |
| :--- | :--- | :--- |
| **Homomorphic Encryption (FHE / PHE)** | Allows mathematical computations directly over ciphertext ($E(a) \times E(b) = E(ab)$) without decrypting. | Secure cloud-hosted machine learning inference on sensitive medical and financial records. |
| **Zero-Knowledge Proofs (ZKP)** | Proves a statement is true (e.g. age $\ge 18$, balance $\ge \$1000$) without revealing the underlying data. | Privacy-preserving KYC verification and anonymous credential authentication. |
| **Secure Multi-Party Computation (SMPC)** | Multiple parties jointly compute a function over their inputs while keeping inputs private. | Cross-bank anti-money laundering (AML) joint anomaly detection without pooling raw PII. |

### 1.4 Immutable WORM Audit Logging & Forensics Readiness
- **5-Year Statutory Retention**: Access trace logs containing PII queries must be retained for at least 5 years under statutory security plan standards.
- **WORM Immutability (Write Once Read Many)**: Logs must stream asynchronously via Fluentbit to write-locked object storage (e.g. S3 Object Lock in Compliance Mode with Legal Hold capabilities).
- **Cryptographic Chaining**: Enforce Merkle tree or SHA-256 block hash chaining to detect any log deletion, insertion, or timestamp alteration.

---

## 2. Production Scenario: Privileged DBA Account Compromise & Log Tampering
- **Incident Overview**: Attackers compromised a shared DBA credential via spear-phishing, exfiltrated 200,000 financial records, and attempted to purge Linux `/var/log/secure` access trace logs.
- **Control Defects**: Shared credentials prevented non-repudiation; lack of SoD allowed direct database reads; logs stored locally were vulnerable to deletion.
- **Remediation Architecture**:
  1. Deployed PAM with mandatory individual named accounts, MFA, and JIT elevation workflows.
  2. Routed all application and database query logs via Fluentbit to a dedicated, write-locked WORM bucket in an isolated security account.
  3. Deployed ZKP verification microservices for user identity checks, reducing plaintext PII stored in backend databases.

---

## 3. CRISC / CDPSE Exam Question Bank & Distractor Forensics

### Q1 `[CRISC/CDPSE - MOST]`
To protect highly sensitive personal data (e.g., medical diagnoses, financial records) in a relational database from unauthorized inspection by privileged DBAs, what is the MOST effective cryptographic architecture?
- A. Operating system-level Full Disk Encryption (FDE)
- B. Application-layer field-level envelope encryption with decryption keys secured in an external HSM
- C. Base64 encoding of database connection strings
- D. Native database Transparent Data Encryption (TDE) with keys managed directly by the database engine

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Application-layer envelope encryption ensures that data is encrypted before reaching the database, allowing DBAs to view only ciphertext without access to HSM keys.
> - **Why A and D are Incorrect**: Full disk encryption and native TDE automatically decrypt data when the database engine is running, allowing DBAs to query plaintext.
> - **Why C is Incorrect**: Base64 is an encoding format providing zero cryptographic security.

### Q2 `[CRISC/CDPSE - BEST]`
When an organization needs to verify that a customer is over 18 years old without collecting, storing, or inspecting their actual date of birth, which Privacy-Enhancing Technology (PET) is BEST suited?
- A. Zero-Knowledge Proofs (ZKP)
- B. Symmetric AES-256-CBC encryption
- C. Base64 URL encoding
- D. Disk-level RAID 5 parity mirroring

> **[Correct Answer] A**
> **[Distractor Forensics]**
> - **Why A is Correct**: Zero-Knowledge Proofs allow a prover to cryptographically demonstrate that a statement (e.g. age >= 18) is true without disclosing the underlying secret (date of birth).
> - **Why B is Incorrect**: AES encryption conceals data but requires full decryption of the birth date to perform age verification.
> - **Why C and D are Incorrect**: Base64 is an unencrypted encoding scheme; RAID is a hardware storage fault-tolerance mechanism.

### Q3 `[CRISC/CDPSE - PRIMARY]`
Under personal data protection regulations and digital forensics readiness standards, what is the PRIMARY technical requirement for an audit logging system?
- A. Apply high-ratio data compression to minimize storage costs
- B. Maintain Write Once Read Many (WORM) immutability to ensure log integrity and non-repudiation
- C. Automatically purge logs every weekend to free up storage space
- D. Record only error messages while discarding user identity identifiers

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: WORM storage guarantees that log records cannot be altered or deleted by attackers or malicious insiders, preserving evidential weight.
> - **Why A, C, D are Incorrect**: Compression is a cost optimization; purging violates statutory retention periods; discarding identifiers destroys accountability.

### Q4 `[CRISC/CDPSE - FIRST]`
When provisioning administrative access to an engineer for troubleshooting a production database issue, what is the FIRST step under Just-In-Time (JIT) access governance?
- A. Provide permanent full-admin credentials to the engineer's personal workstation
- B. Validate the documented business justification and obtain time-bound ticket approval
- C. Export all customer PII to an unencrypted CSV spreadsheet
- D. Disable database audit logging during the troubleshooting window

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: JIT access requires verifying documented business need and obtaining formal approval (FIRST) before issuing ephemeral credentials.
> - **Why A, C, D are Incorrect**: Permanent credentials, plaintext data dumps, and disabling logs represent severe security violations.
