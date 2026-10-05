---
id: https://agentic-knowledge-base.dev/id/chunk/b86f5506-c32e-4bd3-b755-14fb39817028
type: artifact
level: executable
title_ko: 해시 고정된 prov-o.ttl·skos.rdf가 페치되고 온톨로지·그래프의 prov·skos 용어가 원문 대조를 통과한다
title: The hash-pinned prov-o.ttl and skos.rdf are fetched and every prov and skos term in the ontology and graphs passes the source check
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/6280e8fa-8289-458a-a3c1-9ededacd2478]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 해시 고정된 외부 입력 둘과 그 원문을 쓰는 게이트 둘을 자극으로 쓴다.

**자극** — `MODULE.bazel`의 `http_file` 둘이다. 검사 대상 그래프는 `//kb/ontology:gate_test`의 온톨로지 모듈·shape와 `//kg:gate_test`의 head·시드·참조·ODD 그래프다. 음성 표본은 서술로만 둔다.

```yaml
prov_o:   {file: prov-o.ttl, sha256: 7d203989…79a96, url: https://www.w3.org/ns/prov-o.ttl}
skos:     {file: skos.rdf,   sha256: e79633b8…9dd6,  url: https://www.w3.org/2009/08/skos-reference/skos.rdf}
negative: {term: skos:defnition}   # 서술 표본 — 접두어는 맞고 원문에 없는 오타
```

**기대** — `bazel build @prov_o//file @skos//file`이 성공한다. 캐시된 원문의 해시가 선언과 같다. `//kb/ontology:gate_test`·`//kg:gate_test`가 PASS이고 출력에 `[vocab]`이 없다. 음성 표본은 `FAIL [vocab] … 표준 어휘 원문에 정의되지 않은 용어 http://www.w3.org/2004/02/skos/core#defnition` 한 줄로 끝난다.

**실행 명령** — `bazel build @prov_o//file @skos//file && bazel test //kb/ontology:gate_test //kg:gate_test`

**판정 범위** — 외부 입력 중 원문 대조까지 있는 것은 표준 어휘 둘뿐이라 이 둘이 버전 고정의 전 분기(선언·해시·실재)를 덮는다. pip 잠금은 해시 고정의 같은 분기라 표본을 늘리지 않는다. 오타 표본은 접두어 검사가 통과시키는 값이라 원문 대조만이 잡는다는 것을 보인다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p11-inputs-as-versioned-vocabulary` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
