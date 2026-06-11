"""
cloud_gap_checker.py
Cloud ISMS Gap Checker - ISO/IEC 27017 + 27018

Reads a CSV gap-assessment file, computes per-domain conformance scores,
flags critical gaps, and produces a Markdown summary report.

Usage:
    python cloud_gap_checker.py --input gap_assessment.csv --output gap_report.md

CSV columns expected:
    Control_ID, Domain, Title, Status, Owner, Evidence, Notes

Status values: Implemented | Partial | Not_Implemented | Not_Applicable
(Spaced equivalents - "Not Implemented" / "Not Applicable" - are also accepted.)
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

# Canonical status weights. "Not_Applicable" is excluded from scoring (None).
STATUS_WEIGHTS = {
    "Implemented": 1.0,
    "Partial": 0.5,
    "Not_Implemented": 0.0,
    "Not_Applicable": None,
}

# Control_IDs that are treated as critical. These MUST match the Control_ID
# values used in the gap-assessment CSV / SoA (bare identifiers, no prefix).
CRITICAL_CONTROLS = {
    "A.8.1",      # PII breach notification
    "A.9.1",      # Geographical location of PII
    "A.10.6",     # Encryption of PII in transit
    "CLD.6.3.1",  # Shared roles and responsibilities
    "CLD.9.5.1",  # Tenant isolation
    "CLD.12.4.5", # Monitoring of cloud services
}


def normalize_status(raw: str) -> str:
    """Accept both underscore and spaced status spellings."""
    s = (raw or "").strip()
    return s.replace(" ", "_") if s else s


def load_rows(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score_rows(rows):
    domain_total = defaultdict(float)
    domain_count = defaultdict(int)
    by_status = defaultdict(int)
    critical_open = []

    for r in rows:
        status = normalize_status(r.get("Status", ""))
        domain = (r.get("Domain") or "Unknown").strip()
        ctrl = (r.get("Control_ID") or "").strip()
        weight = STATUS_WEIGHTS.get(status)
        by_status[status] += 1
        if ctrl in CRITICAL_CONTROLS and status != "Implemented":
            critical_open.append(r)
        if weight is None:
            continue
        domain_total[domain] += weight
        domain_count[domain] += 1

    domain_scores = {
        d: round(100.0 * domain_total[d] / domain_count[d], 1)
        for d in domain_total
    }
    overall = (
        round(100.0 * sum(domain_total.values()) / sum(domain_count.values()), 1)
        if domain_count else 0.0
    )
    return overall, domain_scores, by_status, critical_open


def render_report(overall, domain_scores, by_status, critical_open) -> str:
    today = dt.date.today().isoformat()
    lines = [
        "# Cloud ISMS Gap Assessment - Automated Report",
        "",
        f"**Generated:** {today}",
        "",
        f"## Overall Conformance: **{overall}%**",
        "",
        "## Status Distribution",
        "",
        "| Status | Count |",
        "|--------|------:|",
    ]
    for s, n in sorted(by_status.items()):
        lines.append(f"| {s or '(blank)'} | {n} |")

    lines += ["", "## Domain Scores", "", "| Domain | Score |", "|--------|------:|"]
    for d, sc in sorted(domain_scores.items(), key=lambda x: -x[1]):
        lines.append(f"| {d} | {sc}% |")

    lines += ["", f"## Critical Gaps ({len(critical_open)})", ""]
    if not critical_open:
        lines.append("_No critical gaps detected._")
    else:
        lines += ["| Control | Title | Status | Owner | Notes |",
                  "|---------|-------|--------|-------|-------|"]
        for r in critical_open:
            lines.append(
                f"| {r.get('Control_ID','')} | {r.get('Title','')} | "
                f"{r.get('Status','')} | {r.get('Owner','')} | {r.get('Notes','')} |"
            )
    lines += ["", "---", "_Report produced by cloud_gap_checker.py_"]
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="ISO 27017/27018 cloud gap checker")
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args(argv)

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 2

    rows = load_rows(args.input)
    overall, domain_scores, by_status, critical_open = score_rows(rows)
    args.output.write_text(render_report(overall, domain_scores, by_status, critical_open) + "\n",
                           encoding="utf-8")
    print(f"Wrote {args.output}: overall={overall}% critical_gaps={len(critical_open)}")
    return 1 if critical_open else 0


if __name__ == "__main__":
    sys.exit(main())
