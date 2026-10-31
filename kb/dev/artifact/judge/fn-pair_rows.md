---
id: https://agentic-knowledge-base.dev/id/chunk/8361deae-2526-4bb1-9fd9-bb8b6899d0f2
type: artifact
level: executable
title_ko: 함수 pair_rows (tools/judge.py)
title: function pair_rows in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1dcbf356-b12e-4bc2-b68a-0d4dc08ff69d, https://agentic-knowledge-base.dev/id/chunk/25dbde8d-3165-4a6e-bda8-313cc2ef674b, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb, https://agentic-knowledge-base.dev/id/chunk/9ba49f50-c949-45ae-816e-d24210ec8af6, https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/df43fa6f-d424-49d0-aec2-0aea8545572a]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `pair_rows(root, pairs, qs, resp_sets)` 다. 쌍 × 응답 집합마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_rows(root: Path, pairs: list[dict], qs: dict, resp_sets: list[dict]) -> tuple[list[dict], dict]:
    """쌍 × 응답 집합마다 판정 행 — (행들, 집계 {응답 없음, 낡음, 미끼별 (검출, 응답, 전체)}). 미끼는 행을 내지 않는다."""
    now = kb_lib.utc_stamp(datetime.now(timezone.utc))
    rows, tally = [], {"missing": 0, "stale": 0, "neg": [0, 0, 0], "pos": [0, 0, 0]}
    current: dict = {}
    for p in pairs:
        if p["question"] not in qs or qs[p["question"]]["form"] != "noul":
            raise JudgeError(f"쌍 {p.get('n')}: 질문 {p['question']!r} 이 프로파일의 noul 질문이 아니다")
        if p.get("decoy") in ("neg", "pos"):
            tally[p["decoy"]][2] += 1
            continue
        side = []
        for end in ("anchor", "target"):
            path = at(root, p[end]["path"])
            try:
                meta, _ = parse_chunk(str(path))
                side.append((path.read_bytes(), meta, sample_body_of(str(path))))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{p[end]['path']}: 단위 지식으로 읽을 수 없다 — {e}")
        current[p["fingerprint"]] = all(
            (m.get("title_ko", ""), m.get("title", ""), body) == (p[end]["title_ko"], p[end]["title"], p[end]["body"])
            for (_, m, body), end in zip(side, ("anchor", "target")))
        p["_record"] = kb_lib.pair_record_fingerprint(side[0][0], side[1][0])
        p["_level"] = side[0][1]["level"]
    for data in resp_sets:
        used: set = set()
        for p in pairs:
            ans = pair_answer(data, used, p["question"], p["fingerprint"])
            if p.get("decoy") in ("neg", "pos"):
                if ans:
                    t = tally[p["decoy"]]
                    t[1] += 1
                    t[0] += ans["value"] == ("no" if p["decoy"] == "neg" else "yes")
                continue
            if ans is None:
                tally["missing"] += 1
                continue
            if not current[p["fingerprint"]]:
                tally["stale"] += 1   # 판정지를 만든 뒤 라벨·본문이 바뀌었다 — 판정자가 본 것과 지금 파일이 다르다
                continue
            rows.append({"pair": True, "question": p["question"], "pair_fp": p["fingerprint"],
                         "path": f"{p['anchor']['path']} ↔ {p['target']['path']}",
                         "iri": kb_lib.pair_target(p["anchor"]["id"], p["target"]["id"], p["kind"]), "level": p["_level"],
                         "label": f"{p['anchor']['title_ko']} ↔ {p['target']['title_ko']}", "fingerprint": p["_record"],
                         "at": now, "route": route(), **ans})
    return rows, tally
```
<!-- 인용 끝 -->
