# Cross-Mapping — ISO/IEC 27017 + 27018 ↔ GDPR (EU 2016/679)

**Document ID:** CLOUD-CMM-GDPR-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO | **Review:** Annual

## 1. Purpose

Maps the controls and practices of ISO/IEC 27017:2015 and 27018:2019 (as documented in this toolkit) to the obligations of the EU General Data Protection Regulation (Regulation (EU) 2016/679). UK GDPR is materially equivalent.

## 2. Article-by-Article Mapping

| GDPR Article | Topic | Toolkit Controls / Documents | Evidence |
|--------------|-------|------------------------------|----------|
| Art. 5(1)(a) | Lawfulness, fairness, transparency | Cloud PII Policy; Privacy Notice template | Published notice |
| Art. 5(1)(b) | Purpose limitation | A.2.1 / A.2.2; DPA processing schedule | DPA |
| Art. 5(1)(c) | Data minimisation | A.3.1; Data Inventory | Inventory |
| Art. 5(1)(d) | Accuracy | A.6.1; data-quality SLA | SLA report |
| Art. 5(1)(e) | Storage limitation | Data Retention & Disposal Policy | Retention schedule |
| Art. 5(1)(f) | Integrity & confidentiality | 27017 + 27018 technical controls | SoA |
| Art. 5(2) | Accountability | This whole toolkit | Cert + audit |
| Art. 6 | Lawful basis | Lawful-basis register; Cloud PII Policy | Register |
| Art. 7 | Conditions for consent | Consent management (where controller) | Consent log |
| Art. 9 | Special categories | Heightened controls; DPIA mandatory | DPIA records |
| Art. 12 | Transparent communication | Privacy Notice | Published |
| Art. 13/14 | Information to data subjects | Privacy Notice | Published |
| Art. 15-21 | Data subject rights | Cloud DSR Procedure | DSR register |
| Art. 22 | Automated decision-making | DPIA + safeguards | DPIA |
| Art. 24 | Controller responsibility | Leadership Commitment + ISMS | Cert |
| Art. 25 | Privacy by Design / Default | Architecture review; SSDLC | Design docs |
| Art. 28 | Processor obligations | 27018 (full Annex A) + DPA Template | DPA + 27018 SoA |
| Art. 28(3)(a) | Documented instructions | A.2.1 / A.2.2 | DPA |
| Art. 28(3)(b) | Confidentiality | A.10.1 NDA | NDA register |
| Art. 28(3)(c) | Article 32 measures | 27017/27018 controls | SoA |
| Art. 28(3)(d) | Sub-processors | A.7.1, A.10.11, A.10.12 | Sub-processor list |
| Art. 28(3)(e) | DSR support | A.1.1 | DSR procedure |
| Art. 28(3)(f) | Breach notification | A.8.1; Breach Response Procedure | IR records |
| Art. 28(3)(g) | Return / deletion | A.11.2; CLD.8.1.5 | Termination evidence |
| Art. 28(3)(h) | Audit cooperation | Audit-cooperation procedure (Trust Centre) | Audit reports |
| Art. 30 | Records of processing | ROPA (in Cloud Asset Inventory) | ROPA |
| Art. 32 | Security of processing | Full SoA + KMS + IR | SoA |
| Art. 33 | Breach notification to SA | Breach Response Procedure (72h) | Notification log |
| Art. 34 | Breach communication to data subjects | Breach Response Procedure | Comms log |
| Art. 35 | DPIA | Cloud DPIA Procedure & Template | DPIA register |
| Art. 36 | Prior consultation | DPIA escalation path | Consultation log |
| Art. 37-39 | DPO | DPO appointment letter; DPO ToR | Appointment |
| Art. 44-49 | International transfers | Cross-Border Transfer Procedure; SCCs | Transfer register |
| Art. 82 | Liability | Cyber insurance + indemnities | Policy |

## 3. EU SCCs (2021) — Module Mapping

| Module | Use case | Toolkit reference |
|--------|----------|-------------------|
| 1 (C-to-C) | Controller to non-EEA controller | DPA Annex |
| 2 (C-to-P) | Controller to non-EEA processor | DPA Annex (default for our processor mode) |
| 3 (P-to-P) | Processor to non-EEA sub-processor | Sub-processor DPA |
| 4 (P-to-C) | Processor to non-EEA controller | Rare; documented case-by-case |

## 4. Common Audit Findings (mitigation)

| Finding | Mitigation |
|---------|-----------|
| Outdated ROPA | Quarterly inventory review |
| Sub-processor list out-of-date | 30-day notice; quarterly audit |
| Stale TIAs | Annual TIA refresh schedule |
| Missing breach drill | Bi-annual tabletop |
| Privacy Notice not in plain language | Annual readability review |

---
**Document ID:** CLOUD-CMM-GDPR-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
