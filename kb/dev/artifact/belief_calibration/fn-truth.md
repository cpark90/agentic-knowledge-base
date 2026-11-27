---
id: https://agentic-knowledge-base.dev/id/chunk/f1ef7fed-44fb-45ef-bc75-8f33101fc8cb
type: artifact
level: executable
title_ko: 함수 truth (tools/belief_calibration.py)
title: function truth in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `truth(v)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def truth(v) -> str:
    return kb_lib.NONE_MARK if v is None else ("참" if v else "거짓")
```
<!-- 인용 끝 -->
