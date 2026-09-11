# AGENTS.md — 이 저장소의 에이전트 하네스

이 저장소가 무엇을 만드는지는 [`README.md`](README.md), 목적은
[`docs/purpose.md`](docs/purpose.md)다. 여기는 **에이전트가 이 저장소에서 일하는 규칙**을
정한다 — 역할·권한·소통·커밋. 지식을 어떻게 만드는지는 [`docs/method.md`](docs/method.md),
무엇이 유효한 구조인지는 [`docs/rules.md`](docs/rules.md), 저작 스타일은
[`STYLEGUIDE.md`](STYLEGUIDE.md)가 원본이다.

## 황금률

1. **지식 파일을 고치면 `bazel test //...` 를 돌린다.** 실패하면 고친 파일을 수정한다 —
   shape·게이트 코드를 약화시키지 않는다.
2. **어휘 밖에서 쓰지 않는다.** 데이터의 술어는 `agt:` 온톨로지 또는 등록된 표준 어휘여야
   한다. 새 개념이 필요하면 온톨로지 모듈에 파일을 먼저 추가한다 — 게이트가 한/영 라벨과
   `skos:definition`을 강제한다 ([`docs/ontology.md`](docs/ontology.md)).
3. **ODD가 상위다.** 스코프·가정은 `kb/odd/project-odd.yml`(OpenODD; TTL은 생성물)의 조건만 참조할 수 있다. 없는
   조건이 필요하면 ODD를 먼저 확장한다 — 판정 방법과 등급이 필수다.
4. **한 청크는 한 파일이다.** 지식도, 온톨로지도, shape도 파일 하나가 단위 하나이며 본문
   42줄 이하다. 청크는 포맷이 아니라 **구조 규칙**이다.
5. **지식의 종류는 고유 용어로 부른다** — 조건·개념·변수·후보·결정·가정·시그니처·함수·
   주석·관측. "X 청크"라 하지 않는다. 온톨로지 클래스 이름(`agt:DecisionChunk` 등)을 인용할
   때는 그대로 쓴다.
6. **생성 산출물을 손으로 고치지 않는다.** head 그래프(`//kg:chunks_kg`)는 frontmatter에서
   생성된다. 고칠 것은 원본 파일이다.
7. **문서와 그래프는 일치해야 한다.** 아래 역할 표의 형식 원본은 `kg/catalog-kg.ttl`이다.
   역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.
8. **유저와의 상세 소통은 hci만 한다.** 다른 에이전트는 유저 피드백이 필요하거나 문제·
   특이사항이 생기면 채널(`docs/feedback/agents/`)에 항목을 남긴다 — 유저에게 직접 묻지
   않는다. 채널 규약 원본: [`docs/feedback/README.md`](docs/feedback/README.md).

## 에이전트 역할

형식 원본: `kg/catalog-kg.ttl` (`id:h-akb`) — 역할 5개와 각각의 스코프(`id:scope-*`)가
거기 있다. 각 역할은 자기 write plane 밖을 수정하지 않는다. 설계·구현·운영 역할은 같은
write plane을 공유하지 않는다. 별도 세션으로 도는 역할은 정의 파일을 갖는다
(`.claude/agents/hci.md`); orchestrator는 메인이라 이 표가 정의이고, developer·vnv는
dispatch 시 이 표와 스코프로 브리핑한다.

| 역할 | 책임 | write | read | 구동 | git |
|---|---|---|---|---|---|
| **orchestrator** (=메인) | 계획·dispatch·통합. 요구(유저 관심사의 EARS 저작 — stable 전이는 유저 승인)·결정 저작. 직접 구현하지 않는다 | `requirement` · `decision` | 전 plane | 세션 유지 | ✗ |
| **developer** (dispatch) | 분배된 산출물(코드·설정·온톨로지 개념) 저작. 노트 10.2절 9역할 중 design(T-Box·ODD 편집)을 겸한다 — 유저 결정 C4 | `artifact` (+T-Box·ODD) | `contract`·`schema`·`decision`. **`kb/vv/`는 읽기 전용** | dispatch | ✗ |
| **vnv** (dispatch) | 판정 전용: `bazel test //...` PASS 확인 + 결과 주석. **V&V KB(`kb/vv/`)의 유일한 편집 주체** — `verifies`의 주어는 V&V 청크뿐 | `annotation` + `kb/vv/` | `requirement`·`artifact`·`decision` | dispatch | ✗ |
| **inspection** (별도 세션) | 조사 전용 + git 관리 (add/commit/push, 유저 요청 시) | — | `requirement`·전 plane | 세션 유지 | ✓ |
| **hci** (별도 세션) | **유저 소통 전담 — 유일한 유저 창구.** 조사 요청 접수·구체화·제안 정리·타 에이전트 피드백 검토·중계. 채널 `docs/feedback/` 관리 | — (채널만) | `requirement`·전 plane + 저장소 전체 | 세션 유지 | ✗ |

