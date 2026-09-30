---
id: https://agentic-knowledge-base.dev/id/chunk/808534e8-8fca-4ace-ace9-9e4b7084233e
type: artifact
level: executable
title_ko: 함수 resolve_glob (tools/kb_lib.py)
title: function resolve_glob in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `resolve_glob(pattern, root)` 다. 재귀 glob 을 같은 순서로 찾는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve_glob(pattern: str, root: Path) -> list[Path]:
    """재귀 glob 을 같은 순서로 찾는다 — 첫 번째로 파일이 나오는 뿌리의 결과만.

    bazel-bin 아래의 `*.runfiles/` 사본은 뺀다 — 테스트마다 같은 원본이 복제돼 한 파일이 여러 번 적재되고, 빈 노드(owl:Restriction)를
    가진 파일은 적재마다 다른 노드가 되어 질의 행이 중복된다 (CQ-36 첫 실행 2026-09-18: 7행이 13행으로). IRI 트리플만 있는 파일은
    중복 적재가 결과를 바꾸지 않아 드러나지 않았다.
    """
    import glob as _glob
    for base in (Path("."), root / "bazel-bin", root):
        found = sorted(Path(p) for p in _glob.glob(str(base / pattern), recursive=True)
                       if not any(part.endswith(".runfiles") for part in Path(p).parts))
        if found:
            return found
    return []
```
<!-- 인용 끝 -->
