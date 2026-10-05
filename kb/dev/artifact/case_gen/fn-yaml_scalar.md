---
id: https://agentic-knowledge-base.dev/id/chunk/098b0459-1cbf-4bc0-8bad-a7a5f9cee7fc
type: artifact
level: executable
title_ko: 함수 yaml_scalar (tools/case_gen.py)
title: function yaml_scalar in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32
---
**함수** — `yaml_scalar(content, indent, block)` 다. 파일 내용 하나 → `이름:` 뒤의 YAML 값 줄.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def yaml_scalar(content: str, indent: str, block: bool) -> list[str]:
    """파일 내용 하나 → `이름:` 뒤의 YAML 값 줄. 줄이 여럿이면 literal 블록, 아니면 큰따옴표 한 줄(p8-machine-readable-case)."""
    if block and "\n" in content.rstrip("\n"):
        head = "|" if content.endswith("\n") and not content.endswith("\n\n") else "|-"
        return [head] + [f"{indent}  {ln}" if ln else "" for ln in content.rstrip("\n").split("\n")]
    return [json.dumps(content, ensure_ascii=False)]
```
<!-- 인용 끝 -->
