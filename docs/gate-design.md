# 게이트 설계 — 무엇을 기계가 강제하고 무엇을 규약에 남기는가

노트 6.7절 검사 게이트와 2.5절 온톨로지 위생을 이 저장소가 어떻게 배선했는지
기록한다. 게이트는 `bazel test //...` 하나로 전부 돌고, 그것이
[`id:chunk-d0001`](../chunks/decision/d-0001-bazel-harness.md)의 근거다.

## 확정 결정

- **G1 — 게이트는 테스트 타깃이다.** 스크립트를 따로 실행하는 방식이 아니다.
  우회하려면 `BUILD.bazel`을 고쳐야 하고, 그건 리뷰에 걸린다.
- **G2 — 실패 메시지가 곧 수정 안내다.** 모든 `FAIL`에 `[검사명]`과 **노트 절
  번호**를 붙인다. 절 번호가 없는 검사는 근거가 없는 검사다.
- **G3 — shape는 강화만 한다.** 제약 완화(`maxCount` 상향, `sh:in` 확장,
  검사 삭제)는 유저 승인 사항이다. 게이트가 틀렸다고 판단되면 게이트를 고치지
  말고 채널에 항목을 남긴다.
- **G4 — 판정 가능한 것만 게이트로.** 기계가 판정할 수 없는 규칙은 게이트에
  넣지 않고 `STYLEGUIDE.md`의 `[지킴]`으로 남긴다. 게이트에 넣을 수 없다는
  사실 자체를 기록한다(§4).

## 검사 목록

### `tools/validate.py` — 그래프 게이트

| 검사 | 무엇을 강제하나 | 근거 |
|---|---|---|
| `syntax` | 모든 TTL이 파싱된다 | 파싱 실패는 그 자체로 게이트 실패 |
| `labels` | `agt:` 용어마다 한/영 `rdfs:label` + `skos:definition` | 2.5절 정의 완전성 |
| `boundary` | 한 용어는 한 모듈 파일에서만 정의된다 | 2.3절 모듈 경계 규칙 |
| `vocab` | 데이터의 술어가 온톨로지 또는 등록된 표준 어휘 안 | 4.4절 일관성 · Part XIII 어휘 우회 |
| `odd-ref` | `agt:refersTo`의 대상이 ODD에 존재한다 | 0.4절 — ODD에 없는 조건을 참조할 수 없다 |
| `shacl` | shape 적합성 (아래 표) | 4.4절 |

`vocab`이 핵심 방어선이다. `agt:` 접두어인데 온톨로지에 없으면 **오타 또는
무단 어휘 생성**이고, 등록되지 않은 네임스페이스면 **어휘 우회**다. 둘을 다른
메시지로 구분해 보고한다.

### SHACL shape — `ontology/shapes/`

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `lineCount` ≤ 42 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `state`가 상태 기계 값 |
| `composite-shapes.ttl` | `agt:Composite` | `hasDirectPart` ≤ 9 (7±2) |
| `condition-shapes.ttl` | `agt:Condition`, `agt:ODD` | 조건마다 `checkMethod` 필수 · 등급 A–D · ODD는 조건 ≥1, `mode` 고정 |
| `assumption-shapes.ttl` | `agt:Assumption` | ODD 조건을 `refersTo` ≥1 · `proposition` 필수 |
| `scope-shapes.ttl` | `agt:Scope` | `mode` 고정 · `subsetOf`로 어느 ODD의 부분집합인지 명시 |

**라벨 제약의 함정** — `sh:languageIn`은 *모든* 값에 적용되므로 "한글 하나 +
영어 하나"를 표현하지 못한다. `sh:qualifiedValueShape` + `sh:qualifiedMinCount`를
써야 한다. 처음에 `languageIn`으로 썼다가 고친 자리다.

### `tools/chunk_lint.py` — 파일 게이트

| 검사 | 대상 | 규칙 |
|---|---|---|
| `chunk` | `--chunks` | 본문 42줄 이하. `.md`는 frontmatter 제외, `.ttl`은 `@prefix`·주석·빈 줄 제외 |
| `naming` | `--ttl` | 파일명이 접미사 규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`)을 따른다 |

**온톨로지도 42줄 규율을 받는다.** `//ontology:chunk_lint_test`가 그것이다 —
한 청크 한 파일이 지식에만 적용되는 규칙이 아니라는 것이 A2다.

### `tools/chunk2kg.py` — 생성 겸 검사

