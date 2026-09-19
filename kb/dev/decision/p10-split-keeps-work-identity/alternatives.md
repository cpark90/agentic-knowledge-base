---
id: https://agentic-knowledge-base.dev/id/chunk/569bf475-c625-43c7-8b5d-d608b730df60
type: decision
level: logical
title_ko: 링크 IRI에 시각·주체를 넣거나 모든 조각에 새 uuid를 주는 안은 기각된다
title: Putting time and agent into link IRIs or giving every fragment a new uuid is rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T17:20:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a76160fc-059f-437e-8f64-6e6c405cd18b
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 링크 IRI에 생성 시각·주체 포함(조사 원안) | frontmatter에 저장할 자리가 없어 재생성마다 달라진다. 객체형 링크 값이 필요한데 `p10-restored-link-marking`이 기각했다 |
| 분할 시 모든 조각에 새 uuid | 원 uuid를 가리키던 링크가 전부 고아가 된다. 지금의 손실을 규칙으로 굳힌다 |
| 조각을 복합체로만 묶기 | 구성은 링크가 아니다(4.5절). 이력·증거가 이어지지 않는다 |
| 링크 IRI를 uuid로 frontmatter에 저장 | 객체형 링크 값이다. 첫 형태의 비용이 크다 |
