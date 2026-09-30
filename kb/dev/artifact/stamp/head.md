---
id: https://agentic-knowledge-base.dev/id/chunk/fe9a3f4c-a455-444c-b612-4f93c3897066
type: artifact
level: executable
title_ko: 모듈 머리 tag (tools/stamp.py)
title: module head tag in tools/stamp.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-stamp}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:27:50Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/4ec4de00-ea81-4ed0-abf7-40beedc25e38]
part_of: https://agentic-knowledge-base.dev/id/composite/39d9c5d9-3e2f-4e3b-9f05-84c7476fa96b
---
**모듈 머리** — `tools/stamp.py` 의 모듈 머리 `tag` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.extract import dump_registry, load_registry
except ImportError:
    import kb_lib
    from extract import dump_registry, load_registry

TAG = kb_lib.STAMP_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
```
<!-- 인용 끝 -->
