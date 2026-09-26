# 유저 피드백 채널 (user ↔ hci ↔ agents)

유저와 에이전트 사이의 소통을 모으는 영속 파일 채널. **담당은 hci agent이며, 유저와
직접 상세한 내용을 소통하는 에이전트는 hci뿐이다.** 형식 원본은 `kg/catalog-kg.ttl`의
`id:chan-user-feedback`(`agt:ownedBy id:role-hci`)이고, 이 문서가 규약 원본이다.

**그래프 밖**: 이 폴더의 파일은 지식 산출물이 아니라 소통 기록이다. 검사 게이트의
어휘·shape 검사 대상이 아니므로 자유롭게 서술한다. 소통이 낳은 결론은 채널에 남기지
않고 지식(온톨로지·ODD·청크)이나 문서로 승격되며, 그 승격이 이 채널의 목적이다.
유저 결정의 원문 기록은 [`purpose-statement.md`](purpose-statement.md) §8 원장에 있다.

## 쓰기 권한 (엄격)

| 행위자 | 작성·수정 | 조회 |
|---|---|---|
| **유저** | 전체 | 전체 |
| **hci** | `docs/feedback/**` 전체 + 자기 역할 메모리 `.claude/agent-memory/hci/**` — 이 둘이 hci의 유일한 쓰기 범위다 | 저장소 전체 |
| **다른 에이전트** | `agents/` lane의 **자기 항목만** (유저에게 전달할 내용, 인수 기록 `ref: handoff/…`) | 저장소 전체 (읽기 전용) |

- **승인됨·인수 대기(2026-09-22)**: [`spec-writing-standard-remainder-2026-09-22.md`](spec-writing-standard-remainder-2026-09-22.md) — G10 그림 틀 · 출처 개체 위치.
  인수인계 [`handoff/spec-writing-standard-remainder-2026-09-22.md`](handoff/spec-writing-standard-remainder-2026-09-22.md). 반영되면 제안 원문과 승인 항목을 제거한다
- **유저 판단 대기(2026-09-26)**: [`jev-judge-binding-2026-09-26.md`](jev-judge-binding-2026-09-26.md) — 판정자를 System One 모델에 붙일 것인가 ·
  [`test-hermeticity-2026-09-26.md`](test-hermeticity-2026-09-26.md) — 게이트 하나가 밀폐성에서 벗어난다 ·
  [`composite-beyond-decisions-2026-09-26.md`](composite-beyond-decisions-2026-09-26.md) — 복합체를 결정 밖으로 ·
  [`code-as-chunks-2026-09-26.md`](code-as-chunks-2026-09-26.md) — 코드를 청크로 올릴 것인가
- **승인됨·인수 대기(2026-09-23)**: 여섯 항목이 한꺼번에 승인됐다 — 링크 C·D·E · 형식화 M1·M5 · 관측과 연결 성분 · 요구 stable 전이 · 관측 시각 표기 · 에이전트 검증 도착점.
  인수인계는 `handoff/` 의 동명 항목 여섯이고 **수행 순서는 링크 항목이 먼저**다(유저 지정).
- **유저 판단 대기(2026-09-19)**: [`vv-profile-hazards-2026-09-19.md`](vv-profile-hazards-2026-09-19.md) — 위험 분석 G1~G6 의 입력 · [`workset-budget-gate-2026-09-22.md`](workset-budget-gate-2026-09-22.md) — 예산 초과의 게이트화
- **반영 완료·출처 개체 때문에 유지(2026-09-22)**: [`spec-writing-standard-adoption-2026-09-22.md`](spec-writing-standard-adoption-2026-09-22.md) — 공백 열 채우기 + 기존 저작 적용.
  인수인계 [`handoff/spec-writing-standard-adoption-2026-09-22.md`](handoff/spec-writing-standard-adoption-2026-09-22.md) 는 `closed` 다.
  제안 원문 [`inquiries/spec-writing-standard-proposal.md`](inquiries/spec-writing-standard-proposal.md) 는 `kg/base-kg.ttl` 의 출처 개체가 트리 경로를 가리켜 유지한다 —
  `git:<리비전>:<경로>` 로 바뀌면 둘 다 제거한다.
- **유저 판단 대기(2026-09-21)**: [`generated-requirements-stable-2026-09-21.md`](generated-requirements-stable-2026-09-21.md) — 요구 `r-027`·`r-028` 의 stable 전이 ·
  [`observation-timestamp-notation-2026-09-21.md`](observation-timestamp-notation-2026-09-21.md) — 관측 청크의 시각 표기
- **유저 판단 대기(2026-09-19)**: [`link-model-robustness-cde-2026-09-19.md`](link-model-robustness-cde-2026-09-19.md) — 남은 선택지 C·D·E ·
  [`connected-components-observations-2026-09-19.md`](connected-components-observations-2026-09-19.md) — 관측이 연결 성분을 늘린다 ·
  [`vv-profile-hazards-2026-09-19.md`](vv-profile-hazards-2026-09-19.md) — 위험 분석 G1~G6의 입력
