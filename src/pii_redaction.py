"""
PII Redaction (Candidate Detector)
----------------------------------
Flags likely PII using deterministic patterns and lightweight heuristics.
Outputs character spans and labels for *human review*.

- Patterns: emails, SSN, phone, dates, addresses (coarse), URLs.
- Extend with spaCy NER or Presidio if needed.

Author: [Your Name]
License: MIT
"""
import re
from typing import List, Dict

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SSN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
PHONE = re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})\b")
URL = re.compile(r"https?://\S+")
DATE = re.compile(r"\b(?:\d{1,2}[/-]){2}\d{2,4}\b")  # very coarse
ADDRESS = re.compile(r"\b\d+\s+[A-Za-z0-9'.#\-]+\s+(Street|St|Ave|Avenue|Rd|Road|Blvd|Lane|Ln|Way)\b", re.IGNORECASE)

def detect_pii(text: str) -> List[Dict]:
    findings = []
    for label, rx in [('EMAIL', EMAIL), ('SSN', SSN), ('PHONE', PHONE), ('URL', URL), ('DATE', DATE), ('ADDRESS', ADDRESS)]:
        for m in rx.finditer(text):
            findings.append({'start': m.start(), 'end': m.end(), 'label': label, 'value': m.group()})
    return findings

def redact_text(text: str, findings: List[Dict], mask: str = "█") -> str:
    spans = sorted([(f['start'], f['end']) for f in findings], key=lambda x: x[0])
    out = []
    i = 0
    for s, e in spans:
        out.append(text[i:s])
        out.append(mask * (e - s))
        i = e
    out.append(text[i:])
    return ''.join(out)
