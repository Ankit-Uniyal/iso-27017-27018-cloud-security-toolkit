# Cloud Asset & PII Processing Inventory

**Document ID:** CLOUD-ASSET-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO + DPO | **Review:** Quarterly

## 1. Purpose

Authoritative inventory of cloud assets, processing activities and PII flows. Supports ISO/IEC 27001 cl. 8.1 (Operational Planning), ISO/IEC 27017 (asset awareness in cloud), ISO/IEC 27018 A.9.1 (geographical location of PII), and acts as the ROPA (Record of Processing Activities) for processor obligations.

## 2. Cloud Account / Subscription Inventory

| ID | CSP | Account/Subscription | Purpose | Region(s) | Owner | Criticality |
|----|-----|----------------------|---------|-----------|-------|-------------|
| CA-01 | AWS | prod-eu-1 | Production EU customers | eu-west-1, eu-central-1 | Platform Lead | Critical |
| CA-02 | AWS | prod-us-1 | Production US customers | us-east-1, us-west-2 | Platform Lead | Critical |
| CA-03 | AWS | prod-uae-1 | Production UAE customers | me-central-1 | Platform Lead | Critical |
| CA-04 | AWS | non-prod | Dev/staging | eu-west-1 | Platform Lead | High |
| CA-05 | AWS | security | Centralised logging, GuardDuty | eu-west-1 | SOC | High |
| CA-06 | Azure | prod-india | India customers | centralindia | Platform Lead | Critical |
| CA-07 | Azure | shared-services | IdP, SSO, IAM | West Europe | IAM Lead | Critical |
| CA-08 | GCP | analytics | Aggregated analytics | europe-west4 | Data Eng | Medium |

## 3. Cloud Service Inventory (high-level)

| Service Type | Examples Used | Tenant Model | Data Sensitivity |
|--------------|---------------|--------------|------------------|
| IaaS Compute | EC2, AzureVM | Single-tenant accounts | Up to PII |
| Container | EKS, AKS | Single-tenant cluster | Up to PII |
| Serverless | Lambda, Azure Functions | Multi-tenant runtime | Up to PII |
| Object storage | S3, Blob | Per-account isolation | Up to PII |
| RDBMS | RDS, Azure SQL | Dedicated instances | Up to PII |
| NoSQL | DynamoDB, CosmosDB | Dedicated tables | Up to PII |
| Key management | KMS, Key Vault | CMK per env | Crypto material |
| Identity | IAM Identity Center, Entra ID | Org-level | Auth metadata |
| Logging/Monitoring | CloudTrail, Activity Log, CloudWatch, Sentinel | Centralised | Audit logs (1y+) |
| Email/Comms (SaaS) | Google Workspace, Slack, Zoom | Multi-tenant | Internal docs |
| CRM (SaaS) | Salesforce | Multi-tenant | Customer PII |
| HRIS (SaaS) | Workday | Multi-tenant | Employee PII |

## 4. PII Processing Activities (ROPA)

| ID | Activity | Role | PII Categories | Data Subjects | Lawful Basis | Storage Region | Retention | Sub-Processors | Cross-Border |
|----|----------|------|----------------|---------------|--------------|----------------|-----------|----------------|:------------:|
| P-01 | Customer-app user accounts | Processor | Name, email, IP, usage logs | EU customers' end-users | Customer instruction | eu-west-1 | 7y after termination | AWS, Stripe (EU) | No |
| P-02 | Customer-app user accounts (US) | Processor | Same as P-01 | US end-users | Customer instruction | us-east-1 | 7y | AWS, Stripe (US) | No |
| P-03 | Customer-app user accounts (UAE) | Processor | Same as P-01 | UAE end-users | Customer instruction | me-central-1 | 7y | AWS | No |
| P-04 | Customer-app user accounts (India) | Processor | Same as P-01 | India end-users | Customer instruction | centralindia | 7y | Azure | No |
| P-05 | Support ticket handling | Processor | Email, case content (may contain PII) | Customer end-users | Customer instruction | per-region | 5y | Zendesk | If support follows-the-sun |
| P-06 | Aggregated product analytics | Controller | Pseudonymised events | All end-users | Legitimate interest | europe-west4 | 2y | GCP | Yes (EU→GCP EU only) |
| P-07 | Employee HR records | Controller | Full HR PII | Employees | Contract | EU + US | 7y post-employment | Workday | Yes — SCCs |
| P-08 | Marketing CRM | Controller | Name, email, role, company | B2B prospects | Legitimate interest | EU | Until objection | Salesforce | Yes — SCCs |
| P-09 | Recruitment | Controller | CV data | Candidates | Consent | EU | 6mo | Greenhouse | Yes — SCCs |
| P-10 | Authentication / SSO logs | Controller | Username, IP, device | Employees | Legitimate interest | EU + US | 1y | Entra ID | Inherent in SSO |

## 5. Sub-Processor Register (summary)

| Sub-Processor | Service | Region(s) Used | DPA Status | Sub-processor list URL |
|---------------|---------|----------------|------------|------------------------|
| AWS | Hosting | EU/US/UAE | Signed | aws.amazon.com/compliance/sub-processors |
| Microsoft Azure | Hosting | India + EU | Signed | learn.microsoft.com/.../subprocessors |
| Stripe | Payments | EU/US | Signed | stripe.com/legal/dpa |
| Salesforce | CRM | EU | Signed | salesforce.com/.../infrastructure |
| Workday | HRIS | EU | Signed | workday.com/.../trust |
| Zendesk | Support | EU | Signed | zendesk.com/.../subprocessors |
| Greenhouse | ATS | US (SCCs) | Signed | greenhouse.io/.../privacy |

## 6. Asset Classification

| Class | Examples | Required Controls |
|-------|----------|-------------------|
| Public | Marketing site assets | Integrity only |
| Internal | Internal docs in cloud | Access control |
| Confidential | Source code, designs | Access + encryption |
| Restricted | Customer PII, secrets | Full ISO 27017/27018 + encryption + key segregation |

---
**Document ID:** CLOUD-ASSET-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Quarterly
