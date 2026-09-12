---
id: https://agentic-knowledge-base.dev/id/chunk-d0017
type: decision
level: concrete
title_ko: 실패한 시도는 교훈으로 기록하고 반복되면 표준 규칙으로 승격한다
title: Failed attempts are captured as lessons and promoted to standard rules when they recur
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 시도가 실패·기각되거나 수정을 요구받으면 그 자체가 기록
트리거다: 무엇을 시도했고, 왜 실패했고, 대신 무엇을 하는지를 세션 종료
전 역할 메모리에 남긴다. 같은 교훈이 다음 실행에서 또 나오면 개인
노트로 두지 말고 표준 규칙(guardrail·instruction·스타일 문서 조항)으로
승격한다.

**근거** (harness-functional CLAUDE.md — lesson-capture / lesson-reuse /
lesson-promotion guardrail)
- 각 에이전트는 cold-start이므로 세션 시작 시 역할 메모리를 읽어
  특화하고, 종료 전 재사용 지식을 자기 폴더에 써서 축적한다 (자기 역할
  폴더에만, 파일 하나 + 인덱스 한 줄, 기존 있으면 갱신).
- 읽기는 세션 시작에 이미 하므로, 쓰기만 지키면 다음 세션이 교훈을
  안고 시작한다.
- 반복이 승격의 판정 기준이다 — 한 번 나온 교훈은 메모리, 두 번 나온
  교훈은 규칙.

**이 저장소와의 관계** — 노트 9.4절 메모리 승격 규칙의 실행 형태이며,
승격의 목적지는 memory plane → 주제 plane (일반화의 최소 단위, d-0006).
