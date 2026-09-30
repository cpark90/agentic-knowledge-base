---
id: https://agentic-knowledge-base.dev/id/chunk/068914d2-cc43-489e-bcbe-f60049946a47
type: artifact
level: executable
title_ko: 함수 docstring_parts (tools/gen_skills.py)
title: function docstring_parts in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/210e1533-9390-4961-914e-3e556e96fe3d
---
**함수** — `docstring_parts(path)` 다. 모듈 docstring → (첫 줄의 제목, 첫 문단, 사용법 블록).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def docstring_parts(path: Path) -> tuple[str, str, str]:
    """모듈 docstring → (첫 줄의 제목, 첫 문단, 사용법 블록). 제목은 첫 줄의 " — " 앞이다."""
    doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf-8")))
    if not doc:
        raise GenSkillsError(f"{path.as_posix()}: 모듈 docstring 이 없다 — skill 의 본문은 docstring 에서 생성한다")
    lines = doc.splitlines()
    first = []
    for ln in lines:
        if not ln.strip():
            break
        first.append(ln.strip())
    title = first[0].split(" — ", 1)[0].strip() if " — " in first[0] else ""
    usage: list[str] = []
    for i, ln in enumerate(lines):
        m = USAGE.search(ln)
        if not m:
            continue
        rest = ln[m.end():].strip()
        if rest:
            usage.append(rest)
        for cont in lines[i + 1:]:
            if not cont.strip() or not cont.startswith((" ", "\t")):
                break
            usage.append(cont.strip())
        break
    if not usage:
        raise GenSkillsError(f"{path.as_posix()}: docstring 에 `사용:` 줄이 없다 — skill 의 명령은 사용법에서 생성한다")
    return title, " ".join(first), "\n".join(usage)
```
<!-- 인용 끝 -->
