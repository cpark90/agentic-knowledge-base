#!/usr/bin/env python3
"""생성 문서 게이트 — 에이전트가 만드는 마크다운의 가독성·건전성 규약 G1~G18 (유저 지시 2026-09-21).

규약의 단일 정의처는 `tools/kb_lib.py` 다 (STYLEGUIDE §7). 이 도구는 그 `check_gendoc` 을 파일들에 돌린다.
생성기가 같은 모듈의 `gendoc_header` 로 머리 블록을 내므로, 출력 형태는 생성 전에 고정되고 파싱·형식 복구가 필요 없다.

  머리 블록  G1 h1 한 줄이 첫 줄이고 `(생성 파일)` 로 끝난다 · G2 생성기와 규약 버전 · G3 생성 시각(ISO 8601 UTC 초) ·
             G4 입력 파일 목록과 내용 지문(SHA-256 앞 12자)과 규모 수치 · G5 질의 · G6 자기 자신을 다시 만드는 명령 ·
             G7 성격 경고 한 줄. 순서가 고정이다.
  본문 서식  G8 제목 계층은 한 단계씩 (MD001) · G9 h1 은 문서당 하나 (MD025) · G10 표의 헤더·열 수·앞뒤 빈 줄
             (MD055·MD056·MD058) · G11 펜스에 언어 (MD040) · G12 본문 120줄 초과면 목차 절 (ISO/IEC/IEEE 26514:2022 9.10.5) ·
             G13 링크의 경로·앵커가 생성물이 놓이는 위치 기준으로 실재 · G14 빈 값은 `없음` 하나.
  건전성     G15 비율은 `n/d = p.p%` — 분모 없는 백분율을 쓰지 않는다 · G18 산문은 단정 서술형 (STYLEGUIDE §0).
             G16 목표 표기·G17 시점 의존 표현은 권장이고 게이트가 아니다.

생성 트리 파일(`.claude/skills/*/SKILL.md`)은 `--deterministic` 대상이다 — 생성 시각과 지문을 넣으면 드리프트
바이트 비교가 매번 깨지므로 그 둘을 빼고, 결정론이 그 자리의 건전성 장치라는 사실을 성격 경고 줄에 적는다.

출력  FAIL [gendoc] <파일>:<줄>: <근거>
종료  위반 → EXIT_FAIL · 입력 파일 없음·루트 밖 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)

사용  gendoc.py [--root DIR] <생성 문서 ...>
      bazel test //:gendoc_test
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:  # 규약의 단일 정의처는 kb_lib (STYLEGUIDE §7)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError as e:
        raise SystemExit(f"FAIL [gendoc] kb_lib 을 찾을 수 없다 — {e}")

TAG = kb_lib.GENDOC_GATE
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--empty-dir", action="append", default=[], metavar="DIR",
                    help="파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지)")
    ap.add_argument("files", nargs="*", help="검사할 생성 문서")
    a = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    empty = {d.strip("/") for d in a.empty_dir}

    def exists(rel: str) -> bool:
        return (not rel) or (root / rel).exists() or rel.strip("/") in empty

    docs: list[Path] = []
    for f in a.files:
        p = Path(f)
        if not p.is_absolute() and workdir:
            p = Path(workdir) / p
        p = Path(os.path.abspath(p))
        try:
            docs.append(p.relative_to(root))
        except ValueError:
            print(f"FAIL [{TAG}] {f}: 루트 {root} 밖의 파일이다", file=sys.stderr)
            return EXIT_CONFIG
    missing = [str(d) for d in docs if not (root / d).is_file()]
    if missing:
        print(f"FAIL [{TAG}] 입력 문서가 없다: " + ", ".join(missing), file=sys.stderr)
        return EXIT_CONFIG
    if not docs:
        print(f"SKIP [{TAG}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    errors: list[str] = []
    for doc in sorted(set(docs)):
        text = (root / doc).read_text(encoding="utf-8")
        errors += [f"{doc}:{ln}: {why}" for ln, why in kb_lib.check_gendoc(doc.as_posix(), text, exists)]
    if errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}")
        print(f"\nFAIL [{TAG}] — {len(errors)}건 (생성 문서 {len(docs)}개). "
              f"규약의 단일 정의처는 `tools/kb_lib.py` 의 `gendoc_header`·`check_gendoc` 이다 — 게이트가 아니라 생성기를 고친다")
        return EXIT_FAIL
    print(f"PASS [{TAG}] — 생성 문서 {len(docs)}개")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
