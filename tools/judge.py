#!/usr/bin/env python3
"""판정자 — 등록된 판정 질문을 청크에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-calibration-binding).

게이트 밖 도구다. `bazel test` 는 판정을 부르지 않고 판정 로그의 형식·필수 필드만 본다(게이트 id `judge-log`) —
외부 서비스가 게이트의 입력이 되면 같은 리비전이 네트워크 상태에 따라 다른 판정을 낸다.
질문·척도·임계의 원본은 프로파일 온톨로지와 shape 다(`kb/ontology/profile/development/judge-*-ontology.ttl` ·
`kb/ontology/shapes/judge-question-shapes.ttl`) — 도구는 질문 문장도 임계도 상수로 갖지 않는다. 질문의 형은
noul·choice·score 셋이고 선택 집합은 255 이하다. 넘으면 독립 점수 뒤 명시 선택의 2단계를 안내하고 거부한다.
확신도는 집단 수준의 캘리브레이션이라 개별 답을 보증하지 않으므로, 구간별 정확도를 재기 전에는 자동 적용 구간이
없고 처리는 전부 사람 확인 큐다. 판정자는 설명을 만들지 못하므로 결과 주석의 `본문:` 은 `해당 없음` 이다.
외부 호출은 함수 하나(`call_service`)에 갇혀 있고 자격은 환경 변수 `AKB_JUDGE_ENDPOINT`·`AKB_JUDGE_API_KEY`·
`AKB_JUDGE_MODEL` 로만 받는다. 셋 중 하나라도 없으면 호출하지 않고 무엇이 필요한지 적고 멈춘다. `--fixture` 는
기록된 응답으로 같은 경로를 도는 오프라인 모드이며 로그·주석 생성을 네트워크 없이 시험하는 자리다.
사용: bazel run //tools:judge -- --question <질문 id> [--fixture <json>] [--record] [--into <디렉토리>] <청크 파일…>
      python3 tools/judge.py --question labelRepresentsBody --fixture fx.json kb/dev/decision/<결정>/conclusion.md
출력·종료: 보고는 stdout(`--out` 으로 파일)이고 `--record` 는 판정 로그(`kb/vv/run/judge-<UTC>.md`)와 결과
주석(`kb/vv/verdict/<슬러그>.md`)을 append-only 로 쓴다. 자격 없음·질문 없음·형 밖·선택 집합 255 초과·고정물
응답 없음·읽을 수 없는 입력은 `FAIL [judge] …` + EXIT_CONFIG. 판정 대상이 0건이면 EXIT_SKIP 이다.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, RDF, URIRef
from rdflib.namespace import SKOS

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행
try:  # noqa: E402 — 대상의 IRI·수준은 frontmatter 파서가 읽는다. 값 어휘의 원본은 defs/kb.bzl 이다 (M1 단일 정의처)
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402

AGT = kb_lib.AGT
ID = kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
TAG = kb_lib.JUDGE_GATE
GENERATOR = kb_lib.JUDGE_GENERATOR
PROFILE_DIR = "kb/ontology/profile/development"
SHAPES = "kb/ontology/shapes/judge-question-shapes.ttl"
ODD_IRI = str(ID["odd-agentic-knowledge-base"])
ASSUMPTIONS = [str(ID[a]) for a in kb_lib.JUDGE_ASSUMPTIONS]  # 청크 규약 + 판정 서비스 가정 — 목록의 정의처는 kb_lib 다
MAX_BODY_LINES = 42  # 청크 본문의 상한 (4.1절) — 로그도 청크라 같은 규칙을 받는다
MAX_ROWS = MAX_BODY_LINES - 12  # 로그 한 파일의 판정 행 상한 — 산문 1 + 빈 줄 2 + 표 머리 2 + 요약 1 과 여유를 뺀 나머지
TIMEOUT = 20   # 외부 호출의 상한 초 — 모델 실측 70~500ms 의 넉넉한 상한이다


class JudgeError(Exception):
    """입력·설정 문제 — 메시지가 곧 수정 안내다 (EXIT_CONFIG)."""


def at(root: Path, p: str) -> Path:
    """상대 경로를 워크스페이스 루트 기준으로 푼다 — `bazel run` 의 작업 디렉토리는 runfiles 트리다."""
    path = Path(p)
    return path if path.is_absolute() else root / path


# ── 프로파일에서 질문·척도·임계를 읽는다 (도구는 상수를 갖지 않는다) ────────────────────────────────────────

def load_profile(root: Path, profile: str, shapes: str) -> Graph:
    """프로파일 온톨로지 모듈과 판정 질문 shape 를 한 그래프로 읽는다."""
    g = Graph()
    files = sorted((root / profile).glob("*.ttl")) + ([root / shapes] if (root / shapes).is_file() else [])
    if not files:
        raise JudgeError(f"{profile}: 프로파일 TTL 이 없다 — 질문·척도·임계의 원본이 거기다")
    for f in files:
        g.parse(f, format="turtle")
    return g


def questions(g: Graph) -> dict:
    """등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}."""
    out = {}
    for q in g.subjects(RDF.type, AGT.JudgeQuestion):
        if not isinstance(q, URIRef):
            continue
        form = str(next(g.objects(q, AGT.questionForm), ""))
        out[str(q).rsplit("/", 1)[-1]] = {
            "iri": str(q), "form": form,
            "label": kb_lib.label_of(g, q) or str(q),
            "label_en": kb_lib.label_of(g, q, "en") or str(q).rsplit("/", 1)[-1],
            "text": str(next(g.objects(q, SKOS.definition), "")),
            "scale": sorted(str(s) for s in g.objects(q, AGT.scaleSituation)),
            "options": sorted(str(o) for o in g.objects(q, AGT.choiceOption)),
        }
    return out


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
    """확신도 → 처리. 구간별 정확도를 재기 전에는 자동 적용 구간이 없다 (규칙 ②)."""
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


# ── 외부 호출 — 이 함수 하나가 경계다 ────────────────────────────────────────────────────────────────────

def credentials() -> dict:
    """자격은 환경 변수로만 받는다. 하나라도 없으면 호출하지 않는다."""
    env = {k: os.environ.get(k, "") for k in kb_lib.JUDGE_ENV}
    missing = [k for k, v in env.items() if not v]
    if missing:
        raise JudgeError("판정 서비스 자격이 없다 — 환경 변수 " + " · ".join(f"`{m}`" for m in missing) +
                         " 를 설정하거나 `--fixture <json>` 오프라인 모드로 돈다. 자격은 저장소에 두지 않는다 "
                         "(ODD 조건 id:cond-judge-service)")
    return env


def call_service(env: dict, q: dict, text: str) -> dict:
    """판정 서비스 호출 — 구조화 출력 전용 모델(System One)에 질문 하나를 보내고 값과 확신도를 받는다.

    이 함수가 외부 의존의 유일한 자리다. 요청·응답의 필드 이름은 공개 문서가 밝히지 않아 `미확정` 이다 —
    아는 것만 적었다: 입력은 구조 없는 상태(문자열)이고 출력은 타입 있는 값과 확률이며 질문의 형은 셋이다.
    형식이 확정되면 고칠 곳은 이 함수와 `--fixture` 고정물의 키뿐이다.
    """
    body = {"model": env["AKB_JUDGE_MODEL"], "form": q["form"], "question": q["text"], "input": text}
    if q["form"] == "choice":
        body["options"] = q["options"]
    if q["form"] == "score":
        body["scale"] = q["scale"]
    req = urllib.request.Request(
        env["AKB_JUDGE_ENDPOINT"], data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {env['AKB_JUDGE_API_KEY']}"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:  # noqa: S310 — 주소는 환경 변수가 준다
            payload = json.loads(r.read().decode("utf-8"))
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise JudgeError(f"판정 서비스에 닿지 못했다 — {e}. ODD 조건 id:cond-judge-service 의 판정이 이탈이다")
    return normalize(payload, env["AKB_JUDGE_MODEL"])


def normalize(payload: dict, model: str) -> dict:
    """응답 → {value, confidence, model}. 키 이름은 미확정이라 아는 이름 둘을 차례로 본다."""
    value = payload.get("value", payload.get("decision"))
    conf = payload.get("confidence", payload.get("probability"))
    if value is None or conf is None:
        raise JudgeError(f"응답에 값 또는 확신도가 없다 — 받은 키 {sorted(payload)}. 필요한 것은 `value`·`confidence` 다")
    return {"value": str(value), "confidence": float(conf), "model": str(payload.get("model", model))}


def load_fixture(path: Path) -> dict:
    """오프라인 모드의 기록된 응답 — {model, responses: [{question, fingerprint?, value, confidence}]}."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise JudgeError(f"{path}: 고정물을 읽을 수 없다 — {e}")
    if not isinstance(data, dict) or not isinstance(data.get("responses"), list):
        raise JudgeError(f"{path}: 고정물은 `responses` 목록을 가진 객체다")
    return data


