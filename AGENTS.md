# AGENTS.md — 이 저장소의 에이전트 하네스

이 저장소는 에이전트 지식 관리 체계의 인스턴스이자 **그 체계 자신의 명세를 담는
곳**이다. 정리된 지식(온톨로지·ODD·지식그래프·청크)과 그것을 검사·활용하는 도구를
**Bazel 하네스**로 묶는다. 모든 지식이 파일·디렉토리 기반 청크로 구조화되어 있고,
그 구조를 정리·활용하는 도구가 Bazel이다 — 지식은 데이터 타깃, 검사 게이트(6.7절)는
테스트 타깃, `bazel test //...` 한 번이 게이트 전체다.

체계의 규칙은 결정 청크(`chunks/decision/`), 구현 설계와 진행 상태는 `docs/`에
있다. 산문의 `(노트 N.N절)` 인용은 분해 전 설계 노트에 대한 출처 기록이다
(`docs/README.md`).

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
7. **유저와의 상세 소통은 hci만 한다.** 다른 에이전트는 유저 피드백이 필요하거나
   문제·특이사항이 생기면 채널(`docs/feedback/agents/`)에 항목을 남긴다 — 유저에게
   직접 묻지 않는다. 채널 규약 원본: `docs/feedback/README.md`.

## 에이전트 역할 (노트 9.2절 카탈로그의 부분집합)

형식 원본: `kg/catalog-kg.ttl` (`id:h-akb`) — 역할 5개와 각각의 스코프
(`id:scope-*`)가 거기 있다. 각 역할은 자기 write plane 밖을 수정하지 않는다.
설계/구현/운영 역할은 같은 write plane을 공유하지 않는다. 별도 세션으로 도는
역할은 정의 파일을 갖는다(`.claude/agents/hci.md`); orchestrator는 메인이라
이 표가 정의이고, developer·vnv는 dispatch 시 이 표와 스코프로 브리핑한다.

| 역할 | 책임 | write | read | 구동 | git |
|---|---|---|---|---|---|
| **orchestrator** (=메인) | 계획·dispatch·통합. 결정 청크 저작. 직접 구현하지 않는다 | `decision` | 전 plane | 세션 유지 | ✗ |
| **developer** (dispatch) | 분배된 산출물(코드·설정·온톨로지 청크) 저작 | `artifact` | `contract`·`schema`·`decision` | dispatch | ✗ |
| **vnv** (dispatch) | 판정 전용: `bazel test //...` PASS 확인 + 결과 논평 | `annotation` | `artifact`·`decision` | dispatch | ✗ |
| **inspection** (별도 세션) | 조사 전용 + git 관리 (add/commit/push, 유저 요청 시) | — | 전 plane | 세션 유지 | ✓ |
| **hci** (별도 세션) | **유저 소통 전담 — 유일한 유저 창구.** 조사 요청 접수·구체화·제안 정리·타 에이전트 피드백 검토·중계. 채널 `docs/feedback/` 관리 | — (채널만) | 전 plane + 저장소 전체 | 세션 유지 | ✗ |

- dispatch 대상에게는 전체 컨텍스트가 아니라 **역할 스코프로 거른 situation**만 전달한다
  (9.3절). 저장소를 통째로 컨텍스트에 싣지 않는다.
- **채널 쓰기 경계**: hci의 작성·수정 범위는 소통 채널(`docs/feedback/**`)로 한정되고
  조회 범위는 저장소 전체다. 다른 에이전트는 채널에서 **유저에게 전달할 자기 항목**
  (`agents/` lane)과 조사 lane의 자기 담당 답만 작성·수정할 수 있고, 이외 채널 파일은
  조회만 가능하다.
- 역할별 `agt:maxConcurrent`의 합은 ODD 동적 요소(`id:cond-concurrent-agents`,
  현재 ≤ 5) 안이어야 한다 (9.2절·9.6절). 역할을 추가하면 ODD 한도도 함께 검토한다 —
  지금 이 검사는 규약이고 게이트가 아니다(README "다음" 참조).
- 커밋 전 `bazel test //...` PASS를 확인한다. 커밋은 inspection(또는 유저 지시)만.

## 표준 워크플로

