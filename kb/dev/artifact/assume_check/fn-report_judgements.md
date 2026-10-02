---
id: https://agentic-knowledge-base.dev/id/chunk/31bc1a35-7001-4936-9b80-a0bfffed1335
type: artifact
level: executable
title_ko: 함수 report_judgements (tools/assume_check.py)
title: function report_judgements in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/3d72bcbf-9fce-4ada-9c3b-fff4759fa5fd, https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9]
part_of: https://agentic-knowledge-base.dev/id/composite/5dac7240-2471-496d-a65c-f55a8a067a41
---
**함수** — `report_judgements(g, live, asms, impact, cond_rows, broke_names)` 다. 조건 판정 표 · 가정 표 · 깨진 가정마다의 직접 영향 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_judgements(g: Graph, live: set, asms: list[dict], impact: dict, cond_rows: list[dict],
                      broke_names: list[str]) -> list[str]:
    """조건 판정 표 · 가정 표 · 깨진 가정마다의 직접 영향 집합."""
    body = ["## 조건 판정 (odd_check 와 같은 판정)", "", "| 조건 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"]
    body += [f"| `{local(r['iri'])}` | {r['title_ko']} | {r['grade']} | {r['state']}{' (--break)' if r['name'] in broke_names else ''} |" for r in cond_rows]
    body += ["", "## 가정 — 판정식은 참조 조건 판정의 연언, 등급은 그 최저", "",
            "| 가정 | 판정 유형 | 판정식 | 등급 | 상태 | assumes 하는 살아 있는 청크 | 직접 영향 | suspect 후보 (1홉 / 전이) |",
            "|---|---|---|---|---|---|---|---|"]
    for x in asms:
        n_assumes = sum(1 for c in g.subjects(AGT.assumes, x["iri"]) if c in live)
        d, h1, tr = impact[x["iri"]]
        body.append(f"| `{local(x['iri'])}` {x['label']} | {x['kind']} | {x['expr']} | {x['grade']} | **{x['status']}** | {n_assumes} | {len(d)} | {len(h1)} / {len(tr)} |")
    for x in asms:
        d, h1, tr = impact[x["iri"]]
        if not d:
            continue
        body += ["", f"### 직접 영향 집합 — `{local(x['iri'])}` ({len(d)}건, suspect 후보 전이 {len(tr)}건)", ""]
        body += [f"- {label_of(g, c)} (`{local(c)}`)" for c in sorted(d, key=lambda c: label_of(g, c))[:40]]
        if len(d) > 40:
            body.append(f"- … 외 {len(d) - 40}건")
    return body
```
<!-- 인용 끝 -->
