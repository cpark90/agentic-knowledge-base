---
id: https://agentic-knowledge-base.dev/id/chunk/7b782704-6d75-4344-9b72-f812f73bbfb0
type: artifact
level: executable
title_ko: 함수 check_token_budget (tools/validate.py)
title: function check_token_budget in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/386f974f-846c-47c9-99dc-ee866783f5c5, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5, https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac]
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_token_budget(shapes, bzl_path, shape_paths, vocab)` 다. 본문 토큰 수 상한의 단일 정의처 — shape 가 `kb_lib.BODY_TOKEN_LIMITS` 와 같은 표인가 (게이트 `token-budget`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_token_budget(shapes: Graph, bzl_path: str, shape_paths: list[str], vocab: str = "") -> list[str]:
    """본문 토큰 수 상한의 단일 정의처 — shape 가 `kb_lib.BODY_TOKEN_LIMITS` 와 같은 표인가 (게이트 `token-budget`).

    `residency` 와 같은 형이다. 원본은 파이썬 쪽 표이고(게이트 chunk_lint 가 파일마다 그것으로 판정한다) shape 는
    그것의 RDF 표현이다. plane 은 shape 의 `sh:targetClass` 지역명 `<X>Chunk` 에서 읽는다. plane 목록은
    `defs/kb.bzl` 의 PLANES 이고, 표에 없는 plane 의 상한은 기본 1,092 토큰(42×26)이다
    (결정 p1-chunk-unit-is-tokens — 줄 상한 42·200 은 폐지됐다).
    `artifact`·`memory` 만 값이 다르다 — 본문이 저작이 아니라 소스·실행의 인용이기 때문이다
    (p7-code-extraction-direction "예산").
    **계수기도 이 게이트가 본다**: 토큰으로 적은 상한은 계수기가 고정되지 않으면 상한이 아니므로 어휘 파일의
    sha256 이 `kb_lib.TOKENIZER_VOCAB_SHA256` 과 같은지 대조한다 (ODD id:cond-tokenizer-lock).
    """
    from rdflib.namespace import SH

    gate = kb_lib.TOKEN_BUDGET_GATE
    where = ", ".join(shape_paths) or bzl_path
    try:
        planes, _levels, _table = kb_lib.load_residency(bzl_path)
    except (OSError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] {bzl_path}: plane 목록을 읽을 수 없다 — {e}") from e
    declared = {p: kb_lib.body_token_limit(p) for p in planes}
    found: dict[str, set[int]] = {}
    for shape, cls in shapes.subject_objects(SH.targetClass):
        plane = str(cls).split("/")[-1]
        if not plane.endswith("Chunk"):
            continue
        plane = plane[: -len("Chunk")].lower()
        for prop in shapes.objects(shape, SH.property):
            if (prop, SH.path, kb_lib.AGT.tokenCount) not in shapes:
                continue
            for v in shapes.objects(prop, SH.maxInclusive):
                found.setdefault(plane, set()).add(int(v))
    errors = []
    for plane in sorted(set(declared) | set(found)):
        want, have = declared.get(plane), found.get(plane)
        if want is None:
            errors.append(f"[{gate}] {where}: shape 가 plane {plane} 의 본문 상한을 {sorted(have)} 로 두는데 그런 plane 이 {bzl_path} 의 PLANES 에 없다")
        elif not have:
            errors.append(f"[{gate}] {where}: plane {plane} 의 본문 상한 {want} 토큰에 대응하는 shape 가 없다 — `agt:{plane.capitalize()}Chunk` 의 `agt:tokenCount` 에 `sh:maxInclusive {want}` 를 단다 (표의 원본은 tools/kb_lib.py 의 BODY_TOKEN_LIMITS 다)")
        elif have != {want}:
            errors.append(f"[{gate}] {where}: plane {plane} 의 본문 상한이 갈린다 — tools/kb_lib.py 의 BODY_TOKEN_LIMITS 는 {want}, shape 는 {sorted(have)} 다. 원본은 표이므로 shape 를 맞춘다")
    try:  # 계수기의 고정 — 상한의 단위가 토큰이므로 어휘 파일이 바뀌면 같은 수가 같은 뜻이 아니다
        path = kb_lib.tokenizer_vocab_path(vocab or None)
    except FileNotFoundError as e:
        raise ConfigFailure(f"[{gate}] 어휘 파일 — {e}") from e
    got = kb_lib.tokenizer_vocab_fingerprint(path)
    if got != kb_lib.TOKENIZER_VOCAB_SHA256:
        errors.append(f"[{gate}] {Path(path).as_posix()}: 어휘 파일의 sha256 {got} 가 고정값 "
                      f"{kb_lib.TOKENIZER_VOCAB_SHA256} 과 다르다 — 토큰으로 적은 상한이 재현되지 않는다 "
                      f"(ODD id:cond-tokenizer-lock, 고정처는 MODULE.bazel 의 http_file "
                      f"{kb_lib.TOKENIZER_VOCAB_REPO} 와 tools/kb_lib.py 의 TOKENIZER_VOCAB_SHA256)")
    return errors
```
<!-- 인용 끝 -->
