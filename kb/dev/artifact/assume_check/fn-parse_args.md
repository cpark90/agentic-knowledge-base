---
id: https://agentic-knowledge-base.dev/id/chunk/a3ac2cde-76e2-4d4e-b75f-ecd7060abd39
type: artifact
level: executable
title_ko: 함수 parse_args (tools/assume_check.py)
title: function parse_args in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `parse_args()` 다. 명령줄 인자 — 파서가 곧 형식의 정의처다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_args():
    """명령줄 인자 — 파서가 곧 형식의 정의처다 (무엇을 하는가는 모듈 docstring 이 적는다)."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--odd", default="kb/odd/project-odd.yml", help="OpenODD 문서 (워크스페이스 상대)")
    ap.add_argument("--break", dest="broken", action="append", default=[], metavar="COND",
                    help="이 조건(id:cond-… 의 슬러그 또는 ODD 속성명)을 out 으로 가정한다 — 인위 파괴 실험. 반복 가능")
    ap.add_argument("--record", action="store_true", help=f"결과를 관측으로 {MEMORY_DIR}/obs-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("ttl", nargs="*", help=f"그래프 TTL (기본: {' '.join(DEFAULT_TTL)})")
    return ap.parse_args()
```
<!-- 인용 끝 -->
