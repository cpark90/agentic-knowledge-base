---
id: https://agentic-knowledge-base.dev/id/chunk/f11c5dc9-3d98-4e83-809b-c9350807f5a0
type: artifact
level: executable
title_ko: 절 core-root (tools/kb_lib.py)
title: section core-root in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb
composite: {id: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb, title_ko: 절 복합체 core-root (tools/kb_lib.py), title: section composite core-root in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/f11c5dc9-3d98-4e83-809b-c9350807f5a0, https://agentic-knowledge-base.dev/id/chunk/5bbe9743-feb1-4ec4-8678-c5b66eb40f83, https://agentic-knowledge-base.dev/id/chunk/8ed1af77-96cb-4d77-ae1e-028946b9ebb8, https://agentic-knowledge-base.dev/id/chunk/5690d157-cae5-4d04-8a72-b47782cadf6b, https://agentic-knowledge-base.dev/id/chunk/c72423ba-8082-4594-8317-046edbd135ed], part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2}
---
**절** — `tools/kb_lib.py` 의 절 `core-root` 다. 코어와 작업 트리의 두 뿌리 (task 0327 손질 5·6)

**정의** — `core_root` · `workspace_root` · `core_path` · `default_residency` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 코어와 작업 트리의 두 뿌리 (task 0327 손질 5·6) ────────────────────────────────────────────────
# 이 모듈이 다른 저장소의 Bazel 의존이 되면 도구가 읽는 파일의 뿌리가 둘로 갈린다. 이 모듈이 원본인 T-Box·값 어휘(코어)는
# runfiles 의 이 모듈 디렉토리에 있고, 호출 저장소의 지식은 그 저장소의 작업 트리에 있다. 이 절의 함수가 두 뿌리를 가른다.
```
<!-- 인용 끝 -->
