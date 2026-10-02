---
id: https://agentic-knowledge-base.dev/id/chunk/8d622313-8c2c-4f87-9279-fce0b31cb0ff
type: artifact
level: executable
title_ko: 함수 log_body (tools/judge.py)
title: function log_body in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/25d46f37-11ee-4e27-92e7-9584f2dcb1a0, https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `log_body(rows, q, name, th, source, stamp)` 다. 판정 로그의 **본문 줄들** — 표의 열이 곧 필수 필드다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def log_body(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str) -> list[str]:
    """판정 로그의 **본문 줄들** — 표의 열이 곧 필수 필드다 (게이트 id judge-log).

    frontmatter 를 빼고 내는 까닭은 크기 상한의 대상이 본문이기 때문이다 — `split_rows` 가 이 결과를 재서
    묶음을 가른다 (p1-chunk-unit-is-tokens).
    """
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
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
    return body
```
<!-- 인용 끝 -->
