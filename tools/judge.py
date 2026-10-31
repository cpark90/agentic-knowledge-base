#!/usr/bin/env python3
"""판정자 — 등록된 판정 질문을 단위 지식에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-session-agreement —
질문 형·원자성·척도는 그 결정의 규칙 ⑤를 따르고, 임계는 확신도가 아니라 일치율이다 — 규칙 ③, Q-0056 Q119-a).

게이트 밖 도구다. `bazel test`는 판정을 부르지 않고 판정 로그의 형식·필수 필드만 본다(게이트 id `judge-log`).
판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다(유저 답 2026-09-30,
harness/channel/archive/legacy/handoff/judge-without-service-2026-09-30.md) — 외부 호출은 없고 응답은 `--responses`로 오프라인
입력된다. 질문·척도·임계의 원본은 프로파일 온톨로지와 shape다(`kb/ontology/profile/development/judge-*-ontology.ttl` ·
`kb/ontology/shapes/judge-question-shapes.ttl`) — 도구는 질문 문장을 상수로 갖지 않는다. 질문의 형은
noul·choice·score 셋이고 선택 집합은 255 이하다. 넘으면 독립 점수 → 명시 선택 2단계를 안내하고 거부한다.
확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(세션 판정자마다 하나) 주면
같은 (질문·입력 해시값)의 값 일치 여부를 계산해 로그의 `일치` 열에 낸다. 자동 적용은 정확도·판별력을 잰 뒤에만
켠다(`p8-judge-session-agreement` 규칙 ④) — 지금은 전부 사람 확인 큐다. `--record` 는 로그를 쓰기 전에 shape
(`kb_lib.JUDGE_LOG_SHAPES` — 판정자 둘의 답 · 일치 여부 열 · 미끼 검출 결과 · 단독 응답의 자동 적용 금지)로 검사하고
위반이 있으면 쓰지 않는다.
`--decoys <json>`(`label_sample.py --judge-sheet`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의
라벨+본문(`kb_lib.label_fingerprint`)으로 응답을 대조하고 미끼 검출률을 보고 요약에 낸다 — **대조 해시값은 항상
판정자에게 보인 라벨+본문**이지 단위 지식 파일 바이트가 아니다(2026-09-30 결함 보고, 파일 해시값으로 대조하면 세션
판정자의 응답이 전부 안 잡힌다). 파일 바이트 해시값은 로그의 `입력 해시값` 열에 그대로 남는다 — 추적용이지 대조 키가
아니다.
**쌍 모드** `--pairs <key.json>`(`label_sample.py --pair-sheet` 가 낸 정답 key — task 0262, Q-0061 Q145-a)는 링크 후보 쌍을 판정한다.
행은 쌍 하나이고 `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>`(kb_lib.pair_target)다. 응답은 쌍의 대조 해시값
(`kb_lib.pair_fingerprint`)으로 찾고 일치는 (쌍, 입력 해시값)으로 묶는다. 질문은 쌍마다 key 에 적힌 noul 질문(`overlapsHolds`·
`proposedLinkHolds`)이고 질문마다 판정 로그를 따로 낸다. `입력 해시값` 은 sha256(앵커 파일 바이트 ∥ 대상 파일 바이트)이다. 판정지를
만든 뒤 두 파일 중 하나의 라벨이나 본문이 바뀐 쌍은 낡은 판정이라 행을 내지 않는다. 미끼(음성 — 근거 없는 쌍, 양성 — 확정된 겹침)는
로그와 증거에 넣지 않고 검출률만 남긴다 — 음성 미끼에 no, 양성 미끼에 yes 가 검출이다. 결과 주석은 쌍마다 하나이고(판정자들의 값·확신도·
일치를 한 주석에) 파일 이름에 쌍 해시값 앞 8자를 싣고 `targets:` 에 두 IRI 를 적는다.
사용: bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>]
      [--record] [--into <디렉토리>] <단위 지식 파일…>
      bazel run //tools:judge -- --pairs <key.json> --responses <json> --responses <json> [--record] [--into <디렉토리>]
      python3 tools/judge.py --question labelRepresentsBody --responses r1.json --responses r2.json --decoys key.json
출력·종료: 보고는 stdout(`--out`으로 파일)이고 `--record`는 판정 로그(`kb/vv/run/judge-<UTC>.md`)와 결과
주석(`kb/vv/verdict/<슬러그>.md`)을 append-only로 쓴다. 질문 없음·형 밖·선택 집합 255 초과·응답 없음·읽을 수 없는
입력은 `FAIL [judge] …` + EXIT_CONFIG. 판정 대상(단위 지식·미끼)이 0건이면 EXIT_SKIP이다.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행
try:  # noqa: E402 — 대상의 IRI·수준은 frontmatter 파서가 읽는다. 값 어휘의 원본은 defs/kb.bzl 이다 (M1 단일 정의 위치)
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402
try:  # noqa: E402 — 본문 추출은 label_sample.py 하나가 원본이다(단일 정의 위치, 2026-09-30 vnv 결함 보고)
    from tools.label_sample import body_of as sample_body_of
except ImportError:
    from label_sample import body_of as sample_body_of  # noqa: E402

AGT = kb_lib.AGT
ID = kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
TAG = kb_lib.JUDGE_TAG
GENERATOR = kb_lib.JUDGE_GENERATOR
PROFILE_DIR = kb_lib.JUDGE_PROFILE_DIR
SHAPES = kb_lib.JUDGE_QUESTION_SHAPES
ODD_IRI = str(ID["odd-agentic-knowledge-base"])
ASSUMPTIONS = [str(ID[a]) for a in kb_lib.JUDGE_ASSUMPTIONS]  # 단위 지식 규약 — 판정 서비스 가정은 도입이 되돌려져 없다 (2026-09-30)
# 로그 한 파일의 상한은 **토큰**이고 단일 정의 위치는 `kb_lib.BODY_TOKEN_LIMITS` 다 (결정 p1-chunk-unit-is-tokens).
# 판정 행 수로 자르지 않는다 — 행의 길이가 질문·판정자·값에 따라 달라 행 수는 크기를 뜻하지 않는다. `split_rows`
# 가 묶음을 실제로 렌더해 재고, 그래서 새로 쓰는 로그는 게이트(`chunk`)를 통과한다.
_SLUG = re.compile(r"[^a-z0-9]+")


class JudgeError(Exception):
    """입력·설정 문제 — 메시지가 곧 수정 안내다 (EXIT_CONFIG)."""


def at(root: Path, p: str) -> Path:
    """상대 경로를 워크스페이스 루트 기준으로 푼다 — `bazel run` 의 작업 디렉토리는 runfiles 트리다."""
    path = Path(p)
    return path if path.is_absolute() else root / path


def slug(s: str) -> str:
    """판정자 식별자 → 파일명 조각. 세션 식별자에 `/`·공백이 섞여도 append-only 파일명이 갈리지 않는다."""
    return _SLUG.sub("-", s.lower()).strip("-") or "judge"


# ── 프로파일에서 질문·척도·임계를 읽는다 (도구는 상수를 갖지 않는다) ────────────────────────────────────────
# 원본은 kb_lib(judge_load_profile·judge_questions) 하나다(2026-09-30 vnv 결함 보고 ⑥) — label_sample.py 의
# `--judge-sheet` 가 같은 척도 문장을 그대로 옮기려면 두 도구가 같은 질의를 쓴다. 여기서는 얇게 감싸 JudgeError로만 바꾼다.

def load_profile(root: Path, profile: str, shapes: str) -> Graph:
    """프로파일 온톨로지 모듈과 판정 질문 shape 를 한 그래프로 읽는다."""
    try:
        return kb_lib.judge_load_profile(root, profile, shapes)
    except ValueError as e:
        raise JudgeError(str(e))


def questions(g: Graph) -> dict:
    """등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}."""
    return kb_lib.judge_questions(g)


def route() -> str:
    """판정 행의 처리. 자동 적용은 정확도·판별력을 잰 뒤에만 켜고 단독 응답에는 붙지 않는다 (규칙 ③·④) — 그 측정이
    아직 없으므로 지금은 전부 사람 확인 큐다. 확신도는 자기 보고라 처리를 가르지 않는다 (규칙 ②, Q-0056 Q119-a)."""
    return kb_lib.JUDGE_QUEUE


def check_question(q: dict, name: str) -> None:
    """형이 셋 안이고 선택 집합이 상한 안인가 — 아니면 수정 방향과 함께 거부한다 (규칙 ③)."""
    if q["form"] not in kb_lib.JUDGE_FORMS:
        raise JudgeError(f"질문 {name}: 형 {q['form']!r} 이 {' · '.join(kb_lib.JUDGE_FORMS)} 밖이다 — 자유 서술은 판정이 아니다")
    if q["form"] == "choice" and len(q["options"]) > kb_lib.JUDGE_CHOICE_MAX:
        raise JudgeError(f"질문 {name}: 선택 집합 {len(q['options'])} 개가 상한 {kb_lib.JUDGE_CHOICE_MAX} 를 넘는다 — "
                         f"질문을 2단계로 나눈다: 후보마다 독립 점수(score)를 묻고 상위 {kb_lib.JUDGE_CHOICE_MAX} 이하로 좁힌 뒤 "
                         "명시 선택(choice)을 묻는다 (p8-judge-session-agreement 규칙 ⑤)")


# ── 세션 판정자의 오프라인 응답 (--responses, 승격된 --fixture) ─────────────────────────────────────────────

def load_responses(path: Path) -> dict:
    """세션 판정자의 응답 집합 — {judge: <역할/모델 또는 세션 식별자>, responses: [{question, fingerprint, value, confidence}]}.

    `judge` 가 빠져 있으면 미확정으로 둔다 — 그 값이 판정 로그의 `판정자 식별자` 열에 그대로 실려 게이트
    `judge-log`가 빈 값 표기로 거부한다. 판정자 식별자 없는 판정을 조용히 통과시키지 않는 장치다.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise JudgeError(f"{path}: 응답을 읽을 수 없다 — {e}")
    if not isinstance(data, dict) or not isinstance(data.get("responses"), list):
        raise JudgeError(f"{path}: 응답 집합은 `responses` 목록을 가진 객체다 — {{judge, responses: [...]}}")
    data.setdefault("judge", kb_lib.EMPTY_UNDECIDED)
    return data


