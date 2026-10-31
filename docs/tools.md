# tools — 검사 도구와 활용 도구, 코어 / development / V&V

검사 도구는 [`rules.md`](rules.md)의 규칙을 기계로 수행하고, 활용 도구는 [`method.md`](method.md)의 절차를 기계로
수행한다. 그래서 도구 하나는 규칙 하나나 절차 하나에 대응한다. 이 문서는 구조도 v5에 따라 도구를 **코어,
development, V&V**의 셋으로 나눠 적는다. 코어 도구는 두 KB가 공유하고, 나머지 도구는 각 KB의 규칙과 절차를 수행한다.

## 하네스는 Bazel이다

이 체계에서 지식 산출물은 데이터 타깃이고, 검사 게이트는 테스트 타깃이다. 그래서 `bazel test //...`를 한 번 돌리면
게이트 전체가 돈다. 근거와 기각된 대안은 [`pe-harness-on-bazel`](../kb/dev/decision/pe-harness-on-bazel/conclusion.md)에
있다. 지식 종류별 규칙을 두고 링크를 deps로 바꾼 전환은 도입 3단계의 일이고, 그 근거는
[`pe-bazel-rules`](../kb/dev/decision/pe-bazel-rules/conclusion.md)에 있다.

| 체계의 요구 | Bazel의 성질 |
|---|---|
| 바뀐 지식만 재검증한다(`p10-link-decay-states`의 재검증 시점) | 입력 해시 기반 캐시 — 바뀐 파일의 게이트만 다시 돈다 |
| 산출물 사이의 의존을 밝힌다 | BUILD 그래프가 의존을 선언으로 강제한다 |
| 판정 도구가 재현된다 | hermetic 툴체인과 해시를 고정한 lock |
| 게이트를 우회하지 못한다 | 게이트는 테스트 타깃이라 우회하려면 BUILD를 고쳐야 하고, 그 변경은 리뷰에서 걸러진다 |

**판정 가능한 것만 게이트로 만든다.** 기계가 판정할 수 없는 규칙은 게이트에 넣지 않고 `STYLEGUIDE.md`의
`[지킴]`으로 남기며, 게이트에 넣을 수 없다는 사실은 §"게이트 밖"에 기록한다. shape는 **강화만** 한다. 제약을
완화하려면 유저의 승인을 받는다.

## 게이트 총람 — 원본은 `GATES` 리터럴이고 이 표는 그 투영이다

게이트 id의 단일 정의 위치는 [`defs/kb.bzl`](../defs/kb.bzl)의 `GATES`와 `TOOL_TAGS`다(2026-10-02). 그 전에는 같은
목록이 네 곳에 갈려 있었다. 네 곳은 상수 25개와 코드의 태그, 이 표의 `id` 열, 아래 하네스 문단이다. 아래 표는 등록부의
다섯 키를 게이트마다 한 행으로 옮긴 생성 투영이고 손으로 쓴 셀이 없다(유저 답 Q150-a). 생성기는
`python3 tools/gates2kg.py --catalogue docs/tools.md`이고, `//:doccheck_test`가 표를 다시 그려 바이트로 비교한다.
게이트의 배경과 해소, 측정은 `결정` 열이 가리키는 결정에 있다.

이 표의 틀은 노트 6.7절의 총람이고 측정은 결정에 있다([`p6-gate-catalogue`](../kb/dev/decision/p6-gate-catalogue/conclusion.md)).
실행 계층은 게이트를 어느 기계가 판정하는가를 가르고, 다섯이다.

- **shape**는 SHACL로 지식 단위를 즉시 판정한다.
- **verify**는 SPARQL로 그래프 단위를 재검증 시점에 판정한다.
- **analysis**는 Bazel 분석 시점에 판정하고, 위반하면 빌드가 실패한다.
- **test**는 `bazel test`로 실행해 판정한다.
- **human**은 사람의 승인으로 판정한다.

게이트에 걸린 지식은 `draft`에 머물고, 하류로 전파되지 않는다.

<!-- 생성 시작: 게이트 등록부 defs/kb.bzl 의 GATES 투영 — 손으로 고치지 않는다. 재생성 python3 tools/gates2kg.py --catalogue docs/tools.md, 검사 //:doccheck_test -->

