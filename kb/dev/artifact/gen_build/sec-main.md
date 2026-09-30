---
id: https://agentic-knowledge-base.dev/id/chunk/6f05d1bb-343d-40c7-bba6-b73ba4cedde4
type: artifact
level: executable
title_ko: 절 main (tools/gen_build.py)
title: section main in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/047c5c56-2b6c-4f8b-993e-32f3a35fd1d6, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c, https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e]
part_of: https://agentic-knowledge-base.dev/id/composite/e563bac1-7552-474e-a036-f6ced4999bc4
composite: {id: https://agentic-knowledge-base.dev/id/composite/e563bac1-7552-474e-a036-f6ced4999bc4, title_ko: 절 복합체 main (tools/gen_build.py), title: section composite main in tools/gen_build.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/6f05d1bb-343d-40c7-bba6-b73ba4cedde4, https://agentic-knowledge-base.dev/id/chunk/c45073d7-38c4-4ed0-bea8-16920059e835], part_of: https://agentic-knowledge-base.dev/id/composite/9bb41e68-1b5c-4d4c-aee0-32a2899bedf9}
---
**절** — `tools/gen_build.py` 의 절 `main` 다. 드리프트 비교와 실행

**정의** — `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 드리프트 비교와 실행 ────────────────────



if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- 인용 끝 -->
