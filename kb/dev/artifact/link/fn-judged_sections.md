---
id: https://agentic-knowledge-base.dev/id/chunk/d953c65e-1082-4bf2-be6e-7d71429b9ef8
type: artifact
level: executable
title_ko: 함수 judged_sections (tools/link.py)
title: function judged_sections in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/8c071cee-5922-4176-a0d9-848167ee9316, https://agentic-knowledge-base.dev/id/chunk/ec5e9dfa-5521-4e0c-8ae8-6be045e70e81, https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `judged_sections(u, candidates)` 다. 동시 편집이 첫 근거인 후보의 판정 넷 → (요약 표의 세 행, 네 절의 줄들) (task 0262 Q145-a, task 0303 Q165-c).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judged_sections(u: Units, candidates: list) -> tuple[list[str], list[str]]:
    """동시 편집이 첫 근거인 후보의 판정 넷 → (요약 표의 세 행, 네 절의 줄들) (task 0262 Q145-a, task 0303 Q165-c).

    큐(후보 표)는 첫 근거가 동시 편집이 아닌 후보, 일치(+,+) 전부, 일치(−,−) 의 표본이고 판정자 값 열에 극성과 판정을 싣는다. 표본은
    일치(−,−) 쌍마다 sha256(시드 ∣ 앵커 IRI ∣ 대상 IRI ∣ 링크 종류)이 가장 작은 kb_lib.JUDGED_NO_SAMPLE_SIZE 쌍이고(모자라면 전부) 판정자 값에
    kb_lib.JUDGED_NO_SAMPLE_MARK 를 덧붙인다. 표본 밖 일치(−,−)·불일치·판정 없음은 따로 절을 세운다. 번호는 네 절을 통틀어 후보 순서다."""
    for c in candidates:
        pols = next((e[2].split() for e in c["evs"] if e[1] == "judgement"), [])
        c["judged"] = kb_lib.judged_class(pols) if c["evs"][0][1] == "coEditHistory" else None
        c["judge_cell"] = (f"{' '.join(kb_lib.POLARITY_MARK.get(p, p) for p in pols)} ({c['judged']})" if c["judged"] and pols
                           else kb_lib.EMPTY_NOT_APPLICABLE)
    agree_no = [c for c in candidates if c["judged"] == kb_lib.JUDGED_AGREE_NO]
    rank = {id(c): hashlib.sha256("\t".join((kb_lib.JUDGED_NO_SAMPLE_SEED, str(c["anchor"]), str(c["target"]), str(c["kind"])))
                                  .encode("utf-8")).hexdigest() for c in agree_no}
    sample = {id(c) for c in sorted(agree_no, key=lambda c: rank[id(c)])[:kb_lib.JUDGED_NO_SAMPLE_SIZE]}
    for c in agree_no:
        if id(c) in sample:
            c["judge_cell"] += f" · {kb_lib.JUDGED_NO_SAMPLE_MARK}"
    queue = [c for c in candidates if c["judged"] in (None, kb_lib.JUDGED_AGREE_YES) or id(c) in sample]
    split = {k: [c for c in candidates if c["judged"] == k] for k in (kb_lib.JUDGED_DISAGREE, kb_lib.JUDGED_NONE)}
    outside = [c for c in agree_no if id(c) not in sample]
    judged_n = Counter(c["judged"] for c in candidates if c["judged"])
    four = (kb_lib.JUDGED_AGREE_YES, kb_lib.JUDGED_AGREE_NO, kb_lib.JUDGED_DISAGREE, kb_lib.JUDGED_NONE)
    summary = ["| 동시 편집 첫 근거 후보의 판정 | " + " · ".join(f"{k} {judged_n[k]}" for k in four) + " |",
               f"| 사람 확인 큐 크기 | {len(queue)} — 첫 근거가 동시 편집이 아닌 후보 {sum(1 for c in queue if c['judged'] is None)} · "
               f"{kb_lib.JUDGED_AGREE_YES} {judged_n[kb_lib.JUDGED_AGREE_YES]} · {kb_lib.JUDGED_NO_SAMPLE_MARK} {len(sample)} |",
               f"| {kb_lib.JUDGED_AGREE_NO} 표본 | {len(sample)} / {len(agree_no)} — 시드 `{kb_lib.JUDGED_NO_SAMPLE_SEED}` · 상한 "
               f"{kb_lib.JUDGED_NO_SAMPLE_SIZE} · 큐 밖 {len(outside)} |"]
    header = "| " + " | ".join(kb_lib.LINK_CANDIDATE_COLUMNS) + " |"
    rule = "|" + "---|" * len(kb_lib.LINK_CANDIDATE_COLUMNS)
    numbered = {id(c): i for i, c in enumerate(candidates, 1)}

    def table(rows: list, empty: str) -> list:
        out = [header, rule]
        for c in rows:
            out.append(f"| {numbered[id(c)]} | {cell(u.ko(c['anchor']))} | `{u.loc.get(c['anchor'], '')}` | `{c['kind']}` | {cell(u.ko(c['target']))} | "
                       f"`{kb_lib.compact_iri(str(c['target']))}` | " + " · ".join(e[1] for e in c["evs"]) + " | "
                       + " · ".join(cell(" ".join(kb_lib.POLARITY_MARK.get(p, p) for p in e[2].split()) if e[1] == "judgement" else e[2])
                                    for e in c["evs"]) + f" | {c['judge_cell']} | {kb_lib.NONE_MARK} |")
        if not rows:
            out.append("| " + " | ".join([kb_lib.NONE_MARK] * 2 + [empty] + [kb_lib.NONE_MARK] * (len(kb_lib.LINK_CANDIDATE_COLUMNS) - 3)) + " |")
        return out

    o = ["## 후보 — 사람 확인 큐", "",
         f"첫 근거가 동시 편집이 아닌 후보, 동시 편집이 첫 근거이고 판정자 둘이 {kb_lib.JUDGED_AGREE_YES} 인 후보 전부, {kb_lib.JUDGED_AGREE_NO} 인 후보의 "
         f"표본이다. 판정자 값은 극성과 판정이고 표본에는 `{kb_lib.JUDGED_NO_SAMPLE_MARK}` 가 붙는다. 표본에서 성립하는 링크가 나오면 판정자가 놓친 "
         "비율의 재료다.", ""]
    o += table(queue, f"후보 {kb_lib.NONE_MARK}")
    o += ["", f"## {kb_lib.JUDGED_AGREE_NO} — 큐 밖, 판정 증거와 함께 후보로 남음", "",
          "동시 편집이 첫 근거이고 판정자 둘이 함께 반박한 후보 가운데 표본에 들지 않은 것이다. 사람 확인 큐에 오르지 않고 후보 상태는 그대로다.", ""]
    o += table(outside, f"큐 밖 {kb_lib.NONE_MARK}")
    o += ["", "## 판정 불일치", "", "동시 편집이 첫 근거이고 판정자 둘의 극성이 갈린 후보다. 사람 확인 큐에 오르지 않는다.", ""]
    o += table(split[kb_lib.JUDGED_DISAGREE], f"불일치 {kb_lib.NONE_MARK}")
    o += ["", "## 판정 없음", "",
          "동시 편집이 첫 근거이고 판정자 둘의 판정이 아직 없는 후보다(단독 판정과 낡은 판정을 포함한다). 쌍 판정지 `label_sample.py --pair-sheet` 의 입력이다.", ""]
    o += table(split[kb_lib.JUDGED_NONE], f"판정 대상 {kb_lib.NONE_MARK}")
    return summary, o
```
<!-- 인용 끝 -->
