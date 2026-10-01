# Chapter 04: Infrastructure Security, Multitenant Cloud & Cross-Border Data Transfers

## 1. Statutory Baseline & Infrastructure Engineering
- **PDPA Statutory Article 21**: Authority of central competent authorities to restrict international data transfers (national interests, international treaties, inadequate legal protection, legal evasion).
- **PDPA Enforcement Rules Art 12 Para 2 Item 8**: Security management of equipment and facilities processing personal data.
- **Privacy & Risk Engineering Framework**: Cloud Infrastructure Security, Multitenancy Isolation & Cross-Border Governance.

### 1.1 Cloud Multitenancy Technical Isolation Controls
```
┌─────────────────────────────────────────────────────────────┐
│ Application & API Gateway Layer (JWT Tenant Claim Check)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Compute Layer: Namespace & Pod Security Standards (PSS)      │
│ Confidential Computing: AMD SEV-SNP / Intel SGX (TEE Memory)│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Storage Layer: PostgreSQL Row-Level Security (RLS) Policies │
│ Cryptographic Isolation: Dedicated Cloud HSM / KMS Keys     │
└─────────────────────────────────────────────────────────────┘
```

| Isolation Layer | Technical Mechanism | Verification & Control Standard |
| :--- | :--- | :--- |
| **Compute & Runtime** | Kubernetes Namespaces, Pod Security Standards (PSS Restricted profile), Kata Containers. | Enforce hypervisor or hardware-level container isolation; block privileged root containers. |
| **Confidential Computing** | Trusted Execution Environments (TEE, e.g. AMD SEV-SNP, Intel SGX, AWS Nitro Enclaves). | Encrypt data-in-use in memory; memory contents remain invisible even to hypervisors and host root. |
| **Storage & Database** | Database Row-Level Security (RLS) enforcing `WHERE tenant_id = current_setting(...)`. | Prevent multi-tenant cross-query leakage at database engine level independent of app bugs. |
| **Cryptographic Control** | Bring Your Own Key (BYOK) / Hold Your Own Key (HYOK) with Cloud HSM / Dedicated KMS. | Master root keys generated inside dedicated HSMs; Cloud Service Provider (CSP) cannot view keys. |

### 1.2 Cross-Border Transfer Compliance Pipeline (5-Step TIA)
1. **Data Mapping & Transfer Scoping**: Identify cross-border data flows, recipient categories, transfer frequencies, and processing locations.
2. **Statutory Prohibition Screening**: Verify absence of ministerial restriction orders issued under Taiwan PDPA Art 21.
3. **Third-Country Adequacy & Surveillance Assessment**: Evaluate recipient jurisdiction legal frameworks, judicial redress mechanisms, and government surveillance powers.
4. **Technical & Contractual Safeguards**: Execute Standard Contractual Clauses (SCCs), enforce mandatory in-transit TLS 1.3, and maintain envelope encryption.
5. **Continuous Governance & Transfer Audit**: Periodically review geopolitical changes and audit overseas processor sub-processing chains.

---

## 2. Production Scenario: SaaS Multi-Tenant Leakage & Cross-Border Migration
- **Incident Overview**: An APAC CRM SaaS provider hosted customer data in a shared public cloud database. An application code defect in a reporting endpoint omitted tenant filters, exposing Tenant A customer lists to Tenant B.
- **Root-Cause Analysis**:
  1. The application relied solely on application-level filtering rather than database-enforced Row-Level Security (RLS).
  2. Data at rest was encrypted with a single shared platform master key rather than tenant-isolated cryptographic keys.
  3. The database was hosted in an overseas region without completing a formal Transfer Impact Assessment (TIA).
- **Remediation Architecture**:
  1. Implemented PostgreSQL RLS policies, binding every database connection to authenticated JWT tenant claims.
  2. Migrated encryption to dedicated Cloud HSM with tenant-specific Data Encryption Keys (DEKs).
  3. Completed a formal TIA and signed Binding Corporate Rules (BCRs) / Standard Contractual Clauses with the overseas cloud provider.

