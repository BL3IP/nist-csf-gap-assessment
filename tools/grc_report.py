"""grc_report — NIST CSF 2.0 gap-assessment + risk-register reporting (zero dependencies).

Reads a CSF 2.0 maturity assessment and a risk register (CSV) and produces a markdown
governance report: overall maturity, per-function scores, priority gaps, and a risk summary.

Usage:
    python grc_report.py            # writes reports/gap-assessment-report.md
"""
from __future__ import annotations

import csv
import os
from typing import Dict, List

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

TIERS = {0: "Not Implemented", 1: "Partial", 2: "Risk Informed", 3: "Repeatable", 4: "Adaptive"}
FUNCTION_ORDER = ["GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"]


def load_assessment(path: str) -> List[Dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["Current"] = int(r["Current"])
            r["Target"] = int(r["Target"])
            r["Gap"] = r["Target"] - r["Current"]
            rows.append(r)
    return rows


def load_risks(path: str) -> List[Dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["Likelihood"] = int(r["Likelihood"])
            r["Impact"] = int(r["Impact"])
            r["Score"] = r["Likelihood"] * r["Impact"]
            r["Band"] = risk_band(r["Score"])
            rows.append(r)
    return rows


def maturity_pct(rows: List[Dict]) -> float:
    if not rows:
        return 0.0
    return sum(r["Current"] for r in rows) / (4 * len(rows)) * 100


def priority_gaps(rows: List[Dict], threshold: int = 2) -> List[Dict]:
    return sorted([r for r in rows if r["Gap"] >= threshold], key=lambda r: -r["Gap"])


def per_function(rows: List[Dict]) -> Dict[str, Dict[str, float]]:
    out = {}
    for fn in FUNCTION_ORDER:
        fr = [r for r in rows if r["Function"] == fn]
        if fr:
            out[fn] = {
                "current": sum(r["Current"] for r in fr) / len(fr),
                "target": sum(r["Target"] for r in fr) / len(fr),
            }
    return out


def risk_band(score: int) -> str:
    if score >= 20:
        return "Critical"
    if score >= 12:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"


def risk_summary(rows: List[Dict]) -> Dict[str, int]:
    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    for r in rows:
        counts[r["Band"]] += 1
    return counts


def build_report(assessment: List[Dict], risks: List[Dict]) -> str:
    pct = maturity_pct(assessment)
    gaps = priority_gaps(assessment)
    pf = per_function(assessment)
    counts = risk_summary(risks)

    lines = ["# NIST CSF 2.0 Gap Assessment & Risk Register — Northwind Trading (fictional)", ""]
    lines.append(f"**Overall maturity:** {pct:.1f}% of target tier 4 "
                 f"(mean current {sum(r['Current'] for r in assessment)/len(assessment):.2f}/4)")
    lines.append(f"**Priority gaps (>=2 tiers):** {len(gaps)} of {len(assessment)} categories")
    lines.append(f"**Risks:** {len(risks)} "
                 f"(Critical {counts['Critical']}, High {counts['High']}, "
                 f"Medium {counts['Medium']}, Low {counts['Low']})")
    lines.append("")

    lines.append("## Maturity by Function")
    lines.append("| Function | Current | Target |")
    lines.append("|----------|--------:|-------:|")
    for fn, v in pf.items():
        lines.append(f"| {fn} | {v['current']:.1f} | {v['target']:.1f} |")
    lines.append("")

    lines.append("## Priority Gaps (remediation backlog)")
    lines.append("| ID | Category | Current | Target | Gap |")
    lines.append("|----|----------|--------:|-------:|----:|")
    for r in gaps:
        lines.append(f"| {r['ID']} | {r['Category']} | {r['Current']} | {r['Target']} | {r['Gap']} |")
    lines.append("")

    lines.append("## Risk Register (by score)")
    lines.append("| ID | Risk | CSF | L | I | Score | Band | Treatment |")
    lines.append("|----|------|-----|--:|--:|------:|------|-----------|")
    for r in sorted(risks, key=lambda x: -x["Score"]):
        lines.append(f"| {r['ID']} | {r['Risk']} | {r['CSF']} | {r['Likelihood']} | "
                     f"{r['Impact']} | {r['Score']} | {r['Band']} | {r['Treatment']} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    assessment = load_assessment(os.path.join(DATA, "csf2-assessment.csv"))
    risks = load_risks(os.path.join(DATA, "risk-register.csv"))
    report = build_report(assessment, risks)
    out_dir = os.path.join(ROOT, "reports")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap-assessment-report.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(report)
    print(f"Wrote {out_path}")
    print(f"Overall maturity: {maturity_pct(assessment):.1f}%  |  "
          f"priority gaps: {len(priority_gaps(assessment))}  |  "
          f"risks: {len(risks)} ({risk_summary(risks)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
