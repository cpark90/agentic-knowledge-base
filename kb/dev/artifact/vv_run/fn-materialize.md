---
id: https://agentic-knowledge-base.dev/id/chunk/a52db838-3103-4131-8ba5-17b938049c08
type: artifact
level: executable
title_ko: 함수 materialize (tools/vv_run.py)
title: function materialize in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `materialize(spec, slug)` 다. `files` 를 임시 디렉토리에 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def materialize(spec: dict, slug: str) -> tuple[Path | None, dict[str, str]]:
    """`files` 를 임시 디렉토리에 쓴다 → (디렉토리, 이름 → 절대 경로). 경로는 검증기가 정한다 — 케이스는 이름만 준다.

    워크스페이스 밖(`tempfile`)에 두는 까닭은 둘이다. 케이스가 부르는 `bazel test //...` 가 새 파일을 지식 파일로 읽으면
    양성 명령이 자극 때문에 실패하고, 케이스가 절대 경로를 적으면 병렬 실행이 서로를 덮는다 (p8-machine-readable-case).
    내용은 케이스가 적은 그대로 쓴다 — 줄 수가 자극인 케이스가 있어 검증기가 줄을 더하지 않는다.
    """
    files = spec.get("files") or {}
    if not files:
        return None, {}
    d = Path(tempfile.mkdtemp(prefix=f"vv-{slug}-"))
    subs = {}
    for name, content in files.items():
        (d / name).write_text(content, encoding="utf-8")
        subs[name] = (d / name).as_posix()
    return d, subs
```
<!-- 인용 끝 -->
