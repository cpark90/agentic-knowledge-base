---
id: https://agentic-knowledge-base.dev/id/chunk/7cd61807-8e8e-44e7-a140-c95f9f82e4f9
type: artifact
level: executable
title_ko: 함수 check_gate_registry (tools/validate.py)
title: function check_gate_registry in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/386f974f-846c-47c9-99dc-ee866783f5c5, https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e, https://agentic-knowledge-base.dev/id/chunk/e9c220ba-d7c1-4597-a620-d9ad84df3644, https://agentic-knowledge-base.dev/id/chunk/fd705af7-dd6d-489f-9d6f-620aecadba08]
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_gate_registry(gates_path, sources)` 다. 게이트 id 의 단일 정의처 — 코드의 태그 집합이 `GATES`·`TOOL_TAGS` 리터럴과 같은가 (게이트 `gate-registry`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gate_registry(gates_path: str, sources: list[str]) -> list[str]:
    """게이트 id 의 단일 정의처 — 코드의 태그 집합이 `GATES`·`TOOL_TAGS` 리터럴과 같은가 (게이트 `gate-registry`).

    `residency`·`token-budget` 과 같은 형이다. 원본은 `defs/kb.bzl` 의 두 리터럴이고 파이썬 쪽은 그것을 읽어
    상수를 파생한다. 2026-10-01 실측에서 같은 목록이 넷으로 갈려 있었으므로(상수 26 · 코드의 태그 · 총람의
    `id` 열 · 하네스 목록) 네 방향을 본다 — ① 등록부 밖의 태그, ② 손으로 둔 `*_GATE` 상수, ③ `getattr`
    폴백의 값 드리프트, ④ 등록됐으나 코드에 닿지 않는 id. ④ 의 도달은 태그 자신 또는 파생 상수 이름이다.
    판정 도구가 파이썬 밖인 게이트(`starlark`·`bazel`)는 태그를 찍을 자리가 없어 ④ 에서 빠진다.
    """
    gate = GATE_REGISTRY
    try:
        gates = kb_lib.load_gates(gates_path)
        tool_tags = kb_lib.load_tool_tags(gates_path)
    except (OSError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] {gates_path}: 게이트 등록부를 읽을 수 없다 — {e}") from e
    pys = [Path(s) for s in sources if Path(s).suffix == ".py"]
    if not pys:
        raise ConfigFailure(f"[{gate}] --gate-sources 에 파이썬 소스가 없다 — 태그 전수를 볼 대상이 비면 판정이 아니다")
    try:
        hits = kb_lib.scan_gate_tags(pys)
    except (OSError, SyntaxError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] 태그를 훑을 수 없다 — {e}") from e
    registered = set(gates) | set(tool_tags)
    outside = kb_lib.load_bzl_list(gates_path, "GATE_TOOLS_OUTSIDE_PYTHON")  # 파이썬 밖의 판정 도구 — 태그 자리가 없다
    errors = []
    for tag in sorted(set(hits) - registered):
        errors.append(f"[{gate}] {hits[tag][0]}: 태그 `{tag}` 가 {gates_path} 의 GATES·TOOL_TAGS 밖이다 — "
                      f"게이트면 GATES 에, 입력 문제·보고 태그면 TOOL_TAGS 에 등재한다 (단일 정의처는 그 리터럴이다)")
    hand = re.compile(r"^([A-Z][A-Z0-9_]*_GATE)\s*=\s*[\"']([a-z0-9-]+)[\"']", re.M)
    fallback = re.compile(r"getattr\(\s*kb_lib\s*,\s*[\"']([A-Z][A-Z0-9_]*_GATE)[\"']\s*,\s*[\"']([a-z0-9-]+)[\"']")
    by_name = {kb_lib.gate_constant_name(g): g for g in gates}
    per_file: dict[str, str] = {}
    text = ""
    for p in pys:
        body = p.read_text(encoding="utf-8")
        per_file[p.stem] = body
        text += body
        for name, value in hand.findall(body):
            errors.append(f"[{gate}] {p.as_posix()}: 상수 {name} 에 게이트 id {value!r} 를 손으로 적었다 — "
                          f"{gates_path} 의 GATES 가 단일 정의처이고 kb_lib 이 그 리터럴로 파생한다 (kb_lib.{name})")
        for name, value in fallback.findall(body):
            want = by_name.get(name)
            if want is None:
                errors.append(f"[{gate}] {p.as_posix()}: 폴백 {name} 에 대응하는 게이트가 GATES 에 없다 — "
                              f"리터럴에 등재하거나 폴백을 지운다")
            elif want != value:
                errors.append(f"[{gate}] {p.as_posix()}: 폴백 {name} 의 값 {value!r} 가 GATES 의 {want!r} 와 갈린다 — "
                              f"폴백은 리터럴과 같은 값이어야 한다 (rdflib 없이 도는 생성기의 선언된 예외다)")
    for gid, spec in sorted(gates.items()):
        if spec.get("tool") in outside:
            continue
        own = per_file.get(spec.get("tool"), "")  # 판정 도구가 자기 소스에 id 를 적은 꼴(rdflib 없이 도는 생성기)
        if gid in hits or kb_lib.gate_constant_name(gid) in text or f'"{gid}"' in own or f"'{gid}'" in own:
            continue
        errors.append(f"[{gate}] {gates_path}: 게이트 `{gid}` 가 코드에 닿지 않는다 — 태그도 파생 상수 "
                      f"kb_lib.{kb_lib.gate_constant_name(gid)} 도 없다. 판정 도구가 찍지 않는 게이트는 게이트가 아니다")
    for tag in sorted(tool_tags):
        if tag in hits or (tag.replace("-", "_").upper() + "_TAG") in text:
            continue
        errors.append(f"[{gate}] {gates_path}: 도구 태그 `{tag}` 가 코드에 닿지 않는다 — 쓰이지 않는 태그는 지운다")
    names = {p.stem for p in pys}
    for gid, spec in sorted(gates.items()):
        tool = spec.get("tool")
        if tool in outside or tool in names:
            continue
        errors.append(f"[{gate}] {gates_path}: 게이트 `{gid}` 의 판정 도구 `{tool}` 가 실재하지 않는다 — "
                      f"`tools/{tool}.py` 이거나 파이썬 밖(starlark·bazel) 중 하나다")
    return errors
```
<!-- 인용 끝 -->
