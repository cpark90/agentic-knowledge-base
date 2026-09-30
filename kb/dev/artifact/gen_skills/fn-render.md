---
id: https://agentic-knowledge-base.dev/id/chunk/32e0ebb2-c394-499d-8a6b-3c2f3e5ed23f
type: artifact
level: executable
title_ko: 함수 render (tools/gen_skills.py)
title: function render in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b9b38ba6-d689-44c6-814b-4526153a07b1
---
**함수** — `render(entry, title, what, usage, section_doc, section_text, depth)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(entry: dict, title: str, what: str, usage: str, section_doc: str, section_text: str, depth: int) -> str:
    tool, when = entry["tool"], entry["when"]
    up = "../" * depth
    if ": " in when or " #" in when or when[:1] in "[]{}&*!|>'\"%@`,":
        raise GenSkillsError(f"kb_lib.SKILLS[{tool}].when: YAML 평문 스칼라로 쓸 수 없는 문자(': ' · ' #' · 특수 첫 글자)가 있다")
    cmds = "\n".join(entry["commands"])
    # 생성 트리 파일이므로 생성 시각·지문을 넣지 않는다 (규약 G3·G4 의 예외) — //:skills_drift_test 의 바이트 비교가
    # 그 자리의 건전성 장치다. 나머지 머리 블록은 Bazel 뷰와 같은 순서다
    head = kb_lib.gendoc_header(
        tool, title or f"{tool} 도구의 skill", "tools/gen_skills.py",
        f"이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)",
        "python3 tools/gen_skills.py --root .",
        [f"{TOOLS_DIR}/{tool}.py", f"{TOOLS_DIR}/kb_lib.py", section_doc],
        "", NOTICE, input_kind="원본 파일", stamped=False)
    return "\n".join([
        "---", f"name: {kebab(tool)}", f"description: {when}", "---", ""] + head + [
        what, "",
        "## 언제 쓰는가", "", when, "",
        "## 명령", "", "```bash", cmds, "```", "",
        "## 원본", "",
        f"- 절차: [`{section_doc}` {section_text}]({up}{section_doc}#{entry['section'].split('#', 1)[1]})",
        f"- 도구: `{TOOLS_DIR}/{tool}.py` (`bazel run //{TOOLS_DIR}:{tool}`) — 사용법은 docstring 이 원본이다", "",
        "```text", usage, "```", "",
        "## 실패 시", "",
        f"`FAIL [<id>]` 의 해소는 [`{DOCS_DIR}/tools.md` 게이트 총람]({up}{DOCS_DIR}/tools.md#{RESOLVE_ANCHOR})의 `해소` 열이다. "
        "종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.", "",
    ])
```
<!-- 인용 끝 -->
