---
from: hci
status: approved
targets: [kb/dev/decision/p8-mismatch-attribution/conclusion.md, kb/dev/decision/p6-executable-splits-by-kb/conclusion.md, kb/dev/decision/p8-vv-roles/rationale.md, kb/dev/decision/p8-vv-roles/alternatives.md, kb/dev/decision/p8-pass-criteria/conclusion.md, kb/dev/decision/p8-vv-roles/conclusion.md, tools/consistency.py, docs/glossary.md]
---

# 영문 라벨에 한글이 섞였다 — 용어 치환의 부작용 6건 (2026-09-12)

## 질문

`verifier → 검증기` 치환이 **영문 라벨(`title`)에도 적용**되어 영문 라벨 6개에 한글이 박혔다. 언어 정책은
"산문·정의는 한글, 식별자·라벨(en)은 영어"(0.6절, STYLEGUIDE §0, AGENTS 언어 정책)다. 고치는 것은 기계적이지만,
**같은 일이 다시 일어나지 않게 하는 방법**은 정책 판단이다 — 게이트를 만들 것인가, 규약으로 둘 것인가.

## 이미 정해진 것

- 라벨은 한/영 1:1, 영문은 영어 (0.6절 표기 형식, `p0-notation-format`)
- 라벨이 청크의 인터페이스다 (`p4-label-is-the-interface`) — 라벨 오염은 인터페이스 오염이다
- 판정 가능한 규칙은 게이트로, 불가능한 것만 규약으로 (`tools.md` "게이트 밖")

## 현재 상태 (실측 2026-09-12)

| 파일 | 영문 라벨 |
|---|---|
| `p8-mismatch-attribution/conclusion` | Attributing a **검증기** failure is a decision, … |
| `p6-executable-splits-by-kb/conclusion` | Implementation and **검증기** live in different KBs |
| `p8-vv-roles/rationale` | Keeping gaps in the criteria from becoming gaps in the **검증기** |
| `p8-vv-roles/alternatives` | Rejecting a single author for criteria and **검증기** |
| `p8-pass-criteria/conclusion` | Pass criteria are chunks apart from the **검증기**, bound as link attributes |
| `p8-vv-roles/conclusion` | Five roles write to the V&V KB; criteria author and **검증기 저자** work in different sessions |

온톨로지 `@en` 라벨·정의문에는 오염이 없다(0건). 문서·채널에도 없다. 게이트가 못 잡은 이유: `validate` 의 labels 검사는
**온톨로지 용어**만 보고 청크 frontmatter 는 보지 않으며, `consistency` 는 라벨의 중복·형식만 보고 언어를 보지 않는다.

## 답이 가르는 것

- **게이트로 만들면** 이런 오염이 커밋 전에 걸리고, 규칙("영문 라벨에 한글 금지")이 기계 판정이 된다. 판정은 쉽다 — 정규식 하나.
  비용: 검사 하나 추가(`chunk2kg` 또는 `consistency` 어디에 둘지), 고유명사에 한글이 필요한 예외가 미래에 생기면 예외 처리.
- **규약으로 두면** 치환 도구를 쓸 때마다 사람이 확인해야 한다 — 이번에 놓친 경로다.

## 선택지

1. **`chunk2kg` 에 검사 추가**(권고) — frontmatter 검증에 "`title` 에 한글 금지, `title_ko` 에 라벨 전체가 영문만이면 경고"를
   넣는다. 생성기가 곧 검사기이므로 `bazel build //kg:chunks_kg` 에서 즉시 실패한다. 고침 6건은 developer/orchestrator dispatch.
2. **`consistency` 보고에 추가** — 게이트가 아니라 보고로만. 판정은 사람이 하되 놓치지는 않는다.
3. 규약으로만 — `STYLEGUIDE` 에 한 줄. 비용 0, 재발 가능.

어느 쪽이든 **6건의 정정**(검증기 → verifier)은 필요하다 — 담당 역할이 수행한다.

## 덧붙임 — 같은 소유자(`tools/`)에게: 채널 게이트의 과잉 검출

`tools/channel_lint.py` 의 반영 표지가 여는 괄호 + 역할 이름 형태를 통째로 잡는다. 그래서 채널 안에서 정상인
**서명**(답 절 제목에 역할과 날짜를 괄호로 적는 관례)까지 FAIL 이 된다 (2026-09-12 실측 — 이 항목과 agents 항목 둘 다 걸렸다).
표지를 "반영/수행했다"는 **서술**로 좁히는 편이 맞다. 검사 약화가 아니라 대상 명확화다.

## 답

**유저(2026-09-12): "1,3"** — 선택지 1(`chunk2kg` 에 라벨 언어 검사 추가)과 3(STYLEGUIDE 한 줄) 둘 다.
게이트와 규약을 함께 둔다 — 기계가 잡되 저작 시점에도 읽히게.

담당 역할이 수행할 것:
1. `tools/chunk2kg.py` frontmatter 검증에 "`title` 에 한글 금지" 추가 (생성기가 곧 검사기 — `//kg:chunks_kg` 에서 실패)
2. `STYLEGUIDE.md` 언어 규칙에 "영문 라벨(`title`)에 한글을 섞지 않는다 — 용어 치환 시 한글 필드만 대상" 한 줄
3. 오염 6건 정정 (`검증기` → `verifier`): 위 `targets` 의 앞 6개
4. 덧붙임의 `channel_lint` 표지 완화 (같은 소유자)
