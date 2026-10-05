#!/usr/bin/env python3
"""테스트 통과 도장 — 추출된 코드 청크의 `verified` 를 사람이 아니라 게이트가 찍는다 (p7-code-extraction-direction "도장").

`artifact` plane 의 `verified` 는 사람 검토가 아니라 **테스트 통과**다. 코드는 자주 바뀌므로 사람 도장을 요구하면
수정마다 `generatedAtTime ≤ verifiedAt` 게이트가 걸린다. 판정 주체를 바꾸는 것이지 검사를 약화하는 것이 아니다 —
사람 도장은 결정·요구에 남는다 (`tools/endorse.py`).

**규범: `bazel test //...` 가 종료 0 으로 끝난 뒤에만 이 도구를 돌린다.** 이 도구는 자기 안에서 `bazel test` 를
부르지 않는다 — `bazel run` 안의 중첩 Bazel 호출은 같은 출력 기반을 잠그기 때문이다. 그래서 도장은 호출자의
주장이고, 도구가 지키는 것은 **그 주장이 가리키는 내용이 실재하는가** 하나다: `--rev` 를 주지 않으면 소스 파일이
커밋되어 있어야 하고(작업 트리가 더러우면 리비전이 그 내용을 가리키지 않는다) 도장에는 그때의 소스 해시를 함께
적는다. 소스가 그 뒤에 바뀌면 추출기가 `verified` 를 **빼서** 낸다 — 수정 뒤 미검증이고 재판정이 자동이다.

도장의 자리는 등록부(`<소스>.chunks.yml`)의 `tested` 다. 생성 청크는 뷰이므로 거기에 손으로 적을 자리가 없다.
추출기가 `tested.source_hash` 가 지금 소스와 같을 때만 `verified: [{by: process:bazel-test, at: <tested.at>}]` 를
모든 생성 청크에 낸다. 리비전은 등록부와 파일 청크 본문에 남는다 — `agt:verifiedAt`·`agt:verifiedBy` 밖의 키를
head 그래프가 받지 않으므로 그래프에 리비전을 넣지 않는다.

사용: bazel run //tools:stamp -- tools/kb_lib.chunks.yml [--rev <리비전>] [--at <ISO 8601 UTC>] [--root <루트>]
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리.
      도장 뒤에 `bazel run //tools:extract -- <소스>` 와 `python3 tools/gen_build.py --root .` 를 돌린다.
출력·종료: 거부는 `FAIL [stamp] <경로>: <근거>` + EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
`--at` 이 지금보다 뒤이면 거부한다 — 미래 시각의 도장은 테스트 통과보다 앞선 주장이 되고, 게이트는 시계에 의존할 수 없어
(재현성) 이 판정은 쓰는 시점에만 할 수 있다.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.extract import dump_registry, load_registry, source_digest
except ImportError:
    import kb_lib
    from extract import dump_registry, load_registry, source_digest

TAG = kb_lib.STAMP_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG


# ── 리비전 확인과 등록부 도장 ────────────────────

def git(root: Path, *args: str) -> tuple[int, str]:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=30)
        return out.returncode, out.stdout.strip()
    except (OSError, subprocess.SubprocessError) as e:
        return 1, str(e)


def stamp_one(root: Path, reg_path: Path, rev: str, at: str) -> tuple[str, str]:
    """등록부 하나에 도장을 찍는다 → (소스 경로, 리비전). 커밋되지 않은 소스는 `--rev` 없이 거부한다."""
    reg = load_registry(reg_path)
    if not reg["source"]:
        raise ValueError(f"{reg_path}: 등록부에 `source` 가 없다 — 도장의 대상을 알 수 없다")
    src = root / reg["source"]
    if not src.exists():
        raise ValueError(f"{reg_path}: 소스 {reg['source']} 가 없다")
    if not rev:
        code, dirty = git(root, "status", "--porcelain", "--", reg["source"])
        if code != 0:
            raise ValueError(f"{reg_path}: git 상태를 읽을 수 없다 — {dirty}. 리비전을 아는 호출자가 `--rev` 로 준다")
        if dirty:
            raise ValueError(f"{reg_path}: 소스 {reg['source']} 가 커밋되지 않았다 — 도장의 리비전이 그 내용을 가리키지 "
                             f"않는다. 커밋한 뒤 다시 돌리거나, 리비전을 아는 호출자가 `--rev` 로 준다")
        code, rev = git(root, "rev-parse", "HEAD")
        if code != 0 or not rev:
            raise ValueError(f"{reg_path}: git 리비전을 읽을 수 없다 — `--rev` 로 준다")
    # 해시는 추출기와 같은 함수다 — 질의 디렉토리(EXTRACTED_QUERY_DIRS)는 파일 전부의 해시이고 둘이 갈리면 도장이 무효가 된다
    reg["tested"] = {"rev": rev, "at": at, "source_hash": source_digest(src)}
    reg_path.write_text(dump_registry(reg), encoding="utf-8")
    return reg["source"], rev


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("registries", nargs="+", help="등록부 사이드카 경로 (<소스>.chunks.yml)")
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--rev", default="", help="도장의 리비전. 없으면 git HEAD (소스가 커밋되어 있어야 한다)")
    ap.add_argument("--at", default="", help="도장 시각 (ISO 8601 UTC 초 해상도). 없으면 지금")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    at = a.at or kb_lib.now_utc()
    if a.at:
        try:
            when = datetime.fromisoformat(a.at.strip().replace("Z", "+00:00"))
        except ValueError:
            print(f"FAIL [{TAG}] --at {a.at!r}: ISO 8601 이 아니다", file=sys.stderr)
            return EXIT_FAIL
        when = when.astimezone() if when.tzinfo is None else when
        if when > datetime.now(timezone.utc):
            print(f"FAIL [{TAG}] --at {a.at}: 지금보다 뒤다 — 미래 시각의 도장은 쓰지 않는다 (`date -Iseconds` 실측값)", file=sys.stderr)
            return EXIT_FAIL
    done = []
    for rel in a.registries:
        reg_path = root / rel if not Path(rel).is_absolute() else Path(rel)
        try:
            done.append(stamp_one(root, reg_path, a.rev, at))
        except OSError as e:
            print(f"FAIL [{TAG}] {reg_path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except ValueError as e:
            print(f"FAIL [{TAG}] {e}", file=sys.stderr)
            return EXIT_FAIL
    for src, rev in done:
        print(f"도장 {src} — 리비전 {rev[:12]} · {at}. `bazel run //tools:extract -- {src}` 와 "
              f"`python3 tools/gen_build.py --root .` 를 돌려 청크에 반영하라")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
