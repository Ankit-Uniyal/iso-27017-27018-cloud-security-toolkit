# Cross-Mapping — ISO/IEC 27017 + 27018 ↔ NIST CSF 2.0

**Document ID:** CLOUD-CMM-NIST-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Annual

## 1. Purpose

Maps the controls used in this Cloud ISMS to the NIST Cybersecurity Framework version 2.0 functions, categories and subcategories — useful when reporting to US customers, federal counterparts, or boards that prefer NIST language.

## 2. Function-Level Mapping

### GOVERN (GV)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| GV.OC | Organisational Context | Context & Issues Register; Interested Parties Register |
| GV.RM | Risk Management Strategy | Cloud Risk Assessment Methodology; RTP |
| GV.RR | Roles, Responsibilities, Authorities | RACI Matrix; CSO ToR; Leadership Commitment |
| GV.PO | Policy | Cloud Security Policy; Cloud PII Policy; AUP |
| GV.OV | Oversight | KPI Dashboard; Management Review; Internal Audit Programme |
| GV.SC | Cybersecurity Supply Chain | Supplier Cloud Assurance Questionnaire; Sub-processor management |

### IDENTIFY (ID)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| ID.AM | Asset Management | Cloud Asset & PII Inventory |
| ID.RA | Risk Assessment | Cloud Risk Register; Methodology |
| ID.IM | Improvement | Continual Improvement Log; NCR register |

### PROTECT (PR)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| PR.AA | Identity Management & Access Control | IAM, MFA, PAM (CLD.12.1.5; 8.2/8.5) |
| PR.AT | Awareness & Training | Awareness Programme; Competence Register |
| PR.DS | Data Security | KMS Procedure; Retention Policy; CLD.8.1.5 |
| PR.PS | Platform Security | Hardening (CLD.9.5.2); 8.7 / 8.8 / 8.9 |
| PR.IR | Tech Infrastructure Resilience | DR/BCP; multi-AZ |

### DETECT (DE)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| DE.CM | Continuous Monitoring | CLD.12.4.5; 8.15/8.16; CSPM |
| DE.AE | Adverse Event Analysis | SIEM; SOC runbooks |

### RESPOND (RS)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| RS.MA | Incident Management | Cloud Breach Response Procedure |
| RS.AN | Analysis | Forensic procedure; CSP IR support |
| RS.CO | Communication | Communications Plan; A.8.1 notification |
| RS.MI | Mitigation | IR playbooks |

### RECOVER (RC)

| NIST CSF 2.0 | Description | Toolkit Reference |
|--------------|-------------|-------------------|
| RC.RP | Incident Recovery Plan | DR plan; multi-region |
| RC.CO | Recovery Communications | Comms Plan |

## 3. Implementation Tier

Target Tier: **Tier 3 (Repeatable)** — risk-informed, documented, regularly updated.

## 4. NIST Privacy Framework alignment

The control set referenced above also broadly aligns with the NIST Privacy Framework v1.0 (IDENTIFY-P, GOVERN-P, CONTROL-P, COMMUNICATE-P, PROTECT-P) — particularly:

- IDENTIFY-P → Cloud Asset & PII Inventory
- GOVERN-P → Cloud PII Policy + Leadership Commitment
- CONTROL-P → DSR Procedure + Consent management
- COMMUNICATE-P → Privacy Notice + Trust Centre
- PROTECT-P → Encryption, Access Control, 27018 Annex A

---
**Document ID:** CLOUD-CMM-NIST-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
