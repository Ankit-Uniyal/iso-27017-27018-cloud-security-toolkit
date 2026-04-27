# Cloud Risk Assessment Methodology

**Document ID:** CLOUD-RAM-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Annual

## 1. Purpose & Scope

This methodology defines how cloud information-security and PII risks are identified, analysed, evaluated and treated in line with ISO/IEC 27001:2022 (clause 6.1), ISO/IEC 27005:2022, ISO/IEC 27017:2015 and ISO/IEC 27018:2019. It applies to all cloud services (IaaS/PaaS/SaaS) consumed or provided by the organisation.

## 2. Roles

| Role | Responsibility |
|------|---------------|
| Risk Owner | Accept residual risk; fund treatment |
| CISO | Oversight; methodology custodian |
| Cloud Security Officer | Cloud-risk identification & analysis |
| DPO | PII-risk view; co-owner for 27018 risks |
| Asset Owners | Identify cloud assets in scope |

## 3. Asset & Threat Identification

### 3.1 Cloud Assets
- Workloads (VMs, containers, serverless)
- Data stores (object, block, DB-as-a-service)
- Identity & secrets stores
- Network primitives (VPC, gateways, DNS)
- CSP control-plane access

### 3.2 Threat Catalogue (cloud-specific)
1. Mis-configuration of cloud resources
2. Compromised cloud admin credentials
3. Multi-tenant isolation failure
4. Insider threat at CSP
5. Sub-processor compromise
6. Data exfiltration via public endpoint
7. Cross-border transfer non-compliance
8. Loss of CSP availability
9. Insufficient logging/forensics
10. Supply-chain compromise of CSP code

### 3.3 Vulnerability Sources
- CSP shared-responsibility gaps
- Default-permissive configurations
- Missing encryption (data-at-rest / in-transit)
- Inadequate IAM hygiene
- Lack of continuous monitoring

## 4. Risk Analysis — Likelihood & Impact

### 4.1 Likelihood Scale
| Score | Label | Frequency Guidance |
|:-----:|-------|---------------------|
| 1 | Rare | < once / 5 years |
| 2 | Unlikely | Once / 2-5 years |
| 3 | Possible | Once / year |
| 4 | Likely | Multiple / year |
| 5 | Almost certain | Monthly+ |

### 4.2 Impact Scale (5 dimensions)
| Score | Confidentiality | Integrity | Availability | Privacy (PII) | Financial |
|:-----:|-----------------|-----------|--------------|---------------|-----------|
| 1 | Negligible | Cosmetic | < 1h outage | < 10 records | < 10k |
| 2 | Minor | Minor inaccuracy | 1-4h | 10-100 | 10-50k |
| 3 | Moderate | Significant | 4-24h | 100-1k | 50-250k |
| 4 | Major | Major | 1-3 days | 1k-10k | 250k-1M |
| 5 | Catastrophic | Systemic | > 3 days | > 10k or special-category | > 1M |

### 4.3 Risk Scoring Formula

`Risk = Likelihood × max(Impact dimensions)`

### 4.4 Risk Matrix

|        | I=1 | I=2 | I=3 | I=4 | I=5 |
|--------|:---:|:---:|:---:|:---:|:---:|
| L=5    | M   | H   | H   | C   | C   |
| L=4    | L   | M   | H   | H   | C   |
| L=3    | L   | M   | M   | H   | H   |
| L=2    | L   | L   | M   | M   | H   |
| L=1    | L   | L   | L   | M   | M   |

L=Low, M=Medium, H=High, C=Critical.

## 5. Risk Evaluation Criteria

| Risk Level | Action Required | Approval |
|------------|-----------------|----------|
| Critical | Treat within 30 days | Board |
| High | Treat within 90 days | CISO + Risk Committee |
| Medium | Treat within 6 months | Risk Owner |
| Low | Monitor; treat opportunistically | Risk Owner |

## 6. Treatment Selection (linked to RTP)

Treatments: Modify (M), Avoid (A), Share (S), Retain (R). See CLOUD-RISK-TREATMENT-PLAN.md.

## 7. Cloud-Specific Considerations

- **Shared Responsibility:** explicitly record CSP/CSC/Shared on every risk row.
- **Region/Jurisdiction:** assess legal exposure for each region.
- **Data classification:** PII triggers additional 27018 considerations.
- **Supply chain:** include 4th-party (sub-processor) risk.

## 8. Review Cycle

- Strategic risk review: annual
- Operational risk register update: quarterly
- Trigger-based review: new service onboarding, major incident, regulatory change.

## 9. Records & Evidence

- Cloud Risk Register (05-PLANNING/CLOUD-RISK-REGISTER.md)
- Cloud Risk Treatment Plan (05-PLANNING/CLOUD-RISK-TREATMENT-PLAN.md)
- Risk Committee minutes
- Acceptance letters for retained risks

---
**Document ID:** CLOUD-RAM-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
