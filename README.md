# ISO/IEC 27017:2015 & ISO/IEC 27018:2019 Cloud Security Toolkit

A practical, audit-ready implementation toolkit for **ISO/IEC 27017:2015** (Code of Practice for Information Security Controls based on ISO/IEC 27002 for Cloud Services) and **ISO/IEC 27018:2019** (Code of Practice for Protection of PII in Public Clouds Acting as PII Processors) — extending **ISO 27001:2022** and **ISO 27002:2022** with cloud-specific controls and PII protection requirements for Cloud Service Providers (CSPs) and Cloud Service Customers (CSCs).

> Updated: April 2026 | Standards: ISO/IEC 27017:2015 + ISO/IEC 27018:2019 | Aligned: ISO 27001:2022 / ISO 27002:2022

---

## What This Toolkit Contains

- All **ISO 27017 cloud-extended controls** (37 ISO 27002 controls with cloud-specific guidance + 7 cloud-only controls)
- All **ISO 27018 PII-in-public-cloud controls** (Annex A: 25 PII processor controls, organised under 11 privacy principles)
- **Cloud Gap Assessment** covering both standards mapped to ISO 27002:2022
- **Cloud Risk Register** with CSP/CSC shared-responsibility risk methodology
- **Statement of Applicability (SoA)** for ISO 27017 + ISO 27018 controls
- **Shared Responsibility Matrix** templates (IaaS / PaaS / SaaS)
- **Cloud Service Agreement (CSA) review checklist**
- **PII Processing Notice** templates aligned to ISO 27018
- **Cross-mapping** to GDPR, UAE PDPL, NIST CSF 2.0, CSA CCM v4, SOC 2, FedRAMP
- **Worked examples** for a fictional organisation (Nexus Cloud Services Ltd)
- **Python GRC automation scripts** for SoA tracking, gap checking and DPIA scoring, with sample inputs, unit tests and CI

## Standards Overview

| Standard | Scope | Audience |
|----------|-------|----------|
| **ISO/IEC 27017:2015** | Cloud-specific extension to ISO 27002 — security controls for cloud services | Both CSPs and CSCs |
| **ISO/IEC 27018:2019** | Protection of Personally Identifiable Information (PII) in public clouds acting as PII processors | Public cloud CSPs (PII processors) |

Both standards are certifiable extensions to ISO/IEC 27001 and are usually audited together with the ISMS.

## Repository Structure

| # | Folder / File | Contents |
|---|---------------|----------|
| — | README.md | This file — full index and navigation guide |
| — | 00-IMPLEMENTATION-GUIDE.md | How to use this toolkit; cloud security implementation roadmap |
| 1 | 01-GAP-ASSESSMENT/ | Cloud security gap assessment checklist (27017 + 27018) |
| 2 | 02-CLOUD-POLICY/ | Cloud Security Policy, Cloud PII Policy, Acceptable Use |
| 3 | 03-SCOPE-AND-CONTEXT/ | Cloud scope, CSP/CSC roles, interested parties, legal register |
| 4 | 04-LEADERSHIP/ | Cloud governance, roles, RACI, PII processor responsibilities |
| 5 | 05-PLANNING/ | Cloud risk assessment, treatment, SoA (27017 + 27018 controls) |
| 6 | 06-SUPPORT/ | Cloud competence, awareness, communications, documented info |
| 7 | 07-OPERATION/ | Shared responsibility, CSA review, PII processing, breach response, returns/transfers |
| 8 | 08-PERFORMANCE/ | Cloud KPIs, internal audit, management review |
| 9 | 09-IMPROVEMENT/ | Nonconformities, corrective actions, continual improvement |
| 10 | 10-ISO27017-CONTROLS/ | ISO 27017 cloud control reference (CLD.6.3, CLD.8.1, CLD.9.5, CLD.12.1, CLD.12.4, CLD.13.1) |
| 11 | 11-ISO27018-CONTROLS/ | ISO 27018 PII-in-public-cloud control reference (Annex A extensions) |
| 12 | 12-EVIDENCE-PACKS/ | Audit-ready evidence pack templates (access reviews, vulnerability scans, CAR records) |
| 13 | 12-WORKED-EXAMPLE/ | Fictional Nexus Cloud Services worked implementation *(folder retains "12-" prefix; see Version History)* |
| 14 | 13-SCRIPTS/ | Python GRC automation scripts + samples/ + tests/ (requirements.txt included) |
| 15 | 14-CROSS-MAPPING/ | GDPR, UAE PDPL, NIST CSF 2.0, CSA CCM, SOC 2, FedRAMP cross-mapping |
| 16 | 15-SUPPLEMENTARY-TEMPLATES/ | Shared-responsibility matrix, CSA checklist, supplier assurance, PII notice |

