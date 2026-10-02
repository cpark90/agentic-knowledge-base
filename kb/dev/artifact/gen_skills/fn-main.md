---
id: https://agentic-knowledge-base.dev/id/chunk/689ef793-7510-40b3-8834-b4553728cfeb
type: artifact
level: executable
title_ko: 함수 main (tools/gen_skills.py)
title: function main in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/735aadbc-1b1e-465d-8274-4cb2aee71fb2, https://agentic-knowledge-base.dev/id/chunk/9337f5de-4a6b-420b-b51d-2a1afe8ebbae]
part_of: https://agentic-knowledge-base.dev/id/composite/b9b38ba6-d689-44c6-814b-4526153a07b1
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    a = ap.parse_args()
    root = Path(a.root)
    try:
        outputs = generate(root)
    except GenSkillsError as e:
        print(f"FAIL [{GEN}] {e}")
        return EXIT_FAIL
    except (OSError, SyntaxError) as e:
        print(f"FAIL [{GEN}] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    skills_dir = root / kb_lib.SKILLS_DIR
    stray = sorted(p for p in skills_dir.glob("*/SKILL.md") if str(p) not in outputs) if skills_dir.is_dir() else []
    drift = []
    for path, content in outputs.items():
        p = Path(path)
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(path)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{path} (트리)", f"{path} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content, encoding="utf-8")
    for s in stray:
        print(f"FAIL [{DRIFT}] {s}: kb_lib.SKILLS 에 없는 skill 이다 — 손으로 쓴 skill 은 이중 원본이다. SKILLS 에 항목을 더하고 생성하거나 지운다")
    if a.check:
        for path in drift:
            print(f"FAIL [{DRIFT}] {path}: 원본(docstring · kb_lib.SKILLS)과 어긋난다 — python3 tools/gen_skills.py --root . 를 돌려 커밋하라")
        if drift or stray:
            print(f"\nFAIL [{DRIFT}] — 어긋남 {len(drift)}건 · 손으로 쓴 skill {len(stray)}건 / 생성 skill {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT}] — 생성 skill {len(outputs)}개가 원본과 일치")
        return EXIT_OK
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(Path(d).relative_to(root).as_posix() for d in drift))
    return EXIT_FAIL if stray else EXIT_OK
```
<!-- 인용 끝 -->
