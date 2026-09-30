---
id: https://agentic-knowledge-base.dev/id/chunk/6879310b-514b-406a-b81d-1a7c1118de53
type: artifact
level: executable
title_ko: 함수 main (tools/stamp.py)
title: function main in tools/stamp.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-stamp}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:27:50Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9de96dc9-03ab-40b9-a90a-4481f8f9deb7
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("registries", nargs="+", help="등록부 사이드카 경로 (<소스>.chunks.yml)")
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--rev", default="", help="도장의 리비전. 없으면 git HEAD (소스가 커밋되어 있어야 한다)")
    ap.add_argument("--at", default="", help="도장 시각 (ISO 8601 UTC 초 해상도). 없으면 지금")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    at = a.at or kb_lib.now_utc()
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
```
<!-- 인용 끝 -->
