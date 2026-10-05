#!/usr/bin/env python3
"""라벨 대표성 실험 표본 — 층화 표본 + 미끼 (harness/user/archive/legacy/label-representativeness-protocol.md, 4.13절).

판정자(다른 세션의 에이전트)는 **라벨만** 보고 본문을 예측한 뒤, 본문을 보고 척도(질문
`agt:labelRepresentsBody`의 상황 문장 — 프로파일이 원본, 단일 정의처는 `kb_lib.judge_load_profile`)와
확신도(0~1)를 매긴다. 미끼는 라벨을 다른 청크의 본문에 바꿔 붙인 음성 표본이다 — 판정자가
라벨을 읽지 않고 본문에 순응하면 미끼를 못 잡는다(판별력, 8.14절). seed 고정으로 재현된다.

산출 (같은 seed 면 같은 결과):
  <out>/sheet.md — 실험자 기록물. 항목 번호·라벨(ko/en)만. 본문·출처·미끼 여부 없음
  <out>/key.json — 실험자만 본다. 번호 → 파일·본문·층·미끼 여부(미끼면 본문의 실제 출처)·`tools/judge.py --decoys`의 입력
  <judge-sheet>/labels.md·bodies.md (선택, `--judge-sheet <dir>`) — 세션 판정자에게 **주는 것**. 생성 머리·입력
    파일 절·경로·seed 를 싣지 않는다(저장소 위치·답의 단서를 주지 않는다) — 게이트 대상 생성 문서가 아니라
    실험 자극이므로 `<dir>`은 **워크스페이스 밖**이어야 하고 안이면 거부한다(2026-09-30 vnv 결함 보고 ④).
    labels.md는 번호·라벨(ko/en)·**대조 지문**(`kb_lib.label_fingerprint` — 응답에 그대로 적어 돌려준다),
    bodies.md는 번호·본문이다(라벨 공개 → 예측 → 이 파일로 본문 공개의 순서).

사용: label_sample.py --out <dir> [--judge-sheet <워크스페이스 밖 dir>] [--seed 20260911]
      [--sizes req=10,conc=20,rat=15,alt=15] [--decoys 10] [--profile kb/ontology/profile/development] <청크 .md …>
"""
import argparse
import json
import os
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)·판정자 프로파일 질의·지문의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402

LIVE = {"draft", "stable", "suspect"}
QUESTION = "labelRepresentsBody"  # 이 실험이 언제나 묻는 질문 — 프로파일의 지역명(judge-question-set-ontology.ttl)


# ── 층화 표본과 계층 ────────────────────

def body_of(path: str) -> str:
    """청크 본문 — frontmatter 제거 + 앞뒤 공백 제거. `tools/judge.py`가 이 함수를 그대로 가져다 쓴다(단일 정의처,
    2026-09-30 vnv 결함 보고 ①) — 지문 대조가 성립하려면 두 도구가 같은 문자열을 내야 한다."""
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


# ── 판정자 시트와 실행 ────────────────────

def require_outside_workspace(path: Path, root: Path) -> str:
    """`path`가 워크스페이스(`root`) 밖인가 — 아니면 거부 사유, 밖이면 빈 문자열.

    판정지(labels.md·bodies.md)는 게이트가 보지 않는 실험 자극이다 — 저장소 안에 두면 doccheck·gendoc 스캔 경로에
    들어올 위험과, 판정자 세션이 저장소를 열람해 답의 단서(원본 경로·이웃 파일)를 얻을 위험이 함께 생긴다."""
    resolved, root_resolved = path.resolve(), root.resolve()
    if resolved.is_relative_to(root_resolved):
        return (f"--judge-sheet {path} 이 워크스페이스({root}) 안이다 — 판정지는 저장소 밖에만 쓴다"
                "(게이트 없는 실험 자극, 2026-09-30 vnv 결함 보고 ④)")
    return ""


def write_judge_sheet(dirpath: Path, items: list[dict]) -> None:
    """세션 판정자에게 줄 것 — labels.md(라벨+지문)·bodies.md(본문). 생성 머리·경로·seed 없음."""
    dirpath.mkdir(parents=True, exist_ok=True)
    labels = ["라벨 대표성 판정 — 각 번호에 대해 (1) 라벨만 보고 본문의 주장을 한 문장으로 예측한다 "
              "(2) bodies.md 의 같은 번호를 열어 예측과 대조해 척도 하나와 확신도(0~1)를 정한다 "
              "(3) `judge` 질문 `labelRepresentsBody`·이 번호의 지문·값·확신도를 응답으로 남긴다.", ""]
    bodies = []
    for i, it in enumerate(items, 1):
        fp = kb_lib.label_fingerprint(it)
        labels.append(f"{i}. {it['title_ko']} | {it['title']} | 지문: {fp}")
        bodies += [f"## {i}", "", it["body"], ""]
    (dirpath / "labels.md").write_text("\n".join(labels) + "\n", encoding="utf-8")
    (dirpath / "bodies.md").write_text("\n".join(bodies), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--judge-sheet", default="", metavar="DIR",
                    help="세션 판정자에게 줄 labels.md·bodies.md 를 쓸 디렉토리 — 워크스페이스 밖이어야 한다")
    ap.add_argument("--seed", type=int, default=20260911)
    ap.add_argument("--sizes", default="req=10,conc=20,rat=15,alt=15")
    ap.add_argument("--decoys", type=int, default=10)
    ap.add_argument("--profile", default=kb_lib.JUDGE_PROFILE_DIR,
                    help="판정 질문·척도의 원본 디렉토리 — sheet 의 척도 문장을 여기서 그대로 읽는다(단일 정의처)")
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("chunks", nargs="+")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    apply_plane_level_state(*load_plane_level_state(a.residency))
    sizes = {k: int(v) for k, v in (kv.split("=") for kv in a.sizes.split(","))}

    if a.judge_sheet:
        reason = require_outside_workspace(Path(a.judge_sheet), root)
        if reason:
            print(f"FAIL {reason}", file=sys.stderr)
            return 2

    try:
        g = kb_lib.judge_load_profile(root, a.profile)
        qs = kb_lib.judge_questions(g)
    except (OSError, ValueError) as e:
        print(f"FAIL 프로파일을 읽을 수 없다 — {e}", file=sys.stderr)
        return 2
    q = qs.get(QUESTION)
    if not q or not q["scale"]:
        print(f"FAIL 질문 `agt:{QUESTION}` 이 프로파일에 없거나 척도 상황 문장이 없다 — {a.profile}", file=sys.stderr)
        return 2
    scale_text = " · ".join(q["scale"])

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
        f"한 문장으로 예측하고 (2) 본문을 받은 뒤 예측과 대조해 척도(`agt:{QUESTION}`: {scale_text}) 중 하나와 확신도 0~1 을 적는다",
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
    msg = f"표본 {len(real)} + 미끼 {len(decoys)} → {out}/sheet.md, key.json"
    if a.judge_sheet:
        write_judge_sheet(Path(a.judge_sheet), items)
        msg += f" · {a.judge_sheet}/labels.md, bodies.md"
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
