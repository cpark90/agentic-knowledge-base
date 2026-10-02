---
id: https://agentic-knowledge-base.dev/id/chunk/7902d58a-05cc-4832-9d03-50154c6f403e
type: artifact
level: executable
title_ko: 절 registry-head (tools/extract.py)
title: section registry-head in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
part_of: https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53
composite: {id: https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53, title_ko: 절 복합체 registry-head (tools/extract.py), title: section composite registry-head in tools/extract.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/7902d58a-05cc-4832-9d03-50154c6f403e, https://agentic-knowledge-base.dev/id/chunk/4333655e-49b9-4be9-b2f1-8c28243d8390, https://agentic-knowledge-base.dev/id/chunk/a83e5a5d-15ff-4e18-80b5-2c88dead1cfc], part_of: https://agentic-knowledge-base.dev/id/composite/99abae51-6823-4ed8-9bfe-4255801d4681}
---
**절** — `tools/extract.py` 의 절 `registry-head` 다. 등록부 (사이드카)

**정의** — `load_registry` · `dump_registry` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 등록부 (사이드카) ─────────────────────────────────────────────────────────────────────
# 손으로 쓰는 것은 `layer`·`refines`·`serves` 와 uuid 이고, `at`·`source_hash` 와 신설 uuid 는 추출기가 더한다.
# `layer` 는 소스 하나의 서비스 층이고 생성 청크 전부의 frontmatter 로 옮겨진다 — 도구는 프로세스 층의 실행
# 표면이므로 값은 `process` 다 (결정 p0-service-is-a-three-layer-wiki).
# `serves` 의 정의역은 `agt:DecisionChunk` 다(fulfilment-ontology) — `artifact` 청크가 요구를 직접 `serves` 하면
# 추론이 그것을 결정 청크로 만들고 shape DecisionSubstanceShape 이 거부한다. 코드가 요구에 닿는 길은 결정을
# `refines` 하는 것이고 그 결정이 요구를 `serves`·`refines` 한다 — 사다리를 건너뛰지 않는다 (6.2절).
# YAML 부분집합만 쓴다 — 이 저장소의 frontmatter 파서와 같은 수준이고 외부 의존이 없다.
REGISTRY_HEAD = """\
# 등록부 — 손이 원본이다. 한정 이름 → uuid 가 코드 청크의 정체성이고 이름은 그 위의 라벨이다
# (p10-split-keeps-work-identity · p7-code-extraction-direction). 생성기는 신설 uuid 와 `at`·`source_hash` 만 더한다.
# 개명은 아래 `ids` 의 키를 손으로 고치는 것이고, 삭제는 키를 손으로 지우는 것이다 — 둘 다 사람의 편집이다.
# 생성물은 `{package}/` 이며 손으로 고치면 `//:extract_drift_test` 가 거부한다.
"""
```
<!-- 인용 끝 -->
