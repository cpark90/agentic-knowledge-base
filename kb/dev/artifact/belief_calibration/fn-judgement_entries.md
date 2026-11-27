---
id: https://agentic-knowledge-base.dev/id/chunk/c560e205-9ac6-4bcc-8726-2749915945a6
type: artifact
level: executable
title_ko: 함수 judgement_entries (tools/belief_calibration.py)
title: function judgement_entries in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07748717-33f2-409f-8b8d-9c1a2fc37bc4, https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2]
part_of: https://agentic-knowledge-base.dev/id/composite/1edd84f8-3e8d-4183-996c-4666aefe4a4a
---
**함수** — `judgement_entries(paths, spec)` 다. 판정 로그들 → (링크 IRI → [(종류, 극성, 확신도 Fraction)], 링크 IRI → 판정 로그 이름 집합).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judgement_entries(paths: list[Path], spec: dict) -> tuple[dict, dict]:
    """판정 로그들 → (링크 IRI → [(종류, 극성, 확신도 Fraction)], 링크 IRI → 판정 로그 이름 집합). 쌍 행이 아니거나 값이 yes·no 가 아니거나
    확신도를 읽지 못한 행은 건너뛴다. 같은 (판정 로그, 판정자, 극성, 확신도)는 한 번 센다(run_evidence.judgement_lines 와 같다)."""
    seen: dict[str, set] = defaultdict(set)
    logs: dict[str, set] = defaultdict(set)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        m = _GENERATED_BY.search(text)
        if not m or m.group(1) != kb_lib.JUDGE_GENERATOR:
            continue
        for row in kb_lib.judge_log_rows(text):
            pair = kb_lib.parse_pair_target(row["대상"])
            pol = kb_lib.JUDGE_NOUL_POLARITY.get(row["값"])
            if pair is None or pol is None or not kb_lib.JUDGE_CONFIDENCE.match(row.get("확신도", "")):
                continue
            a, b, kind = pair
            link = f"{ID_BASE}link/{link_hash(work_id(a, spec), kind, work_id(b, spec))}"
            seen[link].add((path.name, row["판정자 식별자"], pol, Fraction(row["확신도"])))
            logs[link].add(path.name)
    return {k: [("agt:judgement", pol, conf) for _, _, pol, conf in sorted(v)] for k, v in seen.items()}, logs
```
<!-- 인용 끝 -->
