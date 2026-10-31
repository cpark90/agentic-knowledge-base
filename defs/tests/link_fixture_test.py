#!/usr/bin/env python3
"""복원 후보 생성기(`tools/link.py`)의 구조 거름 시험 — 양성 하나와 음성 셋 (orchestrator 판정 2026-10-04, 복원 후보 114건).

고정물은 시험이 TEST_TMPDIR 에 쓰는 그래프 파일 하나다. 청크 여덟이고 증거는 본문 인용(`agt:cites`)뿐이다.
  양성  V&V 검증 목표(kb/vv requirement, functional) → 개발 요구의 인용이 `derivesFrom` 후보로 남는다 — 사다리의 functional
        행이 허용하는 정식 링크다 (p8-scenario-ladder-rungs)
  음성  (가) 개발 파일 청크 → V&V 시나리오 자극의 인용 — `satisfies`·`refines` 칸은 있으나 KB 를 가로지른다 (p6-executable-splits-by-kb)
        (나) 함수 청크(파일 복합체의 부분) → 개발 결정의 인용 — 끝점이 코드 부분이다 (p7-code-links-on-file-composite)
        (다) 케이스 → 자기 것이 아닌 시나리오 자극의 인용 — 케이스의 `derivesFrom` 은 생성기가 쓴다 (tools/case_gen.py)
  셋 다 후보 표에 없고 요약의 탈락 분포에 각자의 사유로 1건씩 센다.

쌍 판정 (task 0262, Q-0061 Q145-a) — 고정물은 TEST_TMPDIR 의 작은 트리다.
  뷰    동시 편집 관측의 쌍 넷에 판정 증거가 (+,+) · (−,−) · (+,−) · 없음 으로 붙으면 판정 넷이 1건씩이고, 사람 확인 큐는 일치 둘과
        첫 근거가 동시 편집이 아닌 후보 하나다(일치(−,−) 은 표본 상한 미만이라 전부 오르고 표본 표기를 단다). 불일치와 판정 없음은 각자의 절에
        있고 쌍 판정지(`label_sample.pair_judge_targets`)는 뷰를 되읽어 판정 없음 하나만 고른다
  표본  (task 0303, Q165-c) 일치(−,−) 25 이면 sha256(시드 ∣ 앵커 ∣ 대상 ∣ 종류) 순위로 20 쌍만 큐에 오르고, 입력 순서를 바꿔도 같은 20 이며,
        나머지 5 는 큐 밖 절에 남는다
  상한  (task 0320, Q169-a) 같은 순위·같은 공유 수의 대상 넷과 k = 2 에서 대상의 라벨만 바꾸어도 상한 안의 후보는 대상 IRI 가 작은 둘로 같다
  증거  `run_evidence` 는 판정 로그의 쌍 행을 판정 증거로 읽는다 — (−,−) 쌍도 후보(invalid 아님)이고, 입력 해시값이 지금 파일과 다른 행(낡은
        판정)과 이미 확정된 쌍의 행은 증거를 내지 않는다
  판정  `judge --pairs` 는 미끼 행을 로그에 넣지 않고 검출률(음성에 no, 양성에 yes)만 세고, 판정지 뒤에 본문이 바뀐 쌍은 행을 내지 않으며,
        기록은 질문마다 로그와 쌍마다 결과 주석 하나(파일 이름에 쌍 해시값 앞 8자, `targets:` 에 두 IRI)를 쓴다. 로그는 shape 를 지킨다
머리 전환 (Q161-a) — 판정 로그(`입력 해시값` 열)와 실행 기록(`테스트 케이스` 열)의 머리를 읽는 곳 넷이 기록 시각으로 머리를 가린다.
  전환 시각(kb_lib.RECORD_HEADER_SINCE) 이전 기록 + 새 머리와 이후 기록 + 옛 머리는 FAIL, 맞는 짝은 PASS 다. judge 기록은 새 머리를 쓴다.
사용: link_fixture_test.py [--vocab <o200k_base>]
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import sys
import tempfile
from pathlib import Path

from tools import judge, kb_lib, label_sample, link, run_evidence
from tools.chunk2kg import apply_plane_level_state, load_plane_level_state

ID = "https://agentic-knowledge-base.dev/id/"


def chunk(name: str, cls: str, level: str, loc: str, by: str = "human") -> str:
    return (f"<{ID}fx-{name}> a agt:{cls} ; rdfs:label \"{name}\"@ko ; agt:hasLevel agt:{level} ; agt:tokenCount 10 ; "
            f"agt:status \"stable\" ; agt:generatedBy \"{by}\" ; agt:assertionLocation \"{loc}\" .\n")


FIXTURE = (
    "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    + chunk("goal", "RequirementChunk", "functional", "kb/vv/goal/fx-goal.md")
    + chunk("req", "RequirementChunk", "functional", "kb/dev/requirement/fx-req.md")
    + chunk("module", "ArtifactChunk", "executable", "kb/dev/artifact/fx/module.md")
    + chunk("stim", "DecisionChunk", "logical", "kb/vv/scenario/fx-stimulus.md")
    + chunk("fn", "ArtifactChunk", "executable", "kb/dev/artifact/fx/fn-main.md")
    + chunk("dec", "DecisionChunk", "concrete", "kb/dev/decision/fx-dec.md")
    + chunk("case", "SchemaChunk", "concrete", "kb/vv/case/fx-case-1.md", kb_lib.CASE_GEN_ACTOR)
    + chunk("other", "DecisionChunk", "logical", "kb/vv/scenario/fx-other-stimulus.md")
    + f"<{ID}fx-section> agt:hasDirectPart <{ID}fx-fn> .\n"
    + f"<{ID}fx-goal> agt:cites <{ID}fx-req> .\n"
    + f"<{ID}fx-module> agt:cites <{ID}fx-stim> .\n"
    + f"<{ID}fx-fn> agt:cites <{ID}fx-dec> .\n"
    + f"<{ID}fx-case> agt:cites <{ID}fx-other> .\n"
)


def item(root: Path, rel: str, name: str, extra: str = "") -> str:
    """임시 트리에 결정 결론 하나를 쓰고 IRI 를 돌려준다."""
    iri = f"{ID}fx-{name}"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\nid: {iri}\ntype: decision\nlevel: concrete\ntitle_ko: 고정물 결정 {name}\ntitle: Fixture decision {name}\n"
                    f"status: draft\nsources: [{{resource: {ID}doc-system-notes}}]\nassumes: [{ID}asm-chunk-conventions]\n"
                    f"generated: {{by: developer/fixture, at: 2026-10-25T00:00:00Z}}\n{extra}---\n**결론** — 고정물 {name} 이다.\n",
                    encoding="utf-8")
    return iri


def judgement_view(tmp: Path) -> list[str]:
    """뷰 — 동시 편집 쌍 넷의 판정 넷과 큐, 절, 쌍 판정지의 되읽기."""
    names = ["p1a", "p1b", "p2a", "p2b", "p3a", "p3b", "p4a", "p4b"]
    ttl = "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    ttl += "".join(chunk(n, "DecisionChunk", "concrete", f"kb/dev/decision/fx-{n}/conclusion.md") for n in names)
    ttl += chunk("goal", "RequirementChunk", "functional", "kb/vv/goal/fx-goal.md") + chunk("req", "RequirementChunk", "functional", "kb/dev/requirement/fx-req.md")
    ttl += f"<{ID}fx-goal> agt:cites <{ID}fx-req> .\n"
    for k, pols in enumerate((["+", "+"], ["-", "-"], ["+", "-"]), 1):
        a, b = f"{ID}fx-p{k}a", f"{ID}fx-p{k}b"
        evs = " , ".join(f"<{ID}evidence/fx-{k}-{j}>" for j in range(2))
        ttl += (f"<{ID}link/fx-{k}> a agt:Link , agt:CandidateLink ; agt:linkFrom <{a}> ; agt:linkTo <{b}> ; agt:linkKind agt:overlapsWith ; "
                f"agt:linkState \"candidate\" ; agt:hasEvidence {evs} .\n")
        for j, p in enumerate(pols):
            ttl += f"<{ID}evidence/fx-{k}-{j}> a agt:Evidence ; agt:evidenceKind agt:judgement ; agt:polarity \"{p}\" .\n"
    (tmp / "judged-kg.ttl").write_text(ttl, encoding="utf-8")
    obs = tmp / f"{kb_lib.COEDIT_PREFIX}fx.md"
    rows = "".join(f"| `c{k}` | 2026-10-01T00:00:00Z | 2 | 1 | `fx-p{k}a` · `fx-p{k}b` |\n" for k in range(1, 5))
    obs.write_text(f"---\nid: {ID}fx-obs\n---\n{kb_lib.COEDIT_TABLE_HEADER}\n|---|---|---|---|---|\n{rows}", encoding="utf-8")
    out = tmp / "judged.md"
    sys.argv = ["link.py", "--out", str(out), "--root", str(tmp), "--coedit", str(obs), "--", str(tmp / "judged-kg.ttl")]
    fails = [] if link.main() == 0 else ["판정 뷰: 종료 코드가 0 이 아니다"]
    text = out.read_text(encoding="utf-8") if out.exists() else ""
    want = (f"{kb_lib.JUDGED_AGREE_YES} 1 · {kb_lib.JUDGED_AGREE_NO} 1 · {kb_lib.JUDGED_DISAGREE} 1 · {kb_lib.JUDGED_NONE} 1")
    if f"| 동시 편집 첫 근거 후보의 판정 | {want} |" not in text:
        fails.append(f"판정 뷰: 판정 넷이 1건씩이 아니다 — 기대 `{want}`")
    want_q = (f"| 사람 확인 큐 크기 | 3 — 첫 근거가 동시 편집이 아닌 후보 1 · {kb_lib.JUDGED_AGREE_YES} 1 · "
              f"{kb_lib.JUDGED_NO_SAMPLE_MARK} 1 |")
    if want_q not in text:
        fails.append("판정 뷰: 사람 확인 큐가 일치 둘(일치(−,−) 은 표본 상한 미만이라 전부)과 동시 편집이 아닌 후보 하나(3)가 아니다")
    outside_h = f"## {kb_lib.JUDGED_AGREE_NO} — 큐 밖, 판정 증거와 함께 후보로 남음"
    sections = {h: text.split(h, 1)[1].split("\n## ", 1)[0]
                for h in ("## 후보 — 사람 확인 큐", outside_h, "## 판정 불일치", "## 판정 없음") if h in text}
    p2 = next((ln for ln in sections.get("## 후보 — 사람 확인 큐", "").splitlines() if "fx-p2" in ln), "")
    if kb_lib.JUDGED_NO_SAMPLE_MARK not in p2:
        fails.append(f"판정 뷰: 큐의 일치(−,−) 쌍(p2)에 `{kb_lib.JUDGED_NO_SAMPLE_MARK}` 표기가 없다")
    if outside_h not in sections or "fx-p" in sections[outside_h]:
        fails.append("판정 뷰: 큐 밖 일치(−,−) 절이 없거나, 표본 상한 미만인데 큐 밖에 쌍이 있다")
    where = {"fx-p1a": "## 후보 — 사람 확인 큐", "fx-p2a": "## 후보 — 사람 확인 큐", "fx-p3a": "## 판정 불일치", "fx-p4a": "## 판정 없음"}
    for n, h in where.items():
        if f"fx-{n[3:]}/conclusion.md" not in sections.get(h, "") and f"fx-{n[3:-1]}b/conclusion.md" not in sections.get(h, ""):
            fails.append(f"판정 뷰: {n} 의 쌍이 `{h}` 절에 없다")
    picked = label_sample.pair_judge_targets(label_sample.view_candidates(out))
    if len(picked) != 1 or "fx-p4" not in picked[0]["앵커 파일"] + picked[0]["대상 IRI"]:
        fails.append(f"쌍 판정지: 뷰를 되읽어 판정 없음 하나(p4)만 골라야 한다 — 실제 {[p['앵커 파일'] for p in picked]}")
    return fails


def judged_sample() -> list[str]:
    """일치(−,−) 표본 (task 0303, Q165-c) — 합성 후보로 judged_sections 를 직접 부른다. 일치(−,−) 25 · 일치(+,+) 2 · 동시 편집이 아닌 후보 3 이면
    큐는 3 + 2 + 표본 20 = 25 이고, 표본은 sha256(시드 ∣ 앵커 ∣ 대상 ∣ 종류)이 가장 작은 20 쌍이며 입력 순서를 바꿔도 같다. 표본 밖 5 는 큐 밖 절에 있다."""
    from types import SimpleNamespace
    u = SimpleNamespace(ko=lambda x: str(x).rsplit("/", 1)[-1], loc={})
    co = lambda pols: [(0, "coEditHistory", "`c1`", 0), (9, "judgement", pols, 0)]  # noqa: E731

    def make() -> list:
        cands = [{"anchor": f"{ID}fx-n{k}a", "target": f"{ID}fx-n{k}b", "kind": "overlapsWith", "evs": co("- -")} for k in range(25)]
        cands += [{"anchor": f"{ID}fx-y{k}a", "target": f"{ID}fx-y{k}b", "kind": "overlapsWith", "evs": co("+ +")} for k in range(2)]
        cands += [{"anchor": f"{ID}fx-c{k}a", "target": f"{ID}fx-c{k}b", "kind": "refines", "evs": [(0, "constructionRecord", "x", 0)]}
                  for k in range(3)]
        return cands

    def rank(k: int) -> str:
        key = "\t".join((kb_lib.JUDGED_NO_SAMPLE_SEED, f"{ID}fx-n{k}a", f"{ID}fx-n{k}b", "overlapsWith"))
        return hashlib.sha256(key.encode("utf-8")).hexdigest()
    want = {f"fx-n{k}a" for k in sorted(range(25), key=rank)[:kb_lib.JUDGED_NO_SAMPLE_SIZE]}
    outside_h = f"## {kb_lib.JUDGED_AGREE_NO} — 큐 밖, 판정 증거와 함께 후보로 남음"

    def run(cands: list) -> tuple[list[str], set, set, int]:
        summary, lines = link.judged_sections(u, cands)
        text = "\n".join(lines)
        part = lambda h: text.split(h, 1)[1].split("\n## ", 1)[0] if h in text else ""  # noqa: E731
        rows = lambda h: [ln.split("|") for ln in part(h).splitlines() if ln.startswith("| ") and ln.split("|")[1].strip().isdigit()]  # noqa: E731
        queue = rows("## 후보 — 사람 확인 큐")
        sampled = {r[2].strip() for r in queue if kb_lib.JUDGED_NO_SAMPLE_MARK in "|".join(r)}
        out = {r[2].strip() for r in rows(outside_h)}
        return summary, sampled, out, len(queue)

    fails = []
    summary, sampled, out, n_queue = run(make())
    if kb_lib.JUDGED_NO_SAMPLE_SIZE != 20 or len(sampled) != kb_lib.JUDGED_NO_SAMPLE_SIZE:
        fails.append(f"표본: 크기가 {kb_lib.JUDGED_NO_SAMPLE_SIZE}(20) 이 아니다 — 큐의 표본 표기 {len(sampled)}")
    if sampled != want:
        fails.append("표본: sha256(시드 ∣ 앵커 ∣ 대상 ∣ 종류) 이 가장 작은 20 쌍이 아니다")
    if n_queue != 25:
        fails.append(f"표본: 큐가 3 + 2 + 20 = 25 행이 아니다 — {n_queue}")
    want_q = f"| 사람 확인 큐 크기 | 25 — 첫 근거가 동시 편집이 아닌 후보 3 · {kb_lib.JUDGED_AGREE_YES} 2 · {kb_lib.JUDGED_NO_SAMPLE_MARK} 20 |"
    if want_q not in summary:
        fails.append(f"표본: 요약의 큐 크기 줄이 `{want_q}` 가 아니다 — {summary}")
    if len(out) != 5 or out & sampled or (out | sampled) != {f"fx-n{k}a" for k in range(25)}:
        fails.append(f"표본: 표본 밖 일치(−,−) 5 가 큐 밖 절에 없다 — {len(out)}")
    _, again, _, _ = run(list(reversed(make())))
    if again != sampled:
        fails.append("표본: 입력 순서를 바꾸자 표본이 달라졌다 — 재현되지 않는다")
    return fails


def cap_label_free(tmp: Path) -> list[str]:
    """상한 구성 (task 0320, Q169-a) — 앵커 하나가 같은 순위(본문 인용)·같은 공유 수(0)의 대상 넷을 인용하고 k = 2 이면, 대상의 라벨 순서를
    IRI 순서와 같게 한 그래프와 거꾸로 한 그래프에서 상한 안의 후보 집합이 같다 — 대상 IRI 가 작은 둘이고 탈락은 둘이다
    (p9-candidate-generation-limits). 라벨은 자른 뒤 표시 순서에만 쓴다."""
    head = "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    targets = [f"cap-t{i}" for i in range(1, 5)]
    picked = {}
    for name, labels in (("same", ["가", "나", "다", "라"]), ("reversed", ["라", "다", "나", "가"])):
        ttl = head + chunk("cap-a", "DecisionChunk", "concrete", "kb/dev/decision/fx-cap-a/conclusion.md")
        for t, lab in zip(targets, labels):
            ttl += chunk(t, "DecisionChunk", "concrete", f"kb/dev/decision/fx-{t}/conclusion.md").replace(f'"{t}"@ko', f'"{lab}"@ko')
            ttl += f"<{ID}fx-cap-a> agt:cites <{ID}fx-{t}> .\n"
        src, out = tmp / f"cap-{name}-kg.ttl", tmp / f"cap-{name}.md"
        src.write_text(ttl, encoding="utf-8")
        sys.argv = ["link.py", "--out", str(out), "--root", str(tmp), "--k", "2", "--", str(src)]
        if link.main() != 0:
            return [f"상한 구성: {name} 그래프에서 종료 코드가 0 이 아니다"]
        text = out.read_text(encoding="utf-8")
        rows = [ln for ln in text.splitlines() if ln.startswith("| ") and ln.split("|")[1].strip().isdigit()]
        picked[name] = sorted(t for t in targets for r in rows if f"fx-{t}/conclusion.md" in r or f"fx-{t}`" in r)
        if f"{link.R_CAP} 2" not in next((ln for ln in text.splitlines() if ln.startswith("| 탈락 수 |")), ""):
            return [f"상한 구성: {name} 그래프의 탈락 분포에 `{link.R_CAP} 2` 가 없다"]
    fails = []
    if picked["same"] != picked["reversed"]:
        fails.append(f"상한 구성: 라벨만 바꾸자 상한 안의 후보가 바뀌었다 — {picked['same']} → {picked['reversed']}")
    if picked["same"] != targets[:2]:
        fails.append(f"상한 구성: 상한 안의 후보가 대상 IRI 가 작은 둘({targets[:2]})이 아니다 — {picked['same']}")
    return fails


def judge_log(rows: list[tuple[str, str, str, str]], log_iri: str, at: str = "2026-10-26T00:00:00Z",
              header: str = kb_lib.JUDGE_LOG_TABLE_HEADER) -> str:
    """판정 로그 하나의 글 — rows 는 (대상, 값, 판정자, 입력 해시값). 기본은 전환 시각 뒤의 기록 시각과 새 머리다."""
    body = "".join(f"| `agt:overlapsHolds` | `{t}` | `{v}` | 0.900 | `{j}` | `{fp}` | {at} | 사람 확인 큐 | 일치 |\n"
                   for t, v, j, fp in rows)
    return (f"---\nid: {log_iri}\ntype: memory\nlevel: concrete\ntitle_ko: 고정물 판정 로그\ntitle: Fixture judgement log\nstatus: stable\n"
            f"sources: [{{resource: {ID}doc-system-notes}}]\ngenerated: {{by: {kb_lib.JUDGE_GENERATOR}, at: {at}}}\n---\n"
            f"**관측** — 고정물이다.\n\n{header}\n|---|---|---|---|---|---|---|---|---|\n{body}\n"
            f"{kb_lib.JUDGE_LOG_DECOY}해당 없음 — 고정물\n")


def judgement_evidence(tmp: Path) -> list[str]:
    """증거 — (−,−) 는 후보로 남고 낡은 판정과 확정된 쌍은 증거를 내지 않는다."""
    root = tmp / "ev"
    a, b = item(root, "kb/dev/decision/fx-ea/conclusion.md", "ea"), item(root, "kb/dev/decision/fx-eb/conclusion.md", "eb")
    c = item(root, "kb/dev/decision/fx-ec/conclusion.md", "ec")
    d = item(root, "kb/dev/decision/fx-ed/conclusion.md", "ed", f"overlapsWith: [{ID}fx-ec]\n")
    fresh = kb_lib.pair_record_fingerprint((root / "kb/dev/decision/fx-ea/conclusion.md").read_bytes(),
                                           (root / "kb/dev/decision/fx-eb/conclusion.md").read_bytes())
    stale = kb_lib.pair_record_fingerprint(b"old", b"bytes")
    confirmed = kb_lib.pair_record_fingerprint((root / "kb/dev/decision/fx-ed/conclusion.md").read_bytes(),
                                               (root / "kb/dev/decision/fx-ec/conclusion.md").read_bytes())
    log = root / "kb/vv/run" / f"{kb_lib.JUDGE_LOG_PREFIX}fx.md"
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(judge_log([(kb_lib.pair_target(a, b, "overlapsWith"), "no", "fx/one", fresh),
                              (kb_lib.pair_target(a, b, "overlapsWith"), "no", "fx/two", fresh),
                              (kb_lib.pair_target(b, c, "overlapsWith"), "yes", "fx/one", stale),
                              (kb_lib.pair_target(d, c, "overlapsWith"), "no", "fx/one", confirmed)], f"{ID}fx-log"), encoding="utf-8")
    out = tmp / "ev.ttl"
    sys.argv = ["run_evidence.py", "--out", str(out), "--residency", str(Path("defs/kb.bzl").resolve()),
                *sorted(str(p) for p in root.rglob("*.md"))]
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        code = run_evidence.main()
    from rdflib import Graph
    g = Graph().parse(str(out), format="turtle") if out.exists() else Graph()
    AGT = kb_lib.AGT
    fails = [] if code == 0 else [f"판정 증거: run_evidence 종료 코드 {code} — {err.getvalue()[-300:]}"]
    judged = [e for e in g.subjects(AGT.evidenceKind, AGT.judgement)]
    links = {(str(next(g.objects(l, AGT.linkFrom))), str(next(g.objects(l, AGT.linkTo)))): str(next(g.objects(l, AGT.linkState)))
             for l in g.subjects(AGT.linkState, None)}
    if len(judged) != 2 or {str(next(g.objects(e, AGT.polarity))) for e in judged} != {"-"}:
        fails.append(f"판정 증거: (−,−) 쌍의 판정 증거 둘이 아니다 — 실제 {len(judged)}건")
    if links.get((a, b)) != kb_lib.LINK_STATE_CANDIDATE:
        fails.append(f"판정 증거: 반박만 있는 판정 쌍이 후보가 아니다 — 실제 {links.get((a, b))} (invalid 는 실행 증거 전용)")
    if (b, c) in links or (d, c) in links:
        fails.append("판정 증거: 낡은 판정 또는 확정된 쌍의 행이 링크를 냈다")
    if any(str(r) != f"{ID}fx-log" for e in judged for r in g.objects(e, AGT.evidenceRef)):
        fails.append("판정 증거: 참조가 판정 로그가 아니다")
    return fails


def judgement_pairs(tmp: Path, vocab: str) -> list[str]:
    """판정 — 미끼는 검출률만, 낡은 쌍은 행 없음, 기록은 질문마다 로그와 쌍마다 결과 주석 하나."""
    root = tmp / "jp"
    for n in ("ja", "jb", "jc", "jd", "je", "jf"):
        item(root, f"kb/dev/decision/fx-{n}/conclusion.md", n)
    shown = lambda n: {"path": f"kb/dev/decision/fx-{n}/conclusion.md", "id": f"{ID}fx-{n}", "title_ko": f"고정물 결정 {n}",  # noqa: E731
                       "title": f"Fixture decision {n}", "body": f"**결론** — 고정물 {n} 이다."}
    entries = []
    for k, (x, y, decoy, kind) in enumerate((("ja", "jb", None, "overlapsWith"), ("jc", "jd", None, "refines"), ("jc", "je", None, "overlapsWith"),
                                             ("je", "jf", "neg", "overlapsWith"), ("ja", "jf", "pos", "overlapsWith")), 1):
        an, ta = shown(x), shown(y)
        q = kb_lib.pair_question(kind)
        entries.append({"n": k, "question": q, "kind": kind, "decoy": decoy, "anchor": an, "target": ta,
                        "fingerprint": kb_lib.pair_fingerprint(q, kind, an, ta)})
    (root / "kb/dev/decision/fx-je/conclusion.md").write_text(  # 판정지 뒤에 본문이 바뀐 쌍 — 낡은 판정
        (root / "kb/dev/decision/fx-je/conclusion.md").read_text(encoding="utf-8") + "덧붙인 문장이다.\n", encoding="utf-8")
    key = tmp / "key.json"
    key.write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    resp = []
    for j, flip in (("fx/one", False), ("fx/two", True)):
        rs = [{"question": e["question"], "fingerprint": e["fingerprint"], "confidence": 0.7,
               "value": ("no" if e["decoy"] == "neg" else "yes") if not (flip and e["n"] in (2, 5)) else "no"} for e in entries]
        p = tmp / f"resp-{j[3:]}.json"
        p.write_text(json.dumps({"judge": j, "responses": rs}), encoding="utf-8")
        resp.append(str(p))
    buf, err, old = io.StringIO(), io.StringIO(), os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    os.environ["BUILD_WORKSPACE_DIRECTORY"] = str(Path(".").resolve())
    sys.argv = ["judge.py", "--pairs", str(key), "--responses", resp[0], "--responses", resp[1], "--record", "--into", str(root),
                "--vocab", vocab, "--residency", str(Path("defs/kb.bzl").resolve())]
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            os.chdir(root)  # 쌍의 상대 경로는 워크스페이스 기준이다 — 고정물 트리를 워크스페이스로 본다
            os.environ["BUILD_WORKSPACE_DIRECTORY"] = str(root)
            for sub in ("kb/ontology/profile/development", "kb/ontology/shapes"):
                (root / sub).parent.mkdir(parents=True, exist_ok=True)
                if not (root / sub).exists():
                    (root / sub).symlink_to(Path(RUNFILES, sub).resolve())
            code = judge.main()
    finally:
        os.chdir(RUNFILES)
        if old is None:
            os.environ.pop("BUILD_WORKSPACE_DIRECTORY", None)
        else:
            os.environ["BUILD_WORKSPACE_DIRECTORY"] = old
    out = buf.getvalue()
    fails = [] if code == 0 else [f"쌍 판정: judge 종료 코드 {code} — {err.getvalue()[-300:]}"]
    if "판정 행 4 · 응답 없음 0 · 낡은 판정 2" not in out:
        fails.append("쌍 판정: 행 4(실쌍 둘 × 판정자 둘)와 낡은 판정 2 가 아니다")
    if "음성 미끼 1건 중 응답 대조 2건 · 검출(no) 2건" not in out or "양성 미끼 1건 중 응답 대조 2건 · 검출(yes) 1건" not in out:
        fails.append("쌍 판정: 미끼 검출이 음성 2/2 · 양성 1/2 가 아니다")
    logs = sorted((root / kb_lib.JUDGE_LOG_DIR).glob(f"{kb_lib.JUDGE_LOG_PREFIX}*.md"))
    verdicts = sorted((root / kb_lib.JUDGE_VERDICT_DIR).glob("*.md"))
    if len(logs) != 2:
        fails.append(f"쌍 판정: 로그가 질문마다 하나(2)가 아니다 — {len(logs)}")
    for lg in logs:
        text = lg.read_text(encoding="utf-8")
        if "fx-je" in text or "fx-jf" in text:
            fails.append(f"쌍 판정: {lg.name} 에 미끼나 낡은 쌍의 행이 있다")
        if kb_lib.judge_log_violations(text, Path(RUNFILES, kb_lib.JUDGE_LOG_SHAPES)):
            fails.append(f"쌍 판정: {lg.name} 이 일치율 shape 를 어긴다")
        if kb_lib.JUDGE_LOG_TABLE_HEADER not in text:
            fails.append(f"쌍 판정: {lg.name} 이 새 머리(`입력 해시값` 열)를 쓰지 않는다 — 전환 시각 뒤의 기록이다 (Q161-a)")
        if any(kb_lib.parse_pair_target(r["대상"]) is None for r in kb_lib.judge_log_rows(text)):
            fails.append(f"쌍 판정: {lg.name} 의 대상 열이 쌍 꼴이 아니다")
    want = {f"{kb_lib.JUDGE_LOG_PREFIX}{e['question'].lower()}-pair-{e['fingerprint'][:8]}.md" for e in entries[:2]}
    if {v.name for v in verdicts} != want:
        fails.append(f"쌍 판정: 결과 주석이 쌍마다 하나가 아니다 — {sorted(v.name for v in verdicts)}")
    for v in verdicts:
        text = v.read_text(encoding="utf-8")
        if f"targets: [{ID}fx-ja, {ID}fx-jb]" not in text and f"targets: [{ID}fx-jc, {ID}fx-jd]" not in text:
            fails.append(f"쌍 판정: {v.name} 의 targets 가 두 IRI 가 아니다")
    return fails


def record_header_switch() -> list[str]:
    """기록 표 머리의 전환 (Q161-a) — 머리를 읽는 곳마다 두 방향. 전환 시각 이전 기록 + 새 머리 → FAIL(읽지 않음),
    이후 기록 + 옛 머리 → FAIL, 맞는 짝 → PASS. 판정 로그는 chunk_lint `judge-log` 게이트와 kb_lib.judge_log_rows(run_evidence 판정
    증거·judge_log_graph 의 읽기), 실행 기록은 run_evidence.run_rows 와 weave audit 의 최근 실행 절이다."""
    from types import SimpleNamespace
    from tools import chunk_lint, weave
    before, after = "2026-10-01T00:00:00Z", "2026-10-26T00:00:00Z"
    new_j, old_j = kb_lib.JUDGE_LOG_TABLE_HEADER, kb_lib.JUDGE_LOG_TABLE_HEADER_OLD
    new_r, old_r = kb_lib.RUN_CASE_TABLE_HEADER, kb_lib.RUN_CASE_TABLE_HEADER_OLD
    fp = "0" * 64
    pairs = (("이전 기록 + 새 머리", before, new_j, new_r, False),
             ("이후 기록 + 옛 머리", after, old_j, old_r, False),
             ("이전 기록 + 옛 머리", before, old_j, old_r, True),
             ("이후 기록 + 새 머리", after, new_j, new_r, True))
    fails = []
    for name, at, jh, rh, ok in pairs:
        log = judge_log([(f"{ID}fx-a", "yes", "fx/one", fp)], f"{ID}fx-log", at=at, header=jh)
        gate = chunk_lint.check_judge_log(log)
        if bool(gate) == ok:
            fails.append(f"머리 전환: chunk_lint judge-log 가 {name} 에 {'FAIL' if gate else 'PASS'} 다 — 기대 {'PASS' if ok else 'FAIL'}")
        rows = kb_lib.judge_log_rows(log)
        if bool(rows) != ok or (ok and rows[0].get("입력 해시값") != fp):
            fails.append(f"머리 전환: judge_log_rows 가 {name} 에서 행 {len(rows)}개를 읽었다 — 기대 {'1' if ok else '0'}")
        body = f"**관측** — 고정물이다.\n\n{rh}\n|---|---|---|---|\n| `fx-case` | 1 실행 · 0 건너뜀 | pass | 0.1s |\n"
        read = run_evidence.run_rows(body, at)
        if bool(read) != ok:
            fails.append(f"머리 전환: run_evidence.run_rows 가 {name} 에서 행 {len(read)}개를 읽었다 — 기대 {'1' if ok else '0'}")
        m = SimpleNamespace(at=lambda _c, _at=at: _at, ko=lambda _c: "고정물 실행", location={"r": "kb/vv/run/run-fx.md"})
        audit = "\n".join(weave._audit_latest_run(m, ["r"], "r", body, lambda _c: "process:vv_run"))
        if ("pass **1**" in audit) != ok:
            fails.append(f"머리 전환: weave audit 최근 실행 절이 {name} 에서 {'행을 읽었다' if not ok else '행을 읽지 못했다'}")
    return fails


RUNFILES = Path(".").resolve()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocab", default="")
    args = ap.parse_args()
    apply_plane_level_state(*load_plane_level_state("defs/kb.bzl"))
    tmp = Path(os.environ.get("TEST_TMPDIR") or tempfile.mkdtemp())
    ttl, out = tmp / "fx-kg.ttl", tmp / "link-candidates.md"
    ttl.write_text(FIXTURE, encoding="utf-8")
    sys.argv = ["link.py", "--out", str(out), "--root", str(tmp), str(ttl)]
    code = link.main()
    text = out.read_text(encoding="utf-8") if out.exists() else ""
    rows = [ln for ln in text.splitlines() if ln.startswith("| ") and ln.split("|")[1].strip().isdigit()]
    summary = next((ln for ln in text.splitlines() if ln.startswith("| 탈락 수 |")), "")
    fails = []
    if code != 0:
        fails.append(f"종료 코드 {code} — 0 이어야 한다")
    if len(rows) != 1 or "`kb/vv/goal/fx-goal.md`" not in rows[0] or "`derivesFrom`" not in rows[0]:
        fails.append(f"양성: 후보는 목표 → 요구 derivesFrom 하나여야 한다 — 실제 {rows}")
    for anchor in ("kb/dev/artifact/fx/module.md", "kb/dev/artifact/fx/fn-main.md", "kb/vv/case/fx-case-1.md"):
        if any(f"`{anchor}`" in r for r in rows):
            fails.append(f"음성: {anchor} 앵커 후보가 남았다")
    for reason in (link.R_CROSS_LINK, link.R_CODE_PART, link.R_CASE_DERIVES):
        if f"{reason} 1" not in summary:
            fails.append(f"음성: 탈락 분포에 `{reason} 1` 이 없다 — {summary}")
    fails += judgement_view(tmp) + judged_sample() + cap_label_free(tmp) + judgement_evidence(tmp) + record_header_switch()
    if args.vocab:
        fails += judgement_pairs(tmp, str(Path(args.vocab).resolve()))
    else:
        fails.append("쌍 판정: --vocab 이 없다 — 기록 시험은 계수기가 입력이다")
    for f in fails:
        print(f"FAIL [link-fixture] {f}")
    if not fails:
        print("PASS [link-fixture] — 양성 1 (목표 → 요구 derivesFrom) · 음성 3 (KB 가로지름 · 코드 부분 끝점 · 케이스의 derivesFrom) · "
              "판정 넷 · 일치(−,−) 표본(크기·재현·큐 구성) · 상한 구성(라벨 무관) · 판정 증거(반박만은 후보, 낡음·확정은 없음) · 쌍 판정 기록 · 기록 머리 전환(두 방향 × 읽는 곳 넷)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
