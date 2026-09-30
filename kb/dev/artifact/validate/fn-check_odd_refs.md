---
id: https://agentic-knowledge-base.dev/id/chunk/a0953baf-5b58-4667-ba87-2c4653097756
type: artifact
level: executable
title_ko: 함수 check_odd_refs (tools/validate.py)
title: function check_odd_refs in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/621b8722-ef63-42b3-8470-9560e072a62a
---
**함수** — `check_odd_refs(merged, odd, files)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_odd_refs(merged: Graph, odd: Graph, files: dict[str, Graph]) -> list[str]:
    errors = []
    odd_subjects = {s for s in odd.subjects() if isinstance(s, URIRef)}
    for s, o in merged.subject_objects(AGT.refersTo):
        if o not in odd_subjects:
            errors.append(
                f"[odd-ref] {_where(files, s)}: {merged.qname(s)} 가 ODD에 없는 속성을 참조: {o} (0.4절 — ODD를 먼저 확장하라)"
            )
    return errors
```
<!-- 인용 끝 -->
