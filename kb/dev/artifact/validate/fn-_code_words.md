---
id: https://agentic-knowledge-base.dev/id/chunk/2a4b8195-f60c-4855-abcc-199681ca3549
type: artifact
level: executable
title_ko: 함수 _code_words (tools/validate.py)
title: function _code_words in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/650f6771-cd62-485d-85c3-a08e4df10c41
---
**함수** — `_code_words(lang, code)` 다. 인용 코드 → 그 코드가 쓰는 이름들.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _code_words(lang: str, code: str) -> set[str]:
    """인용 코드 → 그 코드가 쓰는 이름들. 주석과 docstring 은 이름이 아니다.

    파이썬은 AST 의 이름·속성·정의·인자·가져오기 이름과, 문자열 상수 안의 `agt:` 용어다(TTL 을 문자열로 내는 코드가 있다).
    SPARQL 은 주석 줄을 뺀 글의 `agt:` 용어다. AST 로 읽히지 않는 조각은 tokenize 의 이름과 문자열로 읽는다."""
    import ast
    import io
    import textwrap
    import tokenize
    words: set[str] = set()
    if lang == "sparql":
        text = "\n".join(ln for ln in code.splitlines() if not ln.lstrip().startswith("#"))
        return set(_AGT_TOKEN.findall(text))
    src = textwrap.dedent(code)
    try:
        tree = ast.parse(src)
    except SyntaxError:
        try:
            for tok in tokenize.generate_tokens(io.StringIO(src).readline):
                if tok.type == tokenize.NAME:
                    words.add(tok.string)
                elif tok.type == tokenize.STRING:
                    words |= set(_AGT_TOKEN.findall(tok.string))
        except (tokenize.TokenError, IndentationError):
            pass
        return words
    docstrings = set()
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                and isinstance(body[0].value.value, str):
            docstrings.add(id(body[0].value))
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            words.add(node.id)
        elif isinstance(node, ast.Attribute):
            words.add(node.attr)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            words.add(node.name)
        elif isinstance(node, ast.arg):
            words.add(node.arg)
        elif isinstance(node, ast.keyword) and node.arg:
            words.add(node.arg)
        elif isinstance(node, ast.alias):
            words.add(node.asname or node.name)
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docstrings:
            words |= set(_AGT_TOKEN.findall(node.value))
    return words
```
<!-- 인용 끝 -->
