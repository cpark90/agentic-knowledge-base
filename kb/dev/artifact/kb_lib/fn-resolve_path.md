---
id: https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1
type: artifact
level: executable
title_ko: 함수 resolve_path (tools/kb_lib.py)
title: function resolve_path in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5bbe9743-feb1-4ec4-8678-c5b66eb40f83]
part_of: https://agentic-knowledge-base.dev/id/composite/0edbd7df-e79b-4b9f-b913-f8e16daf03ad
---
**함수** — `resolve_path(path, root)` 다. 워크스페이스 상대 경로를 runfiles(현재 디렉토리) → bazel-bin → 소스 → 이 모듈의 코어 순으로 찾는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve_path(path: str, root: Path) -> Path | None:
    """워크스페이스 상대 경로를 runfiles(현재 디렉토리) → bazel-bin → 소스 → 이 모듈의 코어 순으로 찾는다. 없으면 None (호출자가 EXIT_CONFIG).

    마지막 자리는 의존 저장소가 자기 그래프를 두지 않은 코어 생성물(`kg/gates-kg.ttl`)의 것이다 — 타깃의 `data` 로 선언돼
    runfiles 에 놓인 것만 거기 있다.
    """
    for cand in (Path(path), root / "bazel-bin" / path, root / path, core_root() / path):
        if cand.is_file():
            return cand
    return None
```
<!-- 인용 끝 -->
