# agentic-knowledge-base

**이 저장소는 에이전트가 활용할 수 있는 형태로 지식을 축적하기 위한 온톨로지를 설계하고 구현한다. 그 온톨로지를 쓰는 방법론과
도구도 함께 설계하고 구현한다.**

이 체계는 한 분야의 업체가 자기 분야의 지식을 확률적 지식 모델로 쌓고, 그 지식으로 프로젝트마다
시스템을 만들 수 있게 하려고 있다.

특정 분야에서 사업을 하는 업체는 그 분야의 지식을 에이전트가 쓸 수 있는 형태로 쌓는다. 쌓은 지식은
확률적 지식 모델, 곧 "지식을 확률 구조적으로 모델링한 결과물"이다. 추적 링크와 결정 후보는 증거에서 계산한
믿음 정도를 갖고, 질의의 답은 그 믿음 정도에서 유도한 분포로 나온다. 그리고 프로젝트마다 ODD를 정하고
이 지식을 바탕으로 시스템을 만들고 운용한다.

여기서 모델은 "학습 기반 방법에서의 주요요소인 모델"을 뜻하지 않는다(유저 2026-10-24). 지식 베이스는 어떤
모델의 학습 데이터가 아니라 그 자체가 확률적 지식 모델이다.

다만 어떤 지식을 확정할지는 믿음 정도가 정하지 않는다. 그 권한은 지식 베이스의 규칙과 게이트에 있다.

이 저장소가 만드는 것은 그 목적을 위한 **코어**다. 분야 온톨로지와 개별 프로젝트의 ODD와 지식은 여기서 만들지 않는다.
목적과 대상 지식의 전체 진술은 [`docs/purpose.md`](docs/purpose.md)에 있다.

## 세 산출물

| 산출물 | 무엇 | 문서 | 상태 |
|---|---|---|---|
| **ontology** | 지식의 코어와 분야 프로파일 | [`docs/ontology.md`](docs/ontology.md) | 지식 종류와 지식 종류별 허용 수준 표를 담은 코어가 있고, `kb/ontology/profile/development/`에 개발 프로파일이 있다. 모듈 목록의 원본은 생성 파일 `kb/ontology/modules.bzl`이다 |
| **methodology · method · rules** | 순서 · 방법 · 유효한 구조의 규칙 | [`docs/method.md`](docs/method.md) · [`docs/rules.md`](docs/rules.md) | 규칙은 있고, 절차는 문서화하고 있다 |
| **tools** | 규칙을 검사하고 방법을 수행하는 도구 | [`docs/tools.md`](docs/tools.md) | 검사 도구와 생성 도구, 실험 도구, 활용 도구가 있다. 실험 도구는 `label_sample`이고, 활용 도구는 workset과 metrics, impact, handoff, consistency 등이다. 목록의 원본은 `tools/BUILD.bazel`이고, 게이트 목록은 `bazel query 'tests(//...)'`가 낸다 |

현재 상태와 도입 단계의 통과 여부는 생성 뷰 `bazel build //kg:metrics`가 낸다. 문서 색인은 아래 "문서" 절에 있다.

## 저장소 구조

```
kb/ontology/                  # 코어 어휘 (T-Box) — 모듈 = 디렉토리, 개념 = 파일
  project-ontology.ttl     #   최상위. import만 하는 얇은 파일
  entity/knowledge-item/   #   지식 종류(plane) · 정제 수준(level) · 청크·복합체
  profile/development/     #   개발 프로파일
  related/                 #   횡단 개념 (조건·스코프·가정·채널·하네스·링크·상태·태그·결함·서비스 층·신뢰 등급)
  shapes/                  #   SHACL — 규칙의 검사 가능한 형태 (plane×level 수준 허용표 포함)
  proposals/               #   용어 제안 승인 큐 (그래프 밖)
kb/odd/project-odd.yml     # 이 저장소 자신의 운영 조건 (OpenODD) — TTL·택소노미는 생성물
kg/base-kg.ttl             # A-Box — 가정·출처 문서
kg/catalog-kg.ttl          # A-Box — 에이전트 역할·스코프·채널 (하네스 입력)
kg/composite-kg.ttl        # A-Box — 복합체 (손)
kg/chunks-kg.ttl           # (생성) head 그래프 — frontmatter에서 만든다
kg/references-kg.ttl       # (생성) 인용 링크 — 본문에서 뽑는다
INTENT.md                  # 요구의 진입 문서 — 궁극 목적·이해관계자·요구 인덱스
kb/dev/requirement/        # 개발 KB — 요구 (EARS, functional)
kb/dev/decision/           # 개발 KB — 결정 (결론·근거·대안 세 청크 복합체)
kb/dev/{contract,artifact,memory,norm}/  # 개발 KB — 나머지 지식 종류
kb/vv/                     # V&V KB — vnv 역할만 편집
space/                     # 설계 공간 (후보와 제약)
tools/                     # 검사·생성(validate · chunk_lint · chunk2kg · gen_build · channel_lint …) · 활용(workset · metrics · impact · handoff · consistency)
defs/kb.bzl                # 값 어휘(PLANES·LEVELS·STATES)와 게이트 등록부의 원본
defs/knowledge.bzl         # 게이트 매크로
docs/                      # 이 체계의 문서 + 설계 노트 v5 (그래프 밖)
harness/                   # 에이전트 하네스 (그래프 밖) — 프로토콜·역할 지침·채널·질문지·스크립트
.claude/                   # 생성된 skill과 역할별 메모리
```

## 명령

```bash
bazel test //...                 # 검사 게이트 전체 (커밋 전 필수)
bazel run //tools:canonicalize -- --write <files>   # 기계 생성 TTL 정규화
```

