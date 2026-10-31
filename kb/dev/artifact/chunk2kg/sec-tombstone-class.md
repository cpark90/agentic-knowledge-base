---
id: https://agentic-knowledge-base.dev/id/chunk/4ad3e8f0-449f-47fc-a2a4-15e5d9fff594
type: artifact
level: executable
title_ko: 절 tombstone-class (tools/chunk2kg.py)
title: section tombstone-class in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7efb5476-c231-4b0e-9e6c-a2389a12409e
composite: {id: https://agentic-knowledge-base.dev/id/composite/7efb5476-c231-4b0e-9e6c-a2389a12409e, title_ko: 절 복합체 tombstone-class (tools/chunk2kg.py), title: section composite tombstone-class in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/4ad3e8f0-449f-47fc-a2a4-15e5d9fff594, https://agentic-knowledge-base.dev/id/chunk/ee10ae76-e59e-44e2-87ad-d798ab4c0311, https://agentic-knowledge-base.dev/id/chunk/c313808a-9a95-42a4-8ca1-8ffe3e2e8e65, https://agentic-knowledge-base.dev/id/chunk/480b1d93-d4ad-4a70-8cea-3d25a7966d12], part_of: https://agentic-knowledge-base.dev/id/composite/067a8c81-640e-4b58-8235-c18119d80f2e}
---
**절** — `tools/chunk2kg.py` 의 절 `tombstone-class` 다. 묘비

**정의** — `tombstones` · `emit_tombstone` · `is_tombstone_block` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 묘비 ────────────────────
# 파일을 지운 단위 지식의 IRI 를 지키는 최소 노드 (agt:Tombstone, 유저 답 Q-0061#Q146). 노드의 원본은 지운 항목을 대체한
# 살아 있는 항목의 frontmatter `sources` 항목이다 — `{resource: git:<리비전>:<경로>, id: <옛 IRI>, title_ko: …, title: …}`.
# 이 도구는 Bazel 샌드박스 안에서 돌아 git 을 부르지 않는다(밀폐성). 그래서 옛 IRI·라벨은 git 이 아니라 frontmatter 가 싣고,
# git 위치는 사람이 원문을 찾아가는 영구 링크로만 쓴다. 묘비는 파일이 없어 Bazel 타깃이 아니므로 그 IRI 를 향한 링크는
# deps 가 되지 않는다(gen_build.links_of) — 대신 링크 개체와 직접 트리플은 다른 링크와 똑같이 나간다.
TOMBSTONE_CLASS = "agt:Tombstone"
GIT_PERMALINK = re.compile(r"^git:[0-9a-f]{7,40}:[^:\s]+$")  # 영속 위치 = 리비전 + 경로 (kg/base-kg.ttl 의 prov:atLocation 과 같은 꼴)
```
<!-- 인용 끝 -->
