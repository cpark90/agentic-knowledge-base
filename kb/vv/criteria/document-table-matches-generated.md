---
id: https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407
type: contract
level: logical
title_ko: 문서가 적은 수치는 같은 이름의 생성물 수치와 같아야 한다
title: A number written in a document must equal the same-named number in the generated view
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-04T20:18:20+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:23+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0]
---
**합격 기준** — 기준 종류는 불변식이다. 문서 `f`가 적은 수치 `v`에 대해 같은 이름의 생성물 수치 `g(v)`가 있으면 `v = g(v)` 이고, 없으면 `f`가 그 수치의 생성 명령이나 시각을 함께 적는 것이 합격이다.

**확인 절차**

- 생성물을 먼저 낸다. `bazel build //kg:metrics //kg:audit //kg:link_candidates` 뒤 `bazel-bin/kg/`의 세 문서가 값의 원본이다.
- 대조 대상 문서는 진입점 넷이다 — `docs/roadmap.md` · `docs/rules.md` · `docs/method.md` · `docs/tools.md`.
- 대조 대상 이름은 생성물이 내는 열이다 — 살아 있는 청크 · 고아율 · 연결 성분 · 매트릭스 채움 · CQ19 · CQ20 · 링크 개체 · 확정 링크의 구축·복원 내역 · 복원 비율 · 후보 링크 · `cites` · `usesConcept` · 확정 문장 커버리지 · 테스트 수.
- 이름마다 문서의 값과 생성물의 값을 한 쌍으로 적고 어긋난 쌍을 센다. 고칠 것은 문서다. 생성물은 뷰이고 원본은 그래프다.
- 시점을 선언한 스냅샷 절은 대조 밖이다 — `docs/roadmap.md`의 2026-09-11 블록은 생성 명령 대신 시각을 적어 기준의 둘째 절을 만족한다.
- 실측 2026-10-01: 대조 쌍 열여섯 중 어긋난 쌍이 열이라 지금은 **불합격**이다. 맞은 쌍 여섯은 고아율 0% · 연결 성분 1 · CQ19 64.5% · CQ20 100% · 확정 문장 커버리지 148/148 · 테스트 71이다.
- 어긋난 쌍 다섯이 `docs/roadmap.md`에 있다 — 복원 링크 29 대 66 · 복원 비율 3.8% 대 5.3% · 후보 11 대 30 · `cites` 30 대 36 · `usesConcept` 136 대 601이다.
- 나머지 다섯은 `docs/tools.md`의 넷(확정 링크 577 대 1241 · 구축 548 대 1175 · 복원 29 대 66 · 후보 링크 30 대 36)과 `docs/rules.md`의 하나(링크 개체 472 대 1277)다.
- 그 뒤 orchestrator가 어긋난 쌍의 수치를 생성 명령 인용으로 바꿨다. 둘째 실측(`python3 tools/doccheck.py --report`)은 대조 쌍 7 · 어긋난 쌍 0을 낸다. 첫 실측의 수치는 판정 이력이라 지우지 않는다.

**등급** — B다. 생성물 쪽 값이 한 명령으로 나오고 대조 대상이 문서 넷과 이름 열넷으로 닫혀 있다. A가 아닌 까닭은 이름의 짝짓기가 사람의 대조이고 `doccheck`는 링크·앵커·문체만 본다는 것이다. 케이스 [`document-table-matches-generated`](../case/document-table-matches-generated.md)가 선 뒤에도 등급은 B에 머문다 — `--report`는 설계상 상시 종료 0인 보고 모드라 `bazel test //...`의 게이트가 아니고, 등급 A는 사람 해석 없는 게이트 판정을 요구한다.

미확정: 이름의 짝을 기계가 맺는 표기. 문서가 수치 옆에 생성 타깃의 이름을 적는 규약이 서면 이 대조가 게이트로 올라간다.
