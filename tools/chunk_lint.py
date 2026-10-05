#!/usr/bin/env python3
"""청크·명명·산문 린트.

  --chunks <files>   청크 본문(assertion) 파일 검사 (노트 4.1절):
                     본문 1,092 토큰 이하 (게이트 id `chunk`). 단위는 줄이 아니라 **토큰**이고 계수기는
                     `o200k_base`(어휘 파일 sha256 고정)다 — 줄 상한 42·200 은 폐지됐다
                     (결정 p1-chunk-unit-is-tokens, 유저 결정 2026-10-01). YAML frontmatter(head 메타데이터)와
                     앞뒤 빈 줄은 본문이 아니고 본문을 떼는 판정처는 `kb_lib.body_text` 하나다.
                     **상한은 plane 별 프로파일 파라미터**이고 정의처는 `kb_lib.BODY_TOKEN_LIMITS` 하나다 —
                     `artifact`·`memory` 는 2,856 토큰이다(본문이 저작이 아니라 소스·실행의 인용이라 저작 산문의
                     예산이 인위적 분할을 부른다, p7-code-extraction-direction "예산").
                     .md 청크는 산문 문체(STYLEGUIDE §0 단정 서술형, 2026-09-13)도 본다 — 경어·비격식 종결이 문장 끝에
                     오거나 산문에 느낌표가 있으면 위반(kb_lib.check_prose, 게이트 id `prose`). 코드·따옴표·주석 안과
                     `!=`·`![` 는 산문이 아니다. TTL 청크는 산문 검사 대상이 아니다. 추측·구어는 consistency ⑦ 보고다.
                     type: decision 인 .md 는 역할 표지(STYLEGUIDE §4, 게이트 id `decision-role`)도 본다 — 본문 첫 산문 줄이
                     굵은 표지로 시작해야 한다. conclusion.md·rationale.md·alternatives.md 는 각각 **결론**·**근거**·**대안**,
                     선택 넷째 conventions.md 는 **규약**(결정 p4-convention-slot — 이어지는 `규약:` 줄은 목록 항목이 아니다),
                     V&V 시나리오 패키지(kb/vv/scenario)의 `<슬러그>-stimulus.md`·`-factors.md`·`-excluded.md` 는 각각
                     **자극**·**요인**·**배제 자극**(결정 p8-scenario-authoring), 그 밖의 파일명(단일 파일 옛 결정
                     chunks/decision/d-*.md, 단일 청크 시나리오)은 **결론** 이다. 표지 안의 한정어(**대안 없음**)는
                     같은 표지다(kb_lib.DECISION_ROLE_MARKER). status: deprecated 는 대상이 아니다.
                     살아 있는 .md 청크(status draft·stable·suspect, kb_lib.LIVE_STATES)는 첨가와 목록 규칙도 본다
                     (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-slot-answers-one-question·
                     p4-three-empty-values). 게이트 id 셋은 `addition`(메타 문장 "다음과 같다"·채움 문구 "특이사항 없음"),
                     `empty-value`(세 빈 값 `없음`·`해당 없음`·`미확정` 밖의 `N/A`·`TBD`·`미정`·표의 단독 대시 셀),
                     `list-rules`(손 번호 `2.` 이상·항목 9개 초과·중첩 3단계 이상·항목당 240자 초과·빈 항목)이다.
                     검사 함수는 consistency ⑧·⑨ 와 같다(kb_lib.check_addition·check_lists) — 보고와 게이트의 수치가 갈리지 않는다.
                     살아 있는 type: annotation 인 .md 는 주석이다 (STYLEGUIDE §4, 결정 p7-commentary-form). 게이트 id
                     `blocking-comment` 는 그 결정이 정한 **유일한 게이트 효과**를 강제한다 — 첫 줄이 `issue (blocking)` 이면서
                     `해소: 열림` 인 주석이 있으면 FAIL 이다. 그 밖의 라벨·장식·해소 상태는 기록이고 막지 않는다. 첫 줄 꼴과
                     닫힌 어휘·본문 문장 상한은 shape(kb/ontology/shapes/review-comment-body-shapes.ttl)가 본다.
                     `generated.by` 가 `process:judge` 이고 `type: memory` 인 .md 는 **판정 로그**다 (결정
                     p8-judge-calibration-binding). 게이트 id `judge-log` 는 판정만 부르지 않고 로그의 형식만 본다 —
                     판정 표의 헤더가 `kb_lib.JUDGE_LOG_TABLE_HEADER` 와 같고 행마다 질문 id·값·확신도·**판정자 식별자**
                     (세션·모델, 2026-09-30 — 외부 서비스가 아니라 세션 판정자다)·입력 지문(sha256 64자)·시각(ISO 8601 UTC)이
                     비어 있지 않으며 처리가 임계의 세 값 안, `일치` 열이 `일치`·`불일치`·`해당 없음` 셋 안이어야 한다.
                     **판정 로그가 0건이면 거부할 것이 없고 그것은 SKIP 이 아니라 PASS 다** — 로그의 존재를 요구하는
                     것은 이 게이트의 몫이 아니다. 판정 자체는 게이트 밖 도구(`bazel run //tools:judge`)가 한다.
                     살아 있는 .md 청크 본문의 선택 슬롯 `핵심:`(요약 항목)은 **요약 지지 참조** 검사(게이트 id
                     `summary-support`, 2026-09-30, judge-without-service 기계 환원 ①)도 받는다 — 항목마다 `[#id]`·
                     `d-NNNN`·IRI(백틱)·마크다운 링크 중 하나로 본문의 지지 근거를 가리켜야 한다. 슬롯이 없으면 대상이
                     아니다. 오탐 실측(2026-09-30): 저장소가 아직 이 슬롯을 쓰지 않아 0/0 — 사용이 늘면 재실측한다.
  --ttl <files>      TTL 파일명이 산출물 접미사 규약(0.2절)을 따르는지 검사.
  --vocab <file>     토큰 계수기의 어휘 파일. 없으면 runfiles 의 고정 파일을 쓴다 — 해시가 다르면 거부한다.
  --waivers <file>   docs/waivers.md — 게이트 id `chunk`·`prose`·`addition`·`empty-value`·`list-rules`·`blocking-comment`·
                     `judge-log`·`summary-support`(축 파일)로 면제된 파일의 위반은 세지 않는다. 면제된 것은 `WAIVED [<게이트 id>]`
                     줄로 남긴다 (집계에서 빼되 목록에는 남긴다). 없으면 면제 없음.

출력·종료: `FAIL [chunk|naming] <경로>: <메시지>` ·
`FAIL [prose|decision-role|addition|empty-value|list-rules|blocking-comment|judge-log|summary-support] <경로>:<줄>: <이유>` + EXIT_FAIL.
파일 없음·waiver 표 오류는 EXIT_CONFIG, 대상 0건은 EXIT_SKIP (PASS 아님).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from tools import kb_lib  # bazel runfiles 경로
except ImportError:
    import kb_lib  # 직접 실행
try:
    from tools.chunk2kg import comment_form  # 주석 본문의 파서 — 방출(chunk2kg)과 게이트가 같은 판정을 쓴다
except ImportError:
    from chunk2kg import comment_form

ALLOWED_TTL_SUFFIXES = kb_lib.ALLOWED_TTL_SUFFIXES
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건
CHUNK = kb_lib.CHUNK_GATE                        # 본문 토큰 상한 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
PROSE = kb_lib.PROSE_GATE                        # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
DECISION_ROLE = kb_lib.DECISION_ROLE_GATE        # 결정 역할 표지 게이트 id (STYLEGUIDE §4)
ADDITION = kb_lib.ADDITION_GATE                  # 첨가 게이트 id — 메타 문장·채움 문구 (STYLEGUIDE §0, consistency ⑧)
EMPTY_VALUE = kb_lib.EMPTY_VALUE_GATE            # 빈 값 게이트 id — 세 빈 값 밖의 표기 (STYLEGUIDE §0, consistency ⑧)
LIST_RULES = kb_lib.LIST_RULES_GATE              # 목록 게이트 id — 목록 규칙 다섯 (STYLEGUIDE §0, consistency ⑨)
BLOCKING_COMMENT = kb_lib.BLOCKING_COMMENT_GATE  # 주석 게이트 id — 해소되지 않은 issue (blocking) (STYLEGUIDE §4, p7-commentary-form)
JUDGE_LOG = kb_lib.JUDGE_LOG_GATE                # 판정 로그 게이트 id — 로그의 형식·필수 필드 (p8-judge-calibration-binding)
SUMMARY_SUPPORT = kb_lib.SUMMARY_SUPPORT_GATE    # 요약 지지 참조 게이트 id (judge-without-service-2026-09-30 기계 환원 ①)
NAMING = kb_lib.NAMING_GATE                      # TTL 파일 접미사 규약 게이트 id (0.2절)

MAX_BODY_TOKENS = kb_lib.MAX_BODY_TOKENS  # 기본 1,092 토큰 (42×26). plane 별 상한의 정의처는 kb_lib.BODY_TOKEN_LIMITS 다

_FM_FIELD = re.compile(r"^(type|status):\s*(\S+)")  # 역할 표지 판정에 필요한 frontmatter 키 둘 — 전체 파싱은 chunk2kg 의 몫
_FM_GENERATED_BY = re.compile(r"^generated:\s*\{[^}]*?\bby:\s*([^,}\s]+)")  # 생성자 — 판정 로그를 고르는 열쇠 (process:judge)
_CELL_CODE = re.compile(r"^`(.*)`$")  # 표 셀의 코드 스팬 — 값은 그 안이다

# ── 요약 지지 참조 (게이트 id summary-support, judge-without-service-2026-09-30 기계 환원 ①) ──────────────────
# "요약은 집계다" — 요약 블록의 `핵심:` 항목마다 본문의 지지 블록을 가리키는 참조가 있어야 한다(유저 항목이 정의한
# 검사, harness/user/archive/legacy/judge-without-service-2026-09-30.md "요약 — `핵심:` 항목을 지지하는 블록이 있는가"). 이 저장소는
# 아직 `[#id]` 참조 체계를 쓰지 않으므로 참조는 이미 통용되는 셋 중 하나로 받는다 — `[#id]` 앵커, `d-NNNN` 결정
# 식별자(백틱), IRI(백틱), 마크다운 링크. 슬롯이 없는 청크는 검사하지 않는다 — 판정 대상 0건은 PASS 다.
SUMMARY_KEY_MARKER = "핵심:"
SUMMARY_REF_RE = re.compile(r"\[#[^\]]+\]|`(?:d-\d{4}|https?://\S+|agt:\S+)`|\[[^\]]+\]\([^)]+\)")


def check_summary_support(text: str) -> list[tuple[int, str]]:
    """`핵심:` 항목마다 지지 참조가 있는가 (게이트 id `summary-support`) → [(줄 번호, 이유)].

    슬롯은 선택이다 — `미확정:`과 같은 자리 규약(줄 머리 `핵심:`)으로 열리고, 그 뒤 이어지는 목록 항목이 대상이다.
    항목이 다른 슬롯 표지·산문으로 넘어가면 블록이 끝난다. 참조가 하나도 없는 항목만 위반이다.
    """
    fields, body, start = split_frontmatter(text)
    out: list[tuple[int, str]] = []
    in_block = False
    for i, line in enumerate(body):
        s = line.strip()
        if s == SUMMARY_KEY_MARKER or s.startswith(SUMMARY_KEY_MARKER + " "):
            in_block = True
            continue
        if not in_block:
            continue
        if not s:
            continue
        if s.startswith("- "):
            item = s[2:].strip()
            if not SUMMARY_REF_RE.search(item):
                out.append((start + i, f'`핵심:` 항목이 지지 참조가 없다 — "{item}". `[#id]`·`d-NNNN`·IRI(백틱)·'
                                       '마크다운 링크 중 하나로 본문의 지지 블록을 가리킨다 (요약은 집계다, judge-without-service-2026-09-30)'))
            continue
        in_block = False
    return out


def split_frontmatter(text: str) -> tuple[dict[str, str], list[str], int]:
    """(frontmatter 의 type·status, 본문 줄들, 본문 첫 줄의 파일 줄 번호). frontmatter 가 없으면 본문은 전체다."""
    lines = text.splitlines()
    fields: dict[str, str] = {}
    if not lines or lines[0].strip() != "---":
        return fields, lines, 1
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return fields, lines, 1
    for raw in lines[1:end]:
        m = _FM_FIELD.match(raw)
        if m:
            fields[m.group(1)] = m.group(2)
        m = _FM_GENERATED_BY.match(raw)
        if m:
            fields["generated.by"] = m.group(1)
    return fields, lines[end + 1 :], end + 2


def check_decision_role(path: Path, text: str) -> list[tuple[int, str]]:
    """결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

    type: decision 인 .md 만 대상이고 status: deprecated 는 제외한다. 본문 첫 산문 줄(빈 줄 제외 첫 줄)이 굵은 표지로 시작해야 하며,
    표지는 파일 경로가 정한다(kb_lib.decision_role_marker) — conclusion 결론 · rationale 근거 · alternatives 대안,
    V&V 시나리오 패키지의 `-stimulus`·`-factors`·`-excluded` 가 자극·요인·배제 자극, 그 밖(단일 파일 옛 결정·단일 청크
    시나리오)은 결론이다. 굵은 span 이 역할 낱말로 시작하면 한정어가 붙어도 같은 표지다(**대안 없음**·**대안 — 미확정**,
    kb_lib 주석의 첫 실행 실태).
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "decision" or fields.get("status") == "deprecated":
        return []
    expected = kb_lib.decision_role_marker(path)
    for offset, line in enumerate(body):
        if not line.strip():
            continue
        m = kb_lib.DECISION_ROLE_MARKER.match(line)
        if m and m.group(1) == expected:
            return []
        found = f'"**{m.group(1)}…**"' if m else f"{line.strip()[:40]!r}"
        return [(start + offset, f"본문 첫 산문 줄이 **{expected}** 표지로 시작해야 한다 (STYLEGUIDE §4 역할 태그) — 실제 {found}")]
    return [(start, f"본문이 비어 **{expected}** 표지가 없다 (STYLEGUIDE §4)")]


