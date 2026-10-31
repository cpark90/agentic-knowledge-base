---
id: https://agentic-knowledge-base.dev/id/chunk/578f22f5-4d9d-43ef-8b3a-1459989cf6e9
type: artifact
level: executable
title_ko: 함수 label_stmts (tools/chunk2kg.py)
title: function label_stmts in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b]
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
---
**함수** — `label_stmts(en, ko, former)` 다. 라벨 술어 — rdfs:label @en·@ko 와 옛 이름마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_stmts(en: str, ko: str, former: list | None) -> list:
    """라벨 술어 — rdfs:label @en·@ko 와 옛 이름마다 skos:hiddenLabel @ko. 단위 지식과 복합체가 같은 꼴로 낸다 (p0-skos-label-synonyms)."""
    return [f'rdfs:label "{esc(en)}"@en', f'rdfs:label "{esc(ko)}"@ko', *(f'skos:hiddenLabel "{esc(f)}"@ko' for f in former or [])]
```
<!-- 인용 끝 -->
