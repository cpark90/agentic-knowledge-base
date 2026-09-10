---
id: https://agentic-knowledge-base.dev/id/chunk/764abb14-5376-4fa9-aa49-44c89752f524
type: decision
level: logical
title_ko: 라벨 목록 읽기가 본문 적재 없이 성립해야 한다
title: Reading a label list must not require loading any body
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3
---
**근거** (노트 4.9절)

- 읽기 응답이 라벨 목록을 기본으로 하려면(4.4절·5.3절) **라벨·상태·링크를
  얻는 데 본문 적재가 없어야** 한다. 메타데이터를 전부 `-kg`에 두는 것이 그
  조건이다.
- assertion의 위치를 plane마다 다르게 두는 이유는 **각 도메인이 이미 안정적인
  식별자를 갖고 있기 때문**이다(5.1절). 코드에는 심볼이, 산문에는 파일이
  있으므로 새 저장 형식을 만들지 않고 IRI 해석만 plane별로 정의한다.
