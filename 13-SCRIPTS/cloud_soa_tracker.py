"""cloud_soa_tracker.py - ISO/IEC 27017 + 27018 Statement of Applicability tracker.

Document ID: CLOUD-SCRIPT-001 | Version: 2.0

Reads a Statement of Applicability CSV (or, if none is supplied, the bundled
canonical control list) and reports implementation progress per section and
overall.

Usage:
    python cloud_soa_tracker.py --input soa.csv --output soa_status.md
    python cloud_soa_tracker.py            # uses bundled canonical controls

CSV columns expected (header row required):
    Control_ID, Title, Applicable, Status, Responsibility, Justification, Evidence, Last_Reviewed

Status values: Implemented | Partial | Not Implemented | Not Applicable
Applicable values: Yes | No
"""
from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

# Status weights. "Not Applicable" is excluded from scoring (weight None).
STATUS_WEIGHT: Dict[str, Optional[float]] = {
    "Implemented": 1.0,
    "Partial": 0.5,
    "Not Implemented": 0.0,
    "Not Applicable": None,
}


@dataclass
class Control:
    ref: str
    section: str
    title: str
    applicable: bool = True
    status: str = "Not Implemented"

    def score(self) -> Optional[float]:
        if not self.applicable:
            return None
        return STATUS_WEIGHT.get(self.status)


# ---------------------------------------------------------------------------
# Canonical control list (single source of truth shared with the CSV schema).
# ISO 27017 cloud-only (CLD.x) controls + ISO 27018:2019 Annex A controls.
# ---------------------------------------------------------------------------
CLD_CONTROLS = [
    ("CLD.6.3.1", "Shared roles and responsibilities within a cloud environment"),
    ("CLD.8.1.5", "Removal of cloud service customer assets"),
    ("CLD.9.5.1", "Segregation in virtual computing environments"),
    ("CLD.9.5.2", "Virtual machine hardening"),
    ("CLD.12.1.5", "Administrator's operational security"),
    ("CLD.12.4.5", "Monitoring of cloud services"),
    ("CLD.13.1.4", "Alignment of security management for virtual and physical networks"),
]

# ISO/IEC 27018:2019 Annex A - 25 PII processor controls (real identifiers).
ANNEX_A_CONTROLS = [
    ("A.1.1", "Obligation to co-operate regarding PII principals' rights"),
    ("A.2.1", "Public cloud PII processor's purpose"),
    ("A.2.2", "Public cloud PII processor's commercial use"),
    ("A.3.1", "Collection limitation"),
    ("A.4.1", "Secure erasure of temporary files"),
    ("A.5.1", "PII disclosure notification"),
    ("A.5.2", "Recording of PII disclosures"),
    ("A.6.1", "Accuracy and quality"),
    ("A.7.1", "Disclosure of sub-contracted PII processing"),
    ("A.8.1", "Notification of a data breach involving PII"),
    ("A.9.1", "Geographical location of PII (accountability)"),
    ("A.9.2", "Intended destination of PII"),
    ("A.10.1", "Confidentiality or non-disclosure agreements"),
    ("A.10.2", "Restriction of the creation of hardcopy material"),
    ("A.10.3", "Control and logging of data restoration"),
    ("A.10.4", "Protecting data on storage media leaving the premises"),
    ("A.10.5", "Use of unencrypted portable storage media and devices"),
    ("A.10.6", "Encryption of PII transmitted over public networks"),
    ("A.10.7", "Secure disposal of hardcopy materials"),
    ("A.10.8", "Unique use of user IDs"),
    ("A.10.9", "Records of authorised users"),
    ("A.10.10", "User ID management"),
    ("A.10.11", "Contract measures"),
    ("A.10.12", "Sub-contracted PII processing"),
    ("A.10.13", "Access to data on pre-used data storage space"),
]
# Note: A.11.1 / A.11.2 (privacy compliance) are documented in the SoA and the
# 27018 reference; the 25 controls above are the Annex A PII-specific controls.


def default_controls() -> List[Control]:
    out: List[Control] = []
    for ref, title in CLD_CONTROLS:
        out.append(Control(ref=ref, section="ISO27017-CLD", title=title))
    for ref, title in ANNEX_A_CONTROLS:
        out.append(Control(ref=ref, section="ISO27018-AnnexA", title=title))
    return out


def _truthy(value: str) -> bool:
    return str(value).strip().lower() in {"yes", "y", "true", "1", "applicable"}


def load_controls(path: Optional[Path]) -> List[Control]:
    if path is None:
        return default_controls()
    if not path.exists():
        raise FileNotFoundError(f"Input not found: {path}")
    controls: List[Control] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ref = (row.get("Control_ID") or "").strip()
            if not ref:
                continue
            if ref.startswith("CLD"):
                section = "ISO27017-CLD"
            elif ref.startswith("A."):
                section = "ISO27018-AnnexA"
            else:
                section = (row.get("Responsibility") or "Other").strip() or "Other"
            controls.append(
                Control(
                    ref=ref,
                    section=section,
                    title=(row.get("Title") or "").strip(),
                    applicable=_truthy(row.get("Applicable", "Yes")),
                    status=(row.get("Status") or "Not Implemented").strip(),
                )
            )
    return controls


def section_progress(controls: List[Control]) -> Dict[str, Dict[str, float]]:
    summary: Dict[str, Dict[str, float]] = {}
    for c in controls:
        bucket = summary.setdefault(c.section, {"applicable": 0.0, "score_sum": 0.0})
        sc = c.score()
        if sc is None:
            continue
        bucket["applicable"] += 1
        bucket["score_sum"] += sc
    for bucket in summary.values():
        applicable = bucket["applicable"]
        bucket["progress_pct"] = (bucket["score_sum"] / applicable) * 100.0 if applicable else 0.0
    return summary


def overall(controls: List[Control]) -> float:
    scores = [c.score() for c in controls]
    scores = [s for s in scores if s is not None]
    return (sum(scores) / len(scores)) * 100.0 if scores else 0.0


def render(controls: List[Control]) -> str:
    lines = [
        "# ISO 27017 + 27018 SoA Progress Report",
        "",
        "| Section | Applicable | Progress |",
        "|---------|-----------:|---------:|",
    ]
    for section, data in sorted(section_progress(controls).items()):
        lines.append(
            f"| {section} | {int(data['applicable'])} | {data['progress_pct']:.1f}% |"
        )
    lines += [
        f"| **OVERALL** | {sum(1 for c in controls if c.score() is not None)} | {overall(controls):.1f}% |",
        "",
        "_Report produced by cloud_soa_tracker.py_",
    ]
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="ISO 27017/27018 SoA tracker")
    p.add_argument("--input", type=Path, default=None, help="SoA CSV (optional)")
    p.add_argument("--output", type=Path, default=None, help="Markdown report path (optional)")
    args = p.parse_args(argv)

    try:
        controls = load_controls(args.input)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 2

    report = render(controls)
    if args.output:
        args.output.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote {args.output}: overall={overall(controls):.1f}%")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
