---
id: https://agentic-knowledge-base.dev/id/chunk/b6912d83-519c-4a03-8457-c8ba3efd5d55
type: decision
level: logical
title_ko: 자연어 블록 길이 제약의 확정 형태가 42줄 청크이고 편집기가 그것을 강제한다
title: The 42-line chunk is the settled form of the natural-language length constraint the editor enforces
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/922f75fe-58e0-4964-b79b-b9897ac35ce5
---
**근거** (노트 13.4절·12.2절)

- 자연어 블록 길이 제약의 **확정 형태가 42줄 청크**(Part IV)다. "코어 + 중복을
  포함한 상세"라는 구성은 청크의 **라벨 + 본문**과 같다 — 편집기가 강제하는
  것이 바로 이 형태다.
- 라벨 없는 청크는 라벨 목록으로 읽히지 않으므로 사실상 없는 것이다. 그래서
  경고가 아니라 저장 금지다.
- plane·level은 head 그래프가 요구한다. 나중에 채우면 그 사이에 잘못된 툴
  표면으로 읽힌다.
- **사람이 나중에 적는 provenance는 빠진다.** 링크를 만들 수 있던 순간에
  만들지 않으면 남는 것은 사후 복원뿐이다(9.3절).
- 본문과 링크를 한 화면에 두면 "청크는 자기 링크를 모른다"(4.3절)가 곧
  무너진다 — 편집 중에 링크가 본문의 일부처럼 보이기 때문이다.
