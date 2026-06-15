#!/usr/bin/env python3
"""
Bibliography validation script for Morshneva et al. manuscript.

Validates DOIs via CrossRef API, PMIDs via PubMed E-utilities,
and NCT identifiers via ClinicalTrials.gov API.

Outputs:
  - Human-readable terminal report
  - GitHub Actions workflow annotations (::warning::, ::error::)
  - JSON machine-readable report (validation_report.json)

Exit code: 0 if all critical refs pass, 1 if any critical ref fails.

Usage:
    python3 scripts/validate_bibliography.py [--strict] [--json report.json]

Requirements: Python 3.8+ (stdlib only — urllib, json, re, argparse)
"""

import json
import re
import sys
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from typing import Optional


# ── API helpers ──────────────────────────────────────────────────────────────

def fetch_json(url: str, retries: int = 3, delay: float = 1.0) -> Optional[dict]:
    """Fetch JSON from URL with retry logic. Returns None on failure."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Morshneva2025-BibValidator/1.0 (mailto:amorshneva@incras.ru)",
                    "Accept": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, OSError) as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                return None
    return None


_HTML_TAG_RE = re.compile(r"<[^>]+>")

def normalize_title(t: str) -> str:
    """Normalize a title for fuzzy comparison — strips HTML, punctuation, extra ws."""
    t = _HTML_TAG_RE.sub("", t)           # strip <i>, </i>, <sup>, etc.
    t = t.lower().strip().rstrip(".")
    t = re.sub(r"[^a-z0-9\s]", "", t)     # strip punctuation
    t = re.sub(r"\s+", " ", t)            # collapse whitespace
    return t


def titles_match(reported: str, crossref: str, threshold: float = 0.7) -> tuple[bool, float]:
    """Check if two titles are similar enough. Returns (match, similarity)."""
    a = set(normalize_title(reported).split())
    b = set(normalize_title(crossref).split())
    if not a or not b:
        return False, 0.0
    intersection = a & b
    similarity = len(intersection) / max(len(a), len(b))
    return similarity >= threshold, similarity


# ── Validators ───────────────────────────────────────────────────────────────

def validate_doi(doi: str, reported_title: str) -> dict:
    """Validate a DOI via CrossRef API. Returns result dict."""
    result = {
        "doi": doi,
        "status": "unchecked",
        "crossref_title": None,
        "title_match": None,
        "title_similarity": None,
        "message": "",
    }

    data = fetch_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")
    if data is None or data.get("status") != "ok":
        result["status"] = "error"
        result["message"] = f"DOI {doi} — CrossRef API returned no valid response"
        return result

    msg = data["message"]
    crossref_title = None

    # CrossRef stores titles as a list
    title_list = msg.get("title", [])
    if title_list:
        crossref_title = title_list[0]

    if crossref_title is None:
        # Try container title (for journal-level DOIs)
        container = msg.get("container-title", [])
        if container:
            crossref_title = container[0]

    result["crossref_title"] = crossref_title

    if crossref_title:
        match, sim = titles_match(reported_title, crossref_title)
        result["title_match"] = match
        result["title_similarity"] = round(sim, 3)
        if match:
            result["status"] = "ok"
            result["message"] = f"DOI {doi} resolves — title matches (similarity={sim:.2f})"
        else:
            result["status"] = "warning"
            result["message"] = (
                f"DOI {doi} resolves but TITLE MISMATCH.\n"
                f"  Reported: {reported_title[:120]}\n"
                f"  CrossRef: {crossref_title[:120]}\n"
                f"  Similarity: {sim:.2f}"
            )
    else:
        result["status"] = "warning"
        result["message"] = f"DOI {doi} resolved but no title in CrossRef metadata"

    # Also capture journal, year, volume from CrossRef for completeness check
    result["crossref_journal"] = (msg.get("container-title") or [None])[0]
    result["crossref_year"] = msg.get("published-print", {}).get("date-parts", [[None]])[0][0]
    if result["crossref_year"] is None:
        result["crossref_year"] = msg.get("created", {}).get("date-parts", [[None]])[0][0]

    return result


def validate_pmid(pmid: str, reported_title: str) -> dict:
    """Validate a PMID via PubMed E-utilities. Returns result dict."""
    result = {
        "pmid": pmid,
        "status": "unchecked",
        "pubmed_title": None,
        "title_match": None,
        "title_similarity": None,
        "message": "",
    }

    # E-utilities: esummary
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        f"?db=pubmed&id={pmid}&retmode=json"
    )
    data = fetch_json(url)
    if data is None:
        result["status"] = "error"
        result["message"] = f"PMID {pmid} — PubMed E-utilities returned no response"
        return result

    records = data.get("result", {})
    record = records.get(pmid, {})
    if not record or "error" in record:
        result["status"] = "error"
        result["message"] = f"PMID {pmid} — not found in PubMed"
        return result

    pubmed_title = record.get("title", "")
    result["pubmed_title"] = pubmed_title

    if pubmed_title:
        match, sim = titles_match(reported_title, pubmed_title)
        result["title_match"] = match
        result["title_similarity"] = round(sim, 3)
        if match:
            result["status"] = "ok"
            result["message"] = f"PMID {pmid} resolves — title matches (similarity={sim:.2f})"
        else:
            result["status"] = "warning"
            result["message"] = (
                f"PMID {pmid} resolves but TITLE MISMATCH.\n"
                f"  Reported: {reported_title[:120]}\n"
                f"  PubMed:   {pubmed_title[:120]}\n"
                f"  Similarity: {sim:.2f}"
            )
    else:
        result["status"] = "warning"
        result["message"] = f"PMID {pmid} resolved but no title in PubMed record"

    result["pubmed_journal"] = record.get("source", "")
    result["pubmed_year"] = record.get("pubdate", "")[:4]
    return result


def validate_nct(nct_id: str) -> dict:
    """Validate a ClinicalTrials.gov NCT identifier. Returns result dict."""
    result = {
        "nct_id": nct_id,
        "status": "unchecked",
        "nct_title": None,
        "nct_status": None,
        "message": "",
    }

    # ClinicalTrials.gov API v2
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}"
    data = fetch_json(url)
    if data is None:
        result["status"] = "error"
        result["message"] = f"NCT {nct_id} — ClinicalTrials.gov API returned no response"
        return result

    prot = data.get("protocolSection", {})
    ident = prot.get("identificationModule", {})
    status_mod = prot.get("statusModule", {})

    result["nct_title"] = ident.get("briefTitle", ident.get("officialTitle", ""))
    result["nct_status"] = status_mod.get("overallStatus", "")
    result["status"] = "ok"
    result["message"] = (
        f"NCT {nct_id} — \"{result['nct_title'][:100]}...\" "
        f"(status: {result['nct_status']})"
    )
    return result


# ── Report generation ────────────────────────────────────────────────────────

def print_github_annotation(level: str, ref_id: str, message: str, file: str = "references.json") -> None:
    """Print a GitHub Actions workflow annotation (::warning/::error file=...::msg)."""
    # Escape newlines — GitHub annotations are single-line
    clean = message.replace("\n", " | ").replace("%", "%25").replace("\r", "")
    print(f"::{level} file={file},title=ref:{ref_id}::{clean}")


def load_references(path: str) -> list[dict]:
    """Load references from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Validate bibliography — DOIs, PMIDs, NCT identifiers"
    )
    parser.add_argument(
        "--references", default="references.json",
        help="Path to references.json (default: references.json)",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Treat warnings as errors (exit code 1 on any warning)",
    )
    parser.add_argument(
        "--json-report", default="validation_report.json",
        help="Path to write JSON report (default: validation_report.json)",
    )
    parser.add_argument(
        "--no-annotations", action="store_true",
        help="Suppress GitHub Actions annotations",
    )
    args = parser.parse_args()

    refs = load_references(args.references)
    print(f"📚 Loaded {len(refs)} references from {args.references}\n")

    results = []
    stats = {"ok": 0, "warning": 0, "error": 0, "skipped": 0}

    for ref in refs:
        ref_id = ref["id"]
        title = ref.get("title", "")
        doi = ref.get("doi")
        pmid = ref.get("pmid")
        nct = ref.get("nct_id")
        needs_verif = ref.get("needs_verification", False)

        header = f"── [{ref_id}] ──"
        print(header)

        if needs_verif and not doi and not pmid:
            result = {
                "ref_id": ref_id,
                "status": "warning",
                "message": f"[{ref_id}] INCOMPLETE — no DOI/PMID, needs manual verification.\n"
                           f"  Authors: {ref.get('authors', '?')}\n"
                           f"  Title: {title}\n"
                           f"  Note: {ref.get('note', '')}",
            }
            results.append(result)
            stats["warning"] += 1
            print(f"  ⚠️  INCOMPLETE — no identifier to validate")
            if not args.no_annotations:
                print_github_annotation("warning", ref_id, result["message"])
            print()
            continue

        if doi:
            print(f"  DOI: {doi}")
            r = validate_doi(doi, title)
            r["ref_id"] = ref_id
            results.append(r)
            stats[r["status"]] += 1

            emoji = {"ok": "✅", "warning": "⚠️", "error": "❌"}.get(r["status"], "❓")
            print(f"  {emoji} {r['message']}")
            if not args.no_annotations and r["status"] in ("warning", "error"):
                annotation_level = "error" if r["status"] == "error" else "warning"
                print_github_annotation(annotation_level, ref_id, r["message"])

        if pmid:
            print(f"  PMID: {pmid}")
            r = validate_pmid(pmid, title)
            r["ref_id"] = ref_id
            results.append(r)
            stats[r["status"]] += 1

            emoji = {"ok": "✅", "warning": "⚠️", "error": "❌"}.get(r["status"], "❓")
            print(f"  {emoji} {r['message']}")
            if not args.no_annotations and r["status"] in ("warning", "error"):
                annotation_level = "error" if r["status"] == "error" else "warning"
                print_github_annotation(annotation_level, ref_id, r["message"])

        if nct:
            print(f"  NCT: {nct}")
            r = validate_nct(nct)
            r["ref_id"] = ref_id
            results.append(r)
            stats[r["status"]] += 1

            emoji = {"ok": "✅", "error": "❌"}.get(r["status"], "❓")
            print(f"  {emoji} {r['message']}")
            if not args.no_annotations and r["status"] == "error":
                print_github_annotation("error", ref_id, r["message"])

        if not doi and not pmid and not nct:
            result = {
                "ref_id": ref_id,
                "status": "skipped",
                "message": f"[{ref_id}] No identifier (DOI/PMID/NCT) to validate.\n"
                           f"  Title: {title[:150]}",
            }
            results.append(result)
            stats["skipped"] += 1
            print(f"  ⬜ No DOI/PMID/NCT — skipped")
            if not args.no_annotations:
                print_github_annotation("warning", ref_id, result["message"])

        print()

    # ── Summary ───────────────────────────────────────────────────────────
    total = len(refs)
    print("═" * 60)
    print(f"SUMMARY: {total} references checked")
    print(f"  ✅ OK:       {stats['ok']}")
    print(f"  ⚠️  Warning:  {stats['warning']}")
    print(f"  ❌ Error:    {stats['error']}")
    print(f"  ⬜ Skipped:  {stats['skipped']}")
    print("═" * 60)

    # Write JSON report
    report = {
        "summary": {
            "total": total,
            "ok": stats["ok"],
            "warning": stats["warning"],
            "error": stats["error"],
            "skipped": stats["skipped"],
        },
        "results": results,
    }
    with open(args.json_report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n📄 JSON report written to {args.json_report}")

    # Exit code
    if stats["error"] > 0:
        print("\n❌ CRITICAL FAILURES DETECTED — references with broken identifiers")
        sys.exit(1)
    if args.strict and stats["warning"] > 0:
        print("\n⚠️  Warnings treated as errors (--strict mode)")
        sys.exit(1)

    print("\n✅ All critical references pass validation")
    sys.exit(0)


if __name__ == "__main__":
    main()
