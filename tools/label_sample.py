#!/usr/bin/env python3
"""라벨 대표성 실험 표본 — 층화 표본 + 미끼 (docs/feedback/label-representativeness-protocol.md, 4.13절).

판정자(다른 세션의 에이전트)는 **라벨만** 보고 본문을 예측한 뒤, 본문을 보고 3점(적합/부분/부적합)과
확신도(0~1)를 매긴다. 미끼는 라벨을 다른 청크의 본문에 바꿔 붙인 음성 표본이다 — 판정자가
라벨을 읽지 않고 본문에 순응하면 미끼를 못 잡는다(판별력, 8.14절). seed 고정으로 재현된다.

산출 둘 (같은 seed 면 같은 결과):
  <out>/sheet.md — 판정자에게 주는 것. 항목 번호·라벨(ko/en)만. 본문·출처·미끼 여부 없음
  <out>/key.json — 실험자만 본다. 번호 → 파일·본문·층·미끼 여부(미끼면 본문의 실제 출처)

사용: label_sample.py --out <dir> [--seed 20260911] [--sizes req=10,conc=20,rat=15,alt=15] [--decoys 10] <청크 .md …>
"""
import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)의 단일 정의처
from chunk2kg import parse_chunk  # noqa: E402

LIVE = {"draft", "stable", "suspect"}


def body_of(path: str) -> str:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = lines[1:].index("---") + 1
    return "\n".join(lines[end + 1:]).strip()


def stratum(path: str, meta: dict) -> str:
    if meta["type"] == "requirement":
        return "req"
    if meta["type"] == "decision":
        name = Path(path).name
        if name == "conclusion.md":
            return "conc"
        if name == "rationale.md":
            return "rat"
        if name == "alternatives.md":
            return "alt"
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=20260911)
    ap.add_argument("--sizes", default="req=10,conc=20,rat=15,alt=15")
    ap.add_argument("--decoys", type=int, default=10)
    ap.add_argument("chunks", nargs="+")
    a = ap.parse_args()
    sizes = {k: int(v) for k, v in (kv.split("=") for kv in a.sizes.split(","))}

    pool = {k: [] for k in sizes}
    for p in sorted(a.chunks):
        if not p.endswith(".md"):
            continue
        meta, _ = parse_chunk(p)
        if meta.get("status") not in LIVE:
            continue
        s = stratum(p, meta)
        if s in pool:
            pool[s].append({"path": p, "id": meta["id"], "stratum": s,
                            "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
                            "body": body_of(p)})

    rng = random.Random(a.seed)
    real = []
    for s, n in sizes.items():
        if len(pool[s]) < n:
            print(f"FAIL 층 {s}: 표본 {n} > 모집단 {len(pool[s])}", file=sys.stderr)
            return 1
        real += rng.sample(pool[s], n)
    chosen = {r["id"] for r in real}

    # 미끼 — 실표본과 겹치지 않는 청크에서 라벨을, 같은 층의 또 다른 청크에서 본문을
    decoys = []
    rest = [it for s in sizes for it in pool[s] if it["id"] not in chosen]
    rng.shuffle(rest)
    for lab in rest:
        if len(decoys) >= a.decoys:
            break
        donors = [d for d in pool[lab["stratum"]] if d["id"] != lab["id"] and d["id"] not in chosen]
        if not donors:
            continue
        donor = rng.choice(donors)
        decoys.append({"path": lab["path"], "id": lab["id"], "stratum": lab["stratum"],
                       "title_ko": lab["title_ko"], "title": lab["title"],
                       "body": donor["body"], "decoy_body_from": donor["path"]})
        chosen.add(lab["id"]); chosen.add(donor["id"])

    items = real + decoys
    rng.shuffle(items)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    sheet = kb_lib.gendoc_header(
        "sheet", "라벨 대표성 판정지", "tools/label_sample.py",
        f"층화 표본 {len(real)}건과 미끼 {len(decoys)}건을 seed {a.seed} 로 섞어 — 각 항목에 대해 (1) 라벨만 보고 본문이 무엇을 말할지 "
        "한 문장으로 예측하고 (2) 본문을 받은 뒤 예측과 대조해 적합 / 부분 / 부적합 중 하나와 확신도 0~1 을 적는다",
        f"bazel run //tools:label_sample -- --seed {a.seed} --out {a.out}", [it["path"] for it in items],
        f"항목 {len(items)}개 · seed {a.seed}", kb_lib.gendoc_view_notice("각 청크의 라벨과 본문"), input_kind="청크 파일")
    rows = ["| # | 라벨 (ko) | 라벨 (en) |", "|---|---|---|"]
    key = []
    for i, it in enumerate(items, 1):
        rows.append(f"| {i} | {it['title_ko']} | {it['title']} |")
        key.append({"n": i, "path": it["path"], "id": it["id"], "stratum": it["stratum"],
                    "title_ko": it["title_ko"], "title": it["title"], "body": it["body"],
                    "decoy": "decoy_body_from" in it, "decoy_body_from": it.get("decoy_body_from")})
    rows.append("")
    (out / "sheet.md").write_text(kb_lib.gendoc_assemble(sheet, rows, [it["path"] for it in items], input_kind="청크 파일"),
                                  encoding="utf-8")
    (out / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"표본 {len(real)} + 미끼 {len(decoys)} → {out}/sheet.md, key.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
