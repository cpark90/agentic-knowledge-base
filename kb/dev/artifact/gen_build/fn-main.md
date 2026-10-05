---
id: https://agentic-knowledge-base.dev/id/chunk/c45073d7-38c4-4ed0-bea8-16920059e835
type: artifact
level: executable
title_ko: 함수 main (tools/gen_build.py)
title: function main in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551, https://agentic-knowledge-base.dev/id/chunk/50e03067-a51a-4276-beaa-b3062acbca52, https://agentic-knowledge-base.dev/id/chunk/552acfff-57db-463e-82cb-cdace15cb87d, https://agentic-knowledge-base.dev/id/chunk/7e58cd2b-ecf9-4a21-a66b-9e28aa4474e9, https://agentic-knowledge-base.dev/id/chunk/869af6ba-5152-4bae-8ae4-1081f5177303, https://agentic-knowledge-base.dev/id/chunk/9cf3ed9e-81a6-4add-97ba-b933477041ad, https://agentic-knowledge-base.dev/id/chunk/ad68f79e-bbb2-4a80-b6c8-518fdd88a3a2, https://agentic-knowledge-base.dev/id/chunk/e54eb0d7-070d-49c3-80c1-2c299c1c0b7a, https://agentic-knowledge-base.dev/id/chunk/f27e5261-f973-4030-9f81-9dab47f4a21a]
part_of: https://agentic-knowledge-base.dev/id/composite/e563bac1-7552-474e-a036-f6ced4999bc4
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 커밋본과 비교. 어긋나면 1")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root 기준")
    a = ap.parse_args()
    root = Path(a.root)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk2kg] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    try:
        items, iri_to_label = scan(root)
        outputs = {
            str(root / "kb/dev/requirement/BUILD.bazel"): render_chunks("kb/dev/requirement", items, iri_to_label, "//kb:requirement_readers"),
            str(root / "kb/dev/decision/BUILD.bazel"): render_decisions(items, iri_to_label),
            str(root / "chunks/decision/BUILD.bazel"): render_chunks("chunks/decision", items, iri_to_label, "//kb:decision_readers"),
            str(root / MEMORY_PKG / "BUILD.bazel"): render_chunks(MEMORY_PKG, items, iri_to_label, "//kb:memory_readers", allow_empty=True),
            str(root / VV_ROOT / "BUILD.bazel"): render_vv_root(items),
            str(root / ARTIFACT_ROOT / "BUILD.bazel"): render_artifact_root(root),
        }
        for d in sorted(p for p in (root / ARTIFACT_ROOT).iterdir() if p.is_dir()) if (root / ARTIFACT_ROOT).is_dir() else []:
            outputs[str(root / ARTIFACT_ROOT / d.name / "BUILD.bazel")] = render_chunks(
                f"{ARTIFACT_ROOT}/{d.name}", items, iri_to_label, "//kb:artifact_readers")
        outputs[str(root / NORM_ROOT / "BUILD.bazel")] = render_norm_root(root)
        for d in norm_pkgs(root):  # 규범 문서마다 패키지 하나 — 결정의 투영이라 그래프·게이트만 본다 (//kb:norm_readers)
            outputs[str(root / NORM_ROOT / d / "BUILD.bazel")] = render_chunks(f"{NORM_ROOT}/{d}", items, iri_to_label, "//kb:norm_readers")
        for sub in VV_PKGS:  # V&V plane 패키지 — 개발 청크는 볼 수 없다 (//kb:vv_readers, 8.5절 독립성)
            outputs[str(root / VV_ROOT / sub / "BUILD.bazel")] = render_chunks(f"{VV_ROOT}/{sub}", items, iri_to_label, "//kb:vv_readers", allow_empty=True)
        outputs.update(ontology(root))
    except GenBuildError as e:
        print(f"FAIL [gen-build] {e}")
        return EXIT_FAIL
    except ValueError as e:  # parse_chunk 의 frontmatter·본문 규칙 — chunk2kg 의 판정
        print(f"FAIL [chunk2kg] {e}")
        return EXIT_FAIL
    except OSError as e:
        print(f"FAIL [gen-build] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    drift = []
    for path, content in outputs.items():
        p = Path(path)
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(path)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{path} (커밋본)", f"{path} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)  # 비어 있는 관측 패키지의 첫 BUILD
                p.write_text(content, encoding="utf-8")
    if a.check:
        if drift:
            for path in drift:
                print(f"FAIL [build-drift] {path}: frontmatter 와 어긋난다 — tools/gen_build.py 를 돌려 커밋하라 (BUILD 는 뷰, frontmatter 가 원본)")
            print(f"\nFAIL [build-drift] — {len(drift)}건 / 생성 BUILD {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [build-drift] — 생성 BUILD {len(outputs)}개가 원본과 일치")
        return 0
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(Path(d).relative_to(root).as_posix() for d in drift))
    return 0
```
<!-- 인용 끝 -->
