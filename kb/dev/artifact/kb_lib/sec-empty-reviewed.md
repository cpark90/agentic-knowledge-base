---
id: https://agentic-knowledge-base.dev/id/chunk/d9a18587-01e9-4d06-8413-80ea98ce260b
type: artifact
level: executable
title_ko: 절 empty-reviewed (tools/kb_lib.py)
title: section empty-reviewed in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/2a5c7bf9-6e66-4ad7-80de-c8a96b80bb4a
composite: {id: https://agentic-knowledge-base.dev/id/composite/2a5c7bf9-6e66-4ad7-80de-c8a96b80bb4a, title_ko: 절 복합체 empty-reviewed (tools/kb_lib.py), title: section composite empty-reviewed in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d9a18587-01e9-4d06-8413-80ea98ce260b, https://agentic-knowledge-base.dev/id/chunk/764328d8-e7e9-4fdf-9e87-e04f59d61a65, https://agentic-knowledge-base.dev/id/chunk/cd6718e1-2437-43a9-b7a2-174aced3b0e1], part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211}
---
**절** — `tools/kb_lib.py` 의 절 `empty-reviewed` 다. 빈 값·첨가·목록 (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-three-empty-values)

**정의** — `check_addition` · `check_lists` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 빈 값·첨가·목록 (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-three-empty-values) ─────
# 세 빈 값은 서로 다른 사실이다. 하나로 합치면 검토하고 비운 자리·해당하지 않는 자리·답을 기다리는 자리가 같은 모양이
# 되어 감사가 셋을 가르지 못한다. 생성 문서 규약의 NONE_MARK 는 이 셋의 첫 값이고 정의처는 여기 하나다 (STYLEGUIDE §7).
EMPTY_REVIEWED = "없음"            # 찾아봤고 없다 — 다음 행동이 없다
EMPTY_NOT_APPLICABLE = "해당 없음"  # 이 항목에는 적용되지 않는다 — 다음 행동이 없다
EMPTY_UNDECIDED = "미확정"          # 아직 모른다 — 미결로 집계되고 답이 오면 채운다
EMPTY_VALUE = (EMPTY_REVIEWED, EMPTY_NOT_APPLICABLE, EMPTY_UNDECIDED)
# 세 값 밖의 빈 값 표기 — 보고용이다. `미정의`(undefined)는 빈 값이 아니라 낱말이라 뺀다. 따옴표·코드 스팬 안은
# prose_segments 가 이미 뺐으므로 규칙 자신을 인용한 문장(결정 p4-three-empty-values)은 잡히지 않는다
EMPTY_VALUE_REJECTED = re.compile(r"(?<![A-Za-z])[Nn]/[Aa](?![A-Za-z])|(?<![A-Za-z])TBD(?![A-Za-z])|미정(?!의)")
EMPTY_DASH_CELL = re.compile(r"[-–—]")  # 단독 대시로 비운 표 셀 — 헤더·구분 행 뒤의 셀에만 적용한다 (G14 와 같은 규칙)
# 메타 문장 — 슬롯의 질문에 답하지 않고 문서의 구조를 안내하는 문장. 좁게 시작한다: 오탐이 하나 나오면 보고 전체가
# 무시되기 때문이다 (p6-mass-fail-suspects-the-rule). "요약하면"·"참고로" 같은 접속 부사는 정상 용법과 가르기
# 어려워 넣지 않는다. 여기 있는 넷은 뒤따르는 내용을 예고할 뿐 자기 자신이 주장이 아니다
PROSE_META = re.compile(r"다음과 같다|(?:이|아래) (?:절|장|문서|청크|표)에서는|아래에서 (?:설명한다|다룬다|기술한다)|(?:앞서|앞에서) (?:말했|언급했|설명했)")
# 채움 문구 — 빈 값을 피하려고 슬롯을 때우는 문장. 세 빈 값과 다르다: `없음` 은 규칙이 요구하는 값이고 채움은 값이
# 아닌 문장이다. 실측 위반 0 이므로 제안 9.4절의 예시 형태를 그대로 옮긴다
PROSE_FILLER = re.compile(r"특이사항(?:은)? 없|일반적[인이] (?:방식|방법)을? (?:따른다|쓴다)|추후 (?:결정한다|정한다|보완한다|채운다)")
# 목록 규칙 (4.3절) — 상한 셋과 항목 정규식. 순서 목록의 번호는 모든 항목이 `1.` 이고 번호는 렌더러가 매긴다
LIST_MAX_ITEMS = 9
LIST_MAX_DEPTH = 2
# 항목 길이는 소스 줄이 아니라 글자로 잰다 — 이 저장소는 산문을 110~120자에서 손으로 접어 소스 줄과 렌더 줄이 다르다.
# 240 = 120자 × 2줄 (STYLEGUIDE §0, 결정 p4-slot-answers-one-question; 유저 승인 2026-09-22)
LIST_MAX_ITEM_CHARS = 240
MD_LIST_ITEM = re.compile(r"^(\s*)(?:[-*+]|(\d+)[.)])(?:\s+|$)")
# 게이트 id — 보고(consistency ⑧·⑨)와 게이트(chunk_lint)가 같은 이름을 쓴다. docs/waivers.md 가 이 이름으로 면제를 선언하고
# (축 `파일`), 면제된 항목은 집계에서 빼되 목록에는 남긴다. 축을 셋으로 가르는 까닭은 규약의 원본이 둘이기 때문이다 —
# 메타 문장·채움은 p4-slot-answers-one-question, 빈 값 표기는 p4-three-empty-values, 목록 규칙은 두 결정의 4.3절이다
ADDITION_GATE = "addition"        # ⑧ 메타 문장·채움 문구 — FAIL [addition]
EMPTY_VALUE_GATE = "empty-value"  # ⑧ 세 빈 값 밖의 표기 — FAIL [empty-value]
LIST_RULES_GATE = "list-rules"    # ⑨ 목록 규칙 — FAIL [list-rules]
# 살아 있는 청크의 status. 보고와 게이트의 대상 집합이 같아야 수치가 갈리지 않는다 — invalidated·deprecated 는
# 고칠 대상이 아니라 기록이므로 둘 다 제외한다 (나머지 둘은 chunk2kg.STATES)
LIVE_STATES = ("draft", "stable", "suspect")
```
<!-- 인용 끝 -->