def normalize(payload: dict, default_judge: str) -> dict:
    """응답 항목 → {value, confidence, judge}. 키 이름은 `value`·`confidence`·`judge`이고 옛 이름(`decision`·
    `probability`·`model`)도 받는다 — 세션 판정자가 기록 형식을 조금씩 다르게 낼 수 있어서다."""
    value = payload.get("value", payload.get("decision"))
    conf = payload.get("confidence", payload.get("probability"))
    if value is None or conf is None:
        raise JudgeError(f"응답에 값 또는 확신도가 없다 — 받은 키 {sorted(payload)}. 필요한 것은 `value`·`confidence` 다")
    judge_id = str(payload.get("judge", payload.get("model", default_judge)))
    return {"value": str(value), "confidence": float(conf), "judge": judge_id}


def take_response(data: dict, used: set, q: dict, name: str, fp: str) -> dict:
    """응답 집합에서 이 (질문, 대조 해시값)의 응답 하나를 꺼낸다 — 해시값을 적지 않은 응답은 순서로 소비한다.

    `fp`는 **대조 해시값**(`kb_lib.label_fingerprint`)이다 — 세션 판정자가 실제로 본 라벨+본문의 sha256이지,
    단위 지식 파일 바이트의 sha256(로그의 `입력 해시값` 열)이 아니다. 파일 해시값으로 대조하면 판정자의 응답이
    전부 안 잡힌다(2026-09-30 vnv 결함 보고 ①).
    """
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (name, q["iri"]):
            continue
        if r.get("fingerprint") and r["fingerprint"] != fp:
            continue
        used.add(i)
        return normalize(r, str(data.get("judge", kb_lib.EMPTY_UNDECIDED)))
    raise JudgeError(f"응답 집합(판정자 {data.get('judge')})에 질문 {name} · 입력 해시값 {fp[:12]}… 의 응답이 없다 — "
                     "`responses` 에 항목을 더한다")


