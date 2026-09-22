---
name: gendoc
description: 생성기를 고친 뒤 생성 문서의 머리 블록·표·목차·링크·비율 표기가 규약 G1~G18 안인지 게이트와 같은 방식으로 검사할 때 쓴다.
---

# gendoc — 생성 문서 게이트 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/tools.md` · `tools/gendoc.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

생성 문서 게이트 — 에이전트가 만드는 마크다운의 가독성·건전성 규약 G1~G18 (유저 지시 2026-09-21).

## 언제 쓰는가

생성기를 고친 뒤 생성 문서의 머리 블록·표·목차·링크·비율 표기가 규약 G1~G18 안인지 게이트와 같은 방식으로 검사할 때 쓴다.

## 명령

```bash
bazel test //:gendoc_test
bazel run //tools:gendoc -- bazel-bin/kg/metrics.md bazel-bin/kb/dev/index.md
```

## 원본

- 절차: [`docs/tools.md` 게이트 총람 — 이 문서가 원본이다](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)
- 도구: `tools/gendoc.py` (`bazel run //tools:gendoc`) — 사용법은 docstring 이 원본이다

```text
gendoc.py [--root DIR] <생성 문서 ...>
bazel test //:gendoc_test
루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
