---
id: https://agentic-knowledge-base.dev/id/chunk/602ace1f-da3e-411a-84a5-e86d54a3320a
type: norm
level: logical
title_ko: docs/rules.md 절 development의 이어짐 — 정의 사이의 호출과 개발 KB 규칙 표
title: docs/rules.md development section continued — calls between definitions and the development KB rule table
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9740d5da-ea8e-4ebd-8e50-1e287cdba400
continues: true
form: table
columns: [규칙, 내용, 결정]
link_column: 결정
items: [p7-dev-plane-substance#3, p7-alternatives-mandatory#2, p7-decision-spans-three-levels#1, p6-transition-gates#1, p7-contract-first#1, p7-schema-derivation#1, p6-executable-splits-by-kb#1, p7-developer-requires-concrete#1, p7-decision-supersession#1, p7-dev-kb-completion#1, p7-dev-roles-and-scopes#1]
---
**정의 사이의 호출은 `usesDefinition`으로 올라온다** (유저 답 2026-09-30). 정의의 선택 키 `uses`는 같은 모듈의
최상위 정의를 가리키고, 추출기가 AST의 이름 참조에서 그 값을 낸다. `uses`는 `references` 족의 잎이므로 Bazel `deps`도
링크 개체도 아니며, 링크는 그대로 파일 복합체가 갖는다. 방출의 경계는 `defs/kb.bzl`의 `EXTRACTED_SOURCES`이고, 이 경계는
37 파일 전부를 덮으며 측정한 트리플은 476이다. `EXTRACTED_SOURCES`는 `RESIDENCY`와 같은 해법으로 둔 단일 정의 위치다
(2026-10-01). `BUILD.bazel`은 그 리터럴을 load하고 `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 `uses`
방출 경계를 파생하므로, 상수를 둘로 두지 않는다. 또한 `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의
집합과 그 목록이 같은지를 로드 시점에 강제하므로, 둘이 갈리면 bazel 명령이 바로 실패한다.

**치역 경계는 선언이다** (유저 답 1, 2026-10-01). `uses`의 치역은 같은 모듈의 최상위 정의와, `defs/kb.bzl`의
`USES_TARGETS`가 선언한 모듈의 최상위 정의다. 표본 쌍은 `kb_lib` 하나이고, 치역을 넓히려면 그 리터럴에 이름을 더한다.
모듈 밖 해소는 최상위 import와 정의 안의 늦은 import가 묶은 이름을 보고, 별칭을 포함한 `kb_lib.<이름>`과
`from kb_lib import <이름>`의 `Load` 참조를 대상 모듈 등록부의 uuid로 푼다. 측정한 `agt:usesDefinition`은 667이다.
모듈 안이 484, 모듈 간이 183이고 치역은 전부 `kb_lib`이며, 표본 30과 독립 대조에서 오탐과 누락은 모두 0이었다. 채널이 든
사례인 `pct`는 이제 **호출부 12**로 잡힌다.

**남은 사각지대는 셋이다.** 첫째는 치역 경계 밖의 모듈이고, 전부로 넓히면 52가 늘며 그 대부분이 `chunk2kg`의 43이다.
둘째는 함수를 인자로 넘기는 간접 호출 17 표현식이고, 넘기는 쪽은 잡히지만 받는 쪽은 잡히지 않는다. 셋째는 정의가 아닌
이름인 상수와 모듈 변수를 쓰는 관계이고, 그 이름에는 정의가 없어 어느 경계에서도 올라오지 않는다.

단위 지식 100과 복합체 25로 된 표본 `tools/kb_lib.py`의 churn을 측정해 uuid 정체성이 성립함을 확인했고, 이를 근거로 같은 날
대상을 `tools/*.py` 전부로 넓혔다. 그 결과는 **37 파일 전부**, 단위 지식 624, 복합체 184이고, 파일마다 드리프트 테스트
`//:extract_drift_<모듈>`이 있고 그 묶음은 `//:extract_drift_test`다. 절 주석은 최소 하나이므로 파일 복합체의 부분은 둘 이상이다.
클래스는 정의 하나로 올라오고 측정한 최대 길이는 85줄이다. 200줄을 넘던 `consistency`와 `metrics`의 `main` 둘은 상한을
올리지 않고 나눴으며, 나눈 뒤에도 산출물은 바이트 단위로 같다.
