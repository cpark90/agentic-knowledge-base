---
id: https://agentic-knowledge-base.dev/id/chunk/13568c50-9137-4cc7-82ab-dc6e233c5bcc
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/community.py)
title: module head agt in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/822db955-483e-47ed-ad68-fec783bc825b]
part_of: https://agentic-knowledge-base.dev/id/composite/0ef43353-941b-4b48-b8b1-2ef9a8eacf53
---
**모듈 머리** — `tools/community.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
# 군집 계산에 쓰는 링크 종류 (족: references · semanticallyDependsOn · relatedTo). 시간축 supersedes 는 뺀다
EDGE_KINDS = [AGT.refines, AGT.serves, AGT.cites, AGT.usesConcept, AGT.coUpdatesWith, AGT.conflictsWith, AGT.overlapsWith]
MAX_PARTS = 9  # 복합체 부분 상한 (7±2, composite-kg 배너)
```
<!-- 인용 끝 -->
