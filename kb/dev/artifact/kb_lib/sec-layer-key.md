---
id: https://agentic-knowledge-base.dev/id/chunk/b4403a87-b970-44a2-b550-f28855ca6d39
type: artifact
level: executable
title_ko: 절 layer-key (tools/kb_lib.py)
title: section layer-key in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/581eccf7-5ec4-435b-8757-e8042fb462e3
composite: {id: https://agentic-knowledge-base.dev/id/composite/581eccf7-5ec4-435b-8757-e8042fb462e3, title_ko: 절 복합체 layer-key (tools/kb_lib.py), title: section composite layer-key in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/b4403a87-b970-44a2-b550-f28855ca6d39, https://agentic-knowledge-base.dev/id/chunk/0ee2e47f-3e9a-4742-8506-41a3e3aec54e], part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893}
---
**절** — `tools/kb_lib.py` 의 절 `layer-key` 다. 서비스 층 (`layer`) — 지식 종류와 직교하는 역할 속성 agt:inLayer (결정 p0-service-is-a-three-layer-wiki, 2026-10-01)

**정의** — `load_extracted_sources` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 서비스 층 (`layer`) — 지식 종류와 직교하는 역할 속성 agt:inLayer (결정 p0-service-is-a-three-layer-wiki, 2026-10-01) ────
# 항목이 서비스의 어느 층(지식·방법론·프로세스)에서 역할을 갖는지를 frontmatter `layer:` 로 적고 chunk2kg 가
# agt:inLayer 를 방출한다. **링크 키가 아니다**: 대상이 지식이 아니라 온톨로지 개체라 링크 개체(agt:Link)의 치역
# 밖이고 Bazel deps 도 되지 않는다 — agt:targets·agt:exposesFactor 와 같은 자리다.
# **명시가 없어도 방출한다** — 기본값은 지식 층이고, 표시 누락이 산발로 세어지지 않아야 하므로 기본값을 그래프에
# 적는다(결정 근거 "기본값을 지식으로 두는 까닭"). 값 어휘 → 개체의 사상은 chunk2kg.LAYERS 가 단일 정의 위치이고
# (EARS_PATTERNS 와 같은 자리 — 그 도구는 rdflib 없이 타깃마다 돈다), 값의 닫힌 집합은 shape layer-shapes.ttl 이 판정한다.
LAYER_KEY = "layer"
LAYER_PREDICATE = "agt:inLayer"
# 옛 이름 `former_title_ko` — 이름이 바뀐 지식의 과거 표기다(결정 p0-skos-label-synonyms: hiddenLabel 은 과거 표기). 단위 지식의
# 최상위 키는 단위 지식의 옛 이름, `composite:` 선언 안의 같은 키는 복합체의 옛 이름이고 chunk2kg 가 둘 다 `skos:hiddenLabel` @ko 로
# 낸다. 채널 검사 `names` 는 이미 보낸 메시지가 그때의 이름을 적어도 통과시키려고 읽는다 — 발신 전 검사는 현재 이름만 받는다
FORMER_TITLE_KEY = "former_title_ko"
```
<!-- 인용 끝 -->
