---
id: https://agentic-knowledge-base.dev/id/chunk/4fa89da6-040b-46a2-8dda-692155b66811
type: artifact
level: executable
title_ko: 함수 case_spec (tools/vv_run.py)
title: function case_spec in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `case_spec(body)` 다. 본문의 규약 `yaml` 펜스 → ({files, expect}, 형식 오류 목록).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def case_spec(body: str) -> tuple[dict, list[str]]:
    """본문의 규약 `yaml` 펜스 → ({files, expect}, 형식 오류 목록). 규약 키가 없는 펜스는 산문의 예시라 읽지 않는다 (점진 도입)."""
    spec: dict = {}
    errs: list[str] = []
    for raw in yaml_blocks(body):
        if not SPEC_HEAD.search(raw):
            continue
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError as e:
            errs.append(f"`yaml` 펜스를 읽을 수 없다 — {e}")
            continue
        if not isinstance(data, dict):
            errs.append(f"`yaml` 펜스는 매핑이어야 한다 — 키는 {' · '.join(SPEC_KEYS)} 다")
            continue
        for k in data:
            if k not in SPEC_KEYS:
                errs.append(f"`yaml` 펜스의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(SPEC_KEYS)} 뿐이다")
            elif k in spec:
                errs.append(f"키 `{k}` 가 펜스 둘에 있다 — 한 케이스에 하나다")
            else:
                spec[k] = data[k]
    files = spec.get("files")
    if files is not None:
        if not isinstance(files, dict) or not files:
            errs.append("`files` 는 비어 있지 않은 `이름: 내용` 매핑이어야 한다")
            spec.pop("files")
        else:
            for name, content in files.items():
                if not isinstance(name, str) or not FILE_NAME.fullmatch(name):
                    errs.append(f"`files` 의 이름 `{name}` 이 단순 파일 이름이 아니다 — 경로는 검증기가 정한다 (영숫자·`.`·`_`·`-`)")
                elif not isinstance(content, str):
                    errs.append(f"`files` 의 `{name}` 내용이 문자열이 아니다 — 파일 내용을 그대로 적는다")
    expect = spec.get("expect")
    if expect is not None:
        if not isinstance(expect, list) or not expect:
            errs.append("`expect` 는 명령 순서대로의 비어 있지 않은 목록이어야 한다")
            spec.pop("expect")
        else:
            for i, e in enumerate(expect, start=1):
                if not isinstance(e, dict):
                    errs.append(f"`expect` {i}번째 항목이 매핑이 아니다 — 키는 {' · '.join(EXPECT_KEYS)} 다")
                    continue
                for k in e:
                    if k not in EXPECT_KEYS:
                        errs.append(f"`expect` {i}번째의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(EXPECT_KEYS)} 뿐이다")
                if e.get("exit") is not None and not isinstance(e["exit"], int):
                    errs.append(f"`expect` {i}번째의 `exit` 는 정수여야 한다 — 실제 `{e['exit']}`")
                c = e.get("contains")
                if c is not None and not (isinstance(c, str) or (isinstance(c, list) and all(isinstance(x, str) for x in c))):
                    errs.append(f"`expect` {i}번째의 `contains` 는 문구 하나 또는 문구 목록이어야 한다")
    return spec, errs
```
<!-- 인용 끝 -->
