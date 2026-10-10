---
id: https://agentic-knowledge-base.dev/id/chunk/494af882-5ab4-45d1-a95f-198bf734d66d
type: artifact
level: executable
title_ko: 함수 analyse_label_form (tools/consistency.py)
title: function analyse_label_form in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a5547d6c-a232-4c09-83b0-81eb591e8bc6]
part_of: https://agentic-knowledge-base.dev/id/composite/980ff6a4-1f10-4e39-bd06-73c6c65e5d37
---
**함수** — `analyse_label_form(items)` 다. ⑤ 결론 라벨 형식 — 결정의 결론만 문장형.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_label_form(items):
    """⑤ 결론 라벨 형식 — 결정의 결론만 문장형. 판정은 kb_lib.decision_role_marker(경로) == 결론 이다:
    conclusion.md·단일 파일 결정은 결론이고 근거·대안·규약·시나리오의 자극·요인·배제 자극은 결론이 아니다
    """
    def is_conclusion(it):
        return it["type"] == "decision" and kb_lib.decision_role_marker(it["path"]) == "결론"

    return [it for it in items if is_conclusion(it) and not re.search(r"(다|음|함|없음|있음)$", it["title_ko"])]
```
<!-- 인용 끝 -->
