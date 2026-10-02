---
id: https://agentic-knowledge-base.dev/id/chunk/0ec64ac7-ed2b-4c44-b7d8-9e704c344f79
type: artifact
level: executable
title_ko: 함수 _audit_matrix (tools/weave.py)
title: function _audit_matrix in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/75bab730-77dc-4a3d-945e-72e305b4eb8c]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_matrix(g)` 다. 추적 매트릭스 — plane × plane 의 TIM 허용 칸과 채움.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_matrix(g) -> list[str]:
    """추적 매트릭스 — plane × plane 의 TIM 허용 칸과 채움. metrics 3단계 대리와 같은 정의다."""
    body: list[str] = []
    # 6. 추적 매트릭스 — metrics 와 같은 정의 (kb_lib.TIM_CELLS · link_cells)
    seen = kb_lib.link_cells(g)
    filled = [c for c in kb_lib.TIM_CELLS if c in seen]
    outside = sorted(seen - set(kb_lib.TIM_CELLS))
    body += [f"## 추적 매트릭스 — plane × plane, TIM 허용 {len(kb_lib.TIM_CELLS)}칸 중 채움 **{len(filled)}** (metrics 3단계 대리와 같은 정의)", "",
          "| 링크 | 출발 plane | 도착 plane | 채움 |", "|---|---|---|---|"]
    body += [f"| `{k}` | `{a}` | `{b}` | {'채움' if (k, a, b) in seen else '빈 칸'} |" for k, a, b in kb_lib.TIM_CELLS]
    body += ["", f"- 허용표 밖에서 관측된 칸: {len(outside)}" + (" — " + ", ".join(f"`{k}`:{a}→{b}" for k, a, b in outside) if outside else ""), ""]
    return body
```
<!-- 인용 끝 -->
