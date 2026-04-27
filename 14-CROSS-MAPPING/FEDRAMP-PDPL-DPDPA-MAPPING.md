# Cross-Mapping — ISO/IEC 27017 + 27018 ↔ FedRAMP, UAE PDPL & India DPDPA

**Document ID:** CLOUD-CMM-FED-PDPL-DPDPA-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO + DPO | **Review:** Annual

## PART A — FedRAMP (US Federal cloud authorisation)

### A.1 Background

FedRAMP authorises cloud services for use by US federal agencies. Levels: Low / Moderate / High / Tailored. Underlying baseline is NIST SP 800-53 (rev 5).

### A.2 ISO 27017 → FedRAMP control families

| FedRAMP / 800-53 Family | Description | Toolkit Reference |
|-------------------------|-------------|-------------------|
| AC — Access Control | IAM/PAM/MFA | 8.2/8.5; PAM Procedure |
| AT — Awareness & Training | Awareness Programme | 06-SUPPORT |
| AU — Audit & Accountability | Logging/Monitoring | CLD.12.4.5; 8.15 |
| CA — Assessment & Authorization | Internal Audit Programme | 08-PERFORMANCE |
| CM — Configuration Management | IaC, drift detection | 8.9, 8.32 |
| CP — Contingency Planning | DR Plan; multi-AZ | 5.30 |
| IA — Identification & Authentication | MFA, federated SSO | 8.5 |
| IR — Incident Response | Cloud Breach Response Procedure | 5.24-5.28 |
| MA — Maintenance | Change Mgmt; CSP attestations | 8.32 |
| MP — Media Protection | A.10.4-A.10.7 | 27018 |
| PE — Physical & Environmental | Inherited from CSP | CSP attestation |
| PL — Planning | SoA; RTP | 05-PLANNING |
| PS — Personnel Security | HR + AUP | 04-LEADERSHIP |
| RA — Risk Assessment | Methodology + Register | 05-PLANNING |
| SA — System & Services Acquisition | Supplier Cloud Assurance | 15-/Procurement |
| SC — System & Communications Protection | KMS; TLS | KMS Procedure |
| SI — System & Information Integrity | 8.7/8.8; CSPM | Operations |
| SR — Supply Chain Risk Management | Sub-processor mgmt | A.7.1 / A.10.x |

### A.3 FedRAMP Moderate Roadmap (illustrative)

1. Engage 3PAO (Third-Party Assessment Organisation)
2. Develop System Security Plan (SSP) per template
3. Address ~325 Moderate baseline controls
4. ConMon (Continuous Monitoring) plan
5. Authorisation by Agency or JAB
6. Annual assessment + monthly POA&M updates

## PART B — UAE Personal Data Protection Law (PDPL — Federal Decree-Law No. 45/2021)

### B.1 Article-Level Mapping

| PDPL Article | Topic | Toolkit Reference |
|--------------|-------|-------------------|
| Art. 5 | Conditions for processing | Cloud PII Policy + lawful-basis register |
| Art. 6 | Consent | Consent management; A.1.1 |
| Art. 7 | Special categories | Heightened DPIA |
| Art. 8 | Personal Data Breach | Cloud Breach Response (notify UAE DO) |
| Art. 9 | Data subject rights | Cloud DSR Procedure |
| Art. 10 | Withdrawal of consent | DSR procedure |
| Art. 11 | Right to correction | DSR procedure |
| Art. 12 | Right to erasure | DSR procedure |
| Art. 13 | Right to restriction | DSR procedure |
| Art. 14 | Right to object | DSR procedure |
| Art. 15 | Portability | DSR procedure |
| Art. 16 | Automated decisions | DPIA |
| Art. 17 | Controller obligations | Leadership + ISMS |
| Art. 18 | Processor obligations | 27018 + DPA |
| Art. 19 | Records of processing | ROPA |
| Art. 20 | Privacy by Design | SSDLC + Architecture review |
| Art. 21 | DPIA | Cloud DPIA Procedure |
| Art. 22-23 | Cross-border transfer | Cross-Border Transfer Procedure |
| Art. 24 | DPO appointment | DPO ToR / appointment |
| Art. 25 | Complaints | Privacy contact + DSR |

### B.2 UAE-specific operational notes
- Region pinning to me-central-1 for UAE customers
- UAE Data Office (DO) breach-notification timeline tracked in IR runbook

## PART C — India Digital Personal Data Protection Act, 2023 (DPDPA)

### C.1 Mapping

| DPDPA Section | Topic | Toolkit Reference |
|---------------|-------|-------------------|
| s.4 | Grounds for processing | Lawful-basis register |
| s.5 | Notice | Privacy Notice |
| s.6 | Consent | Consent management |
| s.7 | Legitimate uses | Lawful-basis |
| s.8 | Data fiduciary obligations | Cloud PII Policy + ISMS |
| s.8(5) | Reasonable security safeguards | 27017/27018 + 27001 |
| s.8(6) | Breach intimation | Cloud Breach Response |
| s.8(7) | Erasure on purpose end | Retention Policy + DSR |
| s.9 | Children's data | Special-category handling |
| s.10 | Significant Data Fiduciary | DPO + Audit + DPIA |
| s.11-15 | Data Principal rights | Cloud DSR Procedure |
| s.16 | Cross-border transfer | Cross-Border Transfer Procedure |
| s.17 | Exemptions | Documented exception register |
| s.18 | DPB establishment | Liaison via Legal |
| s.27 | Penalties | Cyber-insurance review |

### C.2 Operational notes
- Track Government's notification of restricted-country list for cross-border transfers.
- DPDPA Rules (procedural) tracked separately as they evolve.
- For SDF (Significant Data Fiduciary) status: independent DPIA, audit, DPO mandatory.

## PART D — Compliance Calendar

| Activity | Frequency | Owner |
|----------|-----------|-------|
| FedRAMP ConMon (if pursued) | Monthly POA&M | CSO |
| UAE-DO regulatory horizon scan | Quarterly | DPO |
| India DPDPA Rules tracking | Quarterly | DPO |
| Cross-border transfer-mechanism review | Annual + on-change | DPO |

---
**Document ID:** CLOUD-CMM-FED-PDPL-DPDPA-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
