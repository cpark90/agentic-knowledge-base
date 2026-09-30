---
id: https://agentic-knowledge-base.dev/id/chunk/395769c8-969a-4f2c-9cd8-6d0f4a6c6684
type: artifact
level: executable
title_ko: 절 linkage-excluded-planes (tools/kb_lib.py)
title: section linkage-excluded-planes in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
composite: {id: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6, title_ko: 절 복합체 linkage-excluded-planes (tools/kb_lib.py), title: section composite linkage-excluded-planes in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/395769c8-969a-4f2c-9cd8-6d0f4a6c6684, https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8, https://agentic-knowledge-base.dev/id/chunk/75bab730-77dc-4a3d-945e-72e305b4eb8c], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `linkage-excluded-planes` 다. 연결 지표 제외 plane (유저 승인 2026-09-23 · 2026-09-29 — handoff/verdict-in-metrics-2026-09-27)

**정의** — `chunk_planes` · `link_cells` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 연결 지표 제외 plane (유저 승인 2026-09-23 · 2026-09-29 — handoff/verdict-in-metrics-2026-09-27) ──────────────
# 연결 성분과 CQ20 후방 추적 귀속은 **저작된 지식**만 잰다. `memory`(관측)는 실행의 부산물이고, `annotation`(판정
# 주석)은 산출물에 대한 리뷰이지 요구를 향해 정제되는 항목이 아니다 — 둘 다 저작된 지식의 고립·귀속을 재는 지표의
# 대상이 아니다. `metrics.py` 하나가 이 상수로 성분 계산과 `reaches_req` 분모 두 자리를 채운다.
LINKAGE_EXCLUDED_PLANES = ("memory", "annotation")
```
<!-- 인용 끝 -->
