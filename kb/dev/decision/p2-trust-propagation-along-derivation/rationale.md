---
id: https://agentic-knowledge-base.dev/id/chunk/bc4de86c-2c7c-40d2-a5a5-61a66b1c4b5b
type: decision
level: logical
title_ko: 신뢰 없는 조상은 후손 전부를 신뢰 없게 만든다
title: An untrusted ancestor taints every descendant
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/34cd97d1-50df-4db6-8511-fd10b918eaf3
---
**근거** (노트 2.12절) — 파생 DAG 위에서 신뢰 없는 조상이 있으면 민감 행동을 거부하는 방식이 에이전트 메모리 시스템에서 이미 실증되었다. 이 체계는 같은 DAG(`derives-from`·`sources`)를 이미 갖고 있으면서 신뢰 등급만 전파시키지 않고 있었다.

전파가 없으면 세탁이 일어난다 — 외부 유입 관측을 근거로 만든 결정이 한 단계만 지나면 출처를 잃고 확정처럼 보인다. 6.10절 가정 전파와 같은 구조를 신뢰 등급에 적용하면 그 경로가 막힌다.

질의로 쓰는 것이 결정적이다. 신뢰 등급을 사람이 검토하는 규약으로 두면 검토되지 않은 것이 통과하지만, verify 질의로 두면 통과가 불가능하다 (2.5절).
