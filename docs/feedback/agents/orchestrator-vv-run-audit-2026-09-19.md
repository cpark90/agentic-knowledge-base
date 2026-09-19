---
from: orchestrator
kind: notice
status: open
targets: [tools/vv_run.py, tools/weave.py, tools/kb_lib.py, tools/gen_build.py, kb/vv/run/, kg/BUILD.bazel, docs/roadmap.md, docs/tools.md, docs/method.md, docs/rules.md]
---

# 7단계 실행기와 8단계 첫 형태 — `vv_run`과 감사 보고서 `//kg:audit` (2026-09-19)

유저 "계속해서 진행해줘"에 따라 V&V 순환을 처음 닫았다. 케이스에 적힌 실행 명령을 실제로 돌려 실행 기록을 남기는 executor와, 그 기록·그래프만으로 생성되는 감사 보고서다.

- **`vv_run`**(developer, `bazel run //tools:vv_run -- [--record] [--case <슬러그>…]`): 케이스(`kb/vv/case/*.md`) 본문의 `**실행 명령**`을 `;`·`&&`로 나눠 허용 목록(`bazel test`·`bazel build`·`bazel query`·`gen_build --check`)의 읽기 전용 검증기만 실행하고, 임시 파일(`/tmp/vv-*`) 자극과 `bazel run`은 SKIP으로 적는다. 판정은 실행한 명령의 종료 코드로만 한다(pass·fail·skip). SKIP은 PASS가 아니다(총람 실패 종류 3). 종료 코드 fail 1 · pass 0 · skip만 3.
- **실행 기록**(`kb/vv/run/run-<UTC>.md`, memory·concrete, append-only, `generated.by: process:vv_run`): `assume_check --record`의 관측과 같은 형식이다. 첫 기록 `run-20260919T062548Z.md` — 케이스 8 · 명령 14 중 실행 12 · 건너뜀 2 · pass 8 · fail 0, 리비전 `6ef2ef5`(워킹트리 변경 있음). 도구가 카탈로그의 executor 하위 역할을 맡는 첫 형태라 writer 검사 밖이다. `gen_build`의 `VV_PKGS`에 `run → memory`.
- **첫 기록을 한 번 재생성했다**: 06:16Z 기록은 템플릿 결함(산문에 영어 낱말, 테스트·캐시 수 누락)이 있는 미커밋 파일이라 지우고 06:25Z에 다시 만들었다. append-only는 **첫 커밋 기록부터** 적용한다 — 커밋된 기록은 고치지도 지우지도 않는다.
- **`weave --kind audit`** → `bazel build //kg:audit` → `bazel-bin/kg/audit.md`: 입력은 그래프 union과 관측 본문(`kb/vv/run/`·`kb/dev/memory/`)뿐이다(요구 `audit-self-sufficiency`, 체계 밖 정보 0 — 리비전도 실행 기록에서 읽는다). 절: 검증 현황(검증 대응물 있는 요구 10/33, verifies 대상 결정 8/197, 사슬 8, 기준 없는 verifies 0) · 최근 실행 · 가정(2 valid) · 추적 매트릭스(TIM 15칸 중 6, 허용표 밖 0) · 검증 표시(human 10 · orchestrator 201 · process 60 · 미검증 413, 검증 뒤 수정 0) · 링크 근거(Link 541, 증거 없음 0, 복원 0%) · 자족성 선언. TIM 15칸 정의는 `kb_lib.TIM_CELLS`로 옮겨 `metrics`와 공유한다.
- **skill**: `vv_run`·`weave`가 `kb_lib.SKILLS`에 올라 `.claude/skills/vv-run`·`weave`가 생성됐다(14개). `assume_check` 생성자 문자열은 `kb_lib.ASSUME_CHECK_GENERATOR`로 통합.
- **문서**: 로드맵 7단계(실행 기록 있음)·8단계(첫 형태)·"다음 산출" 7·8 추가, `tools.md`(활용 첫 형태 9, `vv_run` 절, V&V 층 `run`·`vv_report` 행, 배선), `method.md` §9 감사 보고서 행·§11, `rules.md` 접두 표(실행 기록 = memory 청크). `competency-questions.md`의 앵커를 `활용-첫-형태-9`로.
- 남긴 것: 임시 파일 자극의 자동 생성과 기대 문구 대조(지금은 종료 코드만), 시나리오·검증기·판정 주석 항목, V&V 프로파일·`defect`, 검증 대응물 부재 게이트, 복원 파이프라인(`link` 후보 → 확정 비율), 거짓 빈 칸 판정, 6단계 첫 산출.

## hci에 전달
- 원장에 "7단계 실행기·8단계 첫 형태(2026-09-19)" 한 줄. 재판정 대상 없음.
- `kb/vv/run/`의 기록은 `process:vv_run` 생성이라 인수(endorse)가 필요 없다. 커밋 뒤부터 append-only다 — refresh로 지우지 않는다.

## 답
(hci가 채움)
