#!/usr/bin/env python3
"""설계 공간 청크(`-space`) → 설계 공간 그래프(`*-space.ttl`) 생성.

설계 변수 하나가 파일 하나다. 후보 링크는 확정 링크와 **다른 자리**에 저장된다 — 확정은 청크 head(frontmatter
링크 키 → Bazel deps), 후보는 `-space` 청크다. **후보는 결코 deps 가 되지 않는다**: 이 생성기는 `kb_chunk` 타깃을
만들지 않고 A-Box 그래프만 내며, 그 그래프는 `//kg:gate_test` 의 `--data` 로 들어가 통제 어휘·SHACL·안티패턴
질의·`check_space` 의 판정을 받는다 (결정 p9-candidate-storage · p9-design-space-file).

frontmatter 는 청크와 같고(`tools/chunk2kg.py` 의 REQUIRED) `type: agt:Space` · `level: logical` 이다.
본문은 언어 태그 `yaml` 을 단 펜스 블록 하나이고 키는 여섯이다:

  variable     {from: <출발 항목 IRI>, kind: <링크 타입>} (필수) — 미확정은 언제나 두 항목이 연결되는가의
               미확정이므로 변수는 값이 아니라 출발 항목과 링크 타입의 쌍이다 (p9-uncertainty-as-link-uncertainty)
  status       open | resolved (필수) — resolved 면 `state: confirmed` 인 후보가 정확히 하나다
  candidates   후보 목록 (선택 — abstract 단계는 variable 까지만 채운다). 항목의 키는 다섯이다:
               to(대상 IRI, 필수) · state(open|eliminated|confirmed, 필수) · when(CEL 술어, 선택) ·
               evidence(지지 증거 목록 [{kind, ref}], 선택) · eliminated_by(배제 근거 {kind, ref}, eliminated 전용·필수)
  constraints  양립 제약 CEL 술어 목록 (선택) → agt:compatibilityConstraint
  preferences  후보 사이의 부분순서 [{prefer: <IRI>, over: <IRI>}] (선택) → agt:preferredOver. 수치는 붙이지 않는다
  후보의 표면 상태는 링크 상태의 기존 값으로 내린다 (kb_lib.SPACE_STATE_LINK) — open 은 agt:CandidateLink 와
  linkState candidate, eliminated 는 linkState invalid, confirmed 는 agt:ConfirmedLink 와 linkState confirmed 다.
  배제 근거·지지 증거는 증거 기록 한 줄(agt:Evidence)로 나가고 극성은 배제가 `-`, 지지가 `+` 다. 기각된 후보는
  지우지 않는다 — logical 은 근거의 보존소이고, 확정되는 순간 후보가 head 로 옮겨져 한 줄 diff 로 리뷰된다.

출력·종료: 위반은 `FAIL [space] <경로>: <메시지>` + EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
           생성기이므로 입력 0건은 빈 그래프다 (SKIP 아님).
사용: space2kg.py --out <생성.ttl> <-space 청크…>   (bazel build //space:design_space)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chunk2kg  # noqa: E402 — frontmatter 파서·링크 IRI 규칙의 정의처

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행: 스크립트 디렉토리 기준

GATE = kb_lib.SPACE_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
BODY_KEYS = ("variable", "status", "candidates", "constraints", "preferences")
CANDIDATE_KEYS = ("to", "state", "when", "evidence", "eliminated_by")
EVIDENCE_KEYS = ("kind", "ref")
# 증거 종류 — evidence-ontology 의 살아 있는 개체 (폐기된 counterfactualTest 는 뺀다)
EVIDENCE_KINDS = ("constructionRecord", "coEditHistory", "testCoverage", "runResult", "proposal",
                  "embeddingSimilarity", "coRead")
PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 `-space` 청크의 frontmatter 와 본문이다.
# 생성: tools/space2kg.py (bazel build //space:design_space)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


# ── 설계 공간 본문 파싱 ────────────────────

class SpaceError(ValueError):
    """설계 공간의 형식 위반 — 메시지가 `<경로>: <근거>` 다. 게이트 id 는 GATE."""


def body_block(path: str, body: str) -> dict:
    """본문의 `yaml` 펜스 블록 하나를 읽어 매핑으로 돌려준다. 블록이 없거나 둘이면 거부한다."""
    lines, blocks, cur, fence = body.split("\n"), [], None, None
    for line in lines:
        m = kb_lib.MD_FENCE.match(line)
        if fence is None:
            if m:
                fence, cur = m.group(1), []
                if line.strip()[len(fence):].strip() != "yaml":
                    raise SpaceError(f"{path}: 본문 펜스에 언어 태그 `yaml` 이 없다 — 설계 공간의 본문은 yaml 블록 하나다")
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            blocks.append("\n".join(cur))
            fence, cur = None, None
            continue
        cur.append(line)
    if fence is not None:
        raise SpaceError(f"{path}: 본문의 펜스가 닫히지 않았다")
    if len(blocks) != 1:
        raise SpaceError(f"{path}: 본문에 `yaml` 펜스 블록이 정확히 하나여야 한다 — 실제 {len(blocks)}개 (p9-design-space-file)")
    try:
        data = yaml.safe_load(blocks[0])
    except yaml.YAMLError as e:
        raise SpaceError(f"{path}: 본문 yaml 을 읽을 수 없다 — {e}")
    if not isinstance(data, dict):
        raise SpaceError(f"{path}: 본문 yaml 은 매핑이어야 한다 — 키는 {' · '.join(BODY_KEYS)} 다")
    unknown = sorted(set(data) - set(BODY_KEYS))
    if unknown:
        raise SpaceError(f"{path}: 알 수 없는 본문 키 {unknown} — 키는 {' · '.join(BODY_KEYS)} 다 (p9-candidate-storage)")
    return data


def evidence_of(path: str, where: str, value, polarity: str) -> list[tuple[str, str]]:
    """증거 항목 → [(종류, 참조)]. 종류는 evidence-ontology 의 개체 이름이어야 한다."""
    items = value if isinstance(value, list) else [value]
    out = []
    for item in items:
        if not isinstance(item, dict) or sorted(item) != sorted(EVIDENCE_KEYS):
            raise SpaceError(f"{path}: {where} 의 증거는 {{{', '.join(EVIDENCE_KEYS)}}} 여야 한다 — 실제 {item!r}")
        kind, ref = str(item["kind"]), str(item["ref"])
        if kind not in EVIDENCE_KINDS:
            raise SpaceError(f"{path}: {where} 의 증거 종류 {kind!r} 가 어휘 밖이다 — {' | '.join(EVIDENCE_KINDS)} 중 하나다 "
                             f"(evidence-ontology, 10.8절)")
        if not ref:
            raise SpaceError(f"{path}: {where} 의 증거에 ref 가 비어 있다 — 극성 {polarity} 의 증거는 실체를 가리켜야 한다 (9.11절)")
        out.append((kind, ref))
    return out


def parse_space(path: str) -> dict:
    """`-space` 청크 하나 → 방출에 필요한 값들. 형식 위반은 SpaceError 다."""
    meta, body = chunk2kg.parse_chunk(path)
    if meta["type"] != kb_lib.SPACE_TYPE:
        raise SpaceError(f"{path}: type 이 {kb_lib.SPACE_TYPE} 가 아니다 — 실제 {meta['type']!r} (설계 공간이 아닌 청크는 "
                         f"tools/chunk2kg.py 가 head 로 올린다)")
    data = body_block(path, kb_lib.chunk_body(Path(path).read_text(encoding="utf-8")))

    var = data.get("variable")
    if not isinstance(var, dict) or sorted(var) != ["from", "kind"] or not var["from"] or not var["kind"]:
        raise SpaceError(f"{path}: variable 은 {{from: <출발 항목 IRI>, kind: <링크 타입>}} 이어야 한다 — 실제 {var!r} "
                         f"(변수는 값이 아니라 출발 항목과 링크 타입의 쌍이다, p9-uncertainty-as-link-uncertainty)")
    kind = str(var["kind"])
    if kind not in chunk2kg.LINK_KEYS:
        raise SpaceError(f"{path}: variable.kind {kind!r} 가 링크 타입이 아니다 — {' | '.join(chunk2kg.LINK_KEYS)} 중 하나다 (8.2절)")
    status = str(data.get("status", ""))
    if status not in kb_lib.SPACE_STATUS:
        raise SpaceError(f"{path}: status 는 {' | '.join(kb_lib.SPACE_STATUS)} 중 하나다 — 실제 {status!r} (p9-candidate-storage)")

    candidates, seen = [], {}
    for item in data.get("candidates") or []:
        if not isinstance(item, dict) or not set(item) <= set(CANDIDATE_KEYS):
            raise SpaceError(f"{path}: 후보의 키는 {' · '.join(CANDIDATE_KEYS)} 다 — 실제 {item!r}")
        to, state = str(item.get("to", "")), str(item.get("state", ""))
        if not to:
            raise SpaceError(f"{path}: 후보에 to(대상 IRI)가 없다 — {item!r}")
        if state not in kb_lib.SPACE_STATES:
            raise SpaceError(f"{path}: 후보 {to} 의 state {state!r} 가 어휘 밖이다 — {' | '.join(kb_lib.SPACE_STATES)} 중 하나다")
        if to in seen:
            raise SpaceError(f"{path}: 후보 {to} 가 두 번 적혔다 — 한 후보는 한 줄이다")
        seen[to] = state
        support = evidence_of(path, f"후보 {to}", item["evidence"], "+") if item.get("evidence") else []
        elim = None
        if state == "eliminated":
            if not item.get("eliminated_by"):
                raise SpaceError(f"{path}: 후보 {to} 가 eliminated 인데 eliminated_by 가 없다 — 근거 없는 배제를 금지한다 "
                                 f"(요구 r-011-no-groundless-assignment)")
            elim = evidence_of(path, f"후보 {to} 의 배제", item["eliminated_by"], "-")[0]
        elif item.get("eliminated_by"):
            raise SpaceError(f"{path}: 후보 {to} 는 state 가 {state} 인데 eliminated_by 가 있다 — 배제 근거는 eliminated 에만 적는다")
        if state == "confirmed" and not any(k in kb_lib.SPACE_CONFIRMING_EVIDENCE for k, _ in support):
            raise SpaceError(f"{path}: 후보 {to} 가 confirmed 인데 지지 증거가 없다 — 구축 기록 또는 실행 결과"
                             f"({' | '.join(kb_lib.SPACE_CONFIRMING_EVIDENCE)}) 없이 확정할 수 없다 (9.11절, 요구 r-011-no-groundless-assignment)")
        candidates.append({"to": to, "state": state, "when": str(item.get("when", "")), "support": support, "elim": elim})

    prefs = []
    for item in data.get("preferences") or []:
        if not isinstance(item, dict) or sorted(item) != ["over", "prefer"]:
            raise SpaceError(f"{path}: preferences 항목은 {{prefer: <IRI>, over: <IRI>}} 여야 한다 — 실제 {item!r} (8.9절 부분순서)")
        a, b = str(item["prefer"]), str(item["over"])
        for iri in (a, b):
            if iri not in seen:
                raise SpaceError(f"{path}: preferences 가 후보가 아닌 {iri} 를 가리킨다 — 선호는 같은 공간의 두 후보 사이의 부분순서다")
        if a == b:
            raise SpaceError(f"{path}: preferences 의 prefer 와 over 가 같다 ({a}) — 선호는 비대칭 관계다")
        prefs.append((a, b))

    constraints = [str(c) for c in (data.get("constraints") or [])]
    if any(not c for c in constraints):
        raise SpaceError(f"{path}: 빈 양립 제약이 있다 — 제약이 없으면 constraints 를 적지 않는다 (STYLEGUIDE §0 빈 값)")
    return {"meta": meta, "body": body, "path": path, "var": (str(var["from"]), kind), "status": status,
            "candidates": candidates, "constraints": constraints, "preferences": prefs}


# ── 그래프 방출과 보고 ────────────────────

def emit(space: dict, enc) -> list[tuple[str, str]]:
    """설계 공간 하나 → (IRI, 블록) 목록 — 공간 개체 · 후보 링크 개체 · 증거 항목."""
    esc, meta = chunk2kg.esc, space["meta"]
    frm, kind = space["var"]
    out, candidate_iris = [], []
    for c in space["candidates"]:
        h = chunk2kg.link_hash(frm, kind, c["to"])
        link = f"{chunk2kg.ID_BASE}link/{h}"
        classes, state = kb_lib.SPACE_STATE_LINK[c["state"]]
        evidences = []
        for i, (ekind, ref) in enumerate(c["support"]):
            evidences.append((f"{chunk2kg.ID_BASE}evidence/{h}-space{i}", ekind, ref, "+"))
        if c["elim"]:
            evidences.append((f"{chunk2kg.ID_BASE}evidence/{h}-eliminated", c["elim"][0], c["elim"][1], "-"))
        stmts = [f"a {classes}", f"agt:linkFrom <{frm}>", f"agt:linkTo <{c['to']}>", f"agt:linkKind agt:{kind}",
                 f'agt:linkState "{state}"']
        if c["when"]:
            stmts.append(f'agt:when "{esc(c["when"])}"')
        if evidences:
            stmts.append("agt:hasEvidence " + " , ".join(f"<{e}>" for e, _, _, _ in evidences))
        out.append((link, render(link, stmts)))
        for iri, ekind, ref, pol in evidences:
            ev = [f"a agt:Evidence", f"agt:evidenceKind agt:{ekind}",
                  (f"agt:evidenceRef <{ref}>" if ref.startswith("http") else f'agt:evidenceRef "{esc(ref)}"'),
                  f'agt:polarity "{pol}"']
            out.append((iri, render(iri, ev)))
        candidate_iris.append((c["to"], link))

    by_to = dict(candidate_iris)
    for a, b in space["preferences"]:
        out.append((by_to[a] + "|pref", render(by_to[a], [f"agt:preferredOver <{by_to[b]}>"])))

    stmts = [f"a {kb_lib.SPACE_TYPE}",
             f'rdfs:label "{esc(meta["title"])}"@en', f'rdfs:label "{esc(meta["title_ko"])}"@ko',
             f"agt:hasLevel agt:{meta['level']}", f"agt:tokenCount {kb_lib.token_count(space['body'], enc)}",
             f'agt:status "{meta["status"]}"', f'agt:contentHash "{meta["_content_hash"]}"',
             f'agt:generatedBy "{esc(meta["generated"]["by"])}"',
             f'prov:generatedAtTime "{meta["generated"]["at"]}"^^xsd:dateTime',
             f'agt:assertionLocation "{esc(space["path"])}"']
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("sources", []):
        res = d.get("resource") if isinstance(d, dict) else d
        if not res:
            raise SpaceError(f"{space['path']}: sources 항목에 resource 가 없다 (OKF v0.2 §5.1)")
        stmts.append(f"prov:wasDerivedFrom <{res}>")
    stmts += [f'agt:spaceStatus "{space["status"]}"', f"agt:variableFrom <{frm}>", f"agt:variableKind agt:{kind}"]
    stmts += [f'agt:compatibilityConstraint "{esc(c)}"' for c in space["constraints"]]
    stmts += [f"agt:hasCandidate <{l}>" for _, l in candidate_iris]
    out.append((meta["id"], render(meta["id"], stmts)))
    return out


def render(iri: str, stmts: list) -> str:
    lines = [f"<{iri}>"]
    for i, s in enumerate(stmts):
        lines.append(f"    {s}{' .' if i == len(stmts) - 1 else ' ;'}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(design_space 규칙이 명시로 넘긴다)")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    enc = None
    if a.files:  # parse_chunk 를 실제로 부를 때만 값 어휘가 있어야 한다 — 아직 `-space` 청크가 없으면(빈 grap) 필요 없다
        try:
            chunk2kg.apply_plane_level_state(*chunk2kg.load_plane_level_state(a.residency))
        except (OSError, ValueError) as e:
            print(f"FAIL [{GATE}] {a.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        try:  # agt:Space 는 agt:Chunk 의 하위라 크기 사실(agt:tokenCount)을 갖는다 — 계수기는 고정된 어휘 하나다
            enc = kb_lib.load_tokenizer(a.vocab or None)
        except FileNotFoundError as e:
            print(f"FAIL [{GATE}] 어휘 파일 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except ValueError as e:
            print(f"FAIL [{GATE}] {e}", file=sys.stderr)
            return EXIT_FAIL

    blocks, errors, seen = [], [], {}
    for path in sorted(a.files):
        try:
            space = parse_space(path)
        except OSError as e:
            print(f"FAIL [{GATE}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except (SpaceError, ValueError) as e:
            errors.append(str(e))
            continue
        iri = space["meta"]["id"]
        if iri in seen:
            errors.append(f"{path}: IRI {iri} 가 {seen[iri]} 와 중복 — 변수 하나가 파일 하나다")
            continue
        seen[iri] = path
        blocks.append(space)
    variables: dict = {}  # (출발 항목, 링크 타입) → 파일 — 같은 변수를 두 파일이 선언하면 거부한다
    for space in blocks:
        if space["var"] in variables:
            errors.append(f"{space['path']}: 변수 {space['var'][0]} × agt:{space['var'][1]} 가 {variables[space['var']]} 에도 있다 — "
                          f"변수 하나가 파일 하나다 (p9-candidate-storage)")
            continue
        variables[space["var"]] = space["path"]
    if errors:
        for e in errors:
            print(f"FAIL [{GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL

    out: list = []
    for space in blocks:
        out += emit(space, enc)
    body = "\n\n".join(b for _, b in sorted(out))
    Path(a.out).write_text(PREAMBLE + ("\n" + body + "\n" if body else ""), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
