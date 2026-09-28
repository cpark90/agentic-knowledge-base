#!/usr/bin/env python3
"""라벨 목록 뷰 — 청크 파일들의 head에서 index.md를 생성한다 (노트 5.6절, 부록 E.2).

index.md는 OKF 예약 파일이며 손으로 쓰지 않는다 (유저 결정 2026-09-10 Q4). 라벨 목록이
본문보다 먼저 읽히는 것(4.4절)의 파일 형태이고, 생성물이어야 본문과 어긋나지 않는다.
절은 plane 디렉토리(h2)와 그 안의 항목 디렉토리(h3)로 갈리고, 링크는 저장소 루트 기준
경로다 — 생성물이 전 패키지를 한 파일로 합치므로 파일명 상대 링크는 성립하지 않는다 (규약 G13).

사용: labels.py --out index.md <청크 파일...>
"""
import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # runfiles 안에서 같은 디렉토리의 chunk2kg를 찾는다
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402


def plane_of(group: str) -> str:
    """항목 디렉토리 → plane 디렉토리. 결정 복합체처럼 디렉토리가 한 겹 더 있으면 그 부모가 plane 이다."""
    return str(Path(group).parent) if len(Path(group).parts) > 3 else group


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(kb_index 매크로가 명시로 넘긴다)")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [labels] {args.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
        return kb_lib.EXIT_CONFIG

    groups: dict = defaultdict(list)
    for path in args.files:
        meta, n = parse_chunk(path)
        groups[str(Path(path).parent)].append((meta, n, path))
    by_plane: dict = defaultdict(list)
    for d in sorted(groups):
        by_plane[plane_of(d)].append(d)

    head = kb_lib.gendoc_header(
        "index", "라벨 목록", "tools/labels.py",
        "청크 파일마다 frontmatter 의 한글 라벨 · 영문 라벨 · plane/level · 상태 · 본문 줄 수 · 복합체 여부를 "
        "plane 디렉토리와 항목 디렉토리로 묶어 — 라벨 목록이 본문보다 먼저 읽히는 것의 파일 형태다 (4.4절)",
        "bazel build //kb/dev:index", args.files,
        f"청크 {len(args.files)}개 · 디렉토리 {len(groups)}개",
        kb_lib.gendoc_view_notice("각 청크의 frontmatter"), input_kind="청크 파일")

    out: list[str] = []
    for plane in sorted(by_plane):
        out += [f"## {plane}", ""]
        for d in by_plane[plane]:
            if d != plane:
                out += [f"### {d}", ""]
            out.append(kb_lib.GENDOC_QUOTE_OPEN)  # 라벨은 청크에서 그대로 옮긴 값이다 — 생성기가 고쳐 쓰지 않는다
            for meta, n, path in sorted(groups[d], key=lambda t: (t[0]["type"], t[0]["level"], t[0]["title_ko"])):
                comp = " · 복합체" if meta.get("composite") else ""
                # 링크는 저장소 루트 기준이다 — 이 파일은 전 패키지를 한 파일로 합치므로 파일명 상대 링크가 성립하지 않는다 (G13)
                out.append(f"- [{meta['title_ko']}](/{kb_lib.gendoc_input_name(path)}) — {meta['title']} · "
                           f"{meta['type']}/{meta['level']} · {meta['status']} · {n}줄{comp}")
            out += [kb_lib.GENDOC_QUOTE_CLOSE, ""]
    Path(args.out).write_text(kb_lib.gendoc_assemble(head, out, args.files, input_kind="청크 파일"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
