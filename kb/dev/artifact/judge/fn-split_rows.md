---
id: https://agentic-knowledge-base.dev/id/chunk/97961156-fa24-45e3-8c66-a941abf73b4f
type: artifact
level: executable
title_ko: 함수 split_rows (tools/judge.py)
title: function split_rows in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8d622313-8c2c-4f87-9279-fce0b31cb0ff, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `split_rows(rows, q, name, th, source, stamp, enc)` 다. 판정 행을 로그 파일마다의 묶음으로 나눈다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def split_rows(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str, enc) -> list[list[dict]]:
    """판정 행을 로그 파일마다의 묶음으로 나눈다 — 한 묶음의 본문이 `memory` 상한 안이다.

    묶음을 실제로 렌더해 재는 까닭은 상한의 대상이 본문 전체이고 관측 문장·표 머리·요약도 그 안에 들기
    때문이다. 행 하나가 혼자서도 상한을 넘으면 그 행만으로 한 묶음을 만든다 — 자를 자리가 없으면 자르지 않고
    게이트가 그것을 잡는다 (조용히 버리지 않는다).
    """
    limit = kb_lib.body_token_limit("memory")
    parts: list[list[dict]] = []
    cur: list[dict] = []
    for r in rows:
        cand = cur + [r]
        over = kb_lib.token_count("\n".join(log_body(cand, q, name, th, source, stamp)), enc) > limit
        if over and cur:
            parts.append(cur)
            cur = [r]
        else:
            cur = cand
    if cur:
        parts.append(cur)
    return parts
```
<!-- 인용 끝 -->
