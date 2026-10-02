---
id: https://agentic-knowledge-base.dev/id/chunk/5526e00b-4e15-4bca-895d-283fbe9c687b
type: schema
level: concrete
title_ko: 어휘에 슬롯이 없는 frontmatter 키 하나를 가진 임시 청크가 FAIL [element-drop]으로 거부되고 그 키만 뺀 통제는 종료 0이다
title: A temporary chunk carrying one frontmatter key without a vocabulary slot is rejected with FAIL [element-drop], and the control without that key exits 0
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-10-01T01:10:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/4e216613-6a9b-40a2-8c31-d3a13fae72ae]
verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
---
**케이스** — 어휘에 슬롯이 없는 frontmatter 키를 가진 임시 청크 하나를 자극으로 쓴다. 게이트 `element-drop`이 선 뒤 처음으로 그 대조 (a) 키 전수 대조를 케이스로 잰다.

**자극** — 임시 파일 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 필수 키 일곱을 갖추고 `chunk2kg`가 소비하지 않는 키 `provenanceNote` 하나를 더 갖는다. 통제는 그 키만 뺀 같은 청크다.

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
expect:
  - exit: 1
    contains: ["FAIL [element-drop]", "frontmatter 키 'provenanceNote' 를 chunk2kg 가 소비하지 않는다", "FAIL [validate] — 1건"]
  - exit: 0
    contains: "PASS [validate]"
```

**기대** — 자극을 준 실행은 종료 1과 `FAIL [element-drop]`, 미지 키의 이름, 위반 1건을 낸다. 통제는 종료 0과 `PASS [validate]`를 낸다.

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop.md}}; python3 tools/validate.py --ontology kb/ontology/profile/development/plane-substance-ontology.ttl --chunk-files {{vv-element-drop-control.md}}`

**표본 근거** — 이 자극이 어기는 규칙은 frontmatter 키의 전수 대조 하나다(`p8-minimal-negative-stimulus`). `--ontology`에 실체 표의 원본만 주어 대조 (b)의 대칭차가 공집합이 되고, 통제가 같은 명령에서 그 키만 뺀 같은 청크로 종료 0을 내므로 종료 코드가 (a)의 분기만을 가리킨다. 한계: `--chunk-files` 없이 도는 게이트는 `//kg:gate_test` 쪽이고 이 케이스는 그 전수 입력을 재현하지 않는다.
