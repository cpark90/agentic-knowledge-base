---
id: https://agentic-knowledge-base.dev/id/chunk/2b69cd72-19b5-4d4d-adc7-b20e75c687ce
type: artifact
level: executable
title_ko: 함수 log_frontmatter (tools/judge.py)
title: function log_frontmatter in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/25d46f37-11ee-4e27-92e7-9584f2dcb1a0]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `log_frontmatter(rows, q, name, th, stamp)` 다. 판정 로그의 frontmatter — 라벨이 묶음의 요약이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def log_frontmatter(rows: list[dict], q: dict, name: str, th: dict, stamp: str) -> list[str]:
    """판정 로그의 frontmatter — 라벨이 묶음의 요약이다. uuid 는 파일마다 새로 난다."""
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    ko = f"판정 {stamp}: 질문 {q['label']} · 판정 {len(rows)} · 판정자 {len(judges)} · 사람 확인 큐 {n[kb_lib.JUDGE_QUEUE]}"
    en = f"Judgement {stamp}: question {name}, {len(rows)} judged by {len(judges)} judge(s), {n[kb_lib.JUDGE_QUEUE]} queued"
    return ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
```
<!-- 인용 끝 -->
