# Cloud PII Protection Policy (ISO/IEC 27018:2019)

**Document ID:** CLOUD-POL-002 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO

---

## 1. Purpose

This policy defines the controls applied when Personally Identifiable Information (PII) is processed in public cloud environments where the organisation acts as a **PII processor** (CSP role) or as a **PII controller** that has engaged a public cloud PII processor (CSC role). It implements ISO/IEC 27018:2019 in alignment with ISO 27001:2022, ISO 27017:2015 and applicable privacy laws (GDPR, UAE PDPL, etc.).

## 2. Principles

The organisation applies the 11 ISO/IEC 29100 privacy principles when processing PII in the cloud: consent and choice; purpose legitimacy and specification; collection limitation; data minimisation; use, retention and disclosure limitation; accuracy and quality; openness, transparency and notice; individual participation and access; accountability; information security; privacy compliance.

## 3. Policy Statements

### 3.1 Documented Instructions
PII shall be processed only on documented instructions from the PII controller (the CSC), as set out in the Data Processing Agreement (DPA) and CSA.

### 3.2 Purpose Limitation
PII shall not be used for advertising, marketing, profiling or any purpose beyond the contracted scope without the explicit, opt-in consent of the data subject.

### 3.3 Sub-processor Disclosure
A current list of sub-processors shall be maintained and made available to the CSC. Notification shall be provided in advance of any addition or replacement, with a defined objection window.

### 3.4 Sub-processor Flow-down
Sub-processors shall be bound by contract to equivalent PII protection obligations. Due-diligence assessments shall be performed and recorded annually.

### 3.5 Geographic Transparency
The locations of PII storage and processing (regions/countries) shall be disclosed to the CSC. International transfers shall use approved safeguards (SCCs, BCRs, adequacy, equivalent UAE PDPL/India DPDPA mechanisms) and a documented Transfer Impact Assessment (TIA).

### 3.6 Encryption and Key Management
PII shall be encrypted in transit and at rest. CSC-controlled key custody (BYOK / HYOK) shall be supported for sensitive PII categories on customer request.

### 3.7 Breach Notification
PII breaches affecting CSC data shall be notified to the CSC without undue delay and within the contractually agreed SLA (commonly 24–72 hours), with the information needed for the CSC to discharge its own regulatory notification obligations.

### 3.8 Data Subject Rights
The CSP shall provide reasonable cooperation, tools and timelines to enable the CSC to respond to data subject requests (access, rectification, erasure, restriction, objection, portability) within statutory deadlines.

### 3.9 Return, Transfer and Disposal
On contract termination or CSC instruction, PII shall be returned in an agreed format and/or irreversibly deleted. A deletion certificate shall be issued.

### 3.10 Disclosure to Law Enforcement
Mandatory disclosures shall be logged. Where lawful, the CSC shall be notified before disclosure or as soon as the legal restriction lifts.

### 3.11 Personnel Confidentiality and Training
Personnel with access to PII shall sign confidentiality undertakings and complete privacy training appropriate to their role.

### 3.12 Independent Assurance
ISO 27001, ISO 27017, ISO 27018 (and where applicable SOC 2) certifications and audit reports shall be maintained and made available to the CSC under NDA.

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| DPO | Oversight of PII processor obligations; CSC interface; breach lead |
| CISO | Security controls, encryption, incident response |
| Cloud Service Owners | Implement and evidence controls per service |
| Procurement & Legal | DPAs, sub-processor flow-down, transfer mechanisms |

## 5. Compliance and Review

Reviewed annually and on regulatory change. Non-compliance is treated as a privacy nonconformity under the ISMS/PIMS improvement procedure.

---

*Approved by: Top Management | Effective Date: April 2026 | Next Review: April 2027*
