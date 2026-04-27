# Cloud Risk Treatment Plan

**Document ID:** CLOUD-RTP-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO / Cloud Security Officer | **Review:** Quarterly

## 1. Purpose

This Risk Treatment Plan documents the chosen treatment for every cloud risk identified in the Cloud Risk Register (05-PLANNING/CLOUD-RISK-REGISTER.md), aligned with ISO/IEC 27001:2022 clause 6.1.3 and ISO/IEC 27017/27018 cloud-specific risk considerations.

## 2. Treatment Options

| Option | Code | Description |
|--------|------|-------------|
| Modify | M | Reduce likelihood/impact via controls |
| Avoid | A | Eliminate the activity |
| Share | S | Transfer to CSP / insurer / 3rd party |
| Retain | R | Accept residual risk with formal sign-off |

## 3. Treatment Plan

| Risk ID | Risk Description | Inherent | Treatment | Controls Applied (27017/27018/27002) | Owner | Target Date | Residual | Status |
|---------|------------------|:--------:|:---------:|--------------------------------------|-------|-------------|:--------:|:------:|
| R-CL-01 | Multi-tenant data leakage between CSP customers | High | M+S | CLD.9.5.1, 8.24, CSP attestations | Cloud Sec Lead | Q1 | Low | Open |
| R-CL-02 | Loss of visibility into CSP infrastructure | Medium | M | CLD.12.4.5, 8.15, 8.16 | SOC Manager | Q1 | Low | Open |
| R-CL-03 | Vendor lock-in / portability | Medium | M | Multi-cloud strategy; data export tooling | CTO | Q2 | Medium | Open |
| R-CL-04 | Cross-border PII transfer non-compliance | High | M | A.9.1, A.9.2, region pinning, SCC | DPO | Q1 | Low | Open |
| R-CL-05 | Insufficient CSP breach notification | High | M+S | A.8.1, contractual 24h SLA | DPO | Q1 | Low | Open |
| R-CL-06 | Mis-configured IaaS resources (public S3, open SG) | High | M | 8.9, IaC + drift detection, CSPM | Platform Lead | Q1 | Low | Open |
| R-CL-07 | Compromised cloud admin credentials | High | M | CLD.12.1.5, 8.2, PAM + MFA | IAM Lead | Q1 | Low | Open |
| R-CL-08 | Sub-processor non-compliance | Medium | M | A.7.1, A.10.11, A.10.12 | Procurement | Q2 | Low | Open |
| R-CL-09 | Inadequate VM/container hardening | Medium | M | CLD.9.5.2, 8.7, 8.8 | Platform Lead | Q1 | Low | Open |
| R-CL-10 | Encryption key compromise | High | M | 8.24, KMS w/ CMK, key rotation | Crypto Lead | Q1 | Low | Open |
| R-CL-11 | DDoS / availability disruption | Medium | M+S | 8.6, CSP DDoS service, multi-AZ | SRE Lead | Q1 | Low | Open |
| R-CL-12 | Inadequate evidence for audit (insufficient logs) | Medium | M | 8.15, central log archive ≥1y | SOC Manager | Q1 | Low | Open |
| R-CL-13 | Loss of customer data on termination | Medium | M | CLD.8.1.5, A.11.2, deletion certificate | Account Mgmt | Q2 | Low | Open |
| R-CL-14 | Shadow IT / unsanctioned cloud usage | Medium | M | 5.23, CASB, allowlist | CISO | Q2 | Low | Open |
| R-CL-15 | Forensic readiness limitation in cloud | Medium | M | 5.28, IR runbook + CSP forensic API | IR Lead | Q3 | Medium | Open |

## 4. Funding & Resource Allocation

| Treatment Programme | CapEx | OpEx | FTE | Source |
|---------------------|-------|------|-----|--------|
| CSPM tooling | 50k | 30k/y | 0.5 | Security budget |
| PAM rollout | 80k | 40k/y | 1.0 | Security budget |
| KMS migration to CMK | 10k | 5k/y | 0.25 | Platform budget |
| SIEM expansion (cloud logs) | 60k | 80k/y | 1.0 | Security budget |
| Annual CSP audit/review | — | 20k/y | 0.25 | Compliance budget |

## 5. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | | | |
| DPO | | | |
| Risk Committee Chair | | | |

---
**Document ID:** CLOUD-RTP-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Quarterly
