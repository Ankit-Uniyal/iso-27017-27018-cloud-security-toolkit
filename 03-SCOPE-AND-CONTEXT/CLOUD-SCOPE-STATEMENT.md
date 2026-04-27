# Cloud Scope Statement (ISO 27017 / ISO 27018 Extension)

**Document ID:** CLOUD-SCOPE-001 | **Version:** 1.0 | **Classification:** Internal

This Scope Statement defines the boundary of the cloud security extension to the ISMS for ISO/IEC 27017 and ISO/IEC 27018 audits.

## 1. Organisation
- Legal entity: [Insert legal entity]
- Locations: [Headquarters and operating sites]
- Business activities relevant to cloud: [Describe]

## 2. Cloud Services in Scope

| # | Service | Type | CSP | Role (CSC/CSP) | PII Processed? | Data Classifications |
|---|---------|------|-----|----------------|----------------|----------------------|
| 1 | Customer CRM | SaaS | Provider X | CSC | Yes | Confidential, PII |
| 2 | Internal data lake | IaaS | Provider Y | CSC | Yes | Confidential, PII |
| 3 | Hosted SaaS platform | SaaS | Self | CSP | Yes | Customer PII |
| 4 | Productivity suite | SaaS | Provider Z | CSC | Limited | Internal |

## 3. CSP / CSC Role Declaration
- For services where the organisation is a **CSC**, the customer-side ISO 27017 controls and ISO 27018-aligned due diligence apply.
- For services where the organisation is a **CSP**, the full set of ISO 27017 cloud-only controls and (where PII is involved) ISO 27018 PII processor obligations apply.

## 4. Geographic Scope
- Storage and processing regions: [List regions]
- Cross-border transfer mechanisms: [SCCs / BCRs / adequacy / UAE PDPL approvals]

## 5. Exclusions
List explicitly excluded services with rationale and any compensating controls.

## 6. Interfaces and Dependencies
- Identity provider: [IdP]
- Sub-processors: [Maintained list reference]
- On-premise interfaces: [Connectivity model]

## 7. Standards in Scope
- ISO/IEC 27001:2022 (base ISMS)
- ISO/IEC 27017:2015 (cloud controls)
- ISO/IEC 27018:2019 (PII in public cloud)
- Where applicable: ISO/IEC 27701:2025 (PIMS)

---

*Approved by: CISO + DPO | Date: April 2026*
