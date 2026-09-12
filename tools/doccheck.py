#!/usr/bin/env python3
"""문서 현행성 게이트 — 죽은 링크·앵커·경로 (agrtls-practices-review N, 2026-09-12).

대상은 진입점 문서(README·AGENTS·STYLEGUIDE·CLAUDE·INTENT)와 docs/**/*.md 다. 채널(docs/feedback/**)은
소멸성이라 대상이 아니고(hci 스캔 몫), 노트(docs/agent-knowledge-system-notes.md)는 유저 문서라 링크
대상으로만 쓴다(--target-only). 기계적으로 참·거짓이 갈리는 것만 게이트다 — 나머지는 검토 재료.

  links   마크다운 링크 [..](경로#앵커): 경로가 실재하고, #앵커는 대상 .md 파일 제목의 GitHub slug 와
          일치한다 (소문자, 공백→'-', 문자·숫자·'-'·'_' 외 제거, 같은 slug 는 -1, -2 …).
          스킴이 있는 것(http·https·mailto·urn …)은 건너뛴다. 코드 펜스·코드 스팬 안은 링크가 아니다.
  paths   백틱 안의 저장소 경로 — kb/ kg/ tools/ docs/ defs/ chunks/ space/ .claude/ 로 시작하는 것 — 가
          실재한다. 패턴·자리표시자·Bazel 라벨·생성물은 건너뛴다: `*` `<` `{` `…` `$` `//` `bazel-bin/`
          `bazel-out` `.wip` 을 포함하거나 `~` 로 시작하는 것. 생성물은 `bazel-bin/` 접두로 적는 것이
          규칙이다 — 표지가 아니라 규칙이므로 `kg/chunks-kg.ttl` 처럼 적힌 생성물은 없는 경로로 잡힌다.
          `파일:줄` 표기는 파일만 본다. 경로에는 ':' 이 없으므로 그 밖의 ':' 은 라벨로 보고 건너뛴다.

출력  FAIL [doccheck] <파일>:<줄>: <종류> <대상> — 근거
종료  위반 → EXIT_FAIL · 입력 파일 없음/루트 밖/인자 오류 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)

사용  doccheck.py [--root DIR] <문서 ...> [--target-only FILE ...]
      bazel run //tools:doccheck -- *.md docs/*.md docs/open-questions/*.md --target-only docs/agent-knowledge-system-notes.md
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 아직 없으면 같은 값의 폴백
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError:
        kb_lib = None
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음·인자 오류·읽을 수 없는 입력
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건 — PASS 가 아니다

TAG = "doccheck"
PATH_PREFIXES = ("kb/", "kg/", "tools/", "docs/", "defs/", "chunks/", "space/", ".claude/")
SKIP_MARKS = ("*", "<", "{", "…", "$", "//", "bazel-bin/", "bazel-out", ".wip")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
CODE_SPAN = re.compile(r"(`+)(.+?)\1")
MD_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
HTML_TAG = re.compile(r"<[^>]+>")
FILE_LINE = re.compile(r":\d+(?:-\d+)?$")


def prose_lines(lines: list[str]):
    """(줄 번호, 줄) — 코드 펜스·frontmatter·HTML 주석 안은 산문이 아니므로 건너뛴다."""
    fence: str | None = None
    in_comment = False
    start = 0
    if lines and lines[0].strip() == "---":
        try:
            start = lines[1:].index("---") + 2
        except ValueError:
            start = 0
    for i, line in enumerate(lines[start:], start=start + 1):
        if in_comment:
            if "-->" in line:
                in_comment = False
                line = line.split("-->", 1)[1]
            else:
                continue
        m = FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        if "<!--" in line:
            head, _, tail = line.partition("<!--")
            if "-->" in tail:
                line = head + tail.split("-->", 1)[1]
            else:
                in_comment = True
                line = head
        yield i, line


def slug(text: str) -> str:
    """GitHub 제목 앵커 규칙 — 소문자, 공백→'-', 문자·숫자·결합 부호·'-'·'_' 외 제거."""
    text = MD_LINK.sub(r"\1", text)
    text = HTML_TAG.sub("", text)
    out = []
    for c in text.lower():
        if c == " ":
            out.append("-")
        elif c in "-_" or c.isalnum() or unicodedata.category(c).startswith("M"):
            out.append(c)
    return "".join(out)


def anchors(lines: list[str]) -> set[str]:
    """파일의 제목 앵커 집합 — 같은 slug 는 GitHub 처럼 -1, -2 … 로 구분한다."""
    seen: dict[str, int] = {}
    out: set[str] = set()
    for _, line in prose_lines(lines):
        m = HEADING.match(line)
        if not m:
            continue
        s = slug(m.group(2).strip())
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.add(s if n == 0 else f"{s}-{n}")
    return out


def find_links(line: str):
    """줄 안의 인라인 링크 목적지 — `](` 뒤에서 괄호 짝을 맞춰 읽는다. 제목("…")은 뗀다."""
    i = 0
    while True:
        j = line.find("](", i)
        if j < 0:
            return
        depth, k = 1, j + 2
        while k < len(line) and depth:
            depth += {"(": 1, ")": -1}.get(line[k], 0)
            k += 1
        if depth:
            return
        dest = line[j + 2 : k - 1].strip()
        i = k
        if dest.startswith("<") and ">" in dest:
            dest = dest[1 : dest.index(">")]
        else:
            dest = dest.split()[0] if dest.split() else ""
        yield dest


def resolve(doc: Path, dest_path: str) -> str | None:
    """문서 기준 상대 경로 → 루트 기준 경로. 루트 밖이면 None."""
    base = "" if dest_path.startswith("/") else doc.parent.as_posix()
    joined = os.path.normpath(os.path.join(base, dest_path.lstrip("/")))
    if joined == "." or joined.startswith(".."):
        return None if joined.startswith("..") else ""
    return joined


class Repo:
    def __init__(self, root: Path, empty_dirs: set[str] = frozenset()):
        self.root = root
        self.empty_dirs = {d.strip("/") for d in empty_dirs}  # 파일이 없어 runfiles 에 안 나타나는 빈 패키지 — BUILD 가 선언
        self._anchors: dict[str, set[str]] = {}

    def exists(self, rel: str) -> bool:
        if not rel:
            return True
        return (self.root / rel).exists() or rel.strip("/") in self.empty_dirs

    def anchors_of(self, rel: str) -> set[str]:
        if rel not in self._anchors:
            self._anchors[rel] = anchors(self.read(rel))
        return self._anchors[rel]

    def read(self, rel: str) -> list[str]:
        return (self.root / rel).read_text(encoding="utf-8").splitlines()


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


def to_rel(path: str, root: Path, workdir: str | None) -> Path:
    p = Path(path)
    if not p.is_absolute() and workdir:
        p = Path(workdir) / p
    p = Path(os.path.abspath(p))  # 심볼릭 링크는 따라가지 않는다 — runfiles 의 링크가 루트 밖을 가리킨다
    try:
        return p.relative_to(root)
    except ValueError:
        raise ValueError(f"{path}: 루트 {root} 밖의 파일이다")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--target-only", action="append", nargs="+", default=[], metavar="FILE",
                    help="링크 대상으로만 쓰고 안에서 나가는 링크는 검사하지 않는 문서 (반복 가능, 검사할 문서 뒤에 둔다)")
    ap.add_argument("--empty-dir", action="append", default=[], metavar="DIR",
                    help="파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지) — kb_doccheck_test 의 empty_dirs")
    ap.add_argument("files", nargs="*", help="검사할 문서")
    args = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(args.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    repo = Repo(root, set(args.empty_dir))
    try:
        skip = {to_rel(f, root, workdir) for group in args.target_only for f in group}
        docs = [d for d in (to_rel(f, root, workdir) for f in args.files) if d not in skip]
        missing = [str(d) for d in docs if not (root / d).is_file()]
        if missing:
            raise ValueError("입력 문서가 없다: " + ", ".join(missing))
    except ValueError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not docs:
        print(f"SKIP [{TAG}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    errors: list[str] = []
    links = paths = 0
    for doc in sorted(set(docs)):
        lines = repo.read(doc.as_posix())
        links += sum(1 for _, l in prose_lines(lines) for _ in find_links(CODE_SPAN.sub(" ", l)))
        paths += sum(1 for _, l in prose_lines(lines) for m in CODE_SPAN.finditer(l) if m.group(2).strip().startswith(PATH_PREFIXES))
        errors += check_links(doc, lines, repo)
        errors += check_paths(doc, lines, repo)

    if errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}")
        print(f"\nFAIL [{TAG}] — {len(errors)}건 (문서 {len(docs)}개)")
        return EXIT_FAIL
    print(f"PASS [{TAG}] — 문서 {len(docs)}개, 링크 {links}개, 백틱 경로 {paths}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