def check_blocking_comment(text: str) -> list[tuple[int, str]]:
    """해소되지 않은 `issue (blocking)` 주석 (게이트 id `blocking-comment`) → [(줄 번호, 이유)].

    결정 p7-commentary-form 이 정한 **유일한 게이트 효과**다. `issue (blocking)` 이면서 `해소: 열림` 인 주석만 막고
    나머지 라벨·장식·해소 상태는 기록이라 막지 않는다. 판정은 해소 상태의 존재만 보고 이유의 내용을 보지 않는다
    (p5-verification-tools-per-plane). 첫 줄 꼴과 닫힌 어휘 자체는 shape(review-comment-body-shapes.ttl)가 본다.
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "annotation" or fields.get("status") not in kb_lib.LIVE_STATES:
        return []
    form = comment_form(body)
    if (form.get("label"), form.get("decoration")) != kb_lib.COMMENT_BLOCKING or form.get("resolution") != kb_lib.COMMENT_OPEN:
        return []
    ln = start + next((i for i, l in enumerate(body) if l.strip()), 0)
    on = " · ".join(form.get("targets") or []) or kb_lib.EMPTY_UNDECIDED
    return [(ln, f'해소되지 않은 `{form["label"]} ({form["decoration"]})` 주석이다 — 대상 {on}, 요지 "{form.get("gist", "")}". '
                 f'대상을 고친 뒤 `해소: {kb_lib.COMMENT_RESOLUTIONS[1]} — <이유>` 로, 받지 않기로 했으면 '
                 f'`해소: {kb_lib.COMMENT_RESOLUTIONS[2]} — <이유>` 로 바꾼다 (p7-commentary-form)')]


# ── 판정 로그·명세 형식·줄 수와 실행 ────────────────────

def is_judge_log(fields: dict[str, str]) -> bool:
    """판정 로그인가 — 생성자가 판정자이고 plane 이 memory 인 청크 (kb/vv/run/judge-<UTC>.md).

    같은 생성자의 결과 주석(type: annotation)은 논평이라 대상이 아니다 — 그쪽은 review-comment-body-shapes 가 본다.
    """
    return fields.get("generated.by") == kb_lib.JUDGE_GENERATOR and fields.get("type") == "memory"


def check_judge_log(text: str) -> list[tuple[int, str]]:
    """판정 로그의 형식과 필수 필드 (게이트 id `judge-log`) → [(줄 번호, 이유)].

    게이트는 판정을 부르지 않고 로그만 본다 (결정 p8-judge-calibration-binding). 판정 표의 열이 곧 필수 필드이므로
    헤더가 `kb_lib.JUDGE_LOG_TABLE_HEADER` 와 글자까지 같아야 하고, 행마다 질문 id·값·확신도·판정자 식별자(세션·모델,
    2026-09-30)·입력 지문·시각이 비어 있지 않아야 한다. 확신도는 0 이상 1 이하, 입력 지문은 sha256 64자, 시각은
    ISO 8601 UTC, 처리는 임계가 가르는 세 값 중 하나, `일치`는 일치·불일치·해당 없음 중 하나다. **판정 로그가 0건이면
    이 검사는 아무 것도 거부하지 않는다** — 검사 대상 없음은 SKIP 이 아니라 PASS 다 (로그의 존재를 강제하는 것은
    이 게이트의 몫이 아니다).
    """
    fields, body, start = split_frontmatter(text)
    if not is_judge_log(fields):
        return []
    header = kb_lib.JUDGE_LOG_TABLE_HEADER
    cols = [c.strip() for c in header.split("|")[1:-1]]
    idx = next((i for i, l in enumerate(body) if l.strip().startswith("| ")), None)
    if idx is None or body[idx].strip() != header:
        found = body[idx].strip() if idx is not None else "표 없음"
        return [(start + (idx or 0), f"판정 표의 헤더가 `{header}` 여야 한다 — 열이 곧 필수 필드다"
                                     f"(필수 {' · '.join(kb_lib.JUDGE_LOG_FIELDS)}). 실제 `{found}` "
                                     "(p8-judge-calibration-binding)")]
    errors, rows = [], 0
    for offset, line in enumerate(body[idx + 2 :], start=idx + 2):
        s = line.strip()
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.split("|")[1:-1]]
        ln = start + offset
        if len(cells) != len(cols):
            errors.append((ln, f"판정 행의 칸이 {len(cells)}개다 — 헤더와 같은 {len(cols)}개여야 한다"))
            continue
        row = dict(zip(cols, cells))
        rows += 1
        for field in kb_lib.JUDGE_LOG_FIELDS:
            bare = _CELL_CODE.sub(r"\1", row[field]).strip()
            if not bare or bare in kb_lib.EMPTY_VALUE:
                errors.append((ln, f"필수 필드 `{field}` 가 비어 있다 — 판정 로그는 여섯을 전부 적는다 "
                                   "(p8-judge-calibration-binding)"))
        conf = _CELL_CODE.sub(r"\1", row["확신도"]).strip()
        if not kb_lib.JUDGE_CONFIDENCE.match(conf):
            errors.append((ln, f"확신도 `{conf}` 가 0 이상 1 이하의 십진 표기가 아니다 — 확신도는 확률이다"))
        fp = _CELL_CODE.sub(r"\1", row["입력 지문"]).strip()
        if not kb_lib.JUDGE_FINGERPRINT.match(fp):
            errors.append((ln, f"입력 지문 `{fp[:20]}` 이 sha256(소문자 16진 64자)이 아니다 — 지문이 없으면 "
                               "같은 입력에 같은 답이 나왔는지 대조할 수 없다"))
        at = _CELL_CODE.sub(r"\1", row["시각"]).strip()
        if not kb_lib.GENDOC_TIME_RE.match(at):
            errors.append((ln, f"시각 `{at}` 이 ISO 8601 UTC 초 해상도(`{kb_lib.GENDOC_TIME_FORMAT}`)가 아니다"))
        if row["처리"] not in kb_lib.JUDGE_ROUTES:
            errors.append((ln, f"처리 `{row['처리']}` 가 {' · '.join(kb_lib.JUDGE_ROUTES)} 밖이다 — "
                               "구간별 정확도를 재기 전에는 전부 사람 확인 큐다 (규칙 ②)"))
        if row["일치"] not in kb_lib.JUDGE_AGREEMENT:
            errors.append((ln, f"일치 `{row['일치']}` 가 {' · '.join(kb_lib.JUDGE_AGREEMENT)} 밖이다 — "
                               "판정자 둘 이상이 같은 (질문·지문)에 답했을 때만 일치·불일치이고 단독이면 해당 없음이다"))
    if not rows:
        errors.append((start + idx, "판정 표에 행이 없다 — 판정 하나도 없는 로그는 로그가 아니다"))
    return errors


def check_spec_form(text: str) -> list[tuple[str, int, str]]:
    """첨가와 목록 규칙 (STYLEGUIDE §0, 결정 p4-slot-answers-one-question·p4-three-empty-values) → [(게이트 id, 줄 번호, 이유)].

    판정은 consistency ⑧·⑨ 와 같은 함수(kb_lib.check_addition·check_lists)가 한다. 여기서 하는 것은 게이트 id 를 붙이고
    메시지의 인용을 수정 방향으로 만드는 일뿐이다 — 검사를 복제하지 않는다 (STYLEGUIDE §7 단일 정의처).
    """
    meta, filler, empty = kb_lib.check_addition(text)
    out = [(ADDITION, ln, f'메타 문장 "{expr}" — 슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다 (STYLEGUIDE §0): {quote}')
           for ln, expr, quote in meta]
    out += [(ADDITION, ln, f'채움 문구 "{expr}" — 채움 자리에는 세 빈 값 중 하나를 쓰거나 실질 답을 적는다 (STYLEGUIDE §0): {quote}')
            for ln, expr, quote in filler]
    out += [(EMPTY_VALUE, ln, f'빈 값 표기 "{expr}" — 빈 자리는 `{"` · `".join(kb_lib.EMPTY_VALUE)}` 셋으로만 적는다 (STYLEGUIDE §0): {quote}')
            for ln, expr, quote in empty]
    out += [(LIST_RULES, ln, why) for ln, why in kb_lib.check_lists(text)]
    return sorted(out, key=lambda t: (t[1], t[0]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--ttl", nargs="*", default=[])
    ap.add_argument("--vocab", default="", metavar="FILE",
                    help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help=f"docs/waivers.md — 게이트 id {CHUNK}·{PROSE}·{ADDITION}·{EMPTY_VALUE}·{LIST_RULES}·{BLOCKING_COMMENT}·"
                         f"{JUDGE_LOG}·{SUMMARY_SUPPORT}(축 파일)로 면제된 파일의 위반은 세지 않는다. 없으면 면제 없음")
    args = ap.parse_args()

    if not args.chunks and not args.ttl:
        print("SKIP [chunk_lint] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    try:
        waivers = kb_lib.load_waivers(args.waivers) if args.waivers else []
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk_lint] waiver 표 — {e}")
        return EXIT_CONFIG

    try:  # 어휘는 한 번만 적재한다 — 크기 판정이 이 계수기 하나로 재현된다 (ODD id:cond-tokenizer-lock)
        enc = kb_lib.load_tokenizer(args.vocab or None)
    except FileNotFoundError as e:
        print(f"FAIL [chunk_lint] 어휘 파일 — {e}")
        return EXIT_CONFIG
    except ValueError as e:  # 해시가 고정값과 다르다 — 계수기가 재현되지 않는다
        print(f"FAIL [{CHUNK}] {e}")
        return EXIT_FAIL

    errors = []
    waived_notes = []  # 면제된 위반 — 집계에서 빼되 목록에는 남긴다 (docs/waivers.md 머리의 규약, ⑥ 이 선례)
    prose_files = 0
    decision_files = 0  # 역할 표지 검사 대상(살아 있는 결정)의 수 — PASS 줄의 실태
    live_files = 0      # 첨가·목록 검사 대상(살아 있는 .md 청크)의 수
    comment_files = 0   # 주석 검사 대상(살아 있는 annotation 청크)의 수
    judge_logs = 0      # 판정 로그 검사 대상의 수 — 0 이면 거부할 것이 없고 그것은 SKIP 이 아니라 PASS 다
    summary_files = 0   # 요약 지지 참조 검사 대상(`핵심:` 슬롯을 쓴 살아 있는 청크)의 수

    for f in args.chunks:
        p = Path(f)
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            print(f"FAIL [{CHUNK}] {f}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        n = kb_lib.token_count(kb_lib.body_text(p, text), enc)
        plane = split_frontmatter(text)[0].get("type") if p.suffix == ".md" else None
        limit = kb_lib.body_token_limit(plane)  # plane 별 프로파일 파라미터 — 정의처는 kb_lib.BODY_TOKEN_LIMITS 하나다
        if n > limit:
            line = (
                f"[{CHUNK}] {f}: 본문 {n}토큰 > {limit}토큰 — 분할하라 (4.10절 분할 신호"
                + (f"; plane {plane} 의 상한은 프로파일 파라미터다 — kb_lib.BODY_TOKEN_LIMITS)" if limit != MAX_BODY_TOKENS else ")")
            )
            (waived_notes if kb_lib.waived(waivers, CHUNK, f, "파일") else errors).append(line)
        if p.suffix == ".md":  # 산문 문체·결정 역할 표지 — TTL 은 대상이 아니다
            prose_files += 1
            prose_errors, _, _ = kb_lib.check_prose(f, text, waivers)
            errors += [f"[{PROSE}] {f}:{ln}: {reason}" for ln, reason in prose_errors]
            fields, _, _ = split_frontmatter(text)
            if fields.get("type") == "decision" and fields.get("status") != "deprecated":
                decision_files += 1
            errors += [f"[{DECISION_ROLE}] {f}:{ln}: {reason}" for ln, reason in check_decision_role(p, text)]
            if is_judge_log(fields):  # 판정 로그 — 게이트는 판정을 부르지 않고 로그의 형식만 본다
                judge_logs += 1
                for ln, reason in check_judge_log(text):
                    line = f"[{JUDGE_LOG}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, JUDGE_LOG, f, "파일") else errors).append(line)
            if fields.get("type") == "annotation" and fields.get("status") in kb_lib.LIVE_STATES:
                comment_files += 1
            for ln, reason in check_blocking_comment(text):  # 해소되지 않은 issue (blocking) — 주석의 유일한 게이트 효과
                line = f"[{BLOCKING_COMMENT}] {f}:{ln}: {reason}"
                (waived_notes if kb_lib.waived(waivers, BLOCKING_COMMENT, f, "파일") else errors).append(line)
            if fields.get("status") in kb_lib.LIVE_STATES:  # 보고(consistency)와 같은 대상 집합 — invalidated·deprecated 는 기록이다
                live_files += 1
                for gate, ln, reason in check_spec_form(text):
                    line = f"[{gate}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, gate, f, "파일") else errors).append(line)
                if any(l.strip() == SUMMARY_KEY_MARKER or l.strip().startswith(SUMMARY_KEY_MARKER + " ")
                       for l in text.splitlines()):
                    summary_files += 1
                for ln, reason in check_summary_support(text):
                    line = f"[{SUMMARY_SUPPORT}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, SUMMARY_SUPPORT, f, "파일") else errors).append(line)

    for f in args.ttl:
        stem = Path(f).stem
        if not any(stem == s.lstrip("-") or stem.endswith(s) for s in ALLOWED_TTL_SUFFIXES):
            errors.append(
                f"[{NAMING}] {f}: 접미사 규약 위반 — {', '.join(ALLOWED_TTL_SUFFIXES)} 중 하나로 끝나야 한다 (0.2절)"
            )

    for w in waived_notes:
        print(f"WAIVED {w} (waivers.md — 집계에서 뺐다)")
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [chunk_lint] — {len(errors)}건 (면제 {len(waived_notes)}건)")
        return EXIT_FAIL

    print(f"PASS [chunk_lint] — 청크 {len(args.chunks)}개 (산문 검사 {prose_files}개, 결정 역할 표지 {decision_files}개, "
          f"첨가·목록 {live_files}개, 주석 {comment_files}개, 판정 로그 {judge_logs}개, 요약 지지 참조 {summary_files}개, "
          f"면제 {len(waived_notes)}건), TTL {len(args.ttl)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
