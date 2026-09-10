---
id: https://agentic-knowledge-base.dev/id/chunk/8e8285e0-77f0-456b-8601-8ecc104585e2
type: decision
level: concrete
title_ko: 네 전이 게이트가 상위 단계에 진 빚을 묻는다
title: Four transition gates ask what each level owes the level above
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
part_of: https://agentic-knowledge-base.dev/id/composite/7daf868e-e331-4e89-bbcc-447c0ce05f29
composite: {id: https://agentic-knowledge-base.dev/id/composite/7daf868e-e331-4e89-bbcc-447c0ce05f29, title_ko: 전이 게이트, title: Transition gates}
---
**결론** — 6.2절 정제의 각 전이는 게이트를 통과해야 한다. 네 게이트 전부가 **"이 단계가 상위 단계에 무엇을 빚지고 있는가"** 를 묻는다.

- **functional → abstract** — 형식 문장이 온톨로지 어휘만 사용하고, 어느 요구의 어느 관심사에 기여하는지 `refines`로 명시. 기여 없는 설계는 거부 → 요구 추가 또는 설계 기각
- **abstract → logical** — 모든 변수에 범위와 제약, 합격 기준에 판정식. 판정식 없는 기준은 abstract로 강등 → 판정식 작성 대기
- **logical → concrete** — 후보가 하나 남고 배제 근거가 청크로 존재, **표본 추출 근거**(등가분할·경계값·조합) 명시. 근거 없는 값 할당 금지 → 대기·유저 피드백
- **concrete → executable** — plane 판정 도구 통과(5.4절)와 `refines` 존재, **검증 역할 청크가 logical 기준을 `verifies`로 바인딩.** 기준 없는 `verifies`는 거부 → 수정 또는 검증 청크 추가

**게이트를 통과하지 않은 전이는 `refines` 링크를 만들 수 없다.**
