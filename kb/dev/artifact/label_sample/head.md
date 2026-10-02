---
id: https://agentic-knowledge-base.dev/id/chunk/0642de89-2ca0-4a05-b091-a2adf00d4e0e
type: artifact
level: executable
title_ko: 모듈 머리 live (tools/label_sample.py)
title: module head live in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4, https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
part_of: https://agentic-knowledge-base.dev/id/composite/06cd565d-e749-42fe-88da-1a56fd71a2a5
---
**모듈 머리** — `tools/label_sample.py` 의 모듈 머리 `live` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록)·판정자 프로파일 질의·지문의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402

LIVE = {"draft", "stable", "suspect"}
QUESTION = "labelRepresentsBody"  # 이 실험이 언제나 묻는 질문 — 프로파일의 지역명(judge-question-set-ontology.ttl)
```
<!-- 인용 끝 -->
