---
id: https://agentic-knowledge-base.dev/id/chunk/0438fb73-9d57-469c-bdf0-52b1e0162b51
type: artifact
level: executable
title_ko: 절 space-type (tools/kb_lib.py)
title: section space-type in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `space-type` 다. 설계 공간 (`-space`) — 열린 설계 변수와 그 후보 (결정 p9-candidate-storage · p9-design-space-file)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 설계 공간 (`-space`) — 열린 설계 변수와 그 후보 (결정 p9-candidate-storage · p9-design-space-file) ───────────
# 후보 링크는 확정 링크와 다른 자리에 산다: 확정은 청크 head(frontmatter 링크 키 → Bazel deps), 후보는 `-space` 청크다.
# **후보는 결코 deps 가 되지 않는다** — `-space` 는 kb_chunk 타깃이 아니라 A-Box 그래프(`*-space.ttl`)로만 올라가고
# 그 그래프는 //kg:gate_test 의 --data 다. type 은 plane 이름이 아니라 온톨로지 클래스 `agt:Space` 이고 level 은 logical 이다.
# 후보의 표면 상태 어휘 셋은 링크 상태(agt:linkState)의 기존 값으로 내린다 — 새 상태 어휘를 만들지 않는다 (STYLEGUIDE §0 재사용):
#   open → candidate(agt:CandidateLink) · eliminated → invalid · confirmed → confirmed(agt:ConfirmedLink)
# 배제 근거는 증거 기록의 (−) 한 줄이다 (agt:Evidence · agt:polarity "-") — 근거 없는 배제 금지가 r-011 의 요지다.
SPACE_TYPE = "agt:Space"    # `-space` 청크의 frontmatter type
SPACE_LEVEL = "logical"     # `-space` 청크의 level — 후보·제약·배제 근거가 사는 수준 (6.4절 수준 허용표)
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
# 확정 근거가 될 수 있는 증거 종류 (9.11절 "구축(+) 또는 실행(+) 없이 확정 불가") — verify 질의 confirmed-without-evidence 와 같은 집합
SPACE_CONFIRMING_EVIDENCE = ("constructionRecord", "runResult")
```
<!-- 인용 끝 -->
