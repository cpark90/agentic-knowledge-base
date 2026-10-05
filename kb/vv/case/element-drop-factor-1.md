---
id: https://agentic-knowledge-base.dev/id/chunk/01f8fc6f-7be6-5cd7-a78a-519ba63aaa4c
type: schema
level: concrete
title_ko: 어휘에 슬롯이 없는 frontmatter 키 provenanceNote를 가진 임시 청크가 FAIL [element-drop]으로 거부되고 그 키만 뺀 통제는 종료 0이다
title: A temporary chunk carrying the frontmatter key provenanceNote without a vocabulary slot is rejected with FAIL [element-drop], and the control without that key exits 0
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/4e216613-6a9b-40a2-8c31-d3a13fae72ae]
verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/08b0f187-6366-5805-8fc7-d651a3f00d80]
---
**케이스** — 어휘에 슬롯이 없는 frontmatter 키 `provenanceNote`를 가진 임시 청크 하나를 자극으로 쓴다.

**자극** — 임시 파일 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 필수 키 일곱을 갖추고 키 `provenanceNote` 하나를 더 갖는다. 통제는 그 키만 뺀 같은 청크다.

```yaml
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
    provenanceNote: 어휘에 슬롯이 없는 키 하나
    ---
    **관측** — 자극이다.
  vv-element-drop-control.md: "---\nid: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-000000000002\ntype: memory\nlevel: concrete\ntitle_ko: 요소 탈락 통제\ntitle: Element drop control\nstatus: draft\ngenerated: {by: vnv/probe, at: 2026-10-01T00:00:00+09:00}\n---\n**관측** — 통제다.\n"
```

**기대** — 자극을 준 실행은 종료 1과 `FAIL [element-drop]`, 미지 키의 이름, 위반 1건을 낸다. 통제는 종료 0과 `PASS [validate]`를 낸다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [element-drop]"
      - "frontmatter 키 'provenanceNote' 를 chunk2kg 가 소비하지 않는다"
      - "FAIL [validate] — 1건"
  - exit: 0
    contains:
      - "PASS [validate]"
```

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop.md}}; python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop-control.md}}`

**표본 근거** — `sampling:factor` · seed `1` · 시나리오 `element-drop` · 요인 `agt:elementWithoutVocabularyDropped`. 값은 `extra_key=provenanceNote`이고 판정 부류는 `reject`(keep 밖)다.
