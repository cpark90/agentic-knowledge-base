---
id: https://agentic-knowledge-base.dev/id/chunk/c0a24368-1326-49c2-a33a-29918b01c696
type: artifact
level: executable
title_ko: 함수 runfiles_roots (tools/chunk2kg.py)
title: function runfiles_roots in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `runfiles_roots()` 다. runfiles 뿌리 후보 — 환경 변수(`RUNFILES_DIR`·`TEST_SRCDIR`) · 이 모듈 위치의 위 · cwd 의 위 순이고 중복은 뺀다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def runfiles_roots() -> list[Path]:
    """runfiles 뿌리 후보 — 환경 변수(`RUNFILES_DIR`·`TEST_SRCDIR`) · 이 모듈 위치의 위 · cwd 의 위 순이고 중복은 뺀다.

    이 파일은 runfiles 에서 `<뿌리>/<이 모듈의 canonical 이름>/tools/chunk2kg.py` 에 놓인다. 그래서 심볼릭 링크를
    풀지 않은 경로의 세 단계 위가 뿌리다. cwd 는 `bazel run`·`bazel test` 에서 `<뿌리>/_main` 이다.
    """
    cands = [os.environ.get("RUNFILES_DIR", ""), os.environ.get("TEST_SRCDIR", "")]
    out: list[Path] = []
    for c in [Path(c) for c in cands if c] + [Path(__file__).absolute().parent.parent.parent, Path("..").absolute()]:
        if c.is_dir() and c not in out:
            out.append(c)
    return out
```
<!-- 인용 끝 -->
