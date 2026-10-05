---
id: https://agentic-knowledge-base.dev/id/chunk/4cf4ea55-9afe-4a27-9b9b-fb3a38503594
type: artifact
level: executable
title_ko: 함수 parse_args (tools/metrics.py)
title: function parse_args in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/be69bcaa-b921-4a3d-9474-cccf29581b17
---
**함수** — `parse_args()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--notes", default="", help="설계 노트 md — 확정 문장 커버리지(1단계 의미 보존 대리)")
    ap.add_argument("--bodies", nargs="*", default=[], help="청크 파일들 — 노트 절 인용 스캔 · 복합체의 선언 청크(연결 성분·후방 추적)")
    ap.add_argument("--mutations", nargs="*", default=[], help="변이 고정물의 시험 정의 — defs/tests/BUILD.bazel · norm_fixture_test.py (7단계 변이 검출률)")
    ap.add_argument("--spaces", nargs="*", default=[], help="설계 공간 그래프(//space:design_space) — 연결 성분의 후보 링크 · 결정 완결률의 후보 결정 (유저 결정 Q60-a)")
    ap.add_argument("--residency", required=True, help="plane·수준·수준 허용표의 원본 defs/kb.bzl (M1 단일 정의처)")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    return a
```
<!-- 인용 끝 -->
