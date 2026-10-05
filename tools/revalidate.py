#!/usr/bin/env python3
"""재검증 후보 — 본문 해시가 바뀐 청크의 링크와 하류 의존자를 재판정 대상으로 보고한다 (dependency-graph-design §5, method §7).

본문(frontmatter 제외)의 contentHash 가 base 리비전과 다르면 그 IRI 에 붙은 링크는 suspect 후보이고 재검증 시점에서
재판정한다 — 링크 부패 규칙(p10 link decay)의 첫 형태. 해시는 tools/chunk2kg.py 의 parse_chunk 를 그대로 써서
head 그래프의 agt:contentHash 와 같다. 재판정 대상은 다섯 갈래를 합친다:
  (a) frontmatter 링크의 상대 — refines·serves·supersedes·verifies·assumes·part_of (+ satisfies·constrains·derivesFrom·allocates·
      coUpdatesWith·overlapsWith), 양방향
  (b) Bazel 하류 의존자 — bazel query rdeps(<universe>, <타깃>) 의 kb_chunk·kb_decision (직접 / 전이)
  (c) **호출부** — 본문 해시가 바뀐 정의 청크를 `uses`(agt:usesDefinition)로 가리키는 출발점. 그 수가 **코드 호출부
      파손의 상한**이다: 같은 모듈의 최상위 이름 참조와 치역 경계(defs/kb.bzl 의 USES_TARGETS — 2026-10-01 표본 쌍은
      `kb_lib` 하나다) 안의 모듈 간 참조를 세므로, 경계 밖의 모듈을 치역으로 하는 호출은 여기 들어오지 않고 실제
      파손은 이 수보다 크다 (유저 답 2026-09-30·2026-10-01, 채널 uses-definition·uses-definition-range).
      링크 개체가 아니라 직접 트리플이므로 (d) 의 표에는 오르지 않는다
  (d) **링크 개체** — 본문 해시가 바뀐 청크를 양 끝 중 하나로 갖는 agt:Link 의 IRI. 그 링크가 suspect 로 유도되는 자리다.
      IRI 는 chunk2kg 와 같은 함수(link_hash × work_id)로 계산하므로 head 그래프의 링크 개체와 같은 것이다 — 그래서 이 보고의
      한 줄이 그래프의 한 개체를 가리킨다. 상태는 저장하지 않는다 (노트 9.11절): suspect 는 여기서 물질화된다.
**정체성은 uuid(frontmatter `id`)이고 경로는 주소다** (p10-split-keeps-work-identity · p10-function-identity-registry).
그래서 base 와 워킹트리를 uuid 로 맞춘다 — 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부풀고 링크가
깨진 것처럼 읽힌다. 경로가 바뀐 것은 **라벨 변경**으로 보고한다. 하류 조회의 타깃 라벨은 `gen_build` 의 `iri_to_label`
에서 온다 — 복합체 묶음 뒤에는 부분마다의 개별 타깃이 없으므로 경로에서 라벨을 지어내면 rdeps 가 늘 0 이다.

git 과 bazel query 를 부르므로 odd_check 처럼 테스트 타깃이 아니다. 판정은 사람/승인된 판정자의 몫이다.
**스냅숏 비교** (유저 답 Q38-c): `--base-dir <d1> --head-dir <d2>` 는 git 리비전 대신 디렉토리 둘(아래의 `*.md` 전부)을, `--base-files`·
`--head-files` 는 파일 목록 둘을 uuid 로 맞춰 같은 재판정 대상을 낸다. git 도 `bazel query` 도 부르지 않으므로 (c)의 하류 의존자는
비고 읽기 전용이다 — V&V 케이스 실행기(`vv_run`)의 허용 목록이 받는 꼴이 이것이다. 파일 목록은 주소가 아니라서 경로 변경을 보고하지 않는다.

사용: bazel run //tools:revalidate -- [--base HEAD] [--universe '//...'] [--out report.md]
      python3 tools/revalidate.py --base-dir <d1> --head-dir <d2> [--out report.md]
      python3 tools/revalidate.py --base-files <f…> --head-files <f…> [--out report.md]
종료: 0 = 변경 없음(재판정 대상 없음), 1 = 재판정 대상 있음, 2 = 입력 문제(스냅숏 한쪽만 · 없는 경로 · 값 어휘)
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
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록·빈 값 표기)의 단일 정의처
from chunk2kg import (ID_BASE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,  # noqa: E402
                      link_hash, load_plane_level_state, parse_chunk, work_id)
from chunk2kg import LINK_KEYS as OBJECT_LINK_KEYS  # noqa: E402 — 링크 개체(agt:Link)를 내는 키. assumes·part_of 는 개체가 없다

CHUNK_DIRS = ("kb", "chunks")
USES_KEY = kb_lib.USES_KEY  # 정의 → 정의 (agt:usesDefinition, 치역은 같은 모듈 + USES_TARGETS). `호출부` 열의 입력이다
# frontmatter 의 링크 키 — 목록 값. part_of 는 스칼라
LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "assumes", "satisfies", "constrains", "derivesFrom", "allocates",
             "coUpdatesWith", "overlapsWith")
# 하류 조회가 세는 타깃 종류 — 복합체 묶음(kb_composite)이 빠지면 추출된 코드 청크의 rdeps 가 늘 0 이다
ITEM_KINDS = "kb_chunk|kb_decision|kb_composite"


# ── 청크 읽기와 링크 해소 ────────────────────

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


def link_objects(index: dict, iris: set) -> list:
    """본문이 바뀐 청크(iris)를 양 끝 중 하나로 갖는 링크 개체 → [(링크 IRI, 종류, 출발, 도착, 방향)].

    IRI 계산은 chunk2kg 와 같다 — 양 끝을 specializationOf 사슬의 뿌리 uuid(work-id)로 올린 뒤 sha256(출발|종류|도착)[:12] 다.
    사슬이 순환하면 그 링크는 건너뛴다 (판정은 validate check_specialization 이 한다).
    """
    spec = {iri: m[SPECIALIZATION_KEY] for iri, (_rel, m) in index.items() if m.get(SPECIALIZATION_KEY)}
    out = []
    for frm, (_rel, meta) in sorted(index.items()):
        for key in OBJECT_LINK_KEYS:
            for to in meta.get(key) or []:
                if frm not in iris and to not in iris:
                    continue
                try:
                    h = link_hash(work_id(frm, spec), key, work_id(to, spec))
                except SpecializationError:
                    continue
                out.append((f"{ID_BASE}link/{h}", key, frm, to, "출발" if frm in iris else "도착"))
    return out


def index_worktree(root: Path) -> tuple:
    """워킹트리의 청크 색인 → (index, incoming, composite_parts, callers, unparsable).

    색인의 열쇠는 IRI 다 — 정체성이 uuid 이고 경로는 주소이기 때문이다 (p10-split-keeps-work-identity).
    """
    # 1. 워킹트리 청크 색인 — IRI → (경로, 라벨, meta), 들어오는 링크
    return index_files([(str(p.relative_to(root)), p) for d in CHUNK_DIRS for p in sorted((root / d).rglob("*.md"))])


def index_files(files: list) -> tuple:
    """(주소, 파일) 목록의 청크 색인 → (index, incoming, composite_parts, callers, unparsable). 워킹트리와 스냅숏이 같은 규칙을 쓴다."""
    index, incoming, unparsable = {}, defaultdict(list), []
    for rel, p in files:
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
    # 호출부 — 대상 정의 IRI → 그것을 `uses` 로 가리키는 출발점들. 링크 키가 아니므로 links_of 와 섞지 않는다:
    # 그래야 `링크(양방향)` 열이 링크 개체의 수를 계속 뜻하고 `호출부` 열이 코드 파손의 상한을 따로 뜻한다
    callers = defaultdict(list)
    for iri, (rel, meta) in index.items():
        for t in meta.get(USES_KEY) or []:
            if t != iri:
                callers[t].append(iri)
    return index, incoming, composite_parts, callers, unparsable


def base_diff(base: str, cwd: str, index: dict) -> tuple:
    """base 리비전과 워킹트리의 차이 → (changed, head_only, base_by_iri, unread).

    비교의 열쇠도 IRI 다 — 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부푼다.
    `changed` 는 (경로, 종류, iri, meta_wt|None, meta_base|None, 사유) 이고 `head_only` 는 본문 해시가 같은 것이다.
    """
    a_base = base
    # 2. base 와의 차이 — 상태 M/A/D/R 인 청크 파일 + 미추적 파일
    status = {}
    for line in run(["git", "diff", "--name-status", a_base, "--", *CHUNK_DIRS], cwd).splitlines():
        parts = line.split("\t")
        st, path = parts[0][0], parts[-1]
        if path.endswith(".md"):
            status[path] = (st, parts[1] if st == "R" else path)
    for path in run(["git", "ls-files", "--others", "--exclude-standard", "--", *CHUNK_DIRS], cwd).splitlines():
        if path.endswith(".md"):
            status[path] = ("A", path)

    # 정체성은 uuid(frontmatter `id`)이고 경로는 주소다 (p10-split-keeps-work-identity · p10-function-identity-registry).
    # 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부풀고 링크가 깨진 것처럼 읽힌다.
    by_path = {rel: iri for iri, (rel, _m) in index.items()}
    base_by_iri, unread = {}, []
    for path, (st, base_path) in sorted(status.items()):
        if st == "A":
            continue
        txt = run(["git", "show", f"{a_base}:{base_path}"], cwd, check=False)
        try:
            bm = parse_text(txt, base_path) if txt else None
        except ValueError:
            unread.append(base_path)
            continue
        if bm:
            base_by_iri[bm["id"]] = (base_path, bm)
    touched = {by_path[p] for p in status if p in by_path} | set(base_by_iri)

    changed, head_only = [], []  # changed: (경로, 종류, iri, meta_wt|None, meta_base|None, 비고)
    for iri in sorted(touched):
        wt = index.get(iri)
        base = base_by_iri.get(iri)
        if wt is None:
            if base:
                changed.append((base[0], "삭제", iri, None, base[1], "이 IRI 를 가리키는 링크는 깨진다"))
            continue
        path, meta = wt
        if base is None:
            changed.append((path, "신규", iri, meta, None, "base 에 이 IRI 가 없다"))
            continue
        base_path, base_meta = base
        moved = f"경로 변경(라벨 변경) `{base_path}` → `{path}`" if base_path != path else ""
        if meta["_content_hash"] != base_meta["_content_hash"]:
            changed.append((path, "본문 변경", iri, meta, base_meta,
                            " · ".join(x for x in (f"{base_meta['_content_hash']} → {meta['_content_hash']}", moved) if x)))
        else:
            keys = sorted(k for k in LINK_KEYS + ("part_of",) if (meta.get(k) or None) != (base_meta.get(k) or None))
            head_only.append((path, keys + ([moved] if moved else [])))
    return changed, head_only, base_by_iri, unread


# ── 스냅숏 비교 — git 리비전 대신 디렉토리·파일 목록 둘 (유저 답 Q38-c) ────────────────────

def snapshot_files(dirs: list, files: list) -> list:
    """스냅숏 한쪽의 (주소, 파일) 목록 — 디렉토리는 그 아래 `*.md` 전부(주소는 디렉토리 상대), 파일은 이름이 주소다."""
    out = [(str(p.relative_to(d)), p) for d in map(Path, dirs) for p in sorted(d.rglob("*.md"))]
    return out + [(Path(f).name, Path(f)) for f in files]


def snapshot_diff(base_index: dict, base_unparsable: list, index: dict, addressed: bool) -> tuple:
    """스냅숏 둘의 차이 → (changed, head_only, base_by_iri, unread) — `base_diff` 와 같은 꼴이고 열쇠도 IRI 다.

    git 이 고른 변경 파일이 없으므로 양쪽 IRI 전부를 맞춘다. `head_only` 에는 본문 해시가 같고 링크 키나 주소가 바뀐 것만
    든다 — 바뀌지 않은 청크까지 넣으면 "head 만 바뀐 청크" 가 스냅숏 전체가 된다. `addressed` 가 거짓(파일 목록)이면 경로는
    주소가 아니라서 경로 변경을 보고하지 않는다.
    """
    base_by_iri = dict(base_index)
    unread = [u.split(":", 1)[0] for u in base_unparsable]
    changed, head_only = [], []
    for iri in sorted(set(index) | set(base_by_iri)):
        wt, base = index.get(iri), base_by_iri.get(iri)
        if wt is None:
            changed.append((base[0], "삭제", iri, None, base[1], "이 IRI 를 가리키는 링크는 깨진다"))
            continue
        path, meta = wt
        if base is None:
            changed.append((path, "신규", iri, meta, None, "base 에 이 IRI 가 없다"))
            continue
        base_path, base_meta = base
        moved = f"경로 변경(라벨 변경) `{base_path}` → `{path}`" if addressed and base_path != path else ""
        if meta["_content_hash"] != base_meta["_content_hash"]:
            changed.append((path, "본문 변경", iri, meta, base_meta,
                            " · ".join(x for x in (f"{base_meta['_content_hash']} → {meta['_content_hash']}", moved) if x)))
            continue
        keys = sorted(k for k in LINK_KEYS + ("part_of",) if (meta.get(k) or None) != (base_meta.get(k) or None))
        if keys or moved:
            head_only.append((path, keys + ([moved] if moved else [])))
    return changed, head_only, base_by_iri, unread


# ── 하류 조회와 보고 ────────────────────

def owner_labels(root: Path) -> dict:
    """IRI → 소유 Bazel 타깃 라벨. 규칙의 원본은 `gen_build` 의 `iri_to_label` 이다 — 여기서 다시 적지 않는다.

    복합체 묶음(`kb_composite`·`kb_decision`) 뒤에는 **부분마다의 개별 타깃이 없다**. 파일 경로에서 라벨을 지어내면
    추출된 코드 청크(`kb/dev/artifact/<모듈>/fn-*.md`)가 존재하지 않는 타깃을 가리켜 `bazel query rdeps` 가 늘 0/0 이
    된다. 생성기를 그대로 불러 사상을 얻는다. 생성 시점 거부(끊긴 링크 등)가 있으면 빈 사상을 돌려주고 경고만 남긴다.
    """
    try:
        from gen_build import GenBuildError, scan
    except ImportError:
        from tools.gen_build import GenBuildError, scan
    try:
        return scan(root)[1]
    except (GenBuildError, ValueError, OSError) as e:
        print(f"WARN [revalidate] 타깃 라벨 사상을 얻지 못했다 — 하류 의존자 없이 보고한다: {e}")
        return {}


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


def parse_args():
    """명령줄 인자 — 파서가 곧 형식의 정의처다."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="HEAD", help="비교할 git 리비전 (기본 HEAD)")
    ap.add_argument("--universe", default="//...", help="rdeps 의 우주")
    ap.add_argument("--out", default="")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root(워크스페이스) 기준")
    ap.add_argument("--base-dir", action="append", default=[], metavar="DIR",
                    help="스냅숏 비교의 base — 이 디렉토리 아래 `*.md` 전부. git 리비전 대신이다 (반복 가능)")
    ap.add_argument("--head-dir", action="append", default=[], metavar="DIR", help="스냅숏 비교의 head — 워킹트리 대신이다 (반복 가능)")
    ap.add_argument("--base-files", nargs="+", default=[], metavar="MD", help="스냅숏 비교의 base 파일 목록 — 이름이 주소다")
    ap.add_argument("--head-files", nargs="+", default=[], metavar="MD", help="스냅숏 비교의 head 파일 목록")
    return ap.parse_args()


