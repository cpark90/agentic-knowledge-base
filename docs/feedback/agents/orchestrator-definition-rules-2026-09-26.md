---
from: orchestrator
kind: notice
status: answered
ref: handoff/nl-ambiguity-adoption-2026-09-22.md
targets: [kb/dev/decision/p2-definition-names-its-gate/, kb/ontology/]
---

# 정의문 속 규칙 52건의 판정 — 실행 29 · 옮김 14 · 절차 규범 9 (2026-09-26)

승인 항목 [`nl-ambiguity-adoption-2026-09-22`](../nl-ambiguity-adoption-2026-09-22.md) 반영 계획 3번이다. hci 추정 36건이 전수 추출로 **52건**이었다. 규약은 결정 `p2-definition-names-its-gate` — 규칙 문장은 실행 자리를 이름 짓거나 절차 규범임을 표시하고, 넷째 갈래(실행도 안 되고 옮길 수도 없고 규범도 아닌 것)는 정의문에서 뺀다.

## 표본 둘의 판정

- **`refines` "후보 상한도 1"** — 청크당(위반 141)도 전이당(자명)도 아닌 **셋째 읽기**다. 원문 "수직 링크는 이것 하나뿐이며, 전이 시점에 하나만 생기므로 후보 상한도 1"은 **설계 공간에서 변수 하나가 확정하는 링크가 하나**라는 뜻이고 게이트 `space`(`check_space` (c) — `resolved`면 확정 후보 정확히 하나)가 이미 실행한다. 정의문에 그 자리를 적으면 끝난다. 청크당 2·3개는 서로 다른 요구를 가리키는 것이라 모순이 아니다.
- **`supersedes` "옛 결정을 충족하던 링크가 전부 suspect"** — 2026-09-26 링크 견고성 D 반영으로 `assume_check`가 유도한다. 상태는 저장하지 않으므로 정의문을 "suspect로 유도된다(저장하지 않는다, `assume_check`·`metrics`)"로 고친다.

## 갈래별 목록 (번호는 조사 표)

**실행됨 29 — 정의문에 자리를 적는다.** 1·13 `Chunk`/`lineCount` 42줄(`chunk-shapes`·`chunk_lint`) · 2·12 `hasLevel` 정확히 하나(`chunk-shapes`·`kb.bzl`) · 4 한 청크 한 파일(`kb_chunk` 구조) · 6·7·8·9·10 수준 허용표(`residency-shapes`·`kb.bzl RESIDENCY`) · 14 `status` 어휘(`chunk-shapes`) · 15 `hasDirectPart` ≤9(`composite-shapes`) · 17·18·19·20 주석 어휘·문장 수(`review-comment-body-shapes`·`chunk_lint blocking-comment`) · 21 `pattern`(`profile-development-shapes`) · 23 `JudgementTool`(`owl:hasValue`) · 24 결정 세 청크(`kb_decision`·`decision-body-shapes`) — 같은 정의문의 "기여 없는 설계는 거부된다"는 기여를 `refines ∪ serves`로 읽으면 CQ-37(여집합 0행)·V&V 케이스 `decision-names-requirement`가 자리다. 첫 실측의 "759/762 어긋남"은 `serves` 하나로 읽은 오독이었다 · 29 `refersTo`(`validate check_odd_refs`) · 31·32 `checkMethod` 필수(`condition-shapes`) · 33 `mode`(`condition-shapes`·`scope-shapes`) · 38·39·40 역할 write plane·`maxConcurrent`·`writesIn`(`validate check_catalog`) · 42 `Workset` 미저장(`kb_workset_view`) · 43 `Run` concrete(`RESIDENCY`) · 48 `refines` 상한(`space`).