| id | 게이트 | 무엇을 거부하는가 | 실행 계층 | 판정 도구 | 결정 |
|---|---|---|---|---|---|
| `shacl` | shape 적합성 | SHACL shape 부적합 | shape | `validate` | [`p4-chunk-rules-as-shacl-shapes`](../kb/dev/decision/p4-chunk-rules-as-shacl-shapes/conclusion.md) |
| `belief-consistency` | 믿음 정도 일관성 | 상태 전이 규칙이 믿음 정도를 읽거나, 닫힌 계산 규칙이 없는데 선호의 동률 깨기가 믿음 정도를 읽음 | verify | `validate` | [`p9-evidence-ledger-with-belief`](../kb/dev/decision/p9-evidence-ledger-with-belief/conclusion.md) |
| `boundary` | 정의 경계 | 한 용어가 두 모듈 파일에서 정의됨 | verify | `validate` | [`p2-ontology-file-is-a-chunk`](../kb/dev/decision/p2-ontology-file-is-a-chunk/conclusion.md) |
| `catalog` | 카탈로그 정합성 | 적용 범위 없는 역할, 미부여 적용 범위, 쓰기 지식 종류 공유, maxConcurrent 합 초과 | verify | `validate` | [`p11-catalog-role-has-granted-scope`](../kb/dev/decision/p11-catalog-role-has-granted-scope/conclusion.md) |
| `code-part-link` | 코드 부분 링크 | 추출 트리의 복합체 부분(정의·구역 단위 지식)이 refines·serves·verifies 의 끝점 | verify | `validate` | [`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md) |
| `cross-kb-link` | KB 가로지름 링크 | verifies 밖의 저작 링크가 두 KB 를 가로지름 (검증 목표 → 요구 derivesFrom 만 예외) | verify | `validate` | [`p8-vv-independence-scope`](../kb/dev/decision/p8-vv-independence-scope/conclusion.md) |
| `dangling` | 참조 무결성 | 인용·부분·가정·요구·정의 호출의 대상이 실재하지 않음 | verify | `validate` | [`p10-extracted-references-are-candidates`](../kb/dev/decision/p10-extracted-references-are-candidates/conclusion.md) |
| `draft-end` | draft 끝 링크 | 살아 있는 단위 지식의 frontmatter 링크가 draft 단위 지식을 끝으로 둠 | verify | `validate` | [`p4-chunk-state-machine`](../kb/dev/decision/p4-chunk-state-machine/conclusion.md) |
| `element-drop` | 요소 탈락 | 어휘에 슬롯이 없어 조용히 빠진 소스 요소 | verify | `validate` | [`p8-odc-defect-subtypes`](../kb/dev/decision/p8-odc-defect-subtypes/conclusion.md) |
| `gate-registry` | 게이트 등록부 | 코드의 게이트 태그 집합이 GATES 리터럴과 갈림 | verify | `validate` | [`p6-gate-tool-code-structure`](../kb/dev/decision/p6-gate-tool-code-structure/conclusion.md) |
| `labels` | 라벨 완전성 | agt: 용어의 한·영 라벨 또는 skos:definition 누락 | verify | `validate` | [`p2-ontology-compiler-three-tiers`](../kb/dev/decision/p2-ontology-compiler-three-tiers/conclusion.md) |
| `odd-ref` | ODD 참조 | ODD 에 없는 조건을 참조하는 적용 범위·가정·변수 | verify | `validate` | [`p3-condition-entity-from-odd-document`](../kb/dev/decision/p3-condition-entity-from-odd-document/conclusion.md) |
| `residency` | 수준 허용표 단일 정의 위치 | 수준 허용표 shape 가 RESIDENCY 리터럴과 갈림 | verify | `validate` | [`p6-plane-level-occupancy`](../kb/dev/decision/p6-plane-level-occupancy/conclusion.md) |
| `rung-before-descent` | 정제 계층 사슬 | 같은 정제 수준의 V&V 대응물(목표·기준·검증기 바인딩) 없이 다음 정제 수준으로 내려간 정제 | verify | `validate` | [`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| `syntax` | 구문 | TTL 이 파싱되지 않음 | verify | `validate` | [`p2-ontology-compiler-three-tiers`](../kb/dev/decision/p2-ontology-compiler-three-tiers/conclusion.md) |
| `token-budget` | 토큰 상한 단일 정의 위치 | 지식 종류별 본문 토큰 상한의 표와 shape 가 갈림, 어휘 파일 해시값 불일치 | verify | `validate` | [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md) |
| `verify` | 안티패턴 | 안티패턴 SPARQL 질의가 위반 행을 냄 | verify | `validate` | [`p2-ontology-compiler-three-tiers`](../kb/dev/decision/p2-ontology-compiler-three-tiers/conclusion.md) |
| `vocab` | 통제 어휘 | 온톨로지와 등록 표준 어휘 밖의 술어·용어 | verify | `validate` | [`p2-ontology-as-vocabulary`](../kb/dev/decision/p2-ontology-as-vocabulary/conclusion.md) |
| `case-gen` | 테스트 케이스 생성 | 생성 시점의 입력 위반 — 표본 근거 없는 테스트 케이스, ODD 속성이 아닌 변수, keep 안의 요인 값, 실행기가 읽지 못하는 테스트 케이스 | analysis | `case_gen` | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| `chunk2kg` | head 생성 | head 그래프 생성 시점의 frontmatter·본문 규칙 위반 | analysis | `chunk2kg` | [`pe-kg-hand-and-generated-files`](../kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md) |
| `chunk2kg-merge` | head 병합 | 타깃별 head 조각의 병합 실패 | analysis | `chunk2kg` | [`p6-validate-the-union`](../kb/dev/decision/p6-validate-the-union/conclusion.md) |
| `extract` | 코드 추출 | 추출 시점의 개명 안내·삭제·부분 상한·등록부 불일치 | analysis | `extract` | [`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md) |
| `extract-refs` | 인용 대상 실재 | 본문 인용의 대상이 실재하지 않음 | analysis | `extract_refs` | [`p10-extracted-references-are-candidates`](../kb/dev/decision/p10-extracted-references-are-candidates/conclusion.md) |
| `gates2kg` | 게이트 그래프 생성 | 게이트 등록부의 키·실행 계층 위반과 판정 도구 개체의 부재 | analysis | `gates2kg` | [`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md) |
| `gen-build` | BUILD 생성 | 생성 시점의 묶음·세 단위 지식·링크 규칙 위반 | analysis | `gen_build` | [`pe-bazel-rules`](../kb/dev/decision/pe-bazel-rules/conclusion.md) |
| `gen-norms` | 규범 문서 생성 | 생성 시점의 절 항목·규약 줄 위반 — 고아 줄·이중 소비·없는 줄·강도 없는 줄·문서 목록 불일치 | analysis | `gen_norms` | [`p12-norm-documents-from-section-chunks`](../kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md) |
| `gen-skills` | skill 생성 | skill 생성 시점의 입력 위반 | analysis | `gen_skills` | [`pe-generated-outputs-stay-in-bazel-out`](../kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md) |
| `odd2kg` | ODD 생성 | OpenODD 문서의 형식과 필수 필드 위반 | analysis | `odd2kg` | [`pe-odd-is-openodd`](../kb/dev/decision/pe-odd-is-openodd/conclusion.md) |
| `restored` | 복원 표시 | restored 의 IRI 가 같은 단위 지식의 링크 키 대상에 없음 | analysis | `chunk2kg` | [`p10-restored-link-marking`](../kb/dev/decision/p10-restored-link-marking/conclusion.md) |
| `space` | 설계 공간 | 근거 없는 배제, 확정 후보 수, 변수와 후보의 불일치 | analysis | `space2kg` | [`p9-design-space-file`](../kb/dev/decision/p9-design-space-file/conclusion.md) |
| `specialization` | 특수화 링크 | specializationOf 의 자기 참조·지식 종류 불일치·폐기 대상·순환 | analysis | `chunk2kg` | [`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md) |
| `taxonomy` | 택소노미 생성 | 택소노미 생성 입력이 읽히거나 파싱되지 않음 | analysis | `taxonomy` | [`p0-condition-taxonomy-extensible`](../kb/dev/decision/p0-condition-taxonomy-extensible/conclusion.md) |
| `tim` | TIM | 링크 타입의 정의역·치역·방향·수준 위반 | analysis | `starlark` | [`p10-traceability-information-model`](../kb/dev/decision/p10-traceability-information-model/conclusion.md) |
| `visibility` | 의존 방향 | 개발 타깃이 V&V 타깃을 의존함 | analysis | `bazel` | [`p8-vv-independence-scope`](../kb/dev/decision/p8-vv-independence-scope/conclusion.md) |
| `vv-case` | V&V 테스트 케이스 형식 | 테스트 케이스의 기계가 읽는 자극·기대 규약 위반 | analysis | `vv_run` | [`p8-machine-readable-case`](../kb/dev/decision/p8-machine-readable-case/conclusion.md) |
| `workset-budget` | 작업 집합 예산 | 앵커가 있는 작업 집합 뷰가 컨텍스트 예산을 넘음 | analysis | `workset` | [`p1-workset-budget-fails-only-with-anchor`](../kb/dev/decision/p1-workset-budget-fails-only-with-anchor/conclusion.md) |
| `addition` | 첨가 | 슬롯의 질문에 답하지 않는 메타 문장과 채움 문구 | test | `chunk_lint` | [`p4-slot-answers-one-question`](../kb/dev/decision/p4-slot-answers-one-question/conclusion.md) |
| `blocking-comment` | 해소되지 않은 차단 주석 | issue (blocking) 이면서 해소가 열린 살아 있는 주석 | test | `chunk_lint` | [`p7-commentary-form`](../kb/dev/decision/p7-commentary-form/conclusion.md) |
| `build-drift` | BUILD 드리프트 | 생성 BUILD 가 frontmatter 링크와 어긋남 | test | `gen_build` | [`p12-generated-lists-with-drift-check`](../kb/dev/decision/p12-generated-lists-with-drift-check/conclusion.md) |
| `case-drift` | 테스트 케이스 드리프트 | 저장소의 테스트 케이스가 논리 시나리오의 생성 결과와 어긋나거나 생성기 밖에서 쓰임 | test | `case_gen` | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| `channel` | 채널 규약 | 하네스 채널(메시지·질문지)의 어휘·단일 작성자·필수 절·짝 없는 완료·경어·감탄·식별자 옆 한글 이름 위반 | test | `channel_lint` | [`p11-harness-two-channels`](../kb/dev/decision/p11-harness-two-channels/conclusion.md) |
| `chunk` | 단위 지식 형식 | 본문 토큰 상한 초과와 frontmatter 형식 위반 | test | `chunk_lint` | [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md) |
| `decision-role` | 결정 역할 표지 | 결론·근거·대안·규약의 첫 산문 줄에 역할 표지가 없음 | test | `chunk_lint` | [`p4-convention-slot`](../kb/dev/decision/p4-convention-slot/conclusion.md) |
| `doccheck` | 문서 현행성 | 문서의 죽은 링크·앵커·백틱 경로와 산문 문체 위반 | test | `doccheck` | [`p12-generated-documents-are-gated`](../kb/dev/decision/p12-generated-documents-are-gated/conclusion.md) |
| `empty-value` | 빈 값 표기 | 세 빈 값 밖의 표기와 표의 단독 대시 셀 | test | `chunk_lint` | [`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md) |
| `extract-drift` | 추출 드리프트 | 추출 생성물이 소스와 등록부에 어긋남 | test | `extract` | [`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md) |
| `frozen` | 동결 문서 | 동결 문서의 sha256 이 kb_lib.FROZEN_DOCS 의 고정값과 다름 | test | `doccheck` | [`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md) |
| `gate-input` | 게이트 입력 | 소유 패키지의 BUILD 가 이름으로도 glob 으로도 담지 않은 kb/ 지식 파일 | test | `gen_build` | [`pe-knowledge-files-are-gate-inputs`](../kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md) |
| `gendoc` | 생성 문서 형태 | 생성 마크다운의 머리 블록과 본문 서식 규약 위반 | test | `gendoc` | [`p12-generated-documents-are-gated`](../kb/dev/decision/p12-generated-documents-are-gated/conclusion.md) |
| `judge-log` | 판정 로그 | 판정 로그의 표 형식과 필수 필드 위반 | test | `chunk_lint` | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| `list-rules` | 목록 규칙 | 손 번호·항목 수·중첩·길이·빈 항목의 목록 규칙 위반 | test | `chunk_lint` | [`p4-slot-answers-one-question`](../kb/dev/decision/p4-slot-answers-one-question/conclusion.md) |
| `naming` | 파일 접미사 | TTL 파일 이름이 접미사 규약 밖 | test | `chunk_lint` | [`p0-artifact-filename-suffix`](../kb/dev/decision/p0-artifact-filename-suffix/conclusion.md) |
| `norms-drift` | 규범 문서 드리프트 | 생성 규범 문서가 절 항목과 결정의 규약 줄에 어긋남 | test | `gen_norms` | [`p12-norm-documents-from-section-chunks`](../kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md) |
| `prose` | 산문 문체 | 경어체 종결과 산문의 느낌표 | test | `chunk_lint` | [`p0-prose-assertive-register`](../kb/dev/decision/p0-prose-assertive-register/conclusion.md) |
| `skills-drift` | skill 드리프트 | 생성 skill 이 docstring 과 SKILLS 에 어긋남 | test | `gen_skills` | [`pe-generated-outputs-stay-in-bazel-out`](../kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md) |
| `stamp` | 도장 | 도장 입력이 등록부와 어긋남 | test | `stamp` | [`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md) |
| `summary-support` | 요약 지지 참조 | 요약 블록의 핵심 항목에 지지 참조가 없음 | test | `chunk_lint` | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| `vv-run-env` | 실행기 환경 격리 | 테스트 케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받음 | test | `vv_run_env_test` | [`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md) |
| `canon` | 정규 직렬화 | TTL 직렬화가 정규형과 다름 | human | `canonicalize` | [`p2-ontology-ttl-layout`](../kb/dev/decision/p2-ontology-ttl-layout/conclusion.md) |
| `writer` | 승인 | 쓰기 권한 밖의 저작과 검토 없는 stable 전이 | human | `validate` | [`p2-judgement-history-in-verified`](../kb/dev/decision/p2-judgement-history-in-verified/conclusion.md) |

<!-- 생성 끝 -->

표의 행은 전부 기계화된 게이트다. 아직 기계화되지 않은 총람 항목(ODD 경계, 기여, 범위·제약, 계약 선행, 판정 도구)은
결정 `p6-gate-catalogue`가 적는다. 등록 게이트의 목록과 실행 계층은 원본 `GATES` 리터럴과 그 생성
그래프 `//kg:gates_kg`에 있다. `id`는 도구의 `FAIL [<id>]` 태그와 같고(agrtls A), 결정 `p6-gate-catalogue`도 같은
id를 적는다. 하네스 자체의 게이트 id(원본 `GATES`, 2026-10-02)는 `naming`(`//:naming_test`) ·
`build-drift`(`//:build_drift_test`) · `gate-input`(`//:gate_input_test`) · `extract`·`extract-drift`(`//:extract_drift_test`) · `stamp`(`//tools:stamp`) · `token-budget`(`validate` — 지식 종류별 본문 토큰 상한의 표와 shape 의 동일성 + 어휘 파일 sha256) ·
`gate-registry`(`//tools:gate_registry_test` — 코드의 태그·상수·폴백이 `GATES`와 같은가) · `gates2kg`(생성=검사) · `labels`·`boundary`·`syntax`(`validate`의 온톨로지 품질 검사) · `restored`·`specialization`(`chunk2kg` 생성 시점) · `chunk2kg-merge`(`kb_kg_merge` — IRI 중복) · `gen-skills`·`skills-drift`(`gen_skills`) · `gen-norms`·`norms-drift`(`//:norms_drift_test`) · `case-gen`·`case-drift`(`//:case_drift_test`, 대상 0) ·
`channel`(`//harness:channel_lint_test`) · `doccheck`(`//:doccheck_test`) · `gendoc`(`//:gendoc_test`) · `addition`·`empty-value`·`list-rules`·`blocking-comment`·`judge-log`·`summary-support`(`chunk_lint`) · `space`(`space2kg` 생성=검사 — 게이트 id는 `space`다) ·
`odd2kg`·`taxonomy`(생성=검사) · `workset-budget`(`//kg:workset`, 앵커가 있을 때만) · `canon`(규약이고 테스트 타깃이 없다 — 등록부의 실행 계층은 `human`이다)이다. **게이트가 아닌 도구 태그**(`consistency`·`endorse`·`judge`·`link`·`open`·`propose`·`revalidate`·`run-evidence`·`tokens`·`validate`·`weave` — 입력 문제·보고, 목록의 원본은 [`defs/kb.bzl`](../defs/kb.bzl)의 `TOOL_TAGS`다)는 같은 대괄호 표기를 쓰되 `TOOL_TAGS`로 갈라 그래프 개체를 받지 않는다. 실패 종류(종료 코드 1·2·3)는
§게이트를 추가할 때에 적혀 있다.

## 코어 — 두 KB가 공유하는 도구

### 검사 (있음)

```bash
bazel test //...                 # 게이트 전체 (커밋 전 필수)
bazel run //tools:validate -- --ontology <files> --shapes <files> --odd <files> --data <files>
bazel run //tools:chunk_lint -- --chunks <files> --ttl <files>
bazel run //tools:canonicalize -- --write <files>    # 커밋 전 정규화
bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:… \
    --label-ko … --label-en … --definition … --cq CQ# \
    --derived-from <관측 IRI> --derived-from <관측 IRI>   # 용어 제안 → 승인 큐
bazel build //kb/odd:odd //kb/dev:index              # 생성물: ODD 그래프·택소노미, 라벨 목록
tools/relock.sh                                      # 파이썬 의존성 재고정
```

#### 온톨로지 검사 3단계 (노트 2.5절 — 온톨로지 검사기)

| 단계 | 정의 | 이 저장소 |
|---|---|---|
| 구문·스타일 (report) | 라벨·정의 누락, 참조 구문, 폐기 규약 | `validate.py`의 labels·boundary + `chunk_lint` |
| **안티패턴** (verify) | "이런 트리플이 존재하면 실패"를 SPARQL로 명세 | `validate.py --verify-queries` — `tools/verify-queries/*.rq` 하나가 안티패턴 하나. 목록의 원본은 그 디렉토리이고 질의마다 `kb/dev/artifact/verify-queries/`의 단위 지식이다 |
| 논리 정합성 (reason) | OWL 추론기 (RL 프로파일 안) | SHACL + `--reason`(OWL-RL). shape로 자연스러운 것(지식 종류별 허용 수준 표·카디널리티)은 shape에 남긴다 |

**용어 제안 워크플로**(`term_propose`)는 일반화가 온톨로지에 닿을 때의 절차다. 이 워크플로는 에이전트를 신뢰할
수 없는 센서로 다루므로, 에이전트는 제안만 한다. 제안은 네 검사를 통과해야 `kb/ontology/proposals/` 승인 큐에
오른다. 네 검사는 상위 개념의 실재와 라벨 중복, 정의 형식, 근거의 실재다. 근거의 실재는 관측이나 판정 주석 둘
이상을 `prov:wasDerivedFrom`으로 가리키는지 본다. 큐는 `//kb/ontology:modules` 밖에 있으므로, 제안은 승인 전에
그래프에 들어가지 않는다.

#### `validate.py` — 그래프 게이트

| 검사 | 강제하는 것 | 규칙 |
|---|---|---|
| `syntax` | 모든 TTL이 파싱된다 | — |
| `labels` | `agt:` 용어마다 한/영 `rdfs:label` + `skos:definition` | [ontology §확장 규칙](ontology.md#확장-규칙) |
| `boundary` | 한 용어는 한 모듈 파일에서만 정의된다 | 같음 |
| `vocab` | 데이터의 술어가 온톨로지 또는 등록된 표준 어휘 안. `--standard-vocab`(PROV-O·SKOS 원문, `MODULE.bazel` `http_file` 해시 고정)를 주면 그 네임스페이스의 용어가 **원문에 실재**하는지까지 — 접두사만 맞는 오타를 잡는다 | [rules §통제 어휘](rules.md#통제-어휘) |
| `odd-ref` | `agt:refersTo`의 대상이 ODD에 존재한다 | [rules §가정](rules.md#가정) |
| `dangling` | `cites`·`usesConcept`·`hasDirectPart`·`assumes`·`refines`·`satisfies`가 가리키는 항목이 실재한다. `usesConcept`의 대상이 폐기 용어(`owl:deprecated`)면 `warn [usesConcept-deprecated]`(FAIL 아님 — LEDGER 용어 일관성 검사) | [rules §4](rules.md#4-traceability--인터페이스를-기준축으로-한-mapping) |
| `cross-kb-link` | frontmatter 링크 키의 링크가 `verifies` 밖이면서 두 KB를 가로지르지 않는다. 예외는 검증 목표(functional) → 개발 요구 `derivesFrom` 하나다. 판정 함수 `kb_lib.cross_kb_link` 는 복원 후보 생성기와 공유한다 | [rules §8](rules.md#8-vv-규칙--vv-kb-노트-8285-811815-84-911) |
| `code-part-link` | 추출 트리 안에서 복합체의 부분인 단위 지식(정의 단위 지식과 구역 단위 지식)은 `refines`·`serves`·`verifies` 의 끝점이 아니다 — 링크는 파일 단위 지식 하나가 갖는다. 판정 함수 `kb_lib.code_part` 는 복원 후보 생성기와 공유한다 | [rules §7](rules.md#7-development-규칙--개발-kb-노트-7277) |
| `rung-before-descent` | 같은 정제 수준의 V&V 대응물 없이 다음 정제 수준으로 내려간 정제가 없다 — R1 정제 계층 사슬(functional→abstract 목표 · logical→concrete 기준 · concrete→executable 검증기가 바인딩한 기준, 사람 확인 기준만 가진 요구는 면제). 판정 함수 `kb_lib.rung_violations` 는 `metrics` 와 대응물 집합(`kb_lib.vv_counterparts`)을 공유한다 | [rules §8](rules.md#8-vv-규칙--vv-kb-노트-8285-811815-84-911) |
| `draft-end` | 살아 있는 단위 지식의 frontmatter 링크가 `draft` 지식을 끝으로 두지 않는다. 판정 함수 `kb_lib.draft_end_links` 는 감사 보고의 "draft 끝 링크" 지표와 같다 | [rules §1](rules.md#1-chunk--자립적-최소-지식-단위) |
| `verify` | 안티패턴 질의 결과 행 = 위반 | 위 표 |
| `shacl` | shape 적합성 (아래). `--waivers <waivers.md>`를 주면 위반의 focus node를 `agt:assertionLocation`으로 파일에 사상해 게이트 id `shacl`(축 `파일`)로 선언된 면제를 집계에서 빼고 `WAIVED [shacl] <파일>: <sh:resultMessage>` 줄로 남긴다 (2026-10-01) | [rules](rules.md) |

`vocab`이 핵심 방어선이다. 어휘 우회를 막지 못하면 나머지 규칙도 전부 우회되기 때문이다.

#### SHACL shape — `kb/ontology/shapes/`

shape 목록의 원본은 그 디렉토리이고, 파일마다 머리 주석이 대상과 근거 결정을 적는다. 아래 표는 그 요약이다.

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `tokenCount` 0 이상 정수 하나 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `status` 값. 크기의 **상한**은 여기 없다 — 지식 종류별 프로파일 파라미터라 `token-budget-shapes.ttl` 이 본다 |
| `token-budget-shapes.ttl` | 지식 종류별 `…Chunk` | 본문 `tokenCount` 상한 — 저작 산문 1,092(42의 26배) · `artifact`·`memory` 2,856(42의 68배). 값의 단일 정의 위치는 `tools/kb_lib.py` 의 `BODY_TOKEN_LIMITS` 이고 게이트 `token-budget` 이 둘의 동일성과 어휘 파일 해시값을 본다 ([`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md), 2026-10-01) |
| `composite-shapes.ttl` | `agt:Composite` | `hasDirectPart` ≤ 9 |
| `composite-order-shapes.ttl` | `co:List` | 순서 있는 복합체의 색인 1..n 연속·중복 없음, `co:itemContent` 집합이 `hasDirectPart`와 일치 (2026-09-29) |
| `residency-shapes.ttl` | 지식 종류별 | 지식 종류별 허용 수준 표 |
| `condition-shapes.ttl` | `agt:Condition`·`agt:ODD` | 조건마다 `checkMethod` 필수 · 등급 A–D · ODD는 조건 ≥ 1 |
| `assumption-shapes.ttl` | `agt:Assumption` | ODD 조건을 `refersTo` ≥ 1 · `proposition` 필수 |
| `scope-shapes.ttl` | `agt:Scope` | `mode` 고정 · `subsetOf`로 어느 ODD의 부분집합인지 |
| `trust-shapes.ttl` | `agt:Chunk` | `generatedBy` 필수 · 가장 늦은 `verifiedAt` ≥ `generatedAtTime`(검증 뒤 수정 금지, `verified`는 누적) |
| `tag-shapes.ttl` | `agt:taggedWith` 대상 | 태그 값은 온톨로지 개념이고 범주에 등록돼 있다 (2026-09-26) |
| `requirement-body-shapes.ttl` | `agt:RequirementChunk` | 요구·검증 목표의 본문 슬롯과 순서 (2026-09-22) |
| `decision-body-shapes.ttl` | `agt:DecisionChunk` | 결론·근거·대안의 본문 슬롯. V&V 시나리오의 **자극**·**요인**·**배제 자극**이 그 세 슬롯에 사상된 대안 셋이다 (2026-09-29) |
| `acceptance-criteria-body-shapes.ttl` | `agt:ContractChunk` | 합격 기준 · 판정 술어 또는 확인 절차 · 등급 |
| `verification-case-body-shapes.ttl` | `agt:SchemaChunk` | 테스트 케이스 · 자극 · 기대 · 실행 명령 · 표본 근거 |
| `review-comment-body-shapes.ttl` | `agt:ReviewComment` | 라벨 일곱·장식 셋·해소 셋의 닫힌 어휘, `대상`·`본문`·`해소` 슬롯, 본문 4문장 상한 |
| `defect-factor-shapes.ttl` | `agt:DefectFactor` 인스턴스 | 현상 개체의 정의·표기·관측 수단·출처 (2026-09-29) |
| `risk-grade-shapes.ttl` | 같음 | 위험 등급 셋의 형·개수와 닫힌 값 어휘 `S0~S3`·`E1~E4`·`D1~D3`. 단계의 판정 조건은 [`risk-grade-scale-stimulus`](../kb/vv/scenario/risk-grade-scale-stimulus.md)이 정의한다 (2026-09-29) |
| `layer-shapes.ttl` | `agt:inLayer` 주어 | 항목의 서비스 층이 정확히 하나이고 값이 `knowledge`·`methodology`·`process` 셋 중 하나다. 층 개체 자체는 층에 속하지 않는다 (2026-10-01) |
| `exposes-factor-shapes.ttl` | `agt:exposesFactor` 주어 | frontmatter `exposes`의 대상이 `defect` 모듈이 선언한 현상 개체다. 없는 개체와 요인 아닌 개체를 둘 다 거부한다 — 링크 개체도 deps도 아니라 여기가 유일한 실재 검사다 (2026-09-29) |
| `space-shapes.ttl` | `agt:Space` | 설계 공간 하나가 변수 하나와 그 후보 집합의 형태를 갖는다 ([`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md)) |
| `convention-slot-shapes.ttl` | `agt:bodySlot` 주어 | `규약:` 줄은 결정의 넷째 단위 지식 `conventions.md`에만 둔다 ([`p4-convention-slot`](../kb/dev/decision/p4-convention-slot/conclusion.md)) |
| `norm-section-shapes.ttl` | `agt:DocumentSectionChunk` | 규범 문서의 절 단위 지식에서 제목과 깊이가 짝이고 깊이는 2 또는 3이다 ([`p12-norm-documents-from-section-chunks`](../kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md)) |
| `profile-development-shapes.ttl` | 지식 종류별 `…Chunk` | 단위 지식은 지식 종류의 실체 하위 클래스이고 요구 문장은 EARS 패턴 하나를 갖는다 |
| `gate-shapes.ttl` | `agt:Gate` | 게이트 개체마다 서비스 층 하나와 실행 계층 하나, 한/영 라벨과 설명 한 줄이 필수다 |
| `projection-shapes.ttl` | `agt:View`·`agt:Skill` | 뷰와 skill 은 원본 지식을 하나 이상 가리키고 층을 갖지 않는다 |
| `judge-question-shapes.ttl` | `agt:JudgeQuestion` | 판정 질문의 형은 noul·choice·score 셋 중 하나이고 choice 의 선택 집합은 255 이하다 ([`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md)) |
| `confidence-threshold-shapes.ttl` | `agt:JudgementLog`·`agt:JudgementRow` | 판정 로그는 판정자 둘의 답과 일치 여부 열, 확신도 열, 미끼 검출 결과를 갖고 단독 응답에는 자동 적용 표시가 붙지 않는다. `tools/judge.py`가 로그를 쓰기 전에 검사한다 ([`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md)) |

라벨 제약은 `sh:qualifiedValueShape`와 `sh:qualifiedMinCount`로 쓴다. `sh:languageIn`은 모든 값에 적용되므로
"한글 하나와 영어 하나"를 표현하지 못하기 때문이다.

shape의 면제도 `waivers.md` 하나에 선언한다(2026-10-01). `//kg:gate_test`가 `waivers = "//docs:waivers"`로 그 표를
넘기면, `validate`는 위반마다 focus node를 `agt:assertionLocation`으로 파일에 대응시켜 게이트 id `shacl`(축 `파일`)의
선언과 대조한다. 면제된 위반은 집계에서 빠지고 `WAIVED [shacl]` 줄로 남는다. 이것은 `chunk_lint`의 `chunk` 면제와
같은 규약이어서, 같은 파일이 두 게이트에 두 행으로 선언된다. **shape는 고치지 않는다.** 상한을 낮추면 면제 대상이
아닌 파일의 판정까지 약해지기 때문이다.

#### `chunk_lint.py` — 파일 게이트

게이트 `chunk`는 본문의 토큰 상한을 강제한다. 상한은 저작 산문이 1,092(42의 26배)이고, `artifact`와 `memory`가
2,856(42의 68배)이다. 단위는 줄이 아니라 토큰이고, 계수기는 `o200k_base` 하나다. 계수기의 어휘 파일은 `MODULE.bazel`의
`http_file`이 sha256으로 고정하고, 도구는 그 파일을 네트워크 없이 runfiles에서 읽는다. 본문을 떼어 내는 판정은
`kb_lib.body_text` 하나가 맡는다. `.md`에서는 frontmatter를 빼고, `.ttl`에서는 `@prefix`와 주석, 빈 줄을 뺀다. 어휘
파일이 없거나 해시가 고정값과 다르면 도구는 판정하지 않고 종료한다(`EXIT_CONFIG`, `FAIL [chunk]`). 게이트 `naming`은
파일명 접미사 규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`)을 강제한다.

**온톨로지 파일도 토큰 상한을 받는다.** 단위 지식은 파일 포맷이 아니라 구조 규칙이기 때문이다.

`chunk`도 `--waivers`가 받는 게이트 id다(2026-10-01). `waivers.md`에 축 `파일`로 면제된 파일의 상한 초과는 집계에서
빼되 `WAIVED [chunk]` 줄로 남긴다. 면제는 append-only 기록(판정 로그 등)처럼 소급 분할이 기록을 다시 쓰는 일이
되어 면제 말고는 해소할 길이 없는 경우에 쓴다. 새로 쓰는 로그는 상한 안에서 나누므로 면제가 늘지 않는다.

게이트 `decision-role`의 표지는 파일 경로가 정한다. `conclusion`과 `rationale`, `alternatives`는 각각 **결론**과
**근거**, **대안**이다. V&V 시나리오 패키지(`kb/vv/scenario/`)의 `<슬러그>-stimulus.md`와 `<슬러그>-factors.md`,
`<슬러그>-excluded.md`는 각각 **자극**과 **요인**, **배제 자극**이다. 이때 선언 단위 지식은 `-stimulus`이고, 타깃
이름도 그것이다. 그 밖의 파일, 곧 단일 파일인 옛 결정과 단일 단위 지식인 시나리오는 **결론**이다(2026-09-29,
[`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md)). 접미사 판정을 시나리오 패키지로
한정한 까닭은 옛 결정 트리에 stem이 `-factors`로 끝나는 결정(후속은 `p8-defect-factor-taxonomy`)이 있었기 때문이다.

단위 지식을 파싱하는 도구는 전부 `--residency <defs/kb.bzl>`를 받는다(2026-09-27). 그 도구는 `chunk2kg`와
`consistency`, `weave`, `labels`, `space2kg`, `revalidate`, `vv_run`, `assume_check`, `label_sample`, `gen_build`다.
인자가 없으면 도구는 `EXIT_CONFIG`로 끝나므로, 직접 실행할 때는 `--residency defs/kb.bzl`을 밝혀 적는다.

#### 생성기 = 검사기

| 도구 | 입력 → 산출 | 실패 조건 |
|---|---|---|
| `chunk2kg.py` | 단위 지식 frontmatter → head 그래프. 지식 종류를 개발 프로파일의 실체 클래스로 함께 타이핑하고 요구의 `pattern`을 방출한다(2026-09-18). **타깃별 조각**(`--fragment`, `kb_chunk`·`kb_decision` 액션) → `kb_kg_merge`(`--merge`) → `bazel-bin/kg/chunks-kg.ttl`. 바뀐 타깃의 조각만 다시 만든다. 묶음의 단위는 파일이 아니라 **액션의 입력 집합**이다 — `kb_decision`(셋 고정)·`kb_composite`(2~9 가변)가 그 집합을 만들고 `kb_chunk` 하나로는 복합체가 서지 않는다. 위험에서 파생된 항목의 선택 키 `exposes: [<agt: 현상 IRI>…]`를 `agt:exposesFactor`로 방출한다(2026-09-29) — 링크 키가 아니라 `targets`와 같은 자리이고 Bazel deps가 되지 않는다. 정의 단위 지식의 선택 키 `uses: [<청크 IRI>…]`를 `agt:usesDefinition`으로 방출한다(2026-09-30, `type: artifact`에서만 — 정의역이 `agt:ArtifactChunk`다) — 같은 자리이고 값의 원본은 손이 아니라 `extract`다. 서비스 층의 선택 키 `layer: knowledge | methodology | process`를 `agt:inLayer`로 방출하고 **명시가 없으면 `agt:knowledgeLayer`를 방출한다**(2026-10-01, 지식 종류 제한 없음 — 층은 지식 종류와 직교하는 역할 속성이다). 기본값을 그래프에 적는 이유는 표시 누락이 산발로 세어지지 않아야 하고 층별 집계(CQ-38)의 분모가 항목 전수여야 한다는 것이다 ([`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md)). 값이 어휘 밖이면 거부한다. 복합체 선언의 선택 키 `composite: {…, ordered: [<부분 IRI>…]}`가 있으면 `agt:Composite , co:List`로 타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`을 그 순서로 낸다(2026-09-29). 없으면 `hasDirectPart`만 낸다 — 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다. **예외는 없다**(유저 승인 2026-09-29) — 결정 기록도 선언으로만 순서를 갖고 그 선언은 생성 BUILD 의 명시 인자를 통해 `--ordered <IRI>`(부분마다 한 번)로 들어온다. 이 도구는 역할 이름·파일 stem 으로 순서를 추측하지 않는다. `--ordered`와 frontmatter `composite.ordered`가 함께 있으면 같아야 한다 — BUILD는 뷰이고 frontmatter가 원본이므로 불일치는 드리프트다 ([`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md)). 본문 슬롯 표지(`agt:bodySlot`)는 굵은 span 이 그 줄의 필드 자리(줄 머리·불릿 `- ` 다음·앞선 필드의 ` · ` 다음)에 있고 표지 뒤 한정어가 짧을 때(마침표 없음, 길이 `BODY_SLOT_QUALIFIER_MAX` 이하)만 방출한다(`body_slots`, 2026-09-29) — 표 셀·산문 접속·목록 항목 전체를 감싼 굵은 강조는 자리가 아니라 표지로 방출하지 않는다. | 필수 키 7개 누락, 값 어휘 밖, 복합체 미선언(조각), `ordered`가 목록이 아님·부분 중복·**부분 집합과 불일치**, **IRI 중복**(병합) — "한 단위 지식은 한 파일"의 기계적 강제 |
| `extract_refs.py` | 본문의 `d-NNNN` 인용 → `references-kg.ttl`의 `agt:cites`; 본문의 `agt:<Term>` 표기 중 온톨로지가 정의한 용어 → `agt:usesConcept`(복원 경로, dependency-graph (f)). 온톨로지에 없는 표기는 `info`로 집계만 한다 | 인용 대상이 실재하지 않음 |
| `run_evidence.py` | 실행 기록의 테스트 케이스 판정(pass → 실행(+) · fail → 실행(−))과 코드 파일 단위 지식의 테스트 통과 도장(`process:bazel-test`) → 코드 파일 단위 지식 → 결정 결론의 `satisfies` 후보 링크와 증거 항목(`agt:runResult`). 판정 로그의 쌍 행(`대상` 이 `<앵커> ↔ <대상> · <종류>`)마다 판정 증거(`agt:judgement`, yes는 +, no는 −)와 후보 링크 개체를 낸다 — 판정은 반박만 있어도 `invalid`가 아니고, 입력 해시값이 지금 두 파일과 다른 낡은 판정과 이미 확정된 쌍은 내지 않는다(task 0262). 후보로 낸 링크마다 열린 계산 규칙 A·B·C의 믿음 정도(`agt:DegreeOfBelief` — 값·계산 규칙·입력 증거 수)를 곁에 싣는다. A는 증거 종류 서열 가중을 극성대로 더해 [0,1]로 접은 점수, B는 Beta(1, 1)에 지지·반박 수를 더한 사후 평균과 분산, C는 판정 확신도의 평균(보정 전)이고, 값은 상태를 바꾸지 않는다(task 0304, 게이트 `belief-consistency`). 출력은 `references-kg.ttl`에 이어 붙는다(p9-evidence-ledger-with-belief) | 읽을 수 없는 단위 지식·값 어휘 |
| `odd2kg.py` + `taxonomy.py` | OpenODD YAML 매핑 문서 `kb/odd/project-odd.yml`(`TAXONOMY`·`MODULES`·`INCLUDE_AND`…) → `project-odd.ttl`; `related/condition` → `taxonomy.yml` (부록 E.4) | 택소노미 밖 범주 · 미선언 속성 · 선언 밖 리터럴 · OpenODD 식이 아닌 값 · `ATTRIBUTES`/`CHECKS` 없는 조건 |
| `gates2kg.py` | 게이트 등록부 `defs/kb.bzl` 의 `GATES` 리터럴 + 등록부 사이드카(`tools/*.chunks.yml`) → `bazel-bin/kg/gates-kg.ttl` 의 `id:gate-<id>` 개체. 게이트는 프로세스 층의 **항목**이라 그래프에 개체가 서야 층별 집계(CQ-38)가 셀 자리를 갖는다 ([`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md)). 개체마다 한/영 라벨·`skos:definition`·`agt:inLayer agt:processLayer`·`agt:gateTier`·`agt:enforcedBy`(판정 도구의 파일 복합체 — `agt:judgedBy` 는 정의역이 `agt:Chunk` 인 개발 프로파일의 술어라 쓸 수 없다)를 낸다 — 판정 도구가 파이썬 밖(`starlark`·`bazel`)인 게이트는 가리킬 코드 지식이 없어 마지막 술어를 갖지 않는다. 생성물이라 `kg/` 에 손으로 쓰지 않는다 | 항목의 네 키 누락 · 실행 계층이 `GATE_TIERS` 밖 · 판정 도구의 파일 복합체 부재 |
| `labels.py` | 단위 지식 head → OKF `index.md` (5.6절) | frontmatter 오류 |
| `metrics.py` | 그래프 → `metrics.md` (4.13절 지표, CQ19·CQ20, 14.1 통과 조건; 구축에는 frontmatter 링크 개체와 본문 식별자 추출(`cites`·`usesConcept`)이 들어가고 복원은 후보 파이프라인 산출만(유저 결정 2026-09-12 (b)), 가정 절에 "기본 가정만 가진 단위 지식"). 연결 성분과 CQ20 후방 추적은 `prov:specializationOf` 를 **연결로 센다**(2026-10-01) — 분할 조각은 원 단위 지식의 정체성을 나눠 가진 것이지 새 지식이 아니고 링크는 승계 단위 지식이 가지므로([`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)) 조각이 그 키 하나만 가져도 고립이 아니다. 그 술어는 추적 링크 네 족 밖(PROV-O)이라 링크 밀도·TIM 에는 들지 않는다. 연결로 세는 술어의 단일 정의 위치는 `kb_lib` 의 `LINKAGE_PREDICATES`·`ASCRIPTION_PREDICATES`·`COMMUNITY_EDGE_KINDS` 셋이고 `metrics`·`community` 가 거기서 읽는다. 연결 성분은 `kb_lib.linkage_predicates` 로 세 족의 하위 속성을 T-Box(`//kb/ontology:modules`)에서 전이적으로 더하고 복합체를 경유 노드로 둔다(2026-10-04) — 절 단위 지식의 `agt:projectsConvention`(치역 결정 기록)과 중첩 복합체(문서 → 묶음)가 그 경로로 이어진다. 성분이 1보다 크면 「주 성분 밖 단위 지식」 절이 성분마다 라벨·지식 종류·경로를 낸다 — 수만으로는 무엇이 떨어졌는지 보고서로 알 수 없다 | 그래프 파싱 실패 |
| `stamp.py` | 등록부의 `tested: {rev, at, source_hash}` 를 갱신한다 — `artifact` 의 `verified` 는 사람 검토가 아니라 **테스트 통과** 도장이고 판정 주체가 바뀐 것이지 검사가 약해진 것이 아니다 ([`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md) "도장"). **`bazel test //...` 가 종료 0 으로 끝난 뒤에만 돌린다** — 중첩 Bazel 호출을 피하려고 도구가 스스로 테스트를 부르지 않으므로 그 순서는 규범이다. 도구가 지키는 것은 리비전이 실재를 가리키는가 하나다: `--rev` 가 없으면 소스가 커밋되어 있어야 한다. 추출기가 `tested.source_hash` 가 지금 소스와 같을 때만 `verified: [{by: process:bazel-test, at: …}]` 를 낸다 — 소스가 도장 뒤에 바뀌면 `verified` 가 빠져 수정 뒤 미검증이 되고 재검증이 자동이다 | 커밋되지 않은 소스에 `--rev` 없는 도장 · `source` 없는 등록부 |
| `extract.py` | 소스 파일 하나(`tools/*.py`) + 등록부 사이드카(`<소스>.chunks.yml`) → `kb/dev/artifact/<모듈>/`의 단위 지식 트리 (`artifact`×`executable`). 코드가 원본이고 단위 지식은 생성물이다 ([`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md)). 구조는 파일 복합체 → 절 복합체(소스의 절 주석 `# ══ 장` · `# ── 절`) → 정의 단위 지식 셋이고, 링크(`refines`)는 등록부가 주어 파일 단위 지식과 절 단위 지식(복합체의 선언 단위 지식)에만 붙는다 — 정의 단위 지식은 `part_of`로만 존재해 함수 churn이 링크를 움직이지 않는다 ([`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md)). 한정 이름 → uuid의 원본은 등록부이고 신설만 자동이다 — 개명·삭제는 사람의 편집이다. 등록부의 손 필드 `layer`는 소스 하나의 서비스 층이고 추출기가 생성 단위 지식 전부(정의·절·파일)의 frontmatter로 옮긴다(2026-10-01) — 도구는 프로세스 층의 실행 표면이라 값은 `process`이고 측정 37 등록부·단위 지식 642다. 정의 단위 지식은 선택 키 `uses: [<청크 IRI>…]`를 갖는다(2026-09-30) — 최상위 정의를 이름으로 쓰는 관계이고 해소는 AST 의 이름 참조뿐이다. 모듈 안 해소(`used_defs`)의 제외는 다섯이다(자기 자신·섀도잉된 이름·최상위 정의가 아닌 이름·`ast.Attribute`의 뒤쪽 이름·다른 모듈의 이름). 경계는 둘이고 둘 다 `--residency`(기본 `<루트>/defs/kb.bzl`)의 리터럴이 단일 정의 위치다. **방출 경계** `EXTRACTED_SOURCES` 안의 소스에서만 내고 — 추출기가 하나라 경계가 없으면 37 파일이 한꺼번에 든다(유저 답 2026-09-30) — 표본 하나에서 시작해 37 파일 전부로 넓혔다(2026-10-01, 유저 답 1). **치역 경계** `USES_TARGETS` 안의 모듈만 모듈 밖 대상으로 삼는다(2026-10-01, 유저 답 1 — 표본 쌍 `kb_lib` 하나부터, 넓히기는 그 리터럴에 이름을 더하는 것이다). 모듈 밖 해소(`import_bindings`·`used_foreign_defs`)는 최상위 import 와 정의 안의 늦은 import 가 묶은 이름을 보고 `kb_lib.<이름>`(별칭 포함)과 `from kb_lib import <이름>`의 `Load` 참조를 대상 모듈 등록부의 `fn:`·`cls:` uuid 로 푼다 — 제외는 넷이다(`as` 별칭으로 철자가 바뀐 이름·섀도잉된 뿌리·등록부에 없는 이름(상수·모듈 변수)·치역 경계 밖의 모듈). 측정 `agt:usesDefinition` **667** 트리플(모듈 안 484 · 모듈 간 183, 치역은 전부 `kb_lib`), 오탐 0·누락 0(독립 정규식 대조 186 중 3은 docstring 인용). `EXTRACTED_SOURCES`의 단일 정의 위치는 `defs/kb.bzl`이다(M1, 2026-10-01 — `BUILD.bazel`은 그 리터럴을 load 하고, `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 파생한다. 전에는 둘로 적혀 있었다). `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의 존재와 그 목록이 같은 집합인지 로드 시점에 강제한다 — 갈리면 bazel 명령이 바로 FAIL 한다. **질의 디렉토리**(2026-10-03, 2단계 편입)도 같은 방향으로 추출한다 — 목록의 단일 정의 위치는 `defs/kb.bzl`의 `EXTRACTED_QUERY_DIRS`이고 소스는 디렉토리 `tools/<이름>`, 그 안의 `*.rq` 질의 파일 하나가 단위 지식 하나(`kb/dev/artifact/<이름>/<stem>.md`)다. 질의는 정의로 나뉘지 않으므로 파일 전체가 인용 하나이고 복합체를 세우지 않으며 링크는 단위 지식마다 붙는다. 등록부는 `tools/<이름>.chunks.yml`(키 `query:<stem>`)이고 `source_hash`는 디렉토리 안 질의 파일 전부의 해시다(`source_digest` — 도장도 같은 함수를 쓴다). 드리프트 테스트는 `//:extract_drift_<이름>`(`-`는 `_`)이고 게이트 id는 같은 `extract-drift`다. 커밋한다 | 직접 부분 9개 초과(절 주석을 요구한다) · 개명 안내(본문 해시가 같고 이름만 다름) · 등록부에 있는데 소스에 없는 이름 · `--check`의 어긋남 |
| `gen_build.py` | 단위 지식 frontmatter → `BUILD.bazel`(`kb_chunk`·`kb_decision`·`kb_composite` 타깃, 링크 = deps; `kb/vv/{goal,scenario,criteria,case,verifier}/`는 디렉토리 = 지식 종류). `kb_composite`의 `ordered`·`part_iris`는 선언 단위 지식의 `composite.ordered`를 옮긴 뷰이고, 선언이 없으면 `ordered` 인자도 없고 `part_iris`는 `srcs` 순서로 뜻을 갖지 않는다. **결정 묶음의 `ordered`는 생성기가 넣는다**(필수, 결론·근거·대안 — 유저 승인 2026-09-29: 결정도 예외 없이 선언한다. 205개 `conclusion.md`를 손으로 고치는 것이 첨가이므로 선언의 자리를 생성 BUILD의 명시 인자로 둔다). 커밋한다 | 세 단위 지식 없는 결정 디렉토리 · 끊긴 링크 · `_check_bundle`(패키지 밖 부분·부분 수·이질·`ordered`가 부분 집합과 불일치·**시나리오 묶음(`kb/vv/scenario/`의 `-stimulus`·`-factors`·`-excluded`)에 `ordered` 없음** — 자극 → 요인 → 배제 자극의 읽기 순서가 정해져 있어 선언 없는 묶음은 거짓 무순서다) |
| `consistency.py` | 단위 지식 본문 + 용어집 → `consistency.md` (`bazel build //kb:consistency`): 정확·근사 중복, 묶인 쌍(`coUpdatesWith`)의 응집 저하(본문 5-gram Jaccard < θ/2 — 의미 응집 검사의 첫 형태, 학습 모델 임베딩은 ODD 명시 제외), 라벨 중복, 결론 라벨 형식(결론만 — 근거·대안 라벨은 명사구 관례), 용어집 옛 표기, 중복률, ⑧ 첨가(메타 문장·채움 문구·빈 값 이상 표기 — `p4-three-empty-values`), ⑨ 목록 규칙(손 번호·항목 수·중첩·항목 길이 — `p4-slot-answers-one-question`), ⑩ 중복 확정 후보(①·③의 미묶음 쌍을 판정자 질문 "이 두 블록은 같은 주장을 담는가?"의 입력으로 다시 낸다), ⑪ 자리 후보(둘 이상의 본문 슬롯을 가진 단위 지식에서 다른 슬롯의 표지 낱말이 자리 밖으로 등장하는 문장을 판정자 질문 "이 문장이 그 슬롯에 있어야 하는가?"의 입력으로 낸다). ⑧·⑨는 2026-09-22에 더했고 **게이트가 아니라 보고**다. 수치가 0이 된 뒤 `chunk_lint`로 올린다. ⑩·⑪은 2026-09-30에 더했고(judge-without-service 기계 환원 ②) **후보 생성까지이며 게이트로 올리지 않는다** — 확정은 판정자(사람 또는 세션 판정자, `tools/judge.py`) 몫이다. 보고 뷰이며 게이트가 아니지만 `//kb:consistency_build_test`가 `bazel test //...`마다 생성한다(rules.md "커밋마다") ([`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)) | 파싱 실패 |

#### 하네스 도구 — 역할 규약과 인수

| 도구 | 하는 일 | 게이트 |
|---|---|---|
| `channel_lint.py` | 하네스 채널(`harness/channel/` 메시지 · `harness/user/` 질문지) 규약 — 어휘, 단일 작성자, type별 방향, `task` 필수 절, `re`·`source` 실재, `result` 없는 `task`의 완료 거부, hci 반영 흔적, 경어·감탄, 식별자 옆 한글 이름 | `//harness:channel_lint_test` |
| `endorse.py` | 인수 — 지식 종류 쓰기 권한이 있는 역할이 검토한 단위 지식에 `verified`를 붙인다. `//kg:gate_test`의 writer 검사(`generated.by` 역할 × 카탈로그 쓰기 권한)를 해소하는 수단이다 | `bazel run //tools:endorse -- --by <역할>/<모델> --at <시각> <청크…>` |
| `label_sample.py` | 라벨 대표성 실험 표본 — 층화 표본 + 미끼, seed 고정 ([`label-representativeness-protocol`](../harness/user/archive/legacy/label-representativeness-protocol.md)). `sheet.md`의 척도 문구는 프로파일(`kb_lib.judge_load_profile`·`judge_questions`)에서 그대로 읽는다(단일 정의 위치, 2026-09-30). `--judge-sheet <dir>`(선택)을 주면 세션 판정자에게 줄 `labels.md`(라벨+`kb_lib.label_fingerprint` 대조 해시값)·`bodies.md`(본문)를 낸다 — 생성 머리·경로·seed 없이, **워크스페이스 밖**에만 쓴다(안이면 거부). `--pair-sheet <dir> --pairs <링크 후보 뷰>`는 쌍 판정지다(task 0262) — 첫 근거가 동시 편집이고 판정이 아직 없는 후보에 음성 미끼(근거 없는 같은 KB 쌍)와 양성 미끼(확정된 `overlapsWith`)를 섞어 `pairs-NN.md`(질문·링크 종류와 정의·두 항목의 라벨과 본문·`kb_lib.pair_fingerprint` 해시값)와 정답 `key.json`을 워크스페이스 밖에 낸다 | 게이트 아님 — 실험 |

YAML은 PyYAML로 읽는다. 잠금은 `pyyaml==6.0.2`이고, 해시는 호스트 휠과 sdist의 둘이다. 부분집합 로더
`kb_yaml.py`는 2026-09-11에 삭제했다. 생성물은 `bazel-bin`에만 두고, 소스 트리에는 같은 이름의 파일을 두지 않는다.
`index.md`와 `log.md`도 마찬가지다.

#### `assume_check.py` — 가정 판정과 전파 (6.9절, 도입 4단계 첫 형태, 2026-09-14)

명령은 `bazel run //tools:assume_check -- [--break <cond-id>…] [--record]`다. 이 도구는 가정마다 `refersTo`로 가리킨
ODD 조건의 판정(`odd_check`와 같은 `CHECKS.cmd`)을 모두 참이어야 하는 조건으로 평가해 `valid`나 `invalidated`,
`unverified`를 낸다. 가정의 판정 술어 등급은 참조한 조건 등급 가운데 가장 낮은 것이다. 깨진 가정을 `assumes`하는
살아 있는 단위 지식이 직접 영향 집합이고, 여기에 링크와 복합체 형제로 닿는 하류를 더한 것이 suspect 후보 집합이다.
이 계산이 전파(`propagate`)의 첫 형태다.

`--break`는 조건 하나를 이탈로 가정하고, 계산된 영향 집합이 실제 의존 집합과 같은지 보는 인위 파괴 실험이다.
`--record`는 실행 결과를 관측(`kb/dev/memory/obs-<시각>.md`, `memory` 지식 종류, append-only)으로 남기고,
이 관측이 무효화 이력의 자리다. 새 어휘는 없다. 가정 자체의 `when` 판정 술어는 다음 단계에서 다룬다.

#### `vv_run.py` — V&V 실행기 (8.15절, 도입 7단계 첫 형태, 2026-09-19)

명령은 `bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--verifier <슬러그>…]`다. 이 도구는 테스트
케이스(`kb/vv/case/*.md`)와 검증기(`kb/vv/verifier/*.md`) 본문의 `**실행 명령**`을 읽는다. 그 가운데 읽기 전용
검증기(`bazel test`, `bazel build`, `bazel query`, `gen_build --check`)만 실행하고, 그 밖의 명령(임시 파일 자극,
`bazel run`)은 SKIP으로 적는다.

검증기는 테스트 케이스와 같은 줄 꼴과 허용 목록, 기대 대조, 판정 규칙으로 돈다(2026-10-04, 유저 답 Q29-a). 비표본
판정을 검증기로 옮긴 뒤에도 그 명령이 실행 경로에 남게 하기 위해서다. 선택이 없으면 둘 다 돌고, `--case`만 주면
테스트 케이스만 도는 보고와 기록의 꼴이 그대로 유지된다. 실행 기록은 검증기 행을 테스트 케이스 표와 따로 둔 검증기
표(`kb_lib.RUN_VERIFIER_TABLE_HEADER`)에 적는다. 실행 증거(`run_evidence`)는 테스트 케이스 표만 읽기 때문이고,
검증기에는 `verifies`가 없어 증거 쌍이 서지 않기 때문이다. 실행 명령 줄이 없는 검증기는 실행 대상 밖으로 따로 센다.
고정물 시험은 `//defs/tests:vv_run_fixture_all_test`와 같은 꼴의 셋(`all`, `case`, `verifier`)이다.

테스트 케이스의 판정은 **명령 전부를 실행해** 정한다(2026-09-22 정정). 전부 0으로 끝나면 `pass`이고, 실행한 명령에
실패가 있으면 `fail`이며, **건너뛴 명령이 하나라도 있으면** `skip`이다. 건너뛴 명령은 게이트가 거부한다는 것을
보이는 절반이므로, 절반만 실행한 테스트 케이스는 기준을 보이지 못한다. 따라서 SKIP은 PASS가 아니다(실패 종류 3).
보고는 명령 단위의 집계(`실행`, `건너뜀`, `명령`)를 따로 낸다. 실행 기록에는 리비전과 UTC 시각, bazel과 python의
버전, 명령별 종료 코드와 소요 시간을 적는다. 리비전 자리에는 **변경된 추적 파일 수**(`git status --porcelain
--untracked-files=no`의 줄 수)를 함께 적는다. 변경된 추적 파일이 있으면 그 실행의 테스트 케이스 판정을
`재현 불가 후보 n/N = p.p%`로 보고와 실행 기록의 판정 요약에 함께 센다(2026-10-01). 같은 리비전을 다시 체크아웃해도
같은 입력이 아니기 때문이고, 이 집계가 현상 `agt:concurrentSessionState`(P22)의 관측 수단이다.

`--record`는 실행 기록(`kb/vv/run/run-<시각>.md`, `memory` 지식 종류, concrete, `generated.by: process:vv_run`)을
append-only로 남긴다. 이것은 도구가 executor 하위 역할을 맡는 첫 형태여서 writer 검사 밖이다. 종료 코드는 fail이
1, pass가 0, skip만 있으면 3이다.

**기대 대조와 자극 생성은 2026-09-23에 들어왔다**([`p8-machine-readable-case`](../kb/dev/decision/p8-machine-readable-case/conclusion.md)).
테스트 케이스가 `**자극**`과 `**기대**` 산문 옆에 `yaml` 펜스로 `files`(이름에서 내용으로의 대응)와 `expect`(명령마다
`exit`과 `contains`)를 적으면, 검증기는 자극을 임시 디렉토리에 쓰고 명령의 `{{이름}}`을 실제 경로로 바꿔 실행한 뒤
지운다. 판정은 종료 코드와 문구가 **둘 다** 맞아야 통과다. 종료 코드만 보면 기대한 사유로 실패했는지 알 수 없기
때문이다.

펜스가 있는 테스트 케이스에 한해 저장소 자신의 읽기 전용 검증기(`python3 tools/<v>.py`)를 더 실행한다. 그 검증기는
닫힌 집합이고, 2026-09-26에 `assume_check`가 들었다. 다만 **허용 목록은 그대로 보안 경계다.** 위험은 자극의 유무가
아니라 명령이 무엇을 할 수 있는가에 있기 때문이다.

- 리다이렉션과 파이프, 백틱이 있는 명령은 실행하지 않는다.
- **쓰기 인자도 막는다.** `--record`(관측을 쓴다)와 저장소 안 경로의 `--out`(`{{이름}}` 자극이 아닌 값)은 SKIP이고,
  사유에 수정 방향을 적는다. `--break <조건>`은 읽기만 하므로 실행한다. 이 검사는 `assume_check` 전용이 아니라 허용
  목록 전체에 걸린다. `--out /dev/null` 같은 예외는 열지 않았다. 허용 목록은 보안 경계여서, 넓히는 판단은 승인을
  받아야 하기 때문이다.
- **`bazel run //tools:<v>` 형태는 허용 목록 밖이고, `FAIL [vv-case]`로 실행 전에 거부한다.** 그 형태에서는 작업
  디렉토리가 runfiles 트리여서 상대 경로가 자극에 닿지 못한다. 그때 나오는 입력 단계 오류는 기대한 거부와 같은 종료
  코드와 문구를 내므로 거짓 통과를 만든다([`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)).

명령은 워크스페이스 루트를 작업 디렉토리로 삼고, 실행기의 파이썬과 runfiles 변수(`PYTHONSAFEPATH`, `PYTHONPATH`,
`PYTHONHOME`, `RUNFILES_*`)를 걷어낸 환경에서 돈다. 실행기를 부르는 방식이 판정을 바꾸면 재현이 아니기 때문이다.
다만 `python3 `로 시작해 검증기를 직접 부르는 명령은 예외 하나를 받는다(2026-10-01, `verifier_env`). 인터프리터는
vv_run 자신의 `sys.executable`로 바꾸고, `PYTHONPATH`는 vv_run 자신의 `sys.path` 가운데 하네스의 pip 폐포
(site-packages) 항목만으로 바꾼다. 걷어내는 대상은 실행기의 **도구 모듈** 문맥(runfiles 사본의 `tools/`)이지 서드파티
패키지가 아니므로, 이 예외는 [`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)과
어긋나지 않는다. 이 예외는 bare `python3`에 `tiktoken` 같은 하네스 전용 패키지가 없어, 토큰 계수가 들어간 검증기가
자극에 닿기 전에 `ModuleNotFoundError`로 죽던 문제(이 저장소 측정, 2026-10-01)를 해소한다. 그래서 vv_run의 BUILD
의존에 `tiktoken`과 `pyshacl`, `owlrl`을 더해, READ_ONLY_VERIFIERS 전체가 쓰는 서드파티 패키지를 그 폐포에 올렸다.

토큰 계수기의 어휘 경로는 실행기가 `--vocab`으로 받아 `KB_TOKENIZER_VOCAB` 환경 변수로 넘긴다(2026-10-01). 값의
원본은 `tools/BUILD.bazel`의 `args = ["--vocab=$(rootpath @tiktoken_o200k_base//file)"]`이고, 다른 도구와 같은 꼴이다.
**runfiles 탐색을 배선의 원본으로 쓰지 않는다.** `use_repo_rule`로 만든 저장소의 runfiles 디렉토리 이름은 canonical
이름 `+http_file+tiktoken_o200k_base`인데, apparent 이름만 찾던 `chunk2kg.tokenizer_vocab_path`의 후보는 전부
빗나갔기 때문이다(이 저장소 측정, 2026-10-01). 그 결과 환경 변수가 비어 테스트 케이스 `token-budget`과
`chunk-42-lines`가 자극에 닿기 전에 죽었다. 지금은 그 후보에 canonical 이름도 더했고, 명시 경로가 우선한다. 어휘를
찾지 못하면 `vv_run`은 테스트 케이스를 하나도 돌리지 않고 `EXIT_CONFIG`로 종료한다. 건너뜀은 판정이 아니라 판정의
공백이므로 `FileNotFoundError`를 삼키지 않는다.

펜스가 없는 테스트 케이스는 지금처럼 양성 명령만 돈다(점진 도입). 형식 위반은 `FAIL [vv-case]`로 실행 전에 멈춘다.
임시 파일 자극의 자동 생성은 이로써 갖춰졌고, seed 고정은 다음 단계에서 한다.

**2026-10-04** — 허용 목록의 읽기 전용 검증기에 `revalidate`의 **스냅숏 꼴**(`--base-dir`와 `--head-dir`, 또는
`--base-files`와 `--head-files`)이 들어왔다(유저 답 Q38-c). 기본 꼴(`--base <rev>`)은 git과 `bazel query`를 부르므로
SKIP이다. `--round stop-rule|budget|complete`는 테스트 케이스를 돌리지 않고, 검증 라운드 하나를 닫는 라운드 기록
`kb/vv/run/round-<UTC>.md`(memory, append-only)를 남긴다(유저 답 Q39-c). 라운드 기록은 라운드 번호와 구간 안의 신규
결함 수, 종료 사유를 담는다. 종료 사유는 온톨로지 `round-end-reason-ontology.ttl`의 개체 셋이고, 정지 규칙은 verify
질의 `round-stop-rule-violated`가 판정한다.

#### `odd_check.py` — ODD 모니터링 (3.5절, 도입 2단계)

`bazel run //tools:odd_check`는 ODD 문서의 `CHECKS.<속성>.cmd`를 실행해 속성마다 in과 out, unverified 가운데 하나로
판정하고 이탈을 보고한다. 종료 코드 1은 이탈이 있다는 뜻이다. 이 도구는 네트워크와 호스트의 상태를 보므로 테스트
타깃으로 두지 않는다. 첫 모니터링(2026-09-11)에서는 7속성이 모두 in이었고, 이탈은 0건이었다.

### 활용

활용 도구가 없으면 "온톨로지를 활용하는 방법론"이 성립하지 않는다. **첫 형태가 있는 활용 도구는 2026-09-11의
`workset`과 `metrics`, `impact`, `handoff`, `consistency`, 2026-09-14의 `query`와 `propagate`/`revalidate`, 2026-09-19의
`weave`와 `gen_skills`다.** 복원 후보를 만드는 `link`도 2026-09-19에 생겼다. 반면 `gendoc`(2026-09-21)은 활용
도구가 아니라 생성 문서 전부의 형태를 보는 게이트이고, 생성기가 쓰는 머리 블록과 검사 함수의 단일 정의 위치는
`kb_lib`다([`STYLEGUIDE.md` §9](../STYLEGUIDE.md#9-생성-문서-bazel-binmd--생성-트리-파일)). 아직 없는 도구는 tangle이다.
구축 쪽 공백의 공통 원인은 하네스의 도구가 읽기 집합과 쓰기 집합을 기록하지 않는 것이다.

| 도구 | 대응 절차 | 하는 일 | 단계 |
|---|---|---|---|
| `workset` / `labels` | [method §8 조회](method.md#8-조회) | **첫 형태 있음** — `bazel build //kg:workset --//kb:role=<role> --//kb:anchor=<라벨|IRI> --//kb:levels=<창> --//kb:hops=1 --//kb:budget=<토큰>` → `bazel-bin/kg/workset.md`: 역할 적용 범위(지식 종류) × 수준 창 × 앵커 이웃(상류 ∪ 하류), 족별 우선순위(앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo ≫ 시간축) 뒤 예산 패킹, 초과분은 라벨만(dependency-graph §4, 2026-09-12). 선택자는 빌드 설정이라 BUILD를 고치지 않는다. 정의(0.5절 정정본)대로 앵커가 양을 거른다 — 예산의 기본값은 `//kb:budget`(원본 `kb_lib.CONTEXT_TOKEN_BUDGET`)이고 뷰의 크기는 생성물 머리 블록이 토큰으로 적는다 | 2 |
| `link` | [method §6 연결](method.md#6-연결) | **첫 형태 있음**(2026-09-19) — 복원 후보 생성기 `bazel build //kg:link_candidates` → `bazel-bin/kg/link-candidates.md`: 그래프 union만으로 본문 식별자(`cites`, 구축 기록)·테스트 공동 커버(`verifies`)·개념 공유(`usesConcept` ≥ 3, `proposal`)에서 후보를 내고 TIM 허용 칸·지식 종류 단방향·수준·복합체 형제로 탈락시키며 앵커당 k ≤ 7이다. 상한 안의 후보는 근거 순위, 공유 개념 수, 대상 IRI 순서로 정하고 라벨로 정하지 않는다([`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md), Q169-a). 채택은 사람이 링크 키와 `restored` 목록에 적는다([`p10-restored-link-marking`](../kb/dev/decision/p10-restored-link-marking/conclusion.md)) — 복원 비율은 `metrics`·`audit`가 `kb_lib.link_origins`로 센다. 구축 쪽: frontmatter 링크마다 `agt:Link` + 구축 기록 증거를 `chunk2kg`가 방출, `handoff`가 workset 뷰의 펼친 지식을 `sources`로 옮긴다 (`bazel run //tools:handoff -- --workset bazel-bin/kg/workset-<role>.md <청크>`). 동시 편집 관측의 쌍(`coEditHistory`)이 첫 근거인 후보는 판정자 둘의 판정 증거(`agt:judgement`)로 일치(+,+) · 일치(−,−) · 불일치 · 판정 없음으로 갈리고, 사람 확인 큐(후보 표)에는 첫 근거가 동시 편집이 아닌 후보, 일치(+,+) 전부, 일치(−,−)의 표본이 판정자 값과 함께 오른다(task 0262, task 0303). 표본은 쌍마다 고정 시드를 붙인 sha256 값(`kb_lib.JUDGED_NO_SAMPLE_SEED`)이 가장 작은 `kb_lib.JUDGED_NO_SAMPLE_SIZE`쌍이고 판정자 값에 `표본(−,−)`이 붙는다. 표본 밖 일치(−,−)는 큐 밖 절에 후보로 남는다. 없는 것: `relatedTo` 후보의 복원 표시 | 3·8 |
| `propagate` / `revalidate` | [method §7 갱신](method.md#7-갱신) | **첫 형태 있음** — `propagate`는 `assume_check`의 전파 절(깨진 가정 → 직접 영향 집합 → 하류 suspect 후보). `revalidate` — `bazel run //tools:revalidate -- --base <rev>`(또는 git 없이 스냅숏 둘 — `--base-dir`·`--head-dir`·`--base-files`·`--head-files`, 2026-10-04 유저 답 Q38-c, 하류 의존자 열은 빈다): base 리비전 대비 본문 해시가 바뀐 단위 지식과 그 링크 양 끝·`part_of` 형제·`rdeps` 하류를 재검증 대상 표로 낸다(종료 1 = 대상 있음). head만 바뀐 단위 지식은 제외한다. **2026-09-26** — `## 재판정 대상 링크 개체` 절이 본문 해시가 바뀐 단위 지식을 양 끝으로 갖는 `agt:Link`(head 그래프와 같은 IRI)를 낸다. **2026-10-01** — 요약과 머리에 **바뀐 끝이 결정 결론(`conclusion.md`)인 재검증 링크 수**를 함께 낸다: 결정의 본문과 구현이 어긋나는 현상(`agt:reasoningActionMismatch`, P16)의 판정 대상 행이고 0 이면 공허 합격이다. **2026-09-30** — 표에 `호출부` 열이 붙는다: 본문 해시가 바뀐 정의를 `uses`(`agt:usesDefinition`)로 가리키는 출발점의 수이고 **코드 호출부 파손의 상한**이다. 모듈 안 호출과 치역 경계(`defs/kb.bzl`의 `USES_TARGETS` — 2026-10-01 표본 쌍은 `kb_lib` 하나다) 안의 모듈 간 호출을 세므로, 경계 밖을 치역으로 하는 호출은 빠지고 실제 파손은 그 수보다 크다. `assume_check`는 링크의 `when`을 ODD 판정으로 평가해 거짓이면 `suspect`를 보고하고(종료 1) `kb_lib.SUSPECT_TRIGGERS`의 켜진 종류(`supersedes`)를 전파한다 — **상태는 저장하지 않는다**. 무효화 전파 8단계·규칙 카탈로그 전체는 없다 | 4 |
| `query` | [competency-questions](competency-questions.md) | **첫 형태 있음** — `bazel run //tools:query -- <CQ> [--labels] [--bind ?v=…]`가 역량 질문 질의(`tools/cq-queries/*.rq`, 하나가 CQ 하나이고 수는 그 디렉토리가 정한다)를 그래프 union 위에서 돌린다. 결과는 라벨 목록이다. 뷰 `bazel build //kg:cq` → `bazel-bin/kg/cq.md`가 CQ마다 행 수와 상위 5행을 낸다(2026-09-14) | 3 |
| `impact` | [method §12 영향 분석](method.md#12-영향-분석) | **첫 형태 있음** — `bazel run //tools:impact -- <타깃>`: `rdeps`로 영향 항목 수·지식 종류 분포·suspect가 될 링크 수·승인 필요 결정 수. 구조 근사이며 가정·무효화 전파는 그래프 질의 몫이다 | 3 |
| `project` / `weave` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음** — `weave`(2026-09-19): `bazel build //kb/dev:adr`(결정 기록의 ADR 뷰) · `//kb/dev:requirements`(요구 색인 — EARS 패턴·정제 수·도달 수준) · `//kb/dev:changelog`(`supersedes` 이력) · `//kg:audit`(감사 보고서 — 검증 현황·최근 실행·**판정 주석**·가정·추적 매트릭스·검증 표시·링크 근거를 그래프 union과 관측 본문만으로, 8단계 첫 형태). 판정 주석 절이 **라운드(날짜)별 신규 주석 수**를 표로 낸다(2026-10-01, `round_section`) — 라운드 경계는 주석의 `prov:generatedAtTime` 날짜이고 `generated.by` 가 `process:judge` 인 판정 결과는 판정자의 응답 기록이라 집계에서 뺀다. 연속한 두 라운드의 신규 수가 줄지 않으면 다음 라운드를 열지 않는 것이 정지 규칙이고 현상 `agt:unknownStopCondition`(P15)의 관측 수단이다. **2026-10-04** — 라운드 기록(`vv_run --round`)이 있으면 경계를 날짜 대신 그 기록으로 자르고(`round_record_section`) 없으면 날짜 대리로 떨어진다(유저 답 Q39-c). 생성물마다 생성 시각과 질의를 적는다(`p12-documents-are-generated`). `communities` — `bazel build //kg:communities`: 결정론적 Louvain으로 복합체 후보(같은 지식 종류·수준, 2~9)와 `relatedTo` 링크 후보(지식 종류·수준을 넘음)를 제안, 판정은 사람이 한다([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)). tangle은 없다 | 8 |
| `gen_skills` | [method](method.md) 정형 절차 | **첫 형태 있음**(2026-09-19) — `python3 tools/gen_skills.py --root .`가 도구 docstring과 `kb_lib.SKILLS`(도구·절 앵커·대표 명령)에서 `.claude/skills/<도구>/SKILL.md`를 생성한다. 트리에 두고 커밋하며 `//:skills_drift_test`가 재생성과 비교한다. BUILD와 같은 생성 트리 파일이며 손으로 고치면 다음 생성이 덮어쓴다 | 6 |
| `open_questions` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음**(2026-09-22) — `bazel build //kg:open` → `bazel-bin/kg/open.md`: 설계 공간(`--spaces` = `//space:design_space`)을 공간마다 한 행(제목·status·변수 from/kind·후보 state별 수·그 공간을 가리키는 슬롯)으로 내고, 공간을 가리키지 않는 선택 슬롯 `미확정:`을 head(`agt:bodySlot`)로 골라 질문과 단위 지식, 지식 종류와 수준, 상세 문서로 낸다. 슬롯의 상세 값이 공간 IRI이면 그 공간의 행에 붙는다. **미결 목록의 유일한 자리다** — 상세 다섯 절은 설계 공간에 있고(Q54-a) 손으로 관리하던 미결 색인 문서의 목록을 대체했다(2026-10-06, 지시 0095; [`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md)) | 6 |
| `space2kg` / `choices` | [method §5 후보 관리](method.md#5-후보-관리) | **첫 형태 있음**(2026-09-22) — `space/*-space.md`(변수 하나 = 파일 하나)를 A-Box `//space:design_space`로 올리고 체크박스 뷰 `//space:choices`를 낸다. 후보는 `kb_chunk` 타깃이 아니므로 **구조적으로 `deps`가 되지 못한다**. 근거 없는 배제와 확정 후보 수를 게이트 `space`가 거부한다 — `r-011`의 실물이다. 없는 것: CEL 평가기(`when`·양립 제약이 문자열) | 5 |
| `tokens` | [rules §1 chunk](rules.md#1-chunk--자립적-최소-지식-단위) | **있음**(2026-10-01) — `bazel run //tools:tokens -- [청크…] [--out <경로>]`: 단위 지식 본문의 토큰 수를 고정된 공개 토크나이저로 세어 지식 종류별 분포(최소·분위수·중앙·최대·줄당 토큰)·**42의 배수마다 초과 단위 지식 수와 비율**(42×1 … 42×20)·컨텍스트 예산의 환산·상위 20 단위 지식을 낸다. 단위 지식의 단위가 줄이 아니라 토큰이라는 유저 결정(2026-10-01)의 측정 수단이고 상한의 숫자(1,092(42의 26배) · 2,856(42의 68배))를 이 분포가 정했다. 계수기는 `tiktoken 0.12.0` + 어휘 `o200k_base`이며 어휘 파일은 `MODULE.bazel`의 `http_file(tiktoken_o200k_base)`가 sha256으로 고정해 네트워크 없이 runfiles에서 읽는다 — 해시가 다르면 로더가 거부하고 ODD 조건 `id:cond-tokenizer-lock`이 이탈한다. 생성 시각을 적지 않아 같은 입력에서 같은 바이트가 나온다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나라 게이트·방출·이 뷰가 같은 문자열을 센다. **게이트가 아니라 뷰다** — 상한의 강제는 `chunk_lint`(`chunk`)와 shape(`token-budget`)의 몫이고 이 도구는 분할 대상을 고르는 자리다 | 1 |
| `metrics` | [methodology 완료 판정](method.md#완료-판정) | **첫 형태 있음** — `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md`: 단위 지식 수·고아율·크기 분포·링크 밀도·CQ19·CQ20·신뢰 등급. **연결 성분과 CQ20 후방 추적은 관측(`memory` 지식 종류) 제외다**(유저 승인 2026-09-23) — 관측은 실행의 부산물이고 append-only라 사후에 링크를 이을 길이 없으며 추적 매트릭스에 `memory` 칸이 0개다. 관측을 세면 실행할수록 지표가 나빠지는데 그것은 고립이 아니라 기록의 축적이다. 없는 것은 suspect 비율·누락률·라벨 대표성이다. 분할 조각의 `prov:specializationOf` 는 그 두 지표에서 연결로 센다(2026-10-01, [`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)) — 조각은 링크를 승계 단위 지식에 두므로 원 단위 지식을 거쳐 요구에 닿는다. 성분이 1보다 크면 「주 성분 밖 단위 지식」 절이 성분마다 라벨·지식 종류·경로를 낸다. 2026-10-04 유저 결정으로 건너뜀을 결정 기록 몫·V&V 정제 계층 몫(V&V KB 안의 합격 기준 → 검증 목표 `refines`, Q30-b · 검증기 → 합격 기준 `refines`, Q41-a)·남는 몫으로 가르고, 5단계 절(결정 완결률·사람 확인 요구를 뺀 전방 추적)과 7단계 행(독립성·음성 고정물의 변이 검출률)을 더했다 | 1 |

`metrics`(1·2단계 대리 포함)와 `workset`, `odd_check`의 첫 형태가 생겼으므로, 문서는 수치를 적지 않고 생성물을
인용한다(`p4-projection-as-query`). 문서에 남아 있는 수치에는 스냅샷 표기를 붙인다.

## development — 개발 KB의 도구 (노트 Part VII, 전부 미구현)

| 도구 | 하는 일 | 규칙·절차 |
|---|---|---|
| `gate` | 전이 게이트 4종 — 기여 명시 / 범위·제약 / 표본 근거 / 기준 바인딩 (6.8) | [rules development](rules.md#7-development-규칙--개발-kb-노트-7277) |
| `space_check` | `-space` 호 일관성 · ODD 경계 · `when` 평가 · 증거 기록 규칙 · 확정 제안 (9.10, 9.11) | [method §5](method.md#5-후보-관리) |
| `feedback` | `-space` → 체크박스 파일 · 되읽기 → 확정 (13.5) | [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| `contract_check` | 계약 선행 · 타입 · 사후조건 CEL 실행 가능성 (7.5) | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| `schema_compat` | 하위 호환 판정, 비호환이면 새 IRI + `supersedes` (7.6) | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `adr` | 결정 기록 뷰 (7.4) — **있음**: `weave --kind adr`, `//kb/dev:adr` (2026-09-19) | [p7-alternatives-mandatory](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| `tangle` | 구현 → 코드 파일 (4.6) | [method §9](method.md#9-뷰) |
| `dev_metrics` | 전방 추적 커버리지 · 후방 추적 커버리지 · 결정 완결률 · `-space` 체류 · 계약 선행률 · 대안 기록률 (7.8) | [p7-dev-kb-outputs-and-metrics](../kb/dev/decision/p7-dev-kb-outputs-and-metrics/conclusion.md) |

## V&V — V&V KB의 도구 (노트 Part VIII, 도입 7단계, `run`·`case_gen` 첫 형태 외 미구현)

| 도구 | 하는 일 | 절 |
|---|---|---|
| `goal_derive` | 요구 → 검증 목표 후보 | 8.19 |
| `scenario_lint` | 변수가 ODD 속성인가 · 부류 참조 · 배제 자극 존재 · 자극 ≠ 기준 | 8.22 |
| `case_gen` | **첫 형태 있음** — `tools/case_gen.py`(2026-10-04, 유저 답 Q27-a): logical 시나리오 자극의 `yaml` 펜스 하나(`keep` · `cover` · `seed` · `case`)에서 concrete 테스트 케이스(`kb/vv/case/*.md` 꼴)을 결정론적으로 낸다. 규칙은 다섯(`sampling:equivalence`·`boundary`·`pairwise`·`factor`·`observed`)이고 규칙·seed·값·부류가 `**표본 근거**`에, 시나리오가 `derivesFrom`에 남는다. 생성 테스트 케이스는 `vv_run`의 파서로 되읽어 실행기가 읽는 꼴인지 본다. 출력은 `--out` 디렉토리이고 저장소 반영은 vnv가 한다. 드리프트 가드 `//:case_drift_test`는 대상 0으로 서 있다 | 8.23 |
| `verifier_bind` | 기준 바인딩 검사. 기준 없는 `verifies` 거부 | 8.11 |
| `env_assign` | 결함 요인 → 환경 단계, 재현성 조건 | 8.10, 8.12 |
| `run` | **첫 형태 있음** — `vv_run`(2026-09-19): 리비전·환경 버전 기록, 실행 기록 append(`kb/vv/run/`). **기대 문구 대조 있음**(2026-09-23, `contains`) · **환경 격리 상시 판정 있음**(`//tools:vv_run_env_test`) · seed 고정은 없다 | 8.15 |
| `judge` | **첫 형태 있음, 외부 서비스 없이 개정**(2026-09-30) — `bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>] [--record] [--into <디렉토리>] <청크 파일…>`: **게이트 밖 도구다.** 판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다 — `call_service`·`urllib` 호출과 자격 환경 변수(`AKB_JUDGE_*`)를 뺐다(유저 답 2026-09-30). `--fixture`(오프라인 고정물)를 정식 입력 `--responses`로 승격했다 — 세션 판정자가 낸 `{judge: <역할/모델 또는 세션 식별자>, responses: [{question, fingerprint, value, confidence}]}`를 받아 같은 형 검사(noul·choice·score, choice ≤ 255)·라우팅·로그·주석 생성을 돈다. 질문·척도·임계는 프로파일(`kb/ontology/profile/development/judge-question-ontology.ttl`·`judge-question-set-ontology.ttl`·`judge-threshold-ontology.ttl`·`judge-calibration-ontology.ttl` + `kb/ontology/shapes/judge-question-shapes.ttl`)에서 읽는다. 확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(판정자마다 하나) 주면 같은 (질문·입력 해시값)의 값 일치 여부를 계산해 로그의 `일치` 열(일치·불일치·해당 없음)에 낸다. 일치율 임계와 자동 적용은 결정 [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md)가 정확도·판별력 재측정 뒤 정한다 — 지금은 전부 사람 확인 큐다. **대조 해시값은 항상 세션 판정자가 실제로 본 라벨+본문**(`kb_lib.label_fingerprint`)이지 단위 지식 파일 바이트가 아니다(2026-09-30 vnv 결함 보고 ① — 파일 바이트로 대조하면 판정자의 응답이 전부 안 잡힌다) — 파일 바이트 해시값은 로그의 `입력 해시값` 열에 추적용으로만 남는다. `--decoys <json>`(`label_sample.py`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의 라벨+본문으로 실표본까지 스스로 대조하고, 미끼 검출률(**검출 = 척도의 최고값(적합)이 아니다**, orchestrator 결정 2026-09-30 — 판별력은 "미끼를 적합으로 통과시키지 않는가")을 보고 요약에 낸다. 결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>-<판정자>`다(2026-09-30 결함 보고 ② — 결정 세 단위 지식은 stem이 conclusion·rationale·alternatives뿐이라 그것만으로는 부딪힌다). 판정 로그(`kb/vv/run/judge-<시각>.md`, memory 지식 종류, append-only — 필수 필드 질문 id·값·확신도·**판정자 식별자**·입력 해시값(sha256)·시각, 읽기 열 대상·처리·일치, `관측` 문장은 응답 파일의 **basename만** 싣는다)와 결과 주석(`kb/vv/verdict/`, 주석 형식 — `본문:` 은 판정자가 쓰지 못해 `해당 없음`)을 낸다. 선택 집합 255 초과는 `FAIL [judge]` 로 거부하며 점수 → 선택 2단계를 안내한다. **쌍 모드** `--pairs <key.json>`(task 0262)는 `label_sample.py --pair-sheet`의 key로 링크 후보 쌍을 판정한다 — 질문은 noul `overlapsHolds`·`proposedLinkHolds`이고 행은 쌍 하나, `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>`, `입력 해시값`은 sha256(앵커 파일 바이트 ∥ 대상 파일 바이트)다. 미끼 행은 로그에 넣지 않고 검출률(음성에 no · 양성에 yes)만 남기며, 판정지 뒤에 라벨이나 본문이 바뀐 쌍은 행을 내지 않는다. 로그는 질문마다, 결과 주석은 쌍마다 하나(`judge-<질문>-pair-<쌍 해시값 8자>.md`, `targets:`에 두 IRI)다. 없는 것: 3지표(정확도·판별력·캘리브레이션) 측정과 head `verified` 반영, 일치율 임계 자체(`p8-judge-session-agreement`) | 8.14, 2.12 |
| `mutate` | 변이 주입 표본 검사 | 8.6 |
| `coverage` | 정제 완주 · 후방 추적 귀속 · logical 공간 커버, 경계값 별도, 6단계 제외 | 8.7 |
| `defect_classify` | `defect-rules` 추론: 요인·한정자·트리거·발견 단계 | 8.16~8.18 |
| `sim_trust` | 시뮬레이션 신뢰도 요인별 상관 | 8.13 |
| `vv_report` | 검증 상태 · 커버리지 · 결함 · 가정 건전성 · 독립성 — 검증 상태·가정 건전성은 `//kg:audit`(2026-09-19)이 낸다. 결함·독립성은 없다 | 8.24 |
| `independence_audit` | 개발 역할의 V&V KB 쓰기 흔적 = 0 | 8.5 |
| `vv_metrics` | 목표 파생률 · 기준 바인딩률 · V&V 완주율 · 실행 통과율 · 변이 검출률 · 재현 실패율 · 검증 대응물 지연 | 8.26 |
| `diagnose` | 불만족 핵 · 보간 · 최약 전제조건 · 명세 추론. 결과는 관측 | [12.12](../kb/dev/decision/p12-symbolic-diagnosis/conclusion.md) |
| `guide` | 지침 생성 — 귀속 후보 · 조치 · 배제된 전략 | [8.4](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| `proactive_vv` | 선제 트리거 감시(ODD 경계 · 커버리지 공백 · 외부 지식 · 증거 노화), 재실행 선택 | [8.27](../kb/dev/decision/p8-proactive-vv/conclusion.md) |

## Bazel 배선

**지식은 Bazel 타깃이다**(2026-09-11, [`bazel-dependency-review`](../harness/user/archive/legacy/bazel-dependency-review.md)
B와 연결성). `defs/kb.bzl`의 규칙 넷이 `ChunkInfo`와 `OntologyModuleInfo` provider를 내보낸다.

- `kb_chunk`는 단위 지식 하나를 타깃 하나로 만든다.
- `kb_decision`은 결정 기록 하나를 타깃 하나로 만들고, 대안을 필수로 요구한다.
- `kb_composite`는 결정 밖의 복합체를 타깃 하나로 만들고, 부분은 2~9개이며 동질이어야 한다.
- `kb_ontology_module`은 온톨로지 모듈 하나를 타깃 하나로 만들고, `owl:imports`를 deps로 삼는다.

frontmatter의 `refines`와 `serves`, `supersedes`, `verifies`가 **deps**다. BUILD는 `tools/gen_build.py`가
frontmatter에서 **생성**하고 커밋하며, `//:build_drift_test`가 원본과 비교한다(`p12-generated-lists-with-drift-check`).
Bazel이 맡는 것은 링크의 **구조**다. 끊긴 링크는 로드 에러가 된다. 링크의 방향은 분석 시점의 `fail()`과
`//kb:*_readers` 가시성이 지킨다. 파급은 `bazel query rdeps`로 계산하고, 토큰 상한과 frontmatter는 검증 액션이
`bazel build`만으로 본다. 반면 의미, 곧 SHACL과 통제 어휘, 상태는 그대로 union 게이트가 본다(`p6-validate-the-union`).
음성 시험은 `//defs/tests`에 있고 skylib analysistest를 쓴다.

```bash
bazel run //tools:impact -- //kb/dev/requirement:r-008-descend-to-executable   # 영향 집합 = rdeps (12.6절 네 수치)
bazel build //kg:workset --//kb:role=developer --//kb:anchor="두 KB" --//kb:levels=concrete   # 작업 집합 뷰, 선택자는 플래그
bazel build //kb/dev/decision:all                                                       # 검증 액션 = 토큰 상한·frontmatter
bazel run //tools:revalidate -- --base HEAD~1                                            # 본문 해시 변경 → 재판정 대상 링크·항목
bazel run //tools:extract -- tools/kb_lib.py                                             # 소스를 고쳤으면 코드 청크 재추출
python3 tools/gen_build.py --root .                                                     # frontmatter 를 고쳤으면 BUILD 재생성
```

`bazel test //...`는 게이트 전체이고, test_suite 없이 패키지의 test 타깃을 전부 돈다. 타깃 목록은 손으로 적지 않고
질의로 얻는다. 게이트 타깃의 목록은 `bazel query 'tests(//...)'`가 내고, 생성 뷰의 목록은
[`defs/kb.bzl`](../defs/kb.bzl)의 `VIEWS`다. 각 테스트 타깃이 어느 게이트 id를 판정하는지는 위
[게이트 총람](#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `id` 열과 그 아래 문단이 적는다.

배선은 두 가지로만 선언하고, `py_test`를 직접 쓰지 않는다. 하나는 `defs/knowledge.bzl`의 매크로(`kb_gate_test`,
`kb_reference_kg`, `kb_chunk_lint_test`, `kb_odd_kg`, `kb_taxonomy`, `kb_index`, `kb_metrics`, `kb_gendoc_test`)이고,
다른 하나는 `defs/kb.bzl`의 규칙(`kb_chunk`, `kb_decision`, `kb_ontology_module`, `kb_bundle`, `kb_kg_merge`,
`kb_workset_view`)이다.

## 게이트를 추가할 때 — 절차·판단 기준·기준선 (agrtls A·C·E, 2026-09-12)

게이트를 추가하는 절차는 결정 [`p6-mass-fail-suspects-the-rule`](../kb/dev/decision/p6-mass-fail-suspects-the-rule/conclusion.md)에
있고, 다음 순서로 진행한다.

1. **이름(id)**을 정한다.
1. **총람 행**에 무엇을 거부하는지와 실행 계층, id, 해소 절차를 적는다.
1. **도구**가 `FAIL [<id>] <경로>: <메시지>`를 내게 한다.
1. **첫 실행의 실태를 기록**한다.
1. **판정**한다.

첫 실행에서 FAIL이 대량으로 나오면 산출물이 아니라 규칙을 먼저 의심한다. 실례로 결론 라벨 형식 위반 197건은 규칙
원문("결론 문장형")대로 범위를 결론으로 좁히자 25건이 되었다.

| 구분 | 기준 | 자리 |
|---|---|---|
| **게이트** | 기계적으로 참·거짓이 갈리고 재현되며 오탐이 없다 | test 타깃 — `bazel test //...` |
| **보고** | 판정에 사람(또는 승인된 판정자)이 필요하다 | build 뷰 — `consistency`·`communities`·`metrics` |

**실패 종류**는 도구의 종료 코드로 나타내고, 그 값은 `tools/kb_lib.py`의 상수다. `1`은 판정 실패이고, `2`는 파일
없음이나 잘못된 인자, 파싱 불가 같은 설정과 입력의 문제이며, `3`은 미실행이다. 미실행은 검사 대상이 0건인 경우다.
**SKIP은 PASS가 아니다.** SKIP은 0이 아닌 종료 코드로 끝나므로 게이트는 실패로 표시된다.

**면제는 선언한다.** 선언하는 곳은 [`waivers.md`](waivers.md)이고, 항목은 게이트 id와 대상, 축, 사유, 판정자,
날짜다. 도구는 면제를 집계에서 빼되 목록에 남기고, 코드 속에는 예외 목록을 두지 않는다.

**비-초록 기준선**은 통과로 표시되지 않지만 알려진 상태이고 결함이 아닌 신호의 목록이다. 이 신호를 고치려 하지
않는다. 대신 상태가 바뀌면 이 표를 고친다.

| 신호 | 상태 | 왜 정상인가 |
|---|---|---|
| `//kg:gate_test` 로그의 `warn [usesConcept-deprecated]` | 정상 | 결정이 폐기 용어(`agt:confidence`·`agt:counterfactualTest`)를 **서술**한다. 경고를 낸 파일은 그 로그가 적는다 |
| `consistency` ⑥ 옛 표기 잔존 | 정상(면제) | 면제된 파일과 사유는 `waivers.md`의 게이트 id `term-drift` 행이고, 건수는 `bazel build //kb:consistency`의 요약 표가 낸다 |
| `metrics` "기본 가정만 가진 단위 지식" | 정상(진행 지표) | 기본 가정 뒤에 좁힌다. 목표 0은 도입 4단계이고 값은 `bazel build //kg:metrics`의 가정 절이 낸다 |
| `communities` 복합체 후보 | 정상(보고) | 후보 생성기의 출력이고 채택은 사람이 후보마다 판정한다. 수는 `bazel build //kg:communities`의 요약 표가 낸다 |
| `consistency` ⑦ 단정성 — 추측 표현·구어 후보·대시 밀도 목록 | 정상(보고) | 판정은 사람이 한다. 단위 지식은 문체만을 이유로 재작성하지 않는다(검증 표시 보존, 유저 결정 2026-09-13) — 신규·수정 문장부터 규칙을 적용한다 |

## 게이트 밖 — 규약으로 남은 것

**게이트도 없고 여기 적히지도 않은 규칙은 사실상 없는 규칙이다.**

| 규칙 | 왜 게이트가 아닌가 | 어디에 |
|---|---|---|
| 라벨이 본문을 대표한다 | 판정 불가 — 게이트로 만들지 않는다 | `STYLEGUIDE.md` §4. 보고 기구는 **세션 판정자**(외부 서비스가 아니다, 2026-09-30) — 질문 `agt:labelRepresentsBody`(score)를 `tools/judge.py --responses`로 묻는다(2026-09-29·2026-09-30) |
| 한 단위 지식은 한 주제 | 판정할 수 없다. 토큰 상한과 분할 신호가 대리 지표다 | `STYLEGUIDE.md` §0. 보고 기구는 **세션 판정자** — 질문 `agt:bodyHasOneClaim`(noul)을 `tools/judge.py --responses`로 묻는다(2026-09-29·2026-09-30) |
| 문서의 수치가 생성물의 수치와 같다 | 이름의 짝짓기가 사람의 대조다 — 문서가 수치 옆에 생성 타깃의 이름을 적는 규약이 서면 게이트로 올린다 | V&V 기준 [`document-table-matches-generated`](../kb/vv/criteria/document-table-matches-generated.md). 보고 기구는 `bazel run //tools:doccheck -- --report`(2026-10-01) — 진입점 문서 넷(위치 인자를 주면 그 목록으로 바뀐다, 2026-10-01 vnv 요청 — 이 모드만 루트 밖 절대 경로를 허용해 `vv_run` 테스트 케이스의 워크스페이스 밖 자극도 대조 대상이 될 수 있다) × 이름 열넷을 생성물(`//kg:metrics`·`//kg:audit`·`//kg:link_candidates`)과 쌍으로 대조해 어긋난 쌍을 센다. 판정이 아니라 보고이므로 종료 0 이고, 이름과 값이 산문으로 떨어져 있으면 쌍이 서지 않는다. 현상 `agt:documentLag`(P18)의 관측 수단이다 |

카탈로그 정합성 검사가 없던 때에 ODD의 동시 에이전트 한도와 카탈로그의 합이 한동안 어긋난 채 지나간 적이 있다.
이 일은 규약만으로는 규칙이 지켜지지 않는다는 증거다.

## 도구 작성 규칙

- 도구는 실패하면 0이 아닌 종료 코드로 끝나고, `FAIL [검사명]` 접두사와 근거 인용을 낸다. 그 메시지가 곧 수정 안내다.
- 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합친다.
- 규약 상수(접미사와 네임스페이스)의 단일 정의 위치는 `tools/kb_lib.py`다.
- 생성기는 검사기다. 생성 실패가 곧 게이트 실패이고, 생성물은 소스 트리에 두지 않는다.
- 검사를 약화하는 변경(삭제나 예외 추가)은 유저의 승인을 받는다.
