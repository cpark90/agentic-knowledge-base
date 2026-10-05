---
id: https://agentic-knowledge-base.dev/id/chunk/8db23029-817e-4897-aa0b-a3c9b3d966e0
type: artifact
level: executable
title_ko: 함수 with_links (tools/gen_norms.py)
title: function with_links in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/d6ddca76-30dd-4d32-aa28-9f123fb1751e]
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `with_links(text, links)` 다. 결정 링크를 첫 문장 끝(마침표 앞)에 둔다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def with_links(text: str, links: list[str]) -> str:
    """결정 링크를 첫 문장 끝(마침표 앞)에 둔다 — 링크 위치의 정규화 규칙 하나다 (p12-norm-documents-from-section-chunks).

    첫 문장이 굵은 span 안에서 끝나면(`**…다.** …`) 마침표를 span 밖으로 옮겨 `**…다** (링크). …` 로 낸다.
    """
    cite = "(" + ", ".join(links) + ")"
    pos = first_sentence_end(text)
    if pos is None:
        return f"{text} {cite}"
    i, bold = pos
    if bold:
        return f"{text[:i]}** {cite}.{text[i + 3:]}"
    return f"{text[:i]} {cite}{text[i:]}"
```
<!-- 인용 끝 -->
