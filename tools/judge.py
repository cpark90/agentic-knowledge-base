#!/usr/bin/env python3
"""판정자 — 등록된 판정 질문을 청크에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-session-agreement —
질문 형·척도·임계 셋 자체는 옛 결정 p8-judge-calibration-binding·p8-judge-question-form 그대로다).

게이트 밖 도구다. `bazel test`는 판정을 부르지 않고 판정 로그의 형식·필수 필드만 본다(게이트 id `judge-log`).
판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다(유저 답 2026-09-30,
docs/feedback/handoff/judge-without-service-2026-09-30.md) — 외부 호출은 없고 응답은 `--responses`로 오프라인
입력된다. 질문·척도·임계의 원본은 프로파일 온톨로지와 shape다(`kb/ontology/profile/development/judge-*-ontology.ttl` ·
`kb/ontology/shapes/judge-question-shapes.ttl`) — 도구는 질문 문장도 임계도 상수로 갖지 않는다. 질문의 형은
noul·choice·score 셋이고 선택 집합은 255 이하다. 넘으면 독립 점수 → 명시 선택 2단계를 안내하고 거부한다.
확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(세션 판정자마다 하나) 주면
같은 (질문·입력 지문)의 값 일치 여부를 계산해 로그의 `일치` 열에 낸다. 일치율 임계와 자동 적용은 별도 결정
(`p8-judge-session-agreement`)이 3지표 중 정확도·판별력의 재측정 뒤에 정한다 — 지금은 전부 사람 확인 큐다.
`--decoys <json>`(`label_sample.py --judge-sheet`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의
라벨+본문(`kb_lib.label_fingerprint`)으로 응답을 대조하고 미끼 검출률을 보고 요약에 낸다 — **대조 지문은 항상
판정자에게 보인 라벨+본문**이지 청크 파일 바이트가 아니다(2026-09-30 결함 보고, 파일 지문으로 대조하면 세션
판정자의 응답이 전부 안 잡힌다). 파일 바이트 지문은 로그의 `입력 지문` 열에 그대로 남는다 — 추적용이지 대조 키가
아니다.
사용: bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>]
      [--record] [--into <디렉토리>] <청크 파일…>
      python3 tools/judge.py --question labelRepresentsBody --responses r1.json --responses r2.json --decoys key.json
출력·종료: 보고는 stdout(`--out`으로 파일)이고 `--record`는 판정 로그(`kb/vv/run/judge-<UTC>.md`)와 결과
주석(`kb/vv/verdict/<슬러그>.md`)을 append-only로 쓴다. 질문 없음·형 밖·선택 집합 255 초과·응답 없음·읽을 수 없는
입력은 `FAIL [judge] …` + EXIT_CONFIG. 판정 대상(청크·미끼)이 0건이면 EXIT_SKIP이다.
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
try:  # noqa: E402 — 대상의 IRI·수준은 frontmatter 파서가 읽는다. 값 어휘의 원본은 defs/kb.bzl 이다 (M1 단일 정의처)
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402
try:  # noqa: E402 — 본문 추출은 label_sample.py 하나가 원본이다(단일 정의처, 2026-09-30 vnv 결함 보고)
    from tools.label_sample import body_of as sample_body_of
except ImportError:
    from label_sample import body_of as sample_body_of  # noqa: E402

AGT = kb_lib.AGT
ID = kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
TAG = kb_lib.JUDGE_GATE
GENERATOR = kb_lib.JUDGE_GENERATOR
PROFILE_DIR = kb_lib.JUDGE_PROFILE_DIR
SHAPES = kb_lib.JUDGE_QUESTION_SHAPES
ODD_IRI = str(ID["odd-agentic-knowledge-base"])
ASSUMPTIONS = [str(ID[a]) for a in kb_lib.JUDGE_ASSUMPTIONS]  # 청크 규약 — 판정 서비스 가정은 도입이 되돌려져 없다 (2026-09-30)
MAX_BODY_LINES = 42  # 청크 본문의 상한 (4.1절) — 로그도 청크라 같은 규칙을 받는다
MAX_ROWS = MAX_BODY_LINES - 12  # 로그 한 파일의 판정 행 상한 — 산문 1 + 빈 줄 2 + 표 머리 2 + 요약 1 과 여유를 뺀 나머지
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


def thresholds(g: Graph) -> dict:
    """확신도 임계 셋 — 자동 적용·사람 확인 경계와 캘리브레이션 상태 (judge-threshold·judge-calibration 온톨로지)."""
    node = AGT[kb_lib.JUDGE_THRESHOLDS]
    got = lambda p, d=None: next(g.objects(node, p), d)  # noqa: E731 — 한 줄 접근자
    if got(AGT.autoApplyThreshold) is None:
        raise JudgeError(f"{SHAPES}: 임계 셋 개체 `agt:{kb_lib.JUDGE_THRESHOLDS}` 가 없다 — 임계의 원본은 프로파일이다")
    return {"auto": float(got(AGT.autoApplyThreshold)), "human": float(got(AGT.humanReviewThreshold, 0)),
            "measured": bool(got(AGT.bandAccuracyMeasured, False)),
            "floor": int(got(AGT.calibrationSampleFloor, 0)), "model": str(got(AGT.calibratedFor, kb_lib.EMPTY_UNDECIDED))}


def route(confidence: float, th: dict) -> str:
    """확신도 → 처리. 구간별 정확도(정확도·판별력)를 재기 전에는 자동 적용 구간이 없다 (규칙 ②) —
    확신도가 세션 판정자의 자기 보고인 지금은 이 경계가 항상 사람 확인 큐로 떨어진다."""
    if not th["measured"]:
        return kb_lib.JUDGE_QUEUE
    if confidence >= th["auto"]:
        return kb_lib.JUDGE_ROUTES[0]
    return kb_lib.JUDGE_ROUTES[1] if confidence >= th["human"] else kb_lib.JUDGE_ROUTES[2]


def check_question(q: dict, name: str) -> None:
    """형이 셋 안이고 선택 집합이 상한 안인가 — 아니면 수정 방향과 함께 거부한다 (규칙 ③)."""
    if q["form"] not in kb_lib.JUDGE_FORMS:
        raise JudgeError(f"질문 {name}: 형 {q['form']!r} 이 {' · '.join(kb_lib.JUDGE_FORMS)} 밖이다 — 자유 서술은 판정이 아니다")
    if q["form"] == "choice" and len(q["options"]) > kb_lib.JUDGE_CHOICE_MAX:
        raise JudgeError(f"질문 {name}: 선택 집합 {len(q['options'])} 개가 상한 {kb_lib.JUDGE_CHOICE_MAX} 를 넘는다 — "
                         f"질문을 2단계로 나눈다: 후보마다 독립 점수(score)를 묻고 상위 {kb_lib.JUDGE_CHOICE_MAX} 이하로 좁힌 뒤 "
                         "명시 선택(choice)을 묻는다 (p8-judge-calibration-binding 규칙 ③)")


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
    """응답 집합에서 이 (질문, 대조 지문)의 응답 하나를 꺼낸다 — 지문을 적지 않은 응답은 순서로 소비한다.

    `fp`는 **대조 지문**(`kb_lib.label_fingerprint`)이다 — 세션 판정자가 실제로 본 라벨+본문의 sha256이지,
    청크 파일 바이트의 sha256(로그의 `입력 지문` 열)이 아니다. 파일 지문으로 대조하면 판정자의 응답이
    전부 안 잡힌다(2026-09-30 vnv 결함 보고 ①).
    """
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (name, q["iri"]):
            continue
        if r.get("fingerprint") and r["fingerprint"] != fp:
            continue
        used.add(i)
        return normalize(r, str(data.get("judge", kb_lib.EMPTY_UNDECIDED)))
    raise JudgeError(f"응답 집합(판정자 {data.get('judge')})에 질문 {name} · 입력 지문 {fp[:12]}… 의 응답이 없다 — "
                     "`responses` 에 항목을 더한다")


# ── 판정 ────────────────────────────────────────────────────────────────────────────────────────────────

def judge_rows(root: Path, paths: list[str], q: dict, name: str, th: dict, resp_sets: list[dict],
              sheet: dict[str, dict] | None = None) -> list[dict]:
    """청크 × 응답 집합마다 판정 행을 만든다.

    지문은 **둘**이다(2026-09-30 vnv 결함 보고 ①) — 로그의 `입력 지문` 열에 실리는 **기록 지문**(청크 파일
    바이트의 sha256, 추적·재현의 열쇠)과, 응답을 찾는 **대조 지문**(`kb_lib.label_fingerprint`, 판정자에게
    실제로 보인 라벨+본문의 sha256)이다. 세션 판정자는 파일을 읽지 않고 `label_sample.py --judge-sheet`가 보인
    것만 보므로 대조는 그 지문으로 해야 한다 — 파일 바이트 지문으로 대조하면 응답이 전부 안 잡힌다(실측 결함).
    `sheet`(선택)는 `--decoys`의 key.json 전체(실표본+미끼)를 경로로 색인한 것이다 — 있으면 그 항목의
    라벨·본문(판정자에게 보인 그대로)으로 대조 지문을 내고, 없으면 청크를 다시 읽어(label_sample.body_of와
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
                raise JudgeError(f"{p}: 청크로 읽을 수 없다 — {e}")
            record_fp = hashlib.sha256(raw).hexdigest()
            shown = sheet.get(posix) or sheet.get(p)
            item = shown if shown else {"title_ko": meta.get("title_ko", ""), "title": meta.get("title", ""),
                                        "body": sample_body_of(str(path))}
            match_fp = kb_lib.label_fingerprint(item)
            answer = take_response(data, used, q, name, match_fp)
            rows.append({"path": posix, "iri": meta["id"], "level": meta["level"],
                         "verdict_stem": f"{path.parent.name}-{path.stem}",
                         "label": meta.get("title_ko", ""), "fingerprint": record_fp, "at": now,
                         "route": route(answer["confidence"], th), **answer})
    return rows


def agreement(rows: list[dict]) -> None:
    """행마다 `일치` 열을 채운다 — 같은 (대상, 입력 지문)에 둘 이상의 판정자 응답이 있을 때만 일치·불일치, 단독이면
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
    판별도 놓쳤다. 척도의 상황 문장 자체는 그대로다 — 척도는 상황으로 적는다(질문 온톨로지, p8-judge-calibration-binding).
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


# ── 판정 로그 (memory plane, append-only) 와 결과 주석 (annotation plane, 논평 형식) ─────────────────────

def log_chunk(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str) -> str:
    """판정 로그 본문 — 표의 열이 곧 필수 필드다 (게이트 id judge-log)."""
    n = counts(rows)
    judges = sorted({r["judge"] for r in rows})
    agree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[0])
    disagree_n = sum(1 for r in rows if r.get("agree") == kb_lib.JUDGE_AGREEMENT[1])
    ko = f"판정 {stamp}: 질문 {q['label']} · 판정 {len(rows)} · 판정자 {len(judges)} · 사람 확인 큐 {n[kb_lib.JUDGE_QUEUE]}"
    en = f"Judgement {stamp}: question {name}, {len(rows)} judged by {len(judges)} judge(s), {n[kb_lib.JUDGE_QUEUE]} queued"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
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
    return "\n".join(head + body) + "\n"


def verdict_chunk(row: dict, q: dict, name: str, stamp: str) -> str:
    """결과 주석 본문 — 논평 형식 (p7-commentary-form). `본문:` 은 판정자가 쓰지 않는다 (규칙 ④)."""
    ko = f"판정 결과 — {q['label']}: 값 {row['value']} · 확신도 {kb_lib.num(row['confidence'])}"
    en = f"Judgement result — {q['label_en']}: value {row['value']}, confidence {kb_lib.num(row['confidence'])}"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: annotation", f"level: {row['level']}",
            f"title_ko: {ko}", f"title: {en}", "status: draft", f"sources: [{{resource: {ODD_IRI}}}]",
            f"assumes: [{', '.join(ASSUMPTIONS)}]", f"targets: [{row['iri']}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    body = [f"thought (non-blocking): 질문 `agt:{name}` 의 값은 `{row['value']}` 이고 확신도는 "
            f"{kb_lib.num(row['confidence'])} 이며 판정자는 `{row['judge']}` 다.", "",
            f"대상: {row['iri']}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{row['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-calibration-binding 규칙 ④). 입력 지문은 "
            f"`{row['fingerprint'][:12]}…` 이고 일치는 `{row.get('agree', kb_lib.JUDGE_AGREEMENT[2])}` 다. 전체는 판정 로그에 있다."]
    return "\n".join(head + body) + "\n"


def write_records(root: Path, rows: list[dict], q: dict, name: str, th: dict, source: str, now: datetime) -> list[Path]:
    """판정 로그와 결과 주석을 쓴다 — 이미 있는 파일을 덮지 않는다 (append-only, r-026).

    결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>`(`verdict_stem`)을 쓴다(2026-09-30 vnv 결함 보고 ②) —
    결정 복합체는 파일 stem이 전부 `conclusion`·`rationale`·`alternatives`뿐이라 파일명이 그대로 부딪힌다
    (실측: 실표본 60 중 50건이 그 충돌로 로그에 못 들어갔다). 부모 디렉토리 이름(결정 슬러그)을 더하면 유일하다.
    """
    stamp = kb_lib.utc_stamp(now)
    log_dir, verdict_dir = root / kb_lib.JUDGE_LOG_DIR, root / kb_lib.JUDGE_VERDICT_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    verdict_dir.mkdir(parents=True, exist_ok=True)
    written = []
    chunks = [rows[i:i + MAX_ROWS] for i in range(0, len(rows), MAX_ROWS)]
    for i, part in enumerate(chunks):
        suffix = "" if i == 0 else f"-{i + 1}"
        target = log_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{now.strftime('%Y%m%dT%H%M%SZ')}{suffix}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 판정 로그는 append-only 다 (r-026)")
        target.write_text(log_chunk(part, q, name, th, source, stamp), encoding="utf-8")
        written.append(target)
    for r in rows:
        target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-{r['verdict_stem']}-{slug(r['judge'])}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 같은 질문·판정자의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
        target.write_text(verdict_chunk(r, q, name, stamp), encoding="utf-8")
        written.append(target)
    return written


# ── 보고 ────────────────────────────────────────────────────────────────────────────────────────────────

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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--question", default="", help="질문 id — 프로파일의 `agt:` 지역명 또는 전체 IRI (`--list` 에는 필요 없다)")
    ap.add_argument("--responses", action="append", default=[], metavar="JSON",
                    help="세션 판정자의 응답 — {judge, responses: [{question, fingerprint, value, confidence}]}. "
                         "판정자마다 한 번씩 반복한다 — 둘 이상이면 일치를 계산한다 (옛 --fixture 의 승격)")
    ap.add_argument("--decoys", default="", metavar="JSON",
                    help="label_sample.py --decoys 가 낸 key.json — 미끼 항목의 검출률을 보고 요약에 낸다(라벨 대표성 실험 전용)")
    ap.add_argument("--record", action="store_true",
                    help=f"판정 로그({kb_lib.JUDGE_LOG_DIR}/judge-<UTC>.md)와 결과 주석({kb_lib.JUDGE_VERDICT_DIR}/)을 쓴다")
    ap.add_argument("--into", default="", metavar="DIR", help="기록의 뿌리 — 기본은 워크스페이스다. 시험물을 밖에 두는 수단이다")
    ap.add_argument("--out", default="", metavar="FILE", help="보고를 파일로도 쓴다")
    ap.add_argument("--profile", default=PROFILE_DIR, help="질문·척도·임계의 원본 디렉토리")
    ap.add_argument("--list", action="store_true", help="등록된 질문만 나열하고 멈춘다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("chunks", nargs="*", help="판정 대상 청크 파일 — 라벨 대표성 실험(`--decoys`)만 쓰면 생략할 수 있다")
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
        # 대조 지문의 원본 — key.json 은 실표본·미끼를 다 담으므로 실표본 지문도 여기서 스스로 대조한다
        # (2026-09-30 vnv 결함 보고 ①). 경로가 곧 색인 키다 — label_sample.py 가 낸 path 그대로다
        sheet_index = {it["path"]: it for it in (decoys_raw or []) if isinstance(it, dict) and it.get("path")}

        if not a.chunks and not decoy_items:
            print(f"SKIP [{TAG}] 판정 대상 0건 — PASS 가 아니다")
            return EXIT_SKIP
        if not a.responses:
            raise JudgeError("`--responses <json>` 이 없다 — 외부 서비스가 없으므로 세션 판정자의 응답을 오프라인으로 받는다")
        resp_sets = [load_responses(at(root, p)) for p in a.responses]

        th = thresholds(g)
        now = datetime.now(timezone.utc)
        rows = judge_rows(root, a.chunks, q, name, th, resp_sets, sheet=sheet_index) if a.chunks else []
        if rows:
            agreement(rows)
        decoy_hit, decoy_seen = decoy_detection_rate(decoy_items, q, resp_sets) if decoy_items else (0, 0)
        # 응답 파일의 이름만 적는다(basename) — 절대 경로는 판정 로그에 실리지 않는다(2026-09-30 vnv 결함 보고 ⑤)
        source = "세션 판정자 응답 " + " · ".join(f"`{Path(p).name}`(판정자 `{d.get('judge')}`)"
                                               for p, d in zip(a.responses, resp_sets))
        text = report(rows, q, name, th, source, now, decoy_hit, decoy_seen, len(decoy_items))
        print(text)
        if a.out:
            at(root, a.out).write_text(text, encoding="utf-8")
        if a.record:
            if not rows:
                raise JudgeError("기록할 판정 행이 없다 — `--decoys` 만으로는 판정 로그를 남기지 않는다(청크 대상이 없다)")
            written = write_records(at(root, a.into) if a.into else root, rows, q, name, th, source, now)
            print("기록: " + " · ".join(p.as_posix() for p in written) +
                  " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    except JudgeError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
