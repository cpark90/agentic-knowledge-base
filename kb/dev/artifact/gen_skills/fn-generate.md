---
id: https://agentic-knowledge-base.dev/id/chunk/735aadbc-1b1e-465d-8274-4cb2aee71fb2
type: artifact
level: executable
title_ko: 함수 generate (tools/gen_skills.py)
title: function generate in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/068914d2-cc43-489e-bcbe-f60049946a47, https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/32e0ebb2-c394-499d-8a6b-3c2f3e5ed23f, https://agentic-knowledge-base.dev/id/chunk/42689d2d-de66-4143-bd55-21a97e71e57c, https://agentic-knowledge-base.dev/id/chunk/9337f5de-4a6b-420b-b51d-2a1afe8ebbae, https://agentic-knowledge-base.dev/id/chunk/f4e15fab-b378-46c2-b8ae-ca2982aa9dcd]
part_of: https://agentic-knowledge-base.dev/id/composite/b9b38ba6-d689-44c6-814b-4526153a07b1
---
**함수** — `generate(root)` 다. {SKILL.md 경로: 내용} — 원본이 없거나 앵커가 틀리거나 산문이 규칙 밖이면 GenSkillsError.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def generate(root: Path) -> dict[str, str]:
    """{SKILL.md 경로: 내용} — 원본이 없거나 앵커가 틀리거나 산문이 규칙 밖이면 GenSkillsError."""
    build = root / TOOLS_DIR / "BUILD.bazel"
    binaries = set(PY_BINARY.findall(build.read_text(encoding="utf-8")))
    anchors: dict[str, dict[str, str]] = {}
    out: dict[str, str] = {}
    depth = len(Path(kb_lib.SKILLS_DIR).parts) + 1  # .claude/skills/<tool>/SKILL.md → 루트
    seen = set()
    for entry in kb_lib.SKILLS:
        tool = entry["tool"]
        if tool in seen:
            raise GenSkillsError(f"kb_lib.SKILLS: {tool} 이 두 번 있다")
        seen.add(tool)
        src = root / TOOLS_DIR / f"{tool}.py"
        if not src.is_file():
            raise GenSkillsError(f"kb_lib.SKILLS[{tool}]: {src.as_posix()} 가 없다")
        if tool not in binaries:
            raise GenSkillsError(f"kb_lib.SKILLS[{tool}]: {build.as_posix()} 에 py_binary {tool!r} 가 없다 — 도구의 실재는 BUILD 다")
        if not 1 <= len(entry.get("commands", [])) <= 3:
            raise GenSkillsError(f"kb_lib.SKILLS[{tool}]: 대표 명령은 1~3개다 — 실제 {len(entry.get('commands', []))}")
        doc_name, _, anchor = entry["section"].partition("#")
        doc = root / DOCS_DIR / doc_name
        if doc_name not in anchors:
            if not doc.is_file():
                raise GenSkillsError(f"kb_lib.SKILLS[{tool}]: 원본 절 문서 {doc.as_posix()} 가 없다")
            anchors[doc_name] = heading_index(doc)
        if anchor not in anchors[doc_name]:
            raise GenSkillsError(f"kb_lib.SKILLS[{tool}]: {doc.as_posix()} 에 제목 앵커 #{anchor} 가 없다 (GitHub 규칙: 소문자, 공백→-, 구두점 제거)")
        title, what, usage = docstring_parts(src)
        path = root / kb_lib.SKILLS_DIR / kebab(tool) / "SKILL.md"
        content = render(entry, title, what, usage, f"{DOCS_DIR}/{doc_name}", anchors[doc_name][anchor], depth)
        errors, _, _ = kb_lib.check_prose(path, content)
        if errors:
            raise GenSkillsError(f"{src.as_posix()} → {path.relative_to(root).as_posix()}: 생성 본문이 산문 규칙 밖이다 — "
                                 + "; ".join(f"{ln}: {msg}" for ln, msg in errors[:3]))
        out[str(path)] = content
    return out
```
<!-- 인용 끝 -->
