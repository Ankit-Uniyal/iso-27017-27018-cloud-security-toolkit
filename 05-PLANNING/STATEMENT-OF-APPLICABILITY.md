# Statement of Applicability — ISO/IEC 27017 + ISO/IEC 27018

**Document ID:** CLOUD-SOA-001 | **Version:** 1.0 | **Classification:** Internal

This SoA records the applicability and implementation status of cloud-extended controls. It supplements the base ISO 27001:2022 SoA.

**Status:** I = Implemented | P = Partial | N = Not Implemented | NA = Not Applicable
**Justification codes:** L = Legal | C = Contractual | R = Risk | B = Business | BP = Best Practice

## Section 1 — ISO 27017 Cloud-Only Controls

| Control | Title | Applicable? | Justification | Status | Owner | Evidence |
|---------|-------|-------------|---------------|--------|-------|----------|
| CLD.6.3.1 | Shared roles and responsibilities | Yes | C, BP | | Cloud Architect | Shared Resp. Matrix |
| CLD.8.1.5 | Removal of CSC assets | Yes | C, L | | Service Owner | Termination procedure |
| CLD.9.5.1 | Segregation in virtual environments | Yes (CSP) | R, BP | | Cloud Architect | Tenant isolation report |
| CLD.9.5.2 | Virtual machine hardening | Yes | BP | | Cloud Architect | Hardening baseline |
| CLD.12.1.5 | Administrator's operational security | Yes (CSP) | R | | CISO | Admin runbook |
| CLD.12.4.5 | Monitoring of cloud services | Yes | R | | SOC | SIEM dashboards |
| CLD.13.1.4 | Alignment of virtual and physical network security | Yes (CSP) | R | | Cloud Architect | Network design doc |

## Section 2 — ISO 27017 Cloud Guidance on ISO 27002:2022 Controls (key)

| ISO 27002 | Cloud-relevant Topic | Applicable? | Status | Owner | Evidence |
|-----------|----------------------|-------------|--------|-------|----------|
| 5.23 | Information security for use of cloud services | Yes | | CISO | Cloud Security Policy |
| 5.10 | Acceptable use of cloud assets | Yes | | CISO | AUP |
| 5.15–5.18 | Identity, access, MFA, authentication | Yes | | IAM Lead | IAM standards |
| 5.30 | ICT readiness for business continuity (cloud) | Yes | | BCM | DR runbooks |
| 5.34 | Privacy and PII (cloud) | Yes | | DPO | Cloud PII Policy |
| 8.9 | Configuration management (cloud) | Yes | | Cloud Architect | Baseline |
| 8.13 | Backup (cloud) | Yes | | Service Owner | Backup tests |
| 8.16 | Monitoring activities | Yes | | SOC | SIEM |
| 8.20–8.23 | Network security (cloud) | Yes | | NetSec | Architecture |
| 8.24 | Use of cryptography (cloud) | Yes | | CryptoLead | Crypto standard |
| 8.25–8.28 | Secure development (cloud) | Yes | | DevSecOps | SSDLC |

## Section 3 — ISO 27018 PII-in-Public-Cloud Annex A Extensions

| Reference | Obligation | Applicable? | Status | Owner | Evidence |
|-----------|------------|-------------|--------|-------|----------|
| A.1 | Documented processing instructions from CSC | Yes | | DPO | DPA |
| A.2 | Purpose limitation; no marketing without consent | Yes | | DPO | Marketing exclusion control |
| A.3 | Sub-processor disclosure and notification | Yes | | DPO | Sub-processor list |
| A.4 | Sub-processor flow-down obligations | Yes | | Procurement | Sub-processor DPAs |
| A.5 | Geographic transparency | Yes | | DPO | Region disclosure |
| A.6 | Encryption in transit and at rest | Yes | | CISO | Crypto register |
| A.7 | BYOK / customer-controlled key option | Where applicable | | CryptoLead | KMS config |
| A.8 | Breach notification to CSC (SLA) | Yes | | DPO | IR procedure |
| A.9 | Data subject rights cooperation | Yes | | DPO | DSR procedure |
| A.10 | Return / transfer / secure disposal | Yes | | Service Owner | Exit procedure |
| A.11 | Law enforcement disclosure handling | Yes | | Legal | LE disclosure log |
| A.12 | Personnel confidentiality and training | Yes | | HR | Training records |
| A.13 | Independent assurance (ISO/SOC 2 reports) | Yes | | CISO | Annual reports |
| A.14 | Records of PII processing operations | Yes | | DPO | ROPA |
| A.15 | PII minimisation and retention controls | Yes | | DPO | Retention schedule |

---

*Approved by: CISO + DPO | Date: April 2026 | Review cycle: At least annually and on significant change*