도구 목록과 각 검사가 무엇을 강제하는지는 [`docs/tools.md`](docs/tools.md)에 있다.

## 이 저장소 자신

이 저장소는 코어를 코어 자신에 적용한 **첫 인스턴스**다. 설계 원본은 노트 v5인
[`docs/agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md)다. 노트의
`[확정]`은 `kb/dev/`의 요구와 결정으로 재도출되어 있다.

작업 규칙은 [`AGENTS.md`](AGENTS.md)에, 저작 스타일은 [`STYLEGUIDE.md`](STYLEGUIDE.md)에 있다.

## 문서
문서는 지식이 아니라 지식을 만드는 체계의 서술이므로 **그래프 밖**이다. 그래서 검사 게이트의 통제 어휘 검사와 shape 검사
대상이 아니다. 문서는 결정을 **복사하지 않고 인용한다**. 복사하면
이중 관리가 되고, 둘이 어긋나는 순간 어느 쪽이 원본인지 알 수 없어지기 때문이다.

### 설계 원본

| 문서 | 다루는 것 |
|---|---|
| [`agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md) | **노트 v5**다. 이 체계의 설계 원본이고, Part 0~XVII과 부록 A~E로 이루어진다. `[확정]`은 결정으로 재도출되어 `kb/dev/decision/`에 있다 |
| [`agentic-knowledge-base-structure.md`](docs/agentic-knowledge-base-structure.md) | **운용 지도**다. 노트를 실제 운용 관점에서 재배열한 구조도다 |

본문의 `(노트 N.N절)` 인용은 전부 이 노트 **v5**의 절 번호다. 2026-09-10에 v3을 v5로 동기화할 때
Part VII이 신설되어, 옛 VII 이후의 번호가 한 칸씩 밀렸다.

### 목적

| 문서 | 다루는 것 |
|---|---|
| [`purpose.md`](docs/purpose.md) | **먼저 읽는다.** 궁극 목적, 대상 지식과 순환, 두 KB, 이 저장소가 만드는 것 |
| [`../INTENT.md`](INTENT.md) | 루트에 있는 요구의 진입 문서다. 이해관계자와 관심사, 요구의 색인을 담는다 |

### 산출물

| 문서 | 다루는 것 |
|---|---|
| [`ontology.md`](docs/ontology.md) | 코어와 분야 프로파일, 확장 규칙을 코어와 development, V&V 세 부분으로 다룬다 |
| [`competency-questions.md`](docs/competency-questions.md) | 온톨로지가 답해야 하는 질문과 현재 답할 수 있는 것을 다루고, 노트 CQ1~20의 대응표를 담는다 |
| [`rules.md`](docs/rules.md) | 무엇이 유효한 구조인가를 코어와 development, V&V로 나누어 다룬다. 코어 부분은 chunk와 복합체, plane, traceability, KG를 다룬다 |
| [`method.md`](docs/method.md) | §0의 운용 순서와 완료 판정, 그리고 각 단계를 어떻게 하는가를 다룬다. 단계는 코어 절차와 development 저작 흐름, V&V의 위험 분석에서 되먹임까지다 |
| [`tools.md`](docs/tools.md) | **게이트 총람의 원본**이다. 코어의 검사 도구와 활용 도구, development와 V&V의 도구, Bazel 배선, 게이트 밖 규약을 다룬다 |

### 진행과 기록

| 문서 | 다루는 것 |
|---|---|
| [`risks-and-tensions.md`](docs/risks-and-tensions.md) | 체계가 실패하는 방식과 대응, 서로 당기는 힘의 균형점 |
| [`references.md`](docs/references.md) | 어느 구조를 어느 표준에서 가져왔는가 |
| [`glossary.md`](docs/glossary.md) | **용어집**이다. 산문 한글 용어의 원본이고, 표준 용어와 영문, 옛 표기, 출처를 담는다 |

미결 목록은 생성 뷰 `bazel build //kg:open`이 내고, 미결 하나의 상세는 설계 공간 `space/*-space.md`에 있다.

### 소통 채널

소통은 [`harness/`](harness/README.md)의 두 채널로 한다. 유저 채널인 `harness/user/`는 hci가 쓰는
파일 질문지이고, hci 에이전트가 유저와 직접 상세 소통하는 유일한 창구다. 에이전트
채널인 `harness/channel/`에는 hci와 orchestrator가 주고받는 번호 메시지가 있다. 반영 허가 신호는 유저가
질문지에 적은 답과 `status: answered` 태깅이다. 프로토콜의 원본은 `harness/README.md`다.
2026-10-03 이전의 유저 결정 원문은 [`purpose-statement.md`](harness/user/archive/legacy/purpose-statement.md)와
[`design-detail-review.md`](harness/user/archive/legacy/design-detail-review.md)에 있다.

### 다른 문서와의 관계

| 문서 | 위치 | 성격 |
|---|---|---|
| `README.md` | 루트 | 저장소 소개다. 세 산출물과 구조, 명령을 다룬다 |
| `AGENTS.md` | 루트 | 에이전트 하네스다. 역할과 권한, 소통, 커밋을 다룬다 |
| `STYLEGUIDE.md` | 루트 | 컴포넌트별 저작 스타일이고, 규칙마다 `[지킴]`이나 `[권장]`을 붙인다 |
| `INTENT.md` | 루트 | 요구의 진입 문서다. 궁극 목적과 요구의 색인을 담는다 |
| `docs/*.md` | 여기 | **체계 자체**를 다룬다. 목적과 순서, 어휘, 규칙, 방법, 도구가 그 내용이다 |
