---
id: https://agentic-knowledge-base.dev/id/chunk/81db317b-9870-4a61-9167-ba1475fe3e19
type: artifact
level: executable
title_ko: 절 parse-chunk (tools/chunk2kg.py)
title: section parse-chunk in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
composite: {id: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94, title_ko: 절 복합체 parse-chunk (tools/chunk2kg.py), title: section composite parse-chunk in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/81db317b-9870-4a61-9167-ba1475fe3e19, https://agentic-knowledge-base.dev/id/chunk/f178c885-f133-4f49-a296-18b123272948, https://agentic-knowledge-base.dev/id/chunk/71a80c9a-cb89-49ce-ae62-9d1fda16125b, https://agentic-knowledge-base.dev/id/chunk/8c320bc2-87f7-43f5-9492-fe4086b13e7c, https://agentic-knowledge-base.dev/id/chunk/a13334ee-3c25-4384-bac2-a81868a47526, https://agentic-knowledge-base.dev/id/chunk/03312fa3-ef91-4e77-b39e-47c5554aba7e], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `parse-chunk` 다. 청크 파싱

**정의** — `parse_chunk` · `split_outside_brackets` · `parse_map` · `split_top_level` · `parse_value` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 청크 파싱 ────────────────────
# frontmatter 의 키 — 이 절의 `parse_chunk` 가 판정하는 것 (OKF v0.2 번들: type·status·generated·verified 는
# 그 스펙의 필드명이다). 링크 키는 `링크의 방출과 정체성` 절, 복합체 키는 `복합체의 순서` 절이 적는다.
# 형식은 YAML 부분집합이다 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}.
#   iri:          항목 IRI (필수)
#   type:         requirement | decision | contract | schema | artifact | annotation | memory (필수, OKF).
#                 예외 하나가 `agt:Space` 다 — plane 이름이 아니라 온톨로지 클래스 이름이고, 그 청크는 설계 공간(`-space`)이라
#                 본문의 후보·제약까지 읽어야 그래프가 된다. 여기서는 frontmatter 만 판정하고(level 은 logical 고정) 방출은
#                 tools/space2kg.py 가 한다 — 이 도구에 넘기면 `FAIL [space]` 다 (결정 p9-candidate-storage)
#   level:        functional | abstract | logical | concrete | executable (필수)
#   title_ko:     한글 라벨 (필수) — OKF 확장 키
#   title:        영어 라벨 (필수) — OKF title
#   status:       draft | stable | suspect | invalidated | deprecated (필수, OKF + 확장 2)
#   generated:    {by: <행위자>, at: <ISO 8601>} (필수, OKF)
#   verified:     [{by: <행위자>, at: <ISO 8601>}, ...] (선택, OKF) — human: 접두어가 사람 검토
#   assumes:      가정 IRI 목록 (선택)
#   sources:      OKF v0.2 sources — [{resource: IRI, id?, title?, author?}] (선택). resource → prov:wasDerivedFrom
#   uses:         이 정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 청크 IRI 목록 (선택, type: artifact 에서만 —
#                 agt:usesDefinition 의 정의역이 agt:ArtifactChunk 다). agt:usesDefinition 으로 나간다. 링크 키가 아니다 —
#                 Bazel deps 도 링크 개체도 되지 않는다(링크는 파일 복합체의 것이다, p7-code-links-on-file-composite).
#                 값의 원본은 손이 아니라 tools/extract.py 이고 대상 실재는 validate check_dangling 이 본다
#   layer:        knowledge | methodology | process (선택, plane 제한 없음) — 이 항목이 서비스의 어느 층에서 역할을
#                 갖는가 (결정 p0-service-is-a-three-layer-wiki) → agt:inLayer agt:<값>Layer. **명시가 없으면
#                 knowledge 를 방출한다** — 표시 누락을 산발로 세지 않으려고 기본값을 그래프에 적는다. 층은 plane 과
#                 직교하는 역할 속성이고 값의 닫힌 집합은 shape layer-shapes.ttl 이 판정한다. 코드 청크는 등록부가 process 를 준다
#   exposes:      이 항목이 노출하려는 결함 요인(현상) 개체의 agt: IRI 목록 (선택, 위험 분석 G5 — 노트 8.21절).
#                 agt:exposesFactor 로 나간다. 링크 키가 아니다 — 대상이 청크가 아니라 온톨로지 개체이므로 링크 개체의
#                 치역 밖이고 Bazel deps 도 되지 않는다. 대상의 종류는 shape exposes-factor-shapes.ttl 이 판정한다
#   pattern:      ubiquitous | event-driven | state-driven | unwanted-behaviour | optional | complex (선택, type: requirement 에서만) —
#                 요구 문장의 EARS 패턴 (Mavin RE'09, 결정 p7-dev-plane-substance) → agt:pattern agt:<camelCase 개체>. 다른 plane 에 있으면 거부
#   targets:      주석이 관찰하는 대상 IRI 목록 (선택, type: annotation 에서만) → agt:targets 직접 트리플.
#                 **링크 키가 아니다** — 링크 개체(agt:Link)도 Bazel deps(gen_build.LINKS)도 만들지 않는다. 주석이 대상의 deps 가
#                 되면 주석 하나가 대상의 재빌드를 유발해 리뷰가 빌드 그래프를 오염시킨다. 주석은 대상을 관찰하지 구성하지 않는다
#   주석의 본문:   type: annotation 의 본문은 주석이다 (p7-commentary-form). 첫 줄 `<라벨> (<장식>): <요지>` 와 줄 머리 슬롯 넷
#                 (`대상:`·`본문:`·`제안:`·`해소:`)에서 agt:commentLabel·agt:commentDecoration·agt:resolutionState·
#                 agt:commentSentenceCount 를 낸다. 닫힌 어휘와 문장 상한의 판정은 shape(review-comment-body-shapes.ttl)이고
#                 여기서 거부하는 것은 `대상:` 과 frontmatter `targets` 의 불일치 하나뿐이다
#   프로파일 타이핑: 청크마다 plane 클래스 뒤에 개발 프로파일의 실체 클래스를 더 붙인다 (`a agt:RequirementChunk , agt:RequirementStatement`,
#                 PROFILE_SUBSTANCE). 살아 있는 청크든 폐기된 청크든 같다 — 폐기된 요구 문장도 요구 문장이다
#   라벨 언어:    title 에 한글([ㄱ-ㆎ가-힣])이 있거나 title_ko 에 한글이 없으면 거부 — 영문 라벨에 한글을 섞지 않는다(0.6절).
#                 composite 의 title·title_ko 도 같은 @en/@ko 라벨이므로 같은 규칙으로 거부한다
#   인용원:       본문(frontmatter 제외, **코드 펜스 밖**)에 소멸성 채널 경로(`harness/channel/` · `harness/user/` · 옛 `docs/feedback/`)가
#                 있으면 거부 — 근거는 질문 번호(`Q12-a`)로 적는다. 규칙·근거는 영속 지식
#                 (노트·결정)에 둔다 (agrtls-practices-review P). status: deprecated 청크는 제외
```
<!-- 인용 끝 -->
