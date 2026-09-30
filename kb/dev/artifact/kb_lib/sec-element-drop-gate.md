---
id: https://agentic-knowledge-base.dev/id/chunk/e31f02b8-f20b-4349-9076-c3fabce682f4
type: artifact
level: executable
title_ko: 절 element-drop-gate (tools/kb_lib.py)
title: section element-drop-gate in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `element-drop-gate` 다. 요소 탈락 검사 (`element-drop`) — 현상 P19 의 관측 수단 (위험 분석 G1, vnv 설계 2026-09-29)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 요소 탈락 검사 (`element-drop`) — 현상 P19 의 관측 수단 (위험 분석 G1, vnv 설계 2026-09-29) ────────────────
# "어휘가 없는 소스 요소는 슬롯이 없어 조용히 빠진다"(참조 저장소 R3)를 소스 전수와 방출 전수의 차로 잡는다.
# 차가 공집합이 아니면 FAIL 이다 — 조용히 버려진 요소가 있다는 뜻이고, 대응은 어휘 확장이다(가정 asm-missing-vocabulary-is-signal).
# 검사 둘의 소스 집합은 (a) 청크 frontmatter 의 최상위 키, (b) 프로파일이 선언한 plane 실체 클래스다.
ELEMENT_DROP_GATE = "element-drop"  # 게이트 id — FAIL [element-drop]
# chunk2kg 가 emit_chunk 에서 직접 읽는 선택 키. 필수 키는 chunk2kg.REQUIRED, 링크 키는 chunk2kg.LINK_KEYS 가 정의처이고
# 이 셋의 합집합이 "소비되는 키"다. chunk2kg 가 새 키를 읽으면 여기에 등재한다 — 등재 없이 쓰인 키는 이 게이트가 잡는다.
CHUNK_OPTIONAL_KEYS = ("verified", "sources", "assumes", "pattern", "coUpdatesWith", "part_of", "composite",
                       "restored", "specializationOf", "targets", EXPOSES_KEY, USES_KEY)
```
<!-- 인용 끝 -->
