---
id: https://agentic-knowledge-base.dev/id/chunk/cbb17652-19dd-4e9e-833d-0e61dfbd4110
type: artifact
level: executable
title_ko: 함수 report_doc_path (tools/doccheck.py)
title: function report_doc_path in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `report_doc_path(path, root, workdir)` 다. 보고 모드의 문서 경로 — `to_rel` 과 달리 루트 밖 절대 경로를 거부하지 않는다(2026-10-01, vnv 요청 — `vv_run` 이 케이스 자극을 워크스페이스 밖 임시 디렉토리에 두므로 그 파일을 보고 대상으로 줄 수 있어야 한다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_doc_path(path: str, root: Path, workdir: str | None) -> str:
    """보고 모드의 문서 경로 — `to_rel` 과 달리 루트 밖 절대 경로를 거부하지 않는다(2026-10-01, vnv 요청 —
    `vv_run` 이 케이스 자극을 워크스페이스 밖 임시 디렉토리에 두므로 그 파일을 보고 대상으로 줄 수 있어야 한다).
    루트 안이면 상대 경로로 돌려준다(표시가 짧다) — 심볼릭 링크는 따라가지 않는다(runfiles 의 링크가 루트 밖을 가리킨다).
    """
    p = Path(path)
    if not p.is_absolute() and workdir:
        p = Path(workdir) / p
    p = Path(os.path.abspath(p))
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)
```
<!-- 인용 끝 -->
