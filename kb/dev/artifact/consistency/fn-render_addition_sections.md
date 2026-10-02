---
id: https://agentic-knowledge-base.dev/id/chunk/c778a5be-9fdf-41cf-8945-f9ddb6ac9de6
type: artifact
level: executable
title_ko: 함수 render_addition_sections (tools/consistency.py)
title: function render_addition_sections in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2b38088c-7807-429a-a6df-e08e9a052e3a, https://agentic-knowledge-base.dev/id/chunk/75af5f0a-9a09-4d47-8289-a31801125bfe, https://agentic-knowledge-base.dev/id/chunk/fdb7f411-8074-4715-a11f-815131022f96]
part_of: https://agentic-knowledge-base.dev/id/composite/e33ee826-0842-4cdd-8e68-16823604cffa
---
**함수** — `render_addition_sections(p)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_addition_sections(p):
    lines = ["", "## ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기 (보고)", "",
             "### 메타 문장 (다음과 같다 · 이 절에서는 · 아래에서 설명한다 · 앞서 말했듯) — 판정: 주장 문장으로 바꿈 / 삭제", ""]
    lines += listing(p["meta_hits"], 50, lambda h: cite(*h)) + waived_tail(p["meta_waived"], ADDITION_GATE, lambda h: cite(*h))
    lines += ["", "### 채움 문구 (특이사항 없음 · 일반적인 방식을 따른다 · 추후 결정한다) — 판정: 세 빈 값 중 하나로 바꿈 / 실질 답으로 채움", ""]
    lines += listing(p["filler_hits"], 50, lambda h: cite(*h)) + waived_tail(p["filler_waived"], ADDITION_GATE, lambda h: cite(*h))
    lines += ["", f"### 빈 값 이상 표기 — 빈 자리는 `{'` · `'.join(kb_lib.EMPTY_VALUE)}` 셋으로만 적는다 (p4-three-empty-values)", ""]
    lines += listing(p["empty_hits"], 50, lambda h: cite(*h)) + waived_tail(p["empty_waived"], EMPTY_VALUE_GATE, lambda h: cite(*h))
    lines += ["", f"## ⑨ 목록 — 손 번호 · 항목 {LIST_MAX_ITEMS}개 이하 · 중첩 {LIST_MAX_DEPTH}단계 이하 · 항목당 {LIST_MAX_ITEM_CHARS}자 이하 · 빈 항목 (보고)", "",
              "| 규칙 | 위반 |", "|---|---|"]
    lines += [f"| {name} | {count} |" for name, count in p["list_kinds"]] or [f"| {kb_lib.NONE_MARK} | 0 |"]
    lines += ["", "### 위반 목록 (항목 길이는 이어지는 들여쓴 줄을 합치고 공백을 정규화한 뒤 센 글자 수다)", ""]
    _list_ref = lambda h: f"- `{h[0]['path']}:{h[1]}` — {h[2]}"  # noqa: E731
    lines += listing(p["list_hits"], 60, _list_ref) + waived_tail(p["list_waived"], LIST_RULES_GATE, _list_ref)
    return lines
```
<!-- 인용 끝 -->
