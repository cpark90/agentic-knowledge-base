# agentic-knowledge-base

**에이전트가 활용할 수 있는 형태로 지식을 축적하기 위한 온톨로지와, 그것을 쓰는 방법론과
도구를 설계·구현하는 저장소.**

특정 분야에서 사업을 수행하는 업체가 그 분야의 지식을 축적하고, 프로젝트마다 ODD를 정하고,
그 지식 위에서 시스템을 만들고 운용한다 — 이것이 궁극 목적이고, 여기서 만드는 것은 그
목적을 위한 **골격**이다. 분야 온톨로지와 개별 프로젝트의 ODD·지식은 여기서 만들지 않는다.
목적과 대상 지식의 전체 진술은 [`docs/purpose.md`](docs/purpose.md).

## 세 산출물

| 산출물 | 무엇 | 문서 | 상태 |
|---|---|---|---|
| **ontology** | 지식의 골격과 분야 프로파일 | [`docs/ontology.md`](docs/ontology.md) | 골격(모듈 파일 26 · plane 7종 · 상주표) · 프로파일 없음 |
| **methodology · method · rules** | 순서 · 방법 · 유효한 구조의 규칙 | [`docs/methodology.md`](docs/methodology.md) · [`docs/method.md`](docs/method.md) · [`docs/rules.md`](docs/rules.md) | 규칙은 있음 · 절차는 문서화 진행 중 |
| **tools** | 규칙을 검사하고 방법을 수행하는 도구 | [`docs/tools.md`](docs/tools.md) | 검사·생성 6개(3계층 컴파일러) · **활용 도구 0개** |

현재 상태와 도입 순서는 [`docs/roadmap.md`](docs/roadmap.md), 문서 색인은
[`docs/README.md`](docs/README.md).

## 저장소 구조

```
ontology/                  # 골격 어휘 (T-Box) — 모듈 = 디렉토리, 개념 = 파일
  project-ontology.ttl     #   최상위. import만 하는 얇은 파일
  entity/knowledge-item/   #   plane 7종 · level · 청크·구성체
  related/                 #   횡단 개념 (조건·스코프·가정·채널·하네스·링크·상태·태그)
  shapes/                  #   SHACL — 규칙의 검사 가능한 형태 (plane×level 상주표 포함)
  proposals/               #   용어 제안 승인 큐 (그래프 밖)
odd/project-odd.ttl        # 이 저장소 자신의 운영 조건 (조건 7개)
kg/base-kg.ttl             # A-Box — 가정·출처 문서
kg/catalog-kg.ttl          # A-Box — 에이전트 역할·스코프·채널 (하네스 입력)
kg/composite-kg.ttl        # A-Box — 구성체 (손)
kg/chunks-kg.ttl           # (생성) head 그래프 — frontmatter에서 만든다
kg/references-kg.ttl       # (생성) 인용 링크 — 본문에서 뽑는다
intent.md                  # 요구 층 진입 — 궁극 목적·이해관계자·요구 인덱스
kb/dev/requirement/        # 개발 KB — 요구 33건 (EARS, functional)
kb/dev/decision/           # 개발 KB — 결정 182건 (결론·근거·대안 세 청크 구성체)
kb/vv/                     # V&V KB — vnv 역할만 편집 (아직 비어 있음)
chunks/decision/           # v1 유래 옛 결정 (126 deprecated · 27 유효)
space/                     # 설계 공간 (후보와 제약) — 아직 비어 있음
tools/                     # validate · chunk_lint · chunk2kg · extract_refs · canonicalize · term_propose
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

도구 목록과 각 검사가 무엇을 강제하는지는 [`docs/tools.md`](docs/tools.md).

## 이 저장소 자신

골격을 골격 자신에 적용한 **첫 인스턴스**다. 설계 원본은 노트 v3
([`docs/agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md))이고, 그
`[확정]`이 요구 33건과 결정 182건(`kb/dev/`)으로 재도출되어 있다 (v3 145 + v4·v5 델타 37). `chunks/decision/`의
옛 결정은 v1 유래로 126건이 deprecated다. 출처와 처리 경위는
[`docs/decomposition-audit.md`](docs/decomposition-audit.md).

작업 규칙은 [`AGENTS.md`](AGENTS.md), 저작 스타일은 [`STYLEGUIDE.md`](STYLEGUIDE.md).