---

## 3. Scenario Practice & Decision Forensics (Q&A) & Distractor Forensics

### Q1 `[Privacy Engineering - MOST]`
When storing sensitive personal data in a multitenant public cloud database, what is the MOST effective architectural control to prevent cross-tenant data leakage?
- A. Deploy perimeter network firewalls and intrusion prevention systems (IPS)
- B. Enforce database Row-Level Security (RLS) coupled with tenant-specific BYOK encryption
- C. Sign bilateral non-disclosure agreements (NDAs) with all tenant organizations
- D. Restrict database access to standard business hours via VPN tunnels

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In multitenant cloud environments, preventing logic bypass requires storage-layer logical separation (RLS) reinforced by cryptographic isolation (tenant-isolated keys).
> - **Why A is Incorrect**: Network firewalls protect the perimeter ingress, not memory and query segregation between co-located tenants.
> - **Why C is Incorrect**: NDAs are legal administrative agreements that cannot technically prevent software bugs or malicious cross-tenant queries.
> - **Why D is Incorrect**: Time-based access restrictions do not mitigate architectural cross-tenant query flaws.

### Q2 `[Privacy Engineering - FIRST]`
Prior to migrating customer personal data from on-premises servers to an overseas public cloud data center, what is the compliance and risk team's FIRST action?
- A. Order high-bandwidth dedicated international private leased circuits (IPLC)
- B. Conduct a Transfer Impact Assessment (TIA) and verify whether regulatory transfer restrictions apply under Art 21
- C. Email all registered customers notifying them of the migration schedule
- D. Perform cryptographic degaussing on all existing on-premises storage media

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Any cross-border data transfer must begin (FIRST) with legal and risk assessments (TIA) to verify jurisdictional adequacy and statutory compliance.
> - **Why A is Incorrect**: Purchasing network circuits is an implementation step that should occur only after obtaining legal clearance.
> - **Why C is Incorrect**: Customer notification is appropriate only after confirming that the transfer is legally permissible.
> - **Why D is Incorrect**: Decommissioning media occurs only after migration and verification are fully complete.

### Q3 `[Privacy Engineering - BEST]`
Which technology provides the BEST protection for sensitive personal data against unauthorized inspection by cloud hypervisor administrators during active computation?
- A. Transparent Data Encryption (TDE) at rest
- B. Hardware-enforced Confidential Computing with Trusted Execution Environments (TEE)
- C. Transport Layer Security (TLS 1.3) with perfect forward secrecy
- D. Storage Area Network (SAN) snapshot replication

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Confidential Computing (TEE) encrypts data-in-use in physical memory, preventing host hypervisors and root administrators from inspecting plaintext.
> - **Why A is Incorrect**: TDE protects data at rest on disk, not data loaded into RAM during active processing.
> - **Why C is Incorrect**: TLS 1.3 protects data in transit across network wires, not data undergoing computation in host memory.
> - **Why D is Incorrect**: SAN snapshotting is a storage backup mechanism, not an execution isolation control.

### Q4 `[Privacy Engineering - PRIMARY]`
What is the PRIMARY purpose of executing Standard Contractual Clauses (SCCs) when transferring personal data to an overseas cloud vendor?
- A. Guarantee that the cloud provider achieves 99.999% uptime availability SLA
- B. Establish legally binding obligations ensuring the data receives protection equivalent to statutory domestic standards
- C. Waive the data controller's legal liability in the event of an overseas breach
- D. Eliminate the requirement to encrypt personal data during international network transit

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: SCCs serve to contractually bind foreign processors to uphold privacy and security standards equivalent to the originating jurisdiction.
> - **Why A is Incorrect**: Uptime availability is covered in standard commercial Service Level Agreements (SLAs), not SCCs.
> - **Why C is Incorrect**: Data controllers cannot contractually waive statutory breach liability to data subjects.
> - **Why D is Incorrect**: SCCs mandate verified technical security measures, including encryption; they do not exempt entities from technical safeguards.
