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
| **다른 에이전트** | `agents/` lane의 **자기 항목만** (유저에게 전달할 내용) | 저장소 전체 (읽기 전용) |

- 진행 중인 판단 요청: [`external-review-2026-09-11.md`](external-review-2026-09-11.md) §3 (2026-09-11). 채택됨: [`stage-pass-conditions.md`](stage-pass-conditions.md) · [`terminology-normalization.md`](terminology-normalization.md) · [`stage1-pass-measurement.md`](stage1-pass-measurement.md)
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
└── inquiries/           # 조사 lane: hci → 타 에이전트 조사 질문/답
    └── {주제-kebab}.md
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
  허가하는 유일한 신호다. 승인 없이는 어떤 에이전트도 항목을 반영·제거하지 않는다.
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

### 조사 lane (`inquiries/`) — hci → 타 에이전트

유저의 조사 요청을 hci가 조사 질문으로 구체화해 여기에 남긴다. 담당 에이전트
(주로 inspection)가 사이클마다 `status: open`을 스캔해 조사하고, 같은 파일에
`## 답`(결론 + 근거 `file:line` 또는 IRI)을 채운 뒤 `status: answered`로 바꾼다.
hci가 답을 유저 lane으로 중계·소비하면 `status: closed`로 태깅하고, 담당 에이전트가
다음 사이클에 제거한다.

## 완료 마커 — 작성 중 문서는 처리 금지

완료 판정은 시간이 아니라 **상태 확인**으로 한다 (verify-then-proceed):

- 에이전트가 쓰는 항목은 `{name}.wip.md`로 작성하고 완료 시 `{name}.md`로 **rename**
  한다 — rename이 완료 선언이다. 어떤 에이전트도 `*.wip.md`를 처리하지 않는다.
- 유저 답의 placeholder(`(유저가 채움)`)가 남아 있으면 미완성으로 취급한다.

## 처리 파이프라인 (검증 → 유저 승인 → 반영 → refresh)

1. **inbox**: 항목이 유저 lane에 들어온다 (유저 서술 또는 hci의 중계·결정 요청).
2. **검토 (hci)**: 항목을 검토·구체화한다 — 관련 지식(청크 IRI·ODD 조건·결정)을
   찾아 링크하고, 필요하면 조사 lane으로 조사를 시킨 뒤 결과를 항목에 보강한다.
   지식 산출물과 `docs/`의 체계 문서는 편집하지 않는다.
3. **승인 (유저)**: 구체화된 반영 계획을 검토하고 `status: approved`로 고친다.
4. **반영 (담당 역할)**: 승인된 항목만, 반영 계획대로 담당 write plane의 역할이
   반영한다 (결정은 orchestrator, 산출물은 developer). 반영 후 `bazel test //...`
   PASS 확인, 항목에 반영 결과(무엇을 어디에)를 기록한다.
5. **refresh (hci)**: `approved`이고 반영 결과가 기록된 항목만 제거한다. 반영 흔적은
   지식 산출물과 git 이력이 기록이다 — 채널에 사본을 남기지 않는다.
