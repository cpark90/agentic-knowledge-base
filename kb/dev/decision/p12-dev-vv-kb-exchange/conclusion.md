---
id: https://agentic-knowledge-base.dev/id/chunk/71c85a9d-e26c-4a98-be38-3af4656257aa
type: decision
level: concrete
title_ko: 테스트·검증은 활용이 아니라 두 번째 KB이고 활용 면에는 교환 목록만 남는다
title: Test and verification is a second KB, not a use; only the exchange list remains here
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0121]
part_of: https://agentic-knowledge-base.dev/id/composite/d8683edb-e683-4f3f-a6cc-fd448b724280
composite: {id: https://agentic-knowledge-base.dev/id/composite/d8683edb-e683-4f3f-a6cc-fd448b724280, title_ko: 개발 KB와 V&V KB의 교환 목록, title: What the development KB and the V&V KB exchange}
---
**결론** — 테스트·검증은 더 이상 활용 기능이 아니라 **두 번째 지식
베이스**다(Part VIII). 활용 관점에 남는 것은 두 KB가 주고받는 것의 목록이다.

| 개발 KB → V&V KB | V&V KB → 개발 KB |
|---|---|
| 요구 (검증 목표의 출처) | 결함 (요인 분류된 관측) |
| 결정·계약·산출물 (검증 대상) | 커버리지 (완주율·귀속률·공간 커버) |
| ODD (시나리오 변수의 분모) | 상승 후보 (요구·기준·결정·규칙) |
| 가정 (검증 경계) | 검증 상태 (`verifies` 링크의 valid/suspect) |

활용 기능 일반에 대해 체계는 **무엇을 받아 무엇을 하는지만** 적는다.
