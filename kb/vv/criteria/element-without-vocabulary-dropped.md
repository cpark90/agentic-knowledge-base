---
id: https://agentic-knowledge-base.dev/id/chunk/4e216613-6a9b-40a2-8c31-d3a13fae72ae
type: contract
level: logical
title_ko: 소스 요소 집합과 방출 요소 집합의 차는 0이고 어휘를 베낀 표는 온톨로지와 같은 집합이다
title: The difference between the source and emitted element sets is zero and the copied vocabulary table equals the ontology set
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b055c55f-c77b-421f-8cc0-d1e832f7b207]
---
**합격 기준** — 기준 종류는 **전수 대조**다. 소스 요소 집합 `K`와 방출기가 소비하는 요소 집합 `C`에 대해 `K \ C = ∅`이고, 어휘를 베낀 표의 치역 `T`와 온톨로지가 정의한 집합 `O`에 대해 `O = T`인 것이 합격이다. 허용되는 차는 없다.

**판정식**

- 대조 1(frontmatter 키). `K`는 `kb/**/*.md`의 최상위 frontmatter 키 집합이고 `C`는 `chunk2kg`의 `REQUIRED ∪ LINK_KEYS`에 선택 키 열하나를 더한 집합이다. 실측 2026-09-29에 `|K| = 23` · `|C| = 28` · `K \ C = ∅`이다.
- 대조 2(실체 표). `O`는 `kb/ontology/profile/development/plane-substance-ontology.ttl`이 `a owl:Class`로 선언한 IRI 집합이고 `T`는 `chunk2kg.PROFILE_SUBSTANCE`의 치역이다. 실측에 `|O| = |T| = 7`이고 양방향 차가 공집합이다.
- 음성. 온톨로지에 실체 클래스를 하나 더하고 표를 고치지 않으면 `O \ T`가 1이 되고 대조 2가 불합격이다. frontmatter에 알려지지 않은 키를 하나 넣으면 `K \ C`가 1이 되고 대조 1이 불합격이다. 두 음성 모두 지금은 어느 게이트도 내지 않는다.
- 양성. 두 차가 모두 공집합이고 `bazel test //...`가 PASS다. 로드 시점 `assert`는 `PLANE_CLASS`와 `PLANES`만 보고 `PROFILE_SUBSTANCE`와 온톨로지는 보지 않으므로 이 대조가 그 자리를 덮는다.

**등급** — B다. 두 대조가 전부 기계 판정이고 값이 지금 나온다. A가 아닌 까닭은 대조가 게이트 안이 아니라 검증기 밖의 스크립트이고, 도구가 서면 A로 올라간다.

미확정: 대조를 게이트로 올릴 자리가 `validate.py`의 새 검사인지 `chunk_lint`의 검사인지 정해지지 않았다.
