---
id: https://agentic-knowledge-base.dev/id/chunk/fa831b18-16bd-4c86-8fa9-8ac3d941c6f2
type: artifact
level: executable
title_ko: 모듈 머리 r20 (tools/gen_build.py)
title: module head r20 in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9bb41e68-1b5c-4d4c-aee0-32a2899bedf9
---
**모듈 머리** — `tools/gen_build.py` 의 모듈 머리 `r20` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import (EXIT_CONFIG, EXIT_FAIL, NORM_TYPE, ORDERED_KEY, PART_OF_KEY, SPACE_TYPE,  # noqa: E402 — 종료 코드는 chunk2kg 가 kb_lib 에서 가져온 것
                      apply_plane_level_state, load_plane_level_state, norm_item_slugs, parse_chunk)
```
<!-- 인용 끝 -->
