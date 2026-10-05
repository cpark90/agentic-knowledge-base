---
id: https://agentic-knowledge-base.dev/id/chunk/0a97c6fb-2a37-46e9-a895-dbed5741b4da
type: artifact
level: executable
title_ko: 함수 main (tools/case_gen.py)
title: function main in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:09:24Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/006ec0fb-bfe1-4695-9abf-423664b5532d, https://agentic-knowledge-base.dev/id/chunk/14a19009-1b05-4621-b253-ce8233be9f19, https://agentic-knowledge-base.dev/id/chunk/54c8835d-68d1-43d6-85ab-2a0371c2a67e, https://agentic-knowledge-base.dev/id/chunk/770131c5-53ed-4b85-b077-050f12836f80, https://agentic-knowledge-base.dev/id/chunk/7718554a-5a67-4f4b-ab02-c8e91837d716, https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a]
part_of: https://agentic-knowledge-base.dev/id/composite/9b61053c-0a32-44e3-83a7-5cceaaa5c57e
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
