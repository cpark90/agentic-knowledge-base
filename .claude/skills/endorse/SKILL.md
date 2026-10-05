---
name: endorse
description: 쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.
---

# endorse — 인수 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/endorse.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

인수 — 쓰기 권한이 있는 역할이 검토한 청크에 OKF verified 를 붙인다 (writer 검사의 해소 수단).

## 언제 쓰는가

쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.

## 명령

```bash
bazel run //tools:endorse -- --by orchestrator/<모델> --at <ISO 8601> <청크 파일…>
```

## 원본

- 절차: [`docs/method.md#13-저작-흐름과-완료`](../../../docs/method.md#13-저작-흐름과-완료)
- 도구: `tools/endorse.py` (`bazel run //tools:endorse`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:endorse -- --by orchestrator/claude-fable-5 --at 2026-09-11T10:00:00+09:00 <청크 파일...>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
