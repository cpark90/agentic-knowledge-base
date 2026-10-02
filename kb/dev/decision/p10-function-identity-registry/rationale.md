---
id: https://agentic-knowledge-base.dev/id/chunk/1f33f219-a2fa-43e8-b3b6-8c4f735139ee
type: decision
level: logical
title_ko: 이름에서 정체성을 떼지 않으면 개명이 삭제와 신설로 보여 링크와 이력이 끊긴다
title: Unless identity is detached from the name, a rename looks like deletion plus creation and severs links and history
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/fa336de6-3b07-45c0-9b66-b41ce2cdbcba
---
**근거** — 생성물의 uuid를 이름에서 만들면 개명이 곧 새 uuid다. 그러면 그 청크를 가리키던 것(복합체의 부분 목록·검증기의 대상·관측)이 끊기고 이력이 둘로 갈린다 — 유저가 걱정한 "잦은 변경에 약한 형태" 그 자체다. 정체성을 이름 밖에 두어야 개명이 라벨 변경이 된다.

해시로 정체성을 정하지 않는 까닭은 둘이다. 본문을 한 글자 고치면 해시가 바뀌므로 해시는 버전이지 정체성이 아니고, 서로 다른 함수가 같은 본문을 가질 수 있다(짧은 래퍼). 해시가 할 수 있는 것은 "사라진 이름과 같은 본문의 새 이름"을 개명 후보로 **제안**하는 것까지다.

개명을 자동으로 확정하지 않는 까닭은 정체성 변경이 사람의 판단이기 때문이다. 같은 본문의 새 이름이 개명인지 복제인지는 저작자만 안다. 반대로 신설을 자동으로 등록하는 까닭은 새 uuid를 만드는 것이 아무것도 끊지 않기 때문이다.

등록부를 사이드카로 두는 까닭은 소스 파일에 uuid 주석을 심으면 코드 편집이 정체성 편집이 되고, 그것이 곧 tangle의 문제(원본 둘)이기 때문이다.
