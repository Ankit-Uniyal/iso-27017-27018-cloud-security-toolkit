# ISO/IEC 27018:2019 — PII Protection in Public Clouds (Reference)

**Document ID:** CLOUD-27018-REF-001 | **Version:** 2.0 | **Classification:** Internal | **Owner:** Data Protection Officer | **Review:** Annual

## 1. Purpose

ISO/IEC 27018:2019 is the *Code of practice for protection of Personally Identifiable Information (PII) in public clouds acting as PII processors*. This reference covers all 25 Annex A control objectives with cloud-PII-processor implementation guidance, evidence and audit-test guidance.

## 2. Scope of Applicability

Applies wherever the organisation acts as a **PII processor** in a public-cloud context (SaaS provider, multi-tenant platform, customer-data processor). When the organisation is a **PII controller**, ISO/IEC 27701 controls apply in parallel.

## 3. Annex A — PII Processor Controls

### A.1 — Consent and choice

**A.1.1 Obligation to co-operate regarding PII principals' rights** — The PII processor must provide the customer (controller) with the means to comply with PII principals' rights (access, correction, erasure, portability).
- *Implementation:* DSR procedure with controller-facing API/portal; documented SLAs.
- *Evidence:* DSR procedure (07-OPERATION); ticket samples; DPA Article 28-equivalent clauses.
- *Audit test:* Sample 5 DSR tickets, verify SLA compliance.

### A.2 — Purpose legitimacy and specification

**A.2.1 Public cloud PII processor's purpose** — PII processed only for purposes documented in the customer instruction.
- *Evidence:* DPA Schedule of Processing; instruction log.

**A.2.2 Public cloud PII processor's commercial use** — PII shall not be used for the processor's own marketing/advertising without consent.
- *Evidence:* DPA prohibition clause; internal policy.

### A.3 — Collection limitation

**A.3.1 Collection limitation** — Limit PII collected to what is necessary.
- *Evidence:* Data minimisation policy; schema review records.

### A.4 — Data minimisation

**A.4.1 Secure erasure of temporary files** — Temporary files containing PII must be securely erased.
- *Evidence:* Auto-cleanup job logs; OS-level secure-delete configuration.
- *Audit test:* Inspect temp-file lifecycle on a production node.

### A.5 — Use, retention and disclosure limitation

**A.5.1 PII disclosure notification** — Notify the customer of any legally binding request for PII disclosure unless prohibited.
- *Evidence:* Disclosure notification procedure; legal-team escalation path.

**A.5.2 Recording of PII disclosures** — Record every disclosure of PII to third parties (purpose, recipient, date).
- *Evidence:* Disclosure register.
- *Audit test:* Sample disclosures over the last 12 months.

### A.6 — Accuracy and quality

**A.6.1 Accuracy and quality** — Provide tools enabling the controller to keep PII accurate and up-to-date.
- *Evidence:* Edit/correction APIs; data-quality SLA.

### A.7 — Openness, transparency and notice

**A.7.1 Disclosure of sub-contracted PII processing** — Disclose use of sub-processors before they begin processing; obtain controller authorisation.
- *Evidence:* Public sub-processor list; 30-day change-notice procedure; DPA clause.

### A.8 — Individual participation and access

**A.8.1 Notification of a data breach involving PII** — Promptly notify the controller of any breach involving PII; provide details enabling controller to meet its obligations.
- *Evidence:* Cloud Breach Response Procedure (07-OPERATION); 72-hour SLA; notification template.
- *Audit test:* Tabletop exercise records; notification-template review.

### A.9 — Accountability

**A.9.1 Geographical location of PII** — Communicate to the customer in advance the countries where PII may be stored.
- *Evidence:* Region-list in DPA Annex II; product documentation.

**A.9.2 Intended destination of PII** — Communicate purpose of any cross-border transfer.
- *Evidence:* Cross-Border Transfer Procedure (07-OPERATION); transfer log.

### A.10 — Information security

**A.10.1 Confidentiality or non-disclosure agreements** — All personnel with access to PII must sign NDA.
- *Evidence:* NDA register.

