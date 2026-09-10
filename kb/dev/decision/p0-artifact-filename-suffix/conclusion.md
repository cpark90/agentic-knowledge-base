---
id: https://agentic-knowledge-base.dev/id/chunk/0b0949b2-408d-4c50-98e1-e06bb09b792b
type: decision
level: concrete
title_ko: 파일명 접미사를 고정한다
title: Fix the filename suffixes
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0027]
part_of: https://agentic-knowledge-base.dev/id/composite/0af48edc-840f-49e8-ad8b-60dfb331854d
composite: {id: https://agentic-knowledge-base.dev/id/composite/0af48edc-840f-49e8-ad8b-60dfb331854d, title_ko: 산출물 접미사가 성격과 축 위치를 알린다, title: Filename suffix announces artifact kind and axis position}
---
**결론** — 파일명이 그 파일의 성격을 알려주도록 접미사를 고정한다.

- `-ontology` — 어휘와 공리. 개체 없음. 축 위에 없는 기반
- `-rules` — 형식화. 추론 규칙. 어휘와 분리. 축 위에 없는 기반
- `-space` — 설계 공간. abstract는 출발점 선언, logical은 도착점 후보와 양립
  제약을 담는다
- `-kg` — 지식그래프. 어휘의 개체(ABox). concrete
- `-odd` — 프로젝트의 운영 조건 명세. concrete (확정된 경계)
- 실행 산출물(코드·하네스·설정)은 확장자 그대로. executable

**청크는 고유 접미사를 갖지 않는다.** head·provenance·pubinfo는 `-kg`에,
본문은 plane별 위치에 가므로 파일명은 본문의 확장자를 따른다.
**functional 단계도 별도 파일이 아니다** — 어휘 자체를 서술적으로 쓴 것이
functional이므로 온톨로지 파일 안의 주석·라벨로 존재한다.
