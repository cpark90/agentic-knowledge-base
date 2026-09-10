---
id: https://agentic-knowledge-base.dev/id/chunk/24801883-e1ac-4dfe-b3cf-bd29ef1576fb
type: decision
level: logical
title_ko: 코어가 도메인에 오염되면 다음 도메인이 코어를 못 쓴다
title: A domain-contaminated skeleton cannot serve the next domain
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f28573cc-2a81-4db9-9497-160a41fdd56d
---
**근거** (노트 2.11절) — 프로젝트를 넘어 재사용되는 것은 코어다. 코어에 개발 도메인의 개념(심볼 앵커, ODC 결함 유형)이 섞이면 문서 작성이나 운영 프로파일이 그것을 상속받아 무의미한 제약을 진다.

프로파일을 온톨로지 모듈로 두면 2.3절 "확장은 새 모듈 추가로만"이 그대로 적용되고, 코어 수정 여부를 기계로 검사할 수 있다 — 프로파일 모듈이 코어 클래스에 대한 공리를 추가하면 3계층에서 실패한다.

청크는 한 프로파일에 속하되 링크가 프로파일을 넘어야 문서 청크가 코드 청크를 `targets`할 수 있다. 링크까지 프로파일에 가두면 한 프로젝트의 그래프가 프로파일 수만큼 조각난다.
