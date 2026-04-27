# Cloud — Legal & Regulatory Requirements Register

**Document ID:** CLOUD-LRR-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** Legal / Compliance | **Review:** Semi-annual

## 1. Purpose

Captures all legal, regulatory and contractual requirements applicable to the cloud services in scope, mapped to ISMS controls.

## 2. Privacy & Data Protection Laws

| Jurisdiction | Law | Key Cloud Implications | Mapped Controls | Owner |
|--------------|-----|------------------------|-----------------|-------|
| EU/EEA | GDPR (2016/679) | Lawful basis, DSR, breach notice 72h, transfer mechanisms | A.1.1, A.8.1, A.9.x; SCCs | DPO |
| UK | UK GDPR + DPA 2018 | Equivalent to GDPR | Same as GDPR | DPO |
| Switzerland | revFADP | Similar to GDPR | Same as GDPR | DPO |
| UAE | UAE PDPL (Federal Law 45/2021) | Consent, DSR, cross-border transfer rules | A.1.1, A.8.1, A.9.x | DPO |
| KSA | PDPL (Saudi) | Local-storage requirements for some sectors | A.9.1, A.11.1 | DPO |
| India | DPDPA 2023 | Significant Data Fiduciary, DPO, DPIA | A.1.1, A.8.1 | DPO |
| Brazil | LGPD | DPO, DSR, breach reporting | A.1.1, A.8.1 | DPO |
| USA — California | CCPA/CPRA | Consumer rights, opt-out of sale | A.1.1, A.5.x | DPO |
| USA — Virginia/Colorado/Utah/Connecticut/Texas | State privacy acts | Consumer rights | A.1.1, A.5.x | DPO |
| Singapore | PDPA | Consent, breach notification | A.1.1, A.8.1 | DPO |
| Australia | Privacy Act / NDB | Notifiable Data Breach scheme | A.8.1 | DPO |
| Canada | PIPEDA | Consent, breach notification | A.1.1, A.8.1 | DPO |
| China | PIPL | Data localisation, security assessment | A.9.1, A.11.x | DPO |

## 3. Cyber-Security Laws & Sector Regulations

| Jurisdiction | Law / Regulation | Implication | Owner |
|--------------|------------------|-------------|-------|
| EU | NIS 2 Directive | Incident reporting, supply-chain security | CISO |
| EU | DORA (Financial) | ICT third-party risk; resilience testing | CISO |
| EU | Cyber Resilience Act | Product security obligations | CTO |
| US | SEC Cyber Disclosure Rules | Material incident 8-K within 4 days | CISO |
| US | HIPAA / HITECH | PHI cloud-processor obligations | DPO |
| US | FedRAMP | Federal cloud authorisation | Compliance |
| Global | PCI-DSS v4.0 | Cardholder-data environment in cloud | CISO |
| UAE | NESA / SIA Cloud Policy | Cloud computing regulatory framework | CISO |
| KSA | NCA Essential Cybersecurity Controls | Cloud-cybersecurity controls | CISO |
| India | CERT-In Directions 2022 | 6-hour incident reporting; log retention 180d | CISO |
| Singapore | MAS TRM Guidelines (financial) | Outsourcing/cloud risk management | CISO |

## 4. Industry Standards & Frameworks Tracked

| Framework | Status | Mapped In |
|-----------|--------|-----------|
| ISO/IEC 27001:2022 | Certified / In progress | SoA |
| ISO/IEC 27017:2015 | This toolkit | SoA |
| ISO/IEC 27018:2019 | This toolkit | SoA |
| ISO/IEC 27701:2019 | Adjacent (PIMS) | Cross-mapping |
| CSA STAR / CCM v4 | Self-assessed Level 1 | Cross-mapping |
| NIST CSF 2.0 | Mapped | Cross-mapping |
| SOC 2 Type II | Annual | External attestation |
| FedRAMP Moderate | Roadmap | Cross-mapping |

## 5. Contractual Requirements (cloud-relevant)

| Clause Type | Source | Implication |
|-------------|--------|-------------|
| Data Processing Addendum | Customer DPAs | A.2.1, A.2.2, A.7.1 |
| Sub-processor consent | Customer DPAs | A.7.1 |
| Right to audit | Customer MSAs | Audit-cooperation procedure |
| Breach notification SLA | Customer MSAs | A.8.1 |
| Region pinning | Customer DPAs | A.9.1 |
| Encryption at rest | Customer MSAs | 8.24 |

## 6. Compliance Calendar (annual)

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Privacy regulation horizon scan | Quarterly | DPO |
| Internal compliance audit | Annual | Compliance |
| External certification surveillance | Annual | Compliance |
| Customer DPA renewals | Per contract | Legal |
| Sub-processor reviews | Annual / on-change | Procurement |
| ROPA / processing-record refresh | Annual | DPO |

---
**Document ID:** CLOUD-LRR-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Semi-annual
