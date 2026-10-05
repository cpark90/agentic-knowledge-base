---
id: https://agentic-knowledge-base.dev/id/chunk/94abc6b4-5443-51c2-9871-2ea56efb8a0a
type: decision
level: logical
title_ko: 논리 시나리오 자극 — when이 거짓인 확정 링크 하나의 가정 판정
title: Logical scenario stimulus — assumption checking of one confirmed link whose when is false
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4751cd7f-fc42-512c-83a6-077b508c4877
composite: {id: https://agentic-knowledge-base.dev/id/composite/4751cd7f-fc42-512c-83a6-077b508c4877, title_ko: when이 거짓인 확정 링크 하나의 가정 판정, title: Assumption checking of one confirmed link whose when is false, ordered: [https://agentic-knowledge-base.dev/id/chunk/94abc6b4-5443-51c2-9871-2ea56efb8a0a, https://agentic-knowledge-base.dev/id/chunk/852389f8-db54-5797-926c-03c1adbe7c3b, https://agentic-knowledge-base.dev/id/chunk/71a436ab-dc56-563d-82f0-9fcaa598c915]}
---
**자극** — actor는 조건을 깨는 실험자이고 action은 `when`이 조건 하나에 매인 확정 링크를 담은 그래프를 그 조건을 깬 채 `assume_check`로 판정하는 것이다. 순서는 깬 조건으로 판정 → 같은 자극을 깨지 않고 판정이다. `keep()`은 지지 증거를 가진 확정 링크다. 변수는 깨는 조건 `broken` 하나이고 ODD 속성 `id:cond-build-system`(빌드 체계)에 매인다. keep은 `none`(깨지 않음)이다.

```yaml
keep:
  broken: {odd: "id:cond-build-system", values: ["none"], reject: ["cond-build-system"]}
cover:
  - {rule: factor, var: broken, factors: {"agt:brokenAssumption": cond-build-system}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c
  verifies: [https://agentic-knowledge-base.dev/id/chunk/2921c7a6-95a6-49b2-83d1-4b90bfd44c1a]
  title_ko: "when이 거짓인 확정 링크 하나가 ${broken}을 깬 assume_check에서 suspect로 유도되고 종료 코드 1이며 깨지 않은 같은 자극은 종료 0이다"
  title: "A single confirmed link whose when is false is derived to suspect by assume_check with ${broken} broken, and the same stimulus without the break exits 0"
  summary: "`when`이 거짓인 확정 링크 하나를 자극으로 쓴다."
  stimulus: "임시 파일 하나다. 이름은 `vv-when-cycle.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 확정 링크 하나가 `in(${broken})`인 `when`과 지지 증거를 갖는다. 가정·의존 청크는 없다."
  files:
    vv-when-cycle.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> .
      @prefix id:  <https://agentic-knowledge-base.dev/id/> .
      id:link-vv-when-sample a agt:Link , agt:ConfirmedLink ;
          agt:linkFrom id:chunk-vv-when-sample-from ; agt:linkTo id:chunk-vv-when-sample-to ;
          agt:linkKind agt:refines ; agt:linkState "confirmed" ; agt:when "in(${broken})" ;
          agt:hasEvidence id:evidence-vv-when-sample .
      id:evidence-vv-when-sample a agt:Evidence ; agt:evidenceKind agt:runResult ;
          agt:evidenceRef "vv-when-cycle probe" ; agt:polarity "+" .
  command: "python3 tools/assume_check.py --break ${broken} {{vv-when-cycle.ttl}}; python3 tools/assume_check.py {{vv-when-cycle.ttl}}"
  reject:
    prose: "`--break ${broken}`을 준 실행은 종료 1과 `when`이 거짓인 링크, 링크 행 `confirmed → suspect`, 사유를 낸다. `--break` 없는 같은 자극은 종료 0이다."
    expect:
      - {exit: 1, contains: ["`when` 이 거짓인 링크 있음", "confirmed | suspect", "거짓 — `in(${broken})`"]}
      - {exit: 0}
```
