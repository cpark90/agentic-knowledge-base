---
id: https://agentic-knowledge-base.dev/id/chunk/c1b71815-fa52-4137-af7f-397c51beee38
type: artifact
level: executable
title_ko: 절 exposes-key (tools/kb_lib.py)
title: section exposes-key in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `exposes-key` 다. 위험에서 파생된 항목의 표지 (`exposes`) — 위험 분석 G5 (노트 8.21절, 8.22절 "요인" 청크)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 위험에서 파생된 항목의 표지 (`exposes`) — 위험 분석 G5 (노트 8.21절, 8.22절 "요인" 청크) ─────────────────
# 항목이 어느 결함 요인(현상)을 노출하려고 서 있는지를 frontmatter `exposes: [<agt: 현상 IRI>…]` 로 적고
# chunk2kg 가 agt:exposesFactor 를 방출한다. **링크 키가 아니다**: 대상이 청크가 아니라 온톨로지 개체라
# 링크 개체(agt:Link)의 치역 밖이고 Bazel deps 도 되지 않는다 — agt:targets 와 같은 자리다.
# 대상이 agt:DefectFactor 의 하위 개체인지는 shape exposes-factor-shapes.ttl 이 판정한다(없는 개체도 거기서 FAIL).
EXPOSES_KEY = "exposes"
EXPOSES_PREDICATE = "agt:exposesFactor"
```
<!-- 인용 끝 -->
