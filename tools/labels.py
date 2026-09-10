#!/usr/bin/env python3
"""라벨 목록 투영 — 청크 파일들의 head에서 index.md를 생성한다 (노트 5.6절, 부록 E.2).

index.md는 OKF 예약 파일이며 손으로 쓰지 않는다 (유저 결정 2026-09-10 Q4). 라벨 목록이
본문보다 먼저 읽히는 것(4.4절)의 파일 형태이고, 생성물이어야 본문과 어긋나지 않는다.

사용: labels.py --out index.md <청크 파일...>
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # runfiles 안에서 같은 디렉토리의 chunk2kg를 찾는다
from chunk2kg import parse_chunk  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

    groups: dict = defaultdict(list)
    for path in args.files:
        meta, n = parse_chunk(path)
        groups[str(Path(path).parent)].append((meta, n, path))

    out = ["# index — 라벨 목록 (생성 파일, tools/labels.py)", ""]
    for d in sorted(groups):
        out.append(f"## {d}")
        for meta, n, path in sorted(groups[d], key=lambda t: (t[0]["type"], t[0]["level"], t[0]["title_ko"])):
            comp = " · 구성체" if meta.get("composite") else ""
            out.append(f"- [{meta['title_ko']}]({Path(path).name}) — {meta['title']} · {meta['type']}/{meta['level']} · {meta['status']} · {n}줄{comp}")
        out.append("")
    Path(args.out).write_text("\n".join(out), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
