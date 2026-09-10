---
id: https://agentic-knowledge-base.dev/id/chunk/f7f3a3a1-2266-460b-bc5b-38f085f574b8
type: decision
level: concrete
title_ko: ODD 문서는 OpenODD 형식이고 확장 키는 checks와 exclusions_reviewed 둘이다
title: The ODD document is OpenODD, with exactly two extension keys: checks and exclusions_reviewed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f867e42b-0106-4796-8861-4bdc493e15db, title_ko: ODD = OpenODD, title: ODD = OpenODD}
part_of: https://agentic-knowledge-base.dev/id/composite/f867e42b-0106-4796-8861-4bdc493e15db
---
**결론** — ODD = OpenODD (노트 부록 E.4). 택소노미는 `related/condition`에서 생성. 모듈은 INCLUDE_AND/OR·EXCLUDE_AND/OR, 식은 Equal·Range·bound·범주 집합, 다국어 제목, 단위, `any`/`unknown`(= `unverified`), `exclude_when_unknown`(= restrictive). 확장 키 둘 — `checks`(판정식·등급, OpenODD에 없음), `exclusions_reviewed`(명시 제외 기록). 이탈 = COD ∉ ODD, OpenODD 의미론이 정의. 이 저장소(2026-09-10, 도입 순서 (b) 완료): 원본 `kb/odd/project-odd.yml`, `taxonomy.yml`은 `related/condition`에서, `project-odd.ttl`은 문서에서 생성. `checks.cel`은 5단계.

외부 조사로 채운 세부 (ASAM OpenODD 1.0 §6.4·§10.2, 2026-09-11) — 모듈 = `id`·`title`(LangString)·`description`·`comment`·`is_root`·`is_active`·`labels`·`tags`, INCLUDE·EXCLUDE 각 최대 하나에 연산자 AND/OR. **MODULE = INCLUDE ∧ ¬EXCLUDE**, 둘 다 없으면 참. 식은 `LowerBound`·`UpperBound`·`Equal`·`Range [a .. b]`·`CategoricalList` 다섯이고 `unknown` 리터럴은 값이 없을 때 참. 택소노미 YAML은 최상위 `TAXONOMY:` 아래 형 있는 속성(`float velocity`·`boolean`·범주 목록)과 단위 체계. 2026-09-11 정합(유저 결정): 문서를 YAML 매핑 참조의 모양(Release Presentation slide 6·8 — `TAXONOMY:` 아래 `속성: [리터럴…]`/`int count`, `MODULES:` 아래 모듈 id·`title`·`is_root`·`is_active`·`INCLUDE_AND:` 등에 `속성: 식`)으로 다시 썼다. 식은 리터럴·`"< n unit"`·`"[a .. b] unit"`·`unknown`. 이 체계의 확장 키는 대문자로 구분한다 — `ATTRIBUTES`(IRI·라벨)·`LITERALS`·`CHECKS`·`EXCLUSIONS_REVIEWED`·`EXCLUDE_WHEN_UNKNOWN`. 생성기는 PyYAML 위에서 범주·리터럴·식·판정 방법을 검사한다.
