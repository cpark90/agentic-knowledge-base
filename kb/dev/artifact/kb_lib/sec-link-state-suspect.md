---
id: https://agentic-knowledge-base.dev/id/chunk/ad732d7b-a214-41bd-83ad-05e232235dec
type: artifact
level: executable
title_ko: 절 link-state-suspect (tools/kb_lib.py)
title: section link-state-suspect in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/749019ce-0d81-4c5f-b549-f44c1b0d4e55
composite: {id: https://agentic-knowledge-base.dev/id/composite/749019ce-0d81-4c5f-b549-f44c1b0d4e55, title_ko: 절 복합체 link-state-suspect (tools/kb_lib.py), title: section composite link-state-suspect in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/ad732d7b-a214-41bd-83ad-05e232235dec, https://agentic-knowledge-base.dev/id/chunk/8b1b0dcd-b04d-42f6-a3d6-849e3fe97268, https://agentic-knowledge-base.dev/id/chunk/9a2cd33a-ee49-4782-81c9-519aaf5a1621, https://agentic-knowledge-base.dev/id/chunk/b76ee239-c1db-4b7d-b6f0-0f35e7ce919f], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `link-state-suspect` 다. 링크 상태의 물질화 — suspect 는 저장값이 아니라 평가 결과다 (노트 9.11절, link-state-ontology agt:linkState)

**정의** — `_when_tokens` · `odd_states` · `when_eval` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 링크 상태의 물질화 — suspect 는 저장값이 아니라 평가 결과다 (노트 9.11절, link-state-ontology agt:linkState) ────
# 그래프에 적히는 linkState 는 candidate·confirmed·invalid 셋뿐이다. suspect 는 두 경로의 평가 결과이고 생성물
# (assume_check 의 보고 · metrics 의 포화율)에서만 물질화된다 — 저장하면 그래프와 판정이 어긋나고 이 저장소의 생성물은
# bazel-out 에만 있다. 두 경로는 (a) `when` 이 거짓인 확정 링크 · (b) 선언된 트리거가 지목한 확정 링크다.
LINK_STATE_SUSPECT = "suspect"
# `when` 판정식의 범위는 **ODD 속성 참조의 판정**이다 (CEL 전체가 아니다). 항은 `in(<ODD 속성명 | cond 슬러그 | 조건 IRI>)`
# 하나이고 결합은 CEL 연산자 `!`·`&&`·`||` 와 괄호이며 리터럴 `true`·`false` 를 받는다. 비교·산술·함수 호출·ODD 밖 이름은
# 판정하지 않고 unverified 로 남긴다 — 판정 불가를 참으로 읽으면 무효화가 조용히 멈춘다 (0.4절 restrictive).
WHEN_TRUE, WHEN_FALSE, WHEN_UNVERIFIED = "true", "false", "unverified"
# 생성 문서에 그대로 인용되므로 연산자는 코드 스팬으로 감싼다 — 맨 `!` 는 산문의 감탄으로 읽혀 gendoc 이 거부한다
WHEN_GRAMMAR = "`in(<ODD 속성명 | cond 슬러그 | 조건 IRI>)` · `!` · `&&` · `||` · `( )` · `true` · `false`"
_WHEN_IN = re.compile(r"in\s*\(\s*([A-Za-z0-9_:\-./]+)\s*\)")
_WHEN_OP = re.compile(r"&&|\|\||!|\(|\)")
_WHEN_LIT = re.compile(r"(?:true|false)(?![A-Za-z0-9_])")
_WHEN_OTHER = re.compile(r"[^\s()!&|]+|.")
```
<!-- 인용 끝 -->
