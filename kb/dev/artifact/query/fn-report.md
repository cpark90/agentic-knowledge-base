---
id: https://agentic-knowledge-base.dev/id/chunk/0721b4a7-9459-4293-abe0-4cb723016280
type: artifact
level: executable
title_ko: 함수 report (tools/query.py)
title: function report in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/577e30ee-635f-4a97-a192-b3780a178be7, https://agentic-knowledge-base.dev/id/chunk/5b1d87c6-7817-4c3b-8792-288ae36fedf2, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/f9b6b36a-3732-4fca-b346-5a371afb405e]
part_of: https://agentic-knowledge-base.dev/id/composite/4358cd56-6be2-4ce1-9f2f-9fb0ed47b5d3
---
**함수** — `report(g, results, summary_lines, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report(g: Graph, results: list[tuple[CqQuery, list[str], list[tuple]]], summary_lines: list[str], inputs: list[str]) -> str:
    head = kb_lib.gendoc_header(
        "cq", "역량 질문 뷰", "tools/query.py",
        f"등재된 역량 질문 {len(results)}건(`docs/competency-questions.md`)을 그래프 union 에 그대로 물어 — 질문 원문은 각 "
        f"`tools/cq-queries/CQ-NN.rq` 의 머리 주석 첫 줄, 답의 형태는 둘째 줄이다. 행 수는 답이지 판정이 아니다",
        "bazel build //kg:cq", inputs, f"트리플 {len(g)} · 질의 {len(results)}",
        kb_lib.gendoc_view_notice("질의 파일 `tools/cq-queries/*.rq` 와 청크"),
        extra=[f"- CQ 별로 상위 {REPORT_TOP}행을 라벨로 보인다 — 전부는 `bazel run //tools:query -- <CQ> --labels --limit 0`"])
    o = ["## 요약", ""] + summary_lines + [""]
    for q, cols, rows in results:
        o += [f"## {q.id} — {q.question}", "", f"- {FORM_PREFIX}{q.form}" if q.form else f"- {FORM_PREFIX}{kb_lib.NONE_MARK}",
              f"- 행 수 **{len(rows)}**", ""]
        if cols and rows:
            o += table(cols, [[cell(g, t, True, REPORT_CELL) for t in r] for r in rows[:REPORT_TOP]])
            o.append("")  # G10 — 표 뒤에 빈 줄 (MD058)
            if len(rows) > REPORT_TOP:
                o += [f"… 외 {len(rows) - REPORT_TOP}행", ""]
        else:
            o += [kb_lib.NONE_MARK, ""]
    return kb_lib.gendoc_assemble(head, o, inputs)
```
<!-- 인용 끝 -->
