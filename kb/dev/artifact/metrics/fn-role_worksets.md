---
id: https://agentic-knowledge-base.dev/id/chunk/f35029fa-aa72-4c8d-92e7-fcc9e58f314d
type: artifact
level: executable
title_ko: 함수 role_worksets (tools/metrics.py)
title: function role_worksets in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/626bc748-9945-4bc0-9063-fb2f30aa561c
---
**함수** — `role_worksets(g, live, plane, tokens, pct)` 다. 역할·앵커별 작업 집합이 예산 안인 비율과 ODD 에서 파생되지 않은 스코프를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def role_worksets(g, live, plane, tokens, pct):
    """역할·앵커별 작업 집합이 예산 안인 비율과 ODD 에서 파생되지 않은 스코프를 돌려준다.

    예산의 단위는 토큰이다 (p1-chunk-unit-is-tokens — 옛 200줄의 같은 계수기 환산이 5,418 이다). 본문의 크기는
    그래프의 `agt:tokenCount` 를 그대로 쓰고, 머리·제목·라벨 행은 행마다 1 로 센다 — 행 하나가 적어도 토큰
    하나이므로 합계는 **하한**이고 이 비율은 상한 쪽으로 낙관적이다. 정확한 판정은 뷰 자신(`workset`)이 한다.
    """
    # 2단계 — 역할별 작업 집합(라벨 목록) 크기와 스코프 파생
    odd_conds = set(g.objects(None, AGT.hasCondition))
    role_rows, scope_bad = [], []
    nb = defaultdict(set)
    for p_ in LINKS + [AGT.hasDirectPart]:
        for s_, o_ in g.subject_objects(p_):
            nb[s_].add(o_); nb[o_].add(s_)
    BUDGET = kb_lib.CONTEXT_TOKEN_BUDGET  # 컨텍스트 예산 — 단위는 토큰이다 (단일 정의처 kb_lib)
    for role in g.subjects(RDF.type, AGT.Role):
        planes = set(g.objects(role, AGT.reads)) | set(g.objects(role, AGT.writes))
        in_scope = [c for c in live if next(g.objects(c, RDF.type)) in planes]
        ok = 0
        for anc in in_scope:  # 앵커마다: 헤더 2 + plane 제목 + 이웃 라벨 + (앵커+이웃) 본문
            nbs = [n for n in nb.get(anc, ()) if n in tokens and n in live and next(g.objects(n, RDF.type)) in planes]
            total = 2 + len({plane[x] for x in [anc] + nbs}) + 1 + len(nbs) + tokens[anc] + sum(tokens[n] for n in nbs)
            ok += total <= BUDGET
        role_rows.append(f"`{str(role).split('/')[-1].replace('role-','')}` {pct(ok, len(in_scope))}")
        scope = ID[str(role).split('/')[-1].replace('role-', 'scope-')]
        inc = set(g.objects(scope, AGT.includesCondition))
        if (scope, AGT.subsetOf, None) not in g or not inc or not inc <= odd_conds:
            scope_bad.append(str(scope).split('/')[-1])
    return role_rows, scope_bad, BUDGET
```
<!-- 인용 끝 -->
