---
id: https://agentic-knowledge-base.dev/id/chunk/f2618270-3e11-40c7-b5d0-36c828923ff0
type: contract
level: logical
title_ko: 온톨로지 밖 술어는 vocab 검사가 거부하고 커밋된 그래프의 술어는 전부 정의돼 있다
title: A predicate outside the ontology is rejected by the vocab check and every committed predicate is defined
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/50af6125-94e4-4d69-8181-df29db77451d]
---
**합격 기준** — 기준 종류는 **명세 대조**다. 데이터 그래프의 모든 술어 `p`에 대해 `p ∈ 온톨로지 정의 ∪ 등록 표준 어휘`가 성립한다. 명세는 `//kb/ontology:modules`의 정의와 `--standard-vocab`으로 등록된 원문이다.

**판정식**

- 음성(agt): `agt:` 네임스페이스이되 온톨로지에 없는 술어를 가진 데이터 그래프를 검사에 넣으면 `FAIL [vocab] <경로>: 온톨로지에 정의되지 않은 agt: 술어 <IRI>`로 끝난다.
- 음성(미등록): 등록되지 않은 네임스페이스의 술어는 `FAIL [vocab] <경로>: 미등록 어휘의 술어 <IRI>`로 끝난다.
- 음성(표준 오타): `prov:`·`skos:` 원문에 없는 용어는 `표준 어휘 원문에 정의되지 않은 용어`로 끝난다.
- 양성: `bazel test //kg:gate_test`가 PASS다. 입력은 head 그래프·시드 그래프·참조 그래프·ODD 그래프 전부다.

**등급** — B다. 판정은 기계가 하되 그래프 병합과 검사의 실행 비용이 있다.

기준의 대상은 `//kg:gate_test`의 `data`에 오르는 모든 그래프이고 판정의 원본은 `tools/validate.py`의 `check_vocab`·`check_standard_vocab`이다.
