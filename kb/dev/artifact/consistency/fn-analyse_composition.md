---
id: https://agentic-knowledge-base.dev/id/chunk/7a94b224-3b1c-4dea-b118-924d591a9729
type: artifact
level: executable
title_ko: 함수 analyse_composition (tools/consistency.py)
title: function analyse_composition in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/004314d0-b3f3-4281-9fdf-7c7454babcad]
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `analyse_composition(items)` 다. ⑫ 문장 구성 — 규칙마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_composition(items):
    """⑫ 문장 구성 — 규칙마다 [(항목, 줄, 표현)…]. 보고이고 게이트가 아니다 — 판정은 리뷰가 한다(p0-sentence-composition)."""
    out: dict[str, list] = {key: [] for key, _ in COMPOSITION_RULES}
    for it in items:
        for key, hits in check_composition(Path(it["path"]).read_text(encoding="utf-8")).items():
            out[key] += [(it, ln, expr) for ln, expr in hits]
    return out
```
<!-- 인용 끝 -->
