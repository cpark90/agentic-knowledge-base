---
id: https://agentic-knowledge-base.dev/id/chunk/55f7ac49-6b7a-4b63-a02d-b2566f69b562
type: requirement
level: functional
pattern: ubiquitous
title_ko: 체계 밖에서 오는 입력은 선언되고 버전이 고정되어야 한다
title: An input from outside the system must be declared and pinned to a version
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
---
**검증 목표** — 입력을 온톨로지 어휘로 쓰고 ODD와 같은 방식으로 버전 관리한다는 결정이 빌드 입력의 해시 고정과 실재 검사로 강제된다는 것이 보여져야 한다. 표준 어휘 원문과 파이썬 의존은 선언된 버전으로만 들어온다.

- **이해관계자**: 업체 · 운영 역할 · **관심사**: 재구성 가능성

**무엇을 관측하면 성립하는가**

- 표준 어휘 원문(PROV-O·SKOS)은 `MODULE.bazel`의 `http_file`이 `sha256`으로 고정해 가져오고, 해시가 다르면 페치가 실패한다.
- 데이터·온톨로지가 쓴 `prov:`·`skos:` 용어가 그 원문에 실재하지 않으면 `FAIL [vocab]`로 거부된다.
- 파이썬 의존은 `tools/requirements_lock.txt`의 고정 버전(`PyYAML==6.0.2` 등)으로만 해석되고 `MODULE.bazel.lock`이 해시를 적는다.
- 에이전트 카탈로그의 역할·실행 모드는 `kg/catalog-kg.ttl`의 온톨로지 어휘로 쓰이고 `//kg:gate_test`의 `catalog` 검사를 통과한다.

판정의 원본은 `MODULE.bazel`·`tools/requirements_lock.txt`와 `tools/validate.py`의 `check_standard_vocab`이다.
