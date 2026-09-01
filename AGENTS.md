# AGENTS.md — 이 저장소의 에이전트 하네스

이 저장소는 에이전트 지식 관리 체계(`agent-knowledge-system-notes.md`, 이하 "노트")의
인스턴스다. 정리된 지식(온톨로지·ODD·지식그래프·청크)과 그것을 검사·활용하는 도구를
**Bazel 하네스**로 묶는다. 모든 지식이 파일·디렉토리 기반 청크로 구조화되어 있고,
그 구조를 정리·활용하는 도구가 Bazel이다 — 지식은 데이터 타깃, 검사 게이트(노트
6.7절)는 테스트 타깃, `bazel test //...` 한 번이 게이트 전체다.

작성 스타일(각 컴포넌트별 규칙)은 **`STYLEGUIDE.md`가 단일 진실 공급원**이다.
저작·수정 세션을 시작할 때 그 문서를 읽는다.

## 황금률

1. **지식 파일을 고치면 `bazel test //...` 를 돌린다.** 실패하면 고친 파일을 수정한다 —
   shape·게이트 코드를 약화시키지 않는다.
2. **어휘 밖에서 쓰지 않는다.** 데이터(kg·odd·space)의 술어는 `agt:` 온톨로지 또는 표준
   어휘여야 한다. 새 개념이 필요하면 온톨로지 청크(파일)를 먼저 추가한다 — 게이트가
   한/영 라벨과 `skos:definition`을 강제한다.
3. **ODD가 상위다.** 스코프·가정은 `odd/project-odd.ttl`의 조건만 참조할 수 있다(0.4절).
   없는 조건이 필요하면 ODD를 먼저 확장한다 — 판정 방법과 등급(A–D)이 필수다.
4. **한 청크는 한 파일이다.** 지식도, 온톨로지도, shape도 파일 하나 = 청크 하나.
   본문 42줄 이하(4.1절), 한 주제, 라벨이 본문을 대표해야 한다.
5. **생성 산출물을 손으로 고치지 않는다.** 청크 head 그래프(`//kg:chunks_kg`)는
   frontmatter에서 생성된다. 고칠 것은 원본 청크 파일이다.
6. **문서와 그래프는 일치해야 한다.** 아래 역할 표의 원본은 `kg/catalog-kg.ttl`이다.
   역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.

## 에이전트 역할 (노트 9.2절 카탈로그의 부분집합)

형식 원본: `kg/catalog-kg.ttl` (`id:h-akb`). 각 역할은 자기 write plane 밖을 수정하지
않는다. 설계/구현/운영 역할은 같은 write plane을 공유하지 않는다.

| 역할 | 책임 | write | read | 구동 | git |
|---|---|---|---|---|---|
| **orchestrator** (=메인) | 계획·dispatch·통합. 결정 청크 저작. 직접 구현하지 않는다 | `decision` | 전 plane | 세션 유지 | ✗ |
| **developer** (dispatch) | 분배된 산출물(코드·설정·온톨로지 청크) 저작 | `artifact` | `contract`·`schema`·`decision` | dispatch | ✗ |
| **vnv** (dispatch) | 판정 전용: `bazel test //...` PASS 확인 + 결과 논평 | `annotation` | `artifact`·`decision` | dispatch | ✗ |
| **inspection** (별도 세션) | 조사 전용 + git 관리 (add/commit/push, 사용자 요청 시) | — | 전 plane | 세션 유지 | ✓ |

- dispatch 대상에게는 전체 컨텍스트가 아니라 **역할 스코프로 거른 situation**만 전달한다
  (9.3절). 저장소를 통째로 컨텍스트에 싣지 않는다.
- 동시 활성 수의 합은 ODD 동적 요소(`id:cond-concurrent-agents`, ≤ 2) 안이어야 한다.
- 커밋 전 `bazel test //...` PASS를 확인한다. 커밋은 inspection(또는 사용자 지시)만.

## 표준 워크플로

**① 지식 청크 저작** — 가장 흔한 작업.
1. plane과 level을 정하고 `chunks/<plane>/` 아래 파일 하나를 만든다
   (frontmatter 스키마는 `STYLEGUIDE.md` §4, 형식 예는 `README.md`).
2. 전제가 있으면 가정 개체를 `kg/base-kg.ttl`에 추가하고 frontmatter `assumes`로
   가리킨다. 가정은 ODD 조건을 `agt:refersTo` 해야 한다.
3. `bazel test //...` — chunks-kg 생성과 게이트가 한 번에 돈다.

**② 온톨로지 확장** — 새 개념이 필요할 때.
1. 기존 어휘를 먼저 찾는다 (`grep -r "찾는개념" ontology/`). 같은 뜻의 개념을 둘
   만드는 것이 이 체계가 막는 drift다.
2. 정말 필요하면: 기존 모듈 디렉토리에 새 청크 파일을 추가하거나(주제가 맞을 때),
   새 모듈 디렉토리 + `BUILD.bazel` + `//ontology:modules` 등록(새 주제일 때).
   기존 파일의 개념을 다른 파일에서 재정의하지 않는다 — boundary 게이트가 거부한다.
3. `bazel test //ontology:gate_test //ontology:chunk_lint_test`.

**③ ODD 확장** — 스코프·가정이 새 조건을 필요로 할 때.
1. `odd/project-odd.ttl`에 조건 개체를 추가한다: 3분류 중 하나의 타입, `conditionValue`,
   객관적 `checkMethod`(명령 또는 관측 수단), `verificationGrade`.
2. ODD 개체의 `agt:hasCondition` 목록에 등록한다. `bazel test //odd:gate_test`.

**④ 참조 저장소 내용 승격** — `../harness_ontology`, `../harness-recipes`의 지식 활용.
1. 필요한 부분만 읽는다. 프로젝트 자체를 빌드에 연결하지 않는다 (ODD 명시 제외).
2. 가져올 지식을 `agt:` 어휘의 청크로 다시 쓴다 — `ho:` 어휘를 섞지 않는다.
3. frontmatter `derived_from`에 출처 개체(`id:doc-harness-ontology` /
   `id:doc-harness-recipes`)를 남긴다. 출처 없는 승격은 감사(10.4절)가 잡는다.

**⑤ 게이트 실패 대응.**
- FAIL 메시지에 노트 절 번호가 있다 — 그 절이 수정 방향이다.
- 게이트가 틀렸다고 판단되면 게이트를 고치지 말고 사용자에게 보고한다. shape 약화는
  사용자 승인 사항이다.

## 소통 규칙 (문서 우선)

상태·결정·질문은 해당 산출물(결정은 `decision` 청크, 논평은 `annotation` 청크)에 쓰고,
세션에는 무엇을 어디에 썼는지 요점만 남긴다. 임시 파일은 스크래치패드에 둔다.

## 언어 정책 (노트 0.6절)

산문은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase(`agt:Assumption`), 라벨은
한/영 1:1. 지어낸 용어를 쓰지 않는다 — 확립된 표준어가 있으면 그것을 쓴다(0.0절).

## 셀프체크

작업 완료 전 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화 (2.5절)
```
