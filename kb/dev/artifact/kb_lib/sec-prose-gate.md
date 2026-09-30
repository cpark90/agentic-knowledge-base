---
id: https://agentic-knowledge-base.dev/id/chunk/cbe79d66-7d81-4b6d-9170-a7dd56984eff
type: artifact
level: executable
title_ko: 절 prose-gate (tools/kb_lib.py)
title: section prose-gate in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/99dbbf72-57fc-4b1b-91bd-ef07be848f6e
composite: {id: https://agentic-knowledge-base.dev/id/composite/99dbbf72-57fc-4b1b-91bd-ef07be848f6e, title_ko: 절 복합체 prose-gate (tools/kb_lib.py), title: section composite prose-gate in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/cbe79d66-7d81-4b6d-9170-a7dd56984eff, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/9a10d17d-c778-4340-b082-b27d4e75e275, https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099], part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211}
---
**절** — `tools/kb_lib.py` 의 절 `prose-gate` 다. 산문 문체 (STYLEGUIDE §0 "산문은 단정 서술형", 유저 결정 2026-09-13)

**정의** — `prose_segments` · `_around` · `check_prose` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 산문 문체 (STYLEGUIDE §0 "산문은 단정 서술형", 유저 결정 2026-09-13) ──────────────────────────
# 판정 가능한 것만 게이트 `prose`(chunk_lint·doccheck)다 — 경어·비격식 종결과 산문의 감탄. 판단이 필요한 것(추측·구어)은
# consistency ⑦ 보고다 (p6-mass-fail-suspects-the-rule: 오탐 0 이 게이트의 조건). 코드·따옴표·주석 안은 산문이 아니므로
# prose_segments 가 먼저 뺀다. 표 셀과 불릿은 산문이다 — 경어체는 어디서든 금지다.
PROSE_GATE = "prose"  # 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다 (축 파일)
# 문장 끝의 경어·비격식 종결 — 뒤에 . ! ? ) " 공백 또는 줄끝. 합쇼체 "…ㅂ니다/습니다"(합니다·됩니다·입니다·있습니다)는
# 받침 ㅂ 음절 + "니다" 로 잡는다 — "습" 도 받침 ㅂ 이다. 그냥 "니다" 로 넓히면 평서형 "아니다"(받침 없음)가 오탐이다 (첫 실행 70건 전부)
_HANGUL_B_FINAL = "".join(chr(0xAC00 + i) for i in range(11172) if i % 28 == 17)  # 종성 ㅂ 인 음절 399자
PROSE_FORBIDDEN_ENDINGS = re.compile(r"(?:[" + _HANGUL_B_FINAL + r"]니다|십시오|세요|해요|예요|이에요|죠|네요|군요|어요|아요)(?=[.!?)\"\s]|$)")
# 산문의 느낌표 — `!=`(부등)·`![`(이미지)는 제외. 코드·따옴표·`<!--` 는 prose_segments 가 이미 뺐다
PROSE_EXCLAMATION = re.compile(r"!(?![=\[])")
# 보고용 — 추측 표현과 구어 후보. `되게`·`진짜`는 정상 용법("…되게 한다", "진짜 결함")이 많아 넣지 않는다
PROSE_HEDGES = re.compile(r"것 같|듯하|듯싶|아닐까|않을까|수도 있|아마도|아마 ")
PROSE_COLLOQUIAL = re.compile(r"근데|그냥|좀|엄청|뭔가|약간")
# 문장 끝의 대리(consistency ⑦ 대시 밀도의 분모) — 둘 중 하나: 마침표 뒤에 공백·줄끝·`|`·`)`·닫는 따옴표(굵게 `**` 는 사이에
# 와도 된다; "4.13절" 처럼 숫자·글자가 이어지면 마침표가 아니다), 또는 마침표 없는 종결 "다" 뒤에 `|`(표 셀)·`)`·닫는 따옴표·줄끝.
# 실측(2026-09-13, 살아 있는 청크 621): "다." 만 세면 209건 > 1.0, 종결 "다" 기반으로 넓혀도 130건 — 명사형 종결("기각."·
# "…시점.")과 "…다 (10.3절)." 의 인용 괄호를 놓쳐 대안 양식("**대안** — X 안. 기각 — Y다 (절).")이 전부 걸렸다(대리의
# 결함, p6-mass-fail-suspects-the-rule). 마침표 종결을 세면 28건이고 대안 양식은 빠진다
PROSE_SENTENCE_END = re.compile(r"(?:다(?=\**\s*(?:[|)\"”」'’]|$))|\.(?=\**(?:[|)\"”」'’\s]|$)))")
# 라벨 대시 — 줄·불릿·번호·표 셀 첫머리에서 종결(`다`·`.`) 없는 짧은 라벨(≤40자; 코드 스팬이 지워져 비어 있어도 된다) 바로
# 뒤의 첫 " — " ("**결론** — …", "- **케이스 저장소** — …", "| 결정 | `d-…` — 결론…", "- 답하는 질문 — …"). 절을 이어 붙인
# 대시가 아니라 구조적 구분자라 대시 밀도의 분자에서 뺀다 — 라벨 대시를 세면 표·불릿 중심 청크가 상위를 차지했다(28건 중 상위
# 전부). 절 끝 "…한다 — " 는 `다` 로 끝나므로 라벨이 아니다
PROSE_LABEL_DASH = re.compile(r"(?:^|\|)[ \t]*(?:[-*+][ \t]+|\d+[.)][ \t]+)?(?:[^—|.\n]{0,40}?[^다\s—|.\n])?[ \t]*—[ \t]")

_MD_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_MD_CODE_SPAN = re.compile(r"(`+)(.+?)\1")
# 따옴표 안 — 같은 줄에서 짝이 맞는 것만 뺀다. 홑따옴표는 영문 소유격·축약(it's)을 피하려고 앞뒤가 영숫자가 아닌 것만 짝으로 본다
_MD_QUOTED = re.compile(r"\"[^\"]*\"|“[^”]*”|「[^」]*」|(?<![A-Za-z0-9])'[^']*'(?![A-Za-z0-9])|(?<![A-Za-z0-9])‘[^’]*’(?![A-Za-z0-9])")
```
<!-- 인용 끝 -->