# ── 판정 ────────────────────────────────────────────────────────────────────────────────────────────────

def judge_rows(root: Path, paths: list[str], q: dict, name: str, resp_sets: list[dict],
              sheet: dict[str, dict] | None = None) -> list[dict]:
    """단위 지식 × 응답 집합마다 판정 행을 만든다.

    해시값은 **둘**이다(2026-09-30 vnv 결함 보고 ①) — 로그의 `입력 해시값` 열에 실리는 **기록 해시값**(단위 지식 파일
    바이트의 sha256, 추적·재현의 열쇠)과, 응답을 찾는 **대조 해시값**(`kb_lib.label_fingerprint`, 판정자에게
    실제로 보인 라벨+본문의 sha256)이다. 세션 판정자는 파일을 읽지 않고 `label_sample.py --judge-sheet`가 보인
    것만 보므로 대조는 그 해시값으로 해야 한다 — 파일 바이트 해시값으로 대조하면 응답이 전부 안 잡힌다(측정 결함).
    `sheet`(선택)는 `--decoys`의 key.json 전체(실표본+미끼)를 경로로 색인한 것이다 — 있으면 그 항목의
    라벨·본문(판정자에게 보인 그대로)으로 대조 해시값을 내고, 없으면 단위 지식을 다시 읽어(label_sample.body_of와
    같은 추출) 낸다. 상대 경로는 워크스페이스 루트 기준으로 푼다 — `bazel run`의 작업 디렉토리는 runfiles
    트리라 그대로는 닿지 못한다.
    """
    sheet = sheet or {}
    rows = []
    now = kb_lib.utc_stamp(datetime.now(timezone.utc))
    for data in resp_sets:
        used: set = set()
        for p in paths:
            path = at(root, p)
            posix = Path(p).as_posix()
            try:
                raw = path.read_bytes()
                meta, _ = parse_chunk(str(path))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{p}: 단위 지식으로 읽을 수 없다 — {e}")
            record_fp = hashlib.sha256(raw).hexdigest()
            shown = sheet.get(posix) or sheet.get(p)
            item = shown if shown else {"title_ko": meta.get("title_ko", ""), "title": meta.get("title", ""),
                                        "body": sample_body_of(str(path))}
            match_fp = kb_lib.label_fingerprint(item)
            answer = take_response(data, used, q, name, match_fp)
            rows.append({"path": posix, "iri": meta["id"], "level": meta["level"],
                         "verdict_stem": f"{path.parent.name}-{path.stem}",
                         "label": meta.get("title_ko", ""), "fingerprint": record_fp, "at": now,
                         "route": route(), **answer})
    return rows


def agreement(rows: list[dict]) -> None:
    """행마다 `일치` 열을 채운다 — 같은 (대상, 입력 해시값)에 둘 이상의 판정자 응답이 있을 때만 일치·불일치, 단독이면
    해당 없음이다(규칙: 확신도는 자기 보고이므로 단독 응답으로는 자동 적용이 없다)."""
    groups = defaultdict(list)
    for r in rows:
        groups[(r["iri"], r["fingerprint"])].append(r)
    for grp in groups.values():
        if len(grp) < 2:
            tag = kb_lib.JUDGE_AGREEMENT[2]
        else:
            tag = kb_lib.JUDGE_AGREEMENT[0] if len({g["value"] for g in grp}) == 1 else kb_lib.JUDGE_AGREEMENT[1]
        for g in grp:
            g["agree"] = tag


def counts(rows: list[dict]) -> dict:
    return {r: sum(1 for x in rows if x["route"] == r) for r in kb_lib.JUDGE_ROUTES}


# ── 미끼 검출률 (label_sample.py --decoys, 라벨 대표성 실험 전용) ───────────────────────────────────────────

def _leading_int(scale_situation: str) -> int:
    m = re.match(r"\s*(-?\d+)", scale_situation)
    return int(m.group(1)) if m else 0


def decoy_detection_rate(items: list[dict], q: dict, resp_sets: list[dict]) -> tuple[int, int]:
    """미끼 검출률의 (검출 수, 응답 있는 미끼 수).

    검출 = **"척도의 최고값(적합)이 아니다"**다(orchestrator 결정, 2026-09-30 vnv 결함 보고 ③) — 판별력의 뜻이
    "미끼를 적합으로 통과시키지 않는가"이기 때문이다. 이전 판(최저 척도값과 같아야 검출)은 "부분"으로 답한
    판별도 놓쳤다. 척도의 상황 문장 자체는 그대로다 — 척도는 상황으로 적는다(질문 온톨로지, p8-judge-session-agreement 규칙 ⑤).
    score 형만 잰다 — noul·choice 는 질문마다 "적합"의 뜻이 달라 일반화하지 않는다(9.3절 판별력)."""
    if q["form"] != "score" or not q["scale"]:
        return 0, 0
    full_fit = str(_leading_int(max(q["scale"], key=_leading_int)))
    hit = seen = 0
    for it in items:
        fp = kb_lib.label_fingerprint(it)
        for data in resp_sets:
            for r in data.get("responses", []):
                if r.get("fingerprint") == fp:
                    seen += 1
                    if str(r.get("value")) != full_fit:
                        hit += 1
    return hit, seen


def decoy_summary(hit: int, seen: int, total: int) -> str:
    """판정 로그의 미끼 검출 결과 줄의 값 (agt:decoyResult) — 미끼가 없으면 해당 없음과 그 사유다."""
    if not total:
        return f"{kb_lib.EMPTY_NOT_APPLICABLE} — `--decoys` 를 주지 않았다"
    return f"미끼 {total}건 중 응답 대조 {seen}건 · 검출 {hit}건 · 검출률 {kb_lib.pct(hit, seen)}"


