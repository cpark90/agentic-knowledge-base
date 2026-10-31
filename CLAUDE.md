# CLAUDE.md — 이 저장소에서 일하는 방법

이 파일은 Claude Code가 세션을 시작할 때 읽는 진입점이고, 작업 규칙과 저작 스타일을 다시 적지 않는다.
무엇을 만드는 저장소인지는 [`README.md`](README.md)에 있고, 목적과 대상 지식은
[`docs/purpose.md`](docs/purpose.md)에 있다. 작업 규칙은 **`AGENTS.md`**에서, 저작 스타일은
**`STYLEGUIDE.md`**에서 읽는다. 세션을 시작하면 두 문서를 읽고 그대로 따른다. 두 문서는 생성 파일이고,
원본은 결정의 규약 항목인 `conventions.md`와 `kb/dev/norm/`의 절 항목이다.

아래 요약의 원본도 두 문서와 그 원본 단위 지식이다.

1. 지식 파일을 고치면 `bazel test //...`를 돌린다. 실패하면 게이트가 아니라 산출물을 고친다.
2. 어휘 밖 술어를 쓰지 않는다. 새 개념이 필요하면 온톨로지 모듈에 파일 하나를 먼저 추가한다.
3. 적용 범위와 가정은 ODD의 조건만 참조한다. ODD 문서는 OpenODD 형식의 `kb/odd/project-odd.yml`이다.
   필요한 조건이 없으면 ODD를 먼저 확장한다.
4. **한 단위 지식은 한 파일**이다. 본문은 frontmatter를 빼고 토큰 상한 이하여야 하고, 상한은 저작 산문이 1,092,
   인용이 2,856이다. 2026-10-01 전에는 상한이 42줄이었다. 이 규칙은 온톨로지 파일에도 적용된다.
   head 그래프는 생성물이므로 `kg/`에 손으로 쓰지 않는다.
5. 지식의 종류는 고유 용어로 부른다. 고유 용어는 조건과 개념, 결정, 가정, 관측 등이다. "X 단위 지식"이라
   하지 않는다. 단위 지식은 그 종류들이 따르는 구조 규칙을 말할 때만 쓴다.
6. 역할과 권한을 정한 `AGENTS.md` 표의 형식 원본은 `kg/catalog-kg.ttl`이다. 그래서 문서와 그래프를 같은
   커밋에서 일치시킨다.
7. 참조 저장소 `../harness-functional`과 `../harness-concrete`는 내용의 원천일 뿐 빌드
   의존이 아니다. 가져온 내용에는 `sources`로 출처를 남긴다.
8. 산문은 한글 **단정 서술형**이다. 평서형 "…다"로 쓰고 경어와 감탄, 구어, 추측을 쓰지 않는다.
   세션 보고도 같다. 식별자와 영문 라벨은 영어로 쓴다. 지어낸 용어를 쓰지 않는다.
9. 외부 대상과의 소통은 interpreter 세션이 맡고, 유저와의 상세 소통은 그 하위 역할인 hci가 맡는다. 유저의 결정은
   `harness/user/`의 파일 질문지로 받는다. interpreter와 orchestrator는 `harness/channel/`의 에이전트 채널에
   메시지를 남겨서만 소통한다. 역할 세션은 `harness/scripts/run-interpreter.sh`와 `harness/scripts/run-orchestrator.sh`로
   띄운다. hci는 interpreter 세션이 맡는 하위 역할로 남고, 옛 경로 `harness/scripts/run-hci.sh`도 같은 세션을 띄운다. 프로토콜 원본은 [`harness/README.md`](harness/README.md)다.

무엇을 어떻게 하는지는 [`docs/method.md`](docs/method.md)를, 무엇이 유효한 구조인지는
[`docs/rules.md`](docs/rules.md)를 본다. 저장소를 통째로 컨텍스트에 싣지 않는다.