생성기가 곧 검사기다. frontmatter 필수 키 6개, 값 어휘, **IRI 중복**을 보고
어기면 비영 종료하므로 `//kg:chunks_kg` 빌드가 실패한다. IRI 중복 검사가
"한 청크는 한 파일"의 기계적 강제다.

## Bazel 배선

```
//:gate  (test_suite — 아래 전부)
├── //:naming_test              TTL 접미사 규약 (kg·odd·ontology·shapes)
├── //chunks:lint_test          지식 청크 42줄
├── //ontology:chunk_lint_test  온톨로지 청크 42줄
├── //ontology:gate_test        labels · boundary · SHACL
├── //odd:gate_test             ODD shape (조건 판정 방법·등급·mode)
└── //kg:gate_test              vocab · odd-ref · SHACL  ← //kg:chunks_kg 를 입력으로
```

매크로가 배선을 감춘다 (`defs/knowledge.bzl`):

| 매크로 | 하는 일 |
|---|---|
| `kb_gate_test` | `validate.py`를 지정 그래프에 대해 돌리는 `py_test`. `ontology`/`shapes`/`odd`/`data` 인자가 그대로 플래그가 된다 |
| `kb_chunk_lint_test` | `chunk_lint.py`를 `chunks`/`ttl` 대상에 |
| `kb_chunk_kg` | 청크 파일 → head 그래프 `genrule` |

**`py_test`를 직접 쓰지 않는다** (`STYLEGUIDE.md` §6). 게이트 선언이 매크로
하나로 모여 있어야 검사 추가·변경이 한 곳에서 일어난다.

### 캐시가 재판정 경계를 근사한다

입력 해시가 바뀐 타깃만 다시 돈다. 청크 하나를 고치면 `//kg:*`와
`//chunks:lint_test`만 재실행되고 온톨로지 게이트는 캐시에서 나온다. 노트
8.6절이 요구하는 "재판정 경계"의 기계적 근사이며, 진짜 재판정(가정 위반
전파)은 링크 도입 후에 온다.

## 게이트 밖 — 규약으로 남은 것

G4에 따라, 판정 불가능하거나 아직 기계화하지 않은 규칙을 명시한다. **여기
적히지 않은 채 게이트도 없는 규칙은 사실상 없는 규칙이다.**

| 규칙 | 왜 게이트가 아닌가 | 어디에 있나 |
|---|---|---|
| 라벨이 본문을 대표한다 | 판정 불가 (4.4절이 "검사 불가"로 명시). 운용으로 강제 | `STYLEGUIDE.md` §4 |
| 한 청크는 한 주제 | 판정 불가. 42줄과 분할 신호가 대리 지표 | `STYLEGUIDE.md` §0 |
| 결정 청크의 역할 태그(결론·근거·대안) | 기계화 가능하나 미구현 | `STYLEGUIDE.md` §4 |
| 청크가 구성체에 속한다 (고아율) | 기계화 가능하나 미구현 — 링크와 함께 | `AGENTS.md` 워크플로 ① |
| 9.6절 입력 검증 (카탈로그 정합성) | 기계화 가능하나 미구현 | `AGENTS.md` 역할 절 |
| 정규화 직렬화 | `canonicalize.py --check`가 있으나 게이트에 안 걸림 | `STYLEGUIDE.md` §0 |

**미구현 4건이 다음 작업이다.** 특히 9.6절 입력 검증은 없어서 실제로 ODD의
동시 에이전트 한도와 카탈로그의 합이 어긋난 채 지나간 적이 있다 — 규약만으로는
지켜지지 않는다는 증거다.

## 게이트를 늘릴 때

1. 근거가 되는 **노트 절 번호**를 먼저 찾는다. 없으면 그 검사는 아직 근거가
   없다 — 체계에 먼저 넣는다.
2. `validate.py`에 `check_*() -> list[str]` 독립 함수로 추가하고 `main`에서
   합류시킨다. 검사 간 결합을 만들지 않는다.
3. 실패 메시지에 `[검사명]`과 절 번호를 넣는다 (G2).
4. 새 타깃이 필요하면 매크로를 쓴다. 지식 파일이 어느 게이트의 입력도 아니면
   그것이 이 하네스의 고아다 (`STYLEGUIDE.md` §6).
5. 위 "게이트 밖" 표에서 해당 줄을 지운다 — 표가 실제와 어긋나면 안 된다.
