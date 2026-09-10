---
id: https://agentic-knowledge-base.dev/id/chunk/60faade0-d3e7-4ad4-8bf6-371be22956c3
type: decision
level: concrete
title_ko: 유저는 -space 리포트를 편집해 결정하고 그것이 유일한 UI 요구다
title: The user decides by editing the -space report, and that is the only UI requirement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0144]
part_of: https://agentic-knowledge-base.dev/id/composite/4458fad7-b74e-477f-816a-517940cebde2
composite: {id: https://agentic-knowledge-base.dev/id/composite/4458fad7-b74e-477f-816a-517940cebde2, title_ko: 사용자 피드백 루프와 -space 파일 형식, title: The user feedback loop and the -space file format}
---
**결론** — 유저는 적은 선택지 중 고르지 않는다. **리포트를 받고 거기에
피드백을 입력해 결정한다.** logical 단계의 `-space` 파일이 그대로 리포트이며,
체계가 그것을 **유저가 읽고 편집 가능한 형태로 노출**하는 것이 유일한 UI
요구다. **완결된 피드백만 채널을 통과한다.**

```
## 인증 방식                          [d-17-space]

배경: 외부 클라이언트가 존재하므로 API key는 배제됨.

후보 (남은 것 위주로 편집하세요)
  [x] OAuth2   — 운영 경험 있음
  [ ] mTLS     — 인증서 관리 부담
  [-] API key  — 배제됨 (외부 클라이언트)

메모:
```
