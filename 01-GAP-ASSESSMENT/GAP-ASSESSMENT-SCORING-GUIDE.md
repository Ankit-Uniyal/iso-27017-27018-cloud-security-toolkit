# Gap Assessment Scoring Guide

**Standard:** ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019
**Document ID:** GAP-SCORE-001
**Version:** 1.0
**Classification:** Internal

---

## 1. Purpose
This guide standardises how the organisation rates control implementation maturity during a gap assessment, so that results are repeatable, comparable across assessors and meaningful when tracked over time. It supports the Cloud Gap Assessment Checklist and the `cloud_gap_checker.py` script in folder 13.

## 2. When to use
- Before initial certification (baseline assessment)
- After significant scope, service or supplier change
- Annually as input to the Management Review (folder 09)
- After any major incident, audit finding or regulatory change

## 3. Scoring scale (CMMI-style, 0 — 5)

| Score | Label | Definition | Typical Evidence |
|---|---|---|---|
| 0 | Not Performed | Control is not implemented; no documented intent. | None. |
| 1 | Initial / Ad-hoc | Control is performed reactively or by individual effort, undocumented. | Informal notes, screenshots, ticket comments. |
| 2 | Repeatable | Control is documented but not consistently applied across the cloud estate. | Draft procedure, partial coverage logs. |
| 3 | Defined | Control is documented, approved, applied consistently and integrated with the ISMS. | Approved procedure, training record, sample logs. |
| 4 | Managed | Control performance is measured against KPIs / KRIs and reviewed at defined intervals. | KPI dashboards, periodic review minutes, exception logs. |
| 5 | Optimised | Control is continually improved using metrics, automation and lessons learned. | Trend analysis, automation scripts, improvement actions closed. |

**Pass threshold for certification readiness:** average score >= 3.0 across all applicable controls, with no individual control below 2.

## 4. Scoring procedure

1. **Confirm applicability.** Use the Statement of Applicability (folder 11) to confirm the control is in scope. If "Not Applicable", record N/A and skip.
2. **Identify the control owner.** Record the named owner; an unnamed owner caps the score at 1.
3. **Inspect documentation.** Is there an approved, current procedure? Missing or draft caps the score at 2.
4. **Inspect operation.** Sample at least 3 records / time periods. Inconsistent operation caps the score at 2.
5. **Inspect measurement.** Are KPIs / KRIs defined and reviewed? Absence caps the score at 3.
6. **Inspect improvement.** Are improvements traceable to metrics or lessons learned? Absence caps the score at 4.
7. **Record the score, evidence references and the gap statement.**

## 5. Cloud-specific scoring adjustments (ISO 27017 + 27018)

- **Shared-responsibility clarity:** if the CSP / CSC split is not documented for the control, cap at 2 regardless of operation.
- **Multi-tenant isolation:** for controls touching tenant separation (e.g. CLD.9.5.1, CLD.9.5.2), require CSP attestation evidence to score above 3.
- **Cross-border PII transfer:** for 27018-aligned controls, require a documented transfer mechanism (SCCs, adequacy decision, BCRs) to score above 3.
- **Encryption & key management:** require evidence of key custody, rotation cadence and HSM / KMS attestation to score 4 or 5.
- **Sub-processor management:** for 27018, require an up-to-date sub-processor list with customer notification mechanism to score above 3.

## 6. Aggregation and reporting

- **Per clause:** average across all in-scope controls in that clause.
- **Per Annex A theme:** average across the four themes (5 Organisational, 6 People, 7 Physical, 8 Technological).
- **Overall Cloud ISMS readiness percentage:** `(sum of scores / (5 x count of applicable controls)) x 100`.
- Track quarter-on-quarter; a sustained downward trend in any theme is itself a non-conformity candidate.

## 7. Common scoring errors to avoid

- Treating "we have a policy" as score 3 without checking operation.
- Scoring 5 without quantitative evidence of improvement.
- Failing to cap when ownership or shared-responsibility split is undocumented.
- Aggregating across non-applicable controls (always exclude N/A from averages).
- Allowing the same assessor to both implement and score a control (segregation of duties).

## 8. Inputs and outputs

**Inputs:** SoA (folder 11), Risk Register (folder 05), procedures (folders 04, 06, 07, 08), evidence (folder 12), supplier records (folder 08).

**Outputs:** completed Gap Assessment Checklist with per-control scores; gap report; updated Risk Treatment Plan; updated Continual Improvement Log (folder 10).

---
**Document ID:** GAP-SCORE-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** Annual
