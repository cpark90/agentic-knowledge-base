---
id: https://agentic-knowledge-base.dev/id/chunk-d0105
type: decision
level: concrete
title_ko: 링크는 산출물 밖에 저장하고 앵커는 청크 ID
title: Store links outside artifacts, anchored by chunk ID
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크는 **산출물 안에 쓰지 않는다.** 별도 링크 모델(A-Box이므로
`-kg` 파일)에 두고, 양 끝은 각 plane의 네이티브 앵커로 가리킨다. **앵커는
청크 ID**이고, plane마다 **앵커 해석기**를 둔다.

**근거** (노트 8.5·8.9절)
- 산출물을 열지 않고 링크를 만들고 질의할 수 있다.
- 산출물 형식마다 링크 표기를 따로 정하지 않아도 된다.
- 링크 모델의 저장·시각화·검사를 산출물과 독립적으로 교체할 수 있다.
- 앵커 해석기는 앵커 문자열을 받아 실제 산출물의 원자 단위를 찾아 주는
  것이 전부다. 새 plane이나 새 형식은 **해석기만 추가**하면 되고, 링크
  모델은 앵커가 무엇을 가리키는지 모른다.
- 각 plane은 청크 ID를 자기 분야의 네이티브 식별자로 해석한다 — 산문
  계열은 파일 경로 또는 standoff 앵커, 코드 계열은 심볼 식별자. 청크
  안에서의 위치가 필요할 때만 **selector를 다중화**한다.
- 시각화와 질의(8.7절)는 이 `-kg` 파일 위에서 동작한다.