def take_fixture(data: dict, used: set, q: dict, name: str, fp: str) -> dict:
    """고정물에서 이 (질문, 입력 지문)의 응답 하나를 꺼낸다 — 지문을 적지 않은 응답은 순서로 소비한다."""
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (name, q["iri"]):
            continue
        if r.get("fingerprint") and r["fingerprint"] != fp:
            continue
        used.add(i)
        return normalize(r, str(data.get("model", kb_lib.EMPTY_UNDECIDED)))
    raise JudgeError(f"고정물에 질문 {name} · 입력 지문 {fp[:12]}… 의 응답이 없다 — `responses` 에 항목을 더한다")


# ── 판정 ────────────────────────────────────────────────────────────────────────────────────────────────

def judge(root: Path, paths: list[str], q: dict, name: str, th: dict, env: dict | None, fixture: dict | None) -> list[dict]:
    """청크마다 질문 하나를 물어 판정 행을 만든다. 입력 지문은 보낸 바이트의 sha256 이다.

    상대 경로는 워크스페이스 루트 기준으로 푼다 — `bazel run` 의 작업 디렉토리는 runfiles 트리라 그대로는 닿지 못한다.
    """
    rows, used = [], set()
    for p in paths:
        path = at(root, p)
        try:
            raw = path.read_bytes()
            meta, _ = parse_chunk(str(path))
        except (OSError, ValueError) as e:
            raise JudgeError(f"{p}: 청크로 읽을 수 없다 — {e}")
        fp = hashlib.sha256(raw).hexdigest()
        text = raw.decode("utf-8")
        answer = take_fixture(fixture, used, q, name, fp) if fixture else call_service(env, q, text)
        now = kb_lib.utc_stamp(datetime.now(timezone.utc))
        rows.append({"path": Path(p).as_posix(), "iri": meta["id"], "level": meta["level"], "stem": path.stem,
                     "label": meta.get("title_ko", ""), "fingerprint": fp, "at": now,
                     "route": route(answer["confidence"], th), **answer})
    return rows


