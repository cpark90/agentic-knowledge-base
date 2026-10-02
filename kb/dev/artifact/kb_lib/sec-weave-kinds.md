---
id: https://agentic-knowledge-base.dev/id/chunk/4094bbc8-4190-42c4-bb55-0a73231095d1
type: artifact
level: executable
title_ko: 절 weave-kinds (tools/kb_lib.py)
title: section weave-kinds in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2
---
**절** — `tools/kb_lib.py` 의 절 `weave-kinds` 다. 문서 뷰 (weave — p12-documents-are-generated: 문서는 저장하지 않고 생성하며 생성 시각과 질의를 적는다)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 문서 뷰 (weave — p12-documents-are-generated: 문서는 저장하지 않고 생성하며 생성 시각과 질의를 적는다) ─────────────────
WEAVE_KINDS = ("adr", "requirements", "changelog", "audit")
# 작업 집합 예산 게이트 (도입 2단계 구체화 조건 "역할·앵커별 작업 집합 ≤ 예산", handoff/workset-budget-gate-2026-09-22) —
# 앵커가 주어졌을 때만 문서 전체(라벨 목록 + 펼친 본문) 줄 수가 예산을 넘으면 FAIL. 앵커 없는 뷰(스코프 전체 라벨
# 목록, 구조적으로 예산을 넘는다)는 판정 밖이라 `//kg:workset` 기본 빌드는 깨지지 않는다
DECISION_PART_FILES = {"conclusion": "conclusion.md", "rationale": "rationale.md", "alternatives": "alternatives.md"}  # 결정 복합체의 세 부분 (STYLEGUIDE §4)
```
<!-- 인용 끝 -->
