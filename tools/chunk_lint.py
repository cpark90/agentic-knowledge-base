#!/usr/bin/env python3
"""청크·명명·산문 린트.

  --chunks <files>   청크 본문(assertion) 파일 검사 (노트 4.1절):
                     본문 42줄 이하. YAML frontmatter(head 메타데이터)와
                     끝의 빈 줄은 본문으로 세지 않는다.
                     .md 청크는 산문 문체(STYLEGUIDE §0 단정 서술형, 2026-09-13)도 본다 — 경어·비격식 종결이 문장 끝에
                     오거나 산문에 느낌표가 있으면 위반(kb_lib.check_prose, 게이트 id `prose`). 코드·따옴표·주석 안과
                     `!=`·`![` 는 산문이 아니다. TTL 청크는 산문 검사 대상이 아니다. 추측·구어는 consistency ⑦ 보고다.
                     type: decision 인 .md 는 역할 표지(STYLEGUIDE §4, 게이트 id `decision-role`)도 본다 — 본문 첫 산문 줄이
                     굵은 표지로 시작해야 한다. conclusion.md·rationale.md·alternatives.md 는 각각 **결론**·**근거**·**대안**,
                     그 밖의 파일명(단일 파일 옛 결정 chunks/decision/d-*.md)은 **결론** 이다. 표지 안의 한정어(**대안 없음**)는
                     같은 표지다(kb_lib.DECISION_ROLE_MARKER). status: deprecated 는 대상이 아니다.
  --ttl <files>      TTL 파일명이 산출물 접미사 규약(0.2절)을 따르는지 검사.
  --waivers <file>   docs/waivers.md — 게이트 id `prose`(축 파일)로 면제된 파일의 산문 위반은 세지 않는다. 없으면 면제 없음.

출력·종료: `FAIL [chunk|naming] <경로>: <메시지>` · `FAIL [prose|decision-role] <경로>:<줄>: <이유>` + EXIT_FAIL.
파일 없음·waiver 표 오류는 EXIT_CONFIG, 대상 0건은 EXIT_SKIP (PASS 아님).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from tools import kb_lib  # bazel runfiles 경로
except ImportError:
    import kb_lib  # 직접 실행

ALLOWED_TTL_SUFFIXES = kb_lib.ALLOWED_TTL_SUFFIXES
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건
PROSE = kb_lib.PROSE_GATE                        # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
DECISION_ROLE = kb_lib.DECISION_ROLE_GATE        # 결정 역할 표지 게이트 id (STYLEGUIDE §4)

MAX_BODY_LINES = 42  # 4.1절 — 컨텍스트 한계 200줄의 약 1/5

_FM_FIELD = re.compile(r"^(type|status):\s*(\S+)")  # 역할 표지 판정에 필요한 frontmatter 키 둘 — 전체 파싱은 chunk2kg 의 몫


def split_frontmatter(text: str) -> tuple[dict[str, str], list[str], int]:
    """(frontmatter 의 type·status, 본문 줄들, 본문 첫 줄의 파일 줄 번호). frontmatter 가 없으면 본문은 전체다."""
    lines = text.splitlines()
    fields: dict[str, str] = {}
    if not lines or lines[0].strip() != "---":
        return fields, lines, 1
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return fields, lines, 1
    for raw in lines[1:end]:
        m = _FM_FIELD.match(raw)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields, lines[end + 1 :], end + 2


def check_decision_role(path: Path, text: str) -> list[tuple[int, str]]:
    """결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

    type: decision 인 .md 만 대상이고 status: deprecated 는 제외한다. 본문 첫 산문 줄(빈 줄 제외 첫 줄)이 굵은 표지로 시작해야 하며,
    표지는 파일 stem 이 정한다 — conclusion 결론 · rationale 근거 · alternatives 대안, 그 밖(단일 파일 옛 결정)은 결론.
    굵은 span 이 역할 낱말로 시작하면 한정어가 붙어도 같은 표지다(**대안 없음**·**대안 — 미확정**, kb_lib 주석의 첫 실행 실태).
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "decision" or fields.get("status") == "deprecated":
        return []
    expected = kb_lib.DECISION_ROLE_MARKERS.get(path.stem, kb_lib.DECISION_SINGLE_FILE_MARKER)
    for offset, line in enumerate(body):
        if not line.strip():
            continue
        m = kb_lib.DECISION_ROLE_MARKER.match(line)
        if m and m.group(1) == expected:
            return []
        found = f'"**{m.group(1)}…**"' if m else f"{line.strip()[:40]!r}"
        return [(start + offset, f"본문 첫 산문 줄이 **{expected}** 표지로 시작해야 한다 (STYLEGUIDE §4 역할 태그) — 실제 {found}")]
    return [(start, f"본문이 비어 **{expected}** 표지가 없다 (STYLEGUIDE §4)")]


def body_lines(path: Path, text: str) -> int:
    """본문 줄 수. head에 해당하는 것(md frontmatter, ttl의 @prefix·주석)은 세지 않는다."""
    lines = text.splitlines()
    if path.suffix == ".ttl":
        return sum(
            1
            for l in lines
            if l.strip() and not l.lstrip().startswith(("#", "@prefix", "@base"))
        )
    # 산문 계열: frontmatter 제거
    if lines and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
            lines = lines[end + 1 :]
        except ValueError:
            pass
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return len(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--ttl", nargs="*", default=[])
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help="docs/waivers.md — 게이트 id prose(축 파일)로 면제된 파일의 산문 위반은 세지 않는다. 없으면 면제 없음")
    args = ap.parse_args()

    if not args.chunks and not args.ttl:
        print("SKIP [chunk_lint] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    try:
        waivers = kb_lib.load_waivers(args.waivers) if args.waivers else []
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk_lint] waiver 표 — {e}")
        return EXIT_CONFIG

    errors = []
    prose_files = 0
    decision_files = 0  # 역할 표지 검사 대상(살아 있는 결정)의 수 — PASS 줄의 실태

    for f in args.chunks:
        p = Path(f)
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            print(f"FAIL [chunk] {f}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        n = body_lines(p, text)
        if n > MAX_BODY_LINES:
            errors.append(
                f"[chunk] {f}: 본문 {n}줄 > {MAX_BODY_LINES}줄 — 분할하라 (4.10절 분할 신호)"
            )
        if p.suffix == ".md":  # 산문 문체·결정 역할 표지 — TTL 은 대상이 아니다
            prose_files += 1
            prose_errors, _, _ = kb_lib.check_prose(f, text, waivers)
            errors += [f"[{PROSE}] {f}:{ln}: {reason}" for ln, reason in prose_errors]
            fields, _, _ = split_frontmatter(text)
            if fields.get("type") == "decision" and fields.get("status") != "deprecated":
                decision_files += 1
            errors += [f"[{DECISION_ROLE}] {f}:{ln}: {reason}" for ln, reason in check_decision_role(p, text)]

    for f in args.ttl:
        stem = Path(f).stem
        if not any(stem == s.lstrip("-") or stem.endswith(s) for s in ALLOWED_TTL_SUFFIXES):
            errors.append(
                f"[naming] {f}: 접미사 규약 위반 — {', '.join(ALLOWED_TTL_SUFFIXES)} 중 하나로 끝나야 한다 (0.2절)"
            )

    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [chunk_lint] — {len(errors)}건")
        return EXIT_FAIL

    print(f"PASS [chunk_lint] — 청크 {len(args.chunks)}개 (산문 검사 {prose_files}개, 결정 역할 표지 {decision_files}개), TTL {len(args.ttl)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
