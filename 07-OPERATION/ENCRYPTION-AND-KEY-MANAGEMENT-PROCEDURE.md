# Encryption & Key Management Procedure (Cloud)

**Document ID:** CLOUD-KMS-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** Cryptography Lead / CSO | **Review:** Annual

## 1. Purpose

Defines requirements for the use of cryptography in cloud services, satisfying ISO/IEC 27001:2022 control 8.24, ISO/IEC 27017 cloud guidance, and ISO/IEC 27018 A.10.6 (encryption of PII in transit) and A.10.13 (residual-data protection).

## 2. Cryptographic Standards

| Use | Algorithm Minimum | Notes |
|-----|-------------------|-------|
| Symmetric encryption (data at rest) | AES-256-GCM | CSP-managed or CMK |
| Asymmetric (TLS, signing) | RSA 3072+ or ECDSA P-256+ | Quantum-readiness review by 2027 |
| Hashing (passwords) | Argon2id (or bcrypt cost ≥ 12) | NEVER MD5/SHA1 |
| Hashing (integrity) | SHA-256+ | |
| TLS | 1.2 minimum, prefer 1.3 | HSTS, OCSP stapling |
| Signing | EdDSA / ECDSA | |
| Random | OS CSPRNG / KMS Generate | |

## 3. Key Lifecycle

| Stage | Requirement |
|-------|-------------|
| Generation | In hardware-backed KMS (CSP HSM-backed); never on local devices |
| Distribution | Never distribute private/symmetric keys; envelope encryption |
| Storage | Always in KMS / HSM; never in code, repos, env vars |
| Use | Authenticated, audited; least privilege per CMK |
| Rotation | Customer Master Keys: ≤ 1 year; Data keys: per-object envelope |
| Archival | Versioned in KMS; ciphertext re-encrypted opportunistically |
| Destruction | Schedule key deletion 7-30d (recoverable) then irreversible |

## 4. Key Hierarchy

```
Customer Master Key (CMK in KMS, HSM-backed)
   ↓ wraps
Data Encryption Key (DEK, per object/dataset)
   ↓ encrypts
Plaintext data
```

- CMK never leaves KMS
- DEKs are short-lived; cached in memory only

## 5. Key Custody Models

| Model | Description | When Used |
|-------|-------------|-----------|
| CSP-managed | CSP holds and manages keys | Internal low-sensitivity data |
| Customer-Managed Key (CMK) in CSP-KMS | We define key policy in CSP KMS | Default for customer PII |
| Bring Your Own Key (BYOK) | We import key material; CSP stores | Regulated customers |
| Hold Your Own Key (HYOK) / External KMS | Key never leaves our HSM/external KMS | Highly regulated; rare |

## 6. Key Policy & Access

- Each CMK has a documented key policy describing which IAM principals can use, manage, or rotate.
- Separation of duties: key administrators ≠ key users.
- Break-glass: explicit, monitored, time-bound.
- All key operations logged in CSP audit log; forwarded to SIEM with alert on unusual access.

## 7. PII-Specific Requirements (27018)

- All PII at rest encrypted with CMK in origin region.
- Cryptographic erasure (CMK destruction) supported as deletion mechanism for tenant termination.
- Cross-border PII movement requires CMK in origin jurisdiction (where law mandates).

## 8. Secrets Management (operational)

- Application secrets stored in vault (CSP Secrets Manager / HashiCorp Vault).
- Static secrets prohibited in code or configuration files.
- Secret-scanning enabled on all repos; broken-glass rotation procedure defined.

## 9. Quantum-Readiness

- Track NIST PQC standards (Kyber, Dilithium).
- Maintain crypto-agility: algorithm choices abstracted; rotation plan documented.

## 10. Key Compromise Response

- Treat as a security incident (Cloud Breach Response Procedure).
- Immediately revoke key, re-encrypt affected data with new CMK.
- Notify customers per DPA.

## 11. Records

- KMS configuration export (annual)
- Rotation evidence (CMK rotation timestamps)
- Access-review records (quarterly)
- Compromise / break-glass log

---
**Document ID:** CLOUD-KMS-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
