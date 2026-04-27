# Cloud Risk Register (ISO 27017 / ISO 27018)

**Document ID:** CLOUD-RR-001 | **Version:** 1.0 | **Classification:** Internal

Risk methodology aligned to ISO/IEC 27005:2022. Likelihood (L) and Impact (I) on a 1–5 scale; Risk = L × I (1–25).

| ID | Risk | CSP/CSC | Cause | Consequence | L | I | Score | Treatment | Owner | Target Date |
|----|------|---------|-------|-------------|---|---|-------|-----------|-------|-------------|
| CR-001 | Mis-configured cloud storage exposes data | CSC | Lack of guardrails / drift | Data breach, regulatory fine | 4 | 5 | 20 | Mitigate — CSPM, IaC policy gates | CISO | Q3-2026 |
| CR-002 | Shared responsibility ambiguity | Both | Unclear CSA | Control gaps, audit findings | 3 | 4 | 12 | Mitigate — signed Shared Responsibility Matrix per service | Cloud Architect | Q2-2026 |
| CR-003 | Sub-processor PII flow-down failure | CSP | Inadequate vendor mgmt | ISO 27018 nonconformity, GDPR breach | 3 | 5 | 15 | Mitigate — sub-processor DPAs + annual audit | DPO | Q3-2026 |
| CR-004 | Cross-border PII transfer without safeguards | Both | Missing TIA / SCCs | Regulatory fine, transfer ban | 2 | 5 | 10 | Mitigate — TIA + SCCs / BCRs | DPO + Legal | Q2-2026 |
| CR-005 | Tenant isolation breach (CSP) | CSP | Hypervisor flaw / mis-config | Cross-tenant data exposure | 2 | 5 | 10 | Mitigate — segregation testing, patching | Cloud Architect | Continuous |
| CR-006 | Encryption key compromise | Both | Weak KMS / key custody | Data exposure | 2 | 5 | 10 | Mitigate — BYOK, HSM, rotation | CryptoLead | Q3-2026 |
| CR-007 | CSP outage exceeds RTO | CSC | CSP failure | Service unavailability | 2 | 4 | 8 | Mitigate — multi-region / DR plan | BCM | Q4-2026 |
| CR-008 | Inadequate cloud logging visibility for CSC | CSC | CSP doesn't expose logs | Detection gap | 3 | 4 | 12 | Mitigate — contractual log access (CLD.12.4.5) | SOC | Q2-2026 |
| CR-009 | Use of PII for marketing without consent | CSP | Misuse / mis-config | ISO 27018 violation | 2 | 5 | 10 | Mitigate — purpose lock + audit (A.2) | DPO | Q2-2026 |
| CR-010 | Failure to delete PII on termination | CSP | Process gap | Regulatory + contractual breach | 2 | 4 | 8 | Mitigate — exit procedure + deletion certificate | Service Owner | Q3-2026 |
| CR-011 | Law enforcement disclosure without notice | CSP | Process gap | Trust + contractual breach | 2 | 4 | 8 | Mitigate — LE disclosure procedure (A.11) | Legal | Q2-2026 |
| CR-012 | Identity compromise (cloud admin) | Both | No MFA / weak IAM | Tenant takeover | 3 | 5 | 15 | Mitigate — MFA, PAM, just-in-time access | IAM Lead | Q2-2026 |

---

*Risk owner: CISO (security risks) / DPO (privacy risks) | Review cycle: Quarterly*
