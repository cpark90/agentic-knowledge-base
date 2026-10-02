#!/usr/bin/env python3
"""토큰 계수기 — 청크 본문의 토큰 수 분포를 고정된 공개 토크나이저로 낸다 (결정 p1-chunk-unit-is-tokens).

크기의 단위는 줄이 아니라 토큰이다(유저 결정 2026-10-01). 상한의 숫자는 실측이 정했고 이 도구가 그 실측을
낸다 — plane 별 분포, 42의 배수마다 초과 청크 수와 비율, 컨텍스트 예산의 환산, 상위 20 청크. 게이트가 아니라
뷰다: 상한의 강제는 `chunk_lint`(게이트 id `chunk`)와 shape(`token-budget`)의 몫이고 이 도구는 분할 대상을
고르는 자리다. 계수기는 `kb_lib.load_tokenizer`(tiktoken o200k_base, 어휘 파일 sha256 고정)이고 네트워크를
쓰지 않는다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나이므로 게이트와 이 도구가 같은 문자열을 센다.
출력은 생성 문서 규약(G1~G18)을 따르며 생성 시각을 적지 않는다 — 같은 입력에서 같은 바이트가 나와야 한다.
사용: bazel run //tools:tokens -- [청크 파일…] [--out report.md] [--vocab <어휘 파일>]
출력·종료: 어휘 파일의 해시가 고정값과 다르면 `FAIL [tokens] …` EXIT_FAIL, 읽을 수 없는 입력·어휘 파일
부재는 EXIT_CONFIG, 검사 대상 0건은 SKIP 이다.
"""
from __future__ import annotations

import argparse
import os
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import chunk_lint, kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import chunk_lint  # 직접 실행: 스크립트 디렉토리 기준
    import kb_lib

EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
GATE = kb_lib.TOKENS_TAG  # 보고 접두 — 이 도구는 게이트 타깃이 아니다 (상한의 강제는 chunk_lint·token-budget 이다)
CHUNK_ROOTS = ("chunks", "kb/dev", "kb/vv", "kb/ontology", "space")  # 인자가 없을 때 훑는 자리 — 청크가 사는 디렉토리
# 온톨로지 모듈과 shape 은 `.ttl` 청크다 — 같은 크기 규칙을 받으므로(chunk_lint 가 `--chunks` 로 받는다)
# 실측의 분모도 그것을 담아야 한다 (2026-10-01 정정: `.md` 만 훑어 TTL 청크 78개가 분모에서 빠져 있었다).
# TTL 청크의 판별은 접미사 규약이고 정의처는 `kb_lib.ALLOWED_TTL_SUFFIXES` 의 저작 접미 둘이다 — `-kg`·`-odd`·
# `-space` 는 생성물이라 청크가 아니다.
TTL_CHUNK_SUFFIXES = ("-ontology", "-rules", "-shapes")
MULTIPLES = 20          # 42의 배수를 몇 개까지 보는가 — 42×1 … 42×20
LINE_BUDGET_LINES = 200  # 환산의 분모가 된 옛 예산의 줄 수 (d-0002 "42줄은 200줄의 1/5") — 지금 예산은 토큰이다
BUDGET_PLANES = ("requirement", "decision")  # 줄당 토큰의 표본 — 저작된 산문의 plane 이다
VIEW_PLANES = 5  # 조망 단위 — 한 번에 4~5개를 조망한다 (노트 949행). 예산 ÷ 이 수가 상한의 한 근거다
TOP_N = 20


# ── 청크 적재와 계수 ────────────────────

def discover(root: Path) -> list[Path]:
    """인자가 없을 때의 대상 — 청크 디렉토리의 frontmatter 있는 `.md` 와 저작 접미의 `.ttl` 전부다 (경로 정렬).

    분모는 **게이트가 판정하는 전 청크**여야 한다 — `chunk_lint` 는 `.md` 와 `.ttl` 을 같은 상한으로 보므로
    온톨로지 모듈·shape 도 여기 든다 (2026-10-01 정정).
    """
    out = []
    for d in CHUNK_ROOTS:
        for p in sorted((root / d).rglob("*.md")):
            if p.read_text(encoding="utf-8").startswith("---\n"):
                out.append(p)
        for p in sorted((root / d).rglob("*.ttl")):
            if p.stem.endswith(TTL_CHUNK_SUFFIXES):
                out.append(p)
    return sorted(out, key=lambda p: p.as_posix())


