---
id: https://agentic-knowledge-base.dev/id/chunk/602ace1f-da3e-411a-84a5-e86d54a3320a
type: norm
level: logical
title_ko: docs/rules.md 절 development의 이어짐 — 정의 사이의 호출과 개발 KB 규칙 표
title: docs/rules.md development section continued — calls between definitions and the development KB rule table
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9740d5da-ea8e-4ebd-8e50-1e287cdba400
continues: true
form: table
columns: [규칙, 내용, 결정]
link_column: 결정
items: [p7-dev-plane-substance#3, p7-alternatives-mandatory#2, p7-decision-spans-three-levels#1, p6-transition-gates#1, p7-contract-first#1, p7-schema-derivation#1, p6-executable-splits-by-kb#1, p7-developer-requires-concrete#1, p7-decision-supersession#1, p7-dev-kb-completion#1, p7-dev-roles-and-scopes#1]
---
**정의 사이의 호출은 `usesDefinition`으로 올라온다**(유저 답 2026-09-30). 정의 청크의
선택 키 `uses`가 같은 모듈의 최상위 정의를 가리키고 추출기가 AST의 이름 참조에서 낸다 — `references` 족의 잎이라 Bazel `deps`도
링크 개체도 아니고 링크는 그대로 파일 복합체의 것이다. 방출의 경계는 `defs/kb.bzl`의 `EXTRACTED_SOURCES`(단일 정의처 — `RESIDENCY`와 같은 해법, 2026-10-01)이고 37 파일 전부이며
실측 트리플 476이다. `BUILD.bazel`은 그 리터럴을 load하고 `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 `uses`
방출 경계를 파생한다 — 상수를 둘로 두지 않는다. `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의 집합과
그 목록이 같은지 로드 시점에 강제해 갈리면 bazel 명령이 바로 fail한다. **치역 경계는 선언이다**(유저 답 1, 2026-10-01). `uses`의 치역은 같은 모듈의 최상위 정의와 `defs/kb.bzl`의 `USES_TARGETS`가 선언한
모듈의 최상위 정의다 — 표본 쌍은 `kb_lib` 하나이고 넓히기는 그 리터럴에 이름을 더하는 것이다. 모듈 밖 해소는 최상위 import와
정의 안의 늦은 import가 묶은 이름을 보고 `kb_lib.<이름>`(별칭 포함)과 `from kb_lib import <이름>`의 `Load` 참조를 대상 모듈
등록부의 uuid로 푼다. 실측 `agt:usesDefinition` 667(모듈 안 484 · 모듈 간 183, 치역은 전부 `kb_lib`), 오탐 0 · 누락 0(표본 30 +
독립 대조). 채널이 든 사례(`pct`)는 이제 **호출부 12**로 잡힌다. **남은 사각지대는 셋이다** — ① 치역 경계 밖의 모듈(전부로
넓히면 +52, 그 대부분이 `chunk2kg` 43) ② 함수를 인자로 넘기는 간접 호출(17 표현식 — 넘기는 쪽은 잡히고 받는 쪽은 아니다)
③ 정의가 아닌 이름(상수·모듈 변수)을 쓰는 관계 — 정의 청크가 없어 어느 경계에서도 올라오지 않는다. 표본 `tools/kb_lib.py`(청크 100·복합체 25)의 churn 실측(uuid 정체성 성립)을 근거로 같은 날 `tools/*.py` 전부로 넓혔다 — **37 파일 전부** · 청크 624 · 복합체 184, 파일마다 드리프트 테스트 `//:extract_drift_<모듈>`(묶음 `//:extract_drift_test`). 절 주석은 최소 하나다(파일 복합체의 부분이 둘 이상). 클래스는 정의 청크 하나이고 실측 최대 85줄이다. 200줄을 넘던 `main` 둘(`consistency`·`metrics`)은 상한을 올리지 않고 나눴다 — 산출물 바이트 동일.