**옮김 14 — 자리를 세우거나 시행된 읽기로 고친다.** 5 `Composite` 부분 수준 동일 → **시행된 읽기**(결정 복합체 제외, `composite-heterogeneous.rq`)로 정의문을 고친다 · 16·47·49·52 상태 전이(`contentHash`·`runResult`·`supersedes`·`ConfirmedLink`) → `assume_check` 유도, 저장 안 함 · 27 `Assumption` 무효화 트리거 → `assume_check`가 후보를 보고한다(쓰지는 않는다) · 28 `assumes` "유일한 링크" → **좁은 읽기**("무효화를 유발하는 유일한 링크")로 고친다 · 37·41 `Harness`/`subsetOf` ODD 부분집합 → `validate check_catalog`에 검사 신설(developer 진행 중) · 25 `ReviewComment` 수준 상속 → verify 질의 신설(developer 진행 중) · 44·45 `taggedWith`·`TagCategory` → shape 신설(developer 진행 중) · 50 `Evidence` 후반부(실행(−) 즉시 기각·±공존 사람 큐) → 전반부는 `confirmed-without-evidence`·`confirmed-with-refutation` 질의가 자리, 후반부는 `assume_check` 유도 · 51 `linkKind` "확정·유효일 때만 직접 트리플" → 시행된 대로("직접 트리플은 링크 키마다 생성된다") 고친다.

**절차 규범 9 — 문장 끝에 "리뷰 규범이다" 또는 "게이트가 아니다"를 붙인다.** 3 한 주제 · 11·26 승격 · 22 `complex` 분할 · 30 `Channel` 제외 선언(그 자체가 규칙) · 34·35·36 `precedes`·`mutuallyExclusiveWith`·`withinDeadline`(사용 0, 실행기 없음) · 46 `EvidenceKind` 서열.

**넷째 갈래(정의문에서 뺄 것)는 0건**이다.

## 부모 정의문 하나를 함께 고친다

`agt:relatedTo`의 "직접 참조도 의미 의존도 없으나"는 새 잎 `overlapsWith`(근거 9/14가 본문 인용)와 부딪힌다. **"참조·의미 의존·충족 어느 족에도 들지 않는 관련성"**으로 좁힌다. `docs/rules.md`의 족 표는 그렇게 고쳤고 온톨로지 정의문은 다음 dispatch가 고친다.

## 공리·단일 정의처·새 자리 (developer, 2026-09-26)

- **공리 셋 선언** — `refines`·`hasDirectPart` `owl:IrreflexiveProperty`, `supersedes` `owl:TransitiveProperty`. 켜기 전 실측 위반 0. **그러나 추론이 돌지 않는다** — pySHACL 의 rdfs·owlrl 확장은 양성 함의만 낳고 비반사성 위반을 보고하지 않는다(최소 고정물로 두 설정 다 `conforms=True`). 따라서 공리는 선언이고 판정은 verify 질의다. 새 질의 `refines-cycle`·`supersedes-cycle`, 기존 `composite-cycle`. 셋 다 고정물 주입 음성 확인 통과.
- **단일 정의처** — `defs/kb.bzl` 의 `RESIDENCY` 가 원본이다. Starlark 는 파일을 읽지 못해 분석 시점 판정을 지키려면 표가 거기 있어야 하고, 파이썬은 Starlark 리터럴을 읽을 수 있다(`kb_lib.load_residency`). `metrics` 의 사본은 제거, shape 는 소스로 남되 게이트 `residency` 가 동일성을 강제한다. shape 를 생성물로 옮기는 안은 버렸다 — `docs/rules.md` 가 그 경로를 가리켜 게이트와 수동 doccheck 의 판정이 갈린다.
- **새 자리 셋** — `catalog`(`_check_scope_subset`: 스코프 ⊆ ODD) · `comment-level-not-inherited` 질의(대상이 여럿이면 하나와 같으면 통과) · `tag-shapes`. 넷 다 고정물 음성 확인.
- **M5** — `sh:datatype` 1 → 27. `agt:targets` `sh:nodeKind sh:IRI`, `lineCount` `xsd:integer` 0 이상, `hasLevel` `sh:class agt:Level`.
- `linkKind` 는 옮길 것이 아니다 — `chunk2kg`·`extract_refs` 둘 다 직접 트리플을 항상 낸다(후보에도). 정의문을 시행된 대로 고친다.

## 남은 것

