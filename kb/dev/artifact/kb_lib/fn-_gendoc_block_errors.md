---
id: https://agentic-knowledge-base.dev/id/chunk/845f9424-b055-43c1-bbc8-afa6627dffe2
type: artifact
level: executable
title_ko: 함수 _gendoc_block_errors (tools/kb_lib.py)
title: function _gendoc_block_errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a0841084-48a1-45f6-842a-57f5b8cbf0c9, https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d, https://agentic-knowledge-base.dev/id/chunk/ecb06437-81f9-480c-90ba-0b78a8fde56b]
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
---
**함수** — `_gendoc_block_errors(path, lines, start, body, first, rows, quoted, exists)` 다. G11·G12·G13 — 펜스의 언어·목차 절의 존재·링크 대상의 실재.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_block_errors(path, lines: list[str], start: int, body: list[str], first: int,
                         rows: list, quoted: set, exists) -> list[tuple[int, str]]:
    """G11·G12·G13 — 펜스의 언어·목차 절의 존재·링크 대상의 실재. 문서 밖을 보는 판정이 여기 모인다."""
    errors: list[tuple[int, str]] = []
    # G11 — 펜스 코드 블록에 언어를 명시한다 (MD040)
    fence = None
    for i, line in enumerate(lines[start:], start=start + 1):
        m = MD_FENCE.match(line)
        if not m:
            continue
        if fence:
            if m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        fence = m.group(1)
        if i not in quoted and not line.strip()[len(m.group(1)):].strip():
            errors.append((i, "G11 펜스 코드 블록에 언어를 명시한다 (MD040) — 예 ```text"))

    # G12 — 긴 문서는 목차 절을 둔다
    headings = [(ln, MD_HEADING.match(line).group(2).strip()) for ln, line in rows if MD_HEADING.match(line)]
    if len(body) > GENDOC_TOC_MIN and not any(h == GENDOC_TOC_HEADING for _, h in headings):
        errors.append((first, f"G12 본문 {len(body)}줄이 {GENDOC_TOC_MIN}줄을 넘는데 `{GENDOC_TOC_HEADING}` 절이 없다 "
                              "(ISO/IEC/IEEE 26514:2022 9.10.5) — kb_lib.gendoc_toc 를 쓴다"))

    # G13 — 링크의 경로와 앵커가 생성물이 놓이는 위치 기준으로 실재한다
    anchors = {a for _, h in headings for a in [slug(h)]} | md_anchors(lines)
    doc_dir = os.path.dirname(str(path))
    for ln, line in rows:
        for dest in find_links(MD_CODE_SPAN.sub(" ", line)):
            if not dest or MD_SCHEME.match(dest):
                continue
            target, _, frag = dest.partition("#")
            if not target:
                if frag and frag not in anchors:
                    errors.append((ln, f"G13 없는 앵커 ({dest}) — 이 문서의 제목 slug 에 #{frag} 가 없다"))
                continue
            if exists is None:
                continue
            rel = os.path.normpath(target[1:] if target.startswith("/") else os.path.join(doc_dir, target))
            if not exists(rel):
                errors.append((ln, f"G13 깨진 링크 ({dest}) — {rel} 가 없다. 생성물은 전 패키지를 한 파일로 합치므로 "
                                   "파일명 상대 링크가 성립하지 않는다. 문서 안 앵커나 저장소 루트 기준 경로(`/`로 시작)로 적는다"))
    return errors
```
<!-- 인용 끝 -->
