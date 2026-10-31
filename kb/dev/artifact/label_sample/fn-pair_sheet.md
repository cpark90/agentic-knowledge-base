---
id: https://agentic-knowledge-base.dev/id/chunk/a1fe4e07-ebf7-4d59-8408-970b8c42755d
type: artifact
level: executable
title_ko: 함수 pair_sheet (tools/label_sample.py)
title: function pair_sheet in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/00a89f1d-2167-43fb-9e95-4a70385078ae, https://agentic-knowledge-base.dev/id/chunk/12124054-d49f-44e2-be10-6fbdb102b578, https://agentic-knowledge-base.dev/id/chunk/13c498a5-52b6-4be6-a555-4099859edbbf, https://agentic-knowledge-base.dev/id/chunk/2cabfcc4-8242-47a2-9710-9ed682ab9f2b, https://agentic-knowledge-base.dev/id/chunk/46efd740-da05-4865-b292-1d80e216e5b3, https://agentic-knowledge-base.dev/id/chunk/674eca0b-5a5b-45f5-b382-4fa958bafcdc, https://agentic-knowledge-base.dev/id/chunk/68ed1ed6-9607-4a24-b3d7-5631a30d0616, https://agentic-knowledge-base.dev/id/chunk/8d6f25bd-f8f1-47b2-a82d-4f2b6d19cd91, https://agentic-knowledge-base.dev/id/chunk/a614648d-b67b-4026-ba49-0d8fa41d0a09, https://agentic-knowledge-base.dev/id/chunk/aa162d57-f8c9-4997-886c-33e23f8cab0a, https://agentic-knowledge-base.dev/id/chunk/ab2cbe51-0701-4753-859c-1019a3b9808f, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99, https://agentic-knowledge-base.dev/id/chunk/db984d6d-3345-4aed-bb9c-6fb4465d7923]
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `pair_sheet(a, root)` 다. 쌍 판정지 모드 — 동시 편집 첫 근거 후보 + 음성·양성 미끼를 섞어 묶음과 key 를 낸다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
