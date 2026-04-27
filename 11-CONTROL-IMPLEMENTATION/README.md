# 11 — Control Implementation (ISO 27001 Annex A + 27017 + 27018)

## Purpose
This folder holds the operational artefacts that evidence implementation of Annex A controls plus the cloud-specific extensions in ISO/IEC 27017:2015 and the PII protections in ISO/IEC 27018:2019. It is the home of the Statement of Applicability (SoA), the per-standard control reference catalogues and CSP/CSC shared-responsibility templates.

## Contents
- `STATEMENT-OF-APPLICABILITY.md` — Authoritative SoA (v2.0) covering all 93 ISO 27001:2022 Annex A controls + 7 ISO 27017 cloud-specific controls + 25 ISO 27018 PII categories, with applicability decision, justification, implementation status and evidence pointers.
- `ISO-27017-CONTROLS-REFERENCE.md` — Implementation guidance, CSP / CSC split and evidence expectations for every clause referenced by 27017.
- `ISO-27018-CONTROLS-REFERENCE.md` — PII-specific guidance, lawful-basis mapping and DPIA triggers for every 27018 category.
- `SHARED-RESPONSIBILITY-MATRIX.md` — Generic CSP-vs-CSC RACI for IaaS, PaaS and SaaS service models.

## How to use
1. Treat the SoA as the single source of truth for control applicability and implementation status. Update at every formal review or whenever scope, services or risk treatment changes.
2. For every "Applicable — Implemented" entry, ensure a corresponding evidence pointer exists in folder 12 (Evidence Packs).
3. For every "Applicable — Planned" entry, ensure a corresponding action exists in the Risk Treatment Plan (folder 05) or Continual Improvement Log (folder 10).
4. Use the Shared-Responsibility Matrix during supplier on-boarding and re-assessment to record which party (CSP, CSC, joint) operates each control.
5. Cross-reference the per-standard catalogues during internal audit (folder 09) to confirm depth of implementation.

## Linked clauses & controls
- ISO/IEC 27001:2022 Clause 6.1.3 d) (production of SoA), Annex A (all controls)
- ISO/IEC 27002:2022 implementation guidance
- ISO/IEC 27017:2015 controls CLD.6.3.1, CLD.8.1.5, CLD.9.5.1, CLD.9.5.2, CLD.12.1.5, CLD.12.4.5, CLD.13.1.4
- ISO/IEC 27018:2019 PII categories A.1 — A.11 (consent, purpose, transparency, transfer, etc.)

## Owner
Cloud Security Officer (CSO), supported by control owners listed in the SoA.

---
**Document ID:** 11-README-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** Annual