**A.10.2 Restriction of the creation of hardcopy material** — Restrict printing of PII.
- *Evidence:* Print-restriction policy; MDM enforcement.

**A.10.3 Control and logging of data restoration** — Log every PII data-restoration event.
- *Evidence:* Restore-log SIEM dashboard.

**A.10.4 Protecting data on storage media leaving the premises** — Encrypt media; control physical movement.
- *Evidence:* CSP attestations (typically inherited from CSP for public-cloud).

**A.10.5 Use of unencrypted portable storage media and devices** — Prohibit unencrypted portable media.
- *Evidence:* MDM USB-block policy.

**A.10.6 Encryption of PII transmitted over public data-transmission networks** — TLS 1.2+ for all PII in transit.
- *Evidence:* TLS configuration scan; HSTS headers.

**A.10.7 Secure disposal of hardcopy materials** — Cross-cut shredding or secure-disposal vendor.
- *Evidence:* Shred-bin contract; certificates of destruction.

**A.10.8 Unique use of user IDs** — No shared accounts.
- *Evidence:* IAM policy banning shared credentials; account audit.

**A.10.9 Records of authorised users** — Maintain register of users authorised to access PII.
- *Evidence:* IAM register; access-review records.

**A.10.10 User ID management** — JML (joiner/mover/leaver) automation.
- *Evidence:* JML workflow; HRIS-IAM integration logs.

**A.10.11 Contract measures** — All sub-processors bound by equivalent contract terms.
- *Evidence:* Sub-processor DPA templates; signed copies.

**A.10.12 Sub-contracted PII processing** — Due diligence and approval of sub-processors.
- *Evidence:* Supplier Cloud Assurance Questionnaire (15-); approval log.

**A.10.13 Access to data on pre-used data storage space** — Ensure no residual data accessible on reused storage.
- *Evidence:* CSP attestation of zeroisation.

### A.11 — Privacy compliance

**A.11.1 Geographical location of PII** — Maintain awareness and customer-facing documentation of PII storage locations.
- *Evidence:* Region pinning configuration; DPA Annex II.

**A.11.2 Return, transfer and disposal of PII** — On contract end, return or securely dispose of PII per customer instruction.
- *Evidence:* Termination procedure; deletion certificate; export tooling.
- *Audit test:* Inspect last termination case.

## 4. Mapping to GDPR Article 28 (Processor Obligations)

| 27018 Annex A | GDPR Art. 28(3) | Notes |
|---------------|-----------------|-------|
| A.2.1, A.2.2 | (a) Documented instructions | DPA processing schedule |
| A.10.1 | (b) Confidentiality | NDA register |
| A.10.6, A.10.x | (c) Article 32 measures | Technical/organisational |
| A.7.1, A.10.11, A.10.12 | (d) Sub-processors | Sub-processor authorisation |
| A.1.1 | (e) Data subject rights | DSR API/portal |
| A.8.1 | (f) Breach notification | 72-hour SLA |
| A.11.2 | (g) Return/deletion | Termination procedure |
| A.5.1, A.5.2 | (h) Audit/disclosure | Disclosure register |

## 5. Audit-Trail Mapping

| 27018 Control | SoA Row | KPI Metric | Worked-Example Artifact |
|---------------|---------|------------|-------------------------|
| A.1.1 | 27018-1 | DSR SLA % | DSR ticket sample |
| A.5.2 | 27018-7 | Disclosures logged % | Disclosure register |
| A.7.1 | 27018-9 | Sub-processor change notices | Sub-processor list |
| A.8.1 | 27018-10 | Breach notifications within 72h | Breach log |
| A.9.1 | 27018-11 | Region-pinning compliance | DPA Annex II |
| A.10.6 | 27018-18 | TLS 1.2+ enforcement % | TLS scan report |
| A.10.10 | 27018-22 | JML automation % | HRIS-IAM logs |
| A.11.2 | 27018-27 | Termination deletions on time | Termination evidence |

---
**Document ID:** CLOUD-27018-REF-001 | **Version:** 2.0 | **Classification:** Internal | **Next Review:** Annual
