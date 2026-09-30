---
id: https://agentic-knowledge-base.dev/id/chunk/8cbfc00d-5819-4b78-a0a8-ad654ef6a56c
type: artifact
level: executable
title_ko: 절 uses-key (tools/kb_lib.py)
title: section uses-key in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893
---
**절** — `tools/kb_lib.py` 의 절 `uses-key` 다. 정의 청크의 호출 관계 (`uses`) — references 족의 잎 agt:usesDefinition (유저 답 2026-09-30, 채널 uses-definition)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 정의 청크의 호출 관계 (`uses`) — references 족의 잎 agt:usesDefinition (유저 답 2026-09-30, 채널 uses-definition) ────
# 코드 청크가 같은 모듈의 어느 최상위 정의를 이름으로 쓰는지를 frontmatter `uses: [<청크 IRI>…]` 로 적고
# chunk2kg 가 agt:usesDefinition 을 방출한다. 값의 원본은 손이 아니라 추출기다 — tools/extract.py 가 정의의 AST 에서 낸다.
# **링크 키가 아니다**(references 족, 확장 규칙 2026-09-26): Bazel deps(gen_build.LINKS)도 링크 개체(agt:Link)도 되지 않아
# 함수 churn 이 빌드 그래프를 움직이지 않는다 — 링크는 파일 복합체의 것이다 (p7-code-links-on-file-composite).
# 대상 실재는 validate check_dangling 이 보고, 본문이 바뀐 대상을 가리키는 출발점은 revalidate 가 `호출부` 열로 낸다.
USES_KEY = "uses"
USES_PREDICATE = "agt:usesDefinition"
# 방출의 경계 — 이 표에 든 소스에서만 `uses` 를 낸다 (유저 답 2026-09-30: 표본 하나에서 먼저 내고 링크 밀도·게이트
# 시간을 잰 뒤 넓힌다). 추출기는 하나이므로 경계를 두지 않으면 37 파일이 한꺼번에 들어온다 — 그것이 배제된 선택지 3이다.
# 넓히기는 이 표에 소스를 **더하는** 것이다: 표를 지워 "전부"로 읽게 하지 않는다 — 어디까지 쟀는지가 표에 남아야 한다.
USES_SOURCES = ("tools/kb_lib.py",)
```
<!-- 인용 끝 -->
