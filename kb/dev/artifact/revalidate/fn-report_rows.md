---
id: https://agentic-knowledge-base.dev/id/chunk/520a6151-01ee-4804-9141-0829d19e2768
type: artifact
level: executable
title_ko: 함수 report_rows (tools/revalidate.py)
title: function report_rows in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `report_rows(per_chunk, rows, objs, head_only, unparsable, unread, label)` 다. 표 셋과 꼬리말 — 변경 청크 · 재판정 대상 · 재판정 링크 개체.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_rows(per_chunk: list, rows: list, objs: list, head_only: list, unparsable: list,
                unread: list, label) -> list[str]:
    """표 셋과 꼬리말 — 변경 청크 · 재판정 대상 · 재판정 링크 개체."""
    body = ["| 변경 청크 | 변경 | 라벨 | 링크(양방향) | 하류(직접/전이) | 호출부 | verified | 비고 |",
            "|---|---|---|---|---|---|---|---|"]
    for path, kind, ko, nl, (nd, nt), nc, v, note in per_chunk:
        body.append(f"| `{path}` | {kind} | {ko or kb_lib.NONE_MARK} | {nl} | {nd}/{nt} | {nc} | "
                    f"{'있음' if v else kb_lib.NONE_MARK} | {note or kb_lib.NONE_MARK} |")  # G14 — 빈 셀을 두지 않는다
    body += ["", "## 재판정 대상", "", "| 변경 청크 | 종류 | 방향 | 상대 | 출처 |", "|---|---|---|---|---|"]
    body += [f"| `{p}` | {k} | {d} | {t} | {src} |" for p, k, d, t, src in rows] or ["| " + " | ".join([kb_lib.NONE_MARK] * 3 + [f"재판정 대상 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body += ["", "## 재판정 대상 링크 개체 — 본문 해시 변경 → 링크 재판정 (노트 9.11절: 상태는 평가 결과다)", "",
             "| 링크 개체 | 종류 | 출발 | 도착 | 바뀐 끝 | 유도 상태 |", "|---|---|---|---|---|---|"]
    body += [f"| `{kb_lib.compact_iri(l)}` | `{k}` | {label(f)} | {label(t)} | {side} | {kb_lib.LINK_STATE_SUSPECT} |"
             for l, k, f, t, side in objs] \
            or ["| " + " | ".join([kb_lib.NONE_MARK] * 4 + [f"재판정 링크 개체 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body.append("")
    if head_only:
        body += ["head 만 바뀐 청크 (링크 키 변경이 있으면 표시): " + " · ".join(f"`{p}`" + (f" [{', '.join(ks)}]" if ks else "") for p, ks in head_only[:20])
                + (f" … 외 {len(head_only) - 20}" if len(head_only) > 20 else "")]
    if unparsable or unread:
        body += ["판독 불가 파일: " + " · ".join((unparsable + [f"{u}: base 판독 불가" for u in unread])[:10])]
    return body
```
<!-- 인용 끝 -->
