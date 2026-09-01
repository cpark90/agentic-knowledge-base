# agentic-knowledge-base

에이전트 지식 관리 체계(`agent-knowledge-system-notes.md`)의 인스턴스.
정리된 지식(온톨로지·ODD·지식그래프·청크)을 보관하고, 그 지식을 체계의
방법론대로 활용하기 위한 도구(검사 게이트·정규화·린트)를 함께 담는다.

**모든 지식은 파일·디렉토리 기반 청크다** — 한 청크는 한 파일, 모듈은
디렉토리. 온톨로지도 마찬가지다. **하네스는 Bazel이다** — 파일·디렉토리로
구조화된 자료를 정리·활용하기에 가장 적합한 도구이기 때문이다. 지식 산출물은
데이터 타깃, 검사 게이트(노트 6.7절)는 테스트 타깃이다. `bazel test //...`
한 번이 게이트 전체 실행이고, 입력 해시 기반 캐시가 "바뀐 지식만 재검사"를
보장한다.

에이전트 하네스 운영 규칙은 `AGENTS.md`, 컴포넌트별 작성 스타일은
`STYLEGUIDE.md`가 원본이다.

## 구조

```
ontology/                  # T-Box — 어휘와 공리 (*-ontology), 모듈 구조는 노트 2.3절
  project-ontology.ttl     #   최상위. import만 하는 얇은 파일
  entity/                  #   plane으로 분류 가능한 개념 (청크·구성체·level)
  related/                 #   횡단 개념 (조건·스코프·가정·하네스)
  shapes/                  #   SHACL shape (*-shapes) — 4.4절 청크 규칙 등
odd/project-odd.ttl        # 이 프로젝트의 운영 설계 영역 (Part III)
kg/base-kg.ttl             # A-Box — 청크가 아닌 개체 (가정·출처 문서)
kg/catalog-kg.ttl          # A-Box — 에이전트 카탈로그 (역할·스코프·하네스, 9.2절)
kg/chunks-kg.ttl           # (생성) 청크 head 그래프 — frontmatter에서 생성 (4.3절)
chunks/<plane>/*.md        # 청크. 한 청크 = 한 파일: frontmatter(head) + 본문 ≤ 42줄
space/                     # 설계 공간 (*-space, Part VII) — 5단계에서 채움
docs/feedback/             # 유저 피드백 채널 (그래프 밖) — hci agent 담당, 규약은 README.md
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

## 도입 단계 (노트 Part XII)

- **1단계 (청크와 plane)** — 이 하네스가 구현. 온톨로지 `entity/` 최소본, 청크·게이트 동작.
- **2단계 (ODD와 스코프)** — 어휘와 `project-odd.ttl` 준비됨. 에이전트 카탈로그·스코프 개체는 다음 작업.
- 3단계 이후(링크·가정 전파·사다리)는 어휘 확장과 함께 진행.

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

`../harness_ontology`(하네스 온톨로지·방법론)와 `../harness-recipes`(조립
명세)는 **내용의 원천**이다. 프로젝트 자체를 빌드에 연결하지 않고, 필요한
지식을 `agt:` 어휘의 청크로 승격해 가져오며 출처를 `prov:wasDerivedFrom`
으로 남긴다 (출처 개체는 `kg/base-kg.ttl`의 `id:doc-harness-ontology`,
`id:doc-harness-recipes`).
