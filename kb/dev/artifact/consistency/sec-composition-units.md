---
id: https://agentic-knowledge-base.dev/id/chunk/52b1c442-b7c8-4e85-bef1-2cda8ff8d862
type: artifact
level: executable
title_ko: 절 composition-units (tools/consistency.py)
title: section composition-units in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
composite: {id: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45, title_ko: 절 복합체 composition-units (tools/consistency.py), title: section composite composition-units in tools/consistency.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/52b1c442-b7c8-4e85-bef1-2cda8ff8d862, https://agentic-knowledge-base.dev/id/chunk/a133095c-86c0-4a59-9f2d-22259a6708f4, https://agentic-knowledge-base.dev/id/chunk/ccb3c961-ba27-4c5b-968c-d35f8cb91fb4, https://agentic-knowledge-base.dev/id/chunk/378dc204-7474-4a47-ab11-c9fc4cb5c778, https://agentic-knowledge-base.dev/id/chunk/cd5413ed-eaa2-466b-b701-bb182e0a5377, https://agentic-knowledge-base.dev/id/chunk/cfb0a4b8-f534-4e19-875d-07dfe88eb9b4, https://agentic-knowledge-base.dev/id/chunk/004314d0-b3f3-4281-9fdf-7c7454babcad, https://agentic-knowledge-base.dev/id/chunk/7a94b224-3b1c-4dea-b118-924d591a9729], part_of: https://agentic-knowledge-base.dev/id/composite/65bc7b55-1885-496f-8600-24e609326f5f}
---
**절** — `tools/consistency.py` 의 절 `composition-units` 다. 축 ⑫ 문장 구성 — 규칙 3·4·5·6 의 정규식 대리

**정의** — `composition_units` · `_joined` · `_convention_stops` · `_line_at` · `_paren_groups` · `check_composition` · `analyse_composition` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 축 ⑫ 문장 구성 — 규칙 3·4·5·6 의 정규식 대리 ────────────────────












COMPOSITION_RULES = (("symbol", "산문 기호 (규칙 3)"), ("noun_end", "명사형 끝맺음 (규칙 4)"),
                     ("chain", "가운뎃점 연쇄 (규칙 5)"), ("paren", "문장 가운데 괄호 (규칙 6)"))
```
<!-- 인용 끝 -->
