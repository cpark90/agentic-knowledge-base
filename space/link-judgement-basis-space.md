---
id: https://agentic-knowledge-base.dev/id/chunk/db64a663-332e-4946-a633-0363daa5a283
type: agt:Space
level: logical
title_ko: 후보 링크를 확정으로 올리는 판단을 무엇으로 하는가
title: What grounds promoting a candidate link to confirmed
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 가능 집합인 후보에서 확정 링크로 넘어가는 순간 "이 둘이 실제로 이 관계에 있다"를 무엇을 근거로 말하는가가 변수다. 구축이면 만든 주체가 알므로 근거가 있다. 복원·후보 축소·유저 확정의 경우 근거의 종류와 강도, 그리고 확정 권한이 누구에게 있는가가 정해지지 않았다. 요구 `r-011`(근거 없는 할당은 불가능해야 한다)에서 이 확정 규칙으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 근거는 검사 가능성 순으로 구축 기록 > 동시 편집 이력 > 테스트 공동 커버 > 임베딩 > 같은 세션에서 읽음이고 임베딩은 후보 추림에만 쓴다(`p10-link-judgement-evidence`). 가능성은 확률이 아니라 가능/불가능 집합이다(`p9-possibility-as-feasible-set`). 후보 없음(모순)은 자동으로 풀지 않고 유저에게 넘긴다(`p9-contradiction-handling`). 임베딩 유사도를 확정 근거로 쓰는 것은 기각됐다(`p10-embedding-similarity-narrows-only`). 옛 설계 문서의 신뢰도 ω는 `p9-evidence-ledger`가 폐기하고 증거 기록(종류·참조·극성)으로 대체했다.

현재 상태(2026-10-06 실측, `bazel build //kg:metrics`) — 링크 개체는 1,128이다(확정 1,015 · 후보 113). 확정 중 구축은 937이고 복원은 78이다. 복원 78은 frontmatter `restored:` 표시로 확정됐고 증거에 `proposal`을 가진다. 이것이 구축이 아닌 확정 판단의 사례다. 후보 113은 본문 추출 참조(`cites` 96 · `satisfies` 17)이고 증거는 구축 기록이다. 미결을 적던 당시에는 링크가 0이었고 가장 가까운 판단 사례는 분해 감사가 `p3-out-of-odd-case-tagging`(옛 d-0067)을 옛 d-0008의 누락 보충으로 산문 판정한 것이었다. 그 근거는 같은 절 출처였다.

답이 가르는 것 — 확정을 에이전트가 할 수 있는지, 유저 확인이 필요한지가 갈린다. "후보를 좁히는 것은 자유, 근거 없이 하나를 할당하는 것은 금지"라는 균형점을 기계 규칙으로 어떻게 쓰는지가 갈린다.

선택지 — A는 근거 종류를 확정 권한으로 쓰는 안이다(`p10-confirm-authority-by-evidence-kind`). B는 제약 전파 결과 하나만 남으면 할당하는 안이다(`p10-sole-candidate-auto-confirm`). C는 항상 유저가 확정하는 안이고 링크 밀도가 낮게 유지되는 대가를 치른다(`p10-user-confirms-every-link`). 기존 결정은 세 선택지와 부분적으로만 겹친다. A는 근거 서열과 증거 종류를 갖지만(`p10-link-judgement-evidence`·`p9-evidence-ledger`) 서열을 권한에 묶지 않는다. B는 유일 후보의 확정 제안(`p9-evidence-ledger`)과 확인 후 승격(`p10-candidate-and-confirmed-link`)과 겹치지만 두 결정은 확인을 요구한다. C는 확정이 사람이 링크 키에 적는 행위라는 결정(`p10-extracted-references-are-candidates`)과 겹치지만 위임된 에이전트의 확인을 배제하지 않는다. 그래서 세 선택지를 새 후보로 세우고 셋 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/5e402e7b-631f-452c-a817-29372d4b60b9
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/8b49a388-065e-4c75-8728-2f81b9893ae3
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/b1abde45-d61e-4d5c-9fca-406efb6e8d3f
    state: open
```
