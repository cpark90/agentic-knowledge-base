---
id: https://agentic-knowledge-base.dev/id/chunk/8809d561-f915-420c-93b5-382d7dd4867c
type: artifact
level: executable
title_ko: 함수 near_miss (tools/vv_run.py)
title: function near_miss in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `near_miss(out, phrase)` 다. 기대 문구에 가장 가까운 출력 줄 — 없으면 마지막 줄.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def near_miss(out: str, phrase: str) -> str:
    """기대 문구에 가장 가까운 출력 줄 — 없으면 마지막 줄. 문구가 어긋났을 때 무엇이 대신 나왔는지가 수정 방향이다."""
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()][-NEAR_LINES:]
    if not lines:
        return "(출력 없음)"
    best = max(lines, key=lambda ln: difflib.SequenceMatcher(None, phrase, ln).ratio())
    return best if difflib.SequenceMatcher(None, phrase, best).ratio() >= NEAR_RATIO else lines[-1]
```
<!-- 인용 끝 -->
