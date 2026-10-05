#!/usr/bin/env python3
"""지표(`tools/metrics.py`)의 설계 공간 회계 시험 — 연결 성분과 결정 완결률 (유저 결정 Q60-a).

고정물은 시험이 메모리에 짓는 그래프 둘이다. 지식 그래프에는 요구 하나와 결정 복합체 넷이 있고, 설계 공간 그래프에는
공간 둘이 있다. 후보 결론은 head 에 `refines` 를 갖지 않는다 (p9-candidate-storage "후보는 절대 deps가 되지 않는다").
  확정       결론이 요구를 `refines` 한다. resolved 공간의 confirmed 후보다 — 확정 결정으로 분모에 남는다
  열린 후보  결론이 open 공간의 open 후보다 — 분모·분자에서 빠지고 따로 센다
  배제 후보  결론이 open 공간의 eliminated 후보다 — 열린 후보가 아니므로 분모에 남는다
  외톨이     어느 공간에도 없고 링크도 없다 — 공간 링크를 세어도 따로 남는 성분이다
  양성  공간 링크를 세면 연결 성분이 4 에서 2 가 된다(외톨이 하나만 남는다). 후보 결정은 열린 후보 하나다
  음성  공간 링크 없이는 후보 복합체가 각자 성분이다. 공간 술어는 추적 링크 잎(링크 밀도·TIM)에 들지 않는다
"""
from __future__ import annotations

import sys

from rdflib import Graph, URIRef

from tools import kb_lib, metrics

ID = "https://agentic-knowledge-base.dev/id/"
PFX = "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n"


def decision(name: str, refines: str = "") -> str:
    """결론·대안 두 부분의 결정 복합체."""
    out = ""
    for slot in ("conclusion", "alternatives"):
        out += f'<{ID}fx-{name}-{slot}> agt:bodySlot "{"결론" if slot == "conclusion" else "대안"}" .\n'
        out += f"<{ID}fx-{name}> agt:hasDirectPart <{ID}fx-{name}-{slot}> .\n"
    if refines:
        out += f"<{ID}fx-{name}-conclusion> agt:refines <{ID}fx-{refines}> .\n"
    return out


# T-Box 한 줄 — kb_lib.linkage_predicates 는 세 족의 잎을 `agt:dependsOn` 아래에서 찾고 없으면 죽는다
TBOX = "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\nagt:refines rdfs:subPropertyOf agt:dependsOn .\n"
KG = PFX + TBOX + decision("fixed", refines="req") + decision("open") + decision("elim") + decision("lone")
NAMES = ["req"] + [f"{n}-{s}" for n in ("fixed", "open", "elim", "lone") for s in ("conclusion", "alternatives")]


def space(name: str, status: str, cands: list[tuple[str, str]]) -> str:
    out = f'<{ID}sp-{name}> a agt:Space ; agt:spaceStatus "{status}" ; agt:variableFrom <{ID}fx-req> .\n'
    for i, (to, state) in enumerate(cands):
        link = f"{ID}link/{name}{i}"
        out += f"<{ID}sp-{name}> agt:hasCandidate <{link}> .\n"
        out += f'<{link}> a agt:Link ; agt:linkTo <{ID}fx-{to}-conclusion> ; agt:linkState "{kb_lib.SPACE_STATE_LINK[state][1]}" .\n'
    return out


SPACES = PFX + space("open", "open", [("open", "open"), ("elim", "eliminated")]) + space("done", "resolved", [("fixed", "confirmed")])


def main() -> int:
    metrics.LEVELS[:] = ["functional", "abstract", "logical", "concrete", "executable"]  # 원본은 defs/kb.bzl — 성분 계산에는 쓰지 않는다
    g, gs = Graph(), Graph()
    g.parse(data=KG, format="turtle")
    gs.parse(data=SPACES, format="turtle")
    chunks = {URIRef(ID + "fx-" + n) for n in NAMES}
    plane = {c: ("requirement" if c.endswith("req") else "decision") for c in chunks}
    level = {c: "logical" for c in chunks}
    status = {c: "draft" for c in chunks}
    comp_of = {o: s for s, o in g.subject_objects(kb_lib.AGT.hasDirectPart)}
    siblings: dict = {}
    for part, comp in comp_of.items():
        siblings.setdefault(comp, set()).add(part)
    authored = sorted(chunks, key=str)
    fails = []

    edges = kb_lib.space_linkage_edges(gs)
    # 공간 둘의 변수 출발 항목 둘 + 후보 셋 (eliminated 도 연결로 센다)
    if len(edges) != 5:
        fails.append(f"공간 연결 쌍이 5 가 아니다: {len(edges)}")
    without = metrics.axis_proxies(g, chunks, plane, level, authored, comp_of, siblings, {})[0]
    with_ = metrics.axis_proxies(g, chunks, plane, level, authored, comp_of, siblings, {}, edges)
    if without != 4:
        fails.append(f"음성: 공간 링크 없이 성분이 4 가 아니다: {without}")
    if with_[0] != 2:
        fails.append(f"양성: 공간 링크를 세면 성분이 2 여야 한다: {with_[0]}")
    if [sorted(str(c) for c in m) for m in with_[1]] != [sorted(f"{ID}fx-lone-{s}" for s in ("alternatives", "conclusion"))]:
        fails.append(f"양성: 주 성분 밖은 외톨이 복합체 하나여야 한다: {with_[1]}")

    open_c = kb_lib.open_space_candidates(gs)
    if open_c != {URIRef(f"{ID}fx-open-conclusion")}:
        fails.append(f"열린 후보 집합이 열린 후보 결론 하나가 아니다: {sorted(map(str, open_c))}")
    decisions, missing, _, cand = metrics.decision_completeness(g, chunks, plane, status, comp_of, siblings, open_c)
    if sorted(map(str, cand)) != [f"{ID}fx-open"]:
        fails.append(f"양성: 후보 결정은 열린 후보 복합체 하나여야 한다: {sorted(map(str, cand))}")
    if sorted(map(str, decisions)) != sorted(f"{ID}fx-{n}" for n in ("fixed", "elim", "lone")):
        fails.append(f"양성: 분모는 확정·배제·외톨이 셋이어야 한다 (confirmed·eliminated 는 남는다): {sorted(map(str, decisions))}")
    if missing:
        fails.append(f"대안 없는 결정이 없어야 한다: {missing}")
    base = metrics.decision_completeness(g, chunks, plane, status, comp_of, siblings)
    if len(base[0]) != 4 or base[3]:
        fails.append(f"음성: 공간 없이는 네 결정이 모두 분모다: {len(base[0])} · 후보 {len(base[3])}")

    if set(kb_lib.SPACE_LINKAGE_PREDICATES) & set(kb_lib.TRACE_LINKS + kb_lib.LINKAGE_PREDICATES):
        fails.append("공간 술어가 추적 링크 잎·연결 술어에 섞였다 — 링크 밀도·TIM 이 바뀐다")

    for f in fails:
        print("FAIL:", f)
    print("PASS" if not fails else f"{len(fails)} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
