---
id: https://agentic-knowledge-base.dev/id/chunk/3bc19461-0841-4806-aafd-93fdbc5f9ab3
type: artifact
level: executable
title_ko: 함수 rebase_links (tools/chunk2kg.py)
title: function rebase_links in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1b8a9132-b68b-46c7-a14e-55e7048494e2, https://agentic-knowledge-base.dev/id/chunk/38150f41-1adc-4ea1-9c7f-f722f721fe9a, https://agentic-knowledge-base.dev/id/chunk/4dcdeb22-0819-48a5-96a4-72da225a3003, https://agentic-knowledge-base.dev/id/chunk/8a9578b7-a0d9-4b0a-951e-aed33d8b8825, https://agentic-knowledge-base.dev/id/chunk/9e16611b-2397-4b7d-a033-267e745a1aeb, https://agentic-knowledge-base.dev/id/chunk/f418fcb4-df9f-496c-9cc7-09f83dc5d1e5]
part_of: https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828
---
**함수** — `rebase_links(blocks, spec)` 다. (IRI, 블록) 목록의 링크·증거 블록 IRI 를 뿌리 uuid 로 다시 계산하고 같은 IRI 의 블록을 합친다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def rebase_links(blocks: list, spec: dict) -> tuple:
    """(IRI, 블록) 목록의 링크·증거 블록 IRI 를 뿌리 uuid 로 다시 계산하고 같은 IRI 의 블록을 합친다 → (블록 목록, 오류 목록).

    spec 은 조각 → 원본 사상(청크 블록의 prov:specializationOf). 링크 블록의 linkFrom·linkTo 를 work_id 로 올려 link_hash 를 다시
    구하고, 해시가 바뀐 링크의 증거 IRI(같은 해시 + 접미)도 함께 바꾼다. 원본을 가리키던 링크 X→O 와 조각을 가리키는 X→F 는
    같은 IRI 가 되어 한 블록이 된다 — 술어별 목적어의 합집합(linkTo 둘, evidenceRef 둘). 청크·복합체 블록은 그대로 둔다.
    사슬 순환은 오류(게이트 id specialization, 순환마다 한 번)다. 합쳐진 블록의 목적어는 정렬 합집합이라 조각 순서와 무관하게 결정적이다.
    """
    errors = [f"{SPECIALIZATION_KEY} 사슬이 순환한다: {' → '.join(cyc + (cyc[0],))} — 조각은 원본을, 원본은 조각을 가리키지 않는다"
              for cyc in spec_cycles(spec)]  # 순환마다 한 번 — 뿌리를 계산할 수 없으므로 링크 IRI 재계산은 하지 않는다
    if errors:
        return blocks, errors
    roots: dict = {}

    def root(iri: str) -> str:
        if iri not in roots:
            roots[iri] = work_id(iri, spec)
        return roots[iri]

    remap: dict = {}
    links, evidences, rest = [], [], []
    for iri, block in blocks:
        if not is_link_block(iri):
            rest.append((iri, block))
            continue
        (links if iri.startswith(LINK_PREFIX) else evidences).append(parse_block(block))
    for iri, stmts in links:
        d = dict(stmts)
        frm, to, kind = d.get("agt:linkFrom", []), d.get("agt:linkTo", []), d.get("agt:linkKind", [""])[0]
        hashes = {link_hash(root(f.strip("<>")), kind.split(":", 1)[-1], root(t.strip("<>"))) for f in frm for t in to}
        old = iri[len(LINK_PREFIX):]
        if len(hashes) == 1 and (new := hashes.pop()) != old:
            remap[old] = new
    def rebased(iri: str) -> str:  # 링크·증거 IRI 의 해시 12자를 바꾼다 — 접미(-proposal)는 그대로
        for prefix in (LINK_PREFIX, EVIDENCE_PREFIX):
            if iri.startswith(prefix):
                old = iri[len(prefix):len(prefix) + 12]
                return prefix + remap.get(old, old) + iri[len(prefix) + 12:]
        return iri

    merged: dict = {}
    for iri, stmts in links + evidences:
        iri = rebased(iri)
        stmts = [(p, [f"<{rebased(o.strip('<>'))}>" if o.startswith("<") else o for o in objs]) for p, objs in stmts]
        if iri not in merged:
            merged[iri] = [(p, list(objs)) for p, objs in stmts]
            continue
        have = merged[iri]  # 같은 IRI 의 두 번째 블록부터 — 술어별 목적어의 정렬 합집합이라 조각 순서와 무관하게 결정적이다 (단일 실행 = 병합)
        for p, objs in stmts:
            slot = next((h for h in have if h[0] == p), None)
            if slot is None:
                have.append((p, list(objs)))
            else:
                slot[1][:] = sorted(set(slot[1]) | set(objs))
    return rest + [(iri, render_block(iri, stmts)) for iri, stmts in merged.items()], errors
```
<!-- 인용 끝 -->