- dispatch 대상에게는 전체 컨텍스트가 아니라 **작업 집합**(스코프 × level 창으로 거른 청크 집합)만 전달한다
  ([`docs/method.md` §8](docs/method.md#8-조회)). 저장소를 통째로 컨텍스트에 싣지 않는다.
- **채널 쓰기 경계**: hci의 작성·수정 범위는 소통 채널(`docs/feedback/**`)과 자기 역할
  메모리(`.claude/agent-memory/hci/**`)뿐이고 조회 범위는 저장소 전체다. 다른 에이전트는
  채널에서 **자기 항목**(`agents/` lane, 조사 lane의 자기 담당 답)만 작성·수정할 수 있고
  이외 채널 파일은 조회만 가능하다.
- 역할별 `agt:maxConcurrent`의 합은 ODD 동적 요소(`id:cond-concurrent-agents`, 현재 ≤ 5)
  안이어야 한다. 역할을 추가하면 ODD 한도도 함께 검토한다 — **지금 이 검사는 규약이고
  게이트가 아니다** ([`docs/tools.md` §게이트 밖](docs/tools.md#게이트-밖--규약으로-남은-것)).
- 커밋 전 `bazel test //...` PASS를 확인한다. 커밋은 inspection(또는 유저 지시)만.

## 작업

지식을 만드는 절차는 전부 [`docs/method.md`](docs/method.md)에 있다 — 프로파일 구축, ODD
작성, 청크 저작, 정제 전이, 후보 관리, 연결, 갱신, 조회, 뷰, 일반화, 검증, 영향 분석.
하네스 쪽에서 추가로 지켜야 할 것은 아래 둘뿐이다.

**게이트 실패 대응.** FAIL 메시지의 인용이 수정 방향이다. 게이트가 틀렸다고 판단되면
게이트를 고치지 말고 채널에 항목을 남긴다 — shape 약화는 유저 승인 사항이다.

**유저 피드백 처리** (파이프라인 원본은 [`docs/feedback/README.md`](docs/feedback/README.md)).
1. 유저 항목(조사 요청·구체화·제안) 또는 에이전트 항목이 채널에 들어온다.
2. hci가 검토·구체화한다 — 조사가 필요하면 조사 lane으로 위임하고, 유저 판단이 필요한
   에이전트 항목은 유저 lane으로 중계한다.
3. 유저가 승인한 항목만(`status: approved` 태깅 또는 담당 역할에게 준 구두 답 — hci는 어느 쪽이든 수행하지 않는다, `//docs/feedback:channel_lint_test`·writer 검사가 강제), 반영 계획대로 담당 write plane의 역할이
   반영한다. 반영 후 `bazel test //...` PASS + 항목에 반영 결과 기록.
4. hci가 반영 확인된 항목을 refresh한다.

## 소통 규칙 (문서 우선)

- **유저와의 상세 소통은 hci와 채널을 경유한다**(황금률 8). 다른 에이전트가 유저에게
  필요로 하는 것은 `agents/` lane에 항목으로 남기고, hci가 확인해 유저 피드백을 받아온다.
- 상태·결정·주석은 해당 산출물에 쓰고(결정은 `decision`, 주석은 `annotation`), 세션에는
  무엇을 어디에 썼는지 요점만 남긴다. 임시 파일은 스크래치패드에 둔다.
- 채널 파일은 그래프 밖이다 — 게이트 검사 대상이 아니며, 소통의 결론은 채널에 남기지 않고
  지식(온톨로지·ODD·청크)으로 승격한다.
- 유저의 판단이 필요한 항목은 **다섯 절**로 쓴다 — 질문 / 이미 정해진 것 / 현재 상태 /
  답이 가르는 것 / 선택지. 한 줄 질문으로는 답을 받을 수 없다(유저 지적 2026-09-02).

## 언어 정책

산문은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase(`agt:Assumption`), 라벨은 한/영
1:1. **지어낸 용어를 쓰지 않는다** — 확립된 표준어가 있으면 그것을 쓴다.

## 셀프체크

작업 완료 전 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화
```
