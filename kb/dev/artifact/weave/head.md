---
id: https://agentic-knowledge-base.dev/id/chunk/b69488a2-ddf2-4c5d-b093-be38c4f5a853
type: artifact
level: executable
title_ko: 모듈 머리 prov (tools/weave.py)
title: module head prov in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/c0b7f63a-353e-4fdf-9389-961b6f3e130c, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/50eac9df-d01a-488f-8254-02ba61b00bf0
---
**모듈 머리** — `tools/weave.py` 의 모듈 머리 `prov` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import EARS_PATTERNS, apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402 — frontmatter 파서와 값 어휘의 단일 정의처

AGT, ID = kb_lib.AGT, kb_lib.ID
PROV = Namespace("http://www.w3.org/ns/prov#")
EXIT_OK, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG
TAG = kb_lib.WEAVE_TAG
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]  # metrics.py 와 같은 순서 (CQ19 정의)
PATTERN_VALUE = {URIRef(str(AGT) + v.split(":")[1]): k for k, v in EARS_PATTERNS.items()}  # agt:eventDriven → event-driven
```
<!-- 인용 끝 -->
