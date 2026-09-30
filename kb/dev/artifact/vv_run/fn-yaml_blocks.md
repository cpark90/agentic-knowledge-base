---
id: https://agentic-knowledge-base.dev/id/chunk/f1c79e23-8146-427e-83da-3d62ae01bb20
type: artifact
level: executable
title_ko: 함수 yaml_blocks (tools/vv_run.py)
title: function yaml_blocks in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `yaml_blocks(body)` 다. 본문의 언어 태그 `yaml` 인 펜스 내용 목록 — 다른 언어의 펜스는 건드리지 않는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def yaml_blocks(body: str) -> list[str]:
    """본문의 언어 태그 `yaml` 인 펜스 내용 목록 — 다른 언어의 펜스는 건드리지 않는다 (space2kg 와 같은 스캐너)."""
    out, cur, fence, tag = [], None, None, ""
    for line in body.split("\n"):
        m = kb_lib.MD_FENCE.match(line)
        if fence is None:
            if m:
                fence, tag, cur = m.group(1), line.strip()[len(m.group(1)):].strip(), []
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            if tag == "yaml":
                out.append("\n".join(cur))
            fence, cur = None, None
            continue
        cur.append(line)
    return out
```
<!-- 인용 끝 -->
