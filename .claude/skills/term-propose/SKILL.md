---
name: term-propose
description: 관측에서 뽑은 개념 후보를 검사를 거쳐 온톨로지 승인 큐(kb/ontology/proposals/)에 제안할 때 쓴다.
---

# term_propose — 용어 제안 워크플로 (노트 2.5절)

> 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring과 `kb_lib.SKILLS` (`tools/gen_skills.py`). 검사: `//:skills_drift_test`

용어 제안 워크플로 (노트 2.5절) — 일반화가 온톨로지에 닿을 때의 절차.

## 언제 쓰는가

관측에서 뽑은 개념 후보를 검사를 거쳐 온톨로지 승인 큐(kb/ontology/proposals/)에 제안할 때 쓴다.

## 명령

```bash
bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:<상위> --label-ko '<한글>' --label-en '<english>' --definition '<속+종차>' --cq CQ-NN
```

## 원본

- 절차: [`docs/method.md` 10. 일반화](../../../docs/method.md#10-일반화)
- 도구: `tools/term_propose.py` (`bazel run //tools:term_propose`) — 사용법은 docstring 이 원본이다

```text
term_propose.py --id retry-policy --kind class --parent agt:Condition \
--label-ko "재시도 정책" --label-en "retry policy" \
--definition "…인 조건. (속+종차)" --cq CQ12 [--derived-from <관측 IRI>]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
