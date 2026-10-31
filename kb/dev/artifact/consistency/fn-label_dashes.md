---
id: https://agentic-knowledge-base.dev/id/chunk/87a05eea-98e4-4ec6-adfb-c640e180af29
type: artifact
level: executable
title_ko: 함수 label_dashes (tools/consistency.py)
title: function label_dashes in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/02bb9c9f-7720-4f02-ae31-b3eee5ba6865
---
**함수** — `label_dashes(seg)` 다. ⑦ 의 분자에서 뺄 라벨 대시 수 — 줄·셀 첫머리 라벨(kb_lib.PROSE_LABEL_DASH)과 줄 가운데 굵은 라벨(BOLD_LABEL_DASH) 뒤의 대시다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_dashes(seg: str) -> int:
    """⑦ 의 분자에서 뺄 라벨 대시 수 — 줄·셀 첫머리 라벨(kb_lib.PROSE_LABEL_DASH)과 줄 가운데 굵은 라벨(BOLD_LABEL_DASH) 뒤의
    대시다. 같은 대시를 두 정규식이 함께 잡을 수 있어 대시 위치의 합집합으로 센다."""
    spots = {m.end() - 2 for m in PROSE_LABEL_DASH.finditer(seg)} | {m.end() - 2 for m in BOLD_LABEL_DASH.finditer(seg)}
    return len(spots)
```
<!-- 인용 끝 -->
