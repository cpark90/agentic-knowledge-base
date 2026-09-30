---
id: https://agentic-knowledge-base.dev/id/chunk/db1802fc-1d6d-4330-9bc8-6779828a8ab7
type: artifact
level: executable
title_ko: 절 esc (tools/chunk2kg.py)
title: section esc in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
composite: {id: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0, title_ko: 절 복합체 esc (tools/chunk2kg.py), title: section composite esc in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/db1802fc-1d6d-4330-9bc8-6779828a8ab7, https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b, https://agentic-knowledge-base.dev/id/chunk/53335074-67d7-45c8-b564-78065ea96eb8], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**절** — `tools/chunk2kg.py` 의 절 `esc` 다. head 트리플의 방출

**정의** — `esc` · `emit_chunk` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── head 트리플의 방출 ────────────────────





LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "satisfies", "constrains", "derivesFrom", "allocates", "generates",
             "overlapsWith")  # overlapsWith 는 relatedTo 족의 약한 잎 — 링크 키라 링크 개체·복원 표시를 받는다 (overlap-ontology)
RESTORED_KEY = "restored"  # 복원 링크의 표시 (p10-restored-link-marking) — 값은 같은 청크의 링크 키 대상 IRI 목록
RESTORED_GATE = getattr(kb_lib, "RESTORED_GATE", "restored")  # 게이트 id — FAIL [restored] (정의처 kb_lib)
ID_BASE = "https://agentic-knowledge-base.dev/id/"
# 증거 종류 — 구축(편집 부산물, 10.3절)은 구축 기록, 복원(restored: 표시 — 도구·에이전트가 제안하고 사람이 확정)은 제안 (evidence-ontology)
EVIDENCE_BUILT = "agt:constructionRecord"
EVIDENCE_RESTORED = "agt:proposal"
```
<!-- 인용 끝 -->
