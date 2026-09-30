---
id: https://agentic-knowledge-base.dev/id/chunk/9995ae36-ac6f-4afb-9596-0ef58fa2a582
type: artifact
level: executable
title_ko: 함수 check_spec_form (tools/chunk_lint.py)
title: function check_spec_form in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3
---
**함수** — `check_spec_form(text)` 다. 첨가와 목록 규칙 (STYLEGUIDE §0, 결정 p4-slot-answers-one-question·p4-three-empty-values) → [(게이트 id, 줄 번호, 이유)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_spec_form(text: str) -> list[tuple[str, int, str]]:
    """첨가와 목록 규칙 (STYLEGUIDE §0, 결정 p4-slot-answers-one-question·p4-three-empty-values) → [(게이트 id, 줄 번호, 이유)].

    판정은 consistency ⑧·⑨ 와 같은 함수(kb_lib.check_addition·check_lists)가 한다. 여기서 하는 것은 게이트 id 를 붙이고
    메시지의 인용을 수정 방향으로 만드는 일뿐이다 — 검사를 복제하지 않는다 (STYLEGUIDE §7 단일 정의처).
    """
    meta, filler, empty = kb_lib.check_addition(text)
    out = [(ADDITION, ln, f'메타 문장 "{expr}" — 슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다 (STYLEGUIDE §0): {quote}')
           for ln, expr, quote in meta]
    out += [(ADDITION, ln, f'채움 문구 "{expr}" — 채움 자리에는 세 빈 값 중 하나를 쓰거나 실질 답을 적는다 (STYLEGUIDE §0): {quote}')
            for ln, expr, quote in filler]
    out += [(EMPTY_VALUE, ln, f'빈 값 표기 "{expr}" — 빈 자리는 `{"` · `".join(kb_lib.EMPTY_VALUE)}` 셋으로만 적는다 (STYLEGUIDE §0): {quote}')
            for ln, expr, quote in empty]
    out += [(LIST_RULES, ln, why) for ln, why in kb_lib.check_lists(text)]
    return sorted(out, key=lambda t: (t[1], t[0]))
```
<!-- 인용 끝 -->