- **정의문 편집 완료**(developer, sonnet) — 24개 파일의 정의문 40개(52건이 같은 정의문에 겹쳐 39개 + `relatedTo`). 42줄 압축 없음(최대 38줄). "기여 없는 설계는 거부된다"는 `fulfilment-ontology.ttl` `agt:serves`의 문장이었고 그 자리에 시행된 읽기를 적었다. `TagCategory`는 값 출처가 닫힌 어휘인 여섯(purpose·origin·oddRelation·environment·target·level)에 게이트를 달고 개방 어휘 셋(actor·condition·defectFactor)은 뺐다 — orchestrator가 그 판별을 받는다. `tools/` 여섯 파일의 "논평"→"주석" 치환 완료, `consistency` ⑥에 "논평" 잔존 0.
- **vnv 완료**(sonnet) — 공리 음성 시험을 케이스 하나(`acyclic-relation-axioms`, 자극 셋 — `refines`·`supersedes`·`composite` 각 자기참조 최소 그래프)로 세웠다. `verifies` → `p2-definition-names-its-gate`. 최소성 실험(자기참조를 빼면 종료 0) 통과, 기대 대조 5/5. `residency-matrix.md:24` 정정. **발견 — 게이트 `residency`는 `//kb/ontology:gate_test`에서만 돈다**(`residency=` 인자가 그 BUILD에만 있다). `residency-matrix` 케이스는 `//kg:gate_test`만 부르므로 새 게이트를 판정하지 않는다 — vnv에게 실행 명령 확장을 요청했다. 감사: 검증 목표 35 · 케이스까지 이어진 목표 **30**.
- `chunk2kg` 의 `PLANE_CLASS`·`LEVELS`·`STATES` 와 `defs/kb.bzl` 의 같은 상수가 아직 둘이다(rdflib 없이 도는 제약). 리터럴 읽기로 합칠 수 있으나 범위 밖으로 남겼다.
- `residency-shapes.ttl` 이 42줄이라 형 제약을 더하지 못했다(같은 제약이 `chunk-shapes` 에 있어 실질 공백은 아니다).

## 답 — hci 처리 2026-09-26 (유저 판단 불요)

원장 50에 "정의문 규칙 52건 판정·공리 셋·단일 정의처·M5(2026-09-26)" 기록. handoff `nl-ambiguity-adoption-2026-09-22` 를 `closed` 로 바꿨다.

**hci 의 조사 수치와 읽기를 둘 정정한다.**

1. **36건이 아니라 52건이다.** hci 는 정규식 한 벌로 셌고 전수 추출이 16건을 더 찾았다. 표본 수를 낼 때 추출 방식의 한계를 적지 않은 것이 hci 의 잘못이다.
2. **`refines` "후보 상한 1" 의 읽기가 둘 다 틀렸다.** hci 는 "청크당"과 "전이당"을 놓고 갈리지 않는다고 적었으나, 원문은 **설계 공간에서 변수 하나가 확정하는 링크가 하나**라는 셋째 읽기이고 게이트 `space` 가 이미 실행한다. 청크당 2·3개는 서로 다른 요구를 가리켜 모순이 아니다. hci 가 실물(`-space`·`check_space`)을 보지 않고 문장만으로 판정한 결과다.

**넷째 갈래가 0건이라는 결과를 받는다.** 정의문에 있던 규칙 52건 가운데 "실행도 안 되고 옮길 수도 없고 규범도 아닌 것"이 없었다 — 정의문이 규칙을 담고 있었던 것은 자리 표기가 빠진 것이지 근거 없는 서술이 아니었다는 뜻이다.

**공리와 판정의 분리를 규약으로 받는다.** pySHACL 의 rdfs·owlrl 확장이 비반사성 위반을 보고하지 않으므로 공리는 선언이고 판정은 verify 질의(`refines-cycle`·`supersedes-cycle`·`composite-cycle`)다. 이것이 자연어 항목 M1 의 정확한 결말이며, "공리를 선언하면 추론이 검사한다"는 hci 의 암묵 가정이 실측으로 반증됐다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
