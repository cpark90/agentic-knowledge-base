---
name: endorse
description: 쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.
---

# endorse — 인수

> 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring과 `kb_lib.SKILLS` (`tools/gen_skills.py`). 검사: `//:skills_drift_test`

인수 — 쓰기 권한이 있는 역할이 검토한 청크에 OKF verified 를 붙인다 (writer 검사의 해소 수단).

## 언제 쓰는가

쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.

## 명령

```bash
bazel run //tools:endorse -- --by orchestrator/<모델> --at <ISO 8601> <청크 파일…>
```

## 원본

- 절차: [`docs/method.md` 13. 저작 흐름과 완료](../../../docs/method.md#13-저작-흐름과-완료)
- 도구: `tools/endorse.py` (`bazel run //tools:endorse`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:endorse -- --by orchestrator/claude-fable-5 --at 2026-09-11T10:00:00+09:00 <청크 파일...>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
