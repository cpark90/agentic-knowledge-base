#!/usr/bin/env python3
"""skill 생성기 — 도구 docstring 과 kb_lib.SKILLS 에서 .claude/skills/<도구-kebab>/SKILL.md 를 생성한다 (로드맵 6단계, agrtls K).

skill 은 손으로 쓰지 않고 지식·절차에서 생성한다. 원본은 둘이다 — 각 도구 모듈의 docstring(첫 문단 = 무엇, `사용:` 줄 = 사용법)과
kb_lib.SKILLS(어떤 도구를 내는가 · 원본 절 앵커 · 언제 쓰는가 · 대표 명령). tools/BUILD.bazel 의 py_binary 목록이 도구의 실재다.
생성물은 트리에 두고 커밋한다(BUILD 와 같은 이유 — 도구가 없어도 skill 이 읽혀야 한다). //:skills_drift_test 가 생성기를 다시
돌려 트리와 비교한다 — docstring·SKILLS 를 고치고 생성을 안 돌린 경우와 손으로 쓴 skill(이중 원본)을 잡는다.
생성 본문도 단정 서술형이다 — kb_lib.check_prose 로 자기 검사한다.
사용: gen_skills.py [--check] [--root .]
출력·종료: 생성 시점 거부(도구·py_binary·docstring·절 앵커 없음, 산문 위반)는 `FAIL [gen-skills] …` EXIT_FAIL,
--check 의 어긋남·손으로 쓴 skill 은 `FAIL [skills-drift] …` EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import ast
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
HEADING, slug = kb_lib.MD_HEADING, kb_lib.slug  # GitHub 제목 앵커 규칙의 단일 정의처는 kb_lib (STYLEGUIDE §7)

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.GEN_SKILLS_GATE, kb_lib.SKILLS_DRIFT_GATE
PY_BINARY = re.compile(r'py_binary\(\s*name\s*=\s*"([\w-]+)"')
# `사용:` 줄 — 줄머리(콜론 없어도 된다: "사용  doccheck.py …") 또는 줄 가운데의 "사용: …". 블록은 뒤따르는 들여쓴 줄까지다
USAGE = re.compile(r"^사용[:：]?(?=\s|$)|사용[:：]\s*")
NOTICE = kb_lib.gendoc_tree_notice("도구 docstring 과 `kb_lib.SKILLS`", "//:skills_drift_test")
DOCS_DIR = "docs"
TOOLS_DIR = "tools"
RESOLVE_ANCHOR = "게이트-총람--이-문서가-원본이다"  # docs/tools.md 의 총람 — `해소` 열이 FAIL [<id>] 의 해소다


class GenSkillsError(Exception):
    """생성 시점 거부 — 메시지가 `<원본>: <근거>` 다."""


def kebab(tool: str) -> str:
    return tool.replace("_", "-")


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


def heading_index(doc: Path) -> dict[str, str]:
    """문서의 제목 앵커 → 제목 텍스트 (doccheck 의 slug 규칙, 같은 slug 는 -1, -2 …). 코드 펜스 안은 제목이 아니다."""
    out, seen, fence = {}, {}, False
    for line in doc.read_text(encoding="utf-8").splitlines():
        if re.match(r"^ {0,3}(`{3,}|~{3,})", line):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        text = m.group(2).strip()
        s = slug(text)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out[s if n == 0 else f"{s}-{n}"] = text
    return out


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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    a = ap.parse_args()
    root = Path(a.root)
    try:
        outputs = generate(root)
    except GenSkillsError as e:
        print(f"FAIL [{GEN}] {e}")
        return EXIT_FAIL
    except (OSError, SyntaxError) as e:
        print(f"FAIL [{GEN}] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    skills_dir = root / kb_lib.SKILLS_DIR
    stray = sorted(p for p in skills_dir.glob("*/SKILL.md") if str(p) not in outputs) if skills_dir.is_dir() else []
    drift = []
    for path, content in outputs.items():
        p = Path(path)
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(path)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{path} (트리)", f"{path} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content, encoding="utf-8")
    for s in stray:
        print(f"FAIL [{DRIFT}] {s}: kb_lib.SKILLS 에 없는 skill 이다 — 손으로 쓴 skill 은 이중 원본이다. SKILLS 에 항목을 더하고 생성하거나 지운다")
    if a.check:
        for path in drift:
            print(f"FAIL [{DRIFT}] {path}: 원본(docstring · kb_lib.SKILLS)과 어긋난다 — python3 tools/gen_skills.py --root . 를 돌려 커밋하라")
        if drift or stray:
            print(f"\nFAIL [{DRIFT}] — 어긋남 {len(drift)}건 · 손으로 쓴 skill {len(stray)}건 / 생성 skill {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT}] — 생성 skill {len(outputs)}개가 원본과 일치")
        return EXIT_OK
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(Path(d).relative_to(root).as_posix() for d in drift))
    return EXIT_FAIL if stray else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