def counts(rows: list[dict]) -> dict:
    return {r: sum(1 for x in rows if x["route"] == r) for r in kb_lib.JUDGE_ROUTES}


# ── 판정 로그 (memory plane, append-only) 와 결과 주석 (annotation plane, 논평 형식) ─────────────────────

def log_chunk(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str) -> str:
    """판정 로그 본문 — 표의 열이 곧 필수 필드다 (게이트 id judge-log)."""
    n = counts(rows)
    ko = f"판정 {stamp}: 질문 {q['label']} · 판정 {len(rows)} · 사람 확인 큐 {n[kb_lib.JUDGE_QUEUE]}"
    en = f"Judgement {stamp}: question {name}, {len(rows)} judged, {n[kb_lib.JUDGE_QUEUE]} queued for human review"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    measured = "있음" if th["measured"] else kb_lib.EMPTY_REVIEWED
    body = [f"**관측** — {stamp} 에 `judge` 가 질문 `agt:{name}`({q['form']} 형)을 청크 {len(rows)}건에 물었다. "
            f"호출은 {source} 다. 임계는 자동 적용 {kb_lib.num(th['auto'])} · 사람 확인 {kb_lib.num(th['human'])} 이고, "
            f"구간별 정확도 측정은 `{measured}` · 구간당 표본 하한은 {th['floor']}건이다.", "",
            kb_lib.JUDGE_LOG_TABLE_HEADER, "|" + "---|" * len(kb_lib.JUDGE_LOG_TABLE_HEADER.split("|")[1:-1])]
    for r in rows:
        body.append(f"| `agt:{name}` | `{r['iri']}` | `{r['value']}` | {kb_lib.num(r['confidence'])} | "
                    f"`{r['model']}` | `{r['fingerprint']}` | {r['at']} | {r['route']} |")
    body += ["", f"판정 요약 — " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES) +
             ". 확신도는 집단 수준의 캘리브레이션이라 개별 답의 정확성을 보증하지 않는다. "
             f"구간별 정확도를 구간당 {th['floor']}건 이상으로 재기 전에는 자동 적용 구간이 없다 — 처리는 전부 사람 확인 큐다. "
             f"캘리브레이션 대상 모델은 `{th['model']}` 이다."]
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
            f"{kb_lib.num(row['confidence'])} 이며 모델은 `{row['model']}` 이다.", "",
            f"대상: {row['iri']}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{row['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-calibration-binding 규칙 ④). 입력 지문은 "
            f"`{row['fingerprint'][:12]}…` 이고 전체는 판정 로그에 있다."]
    return "\n".join(head + body) + "\n"


def write_records(root: Path, rows: list[dict], q: dict, name: str, th: dict, source: str, now: datetime) -> list[Path]:
    """판정 로그와 결과 주석을 쓴다 — 이미 있는 파일을 덮지 않는다 (append-only, r-026)."""
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
        target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-{r['stem']}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 같은 질문의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
        target.write_text(verdict_chunk(r, q, name, stamp), encoding="utf-8")
        written.append(target)
    return written


