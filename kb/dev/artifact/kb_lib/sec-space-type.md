---
id: https://agentic-knowledge-base.dev/id/chunk/0438fb73-9d57-469c-bdf0-52b1e0162b51
type: artifact
level: executable
title_ko: 절 space-type (tools/kb_lib.py)
title: section space-type in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d7f34b4e-71f9-47c7-8540-4f10c1a663db
composite: {id: https://agentic-knowledge-base.dev/id/composite/d7f34b4e-71f9-47c7-8540-4f10c1a663db, title_ko: 절 복합체 space-type (tools/kb_lib.py), title: section composite space-type in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/0438fb73-9d57-469c-bdf0-52b1e0162b51, https://agentic-knowledge-base.dev/id/chunk/908a996f-e2c4-43ce-a43f-63ff651548af, https://agentic-knowledge-base.dev/id/chunk/464fe842-81a3-438f-901c-e9cef6f1dc88], part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893}
---
**절** — `tools/kb_lib.py` 의 절 `space-type` 다. 설계 공간 (`-space`) — 열린 설계 변수와 그 후보 (결정 p9-candidate-storage · p9-design-space-file)

**정의** — `space_link_ends` · `space_candidate_of` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 설계 공간 (`-space`) — 열린 설계 변수와 그 후보 (결정 p9-candidate-storage · p9-design-space-file) ───────────
# 후보 링크는 확정 링크와 다른 자리에 산다: 확정은 단위 지식 head(frontmatter 링크 키 → Bazel deps), 후보는 설계 공간(`-space`)이다.
# **후보는 결코 deps 가 되지 않는다** — `-space` 는 kb_chunk 타깃이 아니라 A-Box 그래프(`*-space.ttl`)로만 올라가고
# 그 그래프는 //kg:gate_test 의 --data 다. type 은 지식 종류 이름이 아니라 온톨로지 클래스 `agt:Space` 이고 level 은 logical 이다.
# 후보의 표면 상태 어휘 셋은 링크 상태(agt:linkState)의 기존 값으로 내린다 — 새 상태 어휘를 만들지 않는다 (STYLEGUIDE §0 재사용):
#   open → candidate(agt:CandidateLink) · eliminated → invalid · confirmed → confirmed(agt:ConfirmedLink)
# 배제 근거는 증거 기록의 (−) 한 줄이다 (agt:Evidence · agt:polarity "-") — 근거 없는 배제 금지가 r-011 의 요지다.
SPACE_TYPE = "agt:Space"    # 설계 공간(`-space`)의 frontmatter type
SPACE_LEVEL = "logical"     # 설계 공간(`-space`)의 level — 후보·제약·배제 근거가 사는 수준 (6.4절 수준 허용표)
SPACE_STATUS = ("open", "resolved")                            # agt:spaceStatus 의 값 어휘
SPACE_STATES = ("open", "eliminated", "confirmed")             # 후보의 표면 상태 어휘 (본문 `state:`)
LINK_STATE_INVALID = "invalid"                                 # 배제된 후보의 링크 상태 (link-state-ontology)
# 표면 상태 → (rdf:type 목록, agt:linkState). CandidateLink·ConfirmedLink 는 linkState 의 클래스 표현이므로
# 짝이 어긋나면 verify 질의 link-state-class-mismatch 가 잡는다 — 배제는 클래스 없이 상태만 invalid 다
SPACE_STATE_LINK = {
    "open": ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE),
    "eliminated": ("agt:Link", LINK_STATE_INVALID),
    "confirmed": ("agt:Link , agt:ConfirmedLink", LINK_STATE_CONFIRMED),
}
# 확정 근거가 될 수 있는 증거 종류 (9.11절 "구축(+) 또는 실행(+) 없이 확정 불가", 결정 p9-evidence-ledger-with-belief 의 확정 규칙).
# 유저 결정은 질문지의 답이므로 확정 근거다 (Q-0055 Q111-a, 2026-10-24). 단일 정의 위치는 이 상수다 — space2kg · validate 가 읽고,
# verify 질의 confirmed-without-evidence 의 FILTER 목록이 이 집합과 같은지를 validate.check_confirming_evidence 가 본다
SPACE_CONFIRMING_EVIDENCE = ("constructionRecord", "runResult", "userDecision")
# 유저 결정 증거의 참조 꼴 (Q-0055 Q111-a) — 질문지와 질문 번호 `Q-NNNN#Qn`, 또는 질문 번호 이전 기록의 `legacy/<파일 이름>.md`
USER_DECISION_KIND = "userDecision"
USER_DECISION_REF = re.compile(r"^Q-\d{4}#Q\d+$|^legacy/[^/\s]+\.md$")
# 변수 종류 → 후보 링크의 방향 (Q-0055 Q112-b). 변수 종류는 (링크 타입, 변수 출발 항목의 지식 종류)이다 — 같은 refines 라도 결정
# 변수(출발이 요구 또는 abstract 결정, 후보가 그것을 정제하는 결정)와 코드 변수(출발이 파일 복합체, 그것이 정제하는 계약이
# 후보)는 방향이 반대다. 값 "candidate" 는 후보가 출발점이고 변수의 출발 항목이 끝점이다, "variable" 은 그 반대다. 어느 쪽이든 확정되면
# 출발점 단위 지식의 frontmatter 에 그 링크 키가 적히므로 head 의 확정 링크와 (출발, 끝, 종류)가 같다. 표에 없는 변수 종류는
# space2kg 가 거부한다(조용히 한쪽으로 읽지 않는다). 방향 규칙은 이 표 하나에만 있다
SPACE_CANDIDATE_DIRECTION = {
    ("refines", "requirement"): "candidate",
    ("refines", "decision"): "candidate",
    ("refines", "artifact"): "variable",
}
```
<!-- 인용 끝 -->
