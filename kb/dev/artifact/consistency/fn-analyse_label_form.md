---
id: https://agentic-knowledge-base.dev/id/chunk/494af882-5ab4-45d1-a95f-198bf734d66d
type: artifact
level: executable
title_ko: 함수 analyse_label_form (tools/consistency.py)
title: function analyse_label_form in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/980ff6a4-1f10-4e39-bd06-73c6c65e5d37
---
**함수** — `analyse_label_form(items)` 다. ⑤ 결론 라벨 형식 — 결정의 결론만 문장형.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_label_form(items):
    """⑤ 결론 라벨 형식 — 결정의 결론만 문장형. 판정은 경로 basename: conclusion.md 이거나
    근거·대안(rationale.md·alternatives.md)이 아닌 단일 파일 결정(chunks/decision/d-*.md)
    """
    def is_conclusion(it):
        return it["type"] == "decision" and Path(it["path"]).name not in ("rationale.md", "alternatives.md")

    return [it for it in items if is_conclusion(it) and not re.search(r"(다|음|함|없음|있음)$", it["title_ko"])]
```
<!-- 인용 끝 -->
