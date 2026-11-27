---
id: https://agentic-knowledge-base.dev/id/chunk/4584a981-d251-4a2b-8951-263c3541bc22
type: artifact
level: executable
title_ko: 함수 resolve_core_glob (tools/kb_lib.py)
title: function resolve_core_glob in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5bbe9743-feb1-4ec4-8678-c5b66eb40f83, https://agentic-knowledge-base.dev/id/chunk/808534e8-8fca-4ace-ace9-9e4b7084233e]
part_of: https://agentic-knowledge-base.dev/id/composite/0edbd7df-e79b-4b9f-b913-f8e16daf03ad
---
**함수** — `resolve_core_glob(pattern, root)` 다. 코어와 호출 저장소의 재귀 glob 합 — 코어(`core_root`)의 결과에 호출 저장소(`resolve_glob`)의 결과를 더하고 실경로로 중복을 뺀다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve_core_glob(pattern: str, root: Path) -> list[Path]:
    """코어와 호출 저장소의 재귀 glob 합 — 코어(`core_root`)의 결과에 호출 저장소(`resolve_glob`)의 결과를 더하고 실경로로 중복을 뺀다.

    온톨로지는 코어 어휘와 의존 저장소의 확장 모듈이 함께 쓰여야 한다 (task 0327 손질 5). 코어 뿌리 밑의 runfiles 사본은 빼지 않는다 —
    거기가 runfiles 자체이기 때문이다.
    """
    import glob as _glob
    out: list[Path] = []
    seen: set[str] = set()
    core = sorted(Path(p) for p in _glob.glob(str(core_root() / pattern), recursive=True))
    for f in core + resolve_glob(pattern, root):
        key = os.path.realpath(f)
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out
```
<!-- 인용 끝 -->