- **반영 완료·C·D·E 때문에 유지**: [`link-model-robustness-2026-09-18.md`](link-model-robustness-2026-09-18.md) — A·B 반영됨(2026-09-19), 조사 원문은 [`inquiries/suggestion.md`](inquiries/suggestion.md)
- **남은 유저 lane 항목 넷** — `docs/` 가 마크다운 링크로 가리켜 아직 제거하지 못한다(링크를 `git:<리비전>:<경로>` 평문 인용으로 바꾸면 제거):
  [`bazel-dependency-review.md`](bazel-dependency-review.md)(`tools.md`) · [`dependency-graph-design.md`](dependency-graph-design.md)(`open-questions/link-judgement-basis.md`) ·
  [`design-detail-review.md`](design-detail-review.md)(`decomposition-audit.md`·`docs/README.md`) · [`label-representativeness-protocol.md`](label-representativeness-protocol.md)(`tools.md`·`roadmap.md`)
- refresh 2026-09-26: 돌아온 handoff 둘(`link-model-robustness-cde`·`nl-ambiguity-adoption`)을 `closed` 로, 기록 다섯을 `answered` 로,
  질문 둘을 유저 lane 항목 셋으로 중계했다. hci 의 조사 오류 둘을 handoff 에 정정으로 남겼다 — 정의문 규칙 36 → 52건, `refines` 상한의 셋째 읽기.
- refresh 2026-09-22: 인수 기록이 돌아온 handoff 1건을 `closed` 로, 기록 2건을 `answered` 로, 질문 2건을 유저 lane 으로 중계했다.
  제거는 없다 — 2026-09-19 기록 6건과 오늘 기록 2건은 발신자가 닫기 전이고, 승인 항목은 출처 개체가 트리 경로를 가리킨다. 기록은 git 이력(`e3b36d2`).
- refresh 2026-09-19: agents 3 제거(발신자 `closed` — 1단계 통과·4단계 첫 형태·`query` 도구 기록). 같은 날 기록 6건은 `answered` 로 두었다 —
  발신자가 `closed` 로 바꾸면 다음 사이클에 제거한다. 조사 lane [`inquiries/suggestion.md`](inquiries/suggestion.md) 는 `closed` 이나
  유저 lane 항목이 링크로 가리켜 유지한다. 기록은 git 이력(`68f9c7c` 이후).
- refresh 2026-09-14: agents 2 제거(발신자 `closed` — inspection 이관·간소화 기록). 유저 lane 넷은 `docs/` 링크가 남아 그대로.
- refresh 2026-09-13(2차): 10건 제거 — 유저 lane 4(라벨 실험 기록지·정답지·에이전트 판정 결과·agrtls 관행 검토) ·
  agents 4(발신자 `closed`) · 조사 lane 2(유저 원문, 답 완료). KG 출처 개체가 `git:<리비전>:<경로>` 를 가리키므로 트리에서 지워도 인용이 산다.
  기록은 git 이력(`36f6273` 이전).

- hci는 지식 산출물(kb/ontology/·kb/odd/·kg/·chunks/·tools/ 등)을 편집하지 않는다.
- 다른 에이전트는 이 채널에서 자기 항목 외 어떤 파일도 수정하지 않는다 — 유저 lane
  항목, hci의 중계문, 타 에이전트의 항목은 읽기 전용이다.

## lane 구조

```
docs/feedback/
├── README.md            # 이 문서 (규약 원본)
├── TEMPLATE.md          # 유저 lane 항목 양식
├── {주제-kebab}.md      # 유저 lane: user ↔ hci 항목
├── agents/              # 에이전트 lane: 타 에이전트 → hci
│   └── {발신역할}-{주제-kebab}.md
├── inquiries/           # 조사 lane: hci → 타 에이전트 조사 질문/답
    └── {주제-kebab}.md
└── handoff/             # 인수인계 lane: hci → 담당 역할 (verdict · 파급효과 · 반영 계획) — README.md 참조
    └── {유저 lane 항목 파일명}
```

### 유저 lane (`./*.md`) — user ↔ hci

유저는 hci를 통해 ① 구현된 내용의 **조사를 요청**하고, ② 구현에 반영할 내용을
**구체화**하며, ③ **제안**하고, ④ 다른 에이전트들로부터 온 **피드백을 검토**한다.

- **유저 → hci**: `{주제-kebab}.md`를 만들어 자유 서술 (`TEMPLATE.md` 참고). 한 파일에
  한 주제 (반영·승인 단위).
- **hci → 유저**: 결정 요청·에이전트 lane에서 올라온 피드백 중계를 항목으로 남긴다.
  유저 판단을 요청하는 항목은 **다섯 절**로 쓴다(`TEMPLATE.md`) — 한 줄 질문으로는 답을
  받을 수 없다. frontmatter에 `status: open`을 **반드시 포함**한다 — 유저는 필드를 새로 적지 않고
  `open`을 `approved`로 **고치기만** 하면 된다.
- **승인 게이트**: `status: approved`는 **유저만** 태깅한다. 이것이 지식 산출물 반영을
  허가하는 유일한 신호다. 승인 없이는 어떤 에이전트도 항목을 반영·제거하지 않는다. 거부는 `status: rejected`(유저만) —
  refresh가 승계 확인 뒤 제거한다 (2026-09-12).
