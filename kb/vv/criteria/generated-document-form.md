---
id: https://agentic-knowledge-base.dev/id/chunk/02fd5ecb-544d-434e-9146-96a0e3607851
type: contract
level: logical
title_ko: 생성 문서 전부가 G8~G15·G18 을 만족하고 빈 셀과 분모 없는 백분율은 gendoc 이 G14·G15 로 거부한다
title: Every generated document satisfies G8 to G15 and G18, and gendoc rejects empty cells and undenominated percentages under G14 and G15
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/37d2df45-7012-498f-9f5f-c3c3ef3e5e51]
---
**합격 기준** — 기준 종류는 **산출물 품질**이다. 뷰마다 `violations(check_gendoc, doc) = ∅` 이고, 규칙 집합은 G8·G9·G10·G11·G12·G13·G14·G15·G18 이며 인용 구역은 G10·G11·G14·G15·G18 을 면제한다. 비율은 전부 `kb_lib.pct` 를 거쳐 `n/d = p.p%` 꼴이다.

**판정식**

- 양성: `bazel test //:gendoc_test` 가 PASS 다. 케이스 `generated-document-provenance` 와 같은 게이트이되 판정 대상 규칙이 본문 쪽이다.
- 음성(빈 값): 대시 셀을 가진 표를 넣으면 ``FAIL [gendoc] <파일>:<줄>: G14 빈 표 셀 — 비우거나 대시를 쓰지 않고 `없음` 으로 적는다 (Microsoft Writing Style Guide, Tables)`` 로 끝난다.
- 음성(비율): `50%` 처럼 분모 없는 백분율은 ``G15 분모 없는 백분율 `50%` — `n/d = p.p%` 꼴로 적는다 (kb_lib.pct)`` 로 끝난다.
- 음성(게이트 밖): `gendoc_test` 의 `docs` 에 없는 생성 뷰는 검사되지 않는다. 뷰를 추가하면 `docs` 에도 추가해야 하고 그 누락은 이 기준이 잡지 못한다.

**등급** — A 다. 판정은 게이트 하나이고 사람 판단이 없다.

판정의 원본은 `tools/kb_lib.py` 의 `check_gendoc`(G8~G15·G18 절)·`GENDOC_QUOTE_EXEMPT`·`pct` 와 `BUILD.bazel` 의 `gendoc_test` 다. G16·G17 은 권장이라 게이트가 아니고 이 기준 밖이다.
