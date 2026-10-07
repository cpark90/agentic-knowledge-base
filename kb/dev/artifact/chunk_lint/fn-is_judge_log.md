---
id: https://agentic-knowledge-base.dev/id/chunk/608da358-1b32-4e5f-b999-82b185e41ef4
type: artifact
level: executable
title_ko: 함수 is_judge_log (tools/chunk_lint.py)
title: function is_judge_log in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3
---
**함수** — `is_judge_log(fields)` 다. 판정 로그인가 — 생성자가 판정자이고 plane 이 memory 인 청크 (kb/vv/run/judge-<UTC>.md).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def is_judge_log(fields: dict[str, str]) -> bool:
    """판정 로그인가 — 생성자가 판정자이고 plane 이 memory 인 청크 (kb/vv/run/judge-<UTC>.md).

    같은 생성자의 결과 주석(type: annotation)은 주석이라 대상이 아니다 — 그쪽은 review-comment-body-shapes 가 본다.
    """
    return fields.get("generated.by") == kb_lib.JUDGE_GENERATOR and fields.get("type") == "memory"
```
<!-- 인용 끝 -->
