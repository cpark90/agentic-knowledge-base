---
name: odd-check
description: 세션 시작이나 환경 변경 뒤에 실제 조건이 ODD 안인지 CHECKS 명령으로 판정해 이탈을 보고할 때 쓴다.
---

# odd_check — ODD 모니터링 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/odd_check.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

ODD 모니터링 — 실제 조건(COD)을 ODD 문서의 CHECKS 로 판정해 이탈을 보고한다 (노트 3.5절).

## 언제 쓰는가

세션 시작이나 환경 변경 뒤에 실제 조건이 ODD 안인지 CHECKS 명령으로 판정해 이탈을 보고할 때 쓴다.

## 명령

```bash
bazel run //tools:odd_check
bazel run //tools:odd_check -- --out /tmp/odd-check.md
```

## 원본

- 절차: [`docs/method.md` 2. ODD 작성](../../../docs/method.md#2-odd-작성)
- 도구: `tools/odd_check.py` (`bazel run //tools:odd_check`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:odd_check -- [--odd kb/odd/project-odd.yml] [--out report.md]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
