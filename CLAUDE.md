# CLAUDE.md — 이 저장소에서 일하는 방법

무엇을 만드는 저장소인지는 [`README.md`](README.md), 목적과 대상 지식은
[`docs/purpose.md`](docs/purpose.md). 작업 규칙의 원본은 **`AGENTS.md`**, 저작 스타일의
원본은 **`STYLEGUIDE.md`**다. 세션 시작 시 두 문서를 읽고 그대로 따른다 — 이 파일은
Claude Code용 진입점이며 두 문서를 재진술하지 않는다.

요약(원본은 위 두 문서):

1. 지식 파일을 고치면 `bazel test //...` — 실패하면 게이트가 아니라 산출물을 고친다.
2. 어휘 밖 술어 금지 — 새 개념은 온톨로지 모듈에 파일 하나를 먼저 추가한다.
3. 스코프·가정은 ODD(`kb/odd/project-odd.yml`, OpenODD)의 조건만 참조 — 필요하면 ODD 먼저 확장.
4. **한 청크는 한 파일**(frontmatter + 본문 ≤ 42줄)이고 이 규칙은 온톨로지·ODD·지식그래프
   파일에도 적용된다. head 그래프는 생성물이다 — `kg/`에 손으로 쓰지 않는다.
5. 지식의 종류는 고유 용어로 부른다(조건·개념·결정·가정·관측…). "X 청크"라 하지 않는다 —
   청크는 그것들이 따르는 구조 규칙이다.
6. 역할·권한(`AGENTS.md` 표)의 형식 원본은 `kg/catalog-kg.ttl` — 문서와 그래프를 같은
   커밋에서 일치시킨다.
7. 참조 저장소(`../harness-functional`·`../harness-concrete`)는 내용의 원천일 뿐 빌드
   의존이 아니다 — `derived_from`으로 출처를 남긴다.
8. 산문은 한글, 식별자·라벨(en)은 영어. 지어낸 용어 금지.

무엇을 어떻게 하는지는 [`docs/method.md`](docs/method.md), 무엇이 유효한 구조인지는
[`docs/rules.md`](docs/rules.md)를 본다. 저장소를 통째로 컨텍스트에 싣지 않는다.
