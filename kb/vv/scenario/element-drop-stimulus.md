---
id: https://agentic-knowledge-base.dev/id/chunk/08b0f187-6366-5805-8fc7-d651a3f00d80
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 어휘에 슬롯이 없는 frontmatter 키 하나를 가진 청크의 방출
title: Logical scenario stimulus — emitting a chunk that carries one frontmatter key without a vocabulary slot
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/4add0b57-4550-4459-9513-179a53525343]
part_of: https://agentic-knowledge-base.dev/id/composite/097dfb73-cb9c-5c47-8675-4561b9952f3f
composite: {id: https://agentic-knowledge-base.dev/id/composite/097dfb73-cb9c-5c47-8675-4561b9952f3f, title_ko: 어휘에 슬롯이 없는 frontmatter 키 하나를 가진 청크의 방출, title: Emitting a chunk that carries one frontmatter key without a vocabulary slot, ordered: [https://agentic-knowledge-base.dev/id/chunk/08b0f187-6366-5805-8fc7-d651a3f00d80, https://agentic-knowledge-base.dev/id/chunk/e560644d-1b59-5c5a-a9e5-2601cca7d6be, https://agentic-knowledge-base.dev/id/chunk/c4ec66e3-fc08-5696-a7f9-3801fbfff410]}
---
**자극** — abstract 자극(어휘에 슬롯이 없는 요소를 담은 소스의 반영)을 frontmatter 키 하나로 좁힌다. actor는 청크를 저작하는 에이전트이고 action은 `chunk2kg`가 소비하지 않는 키 하나를 더한 임시 청크를 `validate --chunk-files`로 대조하는 것이다. 순서는 자극 대조 → 그 키만 뺀 통제 대조다. `keep()`은 필수 키 일곱이다. 변수는 더한 키 `extra_key` 하나이고 ODD 속성 `id:cond-language-policy`(언어 정책 — 키 이름의 허용 범위)에 매인다. keep은 `none`이다.

```yaml
keep:
  extra_key: {odd: "id:cond-language-policy", values: ["none"], reject: ["provenanceNote"]}
cover:
  - {rule: factor, var: extra_key, factors: {"agt:elementWithoutVocabularyDropped": provenanceNote}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/4e216613-6a9b-40a2-8c31-d3a13fae72ae
  verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
  title_ko: "어휘에 슬롯이 없는 frontmatter 키 ${extra_key}를 가진 임시 청크가 FAIL [element-drop]으로 거부되고 그 키만 뺀 통제는 종료 0이다"
  title: "A temporary chunk carrying the frontmatter key ${extra_key} without a vocabulary slot is rejected with FAIL [element-drop], and the control without that key exits 0"
  summary: "어휘에 슬롯이 없는 frontmatter 키 `${extra_key}`를 가진 임시 청크 하나를 자극으로 쓴다."
  stimulus: "임시 파일 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 필수 키 일곱을 갖추고 키 `${extra_key}` 하나를 더 갖는다. 통제는 그 키만 뺀 같은 청크다."
  files:
    vv-element-drop.md: |
      ---
      id: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-000000000001
      type: memory
      level: concrete
      title_ko: 요소 탈락 자극
      title: Element drop stimulus
      status: draft
      generated: {by: vnv/probe, at: 2026-10-01T00:00:00+09:00}
      ${extra_key}: 어휘에 슬롯이 없는 키 하나
      ---
      **관측** — 자극이다.
    vv-element-drop-control.md: |
      ---
      id: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-000000000002
      type: memory
      level: concrete
      title_ko: 요소 탈락 통제
      title: Element drop control
      status: draft
      generated: {by: vnv/probe, at: 2026-10-01T00:00:00+09:00}
      ---
      **관측** — 통제다.
  command: "python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop.md}}; python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop-control.md}}"
  reject:
    prose: "자극을 준 실행은 종료 1과 `FAIL [element-drop]`, 미지 키의 이름, 위반 1건을 낸다. 통제는 종료 0과 `PASS [validate]`를 낸다."
    expect:
      - {exit: 1, contains: ["FAIL [element-drop]", "frontmatter 키 '${extra_key}' 를 chunk2kg 가 소비하지 않는다", "FAIL [validate] — 1건"]}
      - {exit: 0, contains: ["PASS [validate]"]}
```
