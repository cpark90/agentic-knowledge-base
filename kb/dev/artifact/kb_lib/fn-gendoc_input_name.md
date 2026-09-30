---
id: https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20
type: artifact
level: executable
title_ko: 함수 gendoc_input_name (tools/kb_lib.py)
title: function gendoc_input_name in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `gendoc_input_name(path)` 다. 입력 파일의 표기 — 샌드박스의 bazel-out·external 접두를 떼어 워크스페이스 상대 경로로 보인다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_input_name(path: str) -> str:
    """입력 파일의 표기 — 샌드박스의 bazel-out·external 접두를 떼어 워크스페이스 상대 경로로 보인다."""
    return _GENDOC_BAZEL_OUT.sub("", str(path).replace(os.sep, "/"))
```
<!-- 인용 끝 -->
