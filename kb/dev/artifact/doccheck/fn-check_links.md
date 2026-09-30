---
id: https://agentic-knowledge-base.dev/id/chunk/4daa5f81-6009-493b-af58-f97f9a3f388c
type: artifact
level: executable
title_ko: 함수 check_links (tools/doccheck.py)
title: function check_links in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984
---
**함수** — `check_links(doc, lines, repo)` 다. [..](경로#앵커) — 경로 실재 + .md 대상의 앵커가 제목 slug 안에 있다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_links(doc: Path, lines: list[str], repo: Repo) -> list[str]:
    """[..](경로#앵커) — 경로 실재 + .md 대상의 앵커가 제목 slug 안에 있다."""
    errors = []
    for ln, line in prose_lines(lines):
        for dest in find_links(CODE_SPAN.sub(" ", line)):
            if not dest or SCHEME.match(dest):
                continue
            path, _, frag = dest.partition("#")
            path, frag = urllib.parse.unquote(path), urllib.parse.unquote(frag)
            if path:
                target = resolve(doc, path)
                if target is None or not repo.exists(target):
                    errors.append(f"{doc}:{ln}: 깨진 링크 ({dest}) — {target or path} 가 없다")
                    continue
            else:
                target = doc.as_posix()
            if frag and target.endswith(".md") and frag not in repo.anchors_of(target):
                errors.append(f"{doc}:{ln}: 없는 앵커 ({dest}) — {target} 의 제목 slug 에 #{frag} 가 없다 (GitHub 규칙: 소문자, 공백→-, 구두점 제거)")
    return errors
```
<!-- 인용 끝 -->
