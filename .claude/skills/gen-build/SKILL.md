---
name: gen-build
description: 청크를 추가·삭제하거나 frontmatter 링크(refines·serves·supersedes·verifies)를 고친 뒤 BUILD 를 재생성하고 드리프트를 검사할 때 쓴다.
---

# gen_build — BUILD 생성기 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/gen_build.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

BUILD 생성기 — frontmatter·owl:imports 에서 패키지별 BUILD.bazel 을 생성한다 (bazel-dependency-review 2단계).

## 언제 쓰는가

청크를 추가·삭제하거나 frontmatter 링크(refines·serves·supersedes·verifies)를 고친 뒤 BUILD 를 재생성하고 드리프트를 검사할 때 쓴다.

## 명령

```bash
python3 tools/gen_build.py --root .
python3 tools/gen_build.py --check --root .
bazel test //:build_drift_test
```

## 원본

- 절차: [`docs/method.md` 6. 연결](../../../docs/method.md#6-연결)
- 도구: `tools/gen_build.py` (`bazel run //tools:gen_build`) — 사용법은 docstring 이 원본이다

```text
gen_build.py [--check] [--root .]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
