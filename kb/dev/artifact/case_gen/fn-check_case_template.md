---
id: https://agentic-knowledge-base.dev/id/chunk/eb325ac3-9126-44e4-977b-2da002c1b35a
type: artifact
level: executable
title_ko: 함수 check_case_template (tools/case_gen.py)
title: function check_case_template in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T12:40:09Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516
---
**함수** — `check_case_template(where, case, keep)` 다. `case` 템플릿의 형식과 `${변수}` 의 실재.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_case_template(where: str, case, keep: dict) -> list[str]:
    """`case` 템플릿의 형식과 `${변수}` 의 실재."""
    if not isinstance(case, dict):
        return [f"{where}: `case` 는 매핑이다 — 키는 {' · '.join(CASE_KEYS)} 다"]
    errs = [f"{where}: `case` 의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(CASE_KEYS)} 다" for k in case if k not in CASE_KEYS]
    errs += [f"{where}: `case` 에 `{k}` 가 없다" for k in CASE_REQUIRED if not isinstance(case.get(k), str) or not case.get(k).strip()]
    if not str(case.get("criteria", "")).startswith(CHUNK_NS):
        errs.append(f"{where}: `case.criteria` 는 기준 청크 IRI 다 — 케이스는 기준을 `refines` 한다 (p8-pass-criteria)")
    ver = case.get("verifies", [])
    if not isinstance(ver, list) or any(not str(x).startswith(CHUNK_NS) for x in ver):
        errs.append(f"{where}: `case.verifies` 는 청크 IRI 목록이다")
    der = case.get("derivesFrom", [])
    if not isinstance(der, list) or any(not str(x).startswith(CHUNK_NS) for x in der):
        errs.append(f"{where}: `case.derivesFrom` 는 청크 IRI 목록이다")
    files = case.get("files", {})
    if not isinstance(files, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in files.items()):
        errs.append(f"{where}: `case.files` 는 `이름: 내용` 문자열 매핑이다")
    for cls in CLASSES:
        c = case.get(cls)
        if c is None:
            continue
        if not isinstance(c, dict) or set(c) - set(CLASS_KEYS) or not isinstance(c.get("prose"), str) or not isinstance(c.get("expect"), list):
            errs.append(f"{where}: `case.{cls}` 는 {{prose: 문자열, expect: 목록}} 이다")
    used = set(TEMPLATE.findall(json.dumps(case, ensure_ascii=False)))
    errs += [f"{where}: 템플릿의 `${{{u}}}` 가 keep 의 변수가 아니다" for u in sorted(used - set(keep))]
    return errs
```
<!-- 인용 끝 -->
