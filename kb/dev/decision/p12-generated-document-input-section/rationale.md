---
id: https://agentic-knowledge-base.dev/id/chunk/9833c08e-fc1a-466f-a6ff-2016a58560ef
type: decision
level: logical
title_ko: 긴 입력 목록은 머리를 덮고 union 구성이 없으면 트리플 수의 차이가 결함인지 구성 차이인지 가려지지 않는다
title: A long input list buries the header, and without the union composition a triple-count difference cannot be told apart as a defect or a composition change
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:15:22+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/77024f86-3aeb-445d-ad01-6a1bcd9eee54
---
**근거** — 입력 목록 절과 union 구성은 원인이 다르다.

- **입력 파일 절**(2026-09-22, 게이트 `gendoc` 도입과 같은 날): 머리 블록은 여섯 줄의 고정 순서다. 그래프 파일 수십 개를 한 줄에 늘어놓으면 머리가 본문을 덮는다. 개수만 적으면 어느 파일이 들어갔는지 판별되지 않는다. 절로 접고 디렉토리로 묶으면 둘을 함께 얻는다(`kb_lib.gendoc_inputs_section` docstring).
- **union 구성**(2026-09-29, `kb_lib` 주석의 vnv 설계): 같은 이름의 수치가 도구마다 갈리는 현상의 관측 수단이다.

2026-09-19 실측에서 같은 커밋의 트리플 수가 세 값이었다(`metrics` 20418 · `link-candidates` 20361 · `cq`와 weave 넷 21223). 셋은 union 구성이 달랐고 문서만 보고 결함인지 구성 차이인지 가릴 수 없었다. 결함 요인 온톨로지가 이 현상을 `agt:metricVariesByLoadingOption`으로 등록했다.

실측(2026-10-03)에서 `STYLEGUIDE.md` §9는 경계를 "일곱을 넘으면"으로 적었다. 코드의 상한 6은 일곱부터 접는다. 둘이 파일 일곱 개에서 갈렸다. 유저 답 Q6-a(2026-10-03)가 문서를 코드에 맞추기로 정했다. 경계는 "일곱 이상"이다.

2026-10-04 실측에서 도구 사이 트리플 수가 다시 갈렸다(metrics 72,133 · link-candidates 70,355 · audit 72,509). 차는 union 구성원을 선언 순서대로 더한 증분과 정확히 맞았다 — 376은 gates의 증분이다. 구성원 이름만으로는 이 차를 문서 안에서 셈할 수 없다. 구성원 크기는 중복 때문에 단순히 더해지지 않으므로 적을 수는 크기가 아니라 증분이다. 유저 답 Q40-a(2026-10-04)가 `입력` 줄을 증분 표기로 넓히기로 정했다. 구현 뒤 실측은 metrics `트리플 75046 (union: chunks +70531 · base +198 · catalog +116 · composite +0 · references +2404 · odd +71 · ontology +1726)`이고, audit은 같은 열에 `gates +376`이 붙어 차 376이 gates 증분으로 문서 안에서 읽힌다.
