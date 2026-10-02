---
id: https://agentic-knowledge-base.dev/id/chunk/f5bba732-244e-40a1-a3a0-f5c8e97043be
type: artifact
level: executable
title_ko: 함수 check_verify (tools/validate.py)
title: function check_verify in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_verify(merged, query_dir)` 다. 안티패턴 계층 (노트 2.5절) — '이런 트리플이 존재하면 실패'를 SPARQL로 명세.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_verify(merged: Graph, query_dir: str) -> list[str]:
    """안티패턴 계층 (노트 2.5절) — '이런 트리플이 존재하면 실패'를 SPARQL로 명세.

    tools/verify-queries/*.rq 하나가 안티패턴 하나다. 결과 행이 나오면 그 행 수만큼
    위반이며, 질의 첫 주석 줄이 실패 메시지의 근거가 된다. shape로 쓰기 어색한
    제약(연쇄·부정·집계)이 여기로 온다.
    """
    from pathlib import Path
    errors = []
    for rq in sorted(Path(query_dir).glob("*.rq")):
        text = rq.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip() if text.startswith("#") else rq.stem
        try:
            rows = list(merged.query(text))
        except Exception as e:
            errors.append(f"[{VERIFY}] {rq.as_posix()}: 질의 자체가 실패 — {e}")
            continue
        for row in rows[:20]:
            vals = " ".join(str(v) for v in row)
            errors.append(f"[{VERIFY}] {rq.as_posix()}: {vals}  ({title})")
        if len(rows) > 20:
            errors.append(f"[{VERIFY}] {rq.as_posix()}: … 외 {len(rows)-20}건")
    return errors
```
<!-- 인용 끝 -->
