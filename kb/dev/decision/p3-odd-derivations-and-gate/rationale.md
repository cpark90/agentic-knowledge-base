---
id: https://agentic-knowledge-base.dev/id/chunk/606a9e7e-1c1d-443c-b642-1508f67531cf
type: decision
level: logical
title_ko: ODD가 없으면 파생물이 무엇의 부분집합인지 정의되지 않는다
title: Without the ODD nothing defines what derivations are a subset of
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/87eb4cc9-8cf0-4461-a9af-24945dccda21
---
**근거** (노트 3.3절) — ODD가 없으면 스코프는 무엇의 부분집합인지 정의할 수 없고, 가정은 임의 문장이 되어 판정할 수 없으며, 시나리오가 설계 범위 안인지 밖인지 판단할 수 없고, 설계 공간의 선택지가 무한히 열리고, 커버리지의 분모가 없고, 하네스마다 경계를 따로 정의하게 된다.

거부가 강한 이유는 통과를 허용하는 순간 ODD의 폐쇄(3.1절)가 사실상 해제되기 때문이다. 예외를 한 번 만들면 "ODD에 없지만 통과한" 속성 집합이 어디에도 기록되지 않은 채 자란다.

이 거부는 2.5절 안티패턴 계층의 verify 질의 하나로 구현된다 — "ODD에 없는 조건을 참조하는 파생물이 존재하면 실패".
