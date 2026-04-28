# Access Review Evidence Record

**Control:** ISO/IEC 27001:2022 Annex A 5.15 — Access Control  
**Cloud Extension:** ISO/IEC 27017:2015 — Shared Responsibility  
**Document ID:** A.5.15_ACCESS-REVIEW_YYYY-QN  
**Review Period:** YYYY-QN (e.g. 2026-Q1)  
**Classification:** Internal  
**Owner:** Cloud Security Officer  

---

## 1. Review Scope

| Item | Detail |
|---|---|
| Systems / Services covered | [List AWS/Azure/GCP accounts, SaaS apps] |
| Review type | Quarterly privileged-access review |
| Reviewer | [Name, Role] |
| Review date | YYYY-MM-DD |
| Approved by | [Name, Role] |

---

## 2. Access Review Summary

| User / Service Account | Role / Permission | Access Justified? | Action |
|---|---|---|---|
| [user@example.com] | Admin | Yes | No change |
| [svc-account-01] | ReadOnly | Yes | No change |
| [ex-employee@example.com] | Admin | No | **REVOKE — immediate** |

---

## 3. Findings & Actions

| Finding | Risk | Owner | Due Date | Status |
|---|---|---|---|---|
| Stale account with admin rights | High | [IAM Owner] | YYYY-MM-DD | Open |

---

## 4. CSP Shared-Responsibility Note

> Under ISO/IEC 27017, the Cloud Service Customer (CSC) is responsible for managing identities and access permissions within the cloud environment. The CSP (e.g. AWS IAM, Azure RBAC) provides the tooling; this review demonstrates the CSC's operational control.

---

## 5. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Reviewer | | | |
| CSO / ISMS Manager | | | |

---

*Document ID: A.5.15_ACCESS-REVIEW_TEMPLATE | Version: 1.0 | Classification: Internal | Owner: CSO | Review: Quarterly*
