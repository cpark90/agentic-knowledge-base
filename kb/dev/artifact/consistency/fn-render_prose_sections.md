---
id: https://agentic-knowledge-base.dev/id/chunk/3fb3488f-84db-417e-a7a7-e9b0b62db5cc
type: artifact
level: executable
title_ko: 함수 render_prose_sections (tools/consistency.py)
title: function render_prose_sections in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/cef7d803-9333-471c-b5a0-13926f494915
---
**함수** — `render_prose_sections(hedge_hits, colloq_hits, dash_dense, ref)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_prose_sections(hedge_hits, colloq_hits, dash_dense, ref):
    lines = ["", "## ⑦ 단정성 — 추측·구어·대시 밀도 (보고; 경어·감탄은 게이트 `prose` 가 거부한다)", "",
             "### 추측 표현 (것 같·듯하·듯싶·아닐까·않을까·수도 있·아마도·아마) — 판정: 단정으로 고침 / 삭제 / 유지", ""]
    for it, ln, expr in hedge_hits[:50]:
        lines.append(f"- `{expr}`: `{it['path']}:{ln}` — {it['title_ko']}")
    if not hedge_hits:
        lines.append("- 없음")
    if len(hedge_hits) > 50:
        lines.append(f"- … {len(hedge_hits) - 50}건 더")
    lines += ["", "### 구어 후보 (근데·그냥·좀·엄청·뭔가·약간) — `되게`·`진짜`는 정상 용법이 많아 후보에 넣지 않는다", ""]
    for it, ln, expr in colloq_hits[:50]:
        lines.append(f"- `{expr}`: `{it['path']}:{ln}` — {it['title_ko']}")
    if not colloq_hits:
        lines.append("- 없음")
    if len(colloq_hits) > 50:
        lines.append(f"- … {len(colloq_hits) - 50}건 더")
    lines += ["", "### 대시 밀도 > 1.0 (문장당 \" — \" 수, 줄·불릿·셀 첫머리의 라벨 대시 제외; 문장 = 마침표 종결 또는 종결 \"다\" + `|`·`)`·닫는 따옴표·줄끝; 상위 20)", ""]
    for density, dashes, sentences, it in dash_dense[:20]:
        lines.append(f"- {kb_lib.num(density)} (대시 {dashes} / 문장 {sentences}): {ref(it)}")
    if not dash_dense:
        lines.append("- 없음")
    if len(dash_dense) > 20:
        lines.append(f"- … {len(dash_dense) - 20}건 더")
    return lines
```
<!-- 인용 끝 -->
