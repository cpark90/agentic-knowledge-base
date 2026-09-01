# 산출물 배치 — 이 저장소의 격자

이 저장소의 모든 산출물이 체계의 두 축(plane × level)과 ODD 위에서 어디에
놓이는지를 확정한다. 축의 정의는 노트 0.1절, 사다리는 6.1절
([`id:chunk-d0005`](../chunks/decision/d-0005-abstraction-ladder.md)),
plane은 5.1절 ([`id:chunk-d0003`](../chunks/decision/d-0003-plane-by-verification.md)).

**이 문서가 배치의 원본이다.** 새 산출물을 만들 때 어디에 두는지는 §4 규칙으로
정하고, 격자에 자리가 없으면 그것 자체가 신호다(§3).

## 1. 세 가지 위치

산출물은 셋 중 하나다. 이 구분이 먼저다 — 축 위에 없는 것을 축에 억지로
올리면 분류가 무너진다.

| 위치 | 정의 | 이 저장소의 예 |
|---|---|---|
| **기반** | 축 위에 있지 않다. 다른 것의 위치를 정하는 어휘·제약 | 온톨로지, SHACL shape |
| **경계** | ODD와 그 파생물. 조건의 명세 | `project-odd.ttl`, 스코프 |
| **지식** | plane × level 격자 위에 놓인다 | 청크, 구성체 |

판정·운영 도구는 넷째 부류로, 지식을 **검사하는** executable이다 (§2.4).

## 2. 배치표

### 2.1 기반 — 축 위에 없음 (노트 0.1절)

| 산출물 | 파일 | 성격 |
|---|---|---|
| 온톨로지 (T-Box) | `ontology/project-ontology.ttl` (루트, import만) | 어휘와 공리. 개체 없음 |
| | `ontology/entity/knowledge-item/` 4개 | plane으로 분류 가능한 개념 |
| | `ontology/related/{condition,scope,assumption,channel,harness}/` 9개 | 횡단 개념 |
| 형식화 (shape) | `ontology/shapes/` 5개 | 검사 가능한 제약 |

**functional 수준은 별도 파일이 아니다** (노트 0.2절). "무엇을 하려는가"는
어휘를 서술적으로 쓴 것이며, 이 저장소에서는 각 개념의 `rdfs:label`(한/영)과
`skos:definition`으로 존재한다. 그래서 `-functional` 접미사를 가진 파일이 없다.

### 2.2 경계 — ODD와 파생물

| 산출물 | 파일 | level | 근거 |
|---|---|---|---|
| ODD | `odd/project-odd.ttl` (`id:odd-agentic-knowledge-base`) | concrete | 확정된 경계 (0.2절) |
| 조건 7개 | 같은 파일 (`id:cond-*`) | concrete | 정적 4 · 환경 2 · 동적 1 |
| 스코프 5개 | `kg/catalog-kg.ttl` (`id:scope-*`) | concrete | ODD 속성의 부분집합 (3.4절) |
| 가정 | `kg/base-kg.ttl` (`id:asm-*`) | — | ODD 조건 위의 명제 (0.4절) |

ODD가 concrete인 이유: 검토를 마쳐 **확정된** 경계이기 때문이다. 미확정 경계를
논의하는 단계는 ODD가 아니라 설계 공간이다.

### 2.3 지식 — plane × level 격자

**현재 채워진 칸은 하나다.**

| plane \ level | functional | abstract | logical | **concrete** | executable |
|---|---|---|---|---|---|
| `decision` | — | — | — | **청크 20개** | — |
| `contract` | — | — | — | — | — |
| `schema` | — | — | — | — | — |
| `artifact` | — | — | — | — | (§3 참조) |
| `annotation` | — | — | — | — | — |
| `memory` | — | — | — | — | — |

- **결정 청크 20개** — `chunks/decision/*.md`, 전부 `level: concrete`,
  `state: valid`. 본문은 파일, head는 `kg/chunks-kg.ttl`(생성).
- **구성체 7개** — `kg/composite-kg.ttl`, 전부 concrete. 청크 20개가 모두 어느
  하나의 부분이다(고아 0). 부분의 plane·level은 전체와 같다(동질성, 4.5절).

### 2.4 판정·운영 — executable

| 산출물 | 파일 | 역할 |
|---|---|---|
| 게이트 도구 | `tools/validate.py` | 라벨·모듈 경계·어휘 폐쇄·ODD 참조·SHACL |
| | `tools/chunk_lint.py` | 42줄 상한, 접미사 규약 |
| | `tools/chunk2kg.py` | frontmatter → head 그래프 생성 |
| | `tools/canonicalize.py` | 정규화 직렬화 (2.5절) |
| | `tools/kb_lib.py` | 규약 상수의 단일 정의처 |
| 게이트 배선 | `defs/knowledge.bzl`, 각 `BUILD.bazel` | 데이터 타깃 · 테스트 타깃 |
| 하네스 설정 | `MODULE.bazel`, `.bazelrc`, `tools/requirements_lock.txt` | 재현 가능한 툴체인 |

