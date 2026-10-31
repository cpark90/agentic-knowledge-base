#!/usr/bin/env python3
"""라벨 대표성 실험 표본 — 층화 표본 + 미끼 (harness/user/archive/legacy/label-representativeness-protocol.md, 4.13절).

판정자(다른 세션의 에이전트)는 **라벨만** 보고 본문을 예측한 뒤, 본문을 보고 척도(질문
`agt:labelRepresentsBody`의 상황 문장 — 프로파일이 원본, 단일 정의 위치는 `kb_lib.judge_load_profile`)와
확신도(0~1)를 매긴다. 미끼는 라벨을 다른 단위 지식의 본문에 바꿔 붙인 음성 표본이다 — 판정자가
라벨을 읽지 않고 본문에 순응하면 미끼를 못 잡는다(판별력, 8.14절). seed 고정으로 재현된다.

산출 (같은 seed 면 같은 결과):
  <out>/sheet.md — 실험자 기록물. 항목 번호·라벨(ko/en)만. 본문·출처·미끼 여부 없음
  <out>/key.json — 실험자만 본다. 번호 → 파일·본문·층·미끼 여부(미끼면 본문의 실제 출처)·`tools/judge.py --decoys`의 입력
  <judge-sheet>/labels.md·bodies.md (선택, `--judge-sheet <dir>`) — 세션 판정자에게 **주는 것**. 생성 머리·입력
    파일 절·경로·seed 를 싣지 않는다(저장소 위치·답의 단서를 주지 않는다) — 게이트 대상 생성 문서가 아니라
    실험 자극이므로 `<dir>`은 **워크스페이스 밖**이어야 하고 안이면 거부한다(2026-09-30 vnv 결함 보고 ④).
    labels.md는 번호·라벨(ko/en)·**대조 해시값**(`kb_lib.label_fingerprint` — 응답에 그대로 적어 돌려준다),
    bodies.md는 번호·본문이다(라벨 공개 → 예측 → 이 파일로 본문 공개의 순서).

쌍 판정지 (`--pair-sheet`, task 0262 · Q-0061 Q145-a): 링크 후보 뷰(`bazel-bin/kg/link-candidates.md`)의 후보 가운데 첫 근거가 동시
편집이고 판정자 값이 아직 없는 것만 골라, 음성 미끼(근거 없는 같은 KB 안 무작위 쌍 — 후보 표·확정 링크·본문 인용·동시 편집 관측 밖)와
양성 미끼(확정된 `overlapsWith` 링크 쌍)를 섞어 묶음을 낸다.
  <pair-sheet>/pairs-NN.md — 세션 판정자에게 **주는 것**. 쌍 번호·질문 문장·링크 종류와 정의·앵커와 대상의 라벨(ko/en)과 파일 단위 본문·
    대조 해시값(`kb_lib.pair_fingerprint`)만 싣고 경로·근거·미끼 여부는 숨긴다. 질문은 종류가 겹침이면 `overlapsHolds`, 그 밖이면
    `proposedLinkHolds` 다(kb_lib.pair_question). 워크스페이스 밖이어야 한다
  <out>/key.json — 정답 key(경로·IRI·미끼 여부). `tools/judge.py --pairs` 의 입력이고 판정자에게 주지 않는다. 워크스페이스 밖이어야 한다

사용: label_sample.py --out <dir> [--judge-sheet <워크스페이스 밖 dir>] [--seed 20260911]
      [--sizes req=10,conc=20,rat=15,alt=15] [--decoys 10] [--profile kb/ontology/profile/development] <단위 지식 .md …>
      label_sample.py --out <워크스페이스 밖 dir> --pair-sheet <워크스페이스 밖 dir> --pairs bazel-bin/kg/link-candidates.md
      [--decoys-neg 15] [--decoys-pos 9] [--batch 20] [--seed 20261025]
"""
import argparse
import json
import re
import os
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)·판정자 프로파일 질의·해시값의 단일 정의 위치
from chunk2kg import LINK_KEYS, apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402

LIVE = {"draft", "stable", "suspect"}
QUESTION = "labelRepresentsBody"  # 이 실험이 언제나 묻는 질문 — 프로파일의 지역명(judge-question-set-ontology.ttl)


# ── 층화 표본과 계층 ────────────────────

