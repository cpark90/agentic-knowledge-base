---
id: https://agentic-knowledge-base.dev/id/chunk/5bbe9743-feb1-4ec4-8678-c5b66eb40f83
type: artifact
level: executable
title_ko: 함수 core_root (tools/kb_lib.py)
title: function core_root in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb
---
**함수** — `core_root()` 다. 이 모듈의 코어 뿌리 — 이 파일(`<뿌리>/tools/kb_lib.py`)의 두 단계 위다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def core_root() -> Path:
    """이 모듈의 코어 뿌리 — 이 파일(`<뿌리>/tools/kb_lib.py`)의 두 단계 위다 (task 0327 손질 5).

    심볼릭 링크를 풀지 않는다. runfiles 에서 풀지 않은 경로는 `<runfiles>/<이 모듈의 canonical 이름>/` 이고 거기에는 타깃의
    `data` 로 선언된 코어 파일만 있다. 의존 저장소에서 `bazel run @agentic_knowledge_base//tools:query` 로 돌려도 이 뿌리는
    이 모듈을 가리키고, 호출 저장소의 작업 트리(`BUILD_WORKSPACE_DIRECTORY`)는 가리키지 않는다.
    """
    return Path(__file__).absolute().parent.parent
```
<!-- 인용 끝 -->
