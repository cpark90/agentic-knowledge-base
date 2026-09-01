# agentic-knowledge-base

**에이전트 지식 관리 체계**의 인스턴스이자 그 체계 자신의 명세를 담는 저장소.
정리된 지식(온톨로지·ODD·지식그래프·청크)을 보관하고, 그 지식을 체계의
방법론대로 활용하기 위한 도구(검사 게이트·정규화·린트)를 함께 담는다.
체계의 규칙은 결정 청크에, 설계 근거는 [`docs/`](docs/README.md)에 있다.

**모든 지식은 파일·디렉토리 기반 청크다** — 한 청크는 한 파일, 모듈은
디렉토리. 온톨로지도 마찬가지다. **하네스는 Bazel이다** — 파일·디렉토리로
구조화된 자료를 정리·활용하기에 가장 적합한 도구이기 때문이다. 지식 산출물은
데이터 타깃, 검사 게이트(노트 6.7절)는 테스트 타깃이다. `bazel test //...`
한 번이 게이트 전체 실행이고, 입력 해시 기반 캐시가 "바뀐 지식만 재검사"를
보장한다.

에이전트 하네스 운영 규칙은 `AGENTS.md`, 컴포넌트별 작성 스타일은
`STYLEGUIDE.md`, **설계 근거는 [`docs/`](docs/README.md)** 가 원본이다 —
"왜 이 구조인가"는 [`docs/DESIGN.md`](docs/DESIGN.md)부터 읽는다.

## 구조

```
ontology/                  # T-Box — 어휘와 공리 (*-ontology), 모듈 구조는 노트 2.3절
  project-ontology.ttl     #   최상위. import만 하는 얇은 파일
  entity/                  #   plane으로 분류 가능한 개념 (청크·구성체·level)
  related/                 #   횡단 개념 (조건·스코프·가정·채널·하네스)
  shapes/                  #   SHACL shape (*-shapes) — 4.4절 청크 규칙 등
odd/project-odd.ttl        # 이 프로젝트의 운영 설계 영역 (Part III)
kg/base-kg.ttl             # A-Box — 청크가 아닌 개체 (가정·출처 문서)
kg/catalog-kg.ttl          # A-Box — 에이전트 카탈로그 (하네스·역할·스코프·채널, 9.2절)
kg/composite-kg.ttl        # A-Box — 구성체: 청크의 묶음 (4.5절, 부분 ≤ 9)
kg/chunks-kg.ttl           # (생성) 청크 head 그래프 — frontmatter에서 생성 (4.3절)
chunks/<plane>/*.md        # 청크. 한 청크 = 한 파일: frontmatter(head) + 본문 ≤ 42줄
space/                     # 설계 공간 (*-space, Part VII) — 5단계에서 채움
docs/*.md                  # 설계 문서 (그래프 밖) — DESIGN · artifact-placement · storage · gate
docs/feedback/             # 유저 피드백 채널 (그래프 밖) — hci agent 담당, 규약은 그 안 README.md
.claude/agents/            # 에이전트 역할 정의 (hci 등), agent-memory/ 는 역할별 메모리
tools/                     # 판정 도구: validate(게이트) · chunk_lint · chunk2kg · canonicalize
defs/knowledge.bzl         # kb_gate_test · kb_chunk_kg · kb_chunk_lint_test 매크로
```

## 명령

```bash
bazel test //...                 # 검사 게이트 전체 (커밋 전 필수)
bazel test //:gate               # 같은 것 (test_suite)

# 게이트를 손으로 돌릴 때
bazel run //tools:validate -- --ontology <files> --shapes <files> --odd <files> --data <files>
bazel run //tools:chunk_lint -- --chunks <files> --ttl <files>

# 정규화 직렬화 (노트 2.5절) — 기계 생성 TTL을 커밋 전에 정규형으로
bazel run //tools:canonicalize -- --write <files>

# 파이썬 의존성 재고정
tools/relock.sh
```

## 게이트가 검사하는 것

| 검사 | 내용 | 근거 |
|---|---|---|
| syntax | 모든 TTL 파싱 | — |
| labels | agt: 용어에 한/영 라벨 + 정의 | 2.5절 정의 완전성 |
| boundary | 용어는 한 모듈에서만 정의 | 2.3절 경계 규칙 |
| vocab | 데이터의 술어는 온톨로지 안 | 4.4절 일관성, 어휘 우회 방지 |
| odd-ref | 가정·스코프는 ODD 조건만 참조 | 0.4절 |
| shacl | 청크 42줄·라벨·상태, 조건 판정 방법, 구성체 7±2 등 | 4.4절, 3.2절, 4.5절 |
| chunk lint | 본문 파일 42줄 이하 | 4.1절 |
| naming | TTL 접미사 규약 | 0.2절 |

