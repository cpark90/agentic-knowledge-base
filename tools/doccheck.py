#!/usr/bin/env python3
"""문서 현행성 게이트 — 죽은 링크·앵커·경로 (agrtls-practices-review N, 2026-09-12).

대상은 진입점 문서(README·AGENTS·STYLEGUIDE·CLAUDE·INTENT)와 docs/**/*.md, 그리고 하네스 문서
(harness/README.md · harness/agents/*.md · harness/user/README.md)다. 채널 메시지(harness/channel/**)·질문지
(harness/user/Q-*.md · harness/user/archive/**)·옛 채널 기록(legacy/)은 소멸성 소통 기록이라 대상이 아니고 링크
대상으로만 쓴다(채널 규약은 게이트 `channel`). 노트(docs/agent-knowledge-system-notes.md)는 유저 문서라 링크
대상으로만 쓴다(--target-only). 기계적으로 참·거짓이 갈리는 것만 게이트다 — 나머지는 검토 재료.

  links   마크다운 링크 [..](경로#앵커): 경로가 실재하고, #앵커는 대상 .md 파일 제목의 GitHub slug 와
          일치한다 (소문자, 공백→'-', 문자·숫자·'-'·'_' 외 제거, 같은 slug 는 -1, -2 …).
          스킴이 있는 것(http·https·mailto·urn …)은 건너뛴다. 코드 펜스·코드 스팬 안은 링크가 아니다.
  paths   백틱 안의 저장소 경로 — kb/ kg/ tools/ docs/ defs/ chunks/ space/ harness/ .claude/ 로 시작하는 것 — 가
          실재한다. 패턴·자리표시자·Bazel 라벨·생성물은 건너뛴다: `*` `<` `{` `…` `$` `//` `bazel-bin/`
          `bazel-out` `.wip` 을 포함하거나 `~` 로 시작하는 것. 생성물은 `bazel-bin/` 접두로 적는 것이
          규칙이다 — 표지가 아니라 규칙이므로 `kg/chunks-kg.ttl` 처럼 적힌 생성물은 없는 경로로 잡힌다.
          `파일:줄` 표기는 파일만 본다. 경로에는 ':' 이 없으므로 그 밖의 ':' 은 라벨로 보고 건너뛴다.
  prose   산문 문체 (STYLEGUIDE §0 단정 서술형, 유저 결정 2026-09-13) — 경어·비격식 종결(습니다·세요·해요·죠 …)이 문장 끝에
          오거나 산문에 느낌표가 있다 (kb_lib.check_prose 가 단일 정의처). 코드 펜스·코드 스팬·HTML 주석·따옴표 안과 `!=`·`![`
          는 산문이 아니다. --waivers(docs/waivers.md)에 게이트 id `prose`(축 파일)로 면제된 문서는 세지 않는다. 추측·구어는
          판정이 필요하므로 게이트가 아니라 consistency ⑦ 보고다.

  report  **보고 모드**(`--report`, 게이트가 아니다) — 문서(위치 인자, 없으면 진입점 문서 넷 `REPORT_DOCS`)가 적은
          수치를 생성물의 같은 이름 값과 쌍으로 대조해 어긋난 쌍을 센다. 위치 인자를 주면 `REPORT_DOCS` 대신 그
          목록을 대조 대상으로 쓰고, **이 모드에서만** 루트 밖 절대 경로를 허용한다(`report_doc_path` — `vv_run`
          이 케이스 자극을 워크스페이스 밖 임시 디렉토리에 두므로, 2026-10-01 vnv 요청). 이름 열넷의 원본은 V&V 기준
          `kb/vv/criteria/document-table-matches-generated.md` 의 대조 대상 목록이고, 현상은 `agt:documentLag`(P18)이다.
          짝짓기는 이름 뒤 24자 창의 수치이므로 근사다 — 이름과 값이 산문으로 떨어져 있으면 쌍이 서지 않는다.
          시점을 선언한 스냅샷 단락은 대조 밖이고, 생성물 원본이 없는 이름은 문서가 생성 명령이나 시각을 병기하면
          기준의 둘째 절로 합격이다. 생성물이 없으면(`bazel-bin` 미빌드) 그 이름을 건너뛴다고 적는다.

출력  FAIL [doccheck|prose] <파일>:<줄>: <종류> <대상> — 근거 · REPORT [doccheck] <파일>:<줄> <이름> 문서 <값> ↔ 생성물 <값>
종료  위반 → EXIT_FAIL · 입력 파일 없음/루트 밖/인자 오류 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)
      `--report` 는 판정이 아니므로 어긋난 쌍이 있어도 0 이다.

사용  doccheck.py [--root DIR] [--waivers FILE] <문서 ...> [--target-only FILE ...]
      bazel run //tools:doccheck -- *.md docs/*.md --target-only docs/agent-knowledge-system-notes.md
      bazel run //tools:doccheck -- --report      # 문서 수치 대 생성물 수치, FAIL 아님 (진입점 문서 넷)
      bazel run //tools:doccheck -- --report /tmp/x/doc.md   # 위치 인자가 있으면 그 문서로 바꾼다, 루트 밖도 된다
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.parse
from pathlib import Path

try:  # 규약 상수·마크다운 헬퍼의 단일 정의처는 kb_lib (STYLEGUIDE §7)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError as e:  # 산문 검사·앵커 규칙의 단일 정의처라 없으면 돌릴 수 없다
        raise SystemExit(f"FAIL [doccheck] kb_lib 을 찾을 수 없다 — {e}")
EXIT_FAIL = kb_lib.EXIT_FAIL      # 판정 실패
EXIT_CONFIG = kb_lib.EXIT_CONFIG  # 파일 없음·인자 오류·읽을 수 없는 입력
EXIT_SKIP = kb_lib.EXIT_SKIP      # 검사 대상 0건 — PASS 가 아니다

TAG = kb_lib.DOCCHECK_GATE
FROZEN = kb_lib.FROZEN_GATE  # 동결 문서 게이트 id — 원본 해시의 단일 정의처는 kb_lib.FROZEN_DOCS
PROSE = kb_lib.PROSE_GATE  # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
PATH_PREFIXES = ("kb/", "kg/", "tools/", "docs/", "defs/", "chunks/", "space/", "harness/", ".claude/")
SKIP_MARKS = ("*", "<", "{", "…", "$", "//", "bazel-bin/", "bazel-out", ".wip")
# 마크다운 구조 헬퍼는 kb_lib 이 원본이다 — doccheck·weave·gen_skills·gendoc 이 같은 앵커 규칙을 쓴다
SCHEME, FENCE, HEADING, CODE_SPAN = kb_lib.MD_SCHEME, kb_lib.MD_FENCE, kb_lib.MD_HEADING, kb_lib.MD_CODE_SPAN
MD_LINK, HTML_TAG = kb_lib.MD_LINK_TEXT, kb_lib.MD_HTML_TAG
prose_lines, slug, anchors, find_links = kb_lib.md_lines, kb_lib.slug, kb_lib.md_anchors, kb_lib.find_links
FILE_LINE = re.compile(r":\d+(?:-\d+)?$")


# ── 경로 해소와 저장소 목록 ────────────────────

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


# ── 링크·앵커·경로 검사와 실행 ────────────────────

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


# ── 게이트 총람의 투영 — 손 표의 `id` 열 대 GATES 리터럴 (M1 단일 정의처, 2026-10-02) ────────────────────

GATE_CATALOGUE_HEADING = "## 게이트 총람"  # docs/tools.md 의 절 머리 — 이 절이 등록부의 투영이다
GATE_CATALOGUE_ID_COLUMN = "id"            # 그 절 표의 열 이름 — 셀의 백틱 토큰이 게이트 id 다
BACKTICK_TOKEN = re.compile(r"`([a-z0-9][a-z0-9_-]*)`")


def gate_catalogue_section(lines: list[str]) -> tuple[list[str], int]:
    """게이트 총람 절의 줄들과 그 시작 줄 번호 — 절은 다음 `## ` 머리에서 끝난다."""
    start = next((i for i, l in enumerate(lines) if l.startswith(GATE_CATALOGUE_HEADING)), -1)
    if start < 0:
        return [], 0
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return lines[start:end], start + 1


def gate_catalogue_ids(section: list[str]) -> set[str]:
    """총람 표의 `id` 열에 적힌 게이트 id 전수 — 열 자리는 헤더 행이 정한다."""
    col = None
    out: set[str] = set()
    for line in section:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            col = cells.index(GATE_CATALOGUE_ID_COLUMN) if GATE_CATALOGUE_ID_COLUMN in cells else None
            continue
        if set(line.strip()) <= set("|-: ") or col is None or len(cells) <= col:
            continue
        out |= {m.group(1) for m in BACKTICK_TOKEN.finditer(cells[col])}
    return out


def check_gate_catalogue(doc: Path, lines: list[str], gates_path: str) -> tuple[list[str], list[str]]:
    """총람이 게이트 등록부의 투영인가 — (게이트 위반, 보고 줄).

    등록부(`defs/kb.bzl` 의 `GATES`·`TOOL_TAGS`)가 원본이고 총람은 손으로 쓴 투영이다 (3단계에서 생성 뷰로
    바꾼다). **게이트로 올리는 방향은 하나다** — 표의 `id` 열에 등록부 밖의 id 가 있으면 FAIL. 그 반대 방향
    (등록됐으나 총람에 없는 id)은 보고다: 총람 표는 노트 6.7절의 규칙 단위로 묶여 있고 하네스 자체의 게이트는
    표 아래 산문이 적으므로, 누락은 저작 판단이 필요하고 기계가 가를 수 없다.
    """
    section, _ = gate_catalogue_section(lines)
    if not section:
        return [f"{doc}: `{GATE_CATALOGUE_HEADING}` 절이 없다 — 게이트 등록부의 투영이 사라졌다"], []
    try:
        gates = kb_lib.load_gates(gates_path)
        tool_tags = kb_lib.load_tool_tags(gates_path)
    except (OSError, ValueError) as e:
        return [f"{doc}: 게이트 등록부를 읽을 수 없다 — {e}"], []
    registered = set(gates) | set(tool_tags)
    in_table = gate_catalogue_ids(section)
    errors = [f"{doc}: 총람 표의 `{GATE_CATALOGUE_ID_COLUMN}` 열에 등록부 밖의 id `{gid}` 가 있다 — "
              f"원본은 {gates_path} 의 GATES 이고 총람은 그 투영이다"
              for gid in sorted(in_table - registered)]
    tokens = {m.group(1) for line in section for m in BACKTICK_TOKEN.finditer(line)}
    absent = sorted(registered - tokens)
    report = [f"report [{TAG}] 총람에 없는 등록 게이트 {len(absent)}개 — {', '.join(absent)}" if absent else
              f"report [{TAG}] 총람이 등록부 {len(registered)}개를 모두 적는다"]
    return errors, report


# ── 보고 모드 — 문서의 수치 대 생성물의 수치 (V&V 기준 document-table-matches-generated, 현상 agt:documentLag) ──────────

REPORT_DOCS = ("docs/roadmap.md", "docs/rules.md", "docs/method.md", "docs/tools.md")
VIEW_PATHS = {"metrics": "bazel-bin/kg/metrics.md", "audit": "bazel-bin/kg/audit.md",
              "candidates": "bazel-bin/kg/link-candidates.md"}
VIEW_BUILD = "bazel build //kg:metrics //kg:audit //kg:link_candidates"
# (이름, 문서에서 이름을 찾는 정규식, ((생성물, 값 한 그룹을 뽑는 정규식), …)) — 이름 열넷의 원본은 V&V 기준 청크의 대조 대상 목록이다.
# 같은 이름의 생성물 값이 둘 이상인 것(매트릭스 채움·후보 링크)은 어느 하나와 같으면 일치로 본다 — 그 애매성 자체가 현상 P21 이다
NUMBER_NAMES = (
    ("살아 있는 청크", r"살아 있는 청크", (("metrics", r"살아 있는 것 ([\d,]*\d)"),)),
    ("고아율", r"고아율", (("metrics", r"## 고아율[\s\S]{0,400}?살아 있는 청크: \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("연결 성분", r"연결 성분", (("metrics", r"연결 성분 \*\*(\d+)\*\*"),)),
    ("매트릭스 채움", r"매트릭스", (("metrics", r"`refines` 매트릭스 채움 (\d+/\d+)"), ("metrics", r"TIM 허용 칸 채움 \*\*(\d+/\d+)"))),
    ("CQ19", r"CQ19", (("metrics", r"executable까지 닿은 요구: \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("CQ20", r"CQ20", (("metrics", r"비요구 청크\(관측·주석 제외\): \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("링크 개체", r"링크 개체", (("metrics", r"링크 개체 \*\*([\d,]*\d)\*\*"), ("audit", r"`agt:Link` \*\*([\d,]*\d)\*\*"))),
    ("확정 링크의 구축·복원 내역", r"확정 링크|구축(?=[ *`]*\d)|복원(?=[ *`]*\d)",
     (("metrics", r"\(확정 ([\d,]*\d) · 후보"), ("metrics", r"구축\(구축 기록 증거뿐\) ([\d,]*\d)"), ("metrics", r"vs 복원 ([\d,]*\d)"))),
    ("복원 비율", r"복원 비율", (("metrics", r"복원 비율 \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("후보 링크", r"후보 링크|링크 후보|후보 수", (("metrics", r"후보 링크 개체\([^)]*\) \*\*(\d+)\*\*"), ("candidates", r"\| 후보 수 \| (\d+) \|"))),
    ("cites", r"cites", (("metrics", r"`agt:cites` (\d+)"),)),
    ("usesConcept", r"usesConcept", (("metrics", r"`agt:usesConcept` ([\d,]*\d)"),)),
    ("확정 문장 커버리지", r"확정 문장 커버리지", (("metrics", r"확정 문장 커버리지\(절 단위\) \*\*([\d,]*\d/[\d,]*\d)"),)),
    ("테스트 수", r"테스트(?=[ *`]*\d)", ()),
)
WINDOW = 24                      # 이름 뒤로 수치를 찾는 창의 글자 수 — 표 셀 하나가 들어가는 폭이다
CELL_END = re.compile(r"[|·]")   # 창의 경계 — 표 셀과 목록 항목의 구분자
NUM_TOKEN = re.compile(r"(\d[\d,]*(?:\.\d+)?)(?:\s*/\s*(\d[\d,]*(?:\.\d+)?))?\s*%?")
# 이름과 값이 붙어 있을 때만 쌍으로 본다 — 사이에 낱말이 들어가면 그 수치는 이 이름의 값이 아니다. 화살표는 예외다("31.6 → 64.5%")
ADJACENT = re.compile(r"[\s*`]{0,3}$|[\s\d.,%/*`]{0,16}[→~][\s*`]{0,3}$")
NOISE = re.compile(r"\d{4}-\d{2}(?:-\d{2})?|\d+(?:\.\d+)?절|§\d+|[A-Za-z]+-?\d+(?:~[A-Za-z]?\d+)?")  # 날짜·절 번호·식별자
CITED = re.compile(r"`bazel [^`]*`|\d{4}-\d{2}-\d{2}")  # 생성 명령이나 시각의 병기 (기준의 둘째 절)
SNAPSHOT = re.compile(r"스냅샷")


def num_key(tok: re.Match) -> tuple:
    """수치 토큰 → 비교 키. 비율은 두 수, 나머지는 한 수이고 백분율 기호는 키에 넣지 않는다."""
    parts = [float(g.replace(",", "")) for g in tok.groups() if g]
    return tuple(parts)


def name_values(line: str, name: re.Pattern) -> list[tuple[str, tuple]]:
    """한 줄에서 이름 뒤 창의 수치 토큰 → [(원문, 키)]. 이름에 붙지 않은 수치와 날짜·절 번호·식별자는 뺀다."""
    out = []
    for m in name.finditer(line):
        window = NOISE.sub(" ", line[m.end():m.end() + WINDOW])
        cut = CELL_END.search(window)
        window = window[:cut.start()] if cut else window
        for tok in NUM_TOKEN.finditer(window):
            gap = window[:tok.start()]
            if ADJACENT.fullmatch(gap):
                out.append((tok.group(0).strip(), num_key(tok)))
    return out


def snapshot_lines(lines: list[str]) -> set[int]:
    """시점을 선언한 스냅샷 단락의 줄 번호 — 기준의 대조 밖이다 (빈 줄로 가른 단락 단위)."""
    out, block = set(), []
    for i, line in enumerate(lines + [""], 1):
        if line.strip():
            block.append(i)
            continue
        text = "\n".join(lines[j - 1] for j in block)
        if block and SNAPSHOT.search(text) and re.search(r"\d{4}-\d{2}-\d{2}", text):
            out |= set(block)
        block = []
    return out


def generated_values(root: Path) -> tuple[dict, list[str], set[str]]:
    """이름 → [(원문, 키, 생성물)] · 읽지 못한 생성물 목록 · 그 미빌드 때문에 값을 못 얻은 이름의 집합."""
    text, missing = {}, []
    for key, rel in VIEW_PATHS.items():
        try:
            text[key] = (root / rel).read_text(encoding="utf-8")
        except OSError:
            missing.append(rel)
    values, skipped = {}, set()
    for label, _doc_re, sources in NUMBER_NAMES:
        found = []
        for src, pattern in sources:
            m = re.search(pattern, text.get(src, ""))
            if m:
                found.append((m.group(1), num_key(NUM_TOKEN.match(m.group(1))), src))
        values[label] = found
        if sources and not found and any(src not in text for src, _ in sources):
            skipped.add(label)
    return values, missing, skipped


def report_numbers(root: Path, repo: Repo, docs: tuple[str, ...] = REPORT_DOCS) -> tuple[list[str], int, int]:
    """(보고 줄, 대조 쌍 수, 어긋난 쌍 수). 쌍은 (문서, 이름) 하나이고 창의 수치 중 하나가 생성물 값과 같으면 일치다.

    `docs` 를 안 주면 진입점 문서 넷(`REPORT_DOCS`)이다. 주면 그 목록으로 바꾼다 — vv_run 처럼 자극을 워크스페이스
    밖 임시 경로에 두는 호출자를 위해 이 목록의 각 항목은 루트 밖 절대 경로일 수 있다(2026-10-01, vnv 요청).
    """
    values, missing, skipped = generated_values(root)
    lines_out = [f"REPORT [{TAG}] 문서 수치 대 생성물 수치 — 원본은 V&V 기준 `kb/vv/criteria/document-table-matches-generated.md` 다"]
    if missing:
        lines_out.append(f"  생성물 없음 {' · '.join(missing)} — 그 이름은 건너뛴다. 먼저 `{VIEW_BUILD}`")
    pairs = off = 0
    for rel in docs:
        if not repo.exists(rel):
            lines_out.append(f"  {rel}: 문서가 없다 — 대조 밖")
            continue
        lines = repo.read(rel)
        skip = snapshot_lines(lines)
        for label, doc_re, _sources in NUMBER_NAMES:
            name = re.compile(doc_re)
            hits = [(ln, raw, key, bool(CITED.search(line)))
                    for ln, line in prose_lines(lines) if ln not in skip
                    for raw, key in name_values(line, name)]
            if not hits:
                continue
            gen = values.get(label) or []
            if label in skipped:  # 생성물이 없어 값을 못 얻은 이름 — 쌍으로 세지 않는다
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} — 생성물 미빌드로 건너뜀")
                continue
            pairs += 1
            if not gen:
                mark = "생성물 원본 없음 · 명령·시각 병기" if any(h[3] for h in hits) else "생성물 원본 없음 · 병기 없음"
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} — {mark}")
                continue
            agree = [g for g in gen if any(h[2] == g[1] for h in hits)]
            shown = " · ".join(f"{g[0]}({g[2]})" for g in gen)
            if agree:
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} ↔ 생성물 {shown} — 일치")
            else:
                off += 1
                where = " · ".join(f"{rel}:{h[0]} {h[1]}" for h in hits)
                lines_out.append(f"  {rel} {label}: 문서 {where} ↔ 생성물 {shown} — **어긋남**")
    lines_out.append(f"REPORT [{TAG}] 대조 문서 {len(docs)} · 이름 {len(NUMBER_NAMES)} · "
                     f"대조 쌍 {pairs} · 어긋난 쌍 {off} — 판정이 아니라 보고다. 고칠 것은 문서다")
    return lines_out, pairs, off


def report_doc_path(path: str, root: Path, workdir: str | None) -> str:
    """보고 모드의 문서 경로 — `to_rel` 과 달리 루트 밖 절대 경로를 거부하지 않는다(2026-10-01, vnv 요청 —
    `vv_run` 이 케이스 자극을 워크스페이스 밖 임시 디렉토리에 두므로 그 파일을 보고 대상으로 줄 수 있어야 한다).
    루트 안이면 상대 경로로 돌려준다(표시가 짧다) — 심볼릭 링크는 따라가지 않는다(runfiles 의 링크가 루트 밖을 가리킨다).
    """
    p = Path(path)
    if not p.is_absolute() and workdir:
        p = Path(workdir) / p
    p = Path(os.path.abspath(p))
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)


def to_rel(path: str, root: Path, workdir: str | None) -> Path:
    p = Path(path)
    if not p.is_absolute() and workdir:
        p = Path(workdir) / p
    p = Path(os.path.abspath(p))  # 심볼릭 링크는 따라가지 않는다 — runfiles 의 링크가 루트 밖을 가리킨다
    try:
        return p.relative_to(root)
    except ValueError:
        raise ValueError(f"{path}: 루트 {root} 밖의 파일이다")


# ── 동결 문서 — 파일의 sha256 대 kb_lib.FROZEN_DOCS (게이트 id frozen, 유저 답 Q15-c) ────────────────────

def check_frozen(files: list[str], root: Path, workdir: str | None) -> list[str]:
    """동결 문서의 sha256 이 `kb_lib.FROZEN_DOCS` 의 고정값과 같은지 본다 — 고치려면 상수를 같은 커밋에서 바꿔야 한다.

    입력에 없는 등록 문서도 위반이다 — 대조할 파일이 runfiles 에 없으면 동결이 판정되지 않는다.
    """
    import hashlib

    errors = []
    given = {to_rel(f, root, workdir).as_posix() for f in files}
    for rel in sorted(set(kb_lib.FROZEN_DOCS) - given):
        errors.append(f"{rel}: 동결 문서가 입력에 없다 — kb_frozen_docs_test 의 docs 에 넣는다")
    for rel in sorted(given):
        want = kb_lib.FROZEN_DOCS.get(rel)
        if want is None:
            errors.append(f"{rel}: kb_lib.FROZEN_DOCS 에 없는 문서다 — 동결하려면 해시를 등록한다")
            continue
        got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if got != want:
            errors.append(f"{rel}: sha256 {got[:12]} 이 고정값 {want[:12]} 과 다르다 — 동결 문서는 고치지 않는다. "
                          f"의도한 정정이면 kb_lib.FROZEN_DOCS 의 값을 같은 커밋에서 바꾼다")
    return errors


# ── 실행 ────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--target-only", action="append", nargs="+", default=[], metavar="FILE",
                    help="링크 대상으로만 쓰고 안에서 나가는 링크는 검사하지 않는 문서 (반복 가능, 검사할 문서 뒤에 둔다)")
    ap.add_argument("--empty-dir", action="append", default=[], metavar="DIR",
                    help="파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지) — kb_doccheck_test 의 empty_dirs")
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help="docs/waivers.md — 게이트 id prose(축 파일)로 면제된 문서의 산문 위반은 세지 않는다. 없으면 면제 없음")
    ap.add_argument("--report", action="store_true",
                    help="보고 모드 — 문서(위치 인자, 없으면 진입점 문서 넷)의 수치를 생성물의 같은 이름 값과 대조한다. "
                         "이 모드의 위치 인자는 루트 밖 절대 경로를 허용한다. 판정이 아니므로 종료 코드는 0 이다")
    ap.add_argument("--gates", default="", metavar="FILE",
                    help="게이트 등록부의 원본 defs/kb.bzl — 주면 `docs/tools.md` 게이트 총람이 그 리터럴의 투영인지 "
                         "본다. 표의 `id` 열에 등록부 밖의 id 가 있으면 FAIL 이고, 반대 방향(총람에 없는 등록 id)은 보고다")
    ap.add_argument("--frozen", action="store_true",
                    help="동결 모드 — 위치 인자의 문서가 kb_lib.FROZEN_DOCS 의 sha256 과 같은지만 본다 (게이트 id frozen)")
    ap.add_argument("files", nargs="*", help="검사할 문서 (--report 면 대조할 문서 — 없으면 진입점 문서 넷)")
    args = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(args.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    if args.frozen:
        try:
            frozen_errors = check_frozen(args.files, root, workdir)
        except (OSError, ValueError) as e:
            print(f"FAIL [{FROZEN}] {e}", file=sys.stderr)
            return EXIT_CONFIG
        for e in frozen_errors:
            print(f"FAIL [{FROZEN}] {e}")
        if frozen_errors:
            return EXIT_FAIL
        print(f"PASS [{FROZEN}] — 동결 문서 {len(kb_lib.FROZEN_DOCS)}개")
        return 0
    repo = Repo(root, set(args.empty_dir))
    if args.report:  # 게이트가 아니다 — 어긋난 쌍이 있어도 0 이다 (현상 agt:documentLag 의 관측 수단)
        # 위치 인자가 있으면 REPORT_DOCS(진입점 문서 넷) 대신 그 목록을 대조 대상으로 쓴다(2026-10-01, vnv 요청) —
        # 이 경로는 루트 밖 절대 경로를 허용한다(`report_doc_path`, `to_rel` 과 달리 거부하지 않는다).
        docs = tuple(report_doc_path(f, root, workdir) for f in args.files) if args.files else REPORT_DOCS
        for line in report_numbers(root, repo, docs)[0]:
            print(line)
        return 0
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
    wpath = args.waivers
    if wpath and not os.path.isabs(wpath) and workdir:
        wpath = os.path.join(workdir, wpath)
    try:
        waivers = kb_lib.load_waivers(wpath) if wpath else []
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] waiver 표 — {e}", file=sys.stderr)
        return EXIT_CONFIG

    errors: list[tuple[str, str]] = []  # (게이트 id, 메시지) — 링크·경로는 doccheck, 산문은 prose
    reports: list[str] = []  # 보고 줄 — 판정이 아니다 (게이트 총람의 누락은 저작 판단이다)
    gates_path = args.gates
    if gates_path and not os.path.isabs(gates_path) and workdir:
        gates_path = os.path.join(workdir, gates_path)
    links = paths = segments = 0
    for doc in sorted(set(docs)):
        lines = repo.read(doc.as_posix())
        links += sum(1 for _, l in prose_lines(lines) for _ in find_links(CODE_SPAN.sub(" ", l)))
        paths += sum(1 for _, l in prose_lines(lines) for m in CODE_SPAN.finditer(l) if m.group(2).strip().startswith(PATH_PREFIXES))
        errors += [(TAG, e) for e in check_links(doc, lines, repo)]
        errors += [(TAG, e) for e in check_paths(doc, lines, repo)]
        text = "\n".join(lines)
        segments += len(kb_lib.prose_segments(text))
        prose_errors, _, _ = kb_lib.check_prose(doc.as_posix(), text, waivers)
        errors += [(PROSE, f"{doc}:{ln}: {reason}") for ln, reason in prose_errors]
        if args.gates and GATE_CATALOGUE_HEADING in text:  # 게이트 총람을 담은 문서 하나 (docs/tools.md)
            catalogue_errors, catalogue_report = check_gate_catalogue(doc, lines, gates_path)
            errors += [(TAG, e) for e in catalogue_errors]
            reports += catalogue_report

    for line in reports:
        print(line)
    if errors:
        for tag, e in errors:
            print(f"FAIL [{tag}] {e}")
        n_prose = sum(1 for tag, _ in errors if tag == PROSE)
        print(f"\nFAIL [{TAG}] — {len(errors)}건 (문서 {len(docs)}개; 링크·경로 {len(errors) - n_prose}, 산문 {n_prose})")
        return EXIT_FAIL
    print(f"PASS [{TAG}] — 문서 {len(docs)}개, 링크 {links}개, 백틱 경로 {paths}개, 산문 조각 {segments}줄")
    return 0


if __name__ == "__main__":
    sys.exit(main())
