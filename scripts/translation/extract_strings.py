#!/usr/bin/env python3
"""Extract translatable strings from Frappe/ERPNext/HRMS source trees.

Scans:
  - *.py for _("...") / _('...')
  - *.js, *.vue, *.html for __("...") / __('...')
  - *.json (doctype/report/workspace/print_format defs) for "label" values

Output: one string per line, deduplicated, sorted, written to stdout-ish file.
"""
import json
import os
import re
import sys

ROOTS = sys.argv[1:]

PY_RE = re.compile(r"""_\(\s*(?:f)?"((?:[^"\\]|\\.)*)"|_\(\s*(?:f)?'((?:[^'\\]|\\.)*)'""")
JS_RE = re.compile(r"""__\(\s*"((?:[^"\\]|\\.)*)"|__\(\s*'((?:[^'\\]|\\.)*)'""")

SKIP_DIRS = {".git", "node_modules", "__pycache__", "test", "tests", "locale", "translations", "public", "dist", "build"}

LABEL_KEYS = {"label", "report_name", "print_heading", "module_name"}

results = set()


def add(s: str):
    s = s.strip()
    if not s:
        return
    if len(s) < 2:
        return
    # skip pure format/placeholder-only or code-ish tokens
    if re.fullmatch(r"[\W_0-9]+", s):
        return
    results.add(s)


def scan_py_js(path: str, regex: re.Pattern):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except OSError:
        return
    for m in regex.finditer(content):
        s = m.group(1) if m.group(1) is not None else m.group(2)
        if s is not None:
            add(s.replace('\\"', '"').replace("\\'", "'"))


def walk_json_labels(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in LABEL_KEYS and isinstance(v, str):
                add(v)
            else:
                walk_json_labels(v)
    elif isinstance(obj, list):
        for item in obj:
            walk_json_labels(item)


def scan_json(path: str):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return
    walk_json_labels(data)


for root in ROOTS:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            if fn.endswith(".py"):
                scan_py_js(full, PY_RE)
            elif fn.endswith((".js", ".vue", ".html")):
                scan_py_js(full, JS_RE)
            elif fn.endswith(".json"):
                scan_json(full)

for s in sorted(results, key=lambda x: x.lower()):
    print(s)