- **hci는 수행하지 않는다** (2026-09-11 교정): 유저의 구두 답은 담당 역할(orchestrator 등)에게 유효한
  지시다. 그러나 hci는 어떤 답이든 채널 밖에 반영하지 않는다 — 답을 `## 답`에 옮기고 반영 계획을 구체화해
  담당 역할에 넘긴다. 기계 게이트 `//docs/feedback:channel_lint_test`가 hci의 반영 흔적을 FAIL로 잡고(담당
  역할의 `agents/` 항목 `ref: handoff/…` — 2026-09-12 이전 관례는 `인수: <역할> <날짜>` 줄 — 또는 되돌림·closed로 해소), `//kg:gate_test`의 writer 검사가 청크
  `generated.by`의 역할과 카탈로그 쓰기 권한을 대조한다.
  결정이 더 필요한 항목은 `## 답`에 결정을 적는 것이 먼저다.

### 에이전트 lane (`agents/`) — 타 에이전트 → hci

hci를 제외한 에이전트는 **유저 피드백이 필요할 때, 문제가 생겼을 때, 특이사항이
생겼을 때** 여기에 항목을 작성한다. 유저에게 직접 묻지 않는다.

- 파일명 `{발신역할}-{주제-kebab}.md`, frontmatter: `from: {역할}`, `status: open`,
  본문에 배경 + 필요한 결정/전달 내용 + (선택지가 있으면) 선택지.
- **hci가 사이클마다 스캔**해 검토한다: 유저 판단이 필요하면 유저 lane 항목으로
  중계(원본 링크 명시)하고 원본을 `status: relayed`로 바꾼다. 유저의 답이 오면 hci가
  원본 항목에 `## 답`을 채우고 `status: answered`로 바꾼다.
- 발신 에이전트는 자기 사이클에 자기 항목을 확인해 `answered`를 소비하고
  `status: closed`로 바꾼다. hci는 `closed` 항목을 다음 사이클에 제거한다(refresh).
  **closed 전 제거 금지** (custody transfer — 시간으로 완료를 가정하지 않는다).

### 조사 lane (`inquiries/`) — 유저 요청 원문과 hci의 조사 답

유저의 조사 요청 원문이 여기에 남고, hci가 조사 질문으로 구체화한 뒤 **직접 조사한다**(옛 inspection 역할을
2026-09-13에 hci로 이관). hci는 저장소를 읽어 같은 파일에 `## 답`(결론 + 근거 `file:line` 또는 IRI)을 채우고
`status: answered`로 바꾼 뒤, 유저 lane으로 중계하거나 대화로 보고하고 `closed`로 태깅한다. 개발·검증 판단이
필요한 조사만 `assignee`로 developer·vnv에 넘긴다. `closed` 항목은 다음 사이클에 hci가 제거한다.

## 완료 마커 — 작성 중 문서는 처리 금지

완료 판정은 시간이 아니라 **상태 확인**으로 한다 (verify-then-proceed):

- 에이전트가 쓰는 항목은 `{name}.wip.md`로 작성하고 완료 시 `{name}.md`로 **rename**
  한다 — rename이 완료 선언이다. 어떤 에이전트도 `*.wip.md`를 처리하지 않는다.
- hci가 쓰는 항목(중계·handoff)도 같다 — `.wip.md`로 쓰고 rename한다.
- 답의 placeholder(`(유저가 채움)`·`(hci가 유저의 답을 채움)`)가 남아 있으면 미완성으로 취급한다.

## 처리 파이프라인 (검증 → 유저 승인 → 반영 → refresh)

1. **inbox**: 항목이 유저 lane에 들어온다 (유저 서술 또는 hci의 중계·결정 요청).
2. **검토 (hci)**: 항목을 검토·구체화한다 — 관련 지식(청크 IRI·ODD 조건·결정)을
   찾아 링크하고, 필요하면 조사 lane으로 조사를 시킨 뒤 결과를 항목에 보강한다.
   지식 산출물과 `docs/`의 체계 문서는 편집하지 않는다.
3. **승인 (유저)**: 구체화된 반영 계획을 검토하고 `status: approved`(또는 `rejected`)로 고친다.
3′. **인수인계 (hci)**: 승인된 항목마다 `handoff/` 항목 — verdict·파급효과·반영 계획·확인 못 한 것.
4. **반영 (담당 역할)**: 승인된 항목만, 반영 계획대로 담당 write plane의 역할이
   반영한다 (결정은 orchestrator, 산출물은 developer). 반영 후 `bazel test //...`
   PASS 확인, `agents/` 항목(`ref: handoff/…`)에 반영 결과(무엇을 어디에)를 기록한다 — 유저 lane 항목에는 쓰지 않는다.
5. **refresh (hci)**: `approved`(또는 `rejected`)이고 승계가 확인된(handoff ↔ agents 쌍 닫힘) 항목만 제거한다. 반영 흔적은
   지식 산출물과 git 이력이 기록이다 — 채널에 사본을 남기지 않는다.