def body_of(path: str) -> str:
    """단위 지식 본문 — frontmatter 제거 + 앞뒤 공백 제거. `tools/judge.py`가 이 함수를 그대로 가져다 쓴다(단일 정의 위치,
    2026-09-30 vnv 결함 보고 ①) — 해시값 대조가 성립하려면 두 도구가 같은 문자열을 내야 한다."""
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
    """세션 판정자에게 줄 것 — labels.md(라벨+해시값)·bodies.md(본문). 생성 머리·경로·seed 없음."""
    dirpath.mkdir(parents=True, exist_ok=True)
    labels = ["라벨 대표성 판정 — 각 번호에 대해 (1) 라벨만 보고 본문의 주장을 한 문장으로 예측한다 "
              "(2) bodies.md 의 같은 번호를 열어 예측과 대조해 척도 하나와 확신도(0~1)를 정한다 "
              "(3) `judge` 질문 `labelRepresentsBody`·이 번호의 해시값·값·확신도를 응답으로 남긴다.", ""]
    bodies = []
    for i, it in enumerate(items, 1):
        fp = kb_lib.label_fingerprint(it)
        labels.append(f"{i}. {it['title_ko']} | {it['title']} | 해시값: {fp}")
        bodies += [f"## {i}", "", it["body"], ""]
    (dirpath / "labels.md").write_text("\n".join(labels) + "\n", encoding="utf-8")
    (dirpath / "bodies.md").write_text("\n".join(bodies), encoding="utf-8")


# ── 쌍 판정지 (--pair-sheet) ────────────────────

_ID_LINE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)


