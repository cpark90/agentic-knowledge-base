---
id: https://agentic-knowledge-base.dev/id/chunk/85beb0c7-fa2e-4118-a18c-6f5f7b4ad174
type: decision
level: logical
title_ko: 경로와 줄 번호를 앵커로 쓰면 편집마다 드리프트한다
title: Path-plus-line anchors drift on every edit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5e2184c3-67a9-4745-b0c3-65e8c3f69fd6
---
**근거** (노트 4.8절, 5.1절)

- 파일 추상은 지식의 주소를 **"경로 + 줄 번호"로 붕괴시킨다**(5.1절). 그런
  앵커는 본문을 한 줄 고칠 때마다 어긋나고, 어긋난 링크는 없는 링크보다
  해롭다.
- IRI를 앵커로 두면 **드리프트가 발생할 수 있는 유일한 사건이 IRI 집합의
  변화**, 즉 분할·병합으로 줄어든다. 그 사건은 4.10절이 명시적으로 다루고
  `prov:wasDerivedFrom`으로 추적되므로 재판정 큐가 유한하다.
- 재판정(9.6절)의 트리거도 같은 자리에 있다 — 본문 해시가 바뀌면 그 IRI를
  끝으로 하는 링크가 `suspect`가 된다 (4.3절 해시 IRI).
