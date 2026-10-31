---
id: https://agentic-knowledge-base.dev/id/chunk/8d6f25bd-f8f1-47b2-a82d-4f2b6d19cd91
type: artifact
level: executable
title_ko: 함수 write_pair_sheet (tools/label_sample.py)
title: function write_pair_sheet in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `write_pair_sheet(sheet_dir, out, entries, qs, defs, batch)` 다. 묶음 pairs-NN.md 와 key.json 을 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_pair_sheet(sheet_dir: Path, out: Path, entries: list[dict], qs: dict, defs: dict, batch: int) -> list[Path]:
    """묶음 pairs-NN.md 와 key.json 을 쓴다 — 판정지에는 경로·근거·미끼 여부가 없다."""
    sheet_dir.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    used_q = sorted({e["question"] for e in entries})
    intro = ["쌍 판정 — 쌍마다 질문에 `yes` 또는 `no` 로 답하고 '예'의 확률(0~1)을 확신도로 적는다. 응답은 JSON "
             "`{\"judge\": <판정자 식별자>, \"responses\": [{\"question\": <질문 id>, \"fingerprint\": <쌍의 해시값>, "
             "\"value\": \"yes\"|\"no\", \"confidence\": <0~1>}]}` 로 돌려준다. 다른 쌍의 답을 참고하지 않는다.", ""]
    for name in used_q:
        intro.append(f"- `{name}` — {qs[name]['label']}: {qs[name]['text']}")
    written = []
    for k in range(0, len(entries), batch):
        lines = [f"# 쌍 판정지 {k // batch + 1:02d}", ""] + intro + [""]
        for e in entries[k:k + batch]:
            lines += [f"## 쌍 {e['n']}", "",
                      f"- 질문: {qs[e['question']]['label']} (`{e['question']}`)",
                      f"- 링크 종류: `{e['kind']}` — {defs.get(e['kind'], kb_lib.EMPTY_UNDECIDED)}",
                      f"- 해시값: {e['fingerprint']}", ""]
            for role, it in (("앵커", e["anchor"]), ("대상", e["target"])):
                lines += [f"### {role} — {it['title_ko']} | {it['title']}", "", it["body"], ""]
        path = sheet_dir / f"pairs-{k // batch + 1:02d}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
    (out / "key.json").write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    return written
```
<!-- 인용 끝 -->