# ── 보고 ────────────────────────────────────────────────────────────────────────────────────────────────

def report(rows: list[dict], q: dict, name: str, th: dict, source: str, now: datetime) -> str:
    n = counts(rows)
    rep = kb_lib.gendoc_header(
        "judge", "판정자 판정 결과", "tools/judge.py",
        f"등록된 판정 질문 `agt:{name}` 을 청크에 물어 값과 확신도를 받고 임계로 처리를 가른다 — 게이트 밖이고 "
        "게이트는 판정 로그의 형식만 본다 (8.14절)",
        f"bazel run //tools:judge -- --question {name} <청크 파일…>", [r["path"] for r in rows],
        f"청크 {len(rows)} · 질문 1({q['form']} 형)",
        kb_lib.gendoc_view_notice("판정자의 응답과 프로파일의 질문·임계"), input_kind="판정 대상",
        extra=[f"- 호출: {source}",
               f"- 임계: 자동 적용 {kb_lib.num(th['auto'])} · 사람 확인 {kb_lib.num(th['human'])} · "
               f"구간별 정확도 측정 {'있음' if th['measured'] else kb_lib.EMPTY_REVIEWED} (구간당 표본 하한 {th['floor']})",
               "- 처리: " + " · ".join(f"{k} {n[k]}" for k in kb_lib.JUDGE_ROUTES)])
    body = ["## 판정 — 확신도는 집단 수준의 캘리브레이션이고 개별 답을 보증하지 않는다", "",
            "| 대상 | 라벨 | 값 | 확신도 | 처리 | 입력 지문 |", "|---|---|---|---|---|---|"]
    for r in rows:
        body.append(f"| `{r['path']}` | {r['label'] or kb_lib.NONE_MARK} | `{r['value']}` | "
                    f"{kb_lib.num(r['confidence'])} | {r['route']} | `{r['fingerprint'][:12]}…` |")
    body += ["", "## 질문", "", f"- `agt:{name}` ({q['form']} 형) — {q['text']}"]
    if q["scale"]:
        body += ["- 척도의 상황 문장: " + " · ".join(f"`{s}`" for s in q["scale"])]
    if q["options"]:
        body += [f"- 선택 집합 {len(q['options'])}개(상한 {kb_lib.JUDGE_CHOICE_MAX}): " + " · ".join(f"`{o}`" for o in q["options"])]
    body += ["", f"판정자는 설명을 만들지 못하므로 결과 주석의 `본문:` 은 `{kb_lib.EMPTY_NOT_APPLICABLE}` 이고 "
             "사람 또는 System 2 에이전트가 채운다."]
    return kb_lib.gendoc_assemble(rep, body, [r["path"] for r in rows], input_kind="판정 대상")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--question", default="", help="질문 id — 프로파일의 `agt:` 지역명 또는 전체 IRI (`--list` 에는 필요 없다)")
    ap.add_argument("--fixture", default="", metavar="JSON", help="오프라인 모드 — 기록된 응답으로 같은 경로를 돈다")
    ap.add_argument("--record", action="store_true",
                    help=f"판정 로그({kb_lib.JUDGE_LOG_DIR}/judge-<UTC>.md)와 결과 주석({kb_lib.JUDGE_VERDICT_DIR}/)을 쓴다")
    ap.add_argument("--into", default="", metavar="DIR", help="기록의 뿌리 — 기본은 워크스페이스다. 시험물을 밖에 두는 수단이다")
    ap.add_argument("--out", default="", metavar="FILE", help="보고를 파일로도 쓴다")
    ap.add_argument("--profile", default=PROFILE_DIR, help="질문·척도·임계의 원본 디렉토리")
    ap.add_argument("--list", action="store_true", help="등록된 질문만 나열하고 멈춘다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("chunks", nargs="*", help="판정 대상 청크 파일")
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
        if not a.chunks:
            print(f"SKIP [{TAG}] 판정 대상 0건 — PASS 가 아니다")
            return EXIT_SKIP
        fixture = load_fixture(at(root, a.fixture)) if a.fixture else None
        env = None if fixture else credentials()
        source = f"오프라인 고정물 `{a.fixture}`" if fixture else f"판정 서비스 `{kb_lib.JUDGE_ENV[0]}`"
        th = thresholds(g)
        rows = judge(root, a.chunks, q, name, th, env, fixture)
        now = datetime.now(timezone.utc)
        text = report(rows, q, name, th, source, now)
        print(text)
        if a.out:
            at(root, a.out).write_text(text, encoding="utf-8")
        if a.record:
            written = write_records(at(root, a.into) if a.into else root, rows, q, name, th, source, now)
            print("기록: " + " · ".join(p.as_posix() for p in written) +
                  " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    except JudgeError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
