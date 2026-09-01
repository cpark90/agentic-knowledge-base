# 저장 설계 — 청크는 어떻게 놓이고 head는 어떻게 생성되는가

노트 4.3절(청크 = 네 개의 이름 붙은 그래프)과 4.9절(저장)을 이 저장소가 어떻게
실현했는지 기록한다. 개념적 근거는
[`id:chunk-d0011`](../chunks/decision/d-0011-chunk-four-graphs.md)에 있고,
여기서는 **파일 배치와 생성 파이프라인**만 다룬다.

## 확정 결정

- **S1 — 한 청크는 한 파일.** head 메타데이터(frontmatter)와 본문(assertion)이
  같은 파일에 있다. 두 곳에 나눠 두면 어긋난다.
- **S2 — head 그래프는 생성물이다.** `kg/chunks-kg.ttl`을 손으로 쓰지 않는다.
  `tools/chunk2kg.py`가 frontmatter에서 만들고, `bazel-out`에만 존재한다.
- **S3 — 파생 가능한 값은 저장하지 않는다.** `agt:lineCount`와
  `agt:assertionLocation`은 파일에서 계산된다 — 손으로 적을 수 없으므로 어긋날
  수 없다.
- **S4 — 청크는 자기가 무엇에 연결되는지 모른다.** 링크·구성체 소속은 청크
  파일 밖(`kg/composite-kg.ttl`)에 있다. 그래서 청크가 재사용 가능하다 (4.3절).

## 네 그래프의 실현

노트의 네 이름 붙은 그래프가 이 저장소에서 어디에 사는가:

| 그래프 (4.3절) | 담는 것 | 이 저장소의 위치 |
|---|---|---|
| **head** | 타입·plane·level·라벨·상태 | 청크 파일의 frontmatter → **생성** `kg/chunks-kg.ttl` |
| **assertion** | 본문. 42줄 제한은 여기만 | 청크 파일의 `---` 아래 |
| **provenance** | 이 본문이 무엇에서 왔는가 | frontmatter `derived_from` → `prov:wasDerivedFrom` |
| **pubinfo** | 언제 만들어졌는가, 버전 | frontmatter `generated_at` → `prov:generatedAtTime` |

**차이 — 이름 붙은 그래프를 쓰지 않는다.** 저장 형식이 Turtle(트리플)이므로
네 그래프는 **논리적 구분**으로만 존재하고, 물리적으로는 하나의 기본 그래프에
합쳐진다. 나노출판의 구조를 그대로 쓰려면 TriG(쿼드)와 그래프 IRI가 필요하다.
현재 그 필요가 없어 미루었다 — §미해결 참조.

## 청크 파일 형식

```markdown
---
iri: https://agentic-knowledge-base.dev/id/chunk-d0001   # 필수
plane: decision            # 필수. decision|contract|schema|artifact|annotation|memory
level: concrete            # 필수. functional|abstract|logical|concrete|executable
label_ko: Bazel 하네스 채택  # 필수
label_en: Adopt Bazel harness # 필수
state: valid               # 필수. draft|valid|suspect|invalidated|deprecated
assumes: [<가정 IRI>, ...]   # 선택
derived_from: [<출처 IRI>, ...] # 선택
generated_at: 2026-09-01T00:00:00+09:00  # 선택
---
본문 — 42줄 이하 (frontmatter와 앞뒤 빈 줄은 세지 않는다)
```

값 어휘의 원본은 `tools/chunk2kg.py` 상단이다. frontmatter는 YAML의 부분집합만
파싱한다(`key: value`, 목록은 `[a, b]`) — 완전한 YAML 파서를 쓰지 않는 것은
의존성을 늘리지 않고 형식을 좁게 강제하기 위해서다.

## 생성 파이프라인

```
chunks/<plane>/*.md                    (원본 — 사람이 쓴다)
        │
        │  //kg:chunks_kg  (genrule)
        │  tools/chunk2kg.py --out $@ $(SRCS)
        ▼
bazel-out/.../kg/chunks-kg.ttl         (생성 — 손대지 않는다)
        │
        │  //kg:gate_test 의 --data 입력
        ▼
검사 게이트 (어휘 폐쇄 · SHACL · ODD 참조)
```

생성기가 하는 일:

| 단계 | 내용 | 실패 시 |
|---|---|---|
| frontmatter 파싱 | 필수 키 6개 존재, 값이 어휘 안 | 비영 종료 (게이트 실패) |
| IRI 중복 검사 | 두 파일이 같은 IRI를 선언하지 않음 | 비영 종료 — "한 청크는 한 파일" 위반 |
| `lineCount` 계산 | frontmatter·앞뒤 빈 줄 제외한 본문 줄 수 | — |
| `assertionLocation` | 저장소 상대 경로 (4.9절 앵커) | — |
| head 트리플 방출 | plane → 청크 클래스, level → `agt:hasLevel` | — |

**앵커 해석** (4.9절): 산문 계열 plane은 `IRI → 파일 경로`가 앵커다.
`agt:assertionLocation`이 그 사상이며, 코드 계열(`artifact`)이 생기면 `IRI →
심볼 ID`로 확장해야 한다. 지금은 산문 계열만 있으므로 경로 하나로 충분하다.

## 청크가 아닌 개체

`kg/`의 나머지는 손으로 쓴다 — 생성 대상이 아니다.

| 파일 | 담는 개체 | 왜 손으로 쓰나 |
|---|---|---|
| `base-kg.ttl` | 가정(`asm-`), 출처 문서(`doc-`) | 파일에서 파생되지 않는 판단 |
| `catalog-kg.ttl` | 하네스·역할·스코프·채널 | 입력(9.1절)이지 지식이 아니다 |
| `composite-kg.ttl` | 구성체(`comp-`) | 어느 청크를 묶을지가 판단이다 |

`base-kg.ttl` 상단 배너가 "청크 head를 여기 쓰지 않는다"를 명시한다 — 규약이
파일 안에 있어야 다음 저작자가 본다.

## 정규화 직렬화

기계가 만든 TTL은 커밋 전 정규형으로 바꾼다 (노트 2.5절):

```bash
bazel run //tools:canonicalize -- --write <files>
```

정규형 = 정렬된 `@prefix` 블록 + 주어 정렬 + 술어 정렬(`rdf:type` 우선) +
목적어 정렬, 익명 노드는 rdflib 정준화로 라벨 고정. **직렬화 순서가 불안정하면
git diff가 의미 없는 변경으로 오염되고, 그것이 무효화 판정의 입력을 더럽힌다.**
`--check`는 정규형과 다르면 비영 종료하므로 게이트에 넣을 수 있다.

## 미해결

- **이름 붙은 그래프** — 현재 네 그래프가 논리적 구분일 뿐이다. `annotation`
  plane이 생기면 "어느 그래프에 대한 논평인가"를 말해야 하므로 TriG 전환을
  다시 검토한다.
- **내용 해시 IRI** — 노트 4.3절은 본문 해시를 버전 IRI에 넣어(trusty URI)
  해시 변경이 링크 재판정을 촉발하게 한다. 현재 IRI는 불투명 식별자 하나뿐이고
  버전 IRI가 없다. 링크(3단계)가 없으면 재판정할 대상도 없으므로 그때 함께
  도입하는 것이 순서다.
- **`memory` plane의 42줄 단위** — 노트 4.12절 미해결. 줄이 아니라 항목 수여야
  할 수 있고, 그러면 `chunk_lint.py`가 plane별로 다른 단위를 세야 한다.
