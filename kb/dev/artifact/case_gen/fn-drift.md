---
id: https://agentic-knowledge-base.dev/id/chunk/7718554a-5a67-4f4b-ab02-c8e91837d716
type: artifact
level: executable
title_ko: 함수 drift (tools/case_gen.py)
title: function drift in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9b61053c-0a32-44e3-83a7-5cceaaa5c57e
---
**함수** — `drift(root, cases_dir, scenarios, outputs, all_generated)` 다. 트리의 케이스와 생성 결과의 어긋남 — 다른 바이트 · 없는 케이스 · 생성 결과에 없는 생성 케이스 · (선택) 생성기 밖의 케이스.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
