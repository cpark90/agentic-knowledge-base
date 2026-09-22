---
id: https://agentic-knowledge-base.dev/id/chunk/160ca62a-0dd2-4b06-a5e5-21bb1fc54fbe
type: decision
level: concrete
title_ko: 생성 문서의 본문 서식은 마크다운 표준 규칙과 빈 값 한 표기를 따른다
title: The body of a generated document follows standard Markdown rules and one empty-value form
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/9807be26-ff48-4cca-89c1-129f52e69df4]
serves: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
restored: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:05:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/6364f6e3-f553-4178-946c-36246fed08a9
composite: {id: https://agentic-knowledge-base.dev/id/composite/6364f6e3-f553-4178-946c-36246fed08a9, title_ko: 생성 문서의 본문 서식, title: The body form of a generated document}
---
**결론** — 본문 서식은 여덟 규칙이다. 앞의 일곱은 게이트가 강제하고 여덟째는 권장이다.

| 규칙 | 내용 | 출처 |
|---|---|---|
| 제목 계층 | 한 단계씩 내려간다. h1 다음에 h3을 두지 않는다 | markdownlint MD001 · WCAG 2.2 SC 1.3.1 |
| 제목 하나 | h1은 문서당 하나이고 파일 첫 줄이다. 코드 펜스 안은 제목이 아니다 | markdownlint MD025·MD041 |
| 표 | 헤더 행을 갖고, 모든 행의 열 수가 같고, 앞뒤에 빈 줄이 있다 | markdownlint MD055·MD056·MD058 |
| 펜스 | 코드 블록에 언어를 명시한다 | markdownlint MD040 |
| 목차 | 본문이 120줄을 넘으면 목차 절을 둔다 | ISO/IEC/IEEE 26514:2022 9.10.5 |
| 링크 | 경로와 앵커가 **생성물이 놓이는 위치 기준으로** 실재한다 | 기존 `doccheck` 링크 검사 |
| 빈 값 | `없음` 하나로 적는다. 표 셀을 비우거나 대시로 두지 않는다 | Microsoft Writing Style Guide, Tables |
| 목표 표기 | 목표가 정의된 수치에는 `(목표 <값>)`을 붙인다 — 권장 | 이 저장소의 관행 |

비율은 `n/d = p.p%` 꼴이고 소수 한 자리다. **분모 없는 백분율을 쓰지 않는다.** 0 분모는 `없음`이다. 백분율이 아닌 수치의 자릿수도 `tools/kb_lib.py`의 상수 하나에서 온다.

산문은 단정 서술형이다. `kb_lib.check_prose`를 생성 문서에도 적용한다.

**인용 구역**은 예외다. 청크 본문·라벨을 그대로 옮겨 싣는 구역은 표시로 감싸고, 그 안에서는 표·펜스·빈 값·수치·산문의 다섯을 판정하지 않는다. 생성기는 원문을 고쳐 쓸 수 없고 원본은 이미 자기 게이트를 통과했다. 문서 전체에 걸리는 제목 계층·h1·목차·링크는 구역 안에도 적용한다.

제목 줄과 링크 텍스트는 수치 표기 판정 밖이다. 이름에 든 백분율은 측정이 아니다. 측정은 전부 `kb_lib.pct`를 거친다.
