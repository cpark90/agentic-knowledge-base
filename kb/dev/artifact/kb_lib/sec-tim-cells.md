---
id: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946
type: artifact
level: executable
title_ko: 절 tim-cells (tools/kb_lib.py)
title: section tim-cells in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `tim-cells` 다. 추적 매트릭스 (TIM — plane×plane 의 허용 칸; 노트 14.1 정정본 3단계 "매트릭스", metrics 3단계 대리 · weave audit 이 같은 정의)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 추적 매트릭스 (TIM — plane×plane 의 허용 칸; 노트 14.1 정정본 3단계 "매트릭스", metrics 3단계 대리 · weave audit 이 같은 정의) ──
# (링크 종류, 출발 plane, 도착 plane). 앞 7칸은 개발 KB 안의 정제·대체·만족 링크, 뒤 6칸은 V&V 사슬(p8-scenario-ladder-rungs ·
# p8-pass-criteria): 목표 derivesFrom 요구 · 기준 refines 목표 · 케이스 refines 기준 · 검증기 refines 케이스, 같은 높이의 verifies —
# concrete 케이스 → 결정, executable 검증기 → 산출물. logical 높이는 기준이 목표를 refines 하는 것으로 검증 대응이 성립하므로
# contract→decision `verifies` 칸이 없다 (유저 답 Q30-b, 2026-10-04)
TIM_CELLS = (("refines", "decision", "requirement"), ("serves", "decision", "requirement"), ("supersedes", "decision", "decision"),
             ("satisfies", "contract", "decision"), ("derivesFrom", "schema", "decision"), ("constrains", "schema", "contract"),
             ("satisfies", "artifact", "decision"),
             # 검증 목표 ↔ 요구의 칸은 `derivesFrom` 하나다 — functional 높이의 검증 대응은 목표가 요구를 derivesFrom 하는
             # 것으로 성립하므로 `verifies`:requirement→requirement 칸은 두지 않는다 (유저 답 Q30-b · Q52-a)
             ("derivesFrom", "requirement", "requirement"), ("refines", "contract", "requirement"), ("refines", "schema", "contract"),
             ("refines", "artifact", "schema"), ("verifies", "schema", "decision"),
             ("verifies", "artifact", "artifact"), ("refines", "artifact", "decision"), ("refines", "artifact", "contract"))
# `refines`:artifact→contract 는 V&V 의 정제 계층이다 — verify 질의 `verifies-without-criteria` 가 "검증기는 합격 기준을
# refines 해야 한다"를 이미 강제하므로 그 칸이 표에 없던 것은 누락이었다. 중첩 복합체 보정을 고치자(link_cells) 드러났다.
# `refines`:artifact→decision 은 코드의 정제 계층이다 (p7-code-links-on-file-composite, 유저 승인 2026-09-30) — 파일 복합체가 결정을 `refines` 하고
# 그 결정이 요구에 닿는다. `serves` 가 아닌 까닭은 그 술어의 정의역이 agt:DecisionChunk 이기 때문이다(fulfilment-ontology):
# artifact 청크가 요구를 직접 serves 하면 추론이 그것을 결정 청크로 만들고 shape DecisionSubstanceShape 이 거부한다.
# 링크의 구축·복원 구분 (유저 결정 2026-09-12 (b), p10-restored-link-marking) — 기준은 술어가 아니라 **증거 종류**다.
# 구축 = 증거가 구축 기록(constructionRecord)뿐인 확정 agt:Link. 본문 식별자 추출(extract_refs)은 직접 트리플(LINK_EXTRACTED)과
# 후보 링크 개체(agt:CandidateLink — cites 만, 증거는 구축 기록)로 나가며 구축·복원 어느 쪽에도 세지 않고 후보로 따로 센다.
# 복원 = 구축 기록이 아닌 증거(proposal — 후보의 출처)를 하나라도 가진 확정 agt:Link. frontmatter `restored:` 표시의 링크에 chunk2kg 가
# 확정 기록(constructionRecord — 사람이 frontmatter 에 적은 편집 시점 기록)과 proposal 을 함께 낸다: 9.11절 규칙 "구축(+) 또는
# 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제하므로 proposal 만으로는 확정 링크가 성립하지 않는다.
# `link` 후보 파이프라인(tools/link.py, //kg:link_candidates)이 후보를 내고 사람이 restored: 로 확정한다
LINK_EXTRACTED = (AGT.cites, AGT.usesConcept)
CONSTRUCTION_EVIDENCE = AGT.constructionRecord
# 링크 상태 (link-state-ontology agt:linkState) — 후보·확정의 값. 본문 추출 참조(extract_refs 의 agt:cites)는 후보 링크 개체
# (agt:CandidateLink, "candidate")로 나가고 frontmatter 링크는 확정(agt:ConfirmedLink, "confirmed")이다 (p10-extracted-references-are-
# candidates, 유저 승인 2026-09-19). 상태는 증거 종류가 아니라 "누가 링크 키에 적었는가"로 갈린다 — 둘 다 증거는 구축 기록이다.
# chunk2kg·extract_refs 는 rdflib 없이 돌므로 같은 문자열을 getattr 폴백으로 갖는다
LINK_STATE_CANDIDATE = "candidate"
LINK_STATE_CONFIRMED = "confirmed"
# 청크 uuid 는 work-id 다 (p10-split-keeps-work-identity, 유저 승인 2026-09-19). 분할 조각은 frontmatter `specializationOf: <원 IRI>`
# 로 원본을 가리키고 chunk2kg 가 prov:specializationOf 를 방출한다. 링크 IRI 는 양 끝의 뿌리 uuid(사슬을 따라 올라간 work-id)로
# 계산한다. 대상은 살아 있는 같은 plane 의 청크여야 하고 사슬은 순환하지 않는다 — validate check_specialization 이 FAIL [specialization],
# 대상 부재는 check_dangling 이 FAIL [dangling] 으로 거부한다. 순환은 chunk2kg 도 (뿌리를 계산할 수 없으므로) 같은 게이트 id 로 거부한다
```
<!-- 인용 끝 -->
