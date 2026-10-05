---
id: https://agentic-knowledge-base.dev/id/chunk/3e0a2fd1-776d-4762-b6e5-538b8cd4987d
type: artifact
level: executable
title_ko: 함수 code_part (tools/kb_lib.py)
title: function code_part in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a228d4f1-cdb8-4a79-bd48-f9b961eaa607
---
**함수** — `code_part(location, is_part)` 다. 추출 트리(`EXTRACT_ROOT`) 안에서 복합체의 부분인 청크인가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def code_part(location: str, is_part: bool) -> bool:
    """추출 트리(`EXTRACT_ROOT`) 안에서 복합체의 부분인 청크인가. 파일 청크는 복합체를 선언할 뿐 부분이 아니므로 거짓이다."""
    return is_part and location.startswith(EXTRACT_ROOT + "/")
```
<!-- 인용 끝 -->
