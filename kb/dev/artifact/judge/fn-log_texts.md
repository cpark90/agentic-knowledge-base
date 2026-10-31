---
id: https://agentic-knowledge-base.dev/id/chunk/5e8f0410-5a7f-4fe4-848c-4414e21924d0
type: artifact
level: executable
title_ko: 함수 log_texts (tools/judge.py)
title: function log_texts in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/4398e3e6-d783-4d00-a75b-cd5e24700a7c, https://agentic-knowledge-base.dev/id/chunk/97961156-fa24-45e3-8c66-a941abf73b4f, https://agentic-knowledge-base.dev/id/chunk/a82c512c-7648-4b7c-b506-56a5a18e9cd5]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `log_texts(rows, q, name, decoy, source, stamp, enc, shapes)` 다. 판정 로그의 묶음과 글 — 일치율 shape 를 어기는 글이 하나라도 있으면 JudgeError 다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def log_texts(rows: list[dict], q: dict, name: str, decoy: str, source: str, stamp: str, enc, shapes: Path) -> tuple[list, list]:
    """판정 로그의 묶음과 글 — 일치율 shape 를 어기는 글이 하나라도 있으면 JudgeError 다 (Q-0056 Q119-a). 쓰기 전에 부른다."""
    chunks = split_rows(rows, q, name, decoy, source, stamp, enc)  # 묶음의 상한은 토큰이다 (p1-chunk-unit-is-tokens)
    texts = [log_chunk(part, q, name, decoy, source, stamp) for part in chunks]
    for text in texts:
        bad = kb_lib.judge_log_violations(text, shapes)
        if bad:
            raise JudgeError(f"판정 로그가 {shapes.name} 를 어긴다 — " + " · ".join(bad))
    return chunks, texts
```
<!-- 인용 끝 -->
