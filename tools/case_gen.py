#!/usr/bin/env python3
"""V&V 케이스 생성기 — 논리 시나리오의 `keep`·`cover` 에서 concrete 케이스 청크(`kb/vv/case/*.md` 꼴)를 결정론적으로 만든다.

결정 p8-case-generation: concrete 케이스는 사람이 쓰지 않는다 — `keep`+`cover` 에서 생성하고 표본 근거 없는 케이스는 거부한다.
생성 규칙은 다섯(등가분할 · 경계값 · t-wise 조합 · 요인 주입 · 관측 재현)이고 규칙·seed 는 케이스의 provenance 에 남는다.
결정 p8-scenario-authoring: `keep()` 은 자극의 자리이므로 입력은 `decision`(vv) **logical** 시나리오의 자극 청크(`<슬러그>-stimulus.md`)다.
결정 p8-machine-readable-case: 출력 케이스는 `vv_run` 이 읽는 꼴 그대로다 — 펜스 `files`·`expect`, `**실행 명령**` 한 줄.

입력 — 시나리오 자극 청크 본문의 `yaml` 펜스 하나(키 `keep`·`cover` 가 둘 다 있는 펜스. 그 밖의 펜스는 산문의 예시다):
  keep:  변수 → {odd: <ODD 속성 IRI(id:cond-…)> | outside, range: [lo, hi] (정수) | values: [값…], reject: [값…], domain: [lo, hi]}
         `range`·`values` 가 keep 이다. `reject` 는 열거 변수의 keep 밖 값, `domain` 은 범위 변수의 keep 밖까지 포함한 정의역이다.
         `odd: outside` 인 변수가 든 케이스는 `odd:outside` 를 달아 커버리지에서 빠진다 (p8-scenario-authoring 규약).
  cover: [{rule: equivalence|boundary|pairwise|factor|observed, …}]  — 항목 하나가 표본 추출 근거 하나다.
         equivalence {vars} · boundary {vars} (범위 변수만) · pairwise {vars} (열거 변수 둘 이상) ·
         factor {var, factors: {agt:<요인>: <keep 밖 값>}} · observed {run: kb/vv/run/<기록>.md, values: {변수: 값}}
  seed:  정수 — 등가분할의 대표값을 고르는 난수의 seed. 케이스의 `**표본 근거**` 에 남는다
  case:  {criteria: <기준 IRI>, verifies: [<IRI>…], derivesFrom: [<IRI>…], title_ko, title, summary, stimulus, files: {이름: 내용},
          command, accept: {prose, expect}, reject: {prose, expect}} — 문자열의 `${변수}` 를 케이스의 값으로 바꾼다.
         `derivesFrom` 은 선택이다 — 케이스의 `derivesFrom` 에 시나리오 IRI 다음으로 옮긴다(수기 케이스가 가졌던 출처 링크를 잇는다).
         생성 케이스는 `restored` 를 쓰지 않는다 — 생성기가 템플릿에서 놓는 링크는 복원이 아니라 구축이다
값을 손으로 적은 항목(`cases` 키 · 관측 재현 밖의 `values`)과 `rule` 없는 항목은 표본 근거가 없으므로 FAIL 이다.
나머지 변수는 기준값(범위 변수는 lo, 열거 변수는 values 의 첫째)에 둔다. 값이 하나라도 keep 밖이면 케이스는 `reject` 부류다.

사용: case_gen.py --out <디렉토리> [--root .] [--scenario <자극 청크>…] [--residency defs/kb.bzl] [--odd <ODD yml>]
      case_gen.py --check [--root .] [--scenario <자극 청크>…] [--cases kb/vv/case] [--all-generated]
--scenario 가 없으면 생성 모드는 `kb/vv/scenario/` 의 logical 자극 청크 중 입력 펜스가 있는 것 전부를 읽는다. --check 는 준 시나리오만 본다 —
//:case_drift_test 가 대상 목록을 명시로 준다(빈 목록이면 대상 0 이고 PASS 다. 생성기이므로 SKIP 이 아니다). `--all-generated` 는
케이스 디렉토리의 모든 케이스가 이 생성기의 것인지 본다(수기 케이스 0). 저장소에 쓰는 일은 vnv 가 `--out kb/vv/case` 로 한다.
출력·종료: 생성 시점 거부는 `FAIL [case-gen] …` EXIT_FAIL, --check 의 어긋남은 `FAIL [case-drift] …` EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import difflib
import itertools
import json
import random
import re
import sys
import uuid
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib, vv_run  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    import vv_run
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.CASE_GEN_GATE, kb_lib.CASE_DRIFT_GATE
ACTOR = kb_lib.CASE_GEN_ACTOR  # 케이스의 generated.by — 역할이 아니라 프로세스다. writer 검사 밖이다 (validate check_writer)
SCENARIO_DIR = kb_lib.KB_VV + "/scenario"
CASE_DIR = kb_lib.KB_VV + "/case"
RUN_DIR = kb_lib.VV_RUN_DIR
ODD_FILE = "kb/odd/project-odd.yml"
CHUNK_NS = str(kb_lib.ID) + "chunk/"
STIMULUS_SUFFIX = "-stimulus"
INPUT_HEAD = (re.compile(r"^keep\s*:", re.M), re.compile(r"^cover\s*:", re.M))  # 두 키가 다 있는 펜스만 입력이다
INPUT_KEYS = ("keep", "cover", "seed", "case")
VAR_NAME = re.compile(r"[a-z][a-z0-9_]*")
VAR_KEYS = ("odd", "range", "values", "reject", "domain")
ODD_OUTSIDE = "outside"
RULE_TAGS = {"equivalence": "sampling:equivalence", "boundary": "sampling:boundary", "pairwise": "sampling:pairwise",
             "factor": "sampling:factor", "observed": "sampling:observed"}  # 결정 p8-case-generation 의 근거 태그
RULE_KEYS = {"equivalence": ("vars",), "boundary": ("vars",), "pairwise": ("vars",), "factor": ("var", "factors"),
             "observed": ("run", "values")}
ORIGIN_OBSERVED = "origin:observed"
ODD_OUTSIDE_TAG = "odd:outside"
FACTOR_TAG = re.compile(r"agt:[A-Za-z][A-Za-z0-9]*")
CASE_KEYS = ("criteria", "verifies", "derivesFrom", "title_ko", "title", "summary", "stimulus", "files", "command", "accept", "reject")
CASE_REQUIRED = ("criteria", "title_ko", "title", "summary", "stimulus", "command")
CLASS_KEYS = ("prose", "expect")
CLASSES = ("accept", "reject")
TEMPLATE = re.compile(r"\$\{([^{}\s]*)\}")  # `${변수}` — 셸의 `$(…)`·`$VAR` 와 vv_run 의 `{{이름}}` 은 건드리지 않는다
UNSAMPLED = "표본 근거 없는 케이스다"


class CaseGenError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다. 여러 줄이면 줄마다 하나다."""


