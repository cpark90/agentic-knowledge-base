#!/usr/bin/env python3
"""청크·명명 린트.

  --chunks <files>   청크 본문(assertion) 파일 검사 (노트 4.1절):
                     본문 42줄 이하. YAML frontmatter(head 메타데이터)와
                     끝의 빈 줄은 본문으로 세지 않는다.
  --ttl <files>      TTL 파일명이 산출물 접미사 규약(0.2절)을 따르는지 검사.

출력·종료: `FAIL [chunk|naming] <경로>: <메시지>` + EXIT_FAIL. 파일 없음은 EXIT_CONFIG, 대상 0건은 EXIT_SKIP (PASS 아님).
"""

from __future__ import annotations

import argparse
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

MAX_BODY_LINES = 42  # 4.1절 — 컨텍스트 한계 200줄의 약 1/5


def body_lines(path: Path) -> int:
    """본문 줄 수. head에 해당하는 것(md frontmatter, ttl의 @prefix·주석)은 세지 않는다."""
    lines = path.read_text(encoding="utf-8").splitlines()
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
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--ttl", nargs="*", default=[])
    args = ap.parse_args()

    if not args.chunks and not args.ttl:
        print("SKIP [chunk_lint] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    errors = []

    for f in args.chunks:
        try:
            n = body_lines(Path(f))
        except OSError as e:
            print(f"FAIL [chunk] {f}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        if n > MAX_BODY_LINES:
            errors.append(
                f"[chunk] {f}: 본문 {n}줄 > {MAX_BODY_LINES}줄 — 분할하라 (4.10절 분할 신호)"
            )

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

    print(f"PASS [chunk_lint] — 청크 {len(args.chunks)}개, TTL {len(args.ttl)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
