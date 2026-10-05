---
id: https://agentic-knowledge-base.dev/id/chunk/395769c8-969a-4f2c-9cd8-6d0f4a6c6684
type: artifact
level: executable
title_ko: 절 linkage-excluded-planes (tools/kb_lib.py)
title: section linkage-excluded-planes in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
composite: {id: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6, title_ko: 절 복합체 linkage-excluded-planes (tools/kb_lib.py), title: section composite linkage-excluded-planes in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/395769c8-969a-4f2c-9cd8-6d0f4a6c6684, https://agentic-knowledge-base.dev/id/chunk/3591b8e8-245b-4398-94da-2db2b7e3339d, https://agentic-knowledge-base.dev/id/chunk/3f9e7300-40c1-4755-9e4d-f22da6f54774, https://agentic-knowledge-base.dev/id/chunk/c15db5ea-e132-44e3-b82c-929369970f50, https://agentic-knowledge-base.dev/id/chunk/2aa8020a-1553-48b5-8a54-b93aab820bbe, https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8, https://agentic-knowledge-base.dev/id/chunk/75bab730-77dc-4a3d-945e-72e305b4eb8c], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `linkage-excluded-planes` 다. 연결 지표 제외 plane (유저 승인 2026-09-23 · 2026-09-29 — handoff/verdict-in-metrics-2026-09-27)

**정의** — `space_linkage_edges` · `open_space_candidates` · `linkage_predicates` · `plane_of_node` · `chunk_planes` · `link_cells` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 연결 지표 제외 plane (유저 승인 2026-09-23 · 2026-09-29 — handoff/verdict-in-metrics-2026-09-27) ──────────────
# 연결 성분과 CQ20 후방 추적 귀속은 **저작된 지식**만 잰다. `memory`(관측)는 실행의 부산물이고, `annotation`(판정
# 주석)은 산출물에 대한 리뷰이지 요구를 향해 정제되는 항목이 아니다 — 둘 다 저작된 지식의 고립·귀속을 재는 지표의
# 대상이 아니다. `metrics.py` 하나가 이 상수로 성분 계산과 `reaches_req` 분모 두 자리를 채운다.
LINKAGE_EXCLUDED_PLANES = ("memory", "annotation")

# 연결로 세는 술어 — 단일 정의처 (STYLEGUIDE §7, 유저 지시 2026-10-01). 같은 절에 둔다: 제외 plane 과 함께 읽히는 선언이다.
# 추적 링크의 잎(docs/rules.md §4 링크 족 표)과 시간축 `supersedes` 다. 링크 밀도·plane×plane 매트릭스(TIM)가
# 보는 집합이고 `metrics.LINKS` 가 이 이름을 쓴다.
TRACE_LINKS = tuple(AGT[p] for p in ("refines", "serves", "satisfies", "verifies", "cites", "targets", "assumes", "supersedes",
                                     "derivesFrom", "constrains", "usesConcept", "allocates", "generates", "coUpdatesWith",
                                     "conflictsWith", "overlapsWith", "usesDefinition"))
# 연결 성분이 보는 술어 — 추적 링크 잎 + 구성 관계 + `prov:specializationOf` 다. 분할 조각은 원 청크의 정체성을
# 나눠 가진 것이지 새 지식이 아니므로(p10-split-keeps-work-identity) `specializationOf` 하나만 가진 조각은 고립이
# 아니다. 그 술어는 PROV-O 이고 링크의 세 족과 구성 관계 밖이라(p10-link-families, `supersedes` 와 같은 자리) 링크
# 밀도·TIM 에는 들지 않는다 — 연결과 귀속에만 든다.
LINKAGE_PREDICATES = TRACE_LINKS + (AGT.hasDirectPart, PROV.specializationOf)
# 연결 성분이 설계 공간 그래프(`//space:design_space`)에서 보는 술어 — 공간 → 변수 출발 항목(`agt:variableFrom`)과
# 공간 → 후보 링크 개체 → 후보(`agt:hasCandidate` ∘ `agt:linkTo`)다 (유저 결정 Q60-a). 후보 결론은 head 에 `refines` 를
# 갖지 않으므로(p9-candidate-storage "후보는 절대 deps가 되지 않는다") 이 길이 없으면 후보 결정 복합체가 고립 성분이 된다.
# 연결에만 든다 — 후보는 확정 링크가 아니므로 링크 밀도·TIM·확정 링크 수·전방 추적에는 들지 않는다.
SPACE_LINKAGE_PREDICATES = (AGT.variableFrom, AGT.hasCandidate, AGT.linkTo)






# CQ20 후방 추적 귀속이 거슬러 오르는 술어 — 조각은 원 청크를 거쳐 요구에 닿는다. 복합체 형제 경유는 따로다.
ASCRIPTION_PREDICATES = (AGT.refines, AGT.serves, PROV.specializationOf)
# 군집 탐지(`community`)의 엣지 종류 — 세 족의 잎만 본다. 시간축 `supersedes` 는 빼고, 정체성 관계
# `specializationOf` 도 빼므로 군집은 조각과 원본을 한 단위로 제안하지 않는다 (군집은 연결·귀속 지표가 아니다).
COMMUNITY_EDGE_KINDS = tuple(AGT[p] for p in ("refines", "serves", "cites", "usesConcept", "coUpdatesWith",
                                              "conflictsWith", "overlapsWith"))
```
<!-- 인용 끝 -->
