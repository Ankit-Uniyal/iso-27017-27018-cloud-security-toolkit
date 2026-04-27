# Cloud ISMS — Context & Issues Register

**Document ID:** CLOUD-CTX-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Annual

## 1. Purpose

This register satisfies ISO/IEC 27001:2022 clause 4.1 (Understanding the organisation and its context) for the Cloud ISMS. It identifies external and internal issues that affect the ability to achieve the intended outcomes of the ISMS in a cloud-services context.

## 2. External Issues (PESTLE-aligned)

| ID | Category | Issue | Impact on Cloud ISMS | Trend | Owner |
|----|----------|-------|----------------------|-------|-------|
| E-01 | Political | Sovereignty / data-localisation pressure (EU, India, KSA, UAE) | Region-pinning, sub-processor restrictions | ↑ | DPO |
| E-02 | Economic | FX volatility affecting CSP pricing | Cost optimisation needed | → | CFO |
| E-03 | Social | Customer privacy expectations rising | Stronger 27018 evidence demanded | ↑ | DPO |
| E-04 | Technological | Rapid CSP service evolution; gen-AI risks | New control gaps emerging | ↑ | CISO |
| E-05 | Legal | GDPR, UAE PDPL, India DPDPA, US state laws | Multi-jurisdiction compliance | ↑ | Legal |
| E-06 | Environmental | Sustainability / carbon reporting | Region selection considerations | ↑ | ESG |
| E-07 | Threat | Cloud-targeted ransomware / nation-state actors | Increased monitoring, IR readiness | ↑ | SOC |
| E-08 | Supply chain | CSP outages, single-vendor concentration | Multi-cloud / DR strategy | → | CTO |
| E-09 | Standards | ISO 27001:2022 transition; CSA STAR L3 | Resource for re-certification | ↑ | Compliance |
| E-10 | Customer | RFPs requiring 27017/27018 evidence | Toolkit must be audit-ready | ↑ | Sales/Legal |

## 3. Internal Issues

| ID | Category | Issue | Impact on Cloud ISMS | Owner |
|----|----------|-------|----------------------|-------|
| I-01 | Governance | Cloud Security Officer role newly defined | Authority/RACI clarity needed | CISO |
| I-02 | Skills | Cloud security skill gap (~2 FTE) | Hiring + training plan | CISO |
| I-03 | Architecture | Multi-cloud (AWS + Azure) heterogeneity | Tooling consolidation needed | CTO |
| I-04 | Change rate | High deployment velocity (CI/CD) | Continuous compliance required | Platform Lead |
| I-05 | Data | Customer PII in 7 regions | 27018 controls critical | DPO |
| I-06 | Tooling | CSPM / SIEM still maturing | Investment plan in RTP | CISO |
| I-07 | Culture | Engineering autonomy vs central guardrails | Paved-road approach | CTO |
| I-08 | M&A | 2 acquisitions in last 24 months | Inheriting unknown cloud estate | COO |
| I-09 | Budget | Security budget 5% of cloud spend | Optimise with automation | CFO |
| I-10 | Documentation | Legacy cloud runbooks scattered | Master document list (see 06-) | CISO |

## 4. Strategic Direction Alignment

| Strategic Objective | ISMS Alignment |
|---------------------|----------------|
| Grow EU & UAE customer base | Strengthen 27018 evidence for RFPs |
| Reduce time-to-onboard | Automated controls; paved-road IaC |
| Maintain 99.9% availability | DR + multi-AZ + CSP-tier choice |
| Sustainability targets | Region selection by carbon-intensity |

## 5. Review Triggers

- New regulation in any operating country
- New CSP service adoption
- Major incident
- M&A activity
- Annual review (default)

---
**Document ID:** CLOUD-CTX-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
