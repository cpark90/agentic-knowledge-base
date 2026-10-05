---
id: https://agentic-knowledge-base.dev/id/chunk/d63e1b31-110f-4fb7-ac79-c518f7c04112
type: norm
level: logical
title_ko: docs/rules.md 절 chunk의 이어짐 — 지식의 종류를 부르는 법과 본문 중복의 경계
title: docs/rules.md chunk section continued — naming kinds of knowledge and the bounds of body redundancy
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
continues: true
---
**지식의 종류는 "X 청크"라 부르지 않는다.** 조건·개념·변수·후보·결정·가정·시그니처·
함수·주석·관측처럼 고유 용어로 부르고, "청크"는 그것들이 따르는 구조 규칙을 가리킬 때만
쓴다 (유저 결정 2026-09-04). 온톨로지 클래스 이름(`agt:DecisionChunk` 등)과 그래프 라벨을
인용할 때는 그대로 쓴다. 그것은 구조 타입의 식별자다.

**본문 중복은 안전율로 용인한다** (유저 결정 2026-09-11,
[`p4-redundancy-as-safety-margin`](../../decision/p4-redundancy-as-safety-margin/conclusion.md)).
자립성이 맥락의 반복을 요구하므로 같은 서술이 여러 청크에 있는 것은 결함이 아니다. 단
경계가 있다. **개념·용어·라벨·요구의 중복은 용인하지 않는다.** 그 이유는 어휘 드리프트·
인터페이스 충돌·추적 커버리지 왜곡이다. 알고 둔 중복은 `coUpdatesWith`로 묶어 한쪽의 변경이
다른 쪽을 `suspect`로 만들게 한다. 링크 없는 중복이 드리프트다. 정리는 재검증 시점에서 일괄로
한다. `consistency` 보고는 커밋마다 내며 중복·라벨 형식·용어를 다룬다. 병합·묶기·유지 판정은
도입 단계 끝마다 한다.
