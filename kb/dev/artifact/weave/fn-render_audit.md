---
id: https://agentic-knowledge-base.dev/id/chunk/4ed2982d-49b2-4313-856e-6b86a53fb3b0
type: artifact
level: executable
title_ko: 함수 render_audit (tools/weave.py)
title: function render_audit in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `render_audit(m, bodies, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_audit(m: Model, bodies: dict, inputs: list[str]) -> str:
    g = m.g
    live = {c for c in m.chunks if m.live(c)}
    vv = {c for c in live if kb_lib.kb_of(m.location[c]) == kb_lib.KB_VV}
    dev = live - vv
    by_gen = lambda c: str(next(g.objects(c, AGT.generatedBy), ""))  # noqa: E731
    obs_all = [c for c in m.chunks if m.plane[c] == "memory"]
    runs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.VV_RUN_DIR + "/") and by_gen(c) == kb_lib.RUN_GENERATOR),
                  key=lambda c: (m.at(c), m.location[c]))
    asm_obs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.DEV_MEMORY_DIR + "/") and by_gen(c) == kb_lib.ASSUME_CHECK_GENERATOR),
                     key=lambda c: (m.at(c), m.location[c]))
    latest_run, latest_asm = (runs[-1] if runs else None), (asm_obs[-1] if asm_obs else None)
    run_body = bodies.get(str(latest_run), "") if latest_run is not None else ""
    asm_body = bodies.get(str(latest_asm), "") if latest_asm is not None else ""

    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — metrics 와 같은 정의)

    # 1. 리비전 — 그래프는 리비전을 담지 않는다. 실행 기록이 초기 상태(p8-reproducibility)로 담는다
    rev_m = RUN_REVISION.search(run_body)
    rev_line = (f"실행 기록의 리비전 `{rev_m.group(1)}`" + (f" ({rev_m.group(2)})" if rev_m.group(2) else "") + f" — `{Path(m.location[latest_run]).name}`"
                if rev_m else "실행 기록이 없어 리비전을 알 수 없다 — 그래프는 리비전을 담지 않는다")
    h = head("audit", "감사 보고서", "그래프 union 과 관측 청크 본문(`kb/vv/run/` 실행 기록 · `kb/dev/memory/` 가정 판정)만으로 — 검증 현황 · 최근 실행 · "
             "판정 주석 · 가정 · 추적 매트릭스(`kb_lib.TIM_CELLS`) · 검증 표시 · 링크 근거 · 자족성", g, inputs,
             [f"- 리비전: {rev_line}",
              f"- 입력의 종류: 그래프 union(head · 참조 · 시드 · 카탈로그 · 복합체 · ODD · 온톨로지) · 관측 본문 — 실행 기록 {len(runs)}건 · 가정 판정 {len(asm_obs)}건. "
              f"체계 밖 정보 0 (요구 `audit-self-sufficiency`)",
              f"- 살아 있는 청크 {len(live)} — 개발 KB {len(dev)} · V&V KB {len(vv)}"])
    body: list[str] = []

    # 2. 검증 현황
    dev_reqs = {c for c in dev if m.plane[c] == "requirement"}
    goals = {c for c in vv if m.plane[c] == "requirement"}
    covered = {t for s, t in g.subject_objects(AGT.derivesFrom) if s in goals and t in dev_reqs}
    criteria_of = defaultdict(set)
    cases_of = defaultdict(set)
    verifiers_of = defaultdict(set)
    for s, t in g.subject_objects(AGT.refines):
        if s in vv and t in vv:
            if m.plane[s] == "contract" and t in goals:
                criteria_of[t].add(s)
            elif m.plane[s] == "schema" and m.plane[t] == "contract":
                cases_of[t].add(s)
            elif m.plane[s] == "artifact" and m.plane[t] == "schema":
                verifiers_of[t].add(s)
    chains = [gl for gl in goals if any(cases_of[cr] for cr in criteria_of[gl])]
    verifies = [(s, t) for s, t in g.subject_objects(AGT.verifies) if s in vv]
    no_criteria = [s for s, _ in verifies if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    units = {m.decision_unit(c) for c in dev if m.plane[c] == "decision"}
    verified_units = {m.decision_unit(t) for _, t in verifies if t in m.chunks and m.plane.get(t) == "decision"}
    body += ["## 검증 현황 — 요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria)", "",
          f"- 검증 대응물이 있는 요구(검증 목표가 `agt:derivesFrom` 으로 가리킴): **{pct(len(covered), len(dev_reqs))}** (목표 100.0%)",
          f"- `agt:verifies` 대상이 된 결정 단위: **{pct(len(verified_units), len(units))}** · verifies 링크 {len(verifies)}",
          f"- 사슬: 검증 목표 {len(goals)} · 합격 기준이 달린 목표 {sum(1 for gl in goals if criteria_of[gl])} · 케이스까지 이어진 목표 {len(chains)} · "
          f"검증기 {sum(len(v) for v in verifiers_of.values())} (합격 기준 {sum(len(v) for v in criteria_of.values())} · 케이스 {sum(len(v) for v in cases_of.values())})",
          f"- 기준 없는 `verifies`: **{len(no_criteria)}** (목표 0 — verify 질의 `verifies-without-criteria` 와 같은 정의)", ""]
    uncovered = sorted(dev_reqs - covered, key=lambda c: m.location[c])
    if uncovered:
        body += [f"검증 대응물 없는 요구 {len(uncovered)}건:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)}" for c in uncovered] + [""]

    # 2.5 위험에서 파생된 목표 — 검증 목표가 defect 요인(현상)을 가리키는가 (위험 분석 G1·G5, 노트 8.21·8.22절)
    # 파생의 표지는 둘이다. frontmatter `exposes`(agt:exposesFactor)는 저자가 선언한 것이고 본문의 현상 IRI 인용
    # (agt:usesConcept, extract_refs)은 추출된 것이다. 둘 다 있으면 선언을 적는다 — 선언이 더 검사 가능한 근거다.
    factor_classes = set(g.transitive_subjects(RDFS.subClassOf, AGT.DefectFactor))
    factors = {i for cl in factor_classes for i in g.subjects(RDF.type, cl)}
    exposed: dict = defaultdict(dict)
    for pred, mark in ((AGT.exposesFactor, RISK_MARK_DECLARED), (AGT.usesConcept, RISK_MARK_EXTRACTED)):
        for s, o in g.subject_objects(pred):
            if s in goals and o in factors:
                exposed[s].setdefault(o, mark)
    named = {f for fs in exposed.values() for f in fs}
    body += [f"## 위험에서 파생된 목표 — 검증 목표가 노출하는 결함 요인 (표지 둘 — {RISK_MARK_DECLARED}: `exposes` · {RISK_MARK_EXTRACTED}: 본문의 현상 IRI, 8.21절 G1·G5)", "",
             f"- 위험에서 파생된 검증 목표: **{pct(len(exposed), len(goals))}** — 나머지는 게이트·음성 시험을 사슬로 묶은 것이다",
             f"- 어느 목표에도 가리켜지지 않은 현상: **{pct(len(factors) - len(named), len(factors))}**", ""]
    if not exposed:
        body += [f"위험에서 파생된 검증 목표 {kb_lib.NONE_MARK} — 현상을 가리키는 목표가 없다. `exposes:` 또는 본문의 현상 IRI 인용이 표지다.", ""]
    else:
        body += ["| 검증 목표 | 노출하는 현상 | 표기 | 표지 |", "|---|---|---|---|"]
        for c in sorted(exposed, key=lambda c: m.location[c]):
            for f in sorted(exposed[c], key=lambda f: str(f)):
                note = str(next(g.objects(f, SKOS_NOTATION), "")) or kb_lib.NONE_MARK
                body += [f"| `{Path(m.location[c]).stem}` {m.ko(c)} | {m.ko(f)} (`{kb_lib.compact_iri(str(f))}`) | {note} | {exposed[c][f]} |"]
        body += [""]

    # 3. 최근 실행 — 실행 기록을 그대로 요약한다
    body += ["## 최근 실행 — `kb/vv/run/` 의 최신 실행 기록 (agt:Run, append-only)", ""]
    if latest_run is None:
        body += ["실행 기록 없음 — `bazel run //tools:vv_run -- --record`", ""]
    else:
        rows = observation_table(run_body, kb_lib.RUN_CASE_TABLE_HEADER)
        verdicts = Counter(r[2] for r in rows if len(r) >= 3)
        body += [f"- {m.ko(latest_run)} (`{m.location[latest_run]}`, 생성 {m.at(latest_run)}, {by_gen(latest_run)}) — 실행 기록 전체 {len(runs)}건",
              "- 케이스 " + " · ".join(f"{v} **{verdicts.get(v, 0)}**" for v in kb_lib.RUN_VERDICTS) + " — SKIP 은 PASS 가 아니다", ""]
        first = run_body.split("\n", 1)[0].strip()
        if first:
            body += [f"> {first}", ""]
        if rows:
            body += [kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"] + ["| " + " | ".join(r) + " |" for r in rows] + [""]
        else:
            body += [f"- 본문에 케이스 표(헤더 `{kb_lib.RUN_CASE_TABLE_HEADER}`)가 없다", ""]

    # 4. 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form: issue (blocking) + 해소 열림 만 게이트를 막는다)
    label_of = lambda c: str(next(g.objects(c, AGT.commentLabel), ""))        # noqa: E731
    deco_of = lambda c: str(next(g.objects(c, AGT.commentDecoration), ""))    # noqa: E731
    state_of = lambda c: str(next(g.objects(c, AGT.resolutionState), ""))     # noqa: E731
    comments = sorted((c for c in live if m.plane[c] == "annotation"), key=lambda c: m.location[c])
    open_ = [c for c in comments if state_of(c) == kb_lib.COMMENT_OPEN]
    blocking = [c for c in open_ if (label_of(c), deco_of(c)) == kb_lib.COMMENT_BLOCKING]
    body += ["## 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form)", ""]
    if not comments:
        body += [f"살아 있는 주석 {kb_lib.NONE_MARK} — 판정 주석(`{kb_lib.KB_VV}/verdict/`)이 비어 있다. 게이트 "
                 f"`{kb_lib.BLOCKING_COMMENT_GATE}` 는 서 있고 막을 주석이 아직 없다.", ""]
    else:
        labels = Counter(label_of(c) or kb_lib.NONE_MARK for c in comments)
        states = Counter(state_of(c) or kb_lib.NONE_MARK for c in comments)
        body += [f"- 살아 있는 주석 **{len(comments)}** · 해소되지 않은 것(`해소: {kb_lib.COMMENT_OPEN}`) **{pct(len(open_), len(comments))}** · "
                 f"그중 게이트를 막는 `{kb_lib.COMMENT_BLOCKING[0]} ({kb_lib.COMMENT_BLOCKING[1]})` **{len(blocking)}** "
                 f"(목표 0 — 게이트 `{kb_lib.BLOCKING_COMMENT_GATE}`)", "",
                 "| 라벨 | 주석 수 | 그중 해소 열림 |", "|---|---|---|"]
        body += [f"| `{k}` | {v} | {sum(1 for c in open_ if (label_of(c) or kb_lib.NONE_MARK) == k)} |" for k, v in labels.most_common()]
        body += ["", "| 해소 상태 | 주석 수 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in states.most_common()] + [""]
        if blocking:
            body += ["게이트를 막는 주석:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)} → "
                     + (" · ".join(m.ko(t) for t in g.objects(c, AGT.targets)) or kb_lib.NONE_MARK) for c in blocking] + [""]

    # 5. 가정 — 최신 assume_check 관측
    body += ["## 가정 — `kb/dev/memory/` 의 최신 가정 판정 관측 (assume_check)", ""]
    if latest_asm is None:
        body += ["가정 판정 관측 없음 — `bazel run //tools:assume_check -- --record`", ""]
    else:
        rows = observation_table(asm_body, kb_lib.ASSUME_CHECK_TABLE_HEADER)
        states = Counter(r[3] for r in rows if len(r) >= 4)
        body += [f"- {m.ko(latest_asm)} (`{m.location[latest_asm]}`, 생성 {m.at(latest_asm)}) — 가정 판정 관측 전체 {len(asm_obs)}건",
              "- 가정 " + (" · ".join(f"{k} **{v}**" for k, v in sorted(states.items())) or kb_lib.NONE_MARK + " — 본문에 가정 표가 없다"), ""]
        if rows:
            body += ["| 가정 | 판정 유형 | 등급 | 상태 |", "|---|---|---|---|"] + ["| " + " | ".join(r[:4]) + " |" for r in rows] + [""]

    # 6. 추적 매트릭스 — metrics 와 같은 정의 (kb_lib.TIM_CELLS · link_cells)
    seen = kb_lib.link_cells(g)
    filled = [c for c in kb_lib.TIM_CELLS if c in seen]
    outside = sorted(seen - set(kb_lib.TIM_CELLS))
    body += [f"## 추적 매트릭스 — plane × plane, TIM 허용 {len(kb_lib.TIM_CELLS)}칸 중 채움 **{len(filled)}** (metrics 3단계 대리와 같은 정의)", "",
          "| 링크 | 출발 plane | 도착 plane | 채움 |", "|---|---|---|---|"]
    body += [f"| `{k}` | `{a}` | `{b}` | {'채움' if (k, a, b) in seen else '빈 칸'} |" for k, a, b in kb_lib.TIM_CELLS]
    body += ["", f"- 허용표 밖에서 관측된 칸: {len(outside)}" + (" — " + ", ".join(f"`{k}`:{a}→{b}" for k, a, b in outside) if outside else ""), ""]

    # 7. 검증 표시 — verified 주체 종류와 검증 뒤 수정 (trust shape)
    kinds = Counter()
    none_n, modified = 0, []
    for c in live:
        vbs = [str(v) for v in g.objects(c, AGT.verifiedBy)]
        if not vbs:
            none_n += 1
        for kind in {("human:" if v.startswith("human:") else "process:" if v.startswith("process:") else v.split("/")[0] + "/" if "/" in v else "기타") for v in vbs}:
            kinds[kind] += 1
        gen_at = as_dt(m.at(c))
        for v in g.objects(c, AGT.verifiedAt):
            va = as_dt(str(v))
            if gen_at and va and gen_at > va:
                modified.append(c)
                break
    body += ["## 검증 표시 — `verified` 주체 종류별 살아 있는 청크 수 (한 청크가 여러 종류를 가질 수 있다)", "",
          "| 주체 종류 | 청크 수 |", "|---|---|"] + [f"| `{k}` | {v} |" for k, v in sorted(kinds.items())] + [f"| 없음 (미검증) | {none_n} |", "",
          f"- 검증 뒤 수정(`prov:generatedAtTime` > `agt:verifiedAt`): **{len(modified)}** (목표 0 — `agt:TrustShape` 가 게이트에서 강제)", ""]

    # 8. 링크 근거 — 증거 종류 분포와 복원 비율 (metrics 와 같은 구축·복원 정의: kb_lib.link_origins — 증거 종류 기준)
    links = list(g.subjects(RDF.type, AGT.Link))
    ev_kinds = Counter()
    for l in links:
        for ev in g.objects(l, AGT.hasEvidence):
            ev_kinds[str(next(g.objects(ev, AGT.evidenceKind), "")).split("/")[-1] or "없음"] += 1
    origins = kb_lib.link_origins(g)
    built, restored, no_ev = origins["built"], origins["restored"], origins["no_evidence"]
    states = Counter(str(next(g.objects(l, AGT.linkState), "")) or "없음" for l in links)
    restored_rows = [f"  - {m.ko(next(g.objects(l, AGT.linkFrom), l))} —`{str(next(g.objects(l, AGT.linkKind), '')).split('/')[-1]}`→ "
                     f"{m.ko(next(g.objects(l, AGT.linkTo), l))}" for l in origins["restored_links"]]
    body += ["## 링크 근거 — 링크 개체의 증거 종류와 복원 비율", "",
          f"- 링크 개체 `agt:Link` **{len(links)}** · 증거 없는 링크 {no_ev} (목표 0) · 상태 " + (" · ".join(f"`{k}` {v}" for k, v in sorted(states.items())) or "없음"),
          "- 증거 종류: " + (" · ".join(f"`{k}` {v}" for k, v in ev_kinds.most_common()) or "없음"),
          f"- 확정 {origins['confirmed']} = 구축 {built}(구축 기록 증거뿐) + 복원 {restored}(구축 기록 아닌 증거 `proposal` 을 가진 링크 개체 — frontmatter `restored:` 표시, "
          f"p10-restored-link-marking) → 복원 비율 **{pct(restored, built + restored)}** (목표 20% 미만; 후보는 `//kg:link_candidates`)",
          f"- 후보 {origins['candidates']} (`agt:CandidateLink` — 본문 추출, 증거는 구축 기록; p10-extracted-references-are-candidates): "
          + (" · ".join(f"`{k}` {v}" for k, v in sorted(origins["candidate_kinds"].items())) or "없음")
          + " · 본문 식별자 추출 직접 트리플 " + " · ".join(f"`{k}` {v}" for k, v in origins["extracted"].items())] + restored_rows + [""]

    # 9. 자족성 선언
    body += ["## 자족성 선언", "",
          "이 보고서의 모든 수치는 위 입력(그래프 union · 실행 기록 · 가정 판정 관측)에서 나왔다. 손으로 적은 수치는 없다. "
          "이 보고서를 다시 만드는 명령은 `bazel build //kg:audit` 이고 입력이 같으면 수치가 같다.", ""]
    return kb_lib.gendoc_assemble(h, body, inputs)
```
<!-- 인용 끝 -->
