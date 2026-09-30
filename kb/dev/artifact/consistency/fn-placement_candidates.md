---
id: https://agentic-knowledge-base.dev/id/chunk/9fd939d6-21cd-4952-92e8-2091cf6b93a7
type: artifact
level: executable
title_ko: 함수 placement_candidates (tools/consistency.py)
title: function placement_candidates in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/38dd33c9-2317-4c0a-a596-5bb97eecca1b
---
**함수** — `placement_candidates(it)` 다. 자리 후보 — [(현재 슬롯, 발견된 다른 슬롯 표지, 그 줄)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def placement_candidates(it: dict) -> list[tuple[str, str, str]]:
    """자리 후보 — [(현재 슬롯, 발견된 다른 슬롯 표지, 그 줄)]. 슬롯이 둘 미만인 청크는 대상이 아니다 (⑪)."""
    slots = it.get("slots") or []
    if len(slots) < 2:
        return []
    lines = it["body"].splitlines()
    regions = slot_regions(it["body"])
    out = []
    for own, idxs in regions.items():
        others = [m for m in slots if m != own]
        for i in idxs:
            line = lines[i]
            legit = _legitimate_spans(line)
            for other in others:
                for m in _placement_regex(other).finditer(line):
                    if any(a <= m.start() < b for a, b in legit):
                        continue  # 이 줄의 정당한 필드 선언이다 — 자리 밖 출현이 아니다
                    out.append((own, other, line.strip()[:160]))
                    break
    return out
```
<!-- 인용 끝 -->