def snapshot_mode(a) -> str | None:
    """스냅숏 비교의 입력 문제 — 없으면 None. 한쪽만 주거나 없는 경로를 주면 비교가 성립하지 않는다."""
    base, head = a.base_dir + a.base_files, a.head_dir + a.head_files
    if bool(base) != bool(head):
        return "스냅숏 비교는 base(`--base-dir`·`--base-files`)와 head(`--head-dir`·`--head-files`)를 둘 다 준다"
    missing = [d for d in a.base_dir + a.head_dir if not Path(d).is_dir()] + [f for f in a.base_files + a.head_files if not Path(f).is_file()]
    return f"없는 경로: {' · '.join(missing)}" if missing else None


def revalidation_rows(root: Path, cwd: str, universe: str, changed: list, index: dict, incoming: dict,
                      composite_parts: dict, callers: dict, downstream: bool = True) -> tuple:
    """재판정 대상 → (rows, per_chunk, label, iri_to_label).

    대상은 다섯이다 — frontmatter 링크 양방향 · 복합체 형제 · `uses` 호출부 · `bazel rdeps` 의 하류 · 도장.
    `downstream` 이 거짓(스냅숏 비교)이면 타깃 라벨 사상과 `bazel query` 를 부르지 않는다 — 하류 의존자 열이 빈다.
    """
    # 3. 재판정 대상 — (a) frontmatter 링크 양방향 (b) bazel rdeps
    iri_to_label = owner_labels(root) if downstream else {}
    owners = sorted({iri_to_label[iri] for _p, kind, iri, *_ in changed if kind != "삭제" and iri in iri_to_label})
    rd = bazel_rdeps(cwd, owners, universe) if owners else {}
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
        called_by = sorted(callers.get(iri, ())) if kind in ("본문 변경", "삭제") else []
        for caller in called_by:  # 본문이 바뀐 정의를 이름으로 쓰는 출발점 — 코드 호출부 파손의 상한이다
            rows.append((path, USES_KEY, "←", label(caller), "frontmatter uses"))
        direct, trans = rd.get(iri_to_label.get(iri, ""), (None, None)) if kind != "삭제" else ([], [])
        for t in direct or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 직접"))
        for t in trans or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 전이"))
        verified = bool((meta or {}).get("verified"))
        if verified:
            rows.append((path, "verified", "·", "이 청크 자신 — 검증 뒤 본문이 바뀌었다 (writer 검사 대상)", "frontmatter"))
        per_chunk.append((path, kind, m.get("title_ko", ""), len(out_links) + len(in_links), (len(direct or []), len(trans or [])),
                          len(called_by), verified, note))
    return rows, per_chunk, label, iri_to_label


