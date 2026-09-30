---
id: https://agentic-knowledge-base.dev/id/chunk/39f2a0d8-63e6-48ef-a57b-5291a656e915
type: artifact
level: executable
title_ko: 함수 report (tools/judge.py)
title: function report in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac
---
**함수** — `report(rows, q, name, th, source, now, decoy_hit, decoy_seen, decoy_total)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report(rows: list[dict], q: dict, name: str, th: dict, source: str, now: datetime,
          decoy_hit: int, decoy_seen: int, decoy_total: int) -> str:
    n = counts(rows)
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
    inputs = sorted({r["path"] for r in rows})
    rep = kb_lib.gendoc_header(
        "judge", "판정자 판정 결과", "tools/judge.py",
        f"등록된 판정 질문 `agt:{name}` 을 세션 판정자의 오프라인 응답으로 청크에 물어 값과 확신도를 받고 일치·미끼 "
        "검출을 요약한다 — 게이트 밖이고 게이트는 판정 로그의 형식만 본다 (8.14절)",
        f"bazel run //tools:judge -- --question {name} --responses <json> <청크 파일…>", inputs,
        f"청크 {len(rows)} · 질문 1({q['form']} 형) · 판정자 {len({r['judge'] for r in rows})}",
        kb_lib.gendoc_view_notice("세션 판정자의 응답과 프로파일의 질문·임계"), input_kind="판정 대상",
        extra=[f"- 응답: {source}",
               f"- 임계: 자동 적용 {kb_lib.num(th['auto'])} · 사람 확인 {kb_lib.num(th['human'])} · "
               f"구간별 정확도 측정 {'있음' if th['measured'] else kb_lib.EMPTY_REVIEWED} (구간당 표본 하한 {th['floor']})",
               "- 처리: " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES),
               f"- 일치: 일치 {agree_n} · 불일치 {disagree_n} · 일치율 {kb_lib.pct(agree_n, agree_n + disagree_n)}(단독 응답 제외)",
               f"- 미끼 검출률: {kb_lib.pct(decoy_hit, decoy_seen)}(응답 있는 미끼 {decoy_seen} / 전체 미끼 {decoy_total})"
               if decoy_total else "- 미끼 검출률: 해당 없음(--decoys 없음)"])
    body = ["## 판정 — 확신도는 자기 보고이고 개별 답을 보증하지 않는다", "",
            "| 대상 | 라벨 | 값 | 확신도 | 판정자 | 처리 | 일치 | 입력 지문 |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        body.append(f"| `{r['path']}` | {r['label'] or kb_lib.NONE_MARK} | `{r['value']}` | "
                    f"{kb_lib.num(r['confidence'])} | `{r['judge']}` | {r['route']} | {r.get('agree', kb_lib.JUDGE_AGREEMENT[2])} | "
                    f"`{r['fingerprint'][:12]}…` |")
    if not rows:
        body.append("| " + " | ".join([kb_lib.NONE_MARK] * 8) + " |")
    body += ["", "## 질문", "", f"- `agt:{name}` ({q['form']} 형) — {q['text']}"]
    if q["scale"]:
        body += ["- 척도의 상황 문장: " + " · ".join(f"`{s}`" for s in q["scale"])]
    if q["options"]:
        body += [f"- 선택 집합 {len(q['options'])}개(상한 {kb_lib.JUDGE_CHOICE_MAX}): " + " · ".join(f"`{o}`" for o in q["options"])]
    body += ["", "## 미끼 검출 (라벨 대표성 실험, `--decoys`)", "",
             f"- 미끼 {decoy_total}건 중 응답 대조 {decoy_seen}건 · 검출 {decoy_hit}건 · 검출률 {kb_lib.pct(decoy_hit, decoy_seen)}"
             if decoy_total else "- 없음(`--decoys` 를 주지 않았다)", "",
             f"판정자는 설명을 만들지 못하므로 결과 주석의 `본문:` 은 `{kb_lib.EMPTY_NOT_APPLICABLE}` 이고 "
             "사람 또는 System 2 에이전트가 채운다."]
    return kb_lib.gendoc_assemble(rep, body, inputs, input_kind="판정 대상")
```
<!-- 인용 끝 -->