# ── 판정 로그 (`memory` 지식 종류, append-only) 와 결과 주석 (`annotation` 지식 종류, 주석 형식) ─────────────────────

def log_frontmatter(rows: list[dict], q: dict, name: str, stamp: str) -> list[str]:
    """판정 로그의 frontmatter — 라벨이 묶음의 요약이다. uuid 는 파일마다 새로 난다."""
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    ko = f"판정 {stamp}: 질문 {q['label']} · 판정 {len(rows)} · 판정자 {len(judges)} · 사람 확인 큐 {n[kb_lib.JUDGE_QUEUE]}"
    en = f"Judgement {stamp}: question {name}, {len(rows)} judged by {len(judges)} judge(s), {n[kb_lib.JUDGE_QUEUE]} queued"
    return ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]


def log_body(rows: list[dict], q: dict, name: str, decoy: str, source: str, stamp: str) -> list[str]:
    """판정 로그의 **본문 줄들** — 표의 열이 곧 필수 필드다 (게이트 id judge-log).

    frontmatter 를 빼고 내는 까닭은 크기 상한의 대상이 본문이기 때문이다 — `split_rows` 가 이 결과를 재서
    묶음을 가른다 (p1-chunk-unit-is-tokens).
    """
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
    unit = f"링크 후보 쌍 {len({r['iri'] for r in rows})}개의 판정" if rows and rows[0].get("pair") else "단위 지식"
    body = [f"**관측** — {stamp} 에 `judge` 가 질문 `agt:{name}`({q['form']} 형)을 {unit} {len(rows)}건(판정자 "
            f"{' · '.join(f'`{j}`' for j in judges)})에 물었다. 응답은 {source} 다. 임계는 판정자 둘의 값 일치와 미끼 검출이다 "
            "(p8-judge-session-agreement 규칙 ③).", "",
            kb_lib.JUDGE_LOG_TABLE_HEADER, "|" + "---|" * len(kb_lib.JUDGE_LOG_TABLE_HEADER.split("|")[1:-1])]
    for r in rows:
        body.append(f"| `agt:{name}` | `{r['iri']}` | `{r['value']}` | {kb_lib.num(r['confidence'])} | "
                    f"`{r['judge']}` | `{r['fingerprint']}` | {r['at']} | {r['route']} | {r.get('agree', kb_lib.JUDGE_AGREEMENT[2])} |")
    body += ["", "판정 요약 — " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES) +
             f". 일치 {agree_n} · 불일치 {disagree_n}건(단독 응답은 `{kb_lib.JUDGE_AGREEMENT[2]}`) — 일치율 "
             f"{kb_lib.pct(agree_n, agree_n + disagree_n)}. 확신도는 자기 보고라 개별 답의 정확성을 보증하지 않는다. "
             "자동 적용은 정확도·판별력을 잰 뒤에만 켠다(p8-judge-session-agreement 규칙 ④) — 지금은 전부 사람 확인 큐다.",
             "", kb_lib.JUDGE_LOG_DECOY + decoy]
    return body


def log_chunk(rows: list[dict], q: dict, name: str, decoy: str, source: str, stamp: str) -> str:
    """판정 로그 단위 지식 하나 — frontmatter + 본문."""
    return "\n".join(log_frontmatter(rows, q, name, stamp) + log_body(rows, q, name, decoy, source, stamp)) + "\n"


def split_rows(rows: list[dict], q: dict, name: str, decoy: str, source: str, stamp: str, enc) -> list[list[dict]]:
    """판정 행을 로그 파일마다의 묶음으로 나눈다 — 한 묶음의 본문이 `memory` 상한 안이다.

    묶음을 실제로 렌더해 재는 까닭은 상한의 대상이 본문 전체이고 관측 문장·표 머리·요약도 그 안에 들기
    때문이다. 행 하나가 혼자서도 상한을 넘으면 그 행만으로 한 묶음을 만든다 — 자를 자리가 없으면 자르지 않고
    게이트가 그것을 잡는다 (조용히 버리지 않는다).
    """
    limit = kb_lib.body_token_limit("memory")
    parts: list[list[dict]] = []
    cur: list[dict] = []
    for r in rows:
        cand = cur + [r]
        over = kb_lib.token_count("\n".join(log_body(cand, q, name, decoy, source, stamp)), enc) > limit
        if over and cur:
            parts.append(cur)
            cur = [r]
        else:
            cur = cand
    if cur:
        parts.append(cur)
    return parts


def verdict_chunk(row: dict, q: dict, name: str, stamp: str) -> str:
    """결과 주석 본문 — 주석 형식 (p7-commentary-form). `본문:` 은 판정자가 쓰지 않는다 (규칙 ④)."""
    # 라벨은 질문 라벨에 대상(`verdict_stem`)과 판정자 id 를 더해 같은 질문의 결과 주석끼리 겹치지 않게 한다.
    tail = f"{row['verdict_stem']} · 판정자 {row['judge']}"
    ko = (f"판정 결과 — {q['label']}: 대상 {tail} · 값 {row['value']} · 확신도 {kb_lib.num(row['confidence'])}")
    en = (f"Judgement result — {q['label_en']}: target {row['verdict_stem']}, judge {row['judge']}, "
          f"value {row['value']}, confidence {kb_lib.num(row['confidence'])}")
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: annotation", f"level: {row['level']}",
            f"title_ko: {ko}", f"title: {en}", "status: draft", f"sources: [{{resource: {ODD_IRI}}}]",
            f"assumes: [{', '.join(ASSUMPTIONS)}]", f"targets: [{row['iri']}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    body = [f"thought (non-blocking): 질문 `agt:{name}` 의 값은 `{row['value']}` 이고 확신도는 "
            f"{kb_lib.num(row['confidence'])} 이며 판정자는 `{row['judge']}` 다.", "",
            f"대상: {row['iri']}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{row['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-session-agreement 규칙 ⑤). 입력 해시값은 "
            f"`{row['fingerprint'][:12]}…` 이고 일치는 `{row.get('agree', kb_lib.JUDGE_AGREEMENT[2])}` 다. 전체는 판정 로그에 있다."]
    return "\n".join(head + body) + "\n"


