---
name: doccheck
description: 문서를 고친 뒤 죽은 링크·앵커·백틱 경로·산문 문체를 게이트와 같은 방식으로 검사할 때 쓴다.
---

# doccheck — 문서 현행성 게이트 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/tools.md` · `tools/doccheck.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

문서 현행성 게이트 — 죽은 링크·앵커·경로 (agrtls-practices-review N, 2026-09-12).

## 언제 쓰는가

문서를 고친 뒤 죽은 링크·앵커·백틱 경로·산문 문체를 게이트와 같은 방식으로 검사할 때 쓴다.

## 명령

```bash
bazel run //tools:doccheck -- *.md docs/*.md --target-only docs/agent-knowledge-system-notes.md
bazel test //:doccheck_test
```

## 원본

- 절차: [`docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다`](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)
- 도구: `tools/doccheck.py` (`bazel run //tools:doccheck`) — 사용법은 docstring 이 원본이다

```text
doccheck.py [--root DIR] [--waivers FILE] <문서 ...> [--target-only FILE ...]
bazel run //tools:doccheck -- *.md docs/*.md --target-only docs/agent-knowledge-system-notes.md
bazel run //tools:doccheck -- --report      # 문서 수치 대 생성물 수치, FAIL 아님 (진입점 문서 넷)
bazel run //tools:doccheck -- --report /tmp/x/doc.md   # 위치 인자가 있으면 그 문서로 바꾼다, 루트 밖도 된다
루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
