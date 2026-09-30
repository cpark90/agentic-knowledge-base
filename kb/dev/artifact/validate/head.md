---
id: https://agentic-knowledge-base.dev/id/chunk/f78b9e0e-d84b-4087-9f1d-29bcf769d844
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/validate.py)
title: module head agt in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/f7ac5761-e5da-4a34-8beb-f661f8164328, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
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
```
<!-- 인용 끝 -->
