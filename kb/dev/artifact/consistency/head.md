---
id: https://agentic-knowledge-base.dev/id/chunk/fa1732a8-9290-48de-8e7f-90f31527d6e6
type: artifact
level: executable
title_ko: 모듈 머리 gate-term (tools/consistency.py)
title: module head gate-term in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9d3f4240-66d0-4dfd-9124-9499e65cb57a, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97, https://agentic-knowledge-base.dev/id/chunk/5287133e-f7a3-4913-8aaf-062647cf5491]
part_of: https://agentic-knowledge-base.dev/id/composite/6cf102de-daa9-4edc-bd55-b2dab0f902b8
---
**모듈 머리** — `tools/consistency.py` 의 모듈 머리 `gate-term` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import (BODY_FENCE, BODY_SLOT_KEYWORD, BODY_SLOT_MARKERS, BODY_SLOT_QUALIFIER_MAX, BODY_SLOT_SPAN,  # noqa: E402
                      _body_slot_at_field_head, apply_plane_level_state, load_plane_level_state, parse_chunk)
import kb_lib  # noqa: E402 — 규약 상수·머리 블록·비율 표기의 단일 정의처 (STYLEGUIDE §7)
from kb_lib import (ADDITION_GATE, EMPTY_VALUE_GATE, EXIT_CONFIG, EXIT_OK, LIST_MAX_DEPTH, LIST_MAX_ITEM_CHARS,  # noqa: E402
                    LIST_MAX_ITEMS, LIST_RULES_GATE, LIVE_STATES, PROSE_LABEL_DASH, PROSE_SENTENCE_END,
                    check_addition, check_lists, check_prose, load_waivers, prose_segments, waived)

GATE_TERM = "term-drift"  # ⑥ 의 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다
LIVE = set(LIVE_STATES)  # 게이트 chunk_lint 와 같은 대상 집합 (kb_lib 단일 정의처)
_PLACEMENT_RE_CACHE: dict[str, re.Pattern] = {}  # ⑪ 자리 후보 — 표지 낱말별 정규식 캐시
```
<!-- 인용 끝 -->
