# 13 — GRC: NIST CSF 2.0 Gap Assessment + Risk Register

[![CI](https://github.com/BL3IP/nist-csf-gap-assessment/actions/workflows/ci.yml/badge.svg)](https://github.com/BL3IP/nist-csf-gap-assessment/actions/workflows/ci.yml)

A governance, risk & compliance (GRC) package for a fictional company (**Northwind Trading**):
a **NIST CSF 2.0** maturity gap assessment and a quantified risk register, with a tool that turns
the data into a board-ready report.

## Goal
Demonstrate GRC fundamentals — assess current vs. target security maturity against a recognized
framework, quantify risk, and produce an actionable remediation backlog + management report.

## What's inside
| Path | What it is |
|------|-----------|
| [`data/csf2-assessment.csv`](./data/csf2-assessment.csv) | CSF 2.0 maturity (current/target) across all 6 functions |
| [`data/risk-register.csv`](./data/risk-register.csv) | Risks with likelihood × impact scoring |
| [`tools/grc_report.py`](./tools/grc_report.py) | Generates the markdown report + scores |
| [`reports/gap-assessment-report.md`](./reports/gap-assessment-report.md) | The generated report (proof) |

NIST CSF 2.0 functions covered: **GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER**.
Maturity tiers 0–4 (Not Implemented → Partial → Risk Informed → Repeatable → Adaptive).

## Exact Setup Commands
```powershell
cd C:\Users\banlv\cyber\13-grc
& "C:\Users\banlv\AppData\Local\Programs\Python\Python312\python.exe" -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest tools\ -q
.\.venv\Scripts\python.exe tools\grc_report.py
```

## Proof It Works
**6/6 tests pass.** Generated report summary:
```
Overall maturity: 36.2%  |  priority gaps: 16  |  risks: 8 (Critical 3, High 4, Medium 1, Low 0)
```
- **Overall maturity 36.2%** of target tier 4 (mean current 1.45/4).
- **16 of 20 categories** have a ≥2-tier gap → prioritized remediation backlog; largest gap is
  **DE.CM Continuous Monitoring** (1→4).
- Risk register scored L×I into Critical/High/Medium bands; top risks: no admin MFA, unpatched
  VPN, no SIEM (all score 20 / Critical).

## Screenshots
See [`./screenshots/`](./screenshots). Add: the tool summary line and the rendered report
(`reports/gap-assessment-report.md`). For a PDF, print the markdown to PDF from your editor.

## My Custom Extensions
- **Data-driven, reproducible** GRC reporting (edit a CSV → regenerate the report) instead of a
  static spreadsheet.
- Ties each risk to a **CSF category**, linking the risk register to the maturity gaps.
- Deterministic scoring with a **6-case test suite** validating the maturity %, gap count, and
  risk bands.

## Resume Bullet Points
- Conducted a **NIST CSF 2.0** maturity gap assessment across all six functions, quantifying a
  36% baseline and a prioritized 16-item remediation backlog.
- Built a quantified **risk register** (likelihood × impact) mapped to CSF categories and
  surfaced the top Critical risks for leadership.
- Automated GRC reporting with a tested Python tool that turns assessment data into a
  management-ready report.

## Next-Level Ideas
- Export to a styled PDF and add a maturity radar chart.
- Map gaps to specific CSF 2.0 subcategory outcomes and recommended controls.
- Track remediation over time (quarterly re-assessment + trend).

---
status: ✅ complete & tested
```
✅ PROJECT COMPLETE & FULLY TESTED in its isolated folder. All works. Ready for portfolio.
```
