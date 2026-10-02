---
id: https://agentic-knowledge-base.dev/id/chunk/d63b7431-1668-41dd-b872-475b380f0fd4
type: artifact
level: executable
title_ko: 함수 parse_args (tools/revalidate.py)
title: function parse_args in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `parse_args()` 다. 명령줄 인자 — 파서가 곧 형식의 정의처다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_args():
    """명령줄 인자 — 파서가 곧 형식의 정의처다."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="HEAD", help="비교할 git 리비전 (기본 HEAD)")
    ap.add_argument("--universe", default="//...", help="rdeps 의 우주")
    ap.add_argument("--out", default="")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root(워크스페이스) 기준")
    return ap.parse_args()
```
<!-- 인용 끝 -->