## 현재 담긴 지식

| 산출물 | 수 | 내용 |
|---|---|---|
| 결정 청크 (`chunks/decision/`) | 153 | d-0001 이 저장소의 하네스 채택 / d-0002~d-0012·d-0021~d-0155 **체계 전체**(명명 규약·문제 진술·온톨로지·ODD·청크·plane·사다리·미확정·링크·입력·활용·UX) / d-0013~d-0020·d-0156~d-0185 참조 저장소에서 승격(연합·저작 규율·재현 가능 빌드·선택 정책·검증 가능한 명세) |
| 구성체 (`kg/composite-kg.ttl`) | 38 | 체계의 각 Part별 묶음 + 승격 주제별 묶음 — **모든 청크가 어느 구성체의 부분이다(고아 0)** |
| 온톨로지 청크 (`ontology/**`) | 13 + 루트 | `entity/knowledge-item` 4 + `related/`(condition 3·scope 1·assumption 1·channel 1·harness 3), 그리고 import만 하는 `project-ontology.ttl` |
| SHACL shape | 5 | 청크 · 구성체 · 조건/ODD · 가정 · 스코프 |
| ODD 조건 | 7 | 정적 4 · 환경 2 · 동적 1 (전부 판정 방법·등급 포함) |
| 카탈로그 | 하네스 1 · 역할 5 · 스코프 5 · 채널 1 | `kg/catalog-kg.ttl` — `AGENTS.md` 역할 표의 형식 원본 |

d-0021~d-0155는 이 체계의 설계 노트(2476줄)를 **체계 자신의 규칙에 따라 분해한**
결과다. 절별 대응은 [`docs/decomposition-audit.md`](docs/decomposition-audit.md).
d-0013~d-0020·d-0156~d-0163·d-0176~d-0185는 참조 저장소에서 **승격**된 지식이다.
분해는 원본을 제거했지만 승격은 원본을 남긴다 — 그쪽은 계속 쓰이는 운영
문서이고, 일반 원칙만 가져오면서 이송 표기를 남겼기 때문이다.

## 도입 단계 (노트 Part XII)

- **1단계 (청크와 plane)** — **완료.** 온톨로지 `entity/` 최소본, 한 청크 한 파일,
  42줄 게이트, 라벨·어휘 폐쇄 검사.
- **2단계 (ODD와 스코프)** — **완료.** `project-odd.ttl`(조건 7개, 전부 판정 방법
  보유), 에이전트 카탈로그(역할 5), 역할별 스코프 5, 소통 채널.
- **다음** — 9.6절 입력 검증을 게이트로 (역할별 read plane 최소 1, 설계/구현/운영이
  같은 write plane을 공유하지 않음, `maxConcurrent` 합이 ODD 동적 요소 안). 지금은
  규약으로만 지켜지고 기계가 검사하지 않는다.
- **3단계 이후** (링크·가정 전파·사다리 완성)는 `related/trace` 모듈 추가와 함께.

## 청크 형식 — 한 청크는 한 파일

청크의 모든 것이 파일 하나에 있다: head 메타데이터는 frontmatter, 본문은
그 아래(≤42줄). `-kg`의 head 그래프는 손으로 쓰지 않고 `//kg:chunks_kg`가
frontmatter에서 생성하므로 `lineCount`·`assertionLocation`이 어긋날 수 없다.

```markdown
---
iri: https://agentic-knowledge-base.dev/id/chunk-d0001
plane: decision            # decision|contract|schema|artifact|annotation|memory
level: concrete            # functional|abstract|logical|concrete|executable
label_ko: Bazel 하네스 채택
label_en: Adopt Bazel harness
state: valid               # draft|valid|suspect|invalidated|deprecated
assumes: [<가정 IRI>]      # 선택
derived_from: [<출처 IRI>] # 선택
---
본문 (42줄 이하)
```

## 참조 저장소 — 내용 활용, 직접 의존 없음

참조 저장소들은 이 체계의 추상화 사다리로 재배치되었다:
`../harness-functional`(구 harness_ontology — 하네스의 **ODD + functional**
수준: 어휘 TBox·shapes)과 `../harness-concrete`(구 harness-recipes —
하네스의 **logical + concrete** 수준: union root·부품 라이브러리·조립 명세).
둘 다 **내용의 원천**일 뿐 빌드에 연결하지 않으며, 필요한 지식을 `agt:`
어휘의 청크로 승격해 가져오고 출처를 `prov:wasDerivedFrom`으로 남긴다
(출처 개체는 `kg/base-kg.ttl`의 `id:doc-harness-ontology`,
`id:doc-harness-recipes` — 지속 IRI라 개명 전 이름 유지). 일반 방법론은
이미 청크 d-0013~d-0020으로 이송되었다.
