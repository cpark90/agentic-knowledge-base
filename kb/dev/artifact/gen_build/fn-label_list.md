---
id: https://agentic-knowledge-base.dev/id/chunk/0f0f082a-c9cd-454c-ab65-ca4f3bebc461
type: artifact
level: executable
title_ko: 함수 label_list (tools/gen_build.py)
title: function label_list in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42]
part_of: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd
---
**함수** — `label_list(name, labels, indent)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_list(name, labels, indent="    "):
    if not labels:
        return ""
    return f"{indent}{name} = [\n" + "".join(f"{indent}    {q(l)},\n" for l in sorted(labels)) + f"{indent}],\n"
```
<!-- 인용 끝 -->
