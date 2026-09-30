---
id: https://agentic-knowledge-base.dev/id/chunk/1b8a9132-b68b-46c7-a14e-55e7048494e2
type: artifact
level: executable
title_ko: 함수 spec_cycles (tools/chunk2kg.py)
title: function spec_cycles in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `spec_cycles(spec)` 다. specializationOf 사슬(조각 → 원본)의 순환들 — 순환마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def spec_cycles(spec: dict) -> list:
    """specializationOf 사슬(조각 → 원본)의 순환들 — 순환마다 구성원 튜플 하나(가장 작은 IRI 부터). validate check_specialization 과 같은 판정."""
    cycles, reported = [], set()
    for start in sorted(spec):
        seen, cur = [], start
        while cur in spec and cur not in seen:
            seen.append(cur)
            cur = spec[cur]
        if cur in seen:
            cyc = seen[seen.index(cur):]
            i = cyc.index(min(cyc))
            cyc = tuple(cyc[i:] + cyc[:i])
            if cyc not in reported:
                reported.add(cyc)
                cycles.append(cyc)
    return cycles
```
<!-- 인용 끝 -->
