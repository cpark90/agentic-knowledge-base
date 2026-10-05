---
id: https://agentic-knowledge-base.dev/id/chunk/ca869ce3-18e1-4d2c-abb8-309e21147ccb
type: artifact
level: executable
title_ko: 절 class-plane (tools/chunk2kg.py)
title: section class-plane in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/741f8dd1-f282-478e-b9c0-40e1300f6dce
composite: {id: https://agentic-knowledge-base.dev/id/composite/741f8dd1-f282-478e-b9c0-40e1300f6dce, title_ko: 절 복합체 class-plane (tools/chunk2kg.py), title: section composite class-plane in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/ca869ce3-18e1-4d2c-abb8-309e21147ccb, https://agentic-knowledge-base.dev/id/chunk/9bfb814f-db8d-42dc-b618-9f691a50596d], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `class-plane` 다. plane 클래스의 역 사상

**정의** — `plane_of_class` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── plane 클래스의 역 사상 ────────────────────
# 클래스 지역명 → plane 이름 — PLANE_CLASS 의 역이다. 그래프에서 plane 을 읽는 도구(metrics·weave·workset·community·
# open_questions·validate)가 `<X>Chunk` 의 접두를 소문자로 바꿔 plane 을 얻던 규칙은 `norm` 에서 깨진다 — 그 plane 의
# 클래스는 `agt:DocumentSectionChunk` 다(p12-norm-documents-from-section-chunks). 역 사상의 정의처를 여기 하나로 둔다.
CLASS_PLANE = {cls.split(":", 1)[1]: plane for plane, cls in PLANE_CLASS.items()}
```
<!-- 인용 끝 -->
