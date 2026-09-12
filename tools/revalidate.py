#!/usr/bin/env python3
"""재검증 후보 — 본문 해시가 바뀐 청크의 링크와 하류 의존자를 재판정 대상으로 보고한다 (dependency-graph-design §5, method §7).

본문(frontmatter 제외)의 contentHash 가 base 리비전과 다르면 그 IRI 에 붙은 링크는 suspect 후보이고 재검증 시점에서
재판정한다 — 링크 부패 규칙(p10 link decay)의 첫 형태. 해시는 tools/chunk2kg.py 의 parse_chunk 를 그대로 써서
head 그래프의 agt:contentHash 와 같다. 재판정 대상은 둘을 합친다:
  (a) frontmatter 링크의 상대 — refines·serves·supersedes·verifies·assumes·part_of (+ satisfies·constrains·derivesFrom·allocates·coUpdatesWith), 양방향
  (b) Bazel 하류 의존자 — bazel query rdeps(<universe>, <타깃>) 의 kb_chunk·kb_decision (직접 / 전이)
git 과 bazel query 를 부르므로 odd_check 처럼 테스트 타깃이 아니다. 판정은 사람/승인된 판정자의 몫이다.

사용: bazel run //tools:revalidate -- [--base HEAD] [--universe '//...'] [--out report.md]
종료: 0 = 변경 없음(재판정 대상 없음), 1 = 재판정 대상 있음
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import parse_chunk  # noqa: E402

CHUNK_DIRS = ("kb", "chunks")
# frontmatter 의 링크 키 — 목록 값. part_of 는 스칼라
LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "assumes", "satisfies", "constrains", "derivesFrom", "allocates", "coUpdatesWith")
ITEM_KINDS = "kb_chunk|kb_decision"


def run(cmd: list, cwd: str, check: bool = True) -> str:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(f"revalidate: 실패: {' '.join(cmd)}")
    return r.stdout


def parse_text(text: str, name: str):
    """base 리비전의 파일 내용을 parse_chunk 로 읽는다 — 해시 계산이 head 그래프와 같게."""
    with tempfile.NamedTemporaryFile("w", suffix=".md", prefix=Path(name).stem + "-", delete=False, encoding="utf-8") as t:
        t.write(text)
        tmp = t.name
    try:
        return parse_chunk(tmp)[0]
    finally:
        os.unlink(tmp)


def links_of(meta: dict) -> list:
    out = [(k, t) for k in LINK_KEYS for t in (meta.get(k) or [])]
    if meta.get("part_of"):
        out.append(("part_of", meta["part_of"]))
    return out


def package_of(root: Path, rel: str) -> tuple:
    """가장 가까운 BUILD.bazel 의 패키지와 그 안 경로 → 소스 파일 라벨 //pkg:path 의 두 부분."""
    p = Path(rel)
    for d in [p.parent] + list(p.parents)[:-1]:
        if (root / d / "BUILD.bazel").exists() or (root / d / "BUILD").exists():
            return str(d), str(p.relative_to(d))
    return "", rel


def owner_label(pkg: str, sub: str) -> str:
    """gen_build 의 규약: 결정은 <dir>/{conclusion,rationale,alternatives}.md → //pkg:<dir>, 청크는 <name>.md → //pkg:<name>."""
    m = re.match(r"(.+)/(conclusion|rationale|alternatives)\.md$", sub)
    return f"//{pkg}:{m.group(1) if m else sub[:-3]}"