**① 지식 청크 저작** — 가장 흔한 작업.
1. plane과 level을 정하고 `chunks/<plane>/` 아래 파일 하나를 만든다
   (frontmatter 스키마는 `STYLEGUIDE.md` §4, 형식 예는 `README.md`).
2. 전제가 있으면 가정 개체를 `kg/base-kg.ttl`에 추가하고 frontmatter `assumes`로
   가리킨다. 가정은 ODD 조건을 `agt:refersTo` 해야 한다.
3. **같은 커밋에서 구성체에 잇는다** — `kg/composite-kg.ttl`의 기존 구성체에
   `agt:hasDirectPart`로 넣거나, 주제가 새로우면 구성체를 하나 만든다. 부분은
   최대 9개(7±2)이고 부분의 plane·level은 전체와 같아야 한다(동질성, 4.5절).
   어느 구성체의 부분도 아니고 링크도 없는 청크가 고아다(4.13절 고아율).
4. `bazel test //...` — chunks-kg 생성과 게이트가 한 번에 돈다.

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

**④ 참조 저장소 내용 승격** — `../harness-functional`(구 harness_ontology,
하네스의 functional+ODD)과 `../harness-concrete`(구 harness-recipes, 하네스의
logical+concrete)의 지식 활용.
1. 필요한 부분만 읽는다. 프로젝트 자체를 빌드에 연결하지 않는다 (ODD 명시 제외).
2. 가져올 지식을 `agt:` 어휘의 청크로 다시 쓴다 — `ho:` 어휘를 섞지 않는다.
3. frontmatter `derived_from`에 출처 개체(`id:doc-harness-ontology` /
   `id:doc-harness-recipes` — IRI는 개명 전 이름을 유지, 0.7절 지속 IRI)를
   남긴다. 출처 없는 승격은 감사(10.4절)가 잡는다.
4. 이송(원본에서 제거하며 옮기는 경우)이면 원본 저장소에 이송 표기를 남긴다.

**⑤ 게이트 실패 대응.**
- FAIL 메시지에 노트 절 번호가 있다 — 그 절이 수정 방향이다.
- 게이트가 틀렸다고 판단되면 게이트를 고치지 말고 채널에 항목을 남긴다. shape 약화는
  유저 승인 사항이다.

**⑥ 유저 피드백 처리** — 파이프라인 원본은 `docs/feedback/README.md`.
1. 유저 항목(조사 요청·구체화·제안) 또는 에이전트 항목이 채널에 들어온다.
2. hci가 검토·구체화한다 — 조사가 필요하면 조사 lane으로 위임하고, 유저 판단이
   필요한 에이전트 항목은 유저 lane으로 중계한다.
3. 유저가 `status: approved`로 태깅한 항목만, 반영 계획대로 담당 write plane의 역할이
   지식 산출물에 반영한다 (결정은 orchestrator, 산출물은 developer). 반영 후
   `bazel test //...` PASS + 항목에 반영 결과 기록.
4. hci가 반영 확인된 항목을 refresh한다.

## 소통 규칙 (문서 우선)

- **유저와의 상세 소통은 hci와 채널(`docs/feedback/`)을 경유한다** (황금률 7).
  다른 에이전트가 유저에게 필요로 하는 것(피드백·문제·특이사항)은 `agents/` lane에
  항목으로 남기고, hci가 확인해 유저 피드백을 받아온다.
- 상태·결정·논평은 해당 산출물(결정은 `decision` 청크, 논평은 `annotation` 청크)에
  쓰고, 세션에는 무엇을 어디에 썼는지 요점만 남긴다. 임시 파일은 스크래치패드에 둔다.
- 채널 파일은 그래프 밖이다 — 게이트 검사 대상이 아니며, 소통의 결론은 채널에 남기지
  않고 지식(청크·ODD·온톨로지)으로 승격한다.

## 언어 정책 (노트 0.6절)

산문은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase(`agt:Assumption`), 라벨은
한/영 1:1. 지어낸 용어를 쓰지 않는다 — 확립된 표준어가 있으면 그것을 쓴다(0.0절).

## 셀프체크

작업 완료 전 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화 (2.5절)
```
