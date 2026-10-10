---
id: https://agentic-knowledge-base.dev/id/chunk/705eee66-ca6b-4c59-a89f-fbc929e08be4
type: agt:Space
level: logical
title_ko: 세션 교훈을 역할 메모리와 작업 메모리 중 어디에 두는가
title: Whether session lessons go to role memory or to working memory
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 요구 `r-020`은 시행착오를 memory plane에 두라고 한다. 세션 교훈은 `.claude/agent-memory/`(그래프 밖, 역할 메모리)에 있다. 결정 `p11-memory-promotion-rule`은 역할 메모리를 단기기억·장기기억 어느 쪽으로도 정하지 않는다. 그래서 새 세션 교훈의 자리가 둘로 갈린다. 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). 요구 `r-020`에서 세션 교훈의 자리를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 단기기억은 `memory` plane(작업 메모리)에 두고 첫 실행 시 한 번에 읽는다. 장기기억은 주제 plane으로 승격해 필요한 순간에 읽는다. 승격 규칙은 체계가 고정하지 않는 입력이다(`p11-memory-promotion-rule`). 이 결정의 결론은 head에서 이미 `r-020`을 `refines`하므로 후보로 들지 않고 관련 결정으로 적는다. 작업 메모리의 항목은 관측(실행 기록)이다(`p5-plane-by-verification`, `p0-run-is-an-append-only-memory-chunk`).

현재 상태(2026-10-09 실측) — 역할 메모리는 `.claude/agent-memory/hci/` 하나이고 파일 11개(색인 `MEMORY.md` 포함)다. 작업 메모리 `kb/dev/memory/`의 청크는 관측 3개다. 측정은 `find .claude/agent-memory -type f | wc -l`과 `find kb/dev/memory -name "*.md" | wc -l`이다.

답이 가르는 것 — 새 세션 교훈을 어디에 쓰는지와 그 교훈이 승격 규칙의 대상인 그래프 안에 있는지가 갈린다.

선택지 — A는 세션 교훈을 역할 메모리에 두는 현행 유지안이다(`p11-session-lessons-in-role-memory`). B는 세션 교훈을 작업 메모리에 두는 안이다(`p11-session-lessons-in-memory-plane`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/e45a0f86-ddc6-48ae-8b82-d710629e04ed
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/812a5dca-20bc-4adc-a1a5-5d14700e9420
    state: open
```
