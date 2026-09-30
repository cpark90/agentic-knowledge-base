---
id: https://agentic-knowledge-base.dev/id/chunk/454b2f0a-c75b-42fd-aad2-d24b00a2eb3b
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/choices.py)
title: module head agt in tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/7c9d74e6-1a77-4d52-a126-644a65bfab93]
part_of: https://agentic-knowledge-base.dev/id/composite/020b2093-af80-4cce-8bce-86ac125c1c4a
---
**모듈 머리** — `tools/choices.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = kb_lib.AGT
QUOTE = kb_lib.GENDOC_QUOTE_LINE  # 라벨은 그래프에서 그대로 가져온 값이다 — 생성기가 고쳐 쓰지 않는다
# 링크 상태 → 체크 표시 (p9-candidate-storage 13.5절). 상태의 정의처는 kb_lib.SPACE_STATE_LINK 다
MARK = {kb_lib.LINK_STATE_CANDIDATE: "[ ]", kb_lib.LINK_STATE_INVALID: "[-]", kb_lib.LINK_STATE_CONFIRMED: "[x]"}
```
<!-- 인용 끝 -->
