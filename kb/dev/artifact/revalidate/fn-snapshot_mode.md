---
id: https://agentic-knowledge-base.dev/id/chunk/c97d3b27-6804-4dd0-9ac1-4ab2908eaeeb
type: artifact
level: executable
title_ko: 함수 snapshot_mode (tools/revalidate.py)
title: function snapshot_mode in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `snapshot_mode(a)` 다. 스냅숏 비교의 입력 문제 — 없으면 None.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def snapshot_mode(a) -> str | None:
    """스냅숏 비교의 입력 문제 — 없으면 None. 한쪽만 주거나 없는 경로를 주면 비교가 성립하지 않는다."""
    base, head = a.base_dir + a.base_files, a.head_dir + a.head_files
    if bool(base) != bool(head):
        return "스냅숏 비교는 base(`--base-dir`·`--base-files`)와 head(`--head-dir`·`--head-files`)를 둘 다 준다"
    missing = [d for d in a.base_dir + a.head_dir if not Path(d).is_dir()] + [f for f in a.base_files + a.head_files if not Path(f).is_file()]
    return f"없는 경로: {' · '.join(missing)}" if missing else None
```
<!-- 인용 끝 -->
