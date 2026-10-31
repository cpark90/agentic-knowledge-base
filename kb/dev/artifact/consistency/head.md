---
id: https://agentic-knowledge-base.dev/id/chunk/fa1732a8-9290-48de-8e7f-90f31527d6e6
type: artifact
level: executable
title_ko: 모듈 머리 gate-term (tools/consistency.py)
title: module head gate-term in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6cf102de-daa9-4edc-bd55-b2dab0f902b8
---
**모듈 머리** — `tools/consistency.py` 의 모듈 머리 `gate-term` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import (BODY_FENCE, BODY_SLOT_KEYWORD, BODY_SLOT_SPAN,  # noqa: E402
                      apply_plane_level_state, body_slot_mark, load_plane_level_state, parse_chunk)
import kb_lib  # noqa: E402 — 규약 상수·머리 블록·비율 표기의 단일 정의 위치 (STYLEGUIDE §7)
from kb_lib import (ADDITION_GATE, EMPTY_VALUE_GATE, EXIT_CONFIG, EXIT_OK, LIST_MAX_DEPTH, LIST_MAX_ITEM_CHARS,  # noqa: E402
                    LIST_MAX_ITEMS, LIST_RULES_GATE, LIVE_STATES, PROSE_LABEL_DASH, PROSE_SENTENCE_END,
                    check_addition, check_lists, check_prose, load_waivers, prose_segments, waived)
from gen_norms import CONVENTION_LINE, TABLE_CELL_SEP  # noqa: E402 — 규약 줄과 표 칸 경계의 단일 정의 위치 (⑫ 규칙 6)

GATE_TERM = "term-drift"  # ⑥ 의 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다
# ⑦ 대시 밀도의 라벨 대시 보강 — 줄 가운데의 굵은 라벨("… 기각한다. **대안** — …") 뒤 대시도 구분자다. 굵은 부분이
# "다"·마침표로 끝나면 절이므로 라벨이 아니다. 줄·셀 첫머리의 라벨은 kb_lib.PROSE_LABEL_DASH 가 이미 맡는다
BOLD_LABEL_DASH = re.compile(r"\*\*[^*\n]{0,39}[^*\n다.\s]\*\*[ \t]*—[ \t]")
# ⑫ 문장 구성(결정 p0-sentence-composition, 유저 답 Q104-a) — 규칙 3·4·5·6 의 정규식 대리. 보고이고 게이트가 아니다
COMPOSITION_SYMBOL = re.compile(r"[=+→×]+")       # 규칙 3 — 이어진 기호(`==`·`+=`)는 한 번으로 센다
COMPOSITION_LINK_TARGET = re.compile(r"\]\([^)\s]*\)|<https?://[^>\s]+>|https?://\S+")  # 링크 대상 — 산문이 아니다
COMPOSITION_HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
COMPOSITION_ITEM = re.compile(r"^\s*(?:>\s*)?(?:[-*+]|\d+[.)])\s+")
COMPOSITION_PERIOD = re.compile(r"\.(?=\**(?:[\"”」'’\s]|$))")  # 문장 끝 마침표 — "4.2절" 처럼 글자가 이어지면 아니다
# 규칙 4 — 서술어 종결(평서 "다", 의문 "까", 명령 "라", 청유 "자")이 아닌 한글 음절로 끝나는 문장은 명사형 끝맺음이다
COMPOSITION_PREDICATE_END = set("다까라자")
COMPOSITION_TRAILING = re.compile(r"(?:\s*\([^()]*\)|[\s*\"”」'’])+$")  # 문장 끝의 출처 괄호·굵게·닫는 따옴표
COMPOSITION_CHAIN_BREAK = re.compile(r"[,.;:()\[\]|—]")  # 가운뎃점 연쇄를 끊는 구두점 — 연쇄는 한 구 안에서만 센다
COMPOSITION_ENUM_PAREN = re.compile(r"^\s*(?:[a-zA-Z0-9]{1,2}|[가-하])\s*$")  # "(a)"·"(1)"·"(가)" — 번호이지 괄호 삽입이 아니다
COMPOSITION_GLOSS_PAREN = re.compile(r"^[^가-힣]{1,40}$")  # "정제 수준(refinement level)" — 규칙 8 의 영문 병기다
LIVE = set(LIVE_STATES)  # 게이트 chunk_lint 와 같은 대상 집합 (kb_lib 단일 정의 위치)
_PLACEMENT_RE_CACHE: dict[str, re.Pattern] = {}  # ⑪ 자리 후보 — 표지 낱말별 정규식 캐시
```
<!-- 인용 끝 -->
