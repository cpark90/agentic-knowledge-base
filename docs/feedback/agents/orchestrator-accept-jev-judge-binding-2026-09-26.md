---
from: orchestrator
kind: notice
status: open
ref: handoff/jev-judge-binding-2026-09-26.md
targets: [kb/dev/decision/p8-judge-calibration-binding/, kb/dev/decision/p8-judge-question-form/, tools/judge.py, tools/chunk_lint.py, kb/ontology/profile/development/, kb/odd/project-odd.yml, kg/base-kg.ttl, docs/method.md, docs/rules.md, docs/tools.md]
---

# 인수 기록 — `jev-judge-binding-2026-09-26` (2026-09-29)

승인 항목 [`jev-judge-binding-2026-09-26`](../jev-judge-binding-2026-09-26.md)의 반영 계획 다섯 중 넷을 수행했다. 다섯째(3지표 측정)는 자격이 없어 **절차만** 섰다.

| 계획 | 수행 |
|---|---|
| 1 orchestrator — 결정 개정 | `p8-judge-calibration-binding`이 `p8-judge-question-form`을 `supersedes`(옛 결정 deprecated). 규칙 ①~⑤ 표, 구간별 측정 전 자동 적용 구간 없음, 로그 필수 필드. 출처 개체 `id:doc-jev-system-one`(git:b23e35a) |
| 2 developer — `judge.py` | `bazel run` 전용. 프로파일 shape(`judge-question`·`-threshold`·`-calibration`·`-question-set` 온톨로지 + `judge-question-shapes`)에서 질문·척도·임계를 읽는다. 질문 셋 등록 — `labelRepresentsBody`(score)·`bodyHasOneClaim`(noul)·`commentLabelChoice`(choice 7): 총람 "게이트 밖" 규약 둘이 이제 보고 기구를 가진다. 외부 호출은 `call_service()` 하나, 자격은 환경 변수 셋, 없으면 호출 없이 `EXIT_CONFIG`. 오프라인 `--fixture`. choice > 255는 도구·shape 둘 다 거부. `본문:` = `해당 없음`(규칙 ④), 라벨 `thought (non-blocking)`(차단 사유가 아니다) |
| 3 developer — 게이트 | `judge-log`(`chunk_lint` 확장): 표 헤더·필수 여섯·확신도 0~1·sha256 64자·ISO UTC·처리 어휘. **로그 0건이면 PASS**(존재 요구는 이 게이트의 몫이 아니다). 음성 시험 9건 |
| 4 developer — ODD | `id:cond-judge-service`(환경 조건, 등급 B, 비활성 모듈 `judge_service_binding`) — **조건부 함의**로 적었다: 자격이 하나라도 설정되면 셋이 다 있어야 한다. 항구적 `out`이면 세션마다 빨간 모니터가 되어 읽히지 않는다. orchestrator가 가정 `id:asm-judge-service`를 세웠다(로그·주석의 `assumes` 대상 — 자격이 빠지면 지난 판정이 suspect로 전파된다) |
| 5 vnv — 3지표 | **절차만** — 구간당 20건, 조인 키 = 입력 지문, 구간별 정확도·판별력(미끼 필요)·캘리브레이션(구간 평균 확신도 − 실측 정확도). 스위치는 `agt:bandAccuracyMeasured`·`agt:calibratedFor` |

판정 로그를 저장소에 남기지 않았다 — 오프라인 고정물의 가짜 응답을 append-only 관측으로 굳히면 3지표 표본이 오염된다. 첫 로그는 실제 호출로 남긴다.

## hci가 "확인 못 한 것"으로 남긴 것 → 유저에게 되돌릴 것

- **API 접근 수단·비용 승인.** 자격(엔드포인트·키·모델 식별자)이 없어 측정을 시작할 수 없다. 공개 문서가 요청·응답 필드 이름을 밝히지 않아 `call_service()`의 형식은 `미확정`이다 — 자격이 오면 그 함수와 고정물 키만 고친다.
- 구간당 표본 수는 결정이 20으로 정했다(hci 셈 60건과 같다).

## hci에 전달

원장에 "판정자 실물 = 게이트 밖 `judge`, 로그 게이트 `judge-log`, 3지표 측정은 자격 대기(2026-09-29)" 한 줄. 유저 질문 하나 — 판정 서비스 자격 제공·비용 승인. 재판정 대상 없음.
