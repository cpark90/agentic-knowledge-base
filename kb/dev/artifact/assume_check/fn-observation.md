---
id: https://agentic-knowledge-base.dev/id/chunk/ae67e102-2e22-4234-8638-b2db8fa603b4
type: artifact
level: executable
title_ko: 함수 observation (tools/assume_check.py)
title: function observation in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `observation(now, cond_rows, asms, impact, live_n, broke, broke_show, check, sat)` 다. 관측 청크 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def observation(now: datetime, cond_rows: list[dict], asms: list[dict], impact: dict, live_n: int, broke: list[str],
                broke_show: list[str], check: dict | None, sat: dict) -> str:
    """관측 청크 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory). `memory` plane 상한(2,856토큰) 안이다."""
    stamp = kb_lib.utc_stamp(now)  # G3 표기 하나 — frontmatter 와 본문이 같은 꼴을 쓴다 (유저 승인 2026-09-23)
    n_inv = sum(1 for a in asms if a["status"] == "invalidated")
    n_unv = sum(1 for a in asms if a["status"] == "unverified")
    total_direct = len(set().union(*(impact[a["iri"]][0] for a in asms)) if asms else set())
    ko = f"가정 판정 {stamp}: 가정 {len(asms)} · 무효 {n_inv}"
    en = f"Assumption check {stamp}: {len(asms)} assumptions, {n_inv} invalidated"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{DEFAULT_ASSUMPTION}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    act = (f"`--break {' '.join(broke_show)}` 로 조건 {len(broke)}건을 이탈로 가정한 인위 파괴 실험이다" if broke
           else "`--break` 없는 실측이다")
    body = [f"**관측** — {stamp} 에 `assume_check` 가 ODD 조건 {len(cond_rows)}건을 판정하고 "
            f"가정 {len(asms)}건의 상태를 계산했다. {act}.", "",
            "| 조건 | 등급 | 판정 |", "|---|---|---|"]
    body += [f"| `{local(r['iri'])}` | {r['grade']} | {r['state']}{' (--break)' if r['name'] in broke else ''} |" for r in cond_rows]
    body += ["", "| 가정 | 판정 유형 | 등급 | 상태 | 직접 영향 | suspect 후보(전이) |", "|---|---|---|---|---|---|"]
    body += [f"| `{local(a['iri'])}` | {a['kind']} | {a['grade']} | {a['status']} | {len(impact[a['iri']][0])} | {len(impact[a['iri']][2])} |"
             for a in asms]
    body += ["", f"situation 요약 — 살아 있는 청크 {live_n}, 무효 가정 {n_inv}, 판정 불가 가정 {n_unv}, 직접 영향 집합 {total_direct}.",
             f"링크 요약 — 확정 링크 {sat['confirmed']}, `when` 을 가진 것 {sat['with_when']}, suspect 포화율 "
             f"{kb_lib.pct(sat['suspect'], sat['confirmed'])} (`when` 거짓 {sat['by_when']}, 트리거 {sat['by_trigger']})."]
    if check:
        body.append(f"검증 실험 — 계산된 직접 영향 집합 {check['computed']} 대 실제 의존 집합(frontmatter 스캔) {check['actual']}: "
                    f"정밀도 {check['precision']}, 재현율 {check['recall']}, {'일치' if check['equal'] else '불일치'}.")
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
