---
name: query
description: 역량 질문(CQ)의 답을 그래프에서 라벨 목록으로 얻거나 한 항목이 무엇을 가리키는지 SPARQL 로 확인할 때 쓴다.
---

# query — 일반 질의 도구 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/query.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

일반 질의 도구 — 역량 질문(docs/competency-questions.md)을 SPARQL 로 노출한다 (로드맵 다음 산출 4, 노트 2.7절).

## 언제 쓰는가

역량 질문(CQ)의 답을 그래프에서 라벨 목록으로 얻거나 한 항목이 무엇을 가리키는지 SPARQL 로 확인할 때 쓴다.

## 명령

```bash
bazel run //tools:query
bazel run //tools:query -- CQ-07 --labels
bazel run //tools:query -- CQ-19 --labels --bind '?x=<IRI|id:슬러그|라벨>'
```

## 원본

- 절차: [`docs/method.md#8-조회`](../../../docs/method.md#8-조회)
- 도구: `tools/query.py` (`bazel run //tools:query`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:query -- CQ-07 [--limit N] [--labels] [--bind ?x=<IRI|id:슬러그|agt:용어|라벨>]
bazel run //tools:query                       # 전체 CQ 의 행 수 요약표
query.py --report cq.md --queries <dir|*.rq> --ttl <TTL...>    # 뷰 //kg:cq 의 생성기
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
