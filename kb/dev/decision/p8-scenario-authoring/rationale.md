---
id: https://agentic-knowledge-base.dev/id/chunk/b93237ef-5a6b-414c-9b4c-46537dfa37f7
type: decision
level: logical
title_ko: 사람이 케이스를 쓰면 표본 근거가 사라진다
title: Hand-written cases lose their sampling grounds
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/791e4e4c-db54-45f9-a03b-8922cd7cc3af
---
**근거** (노트 8.22절, 8.23절, 8.2절) — 시나리오가 `decision`인 이유는 "무엇을 자극할 것인가"가 결정이고 결론·근거·배제 대안의 형태가 그대로 맞기 때문이다(8.2절). concrete를 생성기에 맡기는 이유는 케이스마다 `sampling:` 태그(8.23절)가 표본 근거로 남아야 커버리지 분모(`cover()`)가 정의되기 때문이며, 사람이 직접 쓴 케이스에는 그 근거가 없다. 부류에서 시작해야 요인(근거)이 G5 라이브러리와 연결되어 프로젝트를 넘는 재사용이 된다.
