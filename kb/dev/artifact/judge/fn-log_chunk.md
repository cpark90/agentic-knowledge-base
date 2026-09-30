---
id: https://agentic-knowledge-base.dev/id/chunk/a82c512c-7648-4b7c-b506-56a5a18e9cd5
type: artifact
level: executable
title_ko: 함수 log_chunk (tools/judge.py)
title: function log_chunk in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `log_chunk(rows, q, name, th, source, stamp)` 다. 판정 로그 본문 — 표의 열이 곧 필수 필드다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def log_chunk(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str) -> str:
    """판정 로그 본문 — 표의 열이 곧 필수 필드다 (게이트 id judge-log)."""
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
    ko = f"판정 {stamp}: 질문 {q['label']} · 판정 {len(rows)} · 판정자 {len(judges)} · 사람 확인 큐 {n[kb_lib.JUDGE_QUEUE]}"
    en = f"Judgement {stamp}: question {name}, {len(rows)} judged by {len(judges)} judge(s), {n[kb_lib.JUDGE_QUEUE]} queued"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    measured = "있음" if th["measured"] else kb_lib.EMPTY_REVIEWED
    body = [f"**관측** — {stamp} 에 `judge` 가 질문 `agt:{name}`({q['form']} 형)을 청크 {len(rows)}건(판정자 "
            f"{' · '.join(f'`{j}`' for j in judges)})에 물었다. 응답은 {source} 다. 임계는 자동 적용 {kb_lib.num(th['auto'])} · "
            f"사람 확인 {kb_lib.num(th['human'])} 이고, 구간별 정확도 측정은 `{measured}` · 구간당 표본 하한은 {th['floor']}건이다.", "",
            kb_lib.JUDGE_LOG_TABLE_HEADER, "|" + "---|" * len(kb_lib.JUDGE_LOG_TABLE_HEADER.split("|")[1:-1])]
    for r in rows:
        body.append(f"| `agt:{name}` | `{r['iri']}` | `{r['value']}` | {kb_lib.num(r['confidence'])} | "
                    f"`{r['judge']}` | `{r['fingerprint']}` | {r['at']} | {r['route']} | {r.get('agree', kb_lib.JUDGE_AGREEMENT[2])} |")
    body += ["", "판정 요약 — " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES) +
             f". 일치 {agree_n} · 불일치 {disagree_n}건(단독 응답은 `{kb_lib.JUDGE_AGREEMENT[2]}`) — 일치율 "
             f"{kb_lib.pct(agree_n, agree_n + disagree_n)}. 확신도는 자기 보고라 개별 답의 정확성을 보증하지 않는다. "
             "자동 적용은 일치율 임계가 정확도·판별력 재측정 뒤에 열린다(p8-judge-session-agreement) — "
             f"지금은 전부 사람 확인 큐다. 캘리브레이션 대상 모델은 `{th['model']}` 이다."]
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
