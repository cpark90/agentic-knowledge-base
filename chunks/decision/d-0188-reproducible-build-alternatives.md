---
id: https://agentic-knowledge-base.dev/id/chunk-d0188
type: decision
level: concrete
title_ko: 대안 — 재현 가능한 빌드 투영
title: Alternatives — reproducible build projection
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:56+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-reproducible-build
---
**대안** — 묶음의 네 결정마다 원천(harness-functional `docs/materialize-design.md`·harness-concrete `docs/odr-bind-lock.md`)이 대비한 안을 적는다.

- d-0162(검증 선행·결정론): 해석되지 않은 참조를 조용히 빠뜨리는 안과 그것을 빌드 실패로 처리하는 안은 둘 다 기각이다. 빌드는 `.ref` 스텁을 내고 참조마다 상태를 `MANIFEST.json`에 남기며, 오프라인 환경은 실패하지 않고 결손을 표시한 채 내려간다(materialize-design "Validation gate"·참조 해석 절).
- d-0178(lock): 재현한 빌드가 lock의 `policyApplied`를 "lock"으로 고쳐 쓰는 안은 기각이다. 고쳐 쓰면 재현된 트리가 원본과 바이트 동일하지 않으므로 값은 그대로 옮기고 "lock으로 재현했다"는 사실은 빌드 보고에 둔다(odr-bind-lock "The lock").
- d-0179(원자적 생성): 목적지 `--out`에 바로 쓰는 단순 빌드는 기각이다. 해시 대조가 쓰기 도중에 돌므로 불일치가 나면 반쪽 트리가 남는다(materialize-design "Atomic emit").
- d-0180(슬롯 주소): 산출 파일 이름을 선택된 후보 파일의 basename에서 얻는 안은 기각이다. 후보를 바꾸면 파일 이름이 바뀌어 호출자가 깨진다. 후보가 없는 직접 참조 도구만 참조의 basename을 쓴다(materialize-design "Stable emitted filenames").
