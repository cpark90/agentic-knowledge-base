---
id: https://agentic-knowledge-base.dev/id/chunk/d8304dd3-dfe1-49f3-bb99-12294f298b9c
type: artifact
level: executable
title_ko: 함수 check_paths (tools/doccheck.py)
title: function check_paths in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984
---
**함수** — `check_paths(doc, lines, repo)` 다. 백틱 안의 저장소 경로가 실재한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_paths(doc: Path, lines: list[str], repo: Repo) -> list[str]:
    """백틱 안의 저장소 경로가 실재한다. 패턴·자리표시자·라벨·생성물은 판정 밖."""
    errors = []
    for ln, line in prose_lines(lines):
        for m in CODE_SPAN.finditer(line):
            span = m.group(2).strip()
            if not span.startswith(PATH_PREFIXES) or span.startswith("~") or any(k in span for k in SKIP_MARKS):
                continue
            if line[max(m.start() - 1, 0)] == "[" and line.startswith("](", m.end()):
                continue  # 링크 텍스트 [`경로`](경로) — 링크 검사가 같은 대상을 본다, 두 번 세지 않는다
            cand = FILE_LINE.sub("", span.split()[0].partition("#")[0])
            if ":" in cand:  # 경로에는 ':' 이 없다 — Bazel 라벨 표기
                continue
            if not repo.exists(cand):
                errors.append(f"{doc}:{ln}: 없는 경로 `{span}` — {cand} 가 없다 (생성물은 bazel-bin/ 접두로 적는다)")
    return errors
```
<!-- 인용 끝 -->
