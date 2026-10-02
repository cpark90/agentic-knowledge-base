---
name: link
description: frontmatter 링크가 없는 청크 쌍의 복원 후보를 체계 안 증거(본문 인용·테스트 공동 커버·개념 공유)로 뽑아 사람이 restored 표시로 확정할 때 쓴다.
---

# link — 복원 후보 생성기 뷰 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/link.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

복원 후보 생성기 뷰 — frontmatter 링크가 없는 청크 쌍의 링크 후보를 체계 안 증거만으로 낸다 (로드맵 8단계 복원, p10-link-by-construction · p10-candidate-and-confirmed-link · p10-link-judgement-evidence).

## 언제 쓰는가

frontmatter 링크가 없는 청크 쌍의 복원 후보를 체계 안 증거(본문 인용·테스트 공동 커버·개념 공유)로 뽑아 사람이 restored 표시로 확정할 때 쓴다.

## 명령

```bash
bazel build //kg:link_candidates && cat bazel-bin/kg/link-candidates.md
python3 tools/gen_build.py --root . && bazel test //...   # 앵커 청크에 링크 키와 restored: 를 적은 뒤
```

## 원본

- 절차: [`docs/method.md` 6. 연결](../../../docs/method.md#6-연결)
- 도구: `tools/link.py` (`bazel run //tools:link`) — 사용법은 docstring 이 원본이다

```text
link.py --out link-candidates.md [--k 7] [--min-shared 3] <TTL...>   (bazel build //kg:link_candidates)
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
