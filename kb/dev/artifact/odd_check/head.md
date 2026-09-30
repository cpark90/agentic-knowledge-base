---
id: https://agentic-knowledge-base.dev/id/chunk/c64a0d92-d978-4b1c-b12e-c03e8e8d1ef9
type: artifact
level: executable
title_ko: 모듈 머리 states (tools/odd_check.py)
title: module head states in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/8e83391e-5fd2-499b-881c-37e6f9cb60f1, https://agentic-knowledge-base.dev/id/chunk/2df65a05-0d25-4b3c-aae9-8da6dd82218f]
part_of: https://agentic-knowledge-base.dev/id/composite/860d7967-4c4a-48c3-846c-a6f932e81933
---
**모듈 머리** — `tools/odd_check.py` 의 모듈 머리 `states` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)의 단일 정의처

STATES = ("in", "out", "unverified")
ID_BASE = "https://agentic-knowledge-base.dev/id/"
```
<!-- 인용 끝 -->
