---
id: https://agentic-knowledge-base.dev/id/chunk/165313bb-866c-4352-820a-719686c0ca28
type: artifact
level: executable
title_ko: 함수 verify_query_files (tools/validate.py)
title: function verify_query_files in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/386f974f-846c-47c9-99dc-ee866783f5c5]
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `verify_query_files(paths)` 다. `--verify-queries` 의 인자(질의 파일 또는 디렉토리) → 정렬된 `.rq` 경로 (task 0327 손질 2).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def verify_query_files(paths: list[str]) -> list:
    """`--verify-queries` 의 인자(질의 파일 또는 디렉토리) → 정렬된 `.rq` 경로 (task 0327 손질 2).

    게이트 매크로는 질의 filegroup 의 `$(rootpaths)` 를 파일로 넘긴다 — 의존 저장소에서는 질의가 이 모듈의 runfiles 디렉토리에
    놓이므로 고정 경로가 빗나간다. 0개면 ConfigFailure 다: 질의 0개의 PASS 는 판정을 하지 않은 통과다.
    """
    from pathlib import Path
    out: set = set()
    for p in paths:
        path = Path(p)
        if path.is_dir():
            out |= set(path.glob("*.rq"))
        elif path.suffix == ".rq" and path.is_file():
            out.add(path)
    if not out:
        raise ConfigFailure(f"[{VERIFY}] {' '.join(paths) or '(인자 없음)'}: verify 질의가 0개다 — 판정 없이 PASS 하지 않는다. "
                            "kb_gate_test 의 verify_queries 에 질의 filegroup(@agentic_knowledge_base//tools:verify_queries)을 준다")
    return sorted(out)
```
<!-- 인용 끝 -->
