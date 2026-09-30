---
id: https://agentic-knowledge-base.dev/id/chunk/81b17e03-73ce-4c98-82c3-5847b168ced5
type: artifact
level: executable
title_ko: 함수 main (tools/label_sample.py)
title: function main in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/fff3d0e5-ad0f-4eb4-b8c9-e9ae7d1ce791
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