def verdict_pair_chunk(grp: list[dict], q: dict, name: str, stamp: str) -> str:
    """쌍 판정의 결과 주석 하나 — 판정자들의 값·확신도와 일치를 한 주석에 담는다. 주석 형식이고 `본문:` 은 판정자가 쓰지 않는다."""
    first = grp[0]
    a, b, kind = kb_lib.parse_pair_target(first["iri"])
    vals = " · ".join(f"{r['judge']} {r['value']} {kb_lib.num(r['confidence'])}" for r in grp)
    vals_en = ", ".join(f"{slug(r['judge'])} {r['value']} {kb_lib.num(r['confidence'])}" for r in grp)
    agree = first.get("agree", kb_lib.JUDGE_AGREEMENT[2])
    en_agree = {kb_lib.JUDGE_AGREEMENT[0]: "agreed", kb_lib.JUDGE_AGREEMENT[1]: "split"}.get(agree, "single")
    ko = f"판정 결과 — {q['label']}: 쌍 {first['pair_fp'][:8]} · {kind} · {vals} · {agree}"
    en = f"Judgement result — {q['label_en']}: pair {first['pair_fp'][:8]}, {kind}, {vals_en}, {en_agree}"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: annotation", f"level: {first['level']}",
            f"title_ko: {ko}", f"title: {en}", "status: draft", f"sources: [{{resource: {ODD_IRI}}}]",
            f"assumes: [{', '.join(ASSUMPTIONS)}]", f"targets: [{a}, {b}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    said = ", ".join(f"`{r['judge']}` 는 `{r['value']}`(확신도 {kb_lib.num(r['confidence'])})" for r in grp)
    body = [f"thought (non-blocking): 질문 `agt:{name}` 에 {said}를 냈고 일치는 `{agree}` 다. 링크 종류는 `{kind}` 다.", "",
            f"대상: {a} ↔ {b}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{first['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-session-agreement 규칙 ⑤). 입력 해시값은 "
            f"`{first['fingerprint'][:12]}…` 이고 전체는 판정 로그에 있다. 판정은 후보를 확정하지 않는다."]
    return "\n".join(head + body) + "\n"


# ── 쌍 모드 (--pairs, label_sample.py --pair-sheet 의 key.json) ─────────────────────────────────────────────

