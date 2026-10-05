---
id: https://agentic-knowledge-base.dev/id/chunk/0149c880-a2a1-45d1-bad4-6d54b7932fc3
type: artifact
level: executable
title_ko: 모듈 머리 allowed-ttl-suffixes (tools/chunk_lint.py)
title: module head allowed-ttl-suffixes in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f1d91f37-d353-405b-bd98-41132f8d5390
---
**모듈 머리** — `tools/chunk_lint.py` 의 모듈 머리 `allowed-ttl-suffixes` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
ALLOWED_TTL_SUFFIXES = kb_lib.ALLOWED_TTL_SUFFIXES
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건
CHUNK = kb_lib.CHUNK_GATE                        # 본문 토큰 상한 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
PROSE = kb_lib.PROSE_GATE                        # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
DECISION_ROLE = kb_lib.DECISION_ROLE_GATE        # 결정 역할 표지 게이트 id (STYLEGUIDE §4)
ADDITION = kb_lib.ADDITION_GATE                  # 첨가 게이트 id — 메타 문장·채움 문구 (STYLEGUIDE §0, consistency ⑧)
EMPTY_VALUE = kb_lib.EMPTY_VALUE_GATE            # 빈 값 게이트 id — 세 빈 값 밖의 표기 (STYLEGUIDE §0, consistency ⑧)
LIST_RULES = kb_lib.LIST_RULES_GATE              # 목록 게이트 id — 목록 규칙 다섯 (STYLEGUIDE §0, consistency ⑨)
BLOCKING_COMMENT = kb_lib.BLOCKING_COMMENT_GATE  # 주석 게이트 id — 해소되지 않은 issue (blocking) (STYLEGUIDE §4, p7-commentary-form)
JUDGE_LOG = kb_lib.JUDGE_LOG_GATE                # 판정 로그 게이트 id — 로그의 형식·필수 필드 (p8-judge-calibration-binding)
SUMMARY_SUPPORT = kb_lib.SUMMARY_SUPPORT_GATE    # 요약 지지 참조 게이트 id (judge-without-service-2026-09-30 기계 환원 ①)
NAMING = kb_lib.NAMING_GATE                      # TTL 파일 접미사 규약 게이트 id (0.2절)

MAX_BODY_TOKENS = kb_lib.MAX_BODY_TOKENS  # 기본 1,092 토큰 (42×26). plane 별 상한의 정의처는 kb_lib.BODY_TOKEN_LIMITS 다

_FM_FIELD = re.compile(r"^(type|status):\s*(\S+)")  # 역할 표지 판정에 필요한 frontmatter 키 둘 — 전체 파싱은 chunk2kg 의 몫
_FM_GENERATED_BY = re.compile(r"^generated:\s*\{[^}]*?\bby:\s*([^,}\s]+)")  # 생성자 — 판정 로그를 고르는 열쇠 (process:judge)
_CELL_CODE = re.compile(r"^`(.*)`$")  # 표 셀의 코드 스팬 — 값은 그 안이다
```
<!-- 인용 끝 -->