def report_rows(per_chunk: list, rows: list, objs: list, head_only: list, unparsable: list,
                unread: list, label) -> list[str]:
    """표 셋과 꼬리말 — 변경 청크 · 재판정 대상 · 재판정 링크 개체."""
    body = ["| 변경 청크 | 변경 | 라벨 | 링크(양방향) | 하류(직접/전이) | 호출부 | verified | 비고 |",
            "|---|---|---|---|---|---|---|---|"]
    for path, kind, ko, nl, (nd, nt), nc, v, note in per_chunk:
        body.append(f"| `{path}` | {kind} | {ko or kb_lib.NONE_MARK} | {nl} | {nd}/{nt} | {nc} | "
                    f"{'있음' if v else kb_lib.NONE_MARK} | {note or kb_lib.NONE_MARK} |")  # G14 — 빈 셀을 두지 않는다
    body += ["", "## 재판정 대상", "", "| 변경 청크 | 종류 | 방향 | 상대 | 출처 |", "|---|---|---|---|---|"]
    body += [f"| `{p}` | {k} | {d} | {t} | {src} |" for p, k, d, t, src in rows] or ["| " + " | ".join([kb_lib.NONE_MARK] * 3 + [f"재판정 대상 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body += ["", "## 재판정 대상 링크 개체 — 본문 해시 변경 → 링크 재판정 (노트 9.11절: 상태는 평가 결과다)", "",
             "| 링크 개체 | 종류 | 출발 | 도착 | 바뀐 끝 | 유도 상태 |", "|---|---|---|---|---|---|"]
    body += [f"| `{kb_lib.compact_iri(l)}` | `{k}` | {label(f)} | {label(t)} | {side} | {kb_lib.LINK_STATE_SUSPECT} |"
             for l, k, f, t, side in objs] \
            or ["| " + " | ".join([kb_lib.NONE_MARK] * 4 + [f"재판정 링크 개체 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body.append("")
    if head_only:
        body += ["head 만 바뀐 청크 (링크 키 변경이 있으면 표시): " + " · ".join(f"`{p}`" + (f" [{', '.join(ks)}]" if ks else "") for p, ks in head_only[:20])
                + (f" … 외 {len(head_only) - 20}" if len(head_only) > 20 else "")]
    if unparsable or unread:
        body += ["판독 불가 파일: " + " · ".join((unparsable + [f"{u}: base 판독 불가" for u in unread])[:10])]
    return body


def main() -> int:
    a = parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    cwd = str(root)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"CONFIG [revalidate] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}", file=sys.stderr)
        return 2

    problem = snapshot_mode(a)
    if problem:
        print(f"CONFIG [revalidate] {problem}", file=sys.stderr)
        return 2
    snapshot = bool(a.head_dir or a.head_files)
    if snapshot:  # 스냅숏 비교 — git 도 bazel query 도 부르지 않는다 (유저 답 Q38-c)
        index, incoming, composite_parts, callers, unparsable = index_files(snapshot_files(a.head_dir, a.head_files))
        base_index, _i, _c, _u, base_unparsable = index_files(snapshot_files(a.base_dir, a.base_files))
        changed, head_only, base_by_iri, unread = snapshot_diff(base_index, base_unparsable, index, not (a.base_files or a.head_files))
    else:
        index, incoming, composite_parts, callers, unparsable = index_worktree(root)
        changed, head_only, base_by_iri, unread = base_diff(a.base, cwd, index)
    rows, per_chunk, label, iri_to_label = revalidation_rows(
        root, cwd, a.universe, changed, index, incoming, composite_parts, callers, downstream=not snapshot)

    # 4. 본문 해시 변경 → 링크 재판정. 본문이 바뀐 청크를 양 끝 중 하나로 갖는 링크 개체가 suspect 로 유도된다 (노트 9.11절)
    body_changed = {iri for _path, kind, iri, _m, _b, _n in changed if kind in ("본문 변경", "변경", "신규", "삭제")}
    objs = link_objects(index, body_changed)
    # 바뀐 끝이 **결정 결론**인 재판정 링크 — V&V 기준 decision-and-artifact-agree 의 판정 대상 행이고
    # 현상 agt:reasoningActionMismatch(P16)의 관측 자리다. 결론은 결정 복합체의 파일 이름으로 가른다 (kb_lib.DECISION_PART_FILES)
    conclusion_file = kb_lib.DECISION_PART_FILES["conclusion"]
    path_of = lambda iri: (index.get(iri) or base_by_iri.get(iri) or ("", {}))[0]
    is_conclusion = lambda iri: Path(path_of(iri)).name == conclusion_file
    n_conclusion = sum(1 for _l, _k, frm, to, side in objs if is_conclusion(frm if side == "출발" else to))

    if snapshot:
        sides = (" ".join(a.base_dir + a.base_files), " ".join(a.head_dir + a.head_files))
        title, between = "스냅숏 대비 재판정 대상", f"base 스냅숏 `{sides[0]}` 와 head 스냅숏 `{sides[1]}`"
        command = "python3 tools/revalidate.py " + " ".join(
            [f"--base-dir {d}" for d in a.base_dir] + ([f"--base-files {' '.join(a.base_files)}"] if a.base_files else [])
            + [f"--head-dir {d}" for d in a.head_dir] + ([f"--head-files {' '.join(a.head_files)}"] if a.head_files else []))
        downstream = "(c) 하류 의존자 — 스냅숏 비교라 `bazel query` 를 부르지 않아 비어 있다"
        input_note = "스냅숏 둘의 청크 파일 — 스냅숏 대비 차이라 지문을 내지 않는다"
    else:
        title, between = f"base {a.base} 대비 재판정 대상", f"base 리비전 `{a.base}` 와 워킹트리"
        command = f"bazel run //tools:revalidate -- --base {a.base}"
        downstream = "(c) `bazel query rdeps` 의 하류 의존자"
        input_note = f"`git show {a.base}:<청크>` 와 워킹트리의 청크 파일, `bazel query` 결과 — 리비전 대비 차이라 지문을 내지 않는다"
    rep = kb_lib.gendoc_header(
        "revalidate", title, "tools/revalidate.py",
        f"{between} 사이에서 본문 해시가 바뀐 청크마다 — (a) frontmatter 링크의 상대(양방향) · "
        f"(b) 복합체 형제 · {downstream} · (d) 그 정의를 `uses` 로 가리키는 **호출부** · "
        "(e) 그 청크를 양 끝 중 하나로 갖는 **링크 개체**(`agt:Link`)를 재판정 대상으로 (dependency-graph-design §5). 링크 개체의 상태는 저장하지 않고 여기서 물질화한다",
        command, [],
        f"변경 청크 {len(changed)} · 재판정 대상 {len(rows)} · 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} · "
        f"재판정 링크 개체 {len(objs)} (바뀐 끝이 결정 결론인 것 {n_conclusion})",
        kb_lib.gendoc_view_notice("각 청크의 본문과 frontmatter 링크"),
        input_note=input_note,
        extra=[f"- 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} — 본문이 바뀐 정의를 `uses`(agt:usesDefinition)로 "
               "가리키는 출발점이고 **코드 호출부 파손의 상한**이다. 모듈 안 호출과 치역 경계"
               f"(`{kb_lib.USES_TARGETS_NAME}`) 안의 모듈 간 호출을 세므로 경계 밖을 치역으로 하는 호출은 빠진다",
               f"- head 만 바뀐 청크 {len(head_only)} (본문 해시 동일 — 재판정 대상이 아니다)",
               f"- 본문이 바뀐 청크에 붙은 링크 개체 {len(objs)} — 유도 상태는 `{kb_lib.LINK_STATE_SUSPECT}` 다",
               f"- 그중 **바뀐 끝이 결정 결론**(`{conclusion_file}`)인 것 {n_conclusion} — 결정의 본문과 구현이 어긋나는 현상"
               f"(`agt:reasoningActionMismatch`)의 판정 대상 행이고 0 이면 공허 합격이다"])
    body = report_rows(per_chunk, rows, objs, head_only, unparsable, unread, label)
    text = kb_lib.gendoc_assemble(rep, body, [])
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if (rows or objs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
