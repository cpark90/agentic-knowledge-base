---
id: https://agentic-knowledge-base.dev/id/chunk/17fdb102-0df9-45f2-93ff-c64b4df55d44
type: artifact
level: executable
title_ko: 함수 merge (tools/chunk2kg.py)
title: function merge in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/3bc19461-0841-4806-aafd-93fdbc5f9ab3, https://agentic-knowledge-base.dev/id/chunk/480b1d93-d4ad-4a70-8cea-3d25a7966d12, https://agentic-knowledge-base.dev/id/chunk/f418fcb4-df9f-496c-9cc7-09f83dc5d1e5]
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `merge(out, fragments)` 다. 타깃별 head 조각(--fragment 출력)을 하나의 -kg 로 병합한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def merge(out: str, fragments: list) -> int:
    """타깃별 head 조각(--fragment 출력)을 하나의 -kg 로 병합한다. IRI 중복 검사는 여기서 한다 (한 단위 지식은 한 파일).

    링크·증거 블록은 중복 검사 대상이 아니다 — 뿌리 uuid 로 IRI 를 다시 계산하면(rebase_links) 원본과 조각을 가리키는 링크가
    같은 IRI 가 되는 것이 설계다. 조각 → 원본 사상은 단위 지식 블록의 prov:specializationOf 에서 읽는다.
    """
    chunks, comps, seen, errors = [], [], {}, []
    graves: dict = {}  # 묘비 IRI → 블록 — 단위 지식과 같은 IRI 면 아래 중복 검사가 거부한다
    spec: dict = {}
    for frag in fragments:
        try:
            text = Path(frag).read_text(encoding="utf-8").strip("\n")
        except OSError as e:
            print(f"FAIL [chunk2kg-merge] {frag}: 조각을 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        for block in (b for b in text.split("\n\n") if b.strip()):
            iri = block.split("\n", 1)[0].strip("<>")
            if is_link_block(iri):
                chunks.append((iri, block))
                continue
            if is_tombstone_block(block) and iri in graves:  # 같은 묘비를 여러 타깃이 선언한다 — 바이트가 같으면 한 번만 둔다
                if graves[iri] != block:
                    errors.append(f"{frag}: 묘비 {iri} 의 선언이 {seen[iri]} 와 다르다 — 같은 지운 항목의 라벨·위치는 하나다 (Q-0061#Q146)")
                continue
            if iri in seen:
                errors.append(f"{frag}: IRI {iri} 가 {seen[iri]} 와 중복 — 한 단위 지식은 한 파일이다")
                continue
            seen[iri] = frag
            if is_tombstone_block(block):
                graves[iri] = block
            m = _SPEC_LINE.search(block)
            if m:
                spec[iri] = m.group(1)
            (comps if "\n    a agt:Composite" in block else chunks).append((iri, block))
    if errors:
        for e in errors:
            print(f"FAIL [chunk2kg-merge] {e}", file=sys.stderr)
        return EXIT_FAIL
    chunks, spec_errors = rebase_links(chunks, spec)
    if spec_errors:
        for e in spec_errors:
            print(f"FAIL [{SPECIALIZATION_GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL
    blocks = [b for _, b in sorted(chunks)] + [b for _, b in sorted(comps)]
    Path(out).write_text(PREAMBLE + "\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