# ── 입력 — 시나리오 자극 청크와 ODD ────────────────────

def odd_attributes(path: Path) -> set[str]:
    """ODD 문서의 속성 IRI 집합(`ATTRIBUTES.*.iri` — `id:cond-…` 꼴). 변수의 `odd` 가 이 안이어야 한다 (3.3절 ODD 참조)."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    attrs = data.get("ATTRIBUTES") or {}
    return {str(v.get("iri")) for v in attrs.values() if isinstance(v, dict) and v.get("iri")}


def raw_frontmatter(text: str) -> dict[str, str]:
    """frontmatter 의 키 → 원문 값. 생성 케이스가 시나리오의 `sources`·`assumes` 를 바이트 그대로 옮기는 자리다."""
    lines = text.splitlines()
    end = lines[1:].index("---") + 1
    out = {}
    for raw in lines[1:end]:
        key, _, val = raw.partition(":")
        out[key.strip()] = val.strip()
    return out


def load_scenario(path: Path) -> dict:
    """자극 청크 → {path, slug, iri, at, sources, assumes, spec}. logical `decision` 이 아니거나 입력 펜스가 없으면 거부한다."""
    meta, body = parse_chunk(str(path))
    if meta["type"] != "decision" or meta["level"] != "logical":
        raise CaseGenError(f"{path}: 케이스의 입력은 logical 시나리오(`decision`·`logical`)다 — 실제 {meta['type']}·{meta['level']} "
                           f"(p8-scenario-ladder-rungs: 변수 범위는 logical 높이에서 채운다)")
    fences = [f for f in vv_run.yaml_blocks(body) if all(h.search(f) for h in INPUT_HEAD)]
    if len(fences) != 1:
        raise CaseGenError(f"{path}: `keep`·`cover` 를 담은 `yaml` 펜스가 {len(fences)}개다 — 시나리오 하나에 하나다")
    try:
        spec = yaml.safe_load(fences[0])
    except yaml.YAMLError as e:
        raise CaseGenError(f"{path}: 입력 펜스를 읽을 수 없다 — {e}") from e
    raw = raw_frontmatter(path.read_text(encoding="utf-8"))
    at = re.search(r"\bat:\s*([^,}\s]+)", raw.get("generated", ""))
    if not at:
        raise CaseGenError(f"{path}: generated.at 이 없다 — 케이스의 생성 시각은 입력 시나리오의 시각이다(재생성이 바이트로 같아야 한다)")
    slug = path.stem[: -len(STIMULUS_SUFFIX)] if path.stem.endswith(STIMULUS_SUFFIX) else path.stem
    return {"path": path, "slug": slug, "iri": meta["id"], "at": at.group(1), "sources": raw.get("sources", ""),
            "assumes": raw.get("assumes", ""), "spec": spec}


def discover(root: Path) -> list[Path]:
    """`kb/vv/scenario/` 의 logical 자극 청크 중 입력 펜스가 있는 것 — 생성 모드에서 --scenario 가 없을 때의 대상이다."""
    out = []
    for p in sorted((root / SCENARIO_DIR).glob("*.md")):
        meta, body = parse_chunk(str(p))
        if meta["type"] == "decision" and meta["level"] == "logical" and any(
                all(h.search(f) for h in INPUT_HEAD) for f in vv_run.yaml_blocks(body)):
            out.append(p)
    return out


# ── 검사 — keep · cover · case 의 형식 ────────────────────

def check_keep(where: str, keep, odd: set[str]) -> list[str]:
    """`keep` 의 형식 — 변수마다 ODD 참조 하나와 keep 하나(`range` 또는 `values`)."""
    if not isinstance(keep, dict) or not keep:
        return [f"{where}: `keep` 은 비어 있지 않은 `변수: 명세` 매핑이다"]
    errs = []
    for name, v in keep.items():
        at = f"{where}: 변수 `{name}`"
        if not isinstance(name, str) or not VAR_NAME.fullmatch(name):
            errs.append(f"{at} 의 이름이 식별자가 아니다 — 소문자·숫자·`_`")
            continue
        if not isinstance(v, dict):
            errs.append(f"{at} 의 명세가 매핑이 아니다 — 키는 {' · '.join(VAR_KEYS)} 다")
            continue
        errs += [f"{at} 의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(VAR_KEYS)} 다" for k in v if k not in VAR_KEYS]
        ref = v.get("odd")
        if ref != ODD_OUTSIDE and ref not in odd:
            errs.append(f"{at} 의 `odd` {ref!r} 가 ODD 속성이 아니다 — 시나리오의 변수는 ODD 속성에서 온다(`id:cond-…`). "
                        f"ODD 밖이면 `{ODD_OUTSIDE}` 로 적어 커버리지에서 뺀다 (p8-scenario-authoring)")
        if ("range" in v) == ("values" in v):
            errs.append(f"{at} 는 `range` 와 `values` 중 하나를 keep 으로 갖는다")
        elif "range" in v:
            bad = check_interval(at, "range", v["range"]) + (check_interval(at, "domain", v["domain"]) if "domain" in v else [])
            errs += bad
            if "reject" in v:
                errs.append(f"{at}: `reject` 는 열거 변수의 것이다 — 범위 변수의 keep 밖은 `domain` 이 정한다")
            if "domain" in v and not bad:
                if not (v["domain"][0] <= v["range"][0] and v["range"][1] <= v["domain"][1]):
                    errs.append(f"{at}: `domain` {v['domain']} 가 `range` {v['range']} 를 품지 않는다")
        else:
            vals, rej = v.get("values"), v.get("reject", [])
            if not isinstance(vals, list) or not vals or not isinstance(rej, list):
                errs.append(f"{at}: `values` 는 비어 있지 않은 목록이고 `reject` 는 목록이다")
            elif set(map(str, vals)) & set(map(str, rej)) or len(set(map(str, vals + rej))) != len(vals + rej):
                errs.append(f"{at}: `values`·`reject` 에 같은 값이 둘 있다 — 값 하나는 keep 안이거나 밖이다")
            if "domain" in v:
                errs.append(f"{at}: `domain` 은 범위 변수의 것이다 — 열거 변수의 keep 밖은 `reject` 다")
    return errs


def check_interval(at: str, key: str, iv) -> list[str]:
    """`[lo, hi]` 정수 구간인가."""
    if not (isinstance(iv, list) and len(iv) == 2 and all(isinstance(x, int) and not isinstance(x, bool) for x in iv) and iv[0] <= iv[1]):
        return [f"{at}: `{key}` 는 정수 구간 `[lo, hi]`(lo ≤ hi)다 — 실제 {iv!r}"]
    return []


def check_cover(where: str, cover, keep: dict, root: Path) -> list[str]:
    """`cover` 의 형식 — 항목마다 근거 규칙 하나. 규칙 없는 항목과 손으로 적은 값은 표본 근거가 없다."""
    if not isinstance(cover, list) or not cover:
        return [f"{where}: `cover` 는 비어 있지 않은 목록이다 — {UNSAMPLED}(근거 규칙 없이 만들 케이스가 없다)"]
    errs = []
    for i, e in enumerate(cover, start=1):
        at = f"{where}: `cover` {i}번째 항목"
        if not isinstance(e, dict) or e.get("rule") not in RULE_TAGS:
            got = e.get("rule") if isinstance(e, dict) else e
            errs.append(f"{at}에 근거 규칙이 없다(`rule` {got!r}) — {UNSAMPLED}. 규칙은 {' · '.join(RULE_TAGS)} 다 (p8-case-generation)")
            continue
        rule = e["rule"]
        for k in e:
            if k == "values" and rule != "observed":
                errs.append(f"{at}({rule}) 가 값을 손으로 적었다 — {UNSAMPLED}. 손으로 고른 값은 관측 재현(`observed` + `run`)만 받는다")
            elif k != "rule" and k not in RULE_KEYS[rule]:
                errs.append(f"{at}({rule}) 의 키 `{k}` 는 규약 밖이다 — 키는 rule · {' · '.join(RULE_KEYS[rule])} 다")
        errs += check_rule(at, rule, e, keep, root)
    return errs


def check_rule(at: str, rule: str, e: dict, keep: dict, root: Path) -> list[str]:
    """규칙마다 대상 변수의 꼴."""
    errs = []
    if rule in ("equivalence", "boundary", "pairwise"):
        vs = e.get("vars")
        if not isinstance(vs, list) or not vs or any(v not in keep for v in vs):
            return [f"{at}({rule}): `vars` 는 keep 의 변수 목록이다 — 실제 {vs!r}"]
        if rule == "boundary":
            errs += [f"{at}(boundary): 변수 `{v}` 는 범위 변수가 아니다 — 경계값은 `range` 의 양 끝과 바로 안팎이다" for v in vs if "range" not in keep[v]]
        if rule == "pairwise":
            if len(vs) < 2:
                errs.append(f"{at}(pairwise): 변수가 둘 이상이어야 한다 — 조합은 변수 쌍의 값 조합이다")
            errs += [f"{at}(pairwise): 변수 `{v}` 는 열거 변수가 아니다 — 조합의 값은 `values`·`reject` 다" for v in vs if "values" not in keep[v]]
    elif rule == "factor":
        var, factors = e.get("var"), e.get("factors")
        if var not in keep or not isinstance(factors, dict) or not factors:
            return [f"{at}(factor): `var`(keep 의 변수)와 비어 있지 않은 `factors`(요인 → 값)가 있어야 한다"]
        for tag, val in factors.items():
            if not isinstance(tag, str) or not FACTOR_TAG.fullmatch(tag):
                errs.append(f"{at}(factor): 요인 {tag!r} 이 `agt:<이름>` 꼴이 아니다 — 결함 요인 어휘의 개체다")
            elif in_domain(keep[var], val) is not False:
                errs.append(f"{at}(factor): 요인 {tag} 의 값 {val!r} 가 `{var}` 의 keep 밖 정의역 값이 아니다 — 요인 주입은 keep 밖 값이다")
    else:
        run, vals = e.get("run"), e.get("values")
        if not isinstance(run, str) or not run.startswith(RUN_DIR + "/") or not (root / run).is_file():
            errs.append(f"{at}(observed): `run` {run!r} 가 실행 기록(`{RUN_DIR}/…`)이 아니거나 없다 — 관측 재현의 근거는 그 기록이다")
        if not isinstance(vals, dict) or not vals or any(k not in keep for k in vals):
            errs.append(f"{at}(observed): `values` 는 keep 변수 → 값의 비어 있지 않은 매핑이다")
        else:
            errs += [f"{at}(observed): `{k}` 의 값 {v!r} 가 정의역 밖이다" for k, v in vals.items() if in_domain(keep[k], v) is None]
    return errs


def check_case_template(where: str, case, keep: dict) -> list[str]:
    """`case` 템플릿의 형식과 `${변수}` 의 실재."""
    if not isinstance(case, dict):
        return [f"{where}: `case` 는 매핑이다 — 키는 {' · '.join(CASE_KEYS)} 다"]
    errs = [f"{where}: `case` 의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(CASE_KEYS)} 다" for k in case if k not in CASE_KEYS]
    errs += [f"{where}: `case` 에 `{k}` 가 없다" for k in CASE_REQUIRED if not isinstance(case.get(k), str) or not case.get(k).strip()]
    if not str(case.get("criteria", "")).startswith(CHUNK_NS):
        errs.append(f"{where}: `case.criteria` 는 기준 청크 IRI 다 — 케이스는 기준을 `refines` 한다 (p8-pass-criteria)")
    ver = case.get("verifies", [])
    if not isinstance(ver, list) or any(not str(x).startswith(CHUNK_NS) for x in ver):
        errs.append(f"{where}: `case.verifies` 는 청크 IRI 목록이다")
    der = case.get("derivesFrom", [])
    if not isinstance(der, list) or any(not str(x).startswith(CHUNK_NS) for x in der):
        errs.append(f"{where}: `case.derivesFrom` 는 청크 IRI 목록이다")
    files = case.get("files", {})
    if not isinstance(files, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in files.items()):
        errs.append(f"{where}: `case.files` 는 `이름: 내용` 문자열 매핑이다")
    for cls in CLASSES:
        c = case.get(cls)
        if c is None:
            continue
        if not isinstance(c, dict) or set(c) - set(CLASS_KEYS) or not isinstance(c.get("prose"), str) or not isinstance(c.get("expect"), list):
            errs.append(f"{where}: `case.{cls}` 는 {{prose: 문자열, expect: 목록}} 이다")
    used = set(TEMPLATE.findall(json.dumps(case, ensure_ascii=False)))
    errs += [f"{where}: 템플릿의 `${{{u}}}` 가 keep 의 변수가 아니다" for u in sorted(used - set(keep))]
    return errs


# ── 규칙 — 다섯 근거에서 값 배정 ────────────────────

def inside(var: dict, val) -> bool:
    """값이 keep 안인가."""
    if "range" in var:
        return isinstance(val, int) and var["range"][0] <= val <= var["range"][1]
    return str(val) in map(str, var["values"])


def in_domain(var: dict, val):
    """정의역 판정 — True(keep 안) · False(keep 밖 정의역) · None(정의역 밖)."""
    if inside(var, val):
        return True
    if "range" in var:
        lo, hi = var.get("domain", [None, None])
        if not isinstance(val, int) or isinstance(val, bool):
            return None
        return False if lo is None or lo <= val <= hi else None
    return False if str(val) in map(str, var.get("reject", [])) else None


def baseline(keep: dict) -> dict:
    """나머지 변수의 기준값 — 범위 변수는 lo, 열거 변수는 values 의 첫째. 규칙이 건드리지 않는 변수의 값이다."""
    return {k: (v["range"][0] if "range" in v else v["values"][0]) for k, v in keep.items()}


def classes(var: dict) -> list[list]:
    """등가 부류 — 범위 변수는 keep 구간과 `domain` 이 남기는 아래·위 구간, 열거 변수는 keep 값 묶음과 reject 묶음."""
    if "values" in var:
        return [c for c in (list(var["values"]), list(var.get("reject", []))) if c]
    lo, hi = var["range"]
    dlo, dhi = var.get("domain", [lo, hi])
    return [iv for iv in ([dlo, lo - 1], [lo, hi], [hi + 1, dhi]) if iv[0] <= iv[1]]


def boundary_values(var: dict) -> list[int]:
    """각 범위의 양 끝과 바로 안팎 — `domain` 이 있으면 그 밖은 내지 않는다(정의역 밖 값은 케이스가 아니다)."""
    lo, hi = var["range"]
    out = []
    for x in (lo - 1, lo, lo + 1, hi - 1, hi, hi + 1):
        if x not in out and in_domain(var, x) is not None:
            out.append(x)
    return out


def pairwise_rows(keep: dict, vs: list[str]) -> list[dict]:
    """t=2 조합 — 값 곱을 순서대로 훑어 아직 덮이지 않은 쌍을 덮는 행만 고른다(결정론적 탐욕). 모든 쌍이 덮인다."""
    domains = [list(keep[v]["values"]) + list(keep[v].get("reject", [])) for v in vs]
    need = {(i, a, j, b) for i, j in itertools.combinations(range(len(vs)), 2) for a in map(str, domains[i]) for b in map(str, domains[j])}
    rows = []
    for combo in itertools.product(*domains):
        pairs = {(i, str(combo[i]), j, str(combo[j])) for i, j in itertools.combinations(range(len(vs)), 2)}
        if pairs & need:
            need -= pairs
            rows.append(dict(zip(vs, combo)))
        if not need:
            break
    return rows


def assignments(spec: dict) -> list[dict]:
    """cover → [{rule, values, tags, run}] — 항목 순서, 규칙 안 순서대로. 등가분할의 대표값만 seed 의 난수로 고른다."""
    keep, rng, base = spec["keep"], random.Random(spec["seed"]), baseline(spec["keep"])
    out = []
    for e in spec["cover"]:
        rule = e["rule"]
        if rule == "equivalence":
            for v in e["vars"]:
                for cls in classes(keep[v]):
                    pick = rng.randint(cls[0], cls[1]) if "range" in keep[v] else rng.choice(cls)
                    out.append({"rule": rule, "values": {**base, v: pick}})
        elif rule == "boundary":
            out += [{"rule": rule, "values": {**base, v: x}} for v in e["vars"] for x in boundary_values(keep[v])]
        elif rule == "pairwise":
            out += [{"rule": rule, "values": {**base, **row}} for row in pairwise_rows(keep, e["vars"])]
        elif rule == "factor":
            out += [{"rule": rule, "values": {**base, e["var"]: val}, "factor": tag} for tag, val in e["factors"].items()]
        else:
            out.append({"rule": rule, "values": {**base, **e["values"]}, "run": e["run"]})
    return out


# ── 직렬화 — 템플릿 채우기와 실행기가 읽는 펜스 ────────────────────

def fill(text: str, values: dict) -> str:
    """`${변수}` → 값. 변수의 실재는 check_case_template 이 이미 보았다."""
    return TEMPLATE.sub(lambda m: str(values[m.group(1)]), text)


def fill_any(obj, values: dict):
    """템플릿 값 전체(문자열·목록·매핑)에 fill 을 건다."""
    if isinstance(obj, str):
        return fill(obj, values)
    if isinstance(obj, list):
        return [fill_any(x, values) for x in obj]
    if isinstance(obj, dict):
        return {fill(k, values) if isinstance(k, str) else k: fill_any(v, values) for k, v in obj.items()}
    return obj


def yaml_scalar(content: str, indent: str, block: bool) -> list[str]:
    """파일 내용 하나 → `이름:` 뒤의 YAML 값 줄. 줄이 여럿이면 literal 블록, 아니면 큰따옴표 한 줄(p8-machine-readable-case)."""
    if block and "\n" in content.rstrip("\n"):
        head = "|" if content.endswith("\n") and not content.endswith("\n\n") else "|-"
        return [head] + [f"{indent}  {ln}" if ln else "" for ln in content.rstrip("\n").split("\n")]
    return [json.dumps(content, ensure_ascii=False)]


def read_back(lines: list[str]):
    """펜스 줄 → vv_run 이 읽는 값. 펜스 안을 줄바꿈으로만 잇는 것(끝 줄바꿈 없음)이 vv_run.yaml_blocks 의 꼴이다."""
    try:
        return yaml.safe_load("\n".join(lines[1:-1]))
    except yaml.YAMLError:
        return None


def yaml_fence(key: str, value) -> list[str]:
    """`files` 또는 `expect` 펜스 — 손으로 내고 실행기의 꼴로 되읽어 같은지 본다(생성기의 자기 검사).

    literal 블록이 실행기의 읽기에서 내용을 바꾸면(펜스 끝의 줄바꿈이 잘린다) 그 파일만 큰따옴표 한 줄로 다시 낸다.
    """
    if key == "files":
        quoted: set[str] = set()
        for _ in range(2):
            lines = ["```yaml", f"{key}:"]
            for name, content in value.items():
                sc = yaml_scalar(content, "  ", name not in quoted)
                lines += [f"  {name}: {sc[0]}"] + sc[1:]
            lines.append("```")
            back = read_back(lines)
            got = back.get(key, {}) if isinstance(back, dict) and isinstance(back.get(key), dict) else {}
            quoted |= {n for n, c in value.items() if got.get(n) != c}
        want = value
    else:
        lines = ["```yaml", f"{key}:"]
        for e in value:
            lines.append(f"  - exit: {int(e.get('exit', 0))}")
            phrases = vv_run.phrases(e.get("contains"))
            if phrases:
                lines.append("    contains:")
                lines += [f"      - {json.dumps(p, ensure_ascii=False)}" for p in phrases]
        lines.append("```")
        want = [{"exit": int(e.get("exit", 0)), **({"contains": vv_run.phrases(e["contains"])} if e.get("contains") else {})} for e in value]
    if read_back(lines) != {key: want}:
        raise CaseGenError(f"`{key}` 펜스가 실행기의 꼴로 되읽어 같지 않다 — 생성기의 직렬화 결함이다")
    return lines


# ── 조립 — 시나리오 하나에서 케이스 청크들 ────────────────────

def render(sc: dict, a: dict, case: dict, name: str) -> str:
    """값 배정 하나 → 케이스 청크 텍스트. frontmatter 는 현행 케이스의 키 순서를 따른다."""
    keep, vals = sc["spec"]["keep"], a["values"]
    cls = "accept" if all(inside(keep[k], v) for k, v in vals.items()) else "reject"
    tmpl = case.get(cls)
    if tmpl is None:
        raise CaseGenError(f"{sc['path']}: `{name}` 은 `{cls}` 부류인데 `case.{cls}` 가 없다")
    key = json.dumps(vals, sort_keys=True, ensure_ascii=False)
    iri = CHUNK_NS + str(uuid.uuid5(uuid.NAMESPACE_URL, f"{sc['iri']}#case:{key}"))
    fm = ["---", f"id: {iri}", "type: schema", "level: concrete", f"title_ko: {fill(case['title_ko'], vals)}",
          f"title: {fill(case['title'], vals)}", "status: draft", f"sources: {sc['sources']}", f"assumes: {sc['assumes']}",
          f"generated: {{by: {ACTOR}, at: {sc['at']}}}", f"refines: [{case['criteria']}]"]
    if case.get("verifies"):
        fm.append(f"verifies: [{', '.join(case['verifies'])}]")
    derives = [sc["iri"]] + [x for x in dict.fromkeys(case.get("derivesFrom") or []) if x != sc["iri"]]  # 시나리오가 첫째다 — drift 가 첫 출처로 시나리오를 찾는다
    fm += [f"derivesFrom: [{', '.join(derives)}]", "---"]
    body = [f"**케이스** — {fill(case['summary'], vals).strip()}", "", f"**자극** — {fill(case['stimulus'], vals).strip()}", ""]
    files = fill_any(case.get("files") or {}, vals)
    if files:
        body += yaml_fence("files", files) + [""]
    body += [f"**기대** — {fill(tmpl['prose'], vals).strip()}", "", *yaml_fence("expect", fill_any(tmpl["expect"], vals)), ""]
    body += [f"**실행 명령** — `{fill(case['command'], vals).strip()}`", "", provenance(sc, a, cls)]
    return "\n".join(fm + body) + "\n"


def provenance(sc: dict, a: dict, cls: str) -> str:
    """`**표본 근거**` 한 줄 — 근거 태그·seed·시나리오·값·부류. 재생성의 근거가 이 줄과 derivesFrom 이다 (p8-case-generation)."""
    keep = sc["spec"]["keep"]
    tags = list(a["tags"])
    if any(keep[k]["odd"] == ODD_OUTSIDE for k in keep):
        tags.append(ODD_OUTSIDE_TAG)
    vals = " · ".join(f"`{k}={v}`" for k, v in a["values"].items())
    extra = "".join(f" · 요인 `{f}`" for f in a.get("factors", []))
    extra += "".join(f" · 실행 기록 `{r}`" for r in a.get("runs", []))
    side = "keep 안" if cls == "accept" else "keep 밖"
    return (f"**표본 근거** — {' · '.join(f'`{t}`' for t in tags)} · seed `{sc['spec']['seed']}` · 시나리오 `{sc['slug']}`"
            f"{extra}. 값은 {vals}이고 판정 부류는 `{cls}`({side})다.")


def generate(sc: dict, root: Path, odd: set[str]) -> dict[str, str]:
    """시나리오 하나 → {케이스 파일 이름: 텍스트}. 같은 값 배정은 케이스 하나이고 근거 태그를 모은다."""
    spec, where = sc["spec"], str(sc["path"])
    if not isinstance(spec, dict):
        raise CaseGenError(f"{where}: 입력 펜스는 매핑이다 — 키는 {' · '.join(INPUT_KEYS)} 다")
    errs = []
    for k in spec:
        if k == "cases":
            errs.append(f"{where}: `cases` 는 케이스를 손으로 적은 목록이다 — {UNSAMPLED}. 값은 `cover` 의 규칙이 낸다 (p8-case-generation)")
        elif k not in INPUT_KEYS:
            errs.append(f"{where}: 입력 펜스의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(INPUT_KEYS)} 다")
    if not isinstance(spec.get("seed"), int) or isinstance(spec.get("seed"), bool):
        errs.append(f"{where}: `seed` 는 정수다 — 규칙과 seed 가 케이스의 provenance 에 남아야 재생성이 된다")
    kerrs = check_keep(where, spec.get("keep"), odd)
    errs += kerrs
    if not kerrs:
        errs += check_cover(where, spec.get("cover"), spec["keep"], root)
        errs += check_case_template(where, spec.get("case"), spec["keep"])
    if errs:
        raise CaseGenError("\n".join(errs))
    merged: dict[str, dict] = {}
    for a in assignments(spec):
        key = json.dumps(a["values"], sort_keys=True, ensure_ascii=False)
        m = merged.setdefault(key, {"rule": a["rule"], "values": a["values"], "tags": [], "factors": [], "runs": []})
        for t in [RULE_TAGS[a["rule"]]] + ([ORIGIN_OBSERVED] if a["rule"] == "observed" else []):
            if t not in m["tags"]:
                m["tags"].append(t)
        m["factors"] += [a["factor"]] if "factor" in a else []
        m["runs"] += [a["run"]] if "run" in a else []
    out, counts = {}, {}
    for a in merged.values():
        counts[a["rule"]] = counts.get(a["rule"], 0) + 1
        name = f"{sc['slug']}-{a['rule']}-{counts[a['rule']]}.md"
        out[name] = render(sc, a, spec["case"], name)
        errs += [f"{where}: 생성 케이스 `{name}` — {e}" for e in runner_errors(out[name])]
    if errs:
        raise CaseGenError("\n".join(errs))
    return out


def runner_errors(text: str) -> list[str]:
    """생성 케이스를 vv_run 의 파서로 되읽는다 — 실행기가 케이스를 읽는 꼴이 생성 케이스의 출력 꼴이다."""
    body = kb_lib.chunk_body(text)
    line = next((m for ln in body.splitlines() if (m := vv_run.COMMAND_LINE.match(ln.strip()))), None)
    if line is None:
        return ["`**실행 명령**` 줄이 없다 — 실행기가 명령을 찾지 못한다"]
    cmds = [c for c in vv_run.SPLIT.split(line.group(1).strip()) if c]
    spec, errs = vv_run.case_spec(body)
    return errs + vv_run.check_case(spec, cmds)


# ── 실행 — 생성과 드리프트 비교 ────────────────────

def drift(root: Path, cases_dir: Path, scenarios: list[dict], outputs: dict[str, dict[str, str]], all_generated: bool) -> list[str]:
    """트리의 케이스와 생성 결과의 어긋남 — 다른 바이트 · 없는 케이스 · 생성 결과에 없는 생성 케이스 · (선택) 생성기 밖의 케이스."""
    errs = []
    for sc in scenarios:
        made = outputs[sc["slug"]]
        for name, text in made.items():
            p = cases_dir / name
            old = p.read_text(encoding="utf-8") if p.exists() else ""
            if old != text:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), text.splitlines(True), f"{name} (트리)", f"{name} (생성)", n=1))
                errs.append(f"{p.as_posix()}: 시나리오 `{sc['slug']}` 의 생성 결과와 어긋난다 — "
                            f"python3 tools/case_gen.py --scenario {sc['path'].as_posix()} --out {cases_dir.as_posix()} 를 돌려 반영한다 (vnv)")
    by_iri = {sc["iri"]: sc for sc in scenarios}
    for p in sorted(cases_dir.glob("*.md")):
        meta, _ = parse_chunk(str(p))
        gen = meta.get("generated")
        mine = isinstance(gen, dict) and gen.get("by") == ACTOR
        src = [s for s in (meta.get("derivesFrom") or []) if s in by_iri]
        if mine and src and p.name not in outputs[by_iri[src[0]]["slug"]]:
            errs.append(f"{p.as_posix()}: 시나리오 `{by_iri[src[0]]['slug']}` 가 더는 내지 않는 생성 케이스다 — 지운다 (vnv)")
        if all_generated and not mine:
            errs.append(f"{p.as_posix()}: 생성기 밖의 케이스다(generated.by {ACTOR} 아님) — concrete 케이스는 사람이 쓰지 않는다 (p8-case-generation)")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--scenario", action="append", default=[], help="입력 자극 청크(여러 번). 생성 모드에서 없으면 kb/vv/scenario 를 훑는다")
    ap.add_argument("--out", default="", help="생성 케이스를 쓸 디렉토리 — 생성 모드에서 필수")
    ap.add_argument("--check", action="store_true", help="쓰지 않고 --cases 의 트리와 비교. 어긋나면 1")
    ap.add_argument("--cases", default=CASE_DIR, help="--check 의 비교 대상 디렉토리 (--root 기준)")
    ap.add_argument("--all-generated", action="store_true", help="--check 에서 케이스 디렉토리의 모든 케이스가 생성기의 것인지도 본다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root 기준")
    ap.add_argument("--odd", default="", help=f"ODD 문서 — 안 주면 <root>/{ODD_FILE}")
    a = ap.parse_args()
    root = Path(a.root)
    if not a.check and not a.out:
        print(f"FAIL [{GEN}] --out 이 없다 — 생성 케이스를 쓸 디렉토리를 준다(저장소 반영은 vnv 가 `--out {CASE_DIR}` 로 한다)")
        return EXIT_CONFIG
    try:
        apply_plane_level_state(*load_plane_level_state(Path(a.residency) if a.residency else root / "defs" / "kb.bzl"))
        odd = odd_attributes(Path(a.odd) if a.odd else root / ODD_FILE)
        paths = [root / s if not Path(s).is_absolute() and (root / s).exists() else Path(s) for s in a.scenario]
        if not paths and not a.check:
            paths = discover(root)
        scenarios = [load_scenario(p) for p in paths]
        outputs = {sc["slug"]: generate(sc, root, odd) for sc in scenarios}
    except CaseGenError as e:
        for line in str(e).splitlines():
            print(f"FAIL [{GEN}] {line}")
        return EXIT_FAIL
    except ValueError as e:  # parse_chunk 의 frontmatter 규칙 — chunk2kg 의 판정을 생성 시점에 그대로 낸다
        print(f"FAIL [{GEN}] {e}")
        return EXIT_FAIL
    except (OSError, yaml.YAMLError) as e:
        print(f"FAIL [{GEN}] {getattr(e, 'filename', '') or root}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    n = sum(len(v) for v in outputs.values())
    if a.check:
        cases_dir = Path(a.cases) if Path(a.cases).is_absolute() else root / a.cases
        try:
            errs = drift(root, cases_dir, scenarios, outputs, a.all_generated)
        except ValueError as e:
            print(f"FAIL [{DRIFT}] {e}")
            return EXIT_FAIL
        for e in errs:
            print(f"FAIL [{DRIFT}] {e}")
        if errs:
            print(f"\nFAIL [{DRIFT}] — 어긋남 {len(errs)}건 / 시나리오 {len(scenarios)}개 · 생성 케이스 {n}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT}] — " + (f"시나리오 {len(scenarios)}개 · 생성 케이스 {n}개가 트리와 일치" if scenarios else
                                     "대상 시나리오 0개 — 목록이 비어 있어 비교할 생성 결과가 없다")
              + (" · 생성기 밖의 케이스 0" if a.all_generated else ""))
        return EXIT_OK
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for slug, made in outputs.items():
        for name, text in made.items():
            (out / name).write_text(text, encoding="utf-8")
    print(f"생성 {n}개 — 시나리오 {len(scenarios)}개 → {out.as_posix()}"
          + ("" if scenarios else f" (입력 없음: `{SCENARIO_DIR}` 에 keep·cover 펜스를 가진 logical 자극 청크가 없다)"))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
