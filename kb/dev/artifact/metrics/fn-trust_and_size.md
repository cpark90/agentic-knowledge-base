---
id: https://agentic-knowledge-base.dev/id/chunk/3da75bed-e0cb-4848-a438-30001f43fea2
type: artifact
level: executable
title_ko: 함수 trust_and_size (tools/metrics.py)
title: function trust_and_size in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/dcc3c5a3-a8bd-4eb2-8d59-01f4ab1d6e3a
---
**함수** — `trust_and_size(g, chunks, live, lines)` 다. 사람 검토 수·생성자 분포·줄 수 히스토그램·assumes 링크 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def trust_and_size(g, chunks, live, lines):
    """사람 검토 수·생성자 분포·줄 수 히스토그램·assumes 링크 수를 돌려준다."""
    human = sum(1 for c in chunks for v in g.objects(c, AGT.verifiedBy) if str(v).startswith("human:"))
    gen = Counter(str(next(g.objects(c, AGT.generatedBy), "")) for c in chunks)
    hist = Counter(min((lines[c] - 1) // 10, 4) for c in live)
    assumes = sum(1 for _ in g.subject_objects(AGT.assumes))
    return human, gen, hist, assumes
```
<!-- 인용 끝 -->
