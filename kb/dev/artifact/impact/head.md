---
id: https://agentic-knowledge-base.dev/id/chunk/e3651d6a-824c-47cd-bd83-2db367e84196
type: artifact
level: executable
title_ko: 모듈 머리 r15 (tools/impact.py)
title: module head r15 in tools/impact.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-impact}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/05cabe0e-10b0-4e02-81b1-8f5154a94fcc]
part_of: https://agentic-knowledge-base.dev/id/composite/711360b7-62ed-4bfc-9088-27974668e958
---
**모듈 머리** — `tools/impact.py` 의 모듈 머리 `r15` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)의 단일 정의처
```
<!-- 인용 끝 -->
