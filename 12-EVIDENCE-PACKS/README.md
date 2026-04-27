# 12 — Evidence Packs (Audit-Ready Records)

## Purpose
This folder stores curated, audit-ready evidence that demonstrates the Cloud ISMS is designed and operating effectively. The structure follows the same control numbering used in the Statement of Applicability (folder 11) so an external auditor can trace each "Implemented" entry to the supporting evidence in minutes.

## Contents
- `NCS-WORKED-EXAMPLE-PACK.md` — End-to-end worked example showing how a non-conformity is identified, root-caused, corrected, verified and closed.
- `NCS-CAR-RECORD-EXAMPLE.md` — Stand-alone non-conformity / corrective-action record (illustrative).
- (recommended) Quarterly access-review extracts, vulnerability scan reports, change-management tickets, supplier review minutes, encryption configuration exports, key-rotation logs, BCP / DR test reports, etc.

## How to use
1. Maintain at least one current-cycle evidence artefact for every "Applicable — Implemented" control in the SoA.
2. Redact PII and customer data before storing evidence in this repository; store sensitive originals in a controlled GRC tool or evidence vault and reference the location here.
3. Name evidence files using the pattern `<CONTROL-ID>_<EVIDENCE-TYPE>_<YYYY-MM-DD>.<ext>` (e.g. `A.5.15_ACCESS-REVIEW_2026-Q1.md`).
4. Refresh evidence on the cadence stated in the SoA (typically quarterly for access reviews, monthly for vulnerability scans, annually for BCP tests).
5. During audits, use the SoA as the index and link each control row to its evidence file in this folder.

## Linked clauses & controls
- ISO/IEC 27001:2022 Clauses 7.5 (documented information), 9.1 (monitoring), 9.2 (audit), 9.3 (review)
- ISO/IEC 27002:2022 control 5.37 (documented operating procedures)
- ISO/IEC 27017:2015 cloud-specific evidence expectations (logs, configurations, shared-responsibility records)
- ISO/IEC 27018:2019 PII processing records, consent records, breach notification records

## Owner
Cloud Security Officer (CSO), with control owners providing source evidence.

---
**Document ID:** 12-README-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** Annual