이들은 지식을 **검사하는** 것이지 지식이 아니다. 격자에 올리려면
`artifact` plane의 executable 청크로 등록해야 하는데, 아직 하지 않았다(§3).

### 2.5 그래프 밖 — 운영 문서

| 위치 | 성격 |
|---|---|
| `docs/*.md` | 설계 문서. 청크 위의 투영이며 결정은 IRI로 인용만 한다 |
| `docs/feedback/` | 유저 소통 채널 (3-lane, hci 담당) |
| `.claude/` | 에이전트 역할 정의와 역할별 메모리 |

어휘 폐쇄·shape 검사의 대상이 아니다. 소통 기록과 지식을 섞지 않는다는 것이
`DESIGN.md` A5다.

## 3. 빈 칸의 해석

빈 칸은 결함이 아니다 — **도입 순서**(노트 Part XII)의 결과다. 다만 어느 것이
"아직"이고 어느 것이 "설계상 비어 있음"인지는 구분한다.

| 빈 칸 | 해석 | 언제 채워지나 |
|---|---|---|
| `decision`의 functional·abstract·logical | **아직.** 결정 청크가 전부 concrete로 바로 저작되었다 — 사다리를 타지 않았다 | Part XII 5단계. `space/`가 자리를 예약하고 있다 |
| `contract`·`schema` 전 행 | **아직.** 이 저장소가 다루는 지식이 아직 설계 판단뿐이다 | 해당 지식이 생길 때 |
| `artifact`의 executable | **미결.** `tools/*.py`가 실체상 여기 속하나 청크로 등록되지 않았다 | §3.1 |
| `annotation` 전 행 | **아직.** vnv 판정 기록이 쌓이면 채워진다 | vnv 역할 실행 시 |
| `memory` 전 행 | **아직.** 승격 규칙(9.4절)이 정해지면 | 실행 기록 누적 후 |

### 3.1 미결 — 도구 코드를 `artifact` 청크로 등록할 것인가

**찬성**: 노트 5.1절이 `artifact` plane의 개발 프로파일 청크를 "함수(42줄 = 함수
하나)"로 정의하고, 판정 도구는 컴파일·테스트·린터다. `tools/*.py`의 각 검사
함수는 그 정의에 정확히 맞는다.

**반대**: 이 코드는 체계가 **관리하는 지식**이 아니라 체계를 **구현하는
하네스**다. 노트 0.4절이 하네스를 지식 항목이 아닌 횡단 개념(`related/harness`)에
둔 것과 같은 이유다. 등록하면 게이트 도구가 자기 자신을 검사 대상으로 삼는다.

**현재 판단**: 등록하지 않는다. 다만 이것은 확정이 아니라 **미결**이며, 다른
프로젝트의 지식을 이 베이스가 관리하기 시작하면(즉 이 저장소가 자기 자신이
아닌 대상을 다루면) 그 프로젝트의 코드는 당연히 `artifact` 청크가 된다. 그때
"하네스 자신의 코드"와 "관리 대상의 코드"가 갈라지므로 판단이 쉬워진다.

## 4. 배치 규칙 — 새 산출물은 어디에

1. **어휘를 정의하는가** → 기반. `ontology/` 아래 주제가 맞는 모듈 디렉토리에
   새 파일 하나. 새 주제면 새 모듈 디렉토리 + `BUILD.bazel` + `//ontology:modules`
   등록. 한/영 라벨과 `skos:definition` 필수.
2. **조건·경계를 명세하는가** → `odd/project-odd.ttl`. 판정 방법과 등급 필수.
   ODD에 없는 조건을 참조하는 것은 만들 수 없다.
3. **지식인가** → plane과 level을 정하고 `chunks/<plane>/`에 파일 하나.
   같은 커밋에서 구성체에 잇는다. plane 배정 기준은 **판정 방식**이다
   (`id:chunk-d0003`) — 저장 위치나 파일 형식이 아니다.
4. **지식이 아니라 개체인가** (가정·역할·스코프·채널·구성체) → `kg/`의 해당
   `-kg.ttl`. 접두사 표는 `STYLEGUIDE.md` §5.
5. **검사·생성 도구인가** → `tools/`, 게이트 배선은 `defs/knowledge.bzl` 매크로로.
6. **위 어디에도 안 맞는가** → 격자에 자리가 없다는 신호다. plane 추가는
   **판정 방식이 기존 어디와도 다를 때만** 가능하고(5.5절), 그 전에 기존 plane의
   하위 클래스로 흡수되는지 먼저 검토한다. 조용히 `docs/`에 두지 않는다.

## 5. 관련 문서

- 저장 구조와 앵커 해석: [`storage-design.md`](storage-design.md)
- 게이트가 무엇을 강제하는가: [`gate-design.md`](gate-design.md)
- 저작 스타일: [`../STYLEGUIDE.md`](../STYLEGUIDE.md)
