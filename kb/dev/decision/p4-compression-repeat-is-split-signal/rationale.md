---
id: https://agentic-knowledge-base.dev/id/chunk/1f704fae-fa96-422a-a8fe-f23dbfcfc601
type: decision
level: logical
title_ko: 압축을 반복하면 가장 최근 개정이 가장 근거가 얇은 역전이 생긴다
title: Repeated compression inverts the record: the newest revision carries the thinnest rationale
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T16:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ff721aef-2663-430e-a491-4e0cc61f73b2
---
**근거** (노트 4.10절·4.4절; agrtls `design_webservice` L18) — 상한은 자립성과 예산을 지키는 장치이지 내용을 덜어내는
장치가 아니다. 그런데 상한에 걸릴 때마다 압축으로 대응하면 덜어내는 것은 대개 가장 최근에 더한 근거·예외·조건이다 —
개정이 거듭될수록 최근 내용이 가장 얇게 남는 역전이 생기고, 라벨은 그대로인데 본문이 말하는 범위가 줄어 라벨
대표성(4.13절)이 조용히 떨어진다.

4.10절의 분할 신호(라벨 둘·재사용·가정·suspect 입도)는 모두 내용의 성질을 보는 신호라 이 역전을 잡지 못한다.
압축 횟수는 내용을 읽지 않고 이력만으로 세는 신호이고, 42줄 근처에서 줄 수가 오르내린 흔적이 git에 그대로 남는다.
1회 유예를 두는 이유는 첫 압축은 대개 군더더기 제거라서다 — 두 번째부터는 덜어낼 군더더기가 없다.
