---
id: https://agentic-knowledge-base.dev/id/chunk/db1802fc-1d6d-4330-9bc8-6779828a8ab7
type: artifact
level: executable
title_ko: 절 esc (tools/chunk2kg.py)
title: section esc in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
composite: {id: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0, title_ko: 절 복합체 esc (tools/chunk2kg.py), title: section composite esc in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/db1802fc-1d6d-4330-9bc8-6779828a8ab7, https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b, https://agentic-knowledge-base.dev/id/chunk/578f22f5-4d9d-43ef-8b3a-1459989cf6e9, https://agentic-knowledge-base.dev/id/chunk/53335074-67d7-45c8-b564-78065ea96eb8, https://agentic-knowledge-base.dev/id/chunk/16348364-cc1d-4c34-9b3f-ca27ea8e9ad4], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `esc` 다. head 트리플의 방출

**정의** — `esc` · `label_stmts` · `emit_chunk` · `id_base` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── head 트리플의 방출 ────────────────────







LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "satisfies", "constrains", "derivesFrom", "allocates", "generates",
             "overlapsWith")  # overlapsWith 는 relatedTo 족의 약한 잎 — 링크 키라 링크 개체·복원 표시를 받는다 (overlap-ontology)
RESTORED_KEY = "restored"  # 복원 링크의 표시 (p10-restored-link-marking) — 값은 같은 단위 지식의 링크 키 대상 IRI 목록
RESTORED_GATE = getattr(kb_lib, "RESTORED_GATE", "restored")  # 게이트 id — FAIL [restored] (단일 정의 위치 kb_lib)
# 단위 지식 IRI 이름공간 — 호출 저장소가 고른다 (task 0327 손질 9).
# `id:` 이름공간 리터럴의 단일 정의 위치다. `kb_lib` 이 `ID_BASE`·`ID` 로 다시 내보내고 다른 도구는 그것을 쓴다 — 이 모듈이
# 원본인 까닭은 head 액션이 rdflib 없이 돌아 `kb_lib` 을 import 하지 못하기 때문이다(토큰 계수기와 같은 자리). 값은 환경
# 변수 `KB_ID_BASE` 가 주고, 비었으면 이 저장소의 도메인이다. Bazel 에서는 빌드 설정 `//defs:id_base` 가 이 환경 변수를
# 채운다 — 지식 타깃은 루트 모듈의 것에만, 도구 바이너리(`bazel run`)는 어느 저장소의 것에든 준다(defs/knowledge.bzl
# `kb_id_base_var`·`kb_tool_binary`, defs/kb.bzl `_id_base_env`). `agt:` 어휘 이름공간은 매개화하지 않는다 —
# 코어 어휘는 의존 저장소와 공유한다.
ID_BASE_DEFAULT = "https://agentic-knowledge-base.dev/id/"
ID_BASE_ENV = "KB_ID_BASE"




ID_BASE = id_base()

# 증거 종류 — 구축(편집 부산물, 10.3절)은 구축 기록, 복원(restored: 표시 — 도구·에이전트가 제안하고 사람이 확정)은 제안 (evidence-ontology)
EVIDENCE_BUILT = "agt:constructionRecord"
EVIDENCE_RESTORED = "agt:proposal"
```
<!-- 인용 끝 -->
