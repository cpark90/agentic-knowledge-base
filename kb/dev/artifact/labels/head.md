---
id: https://agentic-knowledge-base.dev/id/chunk/019a25f2-901b-47ff-94e4-2449c78f7e2b
type: artifact
level: executable
title_ko: 모듈 머리 r16 (tools/labels.py)
title: module head r16 in tools/labels.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-labels}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f367e186-3a1a-4660-aeb4-7473d4b28b2a
---
**모듈 머리** — `tools/labels.py` 의 모듈 머리 `r16` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))  # runfiles 안에서 같은 디렉토리의 chunk2kg를 찾는다
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402
```
<!-- 인용 끝 -->
