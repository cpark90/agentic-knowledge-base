---
id: https://agentic-knowledge-base.dev/id/chunk/f9b6b36a-3732-4fca-b346-5a371afb405e
type: artifact
level: executable
title_ko: 클래스 CqQuery (tools/query.py)
title: class CqQuery in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/804dd9bd-ceaa-4ecc-9233-ef543578feb9
---
**클래스** — `class CqQuery` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class CqQuery:
    def __init__(self, path: Path):
        self.path = path
        self.id = path.stem
        text = path.read_text(encoding="utf-8")
        heads = [ln[1:].strip() for ln in text.splitlines()[:2] if ln.startswith("#")]
        self.question = heads[0] if heads else path.stem
        form = heads[1] if len(heads) > 1 else ""
        self.form = form[len(FORM_PREFIX):].lstrip() if form.startswith(FORM_PREFIX) else form  # 접두는 출력이 한 번만 붙인다
        self.text = text
        self.prepared = prepareQuery(text)  # 파싱 실패는 여기서 예외 — 호출자가 EXIT_CONFIG
```
<!-- 인용 끝 -->
