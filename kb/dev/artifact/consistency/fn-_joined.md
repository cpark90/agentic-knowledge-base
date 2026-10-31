---
id: https://agentic-knowledge-base.dev/id/chunk/ccb3c961-ba27-4c5b-968c-d35f8cb91fb4
type: artifact
level: executable
title_ko: 함수 _joined (tools/consistency.py)
title: function _joined in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `_joined(pieces)` 다. 단위의 조각을 공백 하나로 잇는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _joined(pieces: list[tuple[int, str]]) -> tuple[str, list[tuple[int, int]]]:
    """단위의 조각을 공백 하나로 잇는다 → (글, [(시작 위치, 줄 번호)…]). 위치에서 줄 번호를 되찾는 데 쓴다."""
    text, starts = "", []
    for ln, seg in pieces:
        if text:
            text += " "
        starts.append((len(text), ln))
        text += seg.strip()
    return text, starts
```
<!-- 인용 끝 -->
