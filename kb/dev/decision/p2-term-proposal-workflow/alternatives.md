---
id: https://agentic-knowledge-base.dev/id/chunk/fd2e495d-b23f-41ad-8154-622cbac898e5
type: decision
level: logical
title_ko: 에이전트 직접 병합과 승인 생략
title: Direct merge by the agent; skipping human approval
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b
---
**대안** — **에이전트가 온톨로지에 직접 병합하는 안.** 배제 — 신뢰할 수 없는 센서가 판정자가 되며, 잘못 만들어진 개념 하나가 그 어휘로 쓴 모든 문장을 오염시킨다.

**컴파일러 통과만으로 자동 병합하는 안.** 배제 — 3계층은 형식·논리·금지 패턴을 잡을 뿐 "이 개념이 이 분야에 실제로 필요한가"를 판정하지 못한다. 과설계(2.10절)는 기계가 잡지 못한다.

**코어 모듈에 병합하는 안.** 배제 — 코어 수정은 import한 모든 모듈의 가정을 흔든다.