def measure(paths: list[Path], root: Path, enc) -> list[dict]:
    """청크마다 (경로, plane, 줄 수, 토큰 수) 한 행.

    본문은 `kb_lib.body_text` 가 뗀다 — 게이트(`chunk_lint`)·방출(`chunk2kg`)과 같은 판정처 하나다. 줄 수는
    그 문자열의 줄 수이고 분포에서 줄당 토큰의 분모로만 쓰인다(크기 규칙은 토큰이다).
    """
    rows = []
    for p in paths:
        text = p.read_text(encoding="utf-8")
        body = kb_lib.body_text(p, text)
        rel = p.relative_to(root).as_posix() if p.is_absolute() else p.as_posix()
        plane = chunk_lint.split_frontmatter(text)[0].get("type", kb_lib.NONE_MARK)
        rows.append({"path": rel, "plane": plane, "lines": len(body.splitlines()),
                     "tokens": len(enc.encode(body))})
    return rows


def quantiles(values: list[int]) -> tuple[int, int, int, int, int]:
    """(최소, 1사분위, 중앙, 3사분위, 최대) — 표본이 하나여도 다섯 값을 낸다."""
    s = sorted(values)
    if len(s) == 1:
        return (s[0],) * 5
    q1, _, q3 = statistics.quantiles(s, n=4, method="inclusive")
    return s[0], round(q1), round(statistics.median(s)), round(q3), s[-1]


# ── 보고 ────────────────────

def plane_table(rows: list[dict]) -> list[str]:
    """plane 별 분포 — 청크 수·최소·1사분위·중앙·3사분위·최대·줄당 토큰 중앙값."""
    out = ["| plane | 청크 | 최소 | 1사분위 | 중앙 | 3사분위 | 최대 | 줄당 토큰 중앙 |", "|---|---|---|---|---|---|---|---|"]
    groups = {}
    for r in rows:
        groups.setdefault(r["plane"], []).append(r)
    for plane in sorted(groups) + ["전체"]:
        g = rows if plane == "전체" else groups[plane]
        lo, q1, med, q3, hi = quantiles([r["tokens"] for r in g])
        per = statistics.median([r["tokens"] / r["lines"] for r in g if r["lines"]])
        out.append(f"| {plane} | {len(g)} | {lo} | {q1} | {med} | {q3} | {hi} | {per:.1f} |")
    return out + [""]


def multiple_table(rows: list[dict]) -> list[str]:
    """42의 배수마다 초과 청크 수와 비율 — 상한을 그 값으로 두면 몇 개를 쪼개야 하는가다."""
    n = len(rows)
    tokens = [r["tokens"] for r in rows]
    out = ["| 상한 | 배수 | 초과 청크 | 비율 |", "|---|---|---|---|"]  # 확정 상한은 42×26 과 42×68 이다
    for k in range(1, MULTIPLES + 1):
        limit = kb_lib.TOKEN_LIMIT_MULTIPLE * k
        over = sum(1 for t in tokens if t > limit)
        out.append(f"| {limit} | 42×{k} | {over} | {over}/{n} = {over / n:.1%} |")
    return out + [""]


def budget_lines(rows: list[dict]) -> list[str]:
    """예산 200줄의 토큰 환산 — 저작된 산문(요구·결정)의 줄당 토큰 중앙값 × 200 이다."""
    sample = [r for r in rows if r["plane"] in BUDGET_PLANES and r["lines"]]
    per = statistics.median([r["tokens"] / r["lines"] for r in sample])
    budget = round(per * LINE_BUDGET_LINES)
    share = budget / VIEW_PLANES
    near = max(1, round(share / kb_lib.TOKEN_LIMIT_MULTIPLE))
    pooled = sum(r["tokens"] for r in sample) / sum(r["lines"] for r in sample)
    return [f"- 표본: {' · '.join(BUDGET_PLANES)} plane 의 청크 {len(sample)}개 — 저작된 산문이다",
            f"- 줄당 토큰 중앙값: {per:.2f}",
            f"- 표본 전체의 토큰 합 ÷ 줄 합: {pooled:.2f} — 중앙값과 갈리면 긴 청크가 끌어올린 값이다",
            f"- 예산 {LINE_BUDGET_LINES}줄의 토큰 환산: {budget}",
            f"- 조망 {VIEW_PLANES}개로 나눈 값: {share:.0f} — 가장 가까운 42의 배수는 "
            f"42×{near} = {kb_lib.TOKEN_LIMIT_MULTIPLE * near}", ""]


