---
id: https://agentic-knowledge-base.dev/id/chunk/d0952dad-2a90-465f-bce8-0789223da6e8
type: artifact
level: executable
title_ko: 함수 form_of (tools/gen_norms.py)
title: function form_of in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `form_of(meta)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def form_of(meta: dict) -> str:
    return meta.get(NORM_FORM_KEY, NORM_FORM_DEFAULT)
```
<!-- 인용 끝 -->
