---
id: https://agentic-knowledge-base.dev/id/chunk/e3dfa007-25f8-4aa0-9b65-c4124af23269
type: artifact
level: executable
title_ko: 함수 fail (tools/belief_calibration.py)
title: function fail in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/53c1af98-94eb-4b8d-81cf-9914292abca6
---
**함수** — `fail(msg)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def fail(msg: str) -> int:
    print(f"FAIL [belief-calibration] {msg}", file=sys.stderr)
    return kb_lib.EXIT_CONFIG
```
<!-- 인용 끝 -->
