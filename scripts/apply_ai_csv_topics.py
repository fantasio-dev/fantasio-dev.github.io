#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply AI CSV rows into existing Jekyll markdown topic pages (excluding exam).

Design goals:
- CSV content first (use 기술요소/매커니즘)
- Daily deck extraction compatible:
  - include headings with: "핵심 암기", "개념 정의", "구성요소" and tables after 구성요소
- Preserve existing body as a backup details section (only once)
"""

from __future__ import annotations

import csv
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional


RE_FRONT_MATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
RE_TITLE_LINE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
RE_CSV_MARKER = re.compile(r"<!--\s*CSV_APPLIED:.*?-->\s*\n", re.DOTALL)


CSV_PATH = "./downloads/기술사_기본필수노트_AI - AI.csv"
REPO_ROOT = "."


NO_TO_PATH: Dict[int, str] = {
    1: "docs/ai/01-machine-learning/supervised-learning.md",
    2: "docs/ai/01-machine-learning/unsupervised-learning.md",
    3: "docs/ai/01-machine-learning/reinforcement-learning.md",
    4: "docs/ai/01-machine-learning/deep-learning-concept.md",
    5: "docs/ai/01-machine-learning/perceptron.md",
    6: "docs/ai/08-ml-process/hyperparameters.md",
    7: "docs/ai/01-machine-learning/activation-function.md",
    8: "docs/ai/01-machine-learning/parameters.md",
    9: "docs/ai/02-deep-learning/vanishing-gradient.md",
    10: "docs/ai/02-deep-learning/overfitting-underfitting.md",
    11: "docs/ai/02-deep-learning/dropout.md",
    12: "docs/ai/02-deep-learning/cnn.md",
    13: "docs/ai/02-deep-learning/pooling-layer.md",
    14: "docs/ai/02-deep-learning/rnn.md",
    15: "docs/ai/02-deep-learning/lstm.md",
    16: "docs/ai/01-machine-learning/svm.md",
    17: "docs/ai/01-machine-learning/knn.md",
    18: "docs/ai/01-machine-learning/data-labeling.md",
    19: "docs/ai/01-machine-learning/dbscan.md",
    20: "docs/ai/01-machine-learning/k-means.md",
    21: "docs/ai/01-machine-learning/som.md",
    22: "docs/ai/01-machine-learning/pca.md",
    23: "docs/ai/02-deep-learning/gan.md",
    24: "docs/ai/02-deep-learning/dcgan.md",
    25: "docs/ai/01-machine-learning/q-learning.md",
    26: "docs/ai/06-ml-evaluation/confusion-matrix.md",
    27: "docs/ai/06-ml-evaluation/precision-recall.md",
    28: "docs/ai/02-deep-learning/catastrophic-forgetting.md",
    29: "docs/ai/04-nlp/mrc.md",
    30: "docs/ai/04-nlp/electra.md",
    31: "docs/ai/03-neural-network/federated-learning.md",
    32: "docs/ai/03-neural-network/gnn.md",
    33: "docs/ai/05-ai-ethics/adversarial-attack.md",
    34: "docs/ai/11-ai-training-data/training-data-cost.md",
    35: "docs/ai/07-learning-techniques/meta-learning.md",
    36: "docs/ai/07-learning-techniques/few-shot-learning.md",
    37: "docs/ai/04-nlp/transformer.md",
    38: "docs/ai/04-nlp/chatgpt.md",
    39: "docs/ai/05-ai-ethics/ai-ethics.md",
    40: "docs/ai/07-ai-service/deep-view.md",
    41: "docs/ai/04-nlp/word-embedding.md",
    42: "docs/ai/06-ml-evaluation/roc-curve.md",
    43: "docs/ai/05-ai-ethics/bias.md",
    44: "docs/ai/05-ai-ethics/ai-security.md",
    45: "docs/ai/07-ai-service/recommendation-system.md",
}


@dataclass
class CsvRow:
    no: int
    topic: str
    mid_topic: str
    mnemonic: str
    tech: str
    mech: str


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def extract_front_matter(md: str) -> Tuple[str, str]:
    m = RE_FRONT_MATTER.match(md)
    if not m:
        return "", md
    fm = m.group(0)
    body = md[len(fm) :]
    return fm, body


def extract_title_from_front_matter(fm: str) -> str:
    m = RE_TITLE_LINE.search(fm or "")
    if not m:
        return ""
    raw = m.group(1).strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1].strip()
    return raw


def extract_label_block(body: str) -> str:
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if "{: .label" in line:
            prev = lines[i - 1].strip() if i - 1 >= 0 else ""
            cur = lines[i].strip()
            if prev:
                return prev + "\n" + cur + "\n"
            return cur + "\n"
    return ""


def first_meaningful_sentence(text: str) -> str:
    if not text:
        return ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            continue
        if line.lower().startswith("ex)"):
            continue
        return re.sub(r"\s+", " ", line)
    return ""


def pick_keywords(mid_topic: str, text: str) -> List[str]:
    pool: List[str] = []
    base = normalize_ws(mid_topic)
    if base:
        pool.append(base.split("(")[0].strip())

    for m in re.finditer(r"\(([^)]+)\)", text or ""):
        t = normalize_ws(m.group(1))
        if t and len(t) <= 28:
            pool.append(t)

    for m in re.finditer(r"\b[A-Za-z][A-Za-z0-9\-]{1,18}\b", text or ""):
        pool.append(m.group(0))

    for m in re.finditer(r"[가-힣]{2,7}", text or ""):
        pool.append(m.group(0))

    out: List[str] = []
    seen = set()
    for t in pool:
        t = normalize_ws(t)
        if not t or t in seen:
            continue
        if t in {"기계학습", "인공지능", "알고리즘", "기법", "기술", "구성요소"}:
            continue
        seen.add(t)
        out.append(t)
        if len(out) >= 3:
            break
    while len(out) < 3:
        out.append("-")
    return out


def parse_sections(text: str) -> List[Tuple[str, List[str]]]:
    if not text:
        return []
    sections: List[Tuple[str, List[str]]] = []
    cur_name = "내용"
    cur_items: List[str] = []

    def flush():
        nonlocal cur_name, cur_items
        items = [i for i in (x.strip() for x in cur_items) if i]
        if items:
            sections.append((cur_name, items))
        cur_items = []

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        m = re.match(r"^\[([^\]]+)\]\s*(.*)$", line.strip())
        if m:
            flush()
            cur_name = normalize_ws(m.group(1))
            tail = normalize_ws(m.group(2))
            if tail:
                cur_items.append(tail)
            continue
        cur_items.append(line.strip())
    flush()
    return sections


def item_to_pair(item_line: str) -> Tuple[str, str]:
    s = re.sub(r"^[\\-\\+\\>•\\*]+\\s*", "", item_line.strip())
    s = re.sub(r"^[0-9]+[\\.\\)]\\s*", "", s)
    s = re.sub(r"^[①②③④⑤⑥⑦⑧⑨⑩]\\s*", "", s)

    for sep in [":", "=", "→", "->", ">", "–", "-"]:
        if sep in s:
            left, right = s.split(sep, 1)
            left = normalize_ws(left)
            right = normalize_ws(right)
            if left and right:
                return left, right
    return normalize_ws(s), ""


def make_table(rows: List[Tuple[str, str]], mnemonic_token: Optional[str] = None) -> str:
    if not rows:
        return "| 항목 | 설명 |\n|:--|:--|\n| - | - |\n"

    use_mn = bool(mnemonic_token) and len(mnemonic_token or "") == len(rows) and len(rows) <= 8
    if use_mn:
        header = "| 암기 | 항목 | 설명 |\n|:--|:--|:--|\n"
        body = ""
        for ch, (a, d) in zip(list(mnemonic_token), rows):
            body += f"| **{ch}** | **{a}** | {d or '-'} |\n"
        return header + body

    header = "| 항목 | 설명 |\n|:--|:--|\n"
    body = ""
    for a, d in rows:
        body += f"| **{a or '-'}** | {d or '-'} |\n"
    return header + body


def build_components_tables(row: CsvRow) -> str:
    sections = parse_sections(row.tech) + parse_sections(row.mech)
    prefer = [
        "구성요소",
        "Layer 구성",
        "기술요소",
        "알고리즘",
        "절차",
        "학습단계",
        "유형",
        "공격기법",
        "방법",
        "평가",
        "특징",
    ]

    chosen_items: List[str] = []
    chosen_name = ""
    for name in prefer:
        for sec_name, items in sections:
            if sec_name.lower() == name.lower() and len(items) >= 3:
                chosen_name = sec_name
                chosen_items = items
                break
        if chosen_items:
            break
    if not chosen_items:
        for sec_name, items in sections:
            if len(items) >= 3:
                chosen_name = sec_name
                chosen_items = items
                break

    pairs = [item_to_pair(x) for x in chosen_items[:8]]
    tokens = [t for t in re.split(r"\s+", normalize_ws(row.mnemonic)) if t]
    token = tokens[0] if tokens else None

    title = chosen_name or "핵심 항목"
    out = ""
    out += f"#### 그룹 1: {title}\n"
    out += "{: .highlight-purple }\n\n"
    out += make_table(pairs, token) + "\n"
    return out


def build_details_sections(row: CsvRow) -> str:
    sections = parse_sections(row.tech) + parse_sections(row.mech)
    if not sections:
        return "내용 없음\n"
    out = ""
    for name, items in sections:
        out += f"#### {name}\n\n"
        for it in items[:40]:
            out += f"- {normalize_ws(it)}\n"
        if len(items) > 40:
            out += "- (… 생략)\n"
        out += "\n"
    return out.strip() + "\n"


def generate_body(row: CsvRow, fm: str, old_body: str) -> str:
    title = extract_title_from_front_matter(fm) or normalize_ws(row.mid_topic) or f"AI 토픽 {row.no}"
    label_block = extract_label_block(old_body)

    base_text = (row.tech or "") + "\n" + (row.mech or "")
    one_line_def = first_meaningful_sentence(row.tech) or first_meaningful_sentence(row.mech) or "CSV 정의를 확인하세요."
    kws = pick_keywords(row.mid_topic, base_text)

    mnemonic_tokens = [t for t in re.split(r"\s+", normalize_ws(row.mnemonic)) if t]
    mnemonic_codes = " ".join([f"`{t}`" for t in mnemonic_tokens]) if mnemonic_tokens else "-"

    marker = f"<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO={row.no} | 중토픽={normalize_ws(row.mid_topic)} -->\n"

    body = ""
    body += marker
    body += f"# {title}\n"
    body += "{: .fs-8 }\n\n"
    if label_block:
        body += label_block + "\n"
    body += "---\n\n"
    body += "## 🎯 기술사 수준 설명\n\n"
    body += "### 📌 핵심 암기 (Quick Reference)\n\n"
    body += "{: .highlight }\n"
    body += f"> **{normalize_ws(row.mid_topic)}**: {one_line_def}\n"
    body += f"> - 암기: {mnemonic_codes}\n"
    body += f"> - 키워드: `{kws[0]}` `{kws[1]}` `{kws[2]}`\n\n"
    body += "---\n\n"

    body += '<div class="exam-concept-block" markdown="1">\n\n'
    body += "## 🧠 개념 영역\n\n"
    body += "### 🔑 핵심 키워드 3개\n\n"
    body += "| 키워드 | 설명 | 예시 |\n|:--|:--|:--|\n"
    body += f"| **{kws[0]}** | 핵심 개념/대상 | - |\n"
    body += f"| **{kws[1]}** | 주요 기법/구성요소 | - |\n"
    body += f"| **{kws[2]}** | 절차/평가/특징 | - |\n\n"

    body += "---\n\n"
    body += "### 📖 등장배경\n\n"
    body += "| 구분 | 내용 |\n|:--|:--|\n"
    body += f"| **문제/필요성** | {one_line_def} |\n"
    example = ""
    for ln in (row.tech or "").splitlines():
        t = ln.strip()
        if t.lower().startswith("ex)"):
            example = normalize_ws(t[3:])
            break
    body += f"| **활용/사례** | {example or '-'} |\n\n"

    body += "---\n\n"
    body += "### 📝 개념 정의\n\n"
    body += "| 구분 | 정의 |\n|:--|:--|\n"
    body += f"| **{normalize_ws(row.mid_topic)}** | {one_line_def} |\n\n"
    body += "</div>\n\n"

    body += "---\n\n"
    body += '<div class="exam-tech-block" markdown="1">\n\n'
    body += "## 🏗️ 기술 영역\n\n"
    body += "### 구성요소\n\n"
    body += build_components_tables(row)
    body += "\n</div>\n\n"

    body += "---\n\n"
    body += '<details markdown="1">\n'
    body += '<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>\n\n'
    body += build_details_sections(row)
    body += "\n</details>\n"

    if old_body.strip() and not RE_CSV_MARKER.search(old_body):
        body += "\n---\n\n"
        body += '<details markdown="1">\n'
        body += '<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>\n\n'
        body += old_body.strip() + "\n"
        body += "\n</details>\n"

    body += "\n"
    return body


def apply_to_file(row: CsvRow, rel_path: str) -> Tuple[bool, str]:
    abs_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.exists(abs_path):
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        title = normalize_ws(row.mid_topic) or f"AI 토픽 {row.no}"
        fm = (
            "---\n"
            "layout: default\n"
            f"title: {title}\n"
            "grand_parent: AI (인공지능)\n"
            "---\n"
        )
        old_body = ""
        new_body = generate_body(row, fm, old_body)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(fm + "\n" + new_body)
        return True, abs_path

    with open(abs_path, "r", encoding="utf-8") as f:
        md = f.read()
    fm, body = extract_front_matter(md)
    if not fm:
        fm = "---\nlayout: default\n---\n"
        body = md

    old_body = RE_CSV_MARKER.sub("", body)
    new_body = generate_body(row, fm, old_body)
    new_md = fm.rstrip("\n") + "\n\n" + new_body
    if new_md == md:
        return False, abs_path
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(new_md)
    return True, abs_path


def load_csv_rows() -> List[CsvRow]:
    rows: List[CsvRow] = []
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            no = int(r["NO"])
            rows.append(
                CsvRow(
                    no=no,
                    topic=normalize_ws(r.get("토픽", "")),
                    mid_topic=normalize_ws(r.get("중토픽", "")),
                    mnemonic=normalize_ws(r.get("암기법", "")),
                    tech=(r.get("기술요소", "") or "").rstrip(),
                    mech=(r.get("매커니즘", "") or "").rstrip(),
                )
            )
    return rows


def main() -> None:
    rows = load_csv_rows()
    changed: List[str] = []
    missing: List[int] = []

    for row in rows:
        rel = NO_TO_PATH.get(row.no)
        if not rel:
            missing.append(row.no)
            continue
        did, path = apply_to_file(row, rel)
        if did:
            changed.append(os.path.relpath(path, REPO_ROOT))

    print("CSV rows:", len(rows))
    print("changed:", len(changed))
    for p in changed:
        print(" -", p)
    if missing:
        print("missing mapping for:", missing)


if __name__ == "__main__":
    main()


