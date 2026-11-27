---
id: https://agentic-knowledge-base.dev/id/chunk/71602697-5642-4dd6-af8c-54ac2af76cb7
type: artifact
level: executable
title_ko: 함수 label_rows (tools/belief_calibration.py)
title: function label_rows in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e]
part_of: https://agentic-knowledge-base.dev/id/composite/1edd84f8-3e8d-4183-996c-4666aefe4a4a
---
**함수** — `label_rows(path)` 다. 라벨 기록 하나 → 항목들 [{문항, 링크 IRI, 라벨(int), 독립(bool), 기록}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_rows(path: Path) -> list[dict]:
    """라벨 기록 하나 → 항목들 [{문항, 링크 IRI, 라벨(int), 독립(bool), 기록}]. 표 머리가 LABEL_COLUMNS 를 모두 갖는 첫 표를 읽는다.
    표가 없거나 라벨이 0·1 이 아니면 ValueError 다."""
    lines = kb_lib.chunk_body(path.read_text(encoding="utf-8")).split("\n")
    for i, line in enumerate(lines):
        cols = [c.strip() for c in line.strip().split("|")[1:-1]] if line.strip().startswith("|") else []
        if not all(c in cols for c in LABEL_COLUMNS):
            continue
        rows = []
        for row in lines[i + 2:]:
            if not row.strip().startswith("|"):
                break
            cells = dict(zip(cols, (c.strip().strip("`").strip() for c in row.strip().split("|")[1:-1])))
            if cells.get("라벨") not in ("0", "1"):
                raise ValueError(f"{path}: 문항 {cells.get('문항')} 의 라벨 {cells.get('라벨')!r} 이 0 또는 1 이 아니다")
            rows.append({"문항": cells["문항"], "link": cells["링크 IRI"], "y": int(cells["라벨"]),
                         "independent": cells["지위"].startswith(INDEPENDENT), "record": path})
        return rows
    raise ValueError(f"{path}: 라벨 표(열 {' · '.join(LABEL_COLUMNS)})가 없다")
```
<!-- 인용 끝 -->
