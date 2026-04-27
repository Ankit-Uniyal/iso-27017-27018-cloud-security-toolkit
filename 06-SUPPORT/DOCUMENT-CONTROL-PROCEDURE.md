# Document Control Procedure (Cloud ISMS)

**Document ID:** CLOUD-DCP-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** Compliance Manager | **Review:** Annual

## 1. Purpose

Defines how Cloud ISMS documented information is created, approved, distributed, accessed, retrieved, retained and disposed of, in accordance with ISO/IEC 27001:2022 clause 7.5.

## 2. Scope

All ISMS documents in this repository, plus linked documents in document-management systems, wikis or runbook stores.

## 3. Roles

| Role | Responsibility |
|------|---------------|
| Document Owner | Drafts, maintains, ensures accuracy |
| Approver | Approves prior to publication |
| Compliance Manager | Master register custodian |
| All Users | Use only approved current versions |

## 4. Document Identification

Every controlled document MUST contain:
- **Document ID** (e.g., CLOUD-AUP-001)
- **Version** (semantic, e.g., 1.0, 1.1, 2.0)
- **Classification** (Public / Internal / Confidential / Restricted)
- **Owner** (role)
- **Review cycle** (e.g., Annual / Quarterly)
- **Approval date** (in version-control commit message)

## 5. Document Lifecycle

```
Draft → Review → Approve → Publish → Operate → Review → (Major change?) → Re-approve
                                              → (Obsolete?) → Archive
```

| State | Action | Evidence |
|-------|--------|----------|
| Draft | Author writes; reviewers comment | PR / branch |
| Review | Reviewers + Owner sign off | PR comments / approval |
| Approve | Approver merges to main | Commit history |
| Publish | Stored in repo at /main; communicated | Repo URL |
| Operate | Used in BAU | Reference in evidence |
| Review | Per review-cycle, re-validate | Reviewed-on date in footer |
| Archive | Move to /archive folder; mark obsolete in master list | Archive folder |

## 6. Version Numbering

- **Major (X.0):** content overhaul, scope change, owner change
- **Minor (1.X):** clarifications, formatting, non-substantive updates
- **Patch (0.0.X):** typo fixes — committed without re-approval

## 7. Distribution & Access

- All approved documents are accessible via this GitHub repository.
- Confidential / Restricted documents reside in access-controlled stores; this repo links by reference only.
- External-facing documents (e.g., Privacy Notice) are mirrored to public website.

## 8. Retention

| Class | Retention |
|-------|-----------|
| Active versions | Indefinite while in force |
| Superseded versions | 7 years (audit evidence) |
| Obsolete archived | 7 years after archive date |

## 9. Audit Evidence

- Commit history acts as immutable audit log.
- Pull-request approvals serve as evidence of review.
- Annual review confirmed by Owner via PR titled "Annual review – [Doc ID] – [Year]".

---
**Document ID:** CLOUD-DCP-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
