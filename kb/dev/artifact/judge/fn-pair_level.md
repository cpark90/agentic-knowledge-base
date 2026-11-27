---
id: https://agentic-knowledge-base.dev/id/chunk/5a45b037-fe24-4b10-8cc4-48a81ebb8314
type: artifact
level: executable
title_ko: 함수 pair_level (tools/judge.py)
title: function pair_level in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7942fad8-bbd8-417d-840d-f33c6f00af3b]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `pair_level(into, where, p, sheet_level)` 다. 결과 주석의 수준 (task 0362, Q185) — 기록 저장소 `into` 에서 살아 있고 수준을 가진 끝점의 수준을 물려받는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_level(into: Path, where: dict[str, str], p: dict, sheet_level: str) -> str:
    """결과 주석의 수준 (task 0362, Q185) — 기록 저장소 `into` 에서 살아 있고 수준을 가진 끝점의 수준을 물려받는다.

    앵커가 그러면 앵커의 수준, 앵커가 묘비이거나 살아 있지 않으면 대상의 수준이다. 두 끝 모두 아니면 판정지 항목(앵커)의 수준
    `sheet_level` 을 쓴다. 수준은 `into` 의 파일에서 읽는다 — 판정지를 옛 트리에서 만들었으면 그 트리의 수준은 지금 저장소의 것과 다를 수 있다.
    """
    for end in ("anchor", "target"):
        level = live_level(into, where, p[end]["id"])
        if level:
            return level
    return sheet_level
```
<!-- 인용 끝 -->
