# agentic-knowledge-base

**에이전트가 활용할 수 있는 형태로 지식을 축적하기 위한 온톨로지와, 그것을 쓰는 방법론과
도구를 설계·구현하는 저장소다.**

궁극 목적은 특정 분야에서 사업을 수행하는 업체가 그 분야의 지식을 축적하고, 프로젝트마다
ODD를 정하고, 그 지식 위에서 시스템을 만들고 운용하는 것이다. 여기서 만드는 것은 그 목적을
위한 **코어**다. 분야 온톨로지와 개별 프로젝트의 ODD·지식은 여기서 만들지 않는다.
목적과 대상 지식의 전체 진술은 [`docs/purpose.md`](docs/purpose.md)에 있다.

## 세 산출물

| 산출물 | 무엇 | 문서 | 상태 |
|---|---|---|---|
| **ontology** | 지식의 코어와 분야 프로파일 | [`docs/ontology.md`](docs/ontology.md) | 코어(모듈 파일 26 · plane 7종 · 수준 허용표) · 프로파일 없음 |
| **methodology · method · rules** | 순서 · 방법 · 유효한 구조의 규칙 | [`docs/method.md`](docs/method.md) · [`docs/rules.md`](docs/rules.md) | 규칙은 있음 · 절차는 문서화 진행 중 |
| **tools** | 규칙을 검사하고 방법을 수행하는 도구 | [`docs/tools.md`](docs/tools.md) | 검사·생성 도구 14(온톨로지 검사 3단계 포함) · 실험 1(`label_sample`) · **활용 첫 형태 5**(workset·metrics·impact·handoff·consistency) |

현재 상태와 도입 순서는 [`docs/roadmap.md`](docs/roadmap.md)에 있고, 문서 색인은 아래 "문서" 절이다.

## 저장소 구조

```
kb/ontology/                  # 코어 어휘 (T-Box) — 모듈 = 디렉토리, 개념 = 파일
  project-ontology.ttl     #   최상위. import만 하는 얇은 파일
  entity/knowledge-item/   #   plane 7종 · level · 청크·복합체
  related/                 #   횡단 개념 (조건·스코프·가정·채널·하네스·링크·상태·태그)
  shapes/                  #   SHACL — 규칙의 검사 가능한 형태 (plane×level 수준 허용표 포함)
  proposals/               #   용어 제안 승인 큐 (그래프 밖)
kb/odd/project-odd.yml     # 이 저장소 자신의 운영 조건 (OpenODD, 조건 7개) — TTL·택소노미는 생성물
kg/base-kg.ttl             # A-Box — 가정·출처 문서
kg/catalog-kg.ttl          # A-Box — 에이전트 역할·스코프·채널 (하네스 입력)
kg/composite-kg.ttl        # A-Box — 복합체 (손)
kg/chunks-kg.ttl           # (생성) head 그래프 — frontmatter에서 만든다
kg/references-kg.ttl       # (생성) 인용 링크 — 본문에서 뽑는다
INTENT.md                  # 요구 층 진입 — 궁극 목적·이해관계자·요구 인덱스
kb/dev/requirement/        # 개발 KB — 요구 33건 (EARS, functional)
kb/dev/decision/           # 개발 KB — 결정 188건 (결론·근거·대안 세 청크 복합체; 1건은 deprecated)
kb/vv/                     # V&V KB — vnv 역할만 편집 (아직 비어 있음)
chunks/decision/           # v1 유래 옛 결정 (126 deprecated · 27 유효)
space/                     # 설계 공간 (후보와 제약) — 아직 비어 있음
tools/                     # 검사·생성(validate · chunk_lint · chunk2kg · gen_build · channel_lint …) · 활용(workset · metrics · impact · handoff · consistency)
defs/knowledge.bzl         # 게이트 매크로
docs/                      # 이 체계의 문서 + 설계 노트 v3 (그래프 밖)
docs/feedback/             # 유저 소통 채널 (그래프 밖) — hci 담당
.claude/                   # 에이전트 역할 정의와 역할별 메모리
```

## 명령

```bash
bazel test //...                 # 검사 게이트 전체 (커밋 전 필수)
bazel run //tools:canonicalize -- --write <files>   # 기계 생성 TTL 정규화
```

도구 목록과 각 검사가 무엇을 강제하는지는 [`docs/tools.md`](docs/tools.md)에 있다.

## 이 저장소 자신

