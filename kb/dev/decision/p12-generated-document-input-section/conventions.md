---
id: https://agentic-knowledge-base.dev/id/chunk/292023ed-ef9e-4c56-9c12-36d37abce90a
type: decision
level: concrete
title_ko: 규범 문서 규약 — 입력이 많은 생성 문서는 목록을 입력 파일 절로 접고 트리플 수에 union 구성을 붙인다
title: Normative-document conventions — A generated document with many inputs folds the list into an input file section and states the union behind its triple count
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:15:22+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/77024f86-3aeb-445d-ad01-6a1bcd9eee54
---
**규약** — `p12-generated-document-input-section`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 머리 `입력` 줄의 형태는 입력 파일 수로 갈린다. 여섯 이하면 파일 목록·지문·규모를 적는다. 일곱 이상이면 개수·지문·규모·`## 입력 파일` 절로의 링크를 적고, 문서 끝의 `## 입력 파일` 절에 파일 전부를 디렉토리로 묶어 적는다. 목록을 생략하지 않는다(G4). 규모 자리의 트리플 수에는 **union 구성**을 함께 적는다(`트리플 <n> (union: chunks +a · base +b · …)`). 구성원마다 붙는 수는 선언 순서대로 앞 구성원들의 합집합에 더한 증분이고, 증분의 합이 총수와 다르거나 증분 없는 옛 표기를 쓴 줄은 G4가 FAIL로 낸다(유저 답 Q40-a, 2026-10-04). 같은 이름의 수치가 도구마다 갈리는 이유가 문서 안에 있어야 한다(현상 `agt:metricVariesByLoadingOption`, 2026-09-29).
