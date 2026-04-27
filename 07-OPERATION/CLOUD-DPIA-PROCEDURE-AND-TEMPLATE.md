# Cloud Data Protection Impact Assessment (DPIA) — Procedure & Template

**Document ID:** CLOUD-DPIA-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO | **Review:** Annual

## PART A — Procedure

### A.1 Purpose

Defines when and how a DPIA is conducted for cloud-based processing of PII. Aligned with GDPR Art. 35, ISO/IEC 27018 (privacy considerations) and adjacent privacy laws (UAE PDPL, India DPDPA, KSA PDPL).

### A.2 Triggers (DPIA mandatory)

A DPIA is required when proposed cloud processing involves:

1. Systematic and extensive automated decisions with significant effect
2. Large-scale processing of special-category PII
3. Systematic monitoring of public areas / employees
4. New technologies (e.g., GenAI, biometrics, IoT in cloud)
5. Large-scale combining of datasets
6. Cross-border transfer to non-adequate jurisdictions
7. Any processing on regulator's mandatory-DPIA list
8. Change of CSP or major architectural shift in cloud

### A.3 Process

1. **Screening** — owner completes a 10-question screening (DPIA needed yes/no). DPO confirms.
2. **Scoping** — define processing description, data flows, parties.
3. **Necessity & proportionality** — lawful basis, purpose, minimisation.
4. **Risk identification** — privacy + cloud-security risks (combined view).
5. **Risk evaluation** — using Cloud Risk Methodology.
6. **Mitigations** — technical (encryption, pseudonymisation, region pinning), organisational (training, contracts).
7. **Residual-risk decision** — accept / treat further / consult regulator.
8. **DPO opinion** — formal written opinion in template.
9. **Approval** — Risk Owner + DPO + (where required) regulator consultation.
10. **Review** — annually or on change.

### A.4 Roles

| Role | Responsibility |
|------|---------------|
| Project / Product Owner | Initiates DPIA, supplies facts |
| DPO | Methodology owner; signs opinion |
| CSO | Cloud-security risk perspective |
| Legal | Lawful basis, transfer mechanisms |
| Engineering | Architecture, data flows |
| Risk Owner | Accepts residual risk |

### A.5 Records

DPIAs are stored as controlled documents (folder TBD per security classification). DPIA register tracks status.

## PART B — DPIA Template

### B.1 Identification

| Field | Value |
|-------|-------|
| DPIA ID | DPIA-YYYY-NNN |
| Project / Service | |
| Owner | |
| DPO Reviewer | |
| Date initiated | |
| Date approved | |
| Next review | |

### B.2 Processing Description

- **Purpose(s):**
- **Lawful basis (per jurisdiction):**
- **Categories of PII:**
- **Categories of data subjects:**
- **Volume:**
- **Sources of PII:**
- **Recipients (incl. sub-processors):**
- **Cross-border transfers:**
- **Retention period:**
- **Cloud architecture summary (CSP, regions, services):**

### B.3 Necessity & Proportionality

- Why is the processing necessary?
- Could the purpose be achieved with less PII?
- Are individual rights preserved?

### B.4 Consultation

- Data subjects consulted? (where appropriate)
- Internal stakeholders consulted

### B.5 Risk Assessment

| ID | Risk to data subjects / cloud asset | Likelihood | Impact | Score | Existing Mitigations | Residual |
|----|-------------------------------------|:----------:|:------:|:-----:|----------------------|:--------:|
| | | | | | | |

### B.6 Mitigations & Treatment

| Mitigation | Owner | Due | Status |
|------------|-------|-----|:------:|
| | | | |

### B.7 DPO Opinion

[Free text; recommendation: proceed / proceed with mitigations / do not proceed / consult regulator.]

### B.8 Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Owner | | | |
| DPO | | | |
| Risk Owner | | | |

---
**Document ID:** CLOUD-DPIA-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
