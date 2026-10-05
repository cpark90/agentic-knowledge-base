---
id: https://agentic-knowledge-base.dev/id/chunk/823b2096-4821-4c38-a7ea-87b9b6cba977
type: decision
level: concrete
title_ko: 규범 문서는 norm plane의 절 청크와 결정의 규약 줄로부터 생성된다
title: Normative documents are generated from section chunks in the norm plane and the convention lines of decisions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b, https://agentic-knowledge-base.dev/id/chunk/cb7ac129-5b94-47cd-84a8-b87e7e238efe]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5c148128-480b-40d0-a8ff-76bcd4884244
composite: {id: https://agentic-knowledge-base.dev/id/composite/5c148128-480b-40d0-a8ff-76bcd4884244, title_ko: 규범 문서의 생성, title: Generation of the normative documents}
---
**결론** — 규범 문서 넷(`STYLEGUIDE.md`·`docs/rules.md`·`docs/method.md`·`AGENTS.md`)은 생성 트리 파일이다(유저 답 Q19-b). 골격은 새 plane **`norm`**의 절 청크이고 문장은 결정의 `conventions.md` 줄이다(`p4-convention-slot`). `CLAUDE.md`만 손 문서다.

| 항목 | 내용 |
|---|---|
| plane·level | `norm`, `logical` 하나(Q21-a). `layer: methodology` |
| 클래스 | `agt:DocumentSectionChunk` — 규범 문서의 절 하나를 투영하는 청크로, 절 제목·도입문·실을 규약 줄의 순서를 담는다 |
| 디렉토리 | `kb/dev/norm/<문서 stem>/` |
| 복합체 | 문서 하나가 복합체 하나다. `title_ko`·`title`은 문서 이름, `ordered`는 절 청크 순서다. 머리 청크가 `composite:`를 선언하고 문서 도입문·범례를 본문에 담는다 |
| `heading` | 절 제목. 절 번호는 생성기가 순서로 붙이고 소스에 두지 않는다 |
| `depth` | 2 또는 3 |
| `items` | 순서 목록. 꼴은 `slug#k`, `slug#k + slug2`(둘째 결정은 링크만), 하위가 있으면 `{규약: slug#k, 하위: [slug#k…]}` |
| 묶음 | 절 청크 하나는 항목 묶음 하나(목록 또는 표)다 |
| 본문 | 묶음 앞의 산문. 표·펜스를 담을 수 있다 |
| `form` | 선택. `bullets`(기본)·`ordered`(항목마다 `1.`)·`table` |
| `columns` | `[열 머리…]`. `table`이면 필수다. 행의 `규약:` 줄은 `a \| b \| c`(바깥 파이프 없음, 링크 열 제외)이고 칸 수 불일치와 강도는 FAIL이다 |
| `link_column` | 선택. `columns`의 마지막 원소이고 그 열을 `slug#k + slug2`에서 생성한다. 없으면 생성기가 표 바로 앞에 `원본: [slug] · [slug].` 한 줄을 낸다. 그 줄은 행의 주·둘째 결정을 처음 나온 순서로 중복 없이 싣는다 |
| `continues` | 선택. `true`면 `heading`·`depth` 없는 이어짐 절 청크다. 앞 묶음 뒤의 산문과 자기 묶음을 낸다. `items`가 없으면 본문만 쓰인다. 첫 절에 둘 수 없고 번호를 소비하지 않는다 |
| 생성 순서 | 제목 → 본문 → 항목 |

- **생성기 `tools/gen_norms.py`**(developer)가 문서를 소스 트리에 내고 `//:norms_drift_test`가 재생성과 바이트로 비교한다. 생성 트리 파일 표(`pe-generated-outputs-stay-in-bazel-out`)에 셋째 행이 된다.
- **생성 문서 규약 G1~G18을 예외 없이 적용한다.** 머리 블록·목차·입력 파일 절을 갖는다. 머리 블록은 생성 트리 파일의 꼴이다(`p12-generated-document-header` — 생성 시각·지문 없음).
- **링크 위치는 정규화 규칙 하나다.** 결정 링크는 항목의 첫 문장 끝에 둔다.
- **모든 살아 있는 `규약:` 줄은 적어도 한 문서에서 쓰이고 한 문서 안에서는 한 번까지만 쓰인다.** 어느 문서도 쓰지 않은 줄(고아 줄)과 한 문서 안에서 두 번 쓰인 줄(이중 소비)은 FAIL이다. 서로 다른 문서가 같은 줄을 한 번씩 싣는 것은 허용한다.
- `chunk2kg`는 절 청크에서 그 줄을 가진 결정 복합체로 `agt:projectsConvention`을 낸다.
- **문서는 투영이고 원본은 청크다.** 원본은 결정의 `conventions.md`와 절 청크다. `CLAUDE.md`·`AGENTS.md`의 "원본" 문장은 "읽는 문서는 X이고 원본은 청크다"로 바뀐다. 이행됐다(2026-10-04).
- 순서는 `STYLEGUIDE.md`·`docs/rules.md`·`docs/method.md`가 먼저이고 `AGENTS.md`가 마지막이다(Q19-b).
