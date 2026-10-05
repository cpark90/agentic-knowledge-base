---
id: https://agentic-knowledge-base.dev/id/chunk/f78b9e0e-d84b-4087-9f1d-29bcf769d844
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/validate.py)
title: module head agt in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fb7cffc9-e5b5-4ed5-af22-40aa50e3c6aa
---
**모듈 머리** — `tools/validate.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = kb_lib.AGT
_FM_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):")  # frontmatter 의 최상위 키 (element-drop)
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음·파싱 불가 입력
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건
# 게이트 id — 단일 정의처는 `defs/kb.bzl` 의 `GATES` 리터럴이고 `kb_lib` 이 리터럴 읽기로 파생한다 (M1, 2026-10-02).
# 여기에 문자열을 적지 않는다 — 리터럴에 없는 id 는 이 줄에서 적재 시점에 죽고, 리터럴 밖의 태그는 게이트
# `gate-registry` 가 거부한다. `VALIDATE_TAG` 는 게이트가 아니라 이 도구 자신의 집계·배선 태그다.
LABELS = kb_lib.LABELS_GATE
BOUNDARY = kb_lib.BOUNDARY_GATE
VOCAB = kb_lib.VOCAB_GATE
ODD_REF = kb_lib.ODD_REF_GATE
DANGLING = kb_lib.DANGLING_GATE
VERIFY = kb_lib.VERIFY_GATE
SYNTAX = kb_lib.SYNTAX_GATE
SHACL = kb_lib.SHACL_GATE
GATE_REGISTRY = kb_lib.GATE_REGISTRY_GATE
VALIDATE_TAG = kb_lib.VALIDATE_TAG
```
<!-- 인용 끝 -->
