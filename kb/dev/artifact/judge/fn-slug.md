---
id: https://agentic-knowledge-base.dev/id/chunk/81e5e72c-14de-43e1-ac54-19566c8df95e
type: artifact
level: executable
title_ko: 함수 slug (tools/judge.py)
title: function slug in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add
---
**함수** — `slug(s)` 다. 판정자 식별자 → 파일명 조각.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def slug(s: str) -> str:
    """판정자 식별자 → 파일명 조각. 세션 식별자에 `/`·공백이 섞여도 append-only 파일명이 갈리지 않는다."""
    return _SLUG.sub("-", s.lower()).strip("-") or "judge"
```
<!-- 인용 끝 -->
