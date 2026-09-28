---
id: https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407
type: contract
level: abstract
title_ko: 문서가 적은 수치는 같은 이름의 생성물 수치와 같아야 한다
title: A number written in a document must equal the same-named number in the generated view
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0]
---
**합격 기준** — 기준 종류는 불변식이다. 문서 `f`가 적은 수치 `v`에 대해 같은 이름의 생성물 수치 `g(v)`가 있으면 `v = g(v)` 이고, 없으면 `f`가 그 수치의 생성 명령을 함께 적는 것이 합격이다.

**확인 절차**

- 진입점 문서(`docs/roadmap.md` · `docs/rules.md` · `docs/method.md`)에서 비율·건수 표기를 뽑는다.
- 같은 이름의 수치를 `bazel build //kg:metrics //kg:audit //kb:consistency` 산출에서 찾아 값을 대조한다.
- 값이 다르면 불합격이고 고칠 것은 문서다. 생성물은 뷰이고 원본은 그래프다.
- 같은 이름의 수치를 내는 도구가 둘이면 문서가 어느 도구의 분모를 쓰는지 적었는지 본다. 적지 않았으면 불합격이다.

**등급** — C다. 수치 이름의 대조가 사람 판단이고 `doccheck` 는 링크·앵커·문체만 본다.

미확정: 대조의 단위가 표 셀인지 줄인지 정해지지 않았다. 단위가 서면 이 기준을 logical로 올리고 판정식을 쓴다.
