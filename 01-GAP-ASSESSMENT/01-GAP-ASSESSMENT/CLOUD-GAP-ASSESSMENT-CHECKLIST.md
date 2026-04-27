# Cloud Security Gap Assessment Checklist — ISO/IEC 27017 + ISO/IEC 27018

**Document ID:** CLOUD-GAP-001 | **Version:** 1.0 | **Classification:** Internal

Use this checklist to score current state against ISO 27017 cloud-specific controls and ISO 27018 PII-in-public-cloud obligations.

**Scoring legend:** 0 = Not Started | 1 = Initial | 2 = Defined | 3 = Implemented | 4 = Managed | 5 = Optimised

---

## Part A — Scope and Role Declaration

| # | Question | Score | Owner | Evidence |
|---|----------|-------|-------|----------|
| A.1 | Have you formally declared whether you act as a CSP, CSC, or both per service? | | | |
| A.2 | Are all cloud services in scope listed and classified (IaaS / PaaS / SaaS)? | | | |
| A.3 | Is a Shared Responsibility Matrix in place for each service? | | | |
| A.4 | For PII processing — have you confirmed the role (controller / processor / sub-processor)? | | | |

---

## Part B — ISO 27017 Cloud-Only Controls

| Control | Question | Score | Owner | Evidence |
|---------|----------|-------|-------|----------|
| CLD.6.3.1 | Are cloud roles and responsibilities documented and signed by both CSP and CSC? | | | |
| CLD.8.1.5 | Are CSC asset removal procedures defined for service termination? | | | |
| CLD.9.5.1 | Is segregation enforced in virtual computing environments (tenant isolation)? | | | |
| CLD.9.5.2 | Are virtual machine hardening baselines defined and applied? | | | |
| CLD.12.1.5 | Are administrator operational security procedures documented? | | | |
| CLD.12.4.5 | Is monitoring of cloud services in place with logs accessible to the CSC? | | | |
| CLD.13.1.4 | Is there alignment between virtual and physical network security management? | | | |

---

## Part C — ISO 27017 Cloud Guidance on ISO 27002 Controls (sample)

| ISO 27002:2022 Control | Cloud Question | Score | Owner | Evidence |
|------------------------|----------------|-------|-------|----------|
| 5.23 | Is information security for use of cloud services governed by policy and contract? | | | |
| 5.10 | Are acceptable use rules defined for cloud assets and services? | | | |
| 5.15 | Are cloud identity and access controls aligned with on-premise IAM? | | | |
| 5.17 | Are authentication mechanisms (MFA, federation, key management) in place for cloud? | | | |
| 8.1 | Are cloud user endpoint controls in place? | | | |
| 8.9 | Is cloud configuration management baseline defined and enforced? | | | |
| 8.13 | Is backup of cloud data tested and recoverable? | | | |
| 8.16 | Is cloud monitoring extended to detect tenant-level anomalies? | | | |
| 8.24 | Is cryptography (incl. key custody) defined for cloud — BYOK / HYOK / CSP-managed? | | | |
| 8.28 | Is secure software development applied to cloud-deployed applications? | | | |

---

## Part D — ISO 27018 PII Processor Obligations

| Principle | Question | Score | Owner | Evidence |
|-----------|----------|-------|-------|----------|
| Consent & Choice | Is PII processed only on documented CSC instructions? | | | |
| Purpose Specification | Is PII use limited to contracted purposes (no marketing/profiling without consent)? | | | |
| Collection Limitation | Are only the PII fields necessary for the contracted purpose collected? | | | |
| Data Minimisation | Are minimisation controls applied (masking, pseudonymisation, retention limits)? | | | |
| Use, Retention, Disclosure | Are retention schedules defined and disclosure logs maintained? | | | |
| Accuracy | Are PII update / correction processes available to data subjects via the CSC? | | | |
| Openness & Transparency | Is sub-processor list published and notification of changes provided? | | | |
| Geographic Transparency | Are PII storage locations disclosed to the CSC? | | | |
| Individual Participation | Are CSC-facing tools available to support data subject rights? | | | |
| Accountability | Is a contact point (DPO or equivalent) identified for PII matters? | | | |
| Information Security | Are encryption-in-transit and encryption-at-rest applied to all PII? | | | |
| Privacy Compliance | Are independent audits (SOC 2 / ISO 27001 / ISO 27018) maintained and shared? | | | |
| Breach Notification | Is breach notification to the CSC defined with target SLA (e.g. 24–72 hours)? | | | |
| PII Return / Transfer / Disposal | Are PII return, transfer and secure disposal procedures contracted and tested? | | | |
| Sub-processor Management | Are all sub-processors flow-down bound by equivalent PII obligations? | | | |
| Marketing Restriction | Is there an enforced control preventing use of PII for advertising / marketing without explicit consent? | | | |
| Law Enforcement Disclosure | Is there a documented process to log and (where lawful) notify the CSC of LE requests? | | | |

---

## Part E — Summary

| Section | Total Items | Average Score | % Compliance |
|---------|-------------|---------------|--------------|
| A — Scope & Role | 4 | | |
| B — ISO 27017 Cloud-Only | 7 | | |
| C — ISO 27017 Cloud Guidance | 10 | | |
| D — ISO 27018 PII | 17 | | |
| **Overall** | **38** | | |

---

## Part F — Top Remediation Actions

| # | Gap | Action | Owner | Target Date |
|---|-----|--------|-------|-------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

*Document Owner: GRC Lead | Review cycle: Quarterly during implementation, then annually*
