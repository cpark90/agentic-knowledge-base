#!/usr/bin/env python3
"""청크·명명·산문 린트.

  --chunks <files>   청크 본문(assertion) 파일 검사 (노트 4.1절):
                     본문 42줄 이하. YAML frontmatter(head 메타데이터)와
                     끝의 빈 줄은 본문으로 세지 않는다.
                     .md 청크는 산문 문체(STYLEGUIDE §0 단정 서술형, 2026-09-13)도 본다 — 경어·비격식 종결이 문장 끝에
                     오거나 산문에 느낌표가 있으면 위반(kb_lib.check_prose, 게이트 id `prose`). 코드·따옴표·주석 안과
                     `!=`·`![` 는 산문이 아니다. TTL 청크는 산문 검사 대상이 아니다. 추측·구어는 consistency ⑦ 보고다.
                     type: decision 인 .md 는 역할 표지(STYLEGUIDE §4, 게이트 id `decision-role`)도 본다 — 본문 첫 산문 줄이
                     굵은 표지로 시작해야 한다. conclusion.md·rationale.md·alternatives.md 는 각각 **결론**·**근거**·**대안**,
                     그 밖의 파일명(단일 파일 옛 결정 chunks/decision/d-*.md)은 **결론** 이다. 표지 안의 한정어(**대안 없음**)는
                     같은 표지다(kb_lib.DECISION_ROLE_MARKER). status: deprecated 는 대상이 아니다.
                     살아 있는 .md 청크(status draft·stable·suspect, kb_lib.LIVE_STATES)는 첨가와 목록 규칙도 본다
                     (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-slot-answers-one-question·
                     p4-three-empty-values). 게이트 id 셋은 `addition`(메타 문장 "다음과 같다"·채움 문구 "특이사항 없음"),
                     `empty-value`(세 빈 값 `없음`·`해당 없음`·`미확정` 밖의 `N/A`·`TBD`·`미정`·표의 단독 대시 셀),
                     `list-rules`(손 번호 `2.` 이상·항목 9개 초과·중첩 3단계 이상·항목당 240자 초과·빈 항목)이다.
                     검사 함수는 consistency ⑧·⑨ 와 같다(kb_lib.check_addition·check_lists) — 보고와 게이트의 수치가 갈리지 않는다.
                     살아 있는 type: annotation 인 .md 는 논평이다 (STYLEGUIDE §4, 결정 p7-commentary-form). 게이트 id
                     `blocking-comment` 는 그 결정이 정한 **유일한 게이트 효과**를 강제한다 — 첫 줄이 `issue (blocking)` 이면서
                     `해소: 열림` 인 논평이 있으면 FAIL 이다. 그 밖의 라벨·장식·해소 상태는 기록이고 막지 않는다. 첫 줄 꼴과
                     닫힌 어휘·본문 문장 상한은 shape(kb/ontology/shapes/review-comment-body-shapes.ttl)가 본다.
  --ttl <files>      TTL 파일명이 산출물 접미사 규약(0.2절)을 따르는지 검사.
  --waivers <file>   docs/waivers.md — 게이트 id `prose`·`addition`·`empty-value`·`list-rules`·`blocking-comment`(축 파일)로 면제된 파일의
                     위반은 세지 않는다. 면제된 것은 `WAIVED [<게이트 id>]` 줄로 남긴다 (집계에서 빼되 목록에는 남긴다).
                     없으면 면제 없음.

출력·종료: `FAIL [chunk|naming] <경로>: <메시지>` ·
`FAIL [prose|decision-role|addition|empty-value|list-rules|blocking-comment] <경로>:<줄>: <이유>` + EXIT_FAIL.
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
    from tools.chunk2kg import comment_form  # 논평 본문의 파서 — 방출(chunk2kg)과 게이트가 같은 판정을 쓴다
except ImportError:
    from chunk2kg import comment_form

ALLOWED_TTL_SUFFIXES = kb_lib.ALLOWED_TTL_SUFFIXES
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건
PROSE = kb_lib.PROSE_GATE                        # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
DECISION_ROLE = kb_lib.DECISION_ROLE_GATE        # 결정 역할 표지 게이트 id (STYLEGUIDE §4)
ADDITION = kb_lib.ADDITION_GATE                  # 첨가 게이트 id — 메타 문장·채움 문구 (STYLEGUIDE §0, consistency ⑧)
EMPTY_VALUE = kb_lib.EMPTY_VALUE_GATE            # 빈 값 게이트 id — 세 빈 값 밖의 표기 (STYLEGUIDE §0, consistency ⑧)
LIST_RULES = kb_lib.LIST_RULES_GATE              # 목록 게이트 id — 목록 규칙 다섯 (STYLEGUIDE §0, consistency ⑨)
BLOCKING_COMMENT = kb_lib.BLOCKING_COMMENT_GATE  # 논평 게이트 id — 해소되지 않은 issue (blocking) (STYLEGUIDE §4, p7-commentary-form)

MAX_BODY_LINES = 42  # 4.1절 — 컨텍스트 한계 200줄의 약 1/5

_FM_FIELD = re.compile(r"^(type|status):\s*(\S+)")  # 역할 표지 판정에 필요한 frontmatter 키 둘 — 전체 파싱은 chunk2kg 의 몫


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
    return fields, lines[end + 1 :], end + 2


def check_decision_role(path: Path, text: str) -> list[tuple[int, str]]:
    """결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

    type: decision 인 .md 만 대상이고 status: deprecated 는 제외한다. 본문 첫 산문 줄(빈 줄 제외 첫 줄)이 굵은 표지로 시작해야 하며,
    표지는 파일 stem 이 정한다 — conclusion 결론 · rationale 근거 · alternatives 대안, 그 밖(단일 파일 옛 결정)은 결론.
    굵은 span 이 역할 낱말로 시작하면 한정어가 붙어도 같은 표지다(**대안 없음**·**대안 — 미확정**, kb_lib 주석의 첫 실행 실태).
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "decision" or fields.get("status") == "deprecated":
        return []
    expected = kb_lib.DECISION_ROLE_MARKERS.get(path.stem, kb_lib.DECISION_SINGLE_FILE_MARKER)
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
    """해소되지 않은 `issue (blocking)` 논평 (게이트 id `blocking-comment`) → [(줄 번호, 이유)].

    결정 p7-commentary-form 이 정한 **유일한 게이트 효과**다. `issue (blocking)` 이면서 `해소: 열림` 인 논평만 막고
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
    return [(ln, f'해소되지 않은 `{form["label"]} ({form["decoration"]})` 논평이다 — 대상 {on}, 요지 "{form.get("gist", "")}". '
                 f'대상을 고친 뒤 `해소: {kb_lib.COMMENT_RESOLUTIONS[1]} — <이유>` 로, 받지 않기로 했으면 '
                 f'`해소: {kb_lib.COMMENT_RESOLUTIONS[2]} — <이유>` 로 바꾼다 (p7-commentary-form)')]


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


def body_lines(path: Path, text: str) -> int:
    """본문 줄 수. head에 해당하는 것(md frontmatter, ttl의 @prefix·주석)은 세지 않는다."""
    lines = text.splitlines()
    if path.suffix == ".ttl":
        return sum(
            1
            for l in lines
            if l.strip() and not l.lstrip().startswith(("#", "@prefix", "@base"))
        )
    # 산문 계열: frontmatter 제거
    if lines and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
            lines = lines[end + 1 :]
        except ValueError:
            pass
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return len(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--ttl", nargs="*", default=[])
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help=f"docs/waivers.md — 게이트 id {PROSE}·{ADDITION}·{EMPTY_VALUE}·{LIST_RULES}·{BLOCKING_COMMENT}(축 파일)로 면제된 "
                         "파일의 위반은 세지 않는다. 없으면 면제 없음")
    args = ap.parse_args()

    if not args.chunks and not args.ttl:
        print("SKIP [chunk_lint] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    try:
        waivers = kb_lib.load_waivers(args.waivers) if args.waivers else []
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk_lint] waiver 표 — {e}")
        return EXIT_CONFIG

    errors = []
    waived_notes = []  # 면제된 위반 — 집계에서 빼되 목록에는 남긴다 (docs/waivers.md 머리의 규약, ⑥ 이 선례)
    prose_files = 0
    decision_files = 0  # 역할 표지 검사 대상(살아 있는 결정)의 수 — PASS 줄의 실태
    live_files = 0      # 첨가·목록 검사 대상(살아 있는 .md 청크)의 수
    comment_files = 0   # 논평 검사 대상(살아 있는 annotation 청크)의 수

    for f in args.chunks:
        p = Path(f)
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            print(f"FAIL [chunk] {f}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        n = body_lines(p, text)
        if n > MAX_BODY_LINES:
            errors.append(
                f"[chunk] {f}: 본문 {n}줄 > {MAX_BODY_LINES}줄 — 분할하라 (4.10절 분할 신호)"
            )
        if p.suffix == ".md":  # 산문 문체·결정 역할 표지 — TTL 은 대상이 아니다
            prose_files += 1
            prose_errors, _, _ = kb_lib.check_prose(f, text, waivers)
            errors += [f"[{PROSE}] {f}:{ln}: {reason}" for ln, reason in prose_errors]
            fields, _, _ = split_frontmatter(text)
            if fields.get("type") == "decision" and fields.get("status") != "deprecated":
                decision_files += 1
            errors += [f"[{DECISION_ROLE}] {f}:{ln}: {reason}" for ln, reason in check_decision_role(p, text)]
            if fields.get("type") == "annotation" and fields.get("status") in kb_lib.LIVE_STATES:
                comment_files += 1
            for ln, reason in check_blocking_comment(text):  # 해소되지 않은 issue (blocking) — 논평의 유일한 게이트 효과
                line = f"[{BLOCKING_COMMENT}] {f}:{ln}: {reason}"
                (waived_notes if kb_lib.waived(waivers, BLOCKING_COMMENT, f, "파일") else errors).append(line)
            if fields.get("status") in kb_lib.LIVE_STATES:  # 보고(consistency)와 같은 대상 집합 — invalidated·deprecated 는 기록이다
                live_files += 1
                for gate, ln, reason in check_spec_form(text):
                    line = f"[{gate}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, gate, f, "파일") else errors).append(line)

    for f in args.ttl:
        stem = Path(f).stem
        if not any(stem == s.lstrip("-") or stem.endswith(s) for s in ALLOWED_TTL_SUFFIXES):
            errors.append(
                f"[naming] {f}: 접미사 규약 위반 — {', '.join(ALLOWED_TTL_SUFFIXES)} 중 하나로 끝나야 한다 (0.2절)"
            )

    for w in waived_notes:
        print(f"WAIVED {w} (waivers.md — 집계에서 뺐다)")
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [chunk_lint] — {len(errors)}건 (면제 {len(waived_notes)}건)")
        return EXIT_FAIL

    print(f"PASS [chunk_lint] — 청크 {len(args.chunks)}개 (산문 검사 {prose_files}개, 결정 역할 표지 {decision_files}개, "
          f"첨가·목록 {live_files}개, 논평 {comment_files}개, 면제 {len(waived_notes)}건), TTL {len(args.ttl)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
