---
id: https://agentic-knowledge-base.dev/id/chunk/06a17fc9-3add-4cb8-9ebd-9c036e43869b
type: artifact
level: executable
title_ko: 모듈 머리 tag (tools/extract.py)
title: module head tag in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
part_of: https://agentic-knowledge-base.dev/id/composite/57a845e1-da27-4d9d-b5b0-b25148ccece7
composite: {id: https://agentic-knowledge-base.dev/id/composite/57a845e1-da27-4d9d-b5b0-b25148ccece7, title_ko: 모듈 머리 복합체 tag (tools/extract.py), title: section composite tag in tools/extract.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/06a17fc9-3add-4cb8-9ebd-9c036e43869b, https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b], part_of: https://agentic-knowledge-base.dev/id/composite/99abae51-6823-4ed8-9bfe-4255801d4681}
---
**모듈 머리** — `tools/extract.py` 의 모듈 머리 `tag` 다. 모듈 머리

**정의** — `ExtractError` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
except ImportError:
    import kb_lib

TAG = kb_lib.EXTRACT_GATE
DRIFT_TAG = kb_lib.EXTRACT_DRIFT_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
CHUNK_IRI = "https://agentic-knowledge-base.dev/id/chunk/"
COMPOSITE_IRI = "https://agentic-knowledge-base.dev/id/composite/"
DEFAULT_ASSUMES = "https://agentic-knowledge-base.dev/id/asm-chunk-conventions"
MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — defs/kb.bzl · gen_build 와 같은 수
_NAME_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
```
<!-- 인용 끝 -->
