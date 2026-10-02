---
id: https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7
type: artifact
level: executable
title_ko: 함수 gendoc_assemble (tools/kb_lib.py)
title: function gendoc_assemble in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0a822cf9-05aa-4c0f-90e3-b293ed84a187, https://agentic-knowledge-base.dev/id/chunk/0ab35aa5-30f6-4c8f-bad6-683509ab787a, https://agentic-knowledge-base.dev/id/chunk/5bf58955-471b-4373-9bc5-24cef0d7f893, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `gendoc_assemble(head, body, inputs, input_kind, toc_note, toc_levels)` 다. 머리 블록 + (G12 가 요구하면) 목차 + 본문 + (G4 가 요구하면) 입력 파일 절 → 문서 전체.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_assemble(head: list[str], body: list[str], inputs, input_kind: str = "입력 파일",
                    toc_note: str = "", toc_levels=(2,)) -> str:
    """머리 블록 + (G12 가 요구하면) 목차 + 본문 + (G4 가 요구하면) 입력 파일 절 → 문서 전체.

    목차 앵커는 문서 전체의 제목으로 계산한다 — 같은 slug 의 -1, -2 구분이 실제 문서와 같아야 링크가 산다.
    본문이 이미 목차 절을 가지면 덧붙이지 않는다.
    """
    n_files = len({gendoc_input_name(p) for p in inputs})
    tail = gendoc_inputs_section(inputs, input_kind) if n_files > GENDOC_INPUT_INLINE_MAX else []
    rest = list(body) + tail
    have_toc = any(t == GENDOC_TOC_HEADING for _, t in _gendoc_headings(rest))
    if len(head) + len(rest) <= GENDOC_TOC_MIN or have_toc:
        return "\n".join(head + rest) + "\n"
    hs = [(2, GENDOC_TOC_HEADING)] + _gendoc_headings(rest)
    anchors = heading_anchors([t for _, t in hs])
    toc = [f"## {GENDOC_TOC_HEADING}", ""] + ([toc_note, ""] if toc_note else [])
    toc += [f"- [{t}](#{a})" for (lvl, t), a in list(zip(hs, anchors))[1:] if lvl in toc_levels]
    return "\n".join(head + toc + [""] + rest) + "\n"
```
<!-- 인용 끝 -->
