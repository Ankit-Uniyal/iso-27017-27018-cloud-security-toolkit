# 14 — Cross-Mapping (Multi-Framework Alignment)

## Purpose
This folder cross-references the ISO/IEC 27001:2022 + 27017:2015 + 27018:2019 control set against major adjacent frameworks so that organisations operating in multi-regulatory environments can re-use a single set of controls and evidence for several certification or compliance objectives.

## Contents
- `27001-27017-27018-CROSS-MAPPING.md` — Master mapping of ISO 27001 Annex A controls to 27017 cloud extensions and 27018 PII categories.
- `GDPR-MAPPING.md` — Article-by-article mapping of EU GDPR to ISO controls (lawful basis, DPIA, breach notification, transfer rules).
- `NIST-CSF-MAPPING.md` — Mapping to NIST Cybersecurity Framework v2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover).
- `CSA-CCM-SOC2-MAPPING.md` — Mapping to CSA Cloud Controls Matrix v4 and AICPA SOC 2 Trust Services Criteria.
- `FEDRAMP-UAE-PDPL-INDIA-DPDPA-MAPPING.md` — Mapping to US FedRAMP Moderate baseline, UAE Federal PDPL and India DPDPA 2023.

## How to use
1. Identify which adjacent frameworks apply to your organisation (regulator, customer contract, market access).
2. Use the relevant mapping file to confirm coverage gaps before scoping a new audit or certification.
3. When a control already exists in the SoA, re-use the same evidence rather than creating duplicate processes.
4. Where a framework introduces a genuinely new requirement (e.g. data localisation under UAE PDPL), raise a risk in folder 05 and a corresponding control / improvement.
5. Refresh mappings whenever a referenced framework publishes a new major version.

## Linked clauses & controls
- ISO/IEC 27001:2022 Clauses 4.2 (interested parties), 4.3 (scope), 6.1.3 (risk treatment)
- ISO/IEC 27017:2015 cloud-specific extensions
- ISO/IEC 27018:2019 PII protections
- External: GDPR (EU 2016/679), NIST CSF v2.0, CSA CCM v4, AICPA SOC 2 TSC, FedRAMP Rev. 5, UAE Federal PDPL, India DPDPA 2023

## Owner
Cloud Security Officer (CSO) and Data Protection Officer (DPO), supported by Legal.

---
**Document ID:** 14-README-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** Annual
