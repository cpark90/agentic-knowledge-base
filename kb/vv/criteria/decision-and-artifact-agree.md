---
id: https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee
type: contract
level: abstract
title_ko: 결정 결론의 내용 해시가 바뀌면 그것을 충족하는 링크가 재판정 대상이 된다
title: When the content hash of a decision conclusion changes, the links that satisfy it become re-judgement targets
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-10-01T01:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a]
---
**합격 기준** — 기준 종류는 불변식이다. 결정 결론 `d`의 `agt:contentHash`가 리비전 사이에 바뀌었으면 `d`를 대상으로 하는 확정 링크 전부가 `suspect`로 유도되거나 재판정 기록을 갖는 것이 합격이다.

**판정식**

- 실행. `bazel run //tools:revalidate -- --base <리비전>`이 본문 해시가 바뀐 청크마다 재판정 대상 링크 개체의 표를 내고 그 표의 `유도 상태` 열이 `suspect`다. 링크 IRI를 `chunk2kg`와 같은 함수로 계산하므로 표의 한 줄이 그래프의 한 개체다.
- 음성. 바뀐 끝이 결정 결론인 행이 `suspect`를 얻지 못하면 불합격이다. 실측 2026-10-01에 base `HEAD~1`은 변경 청크 21 · 재판정 대상 160 · 링크 개체 30(`verifies` 1)을 낸다.
- base `HEAD~4`는 663 · 4771 · 518(`refines` 516 · `supersedes` 1 · `verifies` 1)을 낸다. 두 창 모두 결정 결론의 본문 변경이 0건이라 판정 대상 행이 없고 판정은 **공허 합격**이다.
- 양성. 본문 해시 변경 일반에 대해 같은 표가 30행과 518행을 `suspect`로 물질화하므로 수단은 동작한다. 상태는 저장값이 아니라 이 실행의 평가 결과다.
- 라벨 쪽은 현상 `agt:labelRot`(P14)이다. 라벨이 본문을 대표하는지는 세션 판정자 질문 `agt:labelRepresentsBody`의 값 분포로 재고, 값 1(낱말이 본문에 있으나 소재만 가리킨다)이 라벨 부패의 표지다.
- 그 첫 측정은 2026-09-30이다. 실표본 60건 중 값 1을 받은 항목이 6 = 10.0%(판정자 a 6 · b 4, 양쪽 모두 1인 항목 4)이고 값 일치는 58/60 = 96.7%이며 값 2를 받은 미끼는 0/10이다.

**등급** — B다. `revalidate`가 링크 재판정 후보를 수로 내고 판정 로그가 라벨 값의 분포를 수로 낸다. A가 아닌 까닭은 `revalidate`가 `git`·`bazel query`를 불러 테스트 타깃이 아니고 판정자의 값이 게이트 밖이라는 것이다.

미확정: 결정 결론의 본문이 바뀐 리비전 창. 최근 네 리비전이 전부 코드 청크 갱신이라 공허 합격을 벗어나는 표본이 아직 없다.
