---
id: https://agentic-knowledge-base.dev/id/chunk/205ddaae-9763-4e5b-a48f-c8e0b4a8bc63
type: artifact
level: executable
title_ko: 함수 mutation_fixtures (tools/metrics.py)
title: function mutation_fixtures in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/213f1d8d-a21d-4794-a6f1-f88e4a849f3d, https://agentic-knowledge-base.dev/id/chunk/5043c522-c415-4b84-99a0-cd5627e0b9d4]
part_of: https://agentic-knowledge-base.dev/id/composite/a599c470-8ce8-4e70-a475-1067401bb55c
---
**함수** — `mutation_fixtures(paths)` 다. `defs/tests` 의 변이(음성) 고정물과 그것을 기대 FAIL 문구로 묶는 시험을 시험 정의에서 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def mutation_fixtures(paths):
    """`defs/tests` 의 변이(음성) 고정물과 그것을 기대 FAIL 문구로 묶는 시험을 시험 정의에서 읽는다 (유저 결정 2026-10-04).

    고정물의 종류는 셋이다. `failure_test` 의 `target_under_test`(분석 시점 FAIL), 명령이 `! $(execpath …)` 로 실패를 기대하는
    genrule(실행 시점 FAIL — `build_test` 에 묶여야 `//...` 에 든다), 규범 고정물 시험의 EXPECT 표에서 종료 코드가 0 이 아닌
    사례다. 이름이 `bad_` 인 고정물 타깃을 가리키는 `failure_test` 가 없으면 묶이지 않은 고정물이다.
    돌려주는 행은 (종류, 고정물, 기대 FAIL 문구, 묶임 여부)다. 잡힘의 판정은 묶인 시험의 통과다.
    """
    build = next((p for p in paths if Path(p).name == "BUILD.bazel"), None)
    norm = next((p for p in paths if Path(p).name == "norm_fixture_test.py"), None)
    if not build:
        return None
    tree = ast.parse(Path(build).read_text(encoding="utf-8"))
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
    def is_manual(c):
        tags = _kw(c, "tags")
        return isinstance(tags, ast.List) and any(_const_str(t) == "manual" for t in tags.elts)
    built = {_const_str(t).lstrip(":") for c in calls if c.func.id == "build_test" and not is_manual(c)
             for t in (_kw(c, "targets").elts if isinstance(_kw(c, "targets"), ast.List) else [])}
    rows, guarded = [], set()
    for c in calls:
        if c.func.id == "failure_test":
            fx = _const_str(_kw(c, "target_under_test")).lstrip(":")
            guarded.add(fx)
            expected = _const_str(_kw(c, "expected"))
            rows.append(("failure_test", fx, expected, not is_manual(c) and bool(expected)))
        elif c.func.id == "genrule":
            name, cmd = _const_str(_kw(c, "name")), _const_str(_kw(c, "cmd"))
            if re.search(r"(^|&&\s*)!\s*\$\(execpath", cmd):
                phrases = re.findall(r"(?<!! )grep -qF? '([^']+)'", cmd)
                rows.append(("거부 genrule", name, " · ".join(phrases), name in built and bool(phrases)))
    for c in calls:
        name = _const_str(_kw(c, "name"))
        if c.func.id.startswith("kb_") and name.startswith("bad_") and name not in guarded:
            rows.append(("failure_test", name, "", False))
    if norm:
        cases = {_const_str(e) for n in ast.walk(tree) if isinstance(n, ast.ListComp)
                 and isinstance(n.elt, ast.Call) and getattr(n.elt.func, "id", "") == "kb_norms_fixture_test"
                 for gen in n.generators if isinstance(gen.iter, ast.List) for e in gen.iter.elts}
        expect = next((ast.literal_eval(n.value) for n in ast.walk(ast.parse(Path(norm).read_text(encoding="utf-8")))
                       if isinstance(n, ast.Assign) and any(getattr(t, "id", "") == "EXPECT" for t in n.targets)), {})
        rows += [("규범 고정물 음성", case, text, case in cases) for case, (code, text) in expect.items() if code != 0]
    return rows
```
<!-- 인용 끝 -->
