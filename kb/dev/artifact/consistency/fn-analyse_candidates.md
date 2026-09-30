---
id: https://agentic-knowledge-base.dev/id/chunk/0a3de9a1-f0a2-4183-834b-3cfc160c41ba
type: artifact
level: executable
title_ko: 함수 analyse_candidates (tools/consistency.py)
title: function analyse_candidates in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/c5f10c9e-1f63-4c4a-82da-957ca0cb0e28
---
**함수** — `analyse_candidates(items, exact, near, linked)` 다. ⑩ 중복 확정 후보 — ①·③의 미묶음 쌍을 판정자 질문("이 두 블록은 같은 주장을 담는가?")의 입력으로 다시 낸다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_candidates(items, exact, near, linked):
    """⑩ 중복 확정 후보 — ①·③의 미묶음 쌍을 판정자 질문("이 두 블록은 같은 주장을 담는가?")의 입력으로 다시 낸다.

    ⑪ 자리 후보 — 슬롯 표지가 둘 이상인 청크에서, 다른 슬롯의 표지 낱말이 자리 밖으로 등장하는 문장.
    """
    total_pairs = len(exact) and sum(len(g) * (len(g) - 1) // 2 for g in exact)
    unlinked_exact = [g for g in exact if not all(linked(x, y) for x, y in combinations(g, 2))]
    unlinked_near = [(j, x, y) for j, x, y in near if not linked(x, y)]
    dup_candidates = ([(1.0, x, y) for g in unlinked_exact for x, y in combinations(g, 2)]
                      + [(j, x, y) for j, x, y in unlinked_near])
    dup_candidates.sort(key=lambda t: -t[0])
    placement = [(it, own, other, quote) for it in items for own, other, quote in placement_candidates(it)]
    return total_pairs, unlinked_exact, unlinked_near, dup_candidates, placement
```
<!-- 인용 끝 -->
