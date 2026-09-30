---
id: https://agentic-knowledge-base.dev/id/chunk/ea41de7a-a1a9-49fe-99e7-8d5dbecd8400
type: artifact
level: executable
title_ko: 함수 render_candidate_sections (tools/consistency.py)
title: function render_candidate_sections in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/27289d77-d4f2-4cbc-9869-da8cbbc5d2c8
---
**함수** — `render_candidate_sections(dup_candidates, placement, ref)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_candidate_sections(dup_candidates, placement, ref):
    lines = ["", "## ⑩ 중복 확정 후보 (①·③의 미묶음 쌍 — 판정자 질문: 이 두 블록은 같은 주장을 담는가?)", ""]
    for j, x, y in dup_candidates[:50]:
        lines.append(f"- {kb_lib.num(j)}: {ref(x)}  ↔  {ref(y)}")
    if not dup_candidates:
        lines.append("- 없음")
    if len(dup_candidates) > 50:
        lines.append(f"- … {len(dup_candidates) - 50}건 더")
    lines += ["", "## ⑪ 자리 후보 (다른 슬롯 표지어 재등장 — 판정자 질문: 이 문장이 그 슬롯에 있어야 하는가?)", ""]
    for it, own, other, quote in placement[:50]:
        lines.append(f"- `{own}` 영역에서 `{other}` 발견: {ref(it)} — \"{quote}\"")
    if not placement:
        lines.append("- 없음")
    if len(placement) > 50:
        lines.append(f"- … {len(placement) - 50}건 더")
    lines.append("")
    return lines
```
<!-- 인용 끝 -->
