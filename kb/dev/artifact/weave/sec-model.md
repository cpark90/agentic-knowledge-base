---
id: https://agentic-knowledge-base.dev/id/chunk/6cb7a2fd-8fd8-4145-86f5-40b4618edc3b
type: artifact
level: executable
title_ko: 절 model (tools/weave.py)
title: section model in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574
composite: {id: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574, title_ko: 절 복합체 model (tools/weave.py), title: section composite model in tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/6cb7a2fd-8fd8-4145-86f5-40b4618edc3b, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1, https://agentic-knowledge-base.dev/id/chunk/53b29448-345d-4abe-b57a-44a8f6ed1d5d, https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67, https://agentic-knowledge-base.dev/id/chunk/810e2101-a0d5-405a-a081-39c0b6d82812], part_of: https://agentic-knowledge-base.dev/id/composite/50eac9df-d01a-488f-8254-02ba61b00bf0}
---
**절** — `tools/weave.py` 의 절 `model` 다. 모델 — 그래프와 본문의 적재

**정의** — `Model` · `load_bodies` · `head` · `refs` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 모델 — 그래프와 본문의 적재 ────────────────────





# 자기 자신을 다시 만드는 명령 (G6) — kind 마다 하나다
REPRODUCE = {"adr": "bazel build //kb/dev:adr", "requirements": "bazel build //kb/dev:requirements",
             "changelog": "bazel build //kb/dev:changelog", "audit": "bazel build //kg:audit"}






SKOS_NOTATION = URIRef("http://www.w3.org/2004/02/skos/core#notation")  # 현상의 질문지 표기(P1~P22)
RISK_MARK_DECLARED = "선언"   # frontmatter `exposes` — 저자가 적은 표지
RISK_MARK_EXTRACTED = "인용"  # 본문의 현상 IRI — extract_refs 가 뽑은 표지
COMPOSITES_HEADING = "결정 복합체"  # 결론·근거·대안이 세 파일로 갈린 결정 — 단일 파일 결정과 동격이므로 같은 깊이에 둔다
SINGLES_HEADING = "단일 파일 결정 (v1·harness 유래)"  # chunks/decision/d-*.md — 결론·근거·대안이 한 본문 안에 있다


anchors_of = kb_lib.heading_anchors  # GitHub 제목 앵커 규칙의 단일 정의처는 kb_lib (목차 링크, STYLEGUIDE §7)
```
<!-- 인용 끝 -->