def top_table(rows: list[dict]) -> list[str]:
    """토큰 수 상위 청크 — 분할의 첫 대상이다."""
    out = ["| 토큰 | 줄 | plane | 청크 |", "|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (-r["tokens"], r["path"]))[:TOP_N]:
        out.append(f"| {r['tokens']} | {r['lines']} | {r['plane']} | `{r['path']}` |")
    return out + [""]


def render(rows: list[dict], inputs: list[Path], vocab: Path) -> str:
    """보고 전체 — 생성 문서 규약의 머리 블록 + 네 절이다."""
    head = kb_lib.gendoc_header(
        "tokens", "청크 본문의 토큰 수 분포", "tools/tokens.py",
        f"청크 {len(rows)}개의 본문을 고정된 어휘 `{kb_lib.TOKENIZER_NAME}` 로 세면 분포와 42의 배수별 초과 수가 얼마인가",
        "bazel run //tools:tokens", [], f"청크 {len(rows)}개",
        kb_lib.gendoc_view_notice("각 청크의 본문") + " " + kb_lib.GENDOC_DETERMINISTIC_NOTE,
        input_kind="청크 파일", stamped=False,
        input_note=f"청크 디렉토리 {len(CHUNK_ROOTS)}개: "
                   f"{' · '.join('`' + d + '/`' for d in CHUNK_ROOTS)} 의 frontmatter 있는 `.md` 와 저작 접미"
                   f"({' · '.join('`' + s + '`' for s in TTL_CHUNK_SUFFIXES)})의 `.ttl` 전부 — 분모는 게이트가 "
                   f"판정하는 전 청크다 (2026-10-01 정정: `kb/ontology/` 의 TTL 청크가 빠져 있었다)",
        extra=[f"- 계수기: `{kb_lib.TOKENIZER_PACKAGE} {kb_lib.TOKENIZER_PACKAGE_VERSION}` · 어휘 "
               f"`{kb_lib.TOKENIZER_NAME}` · 어휘 지문 `sha256:{kb_lib.TOKENIZER_VOCAB_SHA256[:12]}` "
               f"(고정처는 `MODULE.bazel` 의 `http_file({kb_lib.TOKENIZER_VOCAB_REPO})`)",
               f"- 입력 지문: `{kb_lib.input_fingerprint(inputs)}`"])
    body = ["## plane 별 분포", "",
            f"단위는 토큰이다. 줄 수는 같은 본문에서 센 값이고 둘의 비가 줄당 토큰이다. `.ttl` 청크는 plane 이 "
            f"없어 `{kb_lib.NONE_MARK}` 행이고 기본 상한 {kb_lib.MAX_BODY_TOKENS} 를 받는다.", ""]
    body += plane_table(rows)
    body += ["## 42의 배수별 초과", "",
             f"상한을 42의 배수로 두면(유저 결정 2026-10-01) 그 값마다 초과 청크가 분할 대상이다. 분모는 청크 {len(rows)}개다.", ""]
    body += multiple_table(rows)
    body += ["## 컨텍스트 예산의 환산", "",
             f"42줄의 근거는 컨텍스트 예산의 1/5 이었다(d-0002). 그 근거를 토큰으로 옮긴 값이 확정 상한 "
             f"{kb_lib.MAX_BODY_TOKENS}(42×26)이고 예산은 {kb_lib.CONTEXT_TOKEN_BUDGET}(42×129)이다 "
             f"(p1-chunk-unit-is-tokens). 아래는 그 환산을 지금 입력에서 다시 잰 것이다.", ""]
    body += budget_lines(rows)
    body += [f"## 상위 {TOP_N} 청크", ""]
    body += top_table(rows)
    return kb_lib.gendoc_assemble(head, body, [], input_kind="청크 파일")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chunks", nargs="*", help="청크 파일. 없으면 청크 디렉토리 전부를 훑는다")
    ap.add_argument("--vocab", default="", help="어휘 파일 경로. 없으면 runfiles 의 고정 파일을 쓴다")
    ap.add_argument("--out", default="", help="보고를 쓸 경로")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    try:
        vocab = kb_lib.tokenizer_vocab_path(a.vocab or None)
        enc = kb_lib.load_tokenizer(vocab)
    except FileNotFoundError as e:
        print(f"FAIL [{GATE}] 어휘 파일 — {e}")
        return EXIT_CONFIG
    except ValueError as e:
        print(f"FAIL [{GATE}] {e}")
        return EXIT_FAIL
    try:
        paths = [Path(c) for c in a.chunks] if a.chunks else discover(root)
        rows = measure(paths, root, enc)
    except OSError as e:
        print(f"FAIL [{GATE}] 입력 — 읽을 수 없다: {e}")
        return EXIT_CONFIG
    if not rows:
        print(f"SKIP [{GATE}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP
    text = render(rows, paths, vocab)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
