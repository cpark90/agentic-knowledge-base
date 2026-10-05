---
id: https://agentic-knowledge-base.dev/id/chunk/4e4de139-7e0c-512a-ba73-0263a7cf9a15
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 앵커를 준 vnv 작업 집합 뷰의 예산 판정
title: Logical scenario stimulus — the budget verdict of the anchored vnv workset view
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T22:58:21+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/753f40c0-a1f4-5fcc-a1ae-e7b5961e4e18
composite: {id: https://agentic-knowledge-base.dev/id/composite/753f40c0-a1f4-5fcc-a1ae-e7b5961e4e18, title_ko: 앵커를 준 vnv 작업 집합 뷰의 예산 판정, title: The budget verdict of the anchored vnv workset view, ordered: [https://agentic-knowledge-base.dev/id/chunk/4e4de139-7e0c-512a-ba73-0263a7cf9a15, https://agentic-knowledge-base.dev/id/chunk/3a2355b4-bcf0-5b08-b129-ae149404c3b4, https://agentic-knowledge-base.dev/id/chunk/0653b14b-2a0a-508d-95b6-eedb6ea09ccc]}
---
**자극** — actor는 dispatch 전에 작업 집합을 뽑는 에이전트이고 action은 vnv 역할의 `//kg:workset`을 셋으로 빌드하는 것이다. 순서는 앵커 + 기본 예산 → 앵커 없는 통제 → 같은 앵커 + 좁힌 예산이다. 앵커는 결정 `p11-execution-mode-and-workset`의 결론(`id:chunk/965f738a-db50-4729-a551-e58a90cd6320`)이다. `keep()`은 역할·앵커·수준 창·홉이다. 변수는 예산 `budget` 하나이고 ODD 속성 `id:cond-tokenizer-lock`(토크나이저 고정 — 예산의 단위인 토큰을 고정 계수기가 센다)에 매인다. keep은 `5418`(빌드 기본값)이고 keep 밖 값은 `10`이다. 양성 두 명령은 예산 플래그를 주지 않아 빌드 기본값을 쓴다.

```yaml
keep:
  budget: {odd: "id:cond-tokenizer-lock", values: [5418], reject: [10]}
cover:
  - {rule: factor, var: budget, factors: {"agt:worksetBudgetOverrun": 10}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/7db997bc-4f86-4b0c-aa3f-e941657a94a7
  verifies: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c]
  title_ko: "결정 p11-execution-mode-and-workset의 결론을 앵커로 준 vnv 작업 집합 뷰가 기본 예산에서 빌드되고 예산 ${budget}에서 FAIL [workset-budget]로 거부된다"
  title: "The vnv workset anchored on the conclusion of the decision p11-execution-mode-and-workset builds within the default budget and is refused with FAIL [workset-budget] at budget ${budget}"
  summary: "앵커를 준 뷰·앵커 없는 통제·예산을 좁힌 음성 자극(예산 ${budget}) 셋을 종료 코드로 판정한다."
  stimulus: "`//kg:workset`을 셋으로 빌드한다. 첫째는 앵커 + 기본 예산, 둘째는 앵커 없는 통제, 셋째는 같은 앵커 + 예산 ${budget}(음성 자극)이다."
  command: "bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320; bazel build //kg:workset --//kb:role=vnv; bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320 --//kb:budget=${budget}"
  reject:
    prose: "첫째·둘째 빌드는 종료 0이다. 성공한 빌드 액션은 산출물 내용을 표준출력에 내지 않으므로 문구 대조는 실패하는 셋째에만 둔다. 셋째는 예산 ${budget}이 라벨 목록 길이보다 작아 `FAIL [workset-budget]`로 실패한다."
    expect:
      - {exit: 0}
      - {exit: 0}
      - {exit: 1, contains: ["FAIL [workset-budget]"]}
```
