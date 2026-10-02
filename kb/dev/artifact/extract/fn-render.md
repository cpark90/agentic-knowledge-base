---
id: https://agentic-knowledge-base.dev/id/chunk/3310d256-a896-401a-ba40-e6bfdc0d474a
type: artifact
level: executable
title_ko: 함수 render (tools/extract.py)
title: function render in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/719f0696-c0dc-4eff-aa6d-bb4dcdf148ce, https://agentic-knowledge-base.dev/id/chunk/cea6fcfc-b3e0-4dab-b8f5-e0727ee9c70d]
part_of: https://agentic-knowledge-base.dev/id/composite/bdbaec34-7407-4d5e-83f8-0706026f0b98
---
**함수** — `render(c, reg, at)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(c: Chunk, reg: dict, at: str = "") -> str:
    fm = [f"id: {c.iri}", "type: artifact", "level: executable", f"title_ko: {c.title_ko}", f"title: {c.title}",
          "status: stable", f"sources: [{{resource: {reg['resource']}}}]", f"assumes: [{DEFAULT_ASSUMES}]",
          f"generated: {{by: {kb_lib.EXTRACT_ACTOR}, at: {at or reg['at']}}}"]
    if reg.get(kb_lib.LAYER_KEY):  # 서비스 층 — 등록부가 소스 하나의 층을 선언하고 그 선언이 생성 청크 전부(정의·절·파일)로
        fm.append(f"{kb_lib.LAYER_KEY}: {reg[kb_lib.LAYER_KEY]}")  # 옮겨진다. 도구는 프로세스 층의 실행 표면이다 (p0-service-is-a-three-layer-wiki)
    if stamped(reg):  # 테스트 통과 도장 — 소스가 도장 뒤에 바뀌면 빠진다 (수정 뒤 미검증, 재판정 자동)
        fm.append(f"verified: [{{by: {kb_lib.STAMP_ACTOR}, at: {reg[kb_lib.STAMP_KEY]['at']}}}]")
    for key in ("refines", "serves"):
        if c.links.get(key):
            fm.append(f"{key}: [" + ", ".join(c.links[key]) + "]")
    if c.uses:  # agt:usesDefinition — 링크 키가 아니다(references 족): deps 도 링크 개체도 아니고 직접 트리플만 남는다
        fm.append(f"{kb_lib.USES_KEY}: [" + ", ".join(c.uses) + "]")
    if c.part_of:
        fm.append(f"part_of: {c.part_of}")
    if c.composite:
        inner = [f"id: {c.composite['id']}", f"title_ko: {c.composite['title_ko']}", f"title: {c.composite['title']}",
                 "ordered: [" + ", ".join(c.composite["ordered"]) + "]"]
        if c.composite.get("part_of"):
            inner.append(f"part_of: {c.composite['part_of']}")
        fm.append("composite: {" + ", ".join(inner) + "}")
    return "---\n" + "\n".join(fm) + "\n---\n" + "\n".join(c.body) + "\n"
```
<!-- 인용 끝 -->
