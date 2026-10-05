---
id: https://agentic-knowledge-base.dev/id/chunk/403eedf2-5844-4233-9481-a499c3ce212c
type: decision
level: concrete
title_ko: 규범 문서 규약 — ODD 문서는 OpenODD 형식이고 확장 키는 checks와 exclusions_reviewed 둘이다
title: Normative-document conventions — The ODD document is OpenODD, with exactly two extension keys: checks and exclusions_reviewed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f867e42b-0106-4796-8861-4bdc493e15db
---
**규약** — `pe-odd-is-openodd`의 결론을 규범 문서에 싣는 문장이다.

규약: 조건과 ODD | `kb/odd/project-odd.yml` (OpenODD YAML 매핑: `TAXONOMY`·`MODULES`·`INCLUDE_AND`…; 확장 키 `ATTRIBUTES`·`LITERALS`·`CHECKS`·`EXCLUSIONS_REVIEWED`) → 생성 `project-odd.ttl`·`taxonomy.yml` | YAML 손, TTL 생성
규약: 각 속성의 범주를 `related/condition`에서 생성된 택소노미(`taxonomy.yml`)에 대응시킨다. 없으면 온톨로지를 먼저 확장한다. 문서는 OpenODD 형식이다.
