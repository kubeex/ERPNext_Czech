#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-apply terminology.py against freshly extracted strings.

Usage (run after extract_strings.py against updated frappe/erpnext/hrms
source trees, e.g. after bumping the ERPNext/HRMS version):

    python3 extract_strings.py /path/to/frappe /path/to/erpnext /path/to/hrms \
        > /tmp/all_strings.txt
    python3 apply_terminology.py /tmp/all_strings.txt

This updates translations/cs.csv with any newly-matched exact phrases from
terminology.py, and appends genuinely new strings (not already in cs.csv or
pending_strings.csv) to pending_strings.csv for manual/AI translation.
Existing entries in either file are left untouched.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from terminology import PHRASES  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CS_CSV = os.path.join(HERE, "..", "..", "czech_localization", "translations", "cs.csv")
PENDING_CSV = os.path.join(HERE, "pending_strings.csv")


def load_csv_keys(path):
    keys = set()
    if not os.path.exists(path):
        return keys
    with open(path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if row:
                keys.add(row[0])
    return keys


def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <extracted_strings.txt>", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        strings = [l.strip() for l in f if l.strip()]

    existing_translated = load_csv_keys(CS_CSV)
    existing_pending = load_csv_keys(PENDING_CSV)

    new_translated = []
    new_pending = []
    for s in strings:
        if s in existing_translated or s in existing_pending:
            continue
        key = s.lower()
        if key in PHRASES:
            new_translated.append((s, PHRASES[key]))
        else:
            new_pending.append(s)

    if new_translated:
        with open(CS_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for en, cz in new_translated:
                w.writerow([en, cz, ""])

    if new_pending:
        with open(PENDING_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for en in new_pending:
                w.writerow([en, "", ""])

    print(f"newly translated (added to cs.csv): {len(new_translated)}")
    print(f"newly pending (added to pending_strings.csv): {len(new_pending)}")


if __name__ == "__main__":
    main()
