---
id: https://agentic-knowledge-base.dev/id/chunk/ba8f30b1-0233-40d8-be6d-4b9fdc60db2e
type: artifact
level: executable
title_ko: 함수 age_days (tools/open_questions.py)
title: function age_days in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `age_days(g, node, now)` 다. 항목의 나이(일) — `prov:generatedAtTime` 부터 now 까지의 온전한 일수.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def age_days(g: Graph, node, now: datetime):
    """항목의 나이(일) — `prov:generatedAtTime` 부터 now 까지의 온전한 일수. 시각이 없거나 읽을 수 없으면 None."""
    raw = str(next(g.objects(node, PROV.generatedAtTime), ""))
    try:
        at = datetime.fromisoformat(raw)
    except ValueError:
        return None
    at = at if at.tzinfo else at.replace(tzinfo=timezone.utc)
    return max((now - at).days, 0)
```
<!-- 인용 끝 -->
