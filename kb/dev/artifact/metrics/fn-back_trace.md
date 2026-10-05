---
id: https://agentic-knowledge-base.dev/id/chunk/ad6647eb-8132-4478-a102-4fe23cf05e98
type: artifact
level: executable
title_ko: 함수 back_trace (tools/metrics.py)
title: function back_trace in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e8aad650-c14d-4d48-a2fb-788808b81c9c
---
**함수** — `back_trace(g, live, plane, reqs, declarer)` 다. 복합체 관계와 요구로 거슬러 오르는 비요구 청크의 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def back_trace(g, live, plane, reqs, declarer):
    """복합체 관계와 요구로 거슬러 오르는 비요구 청크의 수를 돌려준다.

    복합체는 경유 노드다 — 부분에서 복합체로, 복합체에서 그 부분들·선언 청크·상위 복합체로 간다(연결 성분과 같은 규칙).
    선언 청크와 복합체는 한 노드다(`declarer`, 유저 결정 Q49-a): 함수 청크는 절 복합체 → 파일 복합체 → 파일 청크의
    `refines` 로 요구에 닿는다.
    """
    # CQ20: 요구가 아닌 살아 있는 청크 중 refines 연쇄로 요구에 닿는 비율 (복합체 부분은 복합체를 거쳐 선언 청크를 따라간다)
    up = defaultdict(set)
    # 귀속으로 거슬러 오르는 술어의 정의처는 kb_lib.ASCRIPTION_PREDICATES 다 — `refines`·`serves` 와 `prov:specializationOf`.
    # 분할 조각은 링크를 승계 청크에 두므로(p10-split-keeps-work-identity) 원 청크를 거쳐 요구에 닿는다
    for pred in kb_lib.ASCRIPTION_PREDICATES:
        for s, o in g.subject_objects(pred): up[s].add(o)
    comp_of = {}
    for comp, part in g.subject_objects(AGT.hasDirectPart): comp_of[part] = comp
    siblings = defaultdict(set)
    for part, comp in comp_of.items(): siblings[comp].add(part)
    declared = {d_: c_ for c_, d_ in declarer.items()}
    def reaches_req(c):
        seen, stack = set(), [c]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in reqs: return True
            stack.extend(up.get(x, ()))
            if x in comp_of: stack.append(comp_of[x])  # 부분 → 복합체 (상위 복합체도 같은 길로 오른다)
            if x in siblings: stack.extend(siblings[x])  # 복합체 → 부분들
            if x in declarer: stack.append(declarer[x])  # 복합체 → 선언 청크
            if x in declared: stack.append(declared[x])  # 선언 청크 → 복합체
        return False
    # 저작된 지식만 센다 — 관측(memory plane)은 실행의 부산물, 판정 주석(annotation plane)은 산출물에 대한 리뷰라
    # 둘 다 고립·귀속 지표의 대상이 아니다 (유저 승인 2026-09-23 · 2026-09-29, handoff/connected-components-
    # observations-2026-09-19 · handoff/verdict-in-metrics-2026-09-27). 제외 집합의 정의처는 kb_lib 상수 하나다.
    # 같은 정의를 연결 성분도 쓴다
    authored = [c for c in live if plane[c] not in kb_lib.LINKAGE_EXCLUDED_PLANES]
    nonreq = [c for c in authored if plane[c] != "requirement"]
    ascribed = sum(1 for c in nonreq if reaches_req(c))
    return comp_of, siblings, authored, nonreq, ascribed
```
<!-- 인용 끝 -->