def view_candidates(view: Path) -> list[dict]:
    """링크 후보 뷰의 후보 표들(사람 확인 큐·판정 불일치·판정 없음) → 행 [{열 이름: 칸}]. 열은 kb_lib.LINK_CANDIDATE_COLUMNS 다."""
    header = "| " + " | ".join(kb_lib.LINK_CANDIDATE_COLUMNS) + " |"
    rows, inside = [], False
    for ln in view.read_text(encoding="utf-8").splitlines():
        s = ln.strip()
        if s == header:
            inside = True
            continue
        if inside and s.startswith("|---"):
            continue
        if inside and s.startswith("|"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", s)[1:-1]]
            if len(cells) == len(kb_lib.LINK_CANDIDATE_COLUMNS) and cells[0].isdigit():
                rows.append(dict(zip(kb_lib.LINK_CANDIDATE_COLUMNS, (c.strip("`") for c in cells))))
            continue
        inside = False
    return rows


def pair_judge_targets(rows: list[dict]) -> list[dict]:
    """판정 대상 — 첫 근거가 동시 편집이고 판정자 둘의 판정이 아직 없는 후보(뷰의 판정 없음 절: 단독 판정·낡은 판정 포함)."""
    return [r for r in rows if r["근거 종류"].split(" · ")[0] == "coEditHistory"
            and (r["판정자 값"] == kb_lib.EMPTY_NOT_APPLICABLE or kb_lib.JUDGED_NONE in r["판정자 값"])]


def index_items(root: Path) -> dict[str, str]:
    """단위 지식 IRI → 워크스페이스 상대 경로 (kb/ 아래 .md 의 frontmatter `id`)."""
    out = {}
    for f in sorted((root / "kb").rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        m = _ID_LINE.search(text.split("---", 2)[1])
        if m:
            out[m.group(1)] = f.relative_to(root).as_posix()
    return out


def kind_definitions(root: Path) -> dict[str, str]:
    """링크 종류(agt: 지역명) → 한글 skos:definition — 온톨로지 모듈이 원본이다."""
    from rdflib import Graph, Literal
    from rdflib.namespace import SKOS
    g = Graph()
    for f in sorted((root / "kb/ontology").rglob("*-ontology.ttl")):
        g.parse(f, format="turtle")
    out = {}
    for s, o in g.subject_objects(SKOS.definition):
        if str(s).startswith(str(kb_lib.AGT)) and isinstance(o, Literal) and o.language == "ko":
            out[str(s)[len(str(kb_lib.AGT)):]] = str(o)
    return out


_ITEMS: dict = {}


def item_of(root: Path, path: str) -> dict:
    """판정지에 보일 항목 — 경로·IRI·라벨(ko/en)·파일 단위 본문. 같은 경로는 한 번만 읽는다."""
    if path in _ITEMS:
        return dict(_ITEMS[path])
    meta, _ = parse_chunk(str(root / path))
    _ITEMS[path] = {"path": path, "id": meta["id"], "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
            "body": body_of(str(root / path))}
    return dict(_ITEMS[path])


def write_pair_sheet(sheet_dir: Path, out: Path, entries: list[dict], qs: dict, defs: dict, batch: int) -> list[Path]:
    """묶음 pairs-NN.md 와 key.json 을 쓴다 — 판정지에는 경로·근거·미끼 여부가 없다."""
    sheet_dir.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    used_q = sorted({e["question"] for e in entries})
    intro = ["쌍 판정 — 쌍마다 질문에 `yes` 또는 `no` 로 답하고 '예'의 확률(0~1)을 확신도로 적는다. 응답은 JSON "
             "`{\"judge\": <판정자 식별자>, \"responses\": [{\"question\": <질문 id>, \"fingerprint\": <쌍의 해시값>, "
             "\"value\": \"yes\"|\"no\", \"confidence\": <0~1>}]}` 로 돌려준다. 다른 쌍의 답을 참고하지 않는다.", ""]
    for name in used_q:
        intro.append(f"- `{name}` — {qs[name]['label']}: {qs[name]['text']}")
    written = []
    for k in range(0, len(entries), batch):
        lines = [f"# 쌍 판정지 {k // batch + 1:02d}", ""] + intro + [""]
        for e in entries[k:k + batch]:
            lines += [f"## 쌍 {e['n']}", "",
                      f"- 질문: {qs[e['question']]['label']} (`{e['question']}`)",
                      f"- 링크 종류: `{e['kind']}` — {defs.get(e['kind'], kb_lib.EMPTY_UNDECIDED)}",
                      f"- 해시값: {e['fingerprint']}", ""]
            for role, it in (("앵커", e["anchor"]), ("대상", e["target"])):
                lines += [f"### {role} — {it['title_ko']} | {it['title']}", "", it["body"], ""]
        path = sheet_dir / f"pairs-{k // batch + 1:02d}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
    (out / "key.json").write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    return written


def pair_sheet(a, root: Path) -> int:
    """쌍 판정지 모드 — 동시 편집 첫 근거 후보 + 음성·양성 미끼를 섞어 묶음과 key 를 낸다."""
    for flag, d in (("--pair-sheet", a.pair_sheet), ("--out", a.out)):
        reason = require_outside_workspace(Path(d), root)
        if reason:
            print(f"FAIL {reason.replace('--judge-sheet', flag)} — key 와 판정지는 저장소 밖에 둔다", file=sys.stderr)
            return 2
    if a.batch < 1:
        print("FAIL --batch 는 1 이상이다", file=sys.stderr)
        return 2
    try:
        qs = kb_lib.judge_questions(kb_lib.judge_load_profile(root, a.profile))
        rows = view_candidates(Path(a.pairs) if Path(a.pairs).is_absolute() else root / a.pairs)
    except (OSError, ValueError) as e:
        print(f"FAIL 입력을 읽을 수 없다 — {e}", file=sys.stderr)
        return 2
    missing = [q for q in sorted(set(kb_lib.JUDGE_PAIR_QUESTIONS.values()) | {kb_lib.JUDGE_PAIR_DEFAULT}) if q not in qs]
    if missing:
        print(f"FAIL 쌍 판정 질문 {missing} 이 프로파일에 없다 — {a.profile}", file=sys.stderr)
        return 2
    where = index_items(root)
    expand = lambda c: str(kb_lib.ID) + c[len("id:"):] if c.startswith("id:") else c  # noqa: E731
    defs = kind_definitions(root)
    rng = random.Random(a.seed)
    entries, seen = [], set()

    def add(anchor_path: str, target_path: str, kind: str, decoy):
        an, ta = item_of(root, anchor_path), item_of(root, target_path)
        q = kb_lib.pair_question(kind)
        entries.append({"question": q, "kind": kind, "fingerprint": kb_lib.pair_fingerprint(q, kind, an, ta), "decoy": decoy,
                        "anchor": an, "target": ta})
        seen.add(frozenset((an["id"], ta["id"])))

    real = pair_judge_targets(rows)
    for r in real:
        tp = where.get(expand(r["대상 IRI"]))
        if tp is None:
            print(f"FAIL 대상 {r['대상 IRI']} 의 파일이 kb/ 아래에 없다 — 뷰를 다시 만든다", file=sys.stderr)
            return 2
        add(r["앵커 파일"], tp, r["링크 종류"], None)
    endpoints = sorted({e["anchor"]["path"] for e in entries} | {e["target"]["path"] for e in entries})
    # 근거가 있는 쌍 — 후보 표의 모든 쌍 · 확정 링크 · 본문 인용 · 동시 편집 관측. 음성 미끼는 이 밖에서만 고른다
    ids = {p: item_of(root, p) for p in endpoints}
    evidenced = {frozenset((expand(r["대상 IRI"]), item_of(root, r["앵커 파일"])["id"])) for r in rows if where.get(expand(r["대상 IRI"]))}
    confirmed_overlaps = []
    for path in sorted(where.values()):
        meta, _ = parse_chunk(str(root / path))
        for key in LINK_KEYS:
            for t in (meta.get(key) or []) if isinstance(meta.get(key), list) else []:
                evidenced.add(frozenset((meta["id"], t)))
                if key == "overlapsWith" and t in where and meta.get("status") in LIVE:
                    confirmed_overlaps.append((path, where[t]))
    obs = sorted(str(p) for p in (root / kb_lib.DEV_MEMORY_DIR).glob(kb_lib.COEDIT_PREFIX + "*.md"))
    evidenced |= kb_lib.coedit_pairs(obs, set(where))[1]
    neg, tries = 0, 0
    while neg < a.decoys_neg and len(endpoints) > 1 and tries < 1000 * max(1, a.decoys_neg):
        tries += 1
        x, y = rng.sample(endpoints, 2)
        ix, iy = ids[x], ids[y]
        key = frozenset((ix["id"], iy["id"]))
        if (kb_lib.kb_of(x) != kb_lib.kb_of(y) or Path(x).parent == Path(y).parent or key in evidenced or key in seen
                or ix["id"] in iy["body"] or iy["id"] in ix["body"]):
            continue
        add(x, y, "overlapsWith", "neg")
        neg += 1
    rng.shuffle(confirmed_overlaps)
    for x, y in confirmed_overlaps[:a.decoys_pos]:
        if frozenset((item_of(root, x)["id"], item_of(root, y)["id"])) not in seen:
            add(x, y, "overlapsWith", "pos")
    rng.shuffle(entries)
    for i, e in enumerate(entries, 1):
        e["n"] = i
        e["batch"] = (i - 1) // a.batch + 1
    written = write_pair_sheet(Path(a.pair_sheet), Path(a.out), entries, qs, defs, a.batch)
    n_real = sum(1 for e in entries if not e["decoy"])
    print(f"쌍 {n_real} + 음성 미끼 {neg} + 양성 미끼 {sum(1 for e in entries if e['decoy'] == 'pos')} → "
          f"{len(written)}묶음 {a.pair_sheet}/pairs-NN.md · {a.out}/key.json · 질문 "
          + " · ".join(f"{q} {sum(1 for e in entries if e['question'] == q)}" for q in sorted({e['question'] for e in entries})))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--judge-sheet", default="", metavar="DIR",
                    help="세션 판정자에게 줄 labels.md·bodies.md 를 쓸 디렉토리 — 워크스페이스 밖이어야 한다")
    ap.add_argument("--seed", type=int, default=20260911)
    ap.add_argument("--sizes", default="req=10,conc=20,rat=15,alt=15")
    ap.add_argument("--decoys", type=int, default=10)
    ap.add_argument("--profile", default=kb_lib.JUDGE_PROFILE_DIR,
                    help="판정 질문·척도의 원본 디렉토리 — sheet 의 척도 문장을 여기서 그대로 읽는다(단일 정의 위치)")
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("--pair-sheet", default="", metavar="DIR",
                    help="쌍 판정지 pairs-NN.md 를 쓸 디렉토리(워크스페이스 밖) — 링크 후보 쌍 판정 모드")
    ap.add_argument("--pairs", default="bazel-bin/kg/link-candidates.md", metavar="VIEW",
                    help="링크 후보 뷰 bazel-bin/kg/link-candidates.md — 동시 편집 첫 근거 후보를 여기서 고른다")
    ap.add_argument("--decoys-neg", type=int, default=15, help="음성 미끼 수 — 근거 없는 같은 KB 안 무작위 쌍")
    ap.add_argument("--decoys-pos", type=int, default=9, help="양성 미끼 수 — 확정된 overlapsWith 링크 쌍(있는 만큼)")
    ap.add_argument("--batch", type=int, default=20, help="묶음 하나의 쌍 수")
    ap.add_argument("chunks", nargs="*")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    apply_plane_level_state(*load_plane_level_state(a.residency))
    if a.pair_sheet:
        return pair_sheet(a, root)
    if not a.chunks:
        ap.error("단위 지식 .md 가 없다 — 라벨 대표성 표본은 위치 인자로 받는다")
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

    # 미끼 — 실표본과 겹치지 않는 단위 지식에서 라벨을, 같은 층의 또 다른 단위 지식에서 본문을
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
        f"항목 {len(items)}개 · seed {a.seed}", kb_lib.gendoc_view_notice("각 단위 지식의 라벨과 본문"), input_kind="단위 지식 파일")
    rows = ["| # | 라벨 (ko) | 라벨 (en) |", "|---|---|---|"]
    key = []
    for i, it in enumerate(items, 1):
        rows.append(f"| {i} | {it['title_ko']} | {it['title']} |")
        key.append({"n": i, "path": it["path"], "id": it["id"], "stratum": it["stratum"],
                    "title_ko": it["title_ko"], "title": it["title"], "body": it["body"],
                    "decoy": "decoy_body_from" in it, "decoy_body_from": it.get("decoy_body_from")})
    rows.append("")
    (out / "sheet.md").write_text(kb_lib.gendoc_assemble(sheet, rows, [it["path"] for it in items], input_kind="단위 지식 파일"),
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
