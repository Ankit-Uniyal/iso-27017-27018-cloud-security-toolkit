# Cross-Mapping — ISO/IEC 27017 + 27018 ↔ CSA CCM v4 & SOC 2 (TSC 2017, AICPA)

**Document ID:** CLOUD-CMM-CSA-SOC2-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Annual

## PART A — CSA Cloud Controls Matrix v4

### A.1 Domain Coverage

| CSA CCM v4 Domain | Toolkit Reference | Maturity |
|-------------------|-------------------|----------|
| AIS — Application & Interface Security | SSDLC; 8.25-8.29 | Defined |
| AAC — Audit & Assurance | Internal Audit Programme; 5.35 | Defined |
| BCR — Business Continuity & Op. Resilience | DR Plan; 5.30 | Defined |
| CCC — Change Control & Configuration | 8.9, 8.32; IaC | Defined |
| CEK — Cryptography, Encryption, Key Mgmt | KMS Procedure; 8.24 | Defined |
| DCS — Datacenter Security | Inherited from CSP | CSP attestation |
| DSI — Data Security & Information Lifecycle | Retention Policy; A.10.x; CLD.8.1.5 | Defined |
| DSP — Data Subject / Privacy | Cloud PII Policy; DSR; 27018 | Defined |
| GRC — Governance, Risk, Compliance | Methodology; SoA; RTP | Defined |
| HRS — Human Resources | Awareness Programme; AUP | Defined |
| IAM — Identity & Access Management | IAM/PAM/MFA | Defined |
| IPY — Interoperability & Portability | Data export; CLD.8.1.5 | Defined |
| IVS — Infrastructure & Virtualization | CLD.9.5.x; hardening | Defined |
| LOG — Logging & Monitoring | CLD.12.4.5; 8.15/8.16 | Defined |
| SEF — Sec Incident Mgmt, E-Discovery, Forensics | Breach Response; 5.24-5.28 | Defined |
| STA — Supply Chain, Transparency, Accountability | Supplier Cloud Assurance; A.7.1 | Defined |
| TVM — Threat & Vulnerability Management | 8.7/8.8; CSPM | Defined |
| UEM — Universal Endpoint Management | MDM; 8.1 | Defined |

### A.2 STAR Assurance Roadmap

| STAR Level | Status | Target Date |
|------------|--------|-------------|
| Level 1 — CAIQ self-assessment | Published | Done |
| Level 2 — STAR Attestation (third-party) | Planned | Year +1 |
| Level 3 — Continuous Auditing | Aspirational | Year +3 |

## PART B — SOC 2 (AICPA TSC 2017, with 2022 points-of-focus)

### B.1 Trust Services Criteria Coverage

#### Common Criteria (CC) — Security (mandatory)

| TSC | Description | Toolkit Reference |
|-----|-------------|-------------------|
| CC1 | Control Environment | Leadership Commitment; AUP; ToR |
| CC2 | Communication & Information | Communications Plan; Awareness |
| CC3 | Risk Assessment | Methodology; Risk Register |
| CC4 | Monitoring | KPI Dashboard; Internal Audit |
| CC5 | Control Activities | SoA controls |
| CC6 | Logical & Physical Access | IAM; PAM; CSP attestation |
| CC7 | System Operations | Monitoring; IR; SIEM |
| CC8 | Change Management | Change procedure; IaC |
| CC9 | Risk Mitigation | RTP; cyber-insurance |

#### Optional Criteria

| TSC | Description | Toolkit Reference |
|-----|-------------|-------------------|
| A1 — Availability | DR/BCP; multi-AZ; DR tests | Yes |
| C1 — Confidentiality | Classification; KMS; access control | Yes |
| PI1 — Processing Integrity | Data quality SLA; integrity hashing | Where applicable |
| P — Privacy | 27018 Annex A; DSR; Privacy Notice | Yes |

### B.2 Recommended Audit Period

- Type I: Point-in-time, after 3 months of operating controls
- Type II: 6-12 month observation period (preferred for customers)

### B.3 Common Bridge Letters

Provided to customers covering the period between SOC 2 audit completion date and current date.

## PART C — Joint Audit Strategy

For organisations pursuing ISO 27001/27017/27018 + SOC 2 + CSA STAR:

1. Maintain a single control library mapped to all three.
2. Sequence external audits to share evidence collection.
3. Reuse Internal Audit Programme as preparation for all external audits.
4. Re-use Cloud Asset Inventory + ROPA across all schemes.

---
**Document ID:** CLOUD-CMM-CSA-SOC2-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
