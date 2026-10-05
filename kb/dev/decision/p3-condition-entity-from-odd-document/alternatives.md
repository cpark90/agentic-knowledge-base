---
id: https://agentic-knowledge-base.dev/id/chunk/e90e5aae-5c3e-4f9a-b218-172a9ba73a41
type: decision
level: logical
title_ko: TTL 손 저작과 암묵 제외는 기각된다
title: Hand-written ODD TTL and implicit exclusion are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a42db8cd-3f7e-443f-bb88-61ac79945d82
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 조건 개체를 ODD TTL에 손으로 쓰고 `agt:hasCondition`에 따로 등록한다 | 2026-09-10까지의 방식이다. ODD 문서가 OpenODD로 정해져 TTL은 생성물이 됐다(`pe-odd-is-openodd`). 생성물은 손으로 쓰지 않는다 |
| 검토한 제외를 적지 않고 restrictive 모드의 암묵 제외에 맡긴다 | 노트 3.2절이 기각했다. 적지 않은 것과 검토한 뒤 제외한 것이 갈리지 않아 같은 검토가 반복된다 |
