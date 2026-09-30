---
id: https://agentic-knowledge-base.dev/id/chunk/d4b905ee-7efb-48b3-8e28-41d33ddb1f99
type: artifact
level: executable
title_ko: 절 main (tools/handoff.py)
title: section main in tools/handoff.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-handoff}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-11T09:15:09Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/92762c1c-18df-4b8e-9b9d-9d43e4811e0f]
part_of: https://agentic-knowledge-base.dev/id/composite/0b8984a8-4b3a-4b30-9c38-041302b18093
composite: {id: https://agentic-knowledge-base.dev/id/composite/0b8984a8-4b3a-4b30-9c38-041302b18093, title_ko: 절 복합체 main (tools/handoff.py), title: section composite main in tools/handoff.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d4b905ee-7efb-48b3-8e28-41d33ddb1f99, https://agentic-knowledge-base.dev/id/chunk/d2c6d26d-171a-421d-93af-57b68ab462fc], part_of: https://agentic-knowledge-base.dev/id/composite/b1ea15c6-7e5e-4365-91b4-7b2f4ad29839}
---
**절** — `tools/handoff.py` 의 절 `main` 다. 읽은 청크를 새 청크의 sources 로 옮긴다

**정의** — `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 읽은 청크를 새 청크의 sources 로 옮긴다 ────────────────────



if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- 인용 끝 -->
