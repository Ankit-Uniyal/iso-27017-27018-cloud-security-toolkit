# Cloud ISMS — Continual Improvement Log

**Document ID:** CLOUD-CIL-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Quarterly

## 1. Purpose

Captures opportunities for continual improvement (OFIs) of the Cloud ISMS, satisfying ISO/IEC 27001:2022 clause 10.1. Sources: audits, NCRs, KPI shortfalls, threat-landscape changes, customer feedback, management review.

## 2. Status Codes

| Code | Meaning |
|------|---------|
| Open | Logged, not yet evaluated |
| Evaluated | Cost/benefit assessed |
| Approved | Accepted; in delivery |
| Implemented | Change deployed |
| Verified | Effectiveness confirmed |
| Closed | Closed (with or without action) |

## 3. Improvement Log

| ID | Date | Source | Description | Linked NCR / Audit / KPI | Owner | Priority | Status | Closure Evidence |
|----|------|--------|-------------|--------------------------|-------|:--------:|:------:|------------------|
| CIL-25-001 | 2026-Q1 | Internal audit | Standardise paved-road IaC across AWS + Azure | IA-25-02 | Platform Lead | High | Open | |
| CIL-25-002 | 2026-Q1 | KPI shortfall | CSPM critical-finding MTTR > 14d in eu-west-1 | KPI dashboard | CSO | High | Open | |
| CIL-25-003 | 2026-Q1 | Threat intel | Add detection for token-replay in IdP | Threat intel feed | SOC | Medium | Open | |
| CIL-25-004 | 2026-Q1 | Customer feedback | Trust Centre lacks SOC 2 Type II latest | Customer ticket | Trust | Medium | Open | |
| CIL-25-005 | 2026-Q1 | Mgmt review | Quarterly tabletop on data-exfil scenario | MR-25-Q1 | SOC | Medium | Open | |
| CIL-25-006 | 2026-Q1 | NCR | Sub-processor list 30-day notice missed once | NCR-25-002 | DPO | High | Open | |
| CIL-25-007 | 2026-Q1 | Self-assessment | CSA CCM v4 score below target in DSI-04 | CSA review | CSO | Low | Open | |
| CIL-25-008 | 2026-Q1 | Audit | DPIA template unused for new AI feature | IA-25-03 | DPO | High | Open | |
| CIL-25-009 | 2026-Q2 | Regulatory | India DPDPA rules — adjust DSR procedure | LRR | DPO | High | Open | |
| CIL-25-010 | 2026-Q2 | Performance | Reduce SIEM ingest cost by 20% via tiered logs | KPI | SOC | Medium | Open | |

## 4. Effectiveness Verification

For each implemented improvement:
- Verify outcome against original problem statement
- Record evidence (metrics, audit observation, customer feedback)
- Communicate closure to original raiser
- Update KPI baseline if applicable

## 5. Reporting

Quarterly summary in Management Review:
- Total opened
- Total closed (with effectiveness verified)
- Aging analysis
- Top 5 by impact

---
**Document ID:** CLOUD-CIL-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Quarterly

