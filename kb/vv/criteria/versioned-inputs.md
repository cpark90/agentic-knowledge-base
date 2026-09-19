---
id: https://agentic-knowledge-base.dev/id/chunk/6280e8fa-8289-458a-a3c1-9ededacd2478
type: contract
level: logical
title_ko: 표준 어휘 원문은 해시가 맞을 때만 들어오고 쓰인 표준 용어는 전부 원문에 실재한다
title: A standard vocabulary source enters only when its hash matches and every standard term used exists in that source
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/55f7ac49-6b7a-4b63-a02d-b2566f69b562]
---
**합격 기준** — 기준 종류는 **명세 대조**다. 입력마다 `선언(MODULE.bazel·lock) ∧ 버전 고정(sha256·==)`이 성립하고, 데이터가 쓴 표준 용어 집합은 고정된 원문의 정의 집합에 포함된다.

**판정식**

- 음성(해시): `http_file`의 `sha256`을 한 자리 바꾸면 `bazel build @prov_o//file`이 `Checksum was … but wanted …` 문구로 실패한다.
- 음성(용어): `prov:`·`skos:` 접두어이되 원문에 없는 용어를 쓴 그래프는 `FAIL [vocab] <경로>: 표준 어휘 원문에 정의되지 않은 용어 <IRI> (--standard-vocab 기준)`로 끝난다.
- 양성: `bazel build @prov_o//file @skos//file`이 성공하고 `bazel test //kb/ontology:gate_test //kg:gate_test`가 PASS다. 두 게이트 모두 `standard_vocab = ["@prov_o//file", "@skos//file"]`을 받는다.

**등급** — B다. 판정은 기계가 하되 원문 적재와 검사의 실행 비용이 있다.

기준의 대상은 `MODULE.bazel`의 외부 입력 전부(표준 어휘 원문·pip 잠금)이고 판정의 원본은 Bazel의 `http_file` 검증과 `tools/validate.py`의 `load_standard_vocab`·`check_standard_vocab`이다. 열다섯 입력의 목록 자체는 결정 `p11-inputs-are-parameters`의 몫이다.
