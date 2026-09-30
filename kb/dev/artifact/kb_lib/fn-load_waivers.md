---
id: https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f
type: artifact
level: executable
title_ko: 함수 load_waivers (tools/kb_lib.py)
title: function load_waivers in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf
---
**함수** — `load_waivers(path)` 다. docs/waivers.md 의 표를 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_waivers(path: str | Path) -> list[dict]:
    """docs/waivers.md 의 표를 읽는다 → [{gate, targets, axis, reason, judge, date, line}].

    헤더가 WAIVER_COLUMNS 와 다르거나 축이 WAIVER_AXES 밖이면 ValueError, 파일이 없으면 FileNotFoundError —
    둘 다 설정 문제(EXIT_CONFIG)이지 판정 실패가 아니다. `대상` 은 ` · ` 로 구분된 여러 값.
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"{path}: waiver 표가 없다")
    header_seen, out = False, []
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.lstrip().startswith("|"):
            continue
        cells = _cells(line)
        if not header_seen:
            if tuple(cells) != WAIVER_COLUMNS:
                raise ValueError(f"{path}:{n}: waiver 표의 열은 | {' | '.join(WAIVER_COLUMNS)} | 여야 한다 — 실제 {cells}")
            header_seen = True
            continue
        if all(re.fullmatch(r":?-+:?", c) for c in cells) or tuple(cells) == WAIVER_COLUMNS:
            continue
        if len(cells) != len(WAIVER_COLUMNS):
            raise ValueError(f"{path}:{n}: 열이 {len(cells)}개다 (필요 {len(WAIVER_COLUMNS)})")
        gate, targets, axis, reason, judge, date = (c.strip("`") for c in cells)
        if axis not in WAIVER_AXES:
            raise ValueError(f"{path}:{n}: 축 {axis!r} 는 {'|'.join(WAIVER_AXES)} 중 하나여야 한다")
        out.append({"gate": gate, "axis": axis, "reason": reason, "judge": judge, "date": date, "line": n,
                    "targets": [t.strip().strip("`") for t in re.split(r"\s*·\s*", targets) if t.strip()]})
    if not header_seen:
        raise ValueError(f"{path}: waiver 표가 없다")
    return out
```
<!-- 인용 끝 -->
