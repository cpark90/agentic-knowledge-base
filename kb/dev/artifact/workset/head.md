---
id: https://agentic-knowledge-base.dev/id/chunk/58ca0301-520d-4ec2-848b-bfea07859eab
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/workset.py)
title: module head agt in tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c, https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320]
part_of: https://agentic-knowledge-base.dev/id/composite/daba0b21-4c2e-4be6-8cc6-9cef10baa82f
---
**모듈 머리** — `tools/workset.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
ID = Namespace("https://agentic-knowledge-base.dev/id/")
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
# 이웃 링크의 족 — 표의 순서가 곧 펼침 우선순위. supersedes 는 족 밖의 시간축이라 맨 뒤 (kb/ontology/related/trace)
FAMILIES = [
    ("refs", [AGT.cites, AGT.targets]),
    ("dep", [AGT.refines, AGT.serves, AGT.satisfies, AGT.constrains, AGT.verifies, AGT.usesConcept, AGT.derivesFrom, AGT.allocates]),
    ("part", [AGT.hasDirectPart]),
    ("rel", [AGT.coUpdatesWith, AGT.conflictsWith, AGT.overlapsWith]),
    ("time", [AGT.supersedes]),
]
FAMILY_OF = {p: (i + 1, tag) for i, (tag, ps) in enumerate(FAMILIES) for p in ps}
PART = FAMILY_OF[AGT.hasDirectPart]
# 펼친 항목 하나가 본문 앞에 더하는 비-본문 줄 수(빈 줄·제목·iri 주석) — 예산 검사식과 회계식이
# 같은 값을 써야 한다. 둘이 갈리면(검사 +2, 회계 +3) 검사를 통과한 항목이 회계에서 예산을 넘길 수 있다
ENTRY_OVERHEAD = 3
```
<!-- 인용 끝 -->
