---
id: https://agentic-knowledge-base.dev/id/chunk/9126a0ff-4c8a-4088-969f-2b596ee08bdd
type: artifact
level: executable
title_ko: 함수 check_catalog (tools/validate.py)
title: function check_catalog in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7624f877-e0d3-45fd-b51d-91d72c7cf025
---
**함수** — `check_catalog(merged, odd, files)` 다. 카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 노트 9.2·9.6절) — 규약이던 것을 게이트로 (2026-09-13).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_catalog(merged: Graph, odd: Graph | None, files: dict[str, Graph]) -> list[str]:
    """카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 노트 9.2·9.6절) — 규약이던 것을 게이트로 (2026-09-13).

    데이터 그래프에 agt:Harness 가 없으면 대상이 아니다. 하네스마다:
      (a) hasRole 하는 역할마다 대응 스코프가 실재하고 하네스가 grants 한다. 대응은 슬러그다 — id:role-<x> ↔ id:scope-<x>
          (kb_lib.ROLE_ID_PREFIX·SCOPE_ID_PREFIX, rules §개체 IRI 접두사). 카탈로그에 역할→스코프 술어는 없다.
      (b) 역할마다 agt:reads 가 하나 이상이다 — 읽지 못하는 역할은 작업 집합을 받을 수 없다.
      (c) agt:writes 의 plane 은 같은 KB(agt:writesIn — 없으면 kb/dev) 안에서 역할 사이에 겹치지 않는다 — 설계·구현·운영 분리 (9.2절).
          V&V KB 는 코어의 두 번째 인스턴스라 plane 이름이 같으므로(p8-vv-plane-instances) 겹침은 KB 별로 본다 (2026-09-19). writesIn 값은 kb_lib.KB_ROOTS 안이어야 한다.
      (d) agt:maxConcurrent 합 ≤ ODD 동적 요소 id:cond-concurrent-agents 의 상한. 상한은 --odd 그래프의 agt:conditionValue 에서
          kb_lib.odd_upper_bound 로 뽑는다. ODD 가 없거나 조건·상한을 못 뽑으면 ConfigFailure(EXIT_CONFIG) — 판정 불가지 통과가 아니다.
    첫 실행(2026-09-13): 역할 4 · 스코프 4 · write plane 겹침 0 · 합 4 ≤ 5, FAIL 0.
    """
    AGT_, ID = kb_lib.AGT, kb_lib.ID
    gate = kb_lib.CATALOG_GATE
    harnesses = sorted(s for s in merged.subjects(RDF.type, AGT_.Harness) if isinstance(s, URIRef))
    if not harnesses:
        return []
    errors: list[str] = []
    for h in harnesses:
        where = _where(files, h)
        roles = sorted(r for r in merged.objects(h, AGT_.hasRole) if isinstance(r, URIRef))
        grants = set(merged.objects(h, AGT_.grants))
        writers: dict[tuple[str, URIRef], list[URIRef]] = {}  # (KB, plane) → 역할들
        total = 0
        for r in roles:
            rq = _qname(merged, r)
            local = str(r)[len(str(ID)):] if str(r).startswith(str(ID)) else ""
            if not local.startswith(kb_lib.ROLE_ID_PREFIX):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 IRI 가 id:{kb_lib.ROLE_ID_PREFIX}<slug> 가 아니다 — 대응 스코프를 찾을 수 없다 (rules §개체 IRI 접두사)")
            else:
                scope = ID[kb_lib.SCOPE_ID_PREFIX + local[len(kb_lib.ROLE_ID_PREFIX):]]
                if (scope, RDF.type, AGT_.Scope) not in merged:
                    errors.append(f"[{gate}] {where}: 역할 {rq} 에 대응 스코프 {_qname(merged, scope)} 가 없다 — 역할마다 스코프를 선언한다 (STYLEGUIDE §5 카탈로그 완전성)")
                elif scope not in grants:
                    errors.append(f"[{gate}] {where}: 하네스 {_qname(merged, h)} 가 역할 {rq} 의 스코프 {_qname(merged, scope)} 를 agt:grants 하지 않는다 (STYLEGUIDE §5)")
            if not any(True for _ in merged.objects(r, AGT_.reads)):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 read plane 이 0 이다 — agt:reads 를 하나 이상 선언한다 (AGENTS 표 read 열)")
            kbs = _writes_in(merged, r)
            for kb in sorted(kbs - set(kb_lib.KB_ROOTS)):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 agt:writesIn {kb!r} 가 KB 경로 접두({' · '.join(kb_lib.KB_ROOTS)})가 아니다 (pe-storage-layout)")
            for plane in merged.objects(r, AGT_.writes):
                for kb in kbs:
                    writers.setdefault((kb, plane), []).append(r)
            counts = list(merged.objects(r, AGT_.maxConcurrent))
            if not counts:
                errors.append(f"[{gate}] {where}: 역할 {rq} 에 agt:maxConcurrent 가 없다 — 합을 판정할 수 없다 (9.6절)")
                continue
            try:
                total += int(counts[0])
            except (TypeError, ValueError):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 agt:maxConcurrent {counts[0]!r} 이 정수가 아니다")
        for (kb, plane), rs in sorted(writers.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
            if len(rs) > 1:
                names = ", ".join(_qname(merged, r) for r in sorted(rs))
                errors.append(f"[{gate}] {where}: KB {kb} 의 write plane {_qname(merged, plane)} 을 역할 {names} 이 공유한다 — 설계·구현·운영은 같은 KB 안에서 같은 write plane 을 쓰지 않는다 (AGENTS 역할 절, 9.2절; agt:writesIn)")
        cond = kb_lib.CONCURRENT_AGENTS_CONDITION
        if odd is None:
            raise ConfigFailure(f"[{gate}] {where}: maxConcurrent 합의 상한은 ODD 조건 {_qname(merged, cond)} 인데 --odd 그래프가 없다")
        values = list(odd.objects(cond, AGT_.conditionValue))
        if not values:
            raise ConfigFailure(f"[{gate}] {where}: ODD 에 {_qname(merged, cond)} 의 agt:conditionValue 가 없다 — ODD 를 먼저 확장한다 (0.4절)")
        bound = kb_lib.odd_upper_bound(str(values[0]))
        if bound is None:
            raise ConfigFailure(f"[{gate}] {where}: {_qname(merged, cond)} 의 값 {str(values[0])!r} 에서 정수 상한을 뽑을 수 없다 — Range [a .. b] 또는 UpperBound 식이어야 한다")
        if total > bound:
            errors.append(f"[{gate}] {where}: 역할별 agt:maxConcurrent 합 {total} > ODD 동적 요소 {_qname(merged, cond)} 의 상한 {bound} — 역할을 줄이거나 ODD 한도를 먼저 검토한다 (AGENTS 역할 절, 9.6절)")
    errors += _check_scope_subset(merged, odd, files)
    return errors
```
<!-- 인용 끝 -->
