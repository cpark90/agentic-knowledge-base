---
id: https://agentic-knowledge-base.dev/id/chunk/b4059229-f009-4ea7-b6f0-9b5fdb9a936f
type: artifact
level: executable
title_ko: 절 judge-generator (tools/kb_lib.py)
title: section judge-generator in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
composite: {id: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821, title_ko: 절 복합체 judge-generator (tools/kb_lib.py), title: section composite judge-generator in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/b4059229-f009-4ea7-b6f0-9b5fdb9a936f, https://agentic-knowledge-base.dev/id/chunk/48ed45d6-a852-4def-9baa-eee654691bc7, https://agentic-knowledge-base.dev/id/chunk/2cabfcc4-8242-47a2-9710-9ed682ab9f2b, https://agentic-knowledge-base.dev/id/chunk/00a89f1d-2167-43fb-9e95-4a70385078ae], part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893}
---
**절** — `tools/kb_lib.py` 의 절 `judge-generator` 다. 판정자 (게이트 밖 도구 tools/judge.py — 결정 p8-judge-session-agreement, 노트 8.14절)

**정의** — `label_fingerprint` · `judge_load_profile` · `judge_questions` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 판정자 (게이트 밖 도구 tools/judge.py — 결정 p8-judge-session-agreement, 노트 8.14절) ────────────────────────
# 판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다(유저 답 2026-09-30,
# 결정 p8-judge-session-agreement가 옛 결정 p8-judge-calibration-binding을 대체한다). 판정은 `bazel run` 전용이고 세션 판정자의 응답은
# `--responses` 로 오프라인 입력된다 — 네트워크 호출이 없으므로 `bazel test` 의 밀폐성은 애초에 걸리지 않지만, 판정
# 자체가 세션마다 달라질 수 있어 여전히 게이트 밖이다. 게이트는 **판정 로그의 형식과 필수 필드만** 본다(게이트 id
# judge-log, chunk_lint). 로그의 자리는 V&V KB 의 memory plane 실체, 곧 실행 기록 디렉토리다(vv_run 과 같은 곳,
# 파일명 접두로 갈린다) — 판정은 노트 8.20절 다섯 V&V 하위 역할 중 judge 의 실행이고 kb/dev/memory 는 개발 KB 쪽
# 관측의 자리다. 결과 주석은 annotation plane 실체(kb/vv/verdict)에 논평 형식(p7-commentary-form)으로 나간다.
JUDGE_GENERATOR = "process:judge"         # 판정 로그·결과 주석의 generated.by — 역할이 아니라 writer 검사 밖이다
JUDGE_LOG_DIR = VV_RUN_DIR                # 판정 로그의 자리 = 실행 기록 디렉토리 (append-only, r-026)
JUDGE_LOG_PREFIX = "judge-"               # 파일명 judge-<UTC>.md — vv_run 의 run-<UTC>.md 와 한 디렉토리에서 갈린다
JUDGE_VERDICT_DIR = KB_VV + "/verdict"    # 결과 주석의 자리 = 판정 주석 (annotation plane 실체)
# 판정 로그 본문의 판정 표 — 열이 곧 필수 필드다. 열 하나를 지우면 헤더가 달라져 게이트가 거부한다.
# `일치` 는 필수 여섯 밖의 읽기 열이다 — 같은 (질문·입력 지문)을 둘 이상의 세션 판정자가 답했을 때만 뜻을 갖고,
# 단독 응답이면 `해당 없음`이다(2026-09-30, 판정자 둘의 일치가 새 임계의 재료 — 결정 p8-judge-session-agreement)
JUDGE_LOG_TABLE_HEADER = "| 질문 id | 대상 | 값 | 확신도 | 판정자 식별자 | 입력 지문 | 시각 | 처리 | 일치 |"
JUDGE_LOG_FIELDS = ("질문 id", "값", "확신도", "판정자 식별자", "입력 지문", "시각")  # 결정이 필수로 정한 여섯 — 대상·처리·일치는 읽기 위한 열이다
JUDGE_FORMS = ("noul", "choice", "score")  # 질문의 형 셋 — judge-question-shapes 의 sh:in 과 같은 집합
JUDGE_CHOICE_MAX = 255                     # 선택 집합의 상한 (규칙 ③) — 넘으면 점수 → 선택 2단계다
JUDGE_ROUTES = ("자동 적용", "사람 확인 큐", "판정 보류")  # 임계가 가르는 세 처리 (옛 p8-judge-question-form 의 표)
JUDGE_QUEUE = JUDGE_ROUTES[1]              # 구간별 정확도를 재기 전의 유일한 처리 (규칙 ②) — 세션 판정자의 확신도는 자기 보고라 지금은 전부 이 처리다
JUDGE_AGREEMENT = ("일치", "불일치", "해당 없음")  # `일치` 열의 닫힌 어휘 — 세션 판정자 둘 이상이 같은 (질문·지문)에 답했을 때만 일치·불일치, 단독이면 해당 없음
JUDGE_THRESHOLDS = "judgeThresholds"       # 임계 셋 개체의 지역명 (judge-threshold-ontology) — 도구가 값을 여기서 읽는다
# 판정 로그·결과 주석이 `assumes:` 로 참조하는 가정 (kg/base-kg.ttl). 청크 규약 하나뿐이다 — 판정 서비스 가정
# (`asm-judge-service`)은 서비스 도입 자체가 되돌려져 2026-09-30에 뺐다(handoff/judge-without-service-2026-09-30.md)
JUDGE_ASSUMPTIONS = ("asm-chunk-conventions",)
JUDGE_FINGERPRINT = re.compile(r"^[0-9a-f]{64}$")           # 입력 지문 = 입력 바이트의 sha256
JUDGE_CONFIDENCE = re.compile(r"^(?:0(?:\.\d+)?|1(?:\.0+)?)$")  # 확신도 = 0 이상 1 이하의 십진 표기




JUDGE_PROFILE_DIR = "kb/ontology/profile/development"      # 질문·척도·임계 온톨로지 모듈 디렉토리 — 단일 정의처
JUDGE_QUESTION_SHAPES = "kb/ontology/shapes/judge-question-shapes.ttl"
```
<!-- 인용 끝 -->
