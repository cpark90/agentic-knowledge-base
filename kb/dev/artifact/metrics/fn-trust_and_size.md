---
id: https://agentic-knowledge-base.dev/id/chunk/3da75bed-e0cb-4848-a438-30001f43fea2
type: artifact
level: executable
title_ko: 함수 trust_and_size (tools/metrics.py)
title: function trust_and_size in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/32847258-f1c4-4168-8add-3c90daa63de3, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5]
part_of: https://agentic-knowledge-base.dev/id/composite/dcc3c5a3-a8bd-4eb2-8d59-01f4ab1d6e3a
---
**함수** — `trust_and_size(g, chunks, live, plane, tokens)` 다. 사람 검토 수·생성자 분포·크기 히스토그램·assumes 링크 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def trust_and_size(g, chunks, live, plane, tokens):
    """사람 검토 수·생성자 분포·크기 히스토그램·assumes 링크 수를 돌려준다.

    크기의 단위는 토큰이고 상한은 plane 별 프로파일 파라미터이므로(p1-chunk-unit-is-tokens) 히스토그램의 칸은
    절대 수가 아니라 **그 청크의 상한에 대한 비율**이다 — plane 이 섞인 분포에서 "상한 근처에 몰렸는가"를 한
    칸으로 읽으려면 분모가 청크마다 달라야 한다. 마지막 칸(9/10 초과)이 억지 분할의 신호다 (4.13절).
    """
    human = sum(1 for c in chunks for v in g.objects(c, AGT.verifiedBy) if str(v).startswith("human:"))
    gen = Counter(str(next(g.objects(c, AGT.generatedBy), "")) for c in chunks)
    hist = Counter(size_bucket(tokens[c] / kb_lib.body_token_limit(plane[c])) for c in live)
    assumes = sum(1 for _ in g.subject_objects(AGT.assumes))
    return human, gen, hist, assumes
```
<!-- 인용 끝 -->
