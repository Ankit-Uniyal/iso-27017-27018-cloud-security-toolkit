# Data Processing Addendum (DPA) — Cloud Services Template

**Document ID:** CLOUD-DPA-TPL-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** Legal + DPO | **Review:** Annual

> *Template only. Use under qualified legal review. Adapt jurisdictional clauses as appropriate.*

## Parties

This Data Processing Addendum ("**DPA**") forms part of the master agreement between:

- **[Customer Legal Name]** ("**Controller**" or "**Customer**")
- **[Provider Legal Name]** ("**Processor**" or "**Provider**")

Effective from the latest signature date below.

## 1. Definitions

Terms not defined here have the meaning given in the master agreement and applicable data-protection law (GDPR, UK GDPR, UAE PDPL, India DPDPA, etc.).

## 2. Scope

This DPA applies to all processing of Personal Data by Processor on behalf of Controller in connection with the Services. Annex I details the processing.

## 3. Processor Obligations (Art. 28 GDPR-aligned)

3.1 **Documented instructions.** Processor shall process Personal Data only on documented instructions from Controller, including transfers, except where required by law.

3.2 **Confidentiality.** All persons authorised to process Personal Data are bound by appropriate confidentiality obligations.

3.3 **Security (Art. 32).** Processor implements technical and organisational measures including those described in Annex III, aligned to ISO/IEC 27001:2022, ISO/IEC 27017:2015 and ISO/IEC 27018:2019.

3.4 **Sub-processors.** Processor may engage sub-processors only with prior general authorisation per Annex IV. Processor shall notify Controller of intended changes 30 days in advance and provide an objection mechanism. The Processor remains liable for sub-processor acts.

3.5 **Data Subject Rights.** Processor provides reasonable assistance through technical and organisational measures (DSR portal/API) to enable Controller to fulfil rights under applicable law.

3.6 **Personal Data Breach.** Processor notifies Controller without undue delay (and in any case within 24 hours of Processor's awareness) of a Personal Data Breach affecting Controller's Personal Data, providing information specified in Annex V.

3.7 **DPIA assistance.** Processor assists Controller with DPIAs and prior consultations to the extent reasonably required.

3.8 **Return / deletion.** Upon termination, Processor returns or deletes all Personal Data within 30 days, certifying deletion in writing, except where retention is required by law.

3.9 **Audit.** Processor shall make available all information necessary to demonstrate compliance and allow audits by Controller or its mandated auditor — once per year, with reasonable notice, subject to confidentiality. Independent audit reports (SOC 2, ISO 27001/27017/27018) may satisfy this where reasonable.

## 4. International Transfers

Where Personal Data is transferred outside Controller's jurisdiction to a country without an adequacy determination, the parties incorporate the applicable Standard Contractual Clauses / IDTA / equivalent (specified in Annex II) by reference.

## 5. Liability

The liability provisions of the master agreement apply, subject to mandatory law.

## 6. Governing Law

[Insert governing law per master agreement.]

---

## Annex I — Description of Processing

| Field | Detail |
|-------|--------|
| Subject matter | Provision of [Services] |
| Duration | Term of master agreement |
| Nature & purpose | [...] |
| Categories of Personal Data | [...] |
| Categories of data subjects | [...] |
| Recipients | Sub-processors per Annex IV |
| Frequency | Continuous |

## Annex II — Cross-Border Transfer Mechanisms

| Origin | Destination | Mechanism | Notes |
|--------|-------------|-----------|-------|
| EU/EEA | Provider EU regions | None — within EEA | |
| EU/EEA | US (where applicable) | EU-US DPF / EU SCCs (2021) | TIA on file |
| UK | Non-adequate | UK IDTA | TIA on file |
| UAE | Outside UAE | PDPL transfer mechanism | Per Art. 22-23 |
| India | Outside India | DPDPA s.16 | Per notified-country list |

## Annex III — Technical & Organisational Measures (TOMs)

Aligned to ISO/IEC 27001/27017/27018:

- Encryption at rest (AES-256) and in transit (TLS 1.2+); CMK-supported
- Access control: RBAC, MFA, PAM, JML automation
- Network segregation: per-tenant VPC/SG; private endpoints
- Logging: centralised audit logs; 1y hot retention
- Monitoring: 24×7 SOC; SIEM-correlated alerting
- Vulnerability management: CSPM + scanning + patch SLAs
- Backup & recovery: cross-region; tested DR
- Personnel security: NDAs, background checks, training
- Incident response: 24h notification SLA; runbooks
- Sub-processor management: due diligence and contract terms
- Cryptographic erasure on termination

## Annex IV — Authorised Sub-Processors

The current list is published at [URL] and updated with 30-day notice. Initial list (illustrative):

| Sub-Processor | Service | Region(s) |
|---------------|---------|-----------|
| AWS | Hosting | EU/UAE/US |
| Microsoft Azure | Hosting (India) | IN |
| Stripe | Payments | EU/US |
| Zendesk | Support | EU |

## Annex V — Breach Notification Information

The Processor's notification will include:
- Nature of the breach
- Categories and approximate number of data subjects and records
- Contact details of DPO / privacy office
- Likely consequences
- Measures taken or proposed
- Time of incident discovery

---

## Signatures

| Party | Name | Title | Signature | Date |
|-------|------|-------|-----------|------|
| Controller | | | | |
| Processor | | | | |

---
**Document ID:** CLOUD-DPA-TPL-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
