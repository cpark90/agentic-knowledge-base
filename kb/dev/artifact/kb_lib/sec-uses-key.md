---
id: https://agentic-knowledge-base.dev/id/chunk/8cbfc00d-5819-4b78-a0a8-ad654ef6a56c
type: artifact
level: executable
title_ko: 절 uses-key (tools/kb_lib.py)
title: section uses-key in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `uses-key` 다. 정의 청크의 호출 관계 (`uses`) — references 족의 잎 agt:usesDefinition (유저 답 2026-09-30, 채널 uses-definition)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 정의 청크의 호출 관계 (`uses`) — references 족의 잎 agt:usesDefinition (유저 답 2026-09-30, 채널 uses-definition) ────
# 코드 청크가 어느 최상위 정의를 이름으로 쓰는지를 frontmatter `uses: [<청크 IRI>…]` 로 적고 — 같은 모듈의 정의와
# 치역 경계(`USES_TARGETS`) 안의 모듈의 정의가 그 대상이다 —
# chunk2kg 가 agt:usesDefinition 을 방출한다. 값의 원본은 손이 아니라 추출기다 — tools/extract.py 가 정의의 AST 에서 낸다.
# **링크 키가 아니다**(references 족, 확장 규칙 2026-09-26): Bazel deps(gen_build.LINKS)도 링크 개체(agt:Link)도 되지 않아
# 함수 churn 이 빌드 그래프를 움직이지 않는다 — 링크는 파일 복합체의 것이다 (p7-code-links-on-file-composite).
# 대상 실재는 validate check_dangling 이 보고, 본문이 바뀐 대상을 가리키는 출발점은 revalidate 가 `호출부` 열로 낸다.
USES_KEY = "uses"
USES_PREDICATE = "agt:usesDefinition"
# 경계는 둘이고 둘 다 `defs/kb.bzl` 에 산다. **방출 경계** `EXTRACTED_SOURCES` 는 어느 소스에서 `uses` 를
# 내는가이고 — 표본 하나(`tools/kb_lib.py`, 트리플 54)에서 먼저 내고 링크 밀도·게이트 시간을 잰 뒤(유저 답 1,
# 2026-09-30) 37 파일 전부로 넓혔다 — **치역 경계** `USES_TARGETS` 는 모듈 밖의 어느 모듈을 가리킬 수 있는가다
# (유저 답 1, 2026-10-01 — 표본 쌍 `kb_lib` 하나부터). **단일 정의처는 그 두 리터럴**이다(M1,
# RESIDENCY·load_residency 와 같은 해법) — 여기 손으로 목록을 적지 않는다. `load_extracted_sources` 가 이름으로
# 지정된 리터럴을 읽어 돌려주고, 호출자(`tools/extract.py`)가 `tools/<이름>.py`(방출 경계)·대상 모듈의
# 등록부(치역 경계)로 옮긴다. `BUILD.bazel`(`//tools:tools` 패키지의 `check_extracted_sources`)이 등록부 사이드카의
# 존재와 방출 경계가 같은 집합인지, 치역 경계가 그 부분집합인지 로드 시점에 강제하므로, 갈리면 `uses` 가 조용히
# 비기 전에 bazel 명령이 먼저 죽는다.
USES_SOURCES_NAME = "EXTRACTED_SOURCES"  # 방출 경계 리터럴의 이름
USES_TARGETS_NAME = "USES_TARGETS"       # 치역 경계 리터럴의 이름
```
<!-- 인용 끝 -->
