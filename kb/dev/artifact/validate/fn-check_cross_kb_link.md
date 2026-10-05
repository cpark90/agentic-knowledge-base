---
id: https://agentic-knowledge-base.dev/id/chunk/74027bd0-148f-4997-9b67-43e438793d0b
type: artifact
level: executable
title_ko: 함수 check_cross_kb_link (tools/validate.py)
title: function check_cross_kb_link in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4, https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99, https://agentic-knowledge-base.dev/id/chunk/f3fcb094-a1c5-414e-ab93-287b0bec0449]
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_cross_kb_link(merged)` 다. KB 를 가로지르는 저작 링크의 거부 (게이트 id `cross-kb-link`, p6-executable-splits-by-kb · p8-scenario-ladder-rungs).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_cross_kb_link(merged: Graph) -> list[str]:
    """KB 를 가로지르는 저작 링크의 거부 (게이트 id `cross-kb-link`, p6-executable-splits-by-kb · p8-scenario-ladder-rungs).

    대상은 frontmatter 링크 키(`chunk2kg.LINK_KEYS`)의 직접 트리플 전부다. `defs/kb.bzl` 의 `_check_links` 는 Bazel deps
    (refines·serves·supersedes·verifies)만 받으므로 satisfies·derivesFrom·overlapsWith 같은 나머지 키는 분석 시점에 보이지
    않고, 판정에는 두 끝점의 KB·plane·수준이 필요해 타깃마다 한 청크만 보는 `chunk2kg` 도 자리가 아니다 — 병합 그래프를
    보는 여기가 자리다. 판정은 복원 후보 생성기와 같은 함수 `kb_lib.cross_kb_link` 다. 끝점이 복합체면 첫 부분을 따라
    내려가 청크의 값을 쓴다(`kb_lib.link_cells` 와 같은 규칙). plane 을 정할 수 없는 끝점은 판정하지 않는다 — 실재는
    `dangling` 이 본다.
    """
    gate = kb_lib.CROSS_KB_LINK_GATE
    plane = kb_lib.chunk_planes(merged)
    first_part: dict = {}
    for comp, part in sorted(merged.subject_objects(kb_lib.AGT.hasDirectPart), key=lambda cp: (str(cp[0]), str(cp[1]))):
        first_part.setdefault(comp, part)

    def end(node):
        seen = set()
        while node is not None and node not in seen:
            if node in plane:
                loc = str(next(merged.objects(node, kb_lib.AGT.assertionLocation), ""))
                level = str(next(merged.objects(node, kb_lib.AGT.hasLevel), "")).split("/")[-1]
                return kb_lib.kb_of(loc), plane[node], level
            seen.add(node)
            node = first_part.get(node)
        return None

    errors = []
    for key in chunk2kg.LINK_KEYS:
        for s, o in sorted(merged.subject_objects(kb_lib.AGT[key]), key=lambda so: (str(so[0]), str(so[1]))):
            src, dst = end(s), end(o)
            if src is None or dst is None or not kb_lib.cross_kb_link(key, src, dst):
                continue
            errors.append(f"[{gate}] {_chunk_location(merged, s)}: agt:{key} 가 KB 를 가로지른다 ({src[0]} {src[1]} → {dst[0]} {dst[1]}, "
                          f"대상 {_chunk_location(merged, o)}) — KB 사이 링크는 verifies 하나이고 예외는 검증 목표(functional) → "
                          f"요구 derivesFrom 뿐이다 (p6-executable-splits-by-kb · p8-scenario-ladder-rungs)")
    return errors
```
<!-- 인용 끝 -->
