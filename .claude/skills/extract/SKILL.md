---
name: extract
description: 소스 파일을 고친 뒤 `artifact` plane 의 함수·절·파일 청크를 다시 추출하고 등록부의 개명·신설·삭제를 맞출 때 쓴다.
---

# extract — 코드 → 청크 추출기 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/extract.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

코드 → 청크 추출기 — 소스 파일 하나에서 `artifact` plane 의 청크 트리를 생성한다 (p7-code-extraction-direction).

## 언제 쓰는가

소스 파일을 고친 뒤 `artifact` plane 의 함수·절·파일 청크를 다시 추출하고 등록부의 개명·신설·삭제를 맞출 때 쓴다.

## 명령

```bash
bazel run //tools:extract -- tools/kb_lib.py
bazel test //:extract_drift_test
python3 tools/gen_build.py --root . && bazel test //...
```

## 원본

- 절차: [`docs/method.md` 3. 청크 저작](../../../docs/method.md#3-청크-저작)
- 도구: `tools/extract.py` (`bazel run //tools:extract`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check] [--residency <defs/kb.bzl>]
루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
--residency 는 EXTRACTED_SOURCES 리터럴의 원본 — 없으면 <루트>/defs/kb.bzl.
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