def bazel_rdeps(cwd: str, owners: list, universe: str) -> dict:
    """소유 타깃마다 (직접 의존자, 전이 의존자). 질의 한 번 — 유도 부분그래프를 받아 여기서 닫는다."""
    if not owners:
        return {}
    expr = f'kind("{ITEM_KINDS}", rdeps({universe}, set({" ".join(owners)})))'
    r = subprocess.run(["bazel", "query", expr, "--noshow_progress", "--output=graph", "--nograph:factored"], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        print(f"WARN [revalidate] bazel query 실패 — 하류 의존자 없이 보고한다: {expr}")
        return {o: (None, None) for o in owners}
    rdep = defaultdict(set)  # 대상 → 그것에 직접 의존하는 타깃
    for a, b in re.findall(r'"([^"]+)"\s*->\s*"([^"]+)"', r.stdout):
        rdep[b].add(a)
    out = {}
    for o in owners:
        direct = set(rdep.get(o, ()))
        seen, stack = set(), [o]
        while stack:
            x = stack.pop()
            for y in rdep.get(x, ()):
                if y not in seen:
                    seen.add(y); stack.append(y)
        out[o] = (sorted(direct), sorted(seen - direct))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="HEAD", help="비교할 git 리비전 (기본 HEAD)")
    ap.add_argument("--universe", default="//...", help="rdeps 의 우주")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    cwd = str(root)

    # 1. 워킹트리 청크 색인 — IRI → (경로, 라벨, meta), 들어오는 링크
    index, incoming, unparsable = {}, defaultdict(list), []
    for d in CHUNK_DIRS:
        for p in sorted((root / d).rglob("*.md")):
            rel = str(p.relative_to(root))
            try:
                meta = parse_chunk(str(p))[0]
            except ValueError as e:
                unparsable.append(f"{rel}: {e}")
                continue
            index[meta["id"]] = (rel, meta)
    for iri, (rel, meta) in index.items():
        for k, t in links_of(meta):
            incoming[t].append((k, iri))
    composite_parts = defaultdict(list)
    for iri, (rel, meta) in index.items():
        if meta.get("part_of"):
            composite_parts[meta["part_of"]].append(iri)

    # 2. base 와의 차이 — 상태 M/A/D/R 인 청크 파일 + 미추적 파일
    status = {}
    for line in run(["git", "diff", "--name-status", a.base, "--", *CHUNK_DIRS], cwd).splitlines():
        parts = line.split("\t")
        st, path = parts[0][0], parts[-1]
        if path.endswith(".md"):
            status[path] = (st, parts[1] if st == "R" else path)
    for path in run(["git", "ls-files", "--others", "--exclude-standard", "--", *CHUNK_DIRS], cwd).splitlines():
        if path.endswith(".md"):
            status[path] = ("A", path)

    changed, head_only = [], []  # changed: (경로, 종류, iri, meta_wt|None, meta_base|None, 비고)
    for path, (st, base_path) in sorted(status.items()):
        wt = next(((iri, m) for iri, (rel, m) in index.items() if rel == path), None)
        base_meta, note = None, ""
        if st != "A":
            txt = run(["git", "show", f"{a.base}:{base_path}"], cwd, check=False)
            try:
                base_meta = parse_text(txt, base_path) if txt else None
            except ValueError as e:
                note = "base 판독 불가 → 변경으로 간주"
        if st == "D":
            if base_meta:
                changed.append((path, "삭제", base_meta["id"], None, base_meta, "이 IRI 를 가리키는 링크는 깨진다"))
            continue
        if wt is None:
            continue  # 청크가 아닌 md (frontmatter 없음)
        iri, meta = wt
        if st == "A" or base_meta is None:
            changed.append((path, "신규" if st == "A" else "변경", iri, meta, base_meta, note))
        elif meta["_content_hash"] != base_meta["_content_hash"]:
            changed.append((path, "본문 변경", iri, meta, base_meta, f"{base_meta['_content_hash']} → {meta['_content_hash']}"))
        else:
            keys = sorted(k for k in LINK_KEYS + ("part_of",) if (meta.get(k) or None) != (base_meta.get(k) or None))
            head_only.append((path, keys))

    # 3. 재판정 대상 — (a) frontmatter 링크 양방향 (b) bazel rdeps
    owners = sorted({owner_label(*package_of(root, path)) for path, kind, *_ in changed if kind != "삭제"})
    rd = bazel_rdeps(cwd, owners, a.universe) if owners else {}
    label = lambda iri: (f"`{index[iri][0]}` — {index[iri][1].get('title_ko', '')}" if iri in index else f"<{iri}>" + (" (복합체)" if iri in composite_parts else " (없음)"))
    rows, per_chunk = [], []
    for path, kind, iri, meta, base_meta, note in changed:
        m = meta or base_meta
        out_links = links_of(m)
        in_links = [(k, s) for k, s in incoming.get(iri, []) if s != iri]
        if m.get("part_of"):
            in_links += [("part_of(형제)", s) for s in composite_parts.get(m["part_of"], []) if s != iri]
        for k, t in out_links:
            rows.append((path, k, "→", label(t), "frontmatter"))
        for k, s in in_links:
            rows.append((path, k, "←", label(s), "frontmatter"))
        direct, trans = rd.get(owner_label(*package_of(root, path)), (None, None)) if kind != "삭제" else ([], [])
        for t in direct or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 직접"))
        for t in trans or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 전이"))
        verified = bool((meta or {}).get("verified"))
        if verified:
            rows.append((path, "verified", "·", "이 청크 자신 — 검증 뒤 본문이 바뀌었다 (writer 검사 대상)", "frontmatter"))
        per_chunk.append((path, kind, m.get("title_ko", ""), len(out_links) + len(in_links), (len(direct or []), len(trans or [])), verified, note))

    rep = [f"# revalidate — base {a.base}", "",
           f"변경 청크 {len(changed)} (본문 해시 변경·신규·삭제) · head 만 바뀐 청크 {len(head_only)} (해시 동일 — 재판정 대상 아님) · 재판정 대상 {len(rows)}",
           "", "| 변경 청크 | 변경 | 라벨 | 링크(양방향) | 하류(직접/전이) | verified | 비고 |", "|---|---|---|---|---|---|---|"]
    for path, kind, ko, nl, (nd, nt), v, note in per_chunk:
        rep.append(f"| `{path}` | {kind} | {ko} | {nl} | {nd}/{nt} | {'있음' if v else '—'} | {note} |")
    rep += ["", "## 재판정 대상", "", "| 변경 청크 | 종류 | 방향 | 상대 | 출처 |", "|---|---|---|---|---|"]
    rep += [f"| `{p}` | {k} | {d} | {t} | {src} |" for p, k, d, t, src in rows] or ["| — | | | 없음 | |"]
    if head_only:
        rep += ["", "head 만 바뀐 청크 (링크 키 변경이 있으면 표시): " + " · ".join(f"`{p}`" + (f" [{', '.join(ks)}]" if ks else "") for p, ks in head_only[:20])
                + (f" … 외 {len(head_only) - 20}" if len(head_only) > 20 else "")]
    if unparsable:
        rep += ["", "판독 불가 파일: " + " · ".join(unparsable[:10])]
    text = "\n".join(rep) + "\n"
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
