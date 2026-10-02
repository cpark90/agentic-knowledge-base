---
id: https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc
type: decision
level: concrete
title_ko: 함수의 정체성은 등록부의 이름→uuid 대응이 원본이고 개명·삭제는 등록부 편집이다
title: A function's identity is the registry's name→uuid mapping, and rename or deletion is a registry edit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/fa336de6-3b07-45c0-9b66-b41ce2cdbcba
composite: {id: https://agentic-knowledge-base.dev/id/composite/fa336de6-3b07-45c0-9b66-b41ce2cdbcba, title_ko: 함수 정체성의 등록부, title: The registry of function identity}
---
**결론** — 함수 청크의 uuid는 생성되지 않는다. 파일마다 **등록부**(사이드카)가 `한정 이름 → uuid`를 갖고 그것이 정체성의 원본이다. 이름은 라벨, `contentHash`는 버전이다(`p10-split-keeps-work-identity`와 같은 사상).

| 상황 | 추출기의 판정 |
|---|---|
| 이름이 등록부에 있다 | 그 uuid. 본문이 바뀌면 해시만 바뀐다 |
| 새 이름이 있고, 사라진 이름의 **정규화 본문 해시와 같다** | **개명 제안** — 등록부를 자동으로 고치지 않고 `FAIL [extract]`로 "등록부에서 X→Y로 개명하라"를 안내한다. 정체성 변경은 사람의 편집이다 |
| 새 이름이 있고 대응이 없다 | 새 uuid를 등록부에 **자동 추가**한다 — 신설은 정체성 변경이 아니다 |
| 등록부에 있는데 소스에 없다 | FAIL. 삭제는 등록부에서 지우는 명시 행위다 |

Unison은 정의의 해시를 정체성으로 쓰지만 이 저장소의 정체성은 uuid이고 해시는 버전이다 — 그래서 해시는 개명을 **제안**하는 데만 쓰고 정체성을 정하지 않는다. 등록부는 생성물이 아니라 저작물이며 파일 복합체의 링크 선언도 같은 자리에 둔다.
