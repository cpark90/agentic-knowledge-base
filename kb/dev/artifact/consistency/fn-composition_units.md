---
id: https://agentic-knowledge-base.dev/id/chunk/a133095c-86c0-4a59-9f2d-22259a6708f4
type: artifact
level: executable
title_ko: 함수 composition_units (tools/consistency.py)
title: function composition_units in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53]
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `composition_units(text)` 다. 산문 조각(kb_lib.prose_segments)을 단위로 묶는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def composition_units(text: str) -> list[tuple[str, list[tuple[int, str]]]]:
    """산문 조각(kb_lib.prose_segments)을 단위로 묶는다 → [(종류, [(줄 번호, 조각)…])]. 종류는 제목·문단·목록 항목·표 셀이다.

    손 줄바꿈으로 접힌 문단과 목록 항목은 이어지는 줄을 한 단위로 합친다 — 줄 끝의 괄호가 다음 줄의 서술로 이어지는지
    보려면 문단 단위로 읽어야 한다. 링크 대상(`](…)`·URL)은 산문이 아니라 먼저 지운다. 빈 줄은 prose_segments 가
    내지 않으므로 줄 번호가 끊기면 단위도 끊긴다.
    """
    units: list[tuple[str, list[tuple[int, str]]]] = []
    prev_ln = None
    for ln, seg in prose_segments(text):
        seg = COMPOSITION_LINK_TARGET.sub(lambda m: "]" if m.group(0).startswith("]") else " ", seg)
        body = re.sub(r"^\s*>\s?", "", seg)
        if COMPOSITION_HEADING.match(body):
            units.append(("제목", [(ln, body)]))
        elif body.lstrip().startswith("|"):
            units += [("셀", [(ln, cell)]) for cell in body.strip().strip("|").split("|") if cell.strip()]
        elif COMPOSITION_ITEM.match(body):
            units.append(("항목", [(ln, COMPOSITION_ITEM.sub("", body, count=1))]))
        elif units and prev_ln == ln - 1 and units[-1][0] in ("문단", "항목"):
            units[-1][1].append((ln, body))
        else:
            units.append(("문단", [(ln, body)]))
        prev_ln = ln
    return units
```
<!-- 인용 끝 -->
