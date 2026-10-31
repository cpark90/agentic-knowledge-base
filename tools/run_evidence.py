#!/usr/bin/env python3
"""실행·동시 편집·공동 커버 → 링크의 증거 기록 (p9-evidence-ledger-with-belief 결론 "실행 증거가 특별하다", p10-link-types `satisfies`,
p10-co-edit-evidence-from-small-commits, p10-link-judgement-evidence).

검증기의 통과는 `verifies` 뿐 아니라 그것이 검증하는 `satisfies` 후보에도 실행(+)을, 실패는 실행(−)을 적는다 — V&V 결과가
개발 KB 후보의 증거로 흘러드는 유일한 경로이고 링크가 아니라 **증거 기록 항목**이라 방향 규칙(8.5절)을 깨지 않는다.
이 도구가 그 경로의 생성기다. 손으로 쓰는 링크가 아니라 생성물이며 출력은 `//kg:references_kg` 에 이어 붙는다.

후보의 양 끝은 개발 KB 의 코드 **파일 단위 지식**(파일 복합체의 선언 단위 지식, p7-code-links-on-file-composite)와 **결정 결론**이다.
`satisfies` 증거의 원천은 둘이다.

  도장  파일 단위 지식의 `verified` 에 `process:bazel-test`(kb_lib.STAMP_ACTOR)가 있으면 — 추출기가 `tested.source_hash` 가 지금
        소스와 같을 때만 내므로 살아 있는 도장이다 — 그 단위 지식이 `refines` 하는 결정 결론마다 실행(+) 한 줄. 참조는 그 파일 단위 지식이다
        (도장의 시각 `agt:verifiedAt` 이 거기 있다). 도장은 통과 뒤에만 찍히므로 도장에서 (−)는 나오지 않는다.
  실행  V&V 실행 기록(`kb/vv/run/`, generated.by `process:vv_run`)의 테스트 케이스 표 한 행마다 — 그 테스트 케이스가 `verifies` 하는 결정 결론 D 와,
        그 테스트 케이스를 돌린 검증기(같은 합격 기준을 `refines` 하는 검증기, kb_lib.case_verifiers)가 `verifies` 하는 개발 KB 파일 단위 지식
        A 의 쌍 (A, D) 에 pass 는 실행(+), fail 은 실행(−) 한 줄. 참조는 실행 기록·테스트 케이스·검증기 셋이다. skip 은 증거가 아니다
        (SKIP 은 PASS 가 아니다). 건너뛴 명령이 있는데 pass 로 적힌 행도 (+)로 읽지 않는다 — 절반만 실행한 통과다.
        **이 사슬은 generated.at 이 `CHAIN_SINCE` 이후인 실행 기록부터 적용한다** (유저 답 Q96-a). 그 앞의 실행 기록 5건은 테스트 케이스가
        검증기를 직접 가리키던 옛 구조의 기록이고 소급하지 않는다 — 실행 기록은 추가 전용이다(p0-run-is-an-append-only-memory-chunk).
        **verify 질의(구조 안티패턴 게이트)의 실패는 증거로 쓰지 않는다** — 그 질의는 위반 행의 어느 링크가 틀렸는지 정하지 못한다.

링크의 증거 둘을 더 붙인다. 둘 다 지지(+)이고 이미 확정된 링크(frontmatter)에만 붙인다 — 후보는 링크 후보 뷰(tools/link.py)가 낸다.

  동시 편집  동시 편집 관측(kb_lib.coedit_pairs — 바뀐 단위 지식 파일이 kb_lib.COEDIT_MAX_FILES 이하인 커밋의 쌍)의 두 항목을 잇는
             확정 링크에 `agt:coEditHistory`. 참조는 그 관측이다. git 은 읽지 않는다 — 관측은 `--coedit-record` 모드가 쓴다.
  공동 커버  kb_lib.co_cover 의 (검증기 W, 파일 단위 지식 A) 가 확정 링크 `verifies` W→A 이면 그 링크에 `agt:testCoverage`. 참조는 테스트 케이스들이다.

판정 증거 하나를 더 붙인다 (task 0262, Q-0061 Q145-a, p8-judge-session-agreement).

  판정  판정 로그(`kb/vv/run/judge-*.md`, generated.by `process:judge`)의 쌍 행(`대상` 이 `<앵커> ↔ <대상> · <종류>`, kb_lib.parse_pair_target)
        마다 `agt:judgement` 증거 하나 — 참조는 그 판정 로그, 극성은 값 yes 가 +, no 가 − 다(kb_lib.JUDGE_NOUL_POLARITY). 후보 링크 개체
        (`linkKind` 는 판정한 종류, `linkState "candidate"`)를 함께 낸다. 그 쌍이 이미 확정(frontmatter)이면 내지 않는다 — 판정은 사람 확인 큐를
        거르는 증거이고 확정은 사람이 판정을 본 뒤의 행위다. 확정 링크에 (−) 판정을 붙이면 verify 질의 `confirmed-with-refutation` 이 사람의
        확정을 거부한다. **판정 증거는 반박만 있어도 `invalid` 로 만들지 않는다** —
        아래 `invalid` 규칙은 실행 증거 전용이다(p9-evidence-ledger-with-belief). 행의 `입력 해시값` 이 지금 두 파일의 sha256(앵커 바이트 ∥ 대상 바이트,
        kb_lib.pair_record_fingerprint)과 다르면 낡은 판정이라 증거를 내지 않는다. 단일 항목 판정 행은 링크의 증거가 아니다.

믿음 정도를 후보 링크 곁에 싣는다 (task 0304, 요구 r-032, 설계 공간 degree-of-belief-space, Q166-a).

  믿음 정도  이 도구가 후보로 낸 링크(satisfies 후보와 판정 후보)마다 열린 계산 규칙 A·B·C 의 값을 agt:DegreeOfBelief 노드
             (값 · 계산 규칙 · 입력 증거 수, belief-ontology)로 낸다. 입력은 그 링크의 실행 증거와 판정 증거이고 낡은 판정은 들지 않는다.
             A 는 서열 가중을 극성대로 더해 [0,1]로 접은 점수, B 는 Beta(1, 1) 에 지지·반박 수를 더한 사후 평균과 분산, C 는 판정 확신도의
             평균(보정 전)이다. 값은 상태를 바꾸지 않는다 — 상태를 정하는 함수는 값을 계산하는 함수를 부르지 않고, 게이트 belief-consistency
             가 그것을 본다(Q90-a). 확정 링크와 invalid 링크에는 값을 싣지 않는다.

상태는 p9-evidence-ledger-with-belief 의 전이 규칙 그대로다. 실행(−)만 있으면 `invalid`(배제, 클래스 없음 — space2kg 와 같은 표현), (+)가
하나라도 있으면 `candidate`(agt:CandidateLink) — (+)와 (−)가 공존해도 자동 해소하지 않고 후보로 남긴다(충돌 = open + 유저 큐).
확정 제안은 내지 않는다 — 확정은 사람이 frontmatter `satisfies:` 에 적는 행위다. 그 쌍이 이미 확정이면 상태·클래스를 쓰지 않고
증거 항목만 그 링크에 붙인다(확정 링크도 증거 기록을 유지한다). 직접 트리플 `agt:satisfies` 는 내지 않는다 — 후보는 주장이 아니다.
링크 IRI 는 chunk2kg 와 같은 규칙(양 끝 뿌리 uuid 의 link_hash)이다.

출력·종료: 읽을 수 없는 입력은 `FAIL [run-evidence] <경로>: …` + EXIT_CONFIG. 실행 기록이 가리키는 테스트 케이스가 없으면 stderr 에
`info [run-evidence]` 로 세고 건너뛴다 — 실행 기록은 append-only 라 지난 테스트 케이스 이름이 남는다.
사용: run_evidence.py --out <생성.ttl> --residency defs/kb.bzl <단위 지식 파일들...>   (.md 만 읽는다)
      bazel run //tools:run_evidence -- --coedit-record   (git 에서 동시 편집 쌍을 뽑아 kb/dev/memory/obs-coedit-<UTC>.md 하나를 쓴다)
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.chunk2kg import (ID_BASE, LINK_KEYS, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                                body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)
except ImportError:
    import kb_lib
    from chunk2kg import (ID_BASE, LINK_KEYS, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                          body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)

KIND = "satisfies"                           # p10-link-types — artifact → decision 의 수평 링크
EVIDENCE_KIND = "agt:runResult"              # evidence-ontology — 검증기·판정 도구의 통과(+) 또는 실패(−)
CONCLUSION_SLOT = "결론"                      # 결정 결론의 본문 표지 (STYLEGUIDE §4)
CASE_DIR = kb_lib.KB_VV + "/case"            # 테스트 케이스의 자리 — vv_run.CASE_DIR 와 같은 값
VERIFIER_DIR = kb_lib.KB_VV + "/verifier"    # 검증기의 자리 — vv_run.VERIFIER_DIR 와 같은 값
# 실행 사슬의 적용 경계 — generated.at 이 이 시각 이후인 실행 기록만 읽는다. 값은 유저 답 Q96-a 가 전달된 시각(answer 0216)이고, 그 앞의 5건은 소급하지 않는다
CHAIN_SINCE = "2026-10-23T17:33:01Z"
POLARITY = {"pass": "+", "fail": "-"}        # 테스트 케이스 판정 → 극성. skip 은 증거가 아니다
_SKIPPED = re.compile(r"(\d+)\s*건너뜀")
_SLUG = re.compile(r"^`([^`]+)`$")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 실행 기록(kb/vv/run/)·테스트 케이스·검증기와 코드 파일 단위 지식의 도장이다.
# 생성: tools/run_evidence.py (bazel build //kg:references_kg) — satisfies 후보와 실행 증거 (p9-evidence-ledger-with-belief),
# 확정 링크의 동시 편집·공동 커버 증거 (p10-co-edit-evidence-from-small-commits · p10-link-judgement-evidence),
# 판정 로그의 쌍 행 → 판정 증거와 후보 링크 (p8-judge-session-agreement) — 판정은 반박만 있어도 invalid 가 아니고 낡은 판정은 내지 않는다
# 실행 사슬(테스트 케이스 verifies 결정 × 같은 합격 기준의 검증기 verifies 코드)은 generated.at ≥ {since} 인 실행 기록에만 적용한다 — 그 앞은 소급하지 않는다.
# verify 질의의 실패는 증거로 쓰지 않는다. 동시 편집은 관측 {coedit} 만 읽고 git 을 읽지 않는다
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


# ── 실행 기록의 테스트 케이스 표 읽기 ────────────────────

def as_list(v) -> list:
    return v if isinstance(v, list) else []


def run_rows(body: str, at=None) -> list[tuple[str, str, int]]:
    """실행 기록 본문의 테스트 케이스 표 → [(테스트 케이스 슬러그, 판정, 건너뛴 명령 수)]. 헤더의 단일 정의 위치는 kb_lib.RUN_CASE_TABLE_HEADER.

    표 머리는 기록 시각 `at`(frontmatter `generated.at`)으로 가린다 — kb_lib.RECORD_HEADER_SINCE 이전 기록은 `RUN_CASE_TABLE_HEADER_OLD` 만,
    이후 기록과 시각을 읽지 못한 기록은 새 머리만 받는다 (Q161-a)."""
    header = kb_lib.RUN_CASE_TABLE_HEADER_OLD if kb_lib.record_header_old(at) else kb_lib.RUN_CASE_TABLE_HEADER
    rows, inside = [], False
    for ln in body.splitlines():
        s = ln.strip()
        if not inside:
            inside = s == header
            continue
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.strip("|").split("|")]
        m = _SLUG.match(cells[0]) if cells else None
        if len(cells) < 3 or not m or cells[2] not in kb_lib.RUN_VERDICTS:
            continue
        skipped = _SKIPPED.search(cells[1])
        rows.append((m.group(1), cells[2], int(skipped.group(1)) if skipped else 0))
    return rows


def after_chain_since(at) -> bool:
    """실행 기록의 generated.at 이 `CHAIN_SINCE` 이후인가 — 시각을 읽지 못하면 옛 기록으로 본다."""
    try:
        when = datetime.fromisoformat(str(at).replace("Z", "+00:00"))
    except ValueError:
        return False
    when = when if when.tzinfo else when.replace(tzinfo=timezone.utc)
    return when >= datetime.fromisoformat(CHAIN_SINCE.replace("Z", "+00:00"))


# ── 동시 편집 관측의 기록 (`bazel run` 모드 — git 은 밀폐 빌드 밖이다) ────────────────────

def coedit_record(root: Path) -> int:
    """git 이력에서 동시 편집 쌍을 뽑아 관측 하나(kb/dev/memory/obs-coedit-<UTC>.md)로 쓴다 (p10-co-edit-evidence-from-small-commits).

    커밋마다 바뀐 단위 지식 파일(kb_lib.COEDIT_ITEM_PATH)을 세고, 그 수가 kb_lib.COEDIT_MAX_FILES 이하인 커밋만 쓴다. 항목은 지금
    트리의 frontmatter `id` 로 풀고, 지금 없거나 `id` 가 없는 파일은 쌍에서 빼고 센다. 행마다 함께 바뀐 항목들의 모든 두 조합이 쌍이다 —
    쌍을 하나씩 적지 않고 커밋 묶음으로 적어 관측이 memory 의 토큰 상한 안에 든다. 이미 있는 파일은 덮지 않는다.
    """
    log = subprocess.run(["git", "log", "--no-renames", "--name-only", "--format=@@%h %cI"], cwd=root,
                         capture_output=True, text=True, check=True).stdout
    commits: list[tuple[str, str, list[str]]] = []
    for ln in log.splitlines():
        if ln.startswith("@@"):
            sha, at = ln[2:].split(" ", 1)
            commits.append((sha, at, []))
        elif ln.strip() and commits and kb_lib.COEDIT_ITEM_PATH.match(ln.strip()):
            commits[-1][2].append(ln.strip())
    id_line = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
    iri_of: dict[str, str] = {}
    for f in sorted(p.relative_to(root).as_posix() for d in ("kb", "space") if (root / d).is_dir() for p in (root / d).rglob("*.md")):
        text = (root / f).read_text(encoding="utf-8")
        head = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
        m = id_line.search(head)
        if kb_lib.COEDIT_ITEM_PATH.match(f) and m:
            iri_of[f] = m.group(1)
    short_n = Counter(kb_lib.coedit_short(i) for i in iri_of.values())
    form = {i: kb_lib.coedit_short(i) if short_n[kb_lib.coedit_short(i)] == 1 else i[len(ID_BASE):] for i in iri_of.values()}
    touched = [c for c in commits if c[2]]
    small = [c for c in touched if len(set(c[2])) <= kb_lib.COEDIT_MAX_FILES]
    rows, pairs, gone = [], set(), 0
    for sha, at, files in small:
        items = sorted({iri_of[f] for f in set(files) if f in iri_of}, key=lambda i: form[i])
        gone += len(set(files)) - sum(1 for f in set(files) if f in iri_of)
        here = {frozenset((a, b)) for k, a in enumerate(items) for b in items[k + 1:]}
        pairs |= here
        rows.append(f"| `{sha}` | {at} | {len(set(files))} | {len(here)} | " + (" · ".join(f"`{form[i]}`" for i in items) or kb_lib.NONE_MARK) + " |")
    stamp = kb_lib.utc_stamp(datetime.now(timezone.utc))
    span = f"`{commits[-1][0]}`..`{commits[0][0]}`" if commits else kb_lib.NONE_MARK
    out = root / kb_lib.DEV_MEMORY_DIR / f"{kb_lib.COEDIT_PREFIX}{stamp.replace('-', '').replace(':', '')}.md"
    if out.exists():
        print(f"FAIL [run-evidence] {out}: 이미 있다 — 관측은 추가 전용이다", file=sys.stderr)
        return kb_lib.EXIT_CONFIG
    head = ["---", f"id: {ID_BASE}chunk/{uuid.uuid4()}", "type: memory", "level: concrete",
            f"title_ko: 동시 편집 관측 {stamp}: 커밋 {len(small)} · 쌍 {len(pairs)}",
            f"title: Co-edit observation {stamp}: {len(small)} commits, {len(pairs)} pairs", "status: stable",
            f"sources: [{{resource: {ID_BASE}odd-agentic-knowledge-base}}]", f"assumes: [{ID_BASE}asm-chunk-conventions]",
            f"generated: {{by: {kb_lib.COEDIT_GENERATOR}, at: {stamp}}}", "---"]
    body = [f"**관측** — {stamp} 에 `run_evidence --coedit-record` 가 git 이력 {span}(커밋 {len(commits)}개)을 읽었다. 단위 지식 파일"
            f"(`kb/**/*.md` · `space/*.md` · `chunks/**/*.md`)을 바꾼 커밋은 {len(touched)}개다. 그 가운데 바뀐 단위 지식 파일이 "
            f"{kb_lib.COEDIT_MAX_FILES}개 이하인 커밋 {len(small)}개에서 쌍을 뽑았고, 쌍은 중복을 빼고 {len(pairs)}개다. "
            f"지금 트리에 없거나 `id` 가 없어 뺀 파일은 {gone}건이다.", "",
            "항목은 단위 지식 IRI 의 짧은 꼴이다. `chunk/` 뒤의 8자는 uuid 의 앞 8자이고, 짧은 꼴이 겹치는 항목은 `id/` 뒤의 이름 전체로 적었다. "
            "행마다 함께 바뀐 항목들의 모든 두 조합이 쌍이다.", "",
            kb_lib.COEDIT_TABLE_HEADER, "|---|---|---|---|---|"] + rows
    out.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    print(f"[run-evidence] {out.relative_to(root)} — 커밋 {len(small)}/{len(touched)} · 쌍 {len(pairs)} · 뺀 파일 {gone}", file=sys.stderr)
    return kb_lib.EXIT_OK


# ── 판정 증거 — 판정 로그의 쌍 행 (task 0262, p8-judge-session-agreement) ────────────────────

def judged_pairs(meta_of: dict, path_of: dict) -> tuple[dict, list[str], int, int]:
    """판정 로그의 쌍 행 → ((앵커, 종류, 대상) → [(판정 로그, 판정자, 극성, 확신도)], 판정 로그들, 낡은 판정 수, 끝이 없는 쌍 행 수).

    낡은 판정(입력 해시값이 지금 두 파일의 sha256 과 다름)과 끝이 없는 행은 세고 건너뛴다. 확신도는 판정 로그의 `확신도` 칸('예'의 확률)이고
    읽지 못하면 None 이다. 판정 증거(judgement_lines)와 믿음 정도(belief_lines)가 이 한 읽기를 쓴다."""
    judged: dict[tuple[str, str, str], list[tuple[str, str, str, float | None]]] = defaultdict(list)
    judge_logs = sorted(i for i, m in meta_of.items()
                        if f"{kb_lib.JUDGE_LOG_DIR}/" in path_of[i] and Path(path_of[i]).name.startswith(kb_lib.JUDGE_LOG_PREFIX)
                        and isinstance(m.get("generated"), dict) and m["generated"].get("by") == kb_lib.JUDGE_GENERATOR)
    stale = gone_pair = 0
    for log in judge_logs:
        for row in kb_lib.judge_log_rows(Path(path_of[log]).read_text(encoding="utf-8")):
            pair = kb_lib.parse_pair_target(row["대상"])
            pol = kb_lib.JUDGE_NOUL_POLARITY.get(row["값"])
            if pair is None or pol is None:
                continue
            a, b, kind = pair
            if a not in meta_of or b not in meta_of or kind not in LINK_KEYS:
                gone_pair += 1
                continue
            if kb_lib.pair_record_fingerprint(Path(path_of[a]).read_bytes(), Path(path_of[b]).read_bytes()) != row["입력 해시값"]:
                stale += 1
                continue
            conf = float(row["확신도"]) if kb_lib.JUDGE_CONFIDENCE.match(row.get("확신도", "")) else None
            judged[(a, kind, b)].append((log, row["판정자 식별자"], pol, conf))
    return judged, judge_logs, stale, gone_pair


def judgement_lines(meta_of: dict, path_of: dict, spec: dict, ledger: dict,
                    read: tuple[dict, list[str], int, int]) -> tuple[list[str] | None, str, dict, set]:
    """판정 쌍(judged_pairs 의 결과) → (TTL 줄들, 요약 한 줄, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).
    행마다 agt:judgement 증거 하나와, 확정이 아닌 쌍의 후보 링크 개체.

    이미 확정된 쌍은 내지 않고 센다. 판정은 반박만 있어도 후보다 — invalid 는 실행 증거 전용이다(p9-evidence-ledger-with-belief).
    링크 IRI 를 풀지 못하면 (None, 사유, {}, set()) 다."""
    judged, judge_logs, stale, gone_pair = read
    lines: list[str] = []
    inputs: dict[str, list[tuple[str, str, float | None]]] = {}
    emitted: set[str] = set()
    judge_states: Counter[str] = Counter()
    for (a, kind, b) in sorted(judged):
        try:
            h = link_hash(work_id(a, spec), kind, work_id(b, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return None, "", {}, set()
        link = f"{ID_BASE}link/{h}"
        evs = []
        for log, judge, pol, conf in judged[(a, kind, b)]:
            tag = hashlib.sha256(f"{log}\x1f{judge}".encode("utf-8")).hexdigest()[:12]
            evs.append((f"{ID_BASE}evidence/{h}-judge-{tag}", log, pol, conf))
        evs = sorted(set(evs), key=lambda x: x[:3])
        ev_list = " , ".join(f"<{e}>" for e, _, _, _ in evs)
        if b in as_list(meta_of[a].get(kind)):   # 이미 확정 — 판정은 큐를 거르는 증거라 확정 뒤에는 내지 않는다 (사람의 확정이 앞선다)
            judge_states["confirmed-skipped"] += 1
            continue
        if kind == KIND and (a, b) in ledger:   # 실행 증거가 이미 개체를 냈다 — 상태는 실행 증거의 규칙이 정한다
            judge_states["attached"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:   # 판정은 반박만 있어도 후보다 — invalid 는 실행 증거 전용 (p9-evidence-ledger-with-belief)
            judge_states[LINK_STATE_CANDIDATE] += 1
            emitted.add(link)
            lines.append(f"\n<{link}>\n    a agt:Link , agt:CandidateLink ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{b}> ;\n"
                         f"    agt:linkKind agt:{kind} ;\n    agt:linkState \"{LINK_STATE_CANDIDATE}\" ;\n    agt:hasEvidence {ev_list} .")
        inputs[link] = [("agt:judgement", pol, conf) for _, _, pol, conf in evs]
        for e, log, pol, _ in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind agt:judgement ;\n    agt:evidenceRef <{log}> ;\n"
                         f"    agt:polarity \"{pol}\" .")

    note = (f"[run-evidence] 판정 쌍 {len(judged)} (" + (" · ".join(f"{k} {v}" for k, v in sorted(judge_states.items())) or kb_lib.NONE_MARK)
            + f") · 판정 증거 {sum(len(v) for v in judged.values())} · 판정 로그 {len(judge_logs)} · 낡은 판정 {stale} · 끝이 없는 쌍 행 {gone_pair}")
    return lines, note, inputs, emitted


# ── 믿음 정도 — 열린 계산 규칙 A·B·C 의 병기 값 (task 0304, 요구 r-032, 설계 공간 degree-of-belief-space) ────────────────────
# 값은 후보 링크 곁에만 싣고 상태를 바꾸지 않는다(Q90-a). 상태를 정하는 함수(ledger_lines·judgement_lines)는 이 절을 부르지 않는다 —
# 게이트 belief-consistency(validate)가 코드 단위 지식에서 그것을 본다. 세 규칙 모두 열린 후보라 닫지 않는다(Q166-a).
BELIEF_RULES = {   # 계산 규칙 slug → 설계 공간 후보 결정의 결론 IRI
    "kind-rank": ID_BASE + "chunk/8b6a4563-17d3-4c5c-a9a1-ea46f0babdbc",      # A p9-belief-by-evidence-kind-rank
    "beta-binomial": ID_BASE + "chunk/2dc8dfc7-565d-48c6-9f76-6b81afcd6eea",  # B p9-belief-by-beta-binomial
    "judge-mean": ID_BASE + "chunk/88b97e4d-57de-4ec9-8824-5decb2f9184f",     # C p9-belief-by-calibrated-judge (보정 전, 보정은 S3)
}
# A 의 서열 — 구축, 실행, 동시 편집, 공동 커버, 판정, 임베딩, 세션 (p9-evidence-ledger-with-belief, Q118-a). 순위 i(0부터)의 가중은
# (7 − i) / 7 이다 — 가중표의 근거가 아직 없어 서열만 담는 등간격을 고른다. 유저 결정은 서열 밖의 확정 권한이라 가중이 없다
BELIEF_KIND_RANK = ("agt:constructionRecord", "agt:runResult", "agt:coEditHistory", "agt:testCoverage", "agt:judgement",
                    "agt:embeddingSimilarity", "agt:coRead")
BELIEF_KIND_WEIGHT = {k: (len(BELIEF_KIND_RANK) - i) / len(BELIEF_KIND_RANK) for i, k in enumerate(BELIEF_KIND_RANK)}
BELIEF_PRIOR = (1, 1)   # B 의 사전 Beta(α₀, β₀) — 종류마다 같은 균등 사전이다. 종류별로 달리 둘 표본이 아직 없다


def belief_of(entries: list[tuple[str, str, float | None]]) -> dict[str, tuple[float, int, float | None]]:
    """증거 항목들 [(종류, 극성, 확신도)] → 계산 규칙 slug → (값, 입력 증거 수, 사후 분산 또는 None). 입력이 없는 규칙은 값을 내지 않는다.

    A kind-rank      서열 가중 w 를 극성대로 더한 S = Σ ±w 를 W = Σ w 로 나누어 (1 + S / W) / 2 로 접는다. 판정은 서열의 한 종류다.
    B beta-binomial  지지 s · 반박 r (판정의 극성도 그대로 센다)을 사전 Beta(1, 1) 에 더한 사후의 평균 (1 + s) / (2 + s + r) 과 분산.
    C judge-mean     판정 증거의 확신도('예'의 확률) 평균. 보정하지 않은 값이다."""
    out: dict[str, tuple[float, int, float | None]] = {}
    ranked = [(BELIEF_KIND_WEIGHT[k], p) for k, p, _ in entries if k in BELIEF_KIND_WEIGHT]
    total = sum(w for w, _ in ranked)
    if total > 0:
        signed = sum(w if p == "+" else -w for w, p in ranked)
        out["kind-rank"] = ((1 + signed / total) / 2, len(ranked), None)
    s = sum(1 for _, p, _ in entries if p == "+")
    r = sum(1 for _, p, _ in entries if p == "-")
    a, b = BELIEF_PRIOR[0] + s, BELIEF_PRIOR[1] + r
    out["beta-binomial"] = (a / (a + b), s + r, a * b / ((a + b) ** 2 * (a + b + 1)))
    conf = [c for k, _, c in entries if k == "agt:judgement" and c is not None]
    if conf:
        out["judge-mean"] = (sum(conf) / len(conf), len(conf), None)
    return out


def belief_lines(inputs: dict[str, list[tuple[str, str, float | None]]]) -> tuple[list[str], Counter]:
    """후보 링크 → 증거 항목들 을 받아 계산 규칙마다 agt:DegreeOfBelief 노드 하나와 링크의 agt:hasDegreeOfBelief 를 낸다.
    노드 IRI 는 링크 IRI 의 `link/` 를 `belief/` 로 바꾸고 규칙 slug 를 붙인 것이다. 반환은 (TTL 줄들, 규칙 slug → 값을 실은 링크 수)."""
    lines: list[str] = []
    counts: Counter[str] = Counter()
    for link in sorted(inputs):
        for slug, (value, n, var) in sorted(belief_of(inputs[link]).items()):
            node = link.replace(f"{ID_BASE}link/", f"{ID_BASE}belief/", 1) + f"-{slug}"
            counts[slug] += 1
            tail = f" ;\n    agt:beliefVariance {var:.6f}" if var is not None else ""
            lines.append(f"\n<{link}>\n    agt:hasDegreeOfBelief <{node}> .")
            lines.append(f"\n<{node}>\n    a agt:DegreeOfBelief ;\n    agt:beliefValue {value:.4f} ;\n    agt:beliefRule <{BELIEF_RULES[slug]}> ;\n"
                         f"    agt:beliefEvidenceCount \"{n}\"^^xsd:nonNegativeInteger{tail} .")
    return lines, counts


# ── 후보와 증거 항목의 방출 ────────────────────

def ledger_lines(meta_of: dict, path_of: dict, spec: dict, ledger: dict) -> tuple[list[str] | None, Counter, dict, set]:
    """satisfies 증거 기록 (A, D) → [(증거 접미, 참조들, 극성)] → (TTL 줄들, 상태별 수, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).

    상태는 p9-evidence-ledger-with-belief 의 전이 규칙 그대로다 — (+)가 하나라도 있으면 후보, 실행(−)만 있으면 invalid, 이미 확정이면
    증거 항목만 붙인다. 증거 기록만 읽고 확률로 합산한 값을 읽지 않는다. 링크 IRI 를 풀지 못하면 (None, …) 다."""
    lines: list[str] = []
    states: Counter[str] = Counter()
    inputs: dict[str, list[tuple[str, str, float | None]]] = {}
    emitted: set[str] = set()
    for (a, d) in sorted(ledger):
        try:
            h = link_hash(work_id(a, spec), KIND, work_id(d, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return None, states, {}, set()
        link = f"{ID_BASE}link/{h}"
        entries = ledger[(a, d)]
        evs = [(f"{ID_BASE}evidence/{h}-{suffix}", refs, pol) for suffix, refs, pol in entries]
        ev_list = " , ".join(f"<{e}>" for e, _, _ in evs)
        pols = {p for _, _, p in entries}
        inputs[link] = [(EVIDENCE_KIND, pol, None) for _, _, pol in entries]
        if d in as_list(meta_of[a].get(KIND)):   # 이미 확정 — 증거 항목만 그 링크에 붙인다
            states["confirmed"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:
            cls, state = ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE) if "+" in pols else ("agt:Link", kb_lib.LINK_STATE_INVALID)
            states[state] += 1
            if state == LINK_STATE_CANDIDATE:
                emitted.add(link)
            lines.append(f"\n<{link}>\n    a {cls} ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{d}> ;\n"
                         f"    agt:linkKind agt:{KIND} ;\n    agt:linkState \"{state}\" ;\n    agt:hasEvidence {ev_list} .")
        for e, refs, pol in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {EVIDENCE_KIND} ;\n    agt:evidenceRef "
                         + " , ".join(f"<{x}>" for x in refs) + f" ;\n    agt:polarity \"{pol}\" .")
    return lines, states, inputs, emitted


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out")
    ap.add_argument("--residency", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("--coedit-record", action="store_true", help="git 에서 동시 편집 쌍을 뽑아 관측 하나를 쓴다 (bazel run 모드)")
    ap.add_argument("--root", default=os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), help="--coedit-record 의 저장소 뿌리")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.coedit_record:
        try:
            return coedit_record(Path(args.root).resolve())
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"FAIL [run-evidence] {args.root}: git 이력을 읽을 수 없다 — {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
    if not (args.out and args.residency):
        ap.error("--out 과 --residency 가 필요하다 (--coedit-record 가 아닐 때)")
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [run-evidence] {args.residency}: 값 어휘를 읽을 수 없다 — {e}", file=sys.stderr)
        return kb_lib.EXIT_CONFIG

    meta_of: dict[str, dict] = {}
    path_of: dict[str, str] = {}
    conclusion: set[str] = set()
    spec: dict[str, str] = {}
    for path in sorted(p for p in args.files if p.endswith(".md")):
        try:
            meta, body = parse_chunk(path)
        except (OSError, ValueError) as e:
            print(f"FAIL [run-evidence] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        iri = meta.get("id")
        if not isinstance(iri, str):
            continue
        meta["__body"] = body
        meta_of[iri], path_of[iri] = meta, path
        if isinstance(meta.get(SPECIALIZATION_KEY), str):
            spec[iri] = meta[SPECIALIZATION_KEY]
        if meta.get("type") == "decision" and CONCLUSION_SLOT in body_slots(body.splitlines()):
            conclusion.add(iri)

    def in_kb(iri: str, kb: str) -> bool:
        return f"{kb}/" in path_of.get(iri, "")

    def file_chunk(iri: str) -> bool:
        """개발 KB 의 artifact 단위 지식으로 복합체의 부분이 아닌 것 — 파일 단위 지식(선언 단위 지식)과 손으로 쓴 산출물."""
        m = meta_of.get(iri, {})
        return m.get("type") == "artifact" and in_kb(iri, kb_lib.KB_DEV) and not m.get("part_of")

    # (A, D) → [(증거 접미, 참조들, 극성)]
    ledger: dict[tuple[str, str], list[tuple[str, list[str], str]]] = defaultdict(list)

    # 도장 — 살아 있는 process:bazel-test 도장의 파일 단위 지식이 refines 하는 결정 결론
    for a in sorted(meta_of):
        m = meta_of[a]
        if not file_chunk(a) or not any(isinstance(v, dict) and v.get("by") == kb_lib.STAMP_ACTOR for v in as_list(m.get("verified"))):
            continue
        for d in as_list(m.get("refines")):
            if d in conclusion:
                ledger[(a, d)].append(("stamp", [a], "+"))

    # 실행 — 실행 기록의 테스트 케이스 행 × (테스트 케이스를 돌린 검증기가 verifies 하는 파일 단위 지식) × (테스트 케이스가 verifies 하는 결정 결론)
    def in_dir(iri: str, d: str) -> bool:
        return path_of[iri].startswith(d + "/") or f"/{d}/" in path_of[iri]

    case_of = {Path(path_of[i]).stem: i for i in meta_of if in_dir(i, CASE_DIR)}
    refines = {i: as_list(m.get("refines")) for i, m in meta_of.items()}
    verifiers = [i for i in meta_of if in_dir(i, VERIFIER_DIR)]
    runners = kb_lib.case_verifiers(refines, case_of.values(), verifiers)
    unknown: Counter[str] = Counter()
    halves = 0
    runs = sorted(i for i, m in meta_of.items()
                  if f"{kb_lib.VV_RUN_DIR}/" in path_of[i] and isinstance(m.get("generated"), dict)
                  and m["generated"].get("by") == kb_lib.RUN_GENERATOR)
    old_runs = [r for r in runs if not after_chain_since(meta_of[r]["generated"].get("at"))]
    for r in runs:
        if r in old_runs:
            continue
        stem = Path(path_of[r]).stem
        for slug, verdict, skipped in run_rows(meta_of[r]["__body"], meta_of[r]["generated"].get("at")):
            c = case_of.get(slug)
            if c is None:
                unknown[slug] += 1
                continue
            if verdict not in POLARITY:
                continue
            if verdict == "pass" and skipped:
                halves += 1
                continue
            for w in sorted(runners.get(c, ())):
                for a in (x for x in as_list(meta_of[w].get("verifies")) if file_chunk(x)):
                    for d in as_list(meta_of[c].get("verifies")):
                        if d in conclusion:
                            ledger[(a, d)].append((f"{stem}-{slug}", [r, c, w], POLARITY[verdict]))

    # 동시 편집·공동 커버 — 확정 링크(frontmatter)에만 붙는 지지 증거. 링크 IRI 는 chunk2kg 와 같은 (뿌리 uuid, 종류, 뿌리 uuid) 해시다
    obs_path, coedit, coedit_unresolved = kb_lib.coedit_pairs([path_of[i] for i in meta_of], set(meta_of))
    obs = next((i for i in meta_of if path_of[i] == obs_path), None)
    cover = kb_lib.co_cover(refines, {i: as_list(m.get("verifies")) for i, m in meta_of.items()}, case_of.values(), verifiers,
                            [i for i in meta_of if file_chunk(i)])
    extra: list[tuple[str, str, str, str, list[str]]] = []   # (링크 출발, 종류, 도착, 증거 종류, 참조들)
    for a in sorted(meta_of):
        for key in LINK_KEYS:
            for b in as_list(meta_of[a].get(key)):
                if obs and frozenset((a, b)) in coedit:
                    extra.append((a, key, b, "agt:coEditHistory", [obs]))
                if key == "verifies" and (a, b) in cover:
                    extra.append((a, key, b, "agt:testCoverage", sorted(cover[(a, b)])))

    lines = [PREAMBLE.format(since=CHAIN_SINCE, coedit=obs_path or kb_lib.NONE_MARK)]
    ledger_out, states, ledger_inputs, ledger_emitted = ledger_lines(meta_of, path_of, spec, ledger)
    if ledger_out is None:
        return kb_lib.EXIT_CONFIG
    lines += ledger_out

    extra_kinds: Counter[str] = Counter()
    for a, key, b, kind, refs in extra:
        try:
            h = link_hash(work_id(a, spec), key, work_id(b, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        suffix = "coedit" if kind == "agt:coEditHistory" else "cover"
        e = f"{ID_BASE}evidence/{h}-{suffix}"
        extra_kinds[kind] += 1
        lines.append(f"\n<{ID_BASE}link/{h}>\n    agt:hasEvidence <{e}> .")
        lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {kind} ;\n    agt:evidenceRef "
                     + " , ".join(f"<{x}>" for x in refs) + " ;\n    agt:polarity \"+\" .")

    judge_lines, judge_note, judge_inputs, judge_emitted = judgement_lines(meta_of, path_of, spec, ledger, judged_pairs(meta_of, path_of))
    if judge_lines is None:
        return kb_lib.EXIT_CONFIG
    lines += judge_lines
    # 믿음 정도 — 후보로 낸 링크만, 그 링크의 실행 증거와 판정 증거를 입력으로 (상태는 위에서 이미 정해졌고 이 값은 그것을 바꾸지 않는다)
    belief_out, belief_n = belief_lines({link: ledger_inputs.get(link, []) + judge_inputs.get(link, [])
                                         for link in ledger_emitted | judge_emitted})
    lines += belief_out
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    both = sum(1 for k in ledger if {p for _, _, p in ledger[k]} == {"+", "-"})
    print(f"[run-evidence] satisfies 쌍 {len(ledger)} (" + " · ".join(f"{k} {v}" for k, v in sorted(states.items())) +
          f") · 증거 항목 {sum(len(v) for v in ledger.values())} · (+)(−) 공존 {both} · 실행 기록 {len(runs)}"
          f"(사슬 적용 {len(runs) - len(old_runs)} · {CHAIN_SINCE} 앞이라 소급하지 않음 {len(old_runs)})", file=sys.stderr)
    print(f"[run-evidence] 확정 링크의 동시 편집 {extra_kinds['agt:coEditHistory']} · 공동 커버 {extra_kinds['agt:testCoverage']} "
          f"(관측 {obs_path or kb_lib.NONE_MARK} · 쌍 {len(coedit)} · 풀지 못한 항목 {coedit_unresolved})", file=sys.stderr)
    print(judge_note, file=sys.stderr)
    print(f"[run-evidence] 믿음 정도 — 후보 링크 {len(ledger_emitted | judge_emitted)} 곁에 " +
          (" · ".join(f"{slug} {belief_n[slug]}" for slug in sorted(BELIEF_RULES)) or kb_lib.NONE_MARK) +
          " (열린 계산 규칙 셋, 상태 전이에 들지 않는다)", file=sys.stderr)
    if halves:
        print(f"info [run-evidence] 건너뛴 명령이 있는 pass 행 {halves} — 증거로 읽지 않았다", file=sys.stderr)
    for slug, n in sorted(unknown.items()):
        print(f"info [run-evidence] 실행 기록의 테스트 케이스 `{slug}` 가 {CASE_DIR} 에 없다 — 행 {n}", file=sys.stderr)
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
