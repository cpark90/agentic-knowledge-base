---
id: https://agentic-knowledge-base.dev/id/chunk/c321eb50-ec20-462b-b4cd-c1d3a46065a8
type: artifact
level: executable
title_ko: 함수 read_back (tools/case_gen.py)
title: function read_back in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32
---
**함수** — `read_back(lines)` 다. 펜스 줄 → vv_run 이 읽는 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def read_back(lines: list[str]):
    """펜스 줄 → vv_run 이 읽는 값. 펜스 안을 줄바꿈으로만 잇는 것(끝 줄바꿈 없음)이 vv_run.yaml_blocks 의 꼴이다."""
    try:
        return yaml.safe_load("\n".join(lines[1:-1]))
    except yaml.YAMLError:
        return None
```
<!-- 인용 끝 -->
