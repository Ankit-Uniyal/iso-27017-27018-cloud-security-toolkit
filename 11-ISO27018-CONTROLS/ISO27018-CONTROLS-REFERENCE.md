# ISO/IEC 27018:2019 — Controls Reference (PII in Public Cloud)

**Document ID:** CLOUD-27018-001 | **Version:** 1.0 | **Classification:** Public

ISO/IEC 27018:2019 is a code of practice for protection of PII in public clouds acting as **PII processors**. It augments ISO/IEC 27002 with PII-specific controls organised by the 11 ISO/IEC 29100 privacy principles.

## Annex A — Public Cloud PII Processor Extension Set

| Reference | Principle | Obligation | Implementation Notes | Evidence |
|-----------|-----------|------------|----------------------|----------|
| A.1 | Consent and Choice | Process PII only on documented CSC instructions | Reference DPA | DPA |
| A.2 | Purpose Specification | No PII for marketing without explicit opt-in | Purpose lock | Marketing exclusion control |
| A.3 | Collection Limitation | Collect only what is needed | API design review | API spec reviews |
| A.4 | Data Minimisation | Apply minimisation, masking | Privacy by Design | Architecture docs |
| A.5 | Use, Retention & Disclosure | Retention schedule; disclosure logged | Retention engine | Retention tickets |
| A.6 | Accuracy | Enable correction via CSC tools | API for rectification | DSR tooling |
| A.7 | Openness & Transparency | Publish PII handling, sub-processor list | Trust portal | Portal screenshots |
| A.8 | Individual Participation | Cooperate with CSC on DSRs | DSR runbook | DSR samples |
| A.9 | Accountability | DPO appointed; ROPA | DPO terms | DPO charter |
| A.10 | Information Security | Encryption in transit + at rest | TLS, AES-256, BYOK option | Crypto register |
| A.11 | Privacy Compliance | Maintain ISO/SOC 2 etc. | Annual independent assurance | Audit reports |
| A.12 | Sub-processor Disclosure | List + advance notice | Sub-processor portal | Portal log |
| A.13 | Sub-processor Flow-down | Equivalent obligations | Procurement clauses | Sub-processor DPAs |
| A.14 | Transfer Transparency | Disclose locations | Region selector | Region docs |
| A.15 | Transfer Safeguards | SCCs / BCRs / TIA | Legal mechanisms | TIA report |
| A.16 | Breach Notification | Notify CSC within SLA | IR procedure | IR records |
| A.17 | Breach Content | Scope, classes, consequences | IR template | Notification copy |
| A.18 | Return / Disposal | Deletion certificate | Exit procedure | Deletion certificates |
| A.19 | Personnel Confidentiality | NDA, training | HR onboarding | HR records |
| A.20 | Background Screening | Risk-based checks | HR procedure | HR records |
| A.21 | Records of Disclosure | Log mandatory disclosures | Disclosure log | Log samples |
| A.22 | Law Enforcement Requests | Notify CSC where lawful | LE procedure | Case log |
| A.23 | Recovery | Backup with PII protections | Backup tests | Backup test reports |
| A.24 | Media Decommissioning | Secure disposal | Media procedure | Disposal records |
| A.25 | Geographic Transparency | Disclose regions | Region disclosure | Region matrix |

---

*Owner: DPO | Cross-references: ISO/IEC 29100:2011, ISO/IEC 27017:2015*