코어를 코어 자신에 적용한 **첫 인스턴스**다. 설계 원본은 노트 v3
([`docs/agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md))다. 그
`[확정]`이 요구 33건과 결정 188건(`kb/dev/`)으로 재도출되어 있다. 188건은 v3 145건, v4·v5
델타 37건, 2026-09-11~13 추가 6건의 합이다. deprecated는 청크 129다. `chunks/decision/`의 v1
유래 옛 결정 126건과 대체된 새 결정 1건(`p14-adoption-stages`, 청크 3)이 여기 든다. 출처와 처리
경위는 [`docs/decomposition-audit.md`](docs/decomposition-audit.md)에 있다.

작업 규칙은 [`AGENTS.md`](AGENTS.md)에, 저작 스타일은 [`STYLEGUIDE.md`](STYLEGUIDE.md)에 있다.

## 문서
**그래프 밖**이다. 검사 게이트의 통제 어휘·shape 검사 대상이 아니다. 여기 있는 것은 지식이
아니라 지식을 만드는 체계의 서술이다. 문서는 결정을 **복사하지 않고 인용한다**. 복사하면
이중 관리가 되고, 둘이 어긋나는 순간 어느 쪽이 원본인지 알 수 없어진다.

### 설계 원본

| 문서 | 다루는 것 |
|---|---|
| [`agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md) | **노트 v5** — 이 체계의 설계 원본 (3,470줄, Part 0~XVII + 부록 A~E). `[확정]`은 결정으로 재도출되어 `kb/dev/decision/`에 있다 (v3 145건 + v4·v5 델타 37건 = 182건) |
| [`agentic-knowledge-base-structure.md`](docs/agentic-knowledge-base-structure.md) | **운용 지도** — 노트를 실제 운용 관점에서 재배열한 구조도 |

본문의 `(노트 N.N절)` 인용은 전부 이 노트 **v5**의 절 번호다. 2026-09-10의 v3→v5 동기화에서
Part VII이 신설되어 옛 VII 이후가 한 칸 밀렸다.

### 목적

| 문서 | 다루는 것 |
|---|---|
| [`purpose.md`](docs/purpose.md) | **먼저 읽는다.** 궁극 목적, 대상 지식과 순환, 두 KB, 이 저장소가 만드는 것 |
| [`../INTENT.md`](INTENT.md) | 요구 층 진입 문서 — 이해관계자·관심사·요구 33건 인덱스 (루트) |

### 산출물

| 문서 | 다루는 것 |
|---|---|
| [`ontology.md`](docs/ontology.md) | 코어와 분야 프로파일, 확장 규칙 — 코어 / development / V&V 세 층 |
| [`competency-questions.md`](docs/competency-questions.md) | 온톨로지가 답해야 하는 질문과 현재 답할 수 있는 것 (노트 CQ1~20 대응표 포함) |
| [`rules.md`](docs/rules.md) | 무엇이 유효한 구조인가 — 코어(chunk · 복합체 · plane · traceability · KG) / development / V&V |
| [`method.md`](docs/method.md) | 운용 순서·완료 판정(§0)과 각 단계를 어떻게 하는가 — 코어 12절차 / development 저작 흐름 / V&V 위험 분석~되먹임 |
| [`tools.md`](docs/tools.md) | **게이트 총람(원본)**, 코어 검사·활용 도구 / development / V&V 도구, Bazel 배선, 게이트 밖 규약 |

### 진행과 기록

| 문서 | 다루는 것 |
|---|---|
| [`roadmap.md`](docs/roadmap.md) | 도입 8단계에서의 현재 위치와 다음 산출, 실측 |
| [`risks-and-tensions.md`](docs/risks-and-tensions.md) | 체계가 실패하는 방식과 대응, 서로 당기는 힘의 균형점 |
| [`open-questions.md`](docs/open-questions.md) | 미해결 질문 인덱스 — 노트 Part XVII 30건 + 이 저장소의 관찰 (항목 본문은 `open-questions/`) |
| [`references.md`](docs/references.md) | 어느 구조를 어느 표준에서 가져왔는가 |
| [`glossary.md`](docs/glossary.md) | **용어집** — 산문 한글 용어의 원본(표준 용어·영문·옛 표기·출처) |
| [`decomposition-audit.md`](docs/decomposition-audit.md) | 노트·참조 저장소에서 지식이 어디로 갔는가와 감사의 발견 (상세 이력은 git) |

### 소통 채널

[`feedback/`](docs/feedback/README.md)는 유저 피드백 채널이다. hci 에이전트가 담당하며, 유저와 직접
상세 소통하는 유일한 창구다. 3-lane 구조와 승인 게이트는 그 안의 `README.md`가 원본이다.
세 lane은 유저↔hci, 타 에이전트→hci, hci→조사이고, 승인 게이트의 `status: approved`는 유저만
붙인다. 유저 결정의 원문 기록은 [`feedback/purpose-statement.md`](docs/feedback/purpose-statement.md)와
[`feedback/design-detail-review.md`](docs/feedback/design-detail-review.md)에 있다.

### 다른 문서와의 관계

| 문서 | 위치 | 성격 |
|---|---|---|
| `README.md` | 루트 | 저장소 소개 — 세 산출물·구조·명령 |
| `AGENTS.md` | 루트 | 에이전트 하네스 — 역할·권한·소통·커밋 |
| `STYLEGUIDE.md` | 루트 | 컴포넌트별 저작 스타일 — `[지킴]`/`[권장]` |
| `INTENT.md` | 루트 | 요구 층 진입 — 궁극 목적과 요구 인덱스 |
| `docs/*.md` | 여기 | **체계 자체** — 목적·순서·어휘·규칙·방법·도구 |
