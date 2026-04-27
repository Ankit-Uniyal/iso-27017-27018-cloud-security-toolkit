# Non-Conformity & Corrective Action Record — Worked Example

**Document ID:** EVD-NCS-CAR-001
**Version:** 1.0
**Classification:** Internal — Illustrative only
**Owner:** Cloud Security Officer (CSO)

---

## 1. Identification

| Field | Value |
|---|---|
| NC reference | NC-2026-014 |
| Date raised | 2026-03-12 |
| Raised by | Lead internal auditor (J. Doe) |
| Source | Internal audit of folder 11 control A.5.15 (Access Control) and CLD.9.5.1 (Segregation in cloud) |
| Affected scope | Production cloud tenant (eu-west-1) — IAM access reviews |
| Severity | Major |
| Standard / clause | ISO/IEC 27001:2022 A.5.15, A.5.18 ; ISO/IEC 27017:2015 CLD.9.5.1 ; ISO/IEC 27018:2019 A.10.1 |

## 2. Statement of non-conformity

Quarterly access reviews for the production cloud tenant for Q4-2025 were not completed within the cycle defined in the Cloud Acceptable Use Policy and were not evidenced in the GRC tool. Sampling identified seven privileged identities whose access had not been re-attested in the last 180 days, contrary to the documented 90-day cycle.

## 3. Immediate correction (containment)

| # | Action | Owner | Due | Status | Date closed |
|---|---|---|---|---|---|
| 1 | Disable the seven un-attested privileged identities pending re-validation. | Cloud IAM lead | 2026-03-13 | Closed | 2026-03-13 |
| 2 | Re-attest each disabled identity through line manager approval; restore only on approval. | Line managers | 2026-03-19 | Closed | 2026-03-18 |
| 3 | Notify the ISMS Committee of the major NC and interim controls. | CSO | 2026-03-13 | Closed | 2026-03-13 |

## 4. Root-cause analysis (5-Whys)

1. **Why** was the Q4 review not completed? — Reminder workflow in the GRC tool did not fire.
2. **Why** did the workflow not fire? — A schedule change in January 2026 was not migrated to the new GRC instance.
3. **Why** was the schedule not migrated? — The migration runbook did not list scheduled jobs as an in-scope artefact.
4. **Why** was that artefact omitted? — The runbook template predates the GRC tool change and had not been refreshed.
5. **Why** was the template not refreshed? — There is no defined trigger to refresh runbook templates when underlying tooling changes.

**Root cause:** missing change-management linkage between tooling-change tickets and runbook-template refresh.

## 5. Corrective action (systemic fix)

| # | Action | Owner | Due | Status |
|---|---|---|---|---|
| 1 | Add "review and refresh affected runbook templates" as a mandatory checklist item on every tooling-change ticket. | Change Manager | 2026-04-15 | In progress |
| 2 | Re-baseline all GRC scheduled jobs against the Cloud ISMS calendar; reconcile monthly. | Cloud IAM lead | 2026-04-30 | In progress |
| 3 | Add an automated monitor that alerts the CSO when any access-review job has not run in its expected window. | Detection engineering | 2026-05-15 | Open |
| 4 | Update the Cloud Acceptable Use Policy to reference the automated monitor as a compensating control. | CSO | 2026-05-31 | Open |

## 6. Verification of effectiveness

- Verification window: two consecutive review cycles (Q1 + Q2 2026).
- Verification owner: Lead internal auditor.
- Verification evidence: GRC tool job log showing on-time completion; sampled re-attestation records; alert log showing zero misses.
- Closure decision authority: ISMS Committee at the next management review.

## 7. Lessons learned and links

- Lesson: tooling migrations must explicitly cover scheduled compliance jobs.
- Continual Improvement Log (folder 10): linked entry CIL-2026-022.
- Risk Register (folder 05): linked risk R-IAM-007 (residual risk re-rated from High to Medium following corrective action progress).
- Management Review (folder 09): scheduled for review at the Q2-2026 meeting.

## 8. Distribution

CSO, ISMS Committee, Cloud IAM lead, Change Manager, Internal Audit, DPO (information).

---
**Document ID:** EVD-NCS-CAR-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** On closure of NC
