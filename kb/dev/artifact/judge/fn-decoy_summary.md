---
id: https://agentic-knowledge-base.dev/id/chunk/44e9469f-eeb7-42a0-890d-1e784afb4dd1
type: artifact
level: executable
title_ko: 함수 decoy_summary (tools/judge.py)
title: function decoy_summary in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/25ad6efd-997a-44a7-b5c4-dc61c13b63ed
---
**함수** — `decoy_summary(hit, seen, total)` 다. 판정 로그의 미끼 검출 결과 줄의 값 (agt:decoyResult) — 미끼가 없으면 해당 없음과 그 사유다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decoy_summary(hit: int, seen: int, total: int) -> str:
    """판정 로그의 미끼 검출 결과 줄의 값 (agt:decoyResult) — 미끼가 없으면 해당 없음과 그 사유다."""
    if not total:
        return f"{kb_lib.EMPTY_NOT_APPLICABLE} — `--decoys` 를 주지 않았다"
    return f"미끼 {total}건 중 응답 대조 {seen}건 · 검출 {hit}건 · 검출률 {kb_lib.pct(hit, seen)}"
```
<!-- 인용 끝 -->
