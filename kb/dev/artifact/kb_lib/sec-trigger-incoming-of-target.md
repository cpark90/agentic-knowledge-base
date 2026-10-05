---
id: https://agentic-knowledge-base.dev/id/chunk/81e13e64-2189-4bfa-b7ab-60f2c59898b1
type: artifact
level: executable
title_ko: 절 trigger-incoming-of-target (tools/kb_lib.py)
title: section trigger-incoming-of-target in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
composite: {id: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671, title_ko: 절 복합체 trigger-incoming-of-target (tools/kb_lib.py), title: section composite trigger-incoming-of-target in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/81e13e64-2189-4bfa-b7ab-60f2c59898b1, https://agentic-knowledge-base.dev/id/chunk/b92bd358-40c4-4414-b59c-70676927564b, https://agentic-knowledge-base.dev/id/chunk/a6fc9e1e-c79d-4e36-ac7b-36d17aaf0a0a, https://agentic-knowledge-base.dev/id/chunk/a171dc2a-1e86-477b-b9e7-4327ae6185f1, https://agentic-knowledge-base.dev/id/chunk/badba8ff-e4ce-4780-8483-a93e7c6631a5, https://agentic-knowledge-base.dev/id/chunk/9e7b4f02-5771-4b99-bd5c-6b89ee5cbe45, https://agentic-knowledge-base.dev/id/chunk/8bfec137-25dc-4b30-8a96-8897afc667ad, https://agentic-knowledge-base.dev/id/chunk/ff5236c7-129e-43c7-9466-8cf55445d254], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `trigger-incoming-of-target` 다. suspect 트리거의 선언 — 링크 타입별로 좁다 (handoff link-model-robustness-cde-2026-09-19 반영 2)

**정의** — `suspect_triggers_on` · `_confirmed_links` · `suspect_by_trigger` · `when_verdicts` · `suspect_by_when` · `suspect_saturation` · `link_origins` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── suspect 트리거의 선언 — 링크 타입별로 좁다 (handoff link-model-robustness-cde-2026-09-19 반영 2) ──────────────
# 자리: 이 상수가 선언의 원본이다 (STYLEGUIDE §7 — 규약 상수의 단일 정의처는 kb_lib).
# 형식: (링크 종류, 전파 규칙, 켜짐, 근거). **선언에 없는 종류는 돌지 않는다** — 기본이 꺼짐이다.
# 근거: 외부 실무(Eclipse Capra 와 추적성 유지 연구, docs/references.md 추적성)가 전파를 전 타입에 켜면 추적 매트릭스가
# suspect 로 포화한다고 보고한다. 그래서 정의문이 이미 전파를 규정한 supersedes 하나로 시작하고 나머지는 포화율
# (metrics 의 한 줄)을 보고 켠다.
TRIGGER_INCOMING_OF_TARGET = "incoming-of-target"  # 이 링크의 도착점을 가리키던 다른 확정 링크가 suspect 가 된다
SUSPECT_TRIGGERS = (
    ("supersedes", TRIGGER_INCOMING_OF_TARGET, True,
     "agt:supersedes 의 정의문이 규정한다 — 대체가 일어나면 옛 항목을 충족하던 링크가 전부 suspect 다 (8.11절)"),
    ("refines", TRIGGER_INCOMING_OF_TARGET, False,
     "포화 위험 — 확정 링크의 다수가 refines 라 켜면 매트릭스가 suspect 로 덮인다. 본문 변경 경로는 revalidate 가 맡는다"),
    ("verifies", TRIGGER_INCOMING_OF_TARGET, False,
     "검증 대응물의 변경은 vnv 의 판정 주석과 실행 기록이 맡는다 (8.20절) — 링크 전파로 겹치지 않는다"),
)
```
<!-- 인용 끝 -->
