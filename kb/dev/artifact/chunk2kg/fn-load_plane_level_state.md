---
id: https://agentic-knowledge-base.dev/id/chunk/e1d9652e-f3b3-470b-bf7f-f8fa31f8be68
type: artifact
level: executable
title_ko: 함수 load_plane_level_state (tools/chunk2kg.py)
title: function load_plane_level_state in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24
---
**함수** — `load_plane_level_state(path)` 다. `defs/kb.bzl` 의 `PLANES`·`LEVELS`·`STATES` 리터럴을 읽어 값 어휘를 선언 순서 그대로 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_plane_level_state(path) -> tuple[list[str], list[str], list[str]]:
    """`defs/kb.bzl` 의 `PLANES`·`LEVELS`·`STATES` 리터럴을 읽어 값 어휘를 선언 순서 그대로 돌려준다.

    수준 허용표(RESIDENCY)와 같은 결정(M1 단일 정의처, 2026-09-26)이다 — Starlark 는 파일을 읽지 못해 분석 시점
    판정(`_check_residency`)에 쓰이는 그 표가 원본이고, 파이썬 쪽은 `ast.literal_eval` 로 리터럴을 읽어 파생한다.
    이 도구는 rdflib 없이 타깃마다 돌아(head 액션, kb.bzl 의 kb_chunk·kb_decision) kb_lib 를 import 할 수 없으므로
    (위 try/except) 표준 라이브러리만으로 그 리터럴을 여기서 읽는다 — 리터럴 읽기 함수의 정의처는 이 도구 하나이고,
    `tools/kb_lib.py` 의 `load_residency` 는 PLANES·LEVELS 를 구할 때 이 함수를 import 해 쓴다(정의처를 하나로 모은
    형태 — `weave`·`extract_refs` 가 이 파일을 srcs 로 끌어 쓰는 것과 같은 방식). 경로가 없거나 못 읽으면
    OSError(운영체제가 낸다), 표를 못 읽으면 ValueError — 둘 다 판정 불가지 통과가 아니라 호출자가 그대로 죽는다.
    호출자는 이 결과를 **자기 상태에 반영해야만** 쓰인다 — 이 함수는 읽기만 하고 아무 전역도 바꾸지 않는다
    (chunk2kg 자신은 apply_plane_level_state 로 반영한다).
    """
    text = Path(path).read_text(encoding="utf-8")
    names = {m.group(1): ast.literal_eval(m.group(2)) for m in _KB_BZL_LIST.finditer(text)}
    missing = [w for w in ("PLANES", "LEVELS", "STATES") if w not in names]
    if missing:
        raise ValueError(f"{path}: {', '.join(missing)} 리스트를 찾을 수 없다")
    return names["PLANES"], names["LEVELS"], names["STATES"]
```
<!-- 인용 끝 -->
