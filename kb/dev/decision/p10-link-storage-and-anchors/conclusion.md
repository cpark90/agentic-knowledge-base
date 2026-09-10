---
id: https://agentic-knowledge-base.dev/id/chunk/6c1bb389-1c3e-4381-a693-d0d7020f79c4
type: decision
level: concrete
title_ko: 링크는 산출물 밖에 저장하고 앵커는 청크 ID다
title: Links live outside artifacts; the anchor is the chunk ID
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0105]
part_of: https://agentic-knowledge-base.dev/id/composite/c1ce996d-dc84-45c5-b567-a9da42421774
composite: {id: https://agentic-knowledge-base.dev/id/composite/c1ce996d-dc84-45c5-b567-a9da42421774, title_ko: 링크는 산출물 밖에 저장하고 앵커는 청크 ID다, title: Links live outside artifacts; the anchor is the chunk ID}
---
**결론** — **링크는 산출물 안에 쓰지 않는다.** 별도 링크 모델에 두고, 양 끝은 각 plane의 네이티브 앵커(5.1절)로 가리킨다. 링크 모델은 A-Box이므로 **`-kg` 파일**이고, 시각화와 질의는 이 파일 위에서 동작한다.

**앵커는 청크 ID다** (4.4절). 각 plane은 청크 ID를 자기 분야의 네이티브 식별자로 해석한다 — 산문 계열은 파일 경로 또는 standoff 앵커, 코드 계열은 심볼 식별자. 청크 안에서의 위치가 필요할 때만 **selector를 다중화**한다.

plane마다 **앵커 해석기**를 둔다. 앵커 문자열을 받아 실제 산출물의 원자 단위를 찾아 주는 것이 전부이며, 새 plane이나 새 형식을 추가할 때 해석기만 추가한다. **링크 모델은 앵커가 무엇을 가리키는지 모른다.**
