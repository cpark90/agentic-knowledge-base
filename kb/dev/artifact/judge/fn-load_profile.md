---
id: https://agentic-knowledge-base.dev/id/chunk/473ab4af-5806-45ea-a923-d7f635544fdb
type: artifact
level: executable
title_ko: 함수 load_profile (tools/judge.py)
title: function load_profile in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `load_profile(root, profile, shapes)` 다. 프로파일 온톨로지 모듈과 판정 질문 shape 를 한 그래프로 읽는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_profile(root: Path, profile: str, shapes: str) -> Graph:
    """프로파일 온톨로지 모듈과 판정 질문 shape 를 한 그래프로 읽는다."""
    try:
        return kb_lib.judge_load_profile(root, profile, shapes)
    except ValueError as e:
        raise JudgeError(str(e))
```
<!-- 인용 끝 -->
