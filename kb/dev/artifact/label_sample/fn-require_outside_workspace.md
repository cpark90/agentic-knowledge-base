---
id: https://agentic-knowledge-base.dev/id/chunk/68ed1ed6-9607-4a24-b3d7-5631a30d0616
type: artifact
level: executable
title_ko: 함수 require_outside_workspace (tools/label_sample.py)
title: function require_outside_workspace in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fff3d0e5-ad0f-4eb4-b8c9-e9ae7d1ce791
---
**함수** — `require_outside_workspace(path, root)` 다. `path`가 워크스페이스(`root`) 밖인가 — 아니면 거부 사유, 밖이면 빈 문자열.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def require_outside_workspace(path: Path, root: Path) -> str:
    """`path`가 워크스페이스(`root`) 밖인가 — 아니면 거부 사유, 밖이면 빈 문자열.

    판정지(labels.md·bodies.md)는 게이트가 보지 않는 실험 자극이다 — 저장소 안에 두면 doccheck·gendoc 스캔 경로에
    들어올 위험과, 판정자 세션이 저장소를 열람해 답의 단서(원본 경로·이웃 파일)를 얻을 위험이 함께 생긴다."""
    resolved, root_resolved = path.resolve(), root.resolve()
    if resolved.is_relative_to(root_resolved):
        return (f"--judge-sheet {path} 이 워크스페이스({root}) 안이다 — 판정지는 저장소 밖에만 쓴다"
                "(게이트 없는 실험 자극, 2026-09-30 vnv 결함 보고 ④)")
    return ""
```
<!-- 인용 끝 -->