def load_pairs(path: Path) -> list[dict]:
    """쌍 판정지의 정답 key — [{n, question, kind, fingerprint, decoy, anchor:{path,id,title_ko,title,body}, target:{…}}]."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise JudgeError(f"{path}: 쌍 key 를 읽을 수 없다 — {e}")
    if not isinstance(data, list) or not all(isinstance(p, dict) and {"anchor", "target", "fingerprint", "question", "kind"} <= set(p)
                                             for p in data):
        raise JudgeError(f"{path}: 쌍 key 는 label_sample.py --pair-sheet 가 낸 목록이다 — 항목마다 anchor·target·fingerprint·question·kind")
    for p in data:
        fp = kb_lib.pair_fingerprint(p["question"], p["kind"], p["anchor"], p["target"])
        if fp != p["fingerprint"]:
            raise JudgeError(f"{path}: 쌍 {p.get('n')} 의 해시값이 그 내용과 다르다 — key 가 손으로 고쳐졌다. 판정지를 다시 만든다")
    return data


def pair_answer(data: dict, used: set, question: str, fp: str) -> dict | None:
    """응답 집합에서 이 (질문, 쌍 해시값)의 응답 하나 — 쌍 모드는 해시값 없는 응답을 순서로 소비하지 않는다. 없으면 None 이다."""
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (question, f"agt:{question}", str(AGT[question])) or r.get("fingerprint") != fp:
            continue
        used.add(i)
        ans = normalize(r, str(data.get("judge", kb_lib.EMPTY_UNDECIDED)))
        ans["value"] = ans["value"].strip().lower()
        if ans["value"] not in kb_lib.JUDGE_NOUL_POLARITY:
            raise JudgeError(f"판정자 {data.get('judge')} · 쌍 {fp[:12]}…: noul 값은 "
                             f"{' · '.join(kb_lib.JUDGE_NOUL_POLARITY)} 가운데 하나다 — 실제 {ans['value']!r}")
        return ans
    return None


def pair_rows(root: Path, pairs: list[dict], qs: dict, resp_sets: list[dict]) -> tuple[list[dict], dict]:
    """쌍 × 응답 집합마다 판정 행 — (행들, 집계 {응답 없음, 낡음, 미끼별 (검출, 응답, 전체)}). 미끼는 행을 내지 않는다."""
    now = kb_lib.utc_stamp(datetime.now(timezone.utc))
    rows, tally = [], {"missing": 0, "stale": 0, "neg": [0, 0, 0], "pos": [0, 0, 0]}
    current: dict = {}
    for p in pairs:
        if p["question"] not in qs or qs[p["question"]]["form"] != "noul":
            raise JudgeError(f"쌍 {p.get('n')}: 질문 {p['question']!r} 이 프로파일의 noul 질문이 아니다")
        if p.get("decoy") in ("neg", "pos"):
            tally[p["decoy"]][2] += 1
            continue
        side = []
        for end in ("anchor", "target"):
            path = at(root, p[end]["path"])
            try:
                meta, _ = parse_chunk(str(path))
                side.append((path.read_bytes(), meta, sample_body_of(str(path))))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{p[end]['path']}: 단위 지식으로 읽을 수 없다 — {e}")
        current[p["fingerprint"]] = all(
            (m.get("title_ko", ""), m.get("title", ""), body) == (p[end]["title_ko"], p[end]["title"], p[end]["body"])
            for (_, m, body), end in zip(side, ("anchor", "target")))
        p["_record"] = kb_lib.pair_record_fingerprint(side[0][0], side[1][0])
        p["_level"] = side[0][1]["level"]
    for data in resp_sets:
        used: set = set()
        for p in pairs:
            ans = pair_answer(data, used, p["question"], p["fingerprint"])
            if p.get("decoy") in ("neg", "pos"):
                if ans:
                    t = tally[p["decoy"]]
                    t[1] += 1
                    t[0] += ans["value"] == ("no" if p["decoy"] == "neg" else "yes")
                continue
            if ans is None:
                tally["missing"] += 1
                continue
            if not current[p["fingerprint"]]:
                tally["stale"] += 1   # 판정지를 만든 뒤 라벨·본문이 바뀌었다 — 판정자가 본 것과 지금 파일이 다르다
                continue
            rows.append({"pair": True, "question": p["question"], "pair_fp": p["fingerprint"],
                         "path": f"{p['anchor']['path']} ↔ {p['target']['path']}",
                         "iri": kb_lib.pair_target(p["anchor"]["id"], p["target"]["id"], p["kind"]), "level": p["_level"],
                         "label": f"{p['anchor']['title_ko']} ↔ {p['target']['title_ko']}", "fingerprint": p["_record"],
                         "at": now, "route": route(), **ans})
    return rows, tally


def pair_decoy_summary(tally: dict) -> str:
    """쌍 모드 판정 로그의 미끼 검출 결과 줄의 값 — 음성 미끼에 no, 양성 미끼에 yes 가 검출이다."""
    (nh, ns, nt), (ph, ps, pt) = tally["neg"], tally["pos"]
    if not (nt or pt):
        return f"{kb_lib.EMPTY_NOT_APPLICABLE} — 쌍 판정지에 미끼가 없다(`--decoys-neg 0 --decoys-pos 0`)"
    return (f"음성 미끼 {nt}건 중 응답 대조 {ns}건 · 검출(no) {nh}건 · 검출률 {kb_lib.pct(nh, ns)} · "
            f"양성 미끼 {pt}건 중 응답 대조 {ps}건 · 검출(yes) {ph}건 · 검출률 {kb_lib.pct(ph, ps)}")


def log_texts(rows: list[dict], q: dict, name: str, decoy: str, source: str, stamp: str, enc, shapes: Path) -> tuple[list, list]:
    """판정 로그의 묶음과 글 — 일치율 shape 를 어기는 글이 하나라도 있으면 JudgeError 다 (Q-0056 Q119-a). 쓰기 전에 부른다."""
    chunks = split_rows(rows, q, name, decoy, source, stamp, enc)  # 묶음의 상한은 토큰이다 (p1-chunk-unit-is-tokens)
    texts = [log_chunk(part, q, name, decoy, source, stamp) for part in chunks]
    for text in texts:
        bad = kb_lib.judge_log_violations(text, shapes)
        if bad:
            raise JudgeError(f"판정 로그가 {shapes.name} 를 어긴다 — " + " · ".join(bad))
    return chunks, texts


def write_records(root: Path, rows: list[dict], q: dict, name: str, decoy: str, source: str, now: datetime,
                  enc, shapes: Path, first: int = 0) -> list[Path]:
    """판정 로그와 결과 주석을 쓴다 — 이미 있는 파일을 덮지 않는다 (append-only, r-026). 쓰기 전에 로그 글을 일치율
    shape(`shapes`)로 검사하고 위반이 있으면 아무 것도 쓰지 않는다 (Q-0056 Q119-a).

    결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>`(`verdict_stem`)을 쓴다(2026-09-30 vnv 결함 보고 ②) —
    결정 기록은 파일 stem이 전부 `conclusion`·`rationale`·`alternatives`뿐이라 파일명이 그대로 부딪힌다
    (측정: 실표본 60 중 50건이 그 충돌로 로그에 못 들어갔다). 부모 디렉토리 이름(결정 슬러그)을 더하면 유일하다.
    """
    stamp = kb_lib.utc_stamp(now)
    log_dir, verdict_dir = root / kb_lib.JUDGE_LOG_DIR, root / kb_lib.JUDGE_VERDICT_DIR
    chunks, texts = log_texts(rows, q, name, decoy, source, stamp, enc, shapes)  # 위반이 하나라도 있으면 아무 것도 쓰지 않는다
    log_dir.mkdir(parents=True, exist_ok=True)
    verdict_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for i, part in enumerate(chunks, start=first):   # `first` — 한 실행이 질문 여럿의 로그를 쓸 때 파일 번호를 잇는다(쌍 모드)
        suffix = "" if i == 0 else f"-{i + 1}"
        target = log_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{now.strftime('%Y%m%dT%H%M%SZ')}{suffix}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 판정 로그는 append-only 다 (r-026)")
        target.write_text(texts[i - first], encoding="utf-8")
        written.append(target)
    if rows and rows[0].get("pair"):   # 쌍 모드 — 결과 주석은 쌍마다 하나다
        groups: dict = defaultdict(list)
        for r in rows:
            groups[r["iri"]].append(r)
        for grp in groups.values():
            target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-pair-{grp[0]['pair_fp'][:8]}.md"
            if target.exists():
                raise JudgeError(f"{target}: 이미 있다 — 같은 질문·쌍의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
            target.write_text(verdict_pair_chunk(grp, q, name, stamp), encoding="utf-8")
            written.append(target)
        return written
    for r in rows:
        target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-{r['verdict_stem']}-{slug(r['judge'])}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 같은 질문·판정자의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
        target.write_text(verdict_chunk(r, q, name, stamp), encoding="utf-8")
        written.append(target)
    return written


# ── 보고 ────────────────────────────────────────────────────────────────────────────────────────────────

def report(rows: list[dict], q: dict, name: str, source: str, now: datetime,
          decoy_hit: int, decoy_seen: int, decoy_total: int, pair_decoy: str = "") -> str:
    n = counts(rows)
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
    inputs = sorted({r["path"] for r in rows})
    rep = kb_lib.gendoc_header(
        "judge", "판정자 판정 결과", "tools/judge.py",
        f"등록된 판정 질문 `agt:{name}` 을 세션 판정자의 오프라인 응답으로 단위 지식에 물어 값과 확신도를 받고 일치·미끼 "
        "검출을 요약한다 — 게이트 밖이고 게이트는 판정 로그의 형식만 본다 (8.14절)",
        ("bazel run //tools:judge -- --pairs <key.json> --responses <json> --responses <json>" if pair_decoy else
         f"bazel run //tools:judge -- --question {name} --responses <json> <단위 지식 파일…>"), inputs,
        f"단위 지식 {len(rows)} · 질문 1({q['form']} 형) · 판정자 {len({r['judge'] for r in rows})}",
        kb_lib.gendoc_view_notice("세션 판정자의 응답과 프로파일의 질문·임계"), input_kind="판정 대상",
        extra=[f"- 응답: {source}",
               "- 임계: 판정자 둘의 값 일치와 미끼 검출 — 확신도는 자기 보고라 처리를 가르지 않는다 (p8-judge-session-agreement)",
               "- 처리: " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES),
               f"- 일치: 일치 {agree_n} · 불일치 {disagree_n} · 일치율 {kb_lib.pct(agree_n, agree_n + disagree_n)}(단독 응답 제외)",
               (f"- 미끼 검출: {pair_decoy}" if pair_decoy else
                f"- 미끼 검출률: {kb_lib.pct(decoy_hit, decoy_seen)}(응답 있는 미끼 {decoy_seen} / 전체 미끼 {decoy_total})"
                if decoy_total else "- 미끼 검출률: 해당 없음(--decoys 없음)")])
    body = ["## 판정 — 확신도는 자기 보고이고 개별 답을 보증하지 않는다", "",
            "| 대상 | 라벨 | 값 | 확신도 | 판정자 | 처리 | 일치 | 입력 해시값 |", "|---|---|---|---|---|---|---|---|"]
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
    body += ["", "## 미끼 검출 (쌍 판정지, `--pairs`)" if pair_decoy else "## 미끼 검출 (라벨 대표성 실험, `--decoys`)", "",
             f"- {pair_decoy}" if pair_decoy else
             f"- 미끼 {decoy_total}건 중 응답 대조 {decoy_seen}건 · 검출 {decoy_hit}건 · 검출률 {kb_lib.pct(decoy_hit, decoy_seen)}"
             if decoy_total else "- 없음(`--decoys` 를 주지 않았다)", "",
             f"판정자는 설명을 만들지 못하므로 결과 주석의 `본문:` 은 `{kb_lib.EMPTY_NOT_APPLICABLE}` 이고 "
             "사람 또는 System 2 에이전트가 채운다."]
    return kb_lib.gendoc_assemble(rep, body, inputs, input_kind="판정 대상")


def record_args(a, root: Path):
    """`--record` 의 공통 입력 — (기록의 뿌리, 계수기, 일치율 shape 경로)."""
    try:  # 로그를 가르는 상한이 토큰이므로 계수기가 기록의 입력이다 (ODD id:cond-tokenizer-lock)
        enc = kb_lib.load_tokenizer(a.vocab or None)
    except (FileNotFoundError, ValueError) as e:
        raise JudgeError(f"어휘 파일 — {e}") from e
    return (at(root, a.into) if a.into else root), enc, root / kb_lib.JUDGE_LOG_SHAPES


def pairs_main(a, root: Path, qs: dict) -> int:
    """쌍 모드 — key 의 쌍마다 판정자 응답을 찾아 질문별로 보고하고, `--record` 면 질문마다 판정 로그와 쌍마다 결과 주석을 쓴다."""
    pairs = load_pairs(at(root, a.pairs))
    if a.question:
        name = a.question.rsplit("/", 1)[-1].removeprefix("agt:")
        pairs = [p for p in pairs if p["question"] == name]
    if not pairs:
        print(f"SKIP [{TAG}] 판정 대상 쌍 0건 — PASS 가 아니다")
        return EXIT_SKIP
    if not a.responses:
        raise JudgeError("`--responses <json>` 이 없다 — 외부 서비스가 없으므로 세션 판정자의 응답을 오프라인으로 받는다")
    resp_sets = [load_responses(at(root, p)) for p in a.responses]
    rows, tally = pair_rows(root, pairs, qs, resp_sets)
    decoy = pair_decoy_summary(tally)
    source = "세션 판정자 응답 " + " · ".join(f"`{Path(p).name}`(판정자 `{d.get('judge')}`)" for p, d in zip(a.responses, resp_sets))
    now = datetime.now(timezone.utc)
    by_q: dict = defaultdict(list)
    for r in rows:
        by_q[r["question"]].append(r)
    texts = []
    for name in sorted(by_q):
        by_q[name].sort(key=lambda r: (r["iri"], r["judge"]))  # 한 쌍의 판정자 행을 붙여 둔다 — 로그를 토큰 상한으로 갈라도 묶음마다 판정자 둘이 있다
        agreement(by_q[name])
        texts.append(report(by_q[name], qs[name], name, source, now, 0, 0, 0, pair_decoy=decoy))
    print(f"[{TAG}] 쌍 {len({p['fingerprint'] for p in pairs if not p.get('decoy')})} · 판정 행 {len(rows)} · 응답 없음 {tally['missing']} · "
          f"낡은 판정 {tally['stale']} · 미끼 — {decoy}")
    for text in texts:
        print(text)
    if a.out:
        at(root, a.out).write_text("\n".join(texts), encoding="utf-8")
    if a.record:
        if not rows:
            raise JudgeError("기록할 판정 행이 없다 — 미끼만으로는 판정 로그를 남기지 않는다")
        into, enc, shapes = record_args(a, root)
        stamp = kb_lib.utc_stamp(now)
        counts_q = {name: len(log_texts(by_q[name], qs[name], name, decoy, source, stamp, enc, shapes)[1]) for name in sorted(by_q)}
        written, first = [], 0   # 모든 질문의 로그가 shape 를 지킨 뒤에만 쓴다 — 한 질문만 쓰이고 멈추지 않는다
        for name in sorted(by_q):
            written += write_records(into, by_q[name], qs[name], name, decoy, source, now, enc, shapes, first)
            first += counts_q[name]
        print("기록: " + " · ".join(p.as_posix() for p in written) +
              " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    return EXIT_OK


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--question", default="", help="질문 id — 프로파일의 `agt:` 지역명 또는 전체 IRI (`--list` 에는 필요 없다)")
    ap.add_argument("--responses", action="append", default=[], metavar="JSON",
                    help="세션 판정자의 응답 — {judge, responses: [{question, fingerprint, value, confidence}]}. "
                         "판정자마다 한 번씩 반복한다 — 둘 이상이면 일치를 계산한다 (옛 --fixture 의 승격)")
    ap.add_argument("--decoys", default="", metavar="JSON",
                    help="label_sample.py --decoys 가 낸 key.json — 미끼 항목의 검출률을 보고 요약에 낸다(라벨 대표성 실험 전용)")
    ap.add_argument("--pairs", default="", metavar="JSON",
                    help="label_sample.py --pair-sheet 가 낸 key.json — 링크 후보 쌍을 판정한다(쌍 모드). 질문은 쌍마다 key 에 있다")
    ap.add_argument("--record", action="store_true",
                    help=f"판정 로그({kb_lib.JUDGE_LOG_DIR}/judge-<UTC>.md)와 결과 주석({kb_lib.JUDGE_VERDICT_DIR}/)을 쓴다")
    ap.add_argument("--into", default="", metavar="DIR", help="기록의 뿌리 — 기본은 워크스페이스다. 시험물을 밖에 두는 수단이다")
    ap.add_argument("--out", default="", metavar="FILE", help="보고를 파일로도 쓴다")
    ap.add_argument("--profile", default=PROFILE_DIR, help="질문·척도·임계의 원본 디렉토리")
    ap.add_argument("--list", action="store_true", help="등록된 질문만 나열하고 멈춘다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 판정 로그를 `memory` 상한 안으로 가르는 데 쓴다. "
                                               "없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("chunks", nargs="*", help="판정 대상 단위 지식 파일 — 라벨 대표성 실험(`--decoys`)만 쓰면 생략할 수 있다")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))

    try:
        try:
            apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
        except (OSError, ValueError) as e:
            raise JudgeError(f"{a.residency or root / 'defs/kb.bzl'}: 값 어휘의 원본을 읽을 수 없다 — {e}")
        g = load_profile(root, a.profile, SHAPES)
        qs = questions(g)
        if a.list:
            for k, q in sorted(qs.items()):
                print(f"agt:{k} ({q['form']}) — {q['label']}")
            return EXIT_OK
        if a.pairs:
            return pairs_main(a, root, qs)
        if not a.question:
            raise JudgeError("`--question <질문 id>` 가 없다 — 등록된 질문은 `--list` 가 낸다")
        name = a.question.rsplit("/", 1)[-1].removeprefix("agt:")
        if name not in qs:
            raise JudgeError(f"질문 {a.question!r} 이 프로파일에 없다 — 등록된 것은 "
                             + " · ".join(f"`agt:{k}`" for k in sorted(qs)) + f". 새 질문은 {a.profile} 에 파일로 더한다")
        q = qs[name]
        check_question(q, name)

        decoys_raw = None
        if a.decoys:
            try:
                decoys_raw = json.loads(at(root, a.decoys).read_text(encoding="utf-8"))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{a.decoys}: 미끼 목록을 읽을 수 없다 — {e}")
            if not isinstance(decoys_raw, list):
                raise JudgeError(f"{a.decoys}: label_sample.py 의 key.json 은 목록이다")
        decoy_items = [it for it in decoys_raw if isinstance(it, dict) and it.get("decoy")] if decoys_raw else []
        # 대조 해시값의 원본 — key.json 은 실표본·미끼를 다 담으므로 실표본 해시값도 여기서 스스로 대조한다
        # (2026-09-30 vnv 결함 보고 ①). 경로가 곧 색인 키다 — label_sample.py 가 낸 path 그대로다
        sheet_index = {it["path"]: it for it in (decoys_raw or []) if isinstance(it, dict) and it.get("path")}

        if not a.chunks and not decoy_items:
            print(f"SKIP [{TAG}] 판정 대상 0건 — PASS 가 아니다")
            return EXIT_SKIP
        if not a.responses:
            raise JudgeError("`--responses <json>` 이 없다 — 외부 서비스가 없으므로 세션 판정자의 응답을 오프라인으로 받는다")
        resp_sets = [load_responses(at(root, p)) for p in a.responses]

        now = datetime.now(timezone.utc)
        rows = judge_rows(root, a.chunks, q, name, resp_sets, sheet=sheet_index) if a.chunks else []
        if rows:
            agreement(rows)
        decoy_hit, decoy_seen = decoy_detection_rate(decoy_items, q, resp_sets) if decoy_items else (0, 0)
        # 응답 파일의 이름만 적는다(basename) — 절대 경로는 판정 로그에 실리지 않는다(2026-09-30 vnv 결함 보고 ⑤)
        source = "세션 판정자 응답 " + " · ".join(f"`{Path(p).name}`(판정자 `{d.get('judge')}`)"
                                               for p, d in zip(a.responses, resp_sets))
        text = report(rows, q, name, source, now, decoy_hit, decoy_seen, len(decoy_items))
        decoy = decoy_summary(decoy_hit, decoy_seen, len(decoy_items))
        print(text)
        if a.out:
            at(root, a.out).write_text(text, encoding="utf-8")
        if a.record:
            if not rows:
                raise JudgeError("기록할 판정 행이 없다 — `--decoys` 만으로는 판정 로그를 남기지 않는다(단위 지식 대상이 없다)")
            into, enc, shapes = record_args(a, root)
            written = write_records(into, rows, q, name, decoy, source, now, enc, shapes)
            print("기록: " + " · ".join(p.as_posix() for p in written) +
                  " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    except JudgeError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