## ISO 27017 — Cloud-Only Controls Quick Reference

| Control | Title | Applies To |
|---------|-------|-----------|
| CLD.6.3.1 | Shared roles and responsibilities within a cloud computing environment | CSP + CSC |
| CLD.8.1.5 | Removal of cloud service customer assets | CSP |
| CLD.9.5.1 | Segregation in virtual computing environments | CSP |
| CLD.9.5.2 | Virtual machine hardening | CSP + CSC |
| CLD.12.1.5 | Administrator's operational security | CSP |
| CLD.12.4.5 | Monitoring of cloud services | CSP |
| CLD.13.1.4 | Alignment of security management for virtual and physical networks | CSP |

In addition, ISO 27017 provides cloud-specific implementation guidance for 37 existing ISO 27002 controls.

## ISO 27018 — PII-in-Public-Cloud Annex A Extension

ISO 27018 extends ISO 27002 with **25 PII processor controls** (Annex A), organised under **11 privacy principles** (aligned to ISO 29100):

1. Consent and choice
2. Purpose legitimacy and specification
3. Collection limitation
4. Data minimization
5. Use, retention and disclosure limitation
6. Accuracy and quality
7. Openness, transparency and notice
8. Individual participation and access
9. Accountability
10. Information security
11. Privacy compliance

Key obligations include: explicit purpose limitation, no use of PII for marketing/advertising without consent, sub-processor disclosure, PII return/transfer/disposal, breach notification to the CSC, and geographic transparency for PII storage.

## Cross-Mapping

This toolkit cross-maps ISO 27017 + ISO 27018 controls to:

- **GDPR** — Articles 28, 32, 33, 44–49 (processor + transfer obligations)
- **UAE PDPL** — Federal Decree-Law No. 45 of 2021
- **NIST CSF 2.0** — Govern / Identify / Protect / Detect / Respond / Recover
- **CSA Cloud Controls Matrix v4** — 17 domains
- **SOC 2 Trust Services Criteria** — Security, Availability, Confidentiality, Processing Integrity, Privacy
- **FedRAMP Moderate** — NIST SP 800-53 baseline
- **ISO/IEC 27701:2019** — PIMS extension cross-reference

## Automation Scripts

The 13-SCRIPTS/ folder contains three Python tools plus supporting assets:

- cloud_soa_tracker.py — SoA implementation progress (optional CSV input)
- cloud_gap_checker.py — gap-assessment conformance + critical-gap flagging
- dpia_cloud_scorer.py — deterministic DPIA risk score + verdict
- samples/ — controls_master.csv (canonical control list), gap_assessment.csv, soa.csv, dpia.yaml
- tests/ — pytest unit tests
- .github/workflows/ci.yml runs compile checks and tests on every push/PR

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 2026 | Initial release — ISO/IEC 27017:2015 + ISO/IEC 27018:2019 toolkit aligned to ISO 27001:2022 |
| 1.1 | April 2026 | Added evidence pack templates, added requirements.txt, moved AUP to 02-CLOUD-POLICY |
| 1.2 | April 2026 | Fixed GRC scripts (indentation, CSV-driven SoA tracker, corrected critical-gap matching, aligned DPIA verdicts); added canonical controls_master.csv, sample inputs, pytest tests and CI workflow; reconciled PII control count to 25 and corrected ISO 27701 reference to :2019 |

> **Known structural note:** folders 12-EVIDENCE-PACKS and 12-WORKED-EXAMPLE currently share the "12-" numeric prefix. This is a cosmetic naming overlap only; both folders exist and are independent. A future release will renumber 12-WORKED-EXAMPLE.

Maintained by **Ankit Uniyal** — ISO 27001 Lead Auditor | GRC Lead

See 00-IMPLEMENTATION-GUIDE.md for the full implementation roadmap.

---

> ISO/IEC 27017 + 27018 Cloud Security Toolkit | README | CLOUD-README-001 | v1.2 | Classification: Public
