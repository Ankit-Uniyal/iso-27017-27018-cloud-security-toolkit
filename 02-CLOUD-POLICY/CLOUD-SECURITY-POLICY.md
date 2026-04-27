# Cloud Security Policy

**Document ID:** CLOUD-POL-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO

---

## 1. Purpose

This policy establishes the security requirements for the use, provision and operation of cloud services in alignment with **ISO/IEC 27017:2015** and (where PII is processed) **ISO/IEC 27018:2019**. It supplements the ISMS information security policy with cloud-specific obligations.

## 2. Scope

This policy applies to all cloud services consumed (CSC role) or provided (CSP role) by the organisation, including IaaS, PaaS and SaaS, and to all employees, contractors and third parties accessing those services.

## 3. Policy Statements

### 3.1 Cloud Service Approval
All cloud services must be assessed and approved by the cloud governance forum before procurement or deployment. No "shadow IT" cloud services are permitted.

### 3.2 Shared Responsibility
A signed Shared Responsibility Matrix must exist for every cloud service in scope, distinguishing between CSP and CSC obligations across identity, data, application, host, network and physical layers (ISO 27017 CLD.6.3.1).

### 3.3 Cloud Service Agreement (CSA)
Every cloud service contract must include security and (where PII is involved) privacy schedules covering: data ownership, encryption, sub-processors, audit rights, breach notification, return/transfer/disposal of data, and exit assistance.

### 3.4 Identity and Access
Cloud identity must be federated to the corporate IdP. MFA is mandatory for all human and privileged accounts. Service accounts and API keys must be rotated and inventoried.

### 3.5 Data Protection
Data must be encrypted in transit (TLS 1.2+) and at rest (AES-256 or equivalent). Customer-managed keys (CMK/BYOK) are required for sensitive and regulated data classes.

### 3.6 Tenant Segregation (CSP role)
The CSP shall enforce tenant segregation in all virtual computing environments, with documented controls and independent assurance (ISO 27017 CLD.9.5.1).

### 3.7 VM and Container Hardening
Virtual machine and container images must conform to approved hardening baselines (CIS Benchmarks or equivalent) and be scanned continuously (ISO 27017 CLD.9.5.2).

### 3.8 Cloud Monitoring
Cloud security events must be logged, retained for the defined period, and integrated to the SIEM. CSP-side logs that affect customer environments must be made available to CSC tenants (ISO 27017 CLD.12.4.5).

### 3.9 PII in the Cloud
Where PII is processed, the requirements of the Cloud PII Policy (ISO 27018-aligned) apply in addition to this policy.

### 3.10 Exit and Termination
On termination of any cloud service, the CSC shall verify the secure return and irreversible deletion of all data and assets within the contractual SLA (ISO 27017 CLD.8.1.5).

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| CISO | Policy ownership, approval, exceptions |
| Cloud Governance Forum | Service approval, risk acceptance |
| Cloud Architects | Reference architectures, baselines |
| Service Owners | Operate controls, evidence |
| Procurement | Contractual schedules and CSAs |
| DPO | PII processor obligations (ISO 27018) |

## 5. Compliance and Exceptions

Non-compliance must be raised as a risk and treated under the ISMS risk procedure. Exceptions require documented CISO approval with compensating controls and review date.

## 6. Review

This policy is reviewed annually and on significant change to the cloud landscape, regulatory environment or contracted services.

---

*Approved by: Top Management | Effective Date: April 2026 | Next Review: April 2027*
