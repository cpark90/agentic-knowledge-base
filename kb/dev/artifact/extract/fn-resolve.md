---
id: https://agentic-knowledge-base.dev/id/chunk/73d61c8c-9a76-4703-8890-b1aa00936a4e
type: artifact
level: executable
title_ko: 함수 resolve (tools/extract.py)
title: function resolve in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `resolve(reg, names, hashes, pkg_dir, check)` 다. 등록부 갱신 규칙 (a)~(d).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve(reg: dict, names: list[str], hashes: dict[str, str], pkg_dir: Path, check: bool) -> Ids:
    """등록부 갱신 규칙 (a)~(d). 개명·삭제는 사람의 편집이므로 안내만 하고 등록부를 고치지 않는다."""
    want, have = set(names), set(reg["ids"])
    gone = sorted(have - want)          # 등록부에 있는데 소스에 없는 이름
    fresh = sorted(n for n in names if n not in have)
    prev = previous_hashes(pkg_dir)
    renames = []
    for q in fresh:
        was = prev.get(hashes.get(q, ""))
        if was and was in gone:
            renames.append((was, q))
            if "composite:" + was in gone and "composite:" + q in fresh:  # 절 복합체의 키는 절 청크의 키를 따른다
                renames.append(("composite:" + was, "composite:" + q))
    if renames:
        raise ExtractError(f"{reg['source']}: 개명이다 — 본문이 같고 이름만 바뀐 정의가 {len(renames)}건이다. 등록부 "
                           f"{registry_path(reg)} 의 `ids` 에서 "
                           + " · ".join(f"`{a}` → `{b}`" for a, b in renames)
                           + " 로 키를 고친다 (uuid 는 그대로 — 정체성은 uuid 이고 이름은 그 위의 라벨이다, "
                             "p10-split-keeps-work-identity). 정체성의 변경은 사람의 편집이므로 생성기가 하지 않는다")
    left = [g for g in gone if g not in {a for a, _ in renames}]
    if left:
        raise ExtractError(f"{reg['source']}: 등록부에 있는데 소스에 없는 이름이 {len(left)}건이다 — "
                           + " · ".join(f"`{g}`" for g in left)
                           + f". 삭제는 등록부 {registry_path(reg)} 의 `ids` 에서 그 키를 지우는 "
                             "명시 행위다 — 생성기가 정체성을 버리지 않는다")
    if check and fresh:
        raise ExtractError(f"{reg['source']}: 등록부에 없는 새 이름이 {len(fresh)}건이다 — "
                           + " · ".join(f"`{n}`" for n in fresh[:8]) + (" …" if len(fresh) > 8 else "")
                           + ". `bazel run //tools:extract -- " + reg["source"] + "` 를 돌려 등록한다 (신설은 자동이다)")
    return Ids(reg["ids"])
```
<!-- 인용 끝 -->
