---
id: https://agentic-knowledge-base.dev/id/chunk/516aa2b9-e91a-4519-9bdd-e579b651a443
type: artifact
level: executable
title_ko: 함수 decision_link (tools/gen_norms.py)
title: function decision_link in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `decision_link(slug, out)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_link(slug: str, out: str) -> str:
    target = os.path.relpath(f"{DECISION_ROOT}/{slug}/{CONCLUSION_FILE}", os.path.dirname(out) or ".").replace(os.sep, "/")
    return f"[`{slug}`]({target})"
```
<!-- 인용 끝 -->
