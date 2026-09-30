---
id: https://agentic-knowledge-base.dev/id/chunk/f35029fa-aa72-4c8d-92e7-fcc9e58f314d
type: artifact
level: executable
title_ko: 함수 role_worksets (tools/metrics.py)
title: function role_worksets in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/626bc748-9945-4bc0-9063-fb2f30aa561c
---
**함수** — `role_worksets(g, live, plane, lines, pct)` 다. 역할·앵커별 작업 집합이 예산 안인 비율과 ODD 에서 파생되지 않은 스코프를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def role_worksets(g, live, plane, lines, pct):
    """역할·앵커별 작업 집합이 예산 안인 비율과 ODD 에서 파생되지 않은 스코프를 돌려준다."""
    # 2단계 — 역할별 작업 집합(라벨 목록) 크기와 스코프 파생
    odd_conds = set(g.objects(None, AGT.hasCondition))
    role_rows, scope_bad = [], []
    nb = defaultdict(set)
    for p_ in LINKS + [AGT.hasDirectPart]:
        for s_, o_ in g.subject_objects(p_):
            nb[s_].add(o_); nb[o_].add(s_)
    BUDGET = 200
    for role in g.subjects(RDF.type, AGT.Role):
        planes = set(g.objects(role, AGT.reads)) | set(g.objects(role, AGT.writes))
        in_scope = [c for c in live if next(g.objects(c, RDF.type)) in planes]
        ok = 0
        for anc in in_scope:  # 앵커마다: 헤더 2 + plane 제목 + 이웃 라벨 + (앵커+이웃) 본문
            nbs = [n for n in nb.get(anc, ()) if n in lines and n in live and next(g.objects(n, RDF.type)) in planes]
            total = 2 + len({plane[x] for x in [anc] + nbs}) + 1 + len(nbs) + lines[anc] + sum(lines[n] for n in nbs)
            ok += total <= BUDGET
        role_rows.append(f"`{str(role).split('/')[-1].replace('role-','')}` {pct(ok, len(in_scope))}")
        scope = ID[str(role).split('/')[-1].replace('role-', 'scope-')]
        inc = set(g.objects(scope, AGT.includesCondition))
        if (scope, AGT.subsetOf, None) not in g or not inc or not inc <= odd_conds:
            scope_bad.append(str(scope).split('/')[-1])
    return role_rows, scope_bad, BUDGET
```
<!-- 인용 끝 -->
