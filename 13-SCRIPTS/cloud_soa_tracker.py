"""cloud_soa_tracker.py — ISO/IEC 27017 + 27018 SoA tracker.

Document ID: CLOUD-SCRIPT-001 | Version: 1.0
"""
from __future__ import annotations
import csv, sys
from dataclasses import dataclass
from typing import List, Dict, Optional

STATUS_WEIGHT = {"Implemented": 1.0, "Partial": 0.5, "Not Implemented": 0.0, "Not Applicable": None}


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


def default_controls() -> List[Control]:
      cld = [
                ("CLD.6.3.1", "Shared roles and responsibilities"),
                ("CLD.8.1.5", "Removal of CSC assets"),
                ("CLD.9.5.1", "Segregation in virtual environments"),
                ("CLD.9.5.2", "VM hardening"),
                ("CLD.12.1.5", "Administrator's operational security"),
                ("CLD.12.4.5", "Monitoring of cloud services"),
                ("CLD.13.1.4", "Virtual / physical network alignment"),
      ]
    annex_a = [(f"A.{i}", f"ISO 27018 Annex A.{i}") for i in range(1, 26)]
    out: List[Control] = []
    for r, t in cld:
              out.append(Control(ref=r, section="ISO27017-CLD", title=t))
    for r, t in annex_a:
              out.append(Control(ref=r, section="ISO27018-AnnexA", title=t))
    return out


def section_progress(controls: List[Control]) -> Dict[str, Dict[str, float]]:
      summary: Dict[str, Dict[str, float]] = {}
    for c in controls:
              s = summary.setdefault(c.section, {"applicable": 0, "score_sum": 0.0})
        sc = c.score()
        if sc is None:
                      continue
                  s["applicable"] += 1
        s["score_sum"] += sc
    for sec, d in summary.items():
              d["progress_pct"] = (d["score_sum"] / d["applicable"]) * 100.0 if d["applicable"] else 0.0
    return summary


def overall(controls: List[Control]) -> float:
      scores = [c.score() for c in controls if c.score() is not None]
    return (sum(scores) / len(scores)) * 100.0 if scores else 0.0


def report(controls: List[Control]) -> None:
      print("ISO 27017 + 27018 SoA Progress Report")
    print("=" * 50)
    for sec, d in section_progress(controls).items():
              print(f"  {sec:24s}  applicable={int(d['applicable']):3d}  progress={d['progress_pct']:6.1f}%")
    print("-" * 50)
    print(f"  OVERALL                   progress={overall(controls):6.1f}%")


if __name__ == "__main__":
      controls = default_controls()
    for c in controls:
              if c.ref in {"CLD.6.3.1", "CLD.8.1.5", "A.1", "A.2", "A.16"}:
                            c.status = "Implemented"
elif c.ref in {"CLD.12.4.5", "A.7"}:
            c.status = "Partial"
    report(controls)
