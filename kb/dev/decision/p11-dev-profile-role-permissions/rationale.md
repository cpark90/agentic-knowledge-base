---
id: https://agentic-knowledge-base.dev/id/chunk/e6ec0ff2-3568-413f-b1f2-0c81edab76fd
type: decision
level: logical
title_ko: 어휘와 경계의 편집권은 설계에, V&V KB 쓰기는 검증에 묶인다
title: Editing the vocabulary and the boundary belongs to design; writing the V&V KB belongs to verification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4dbb535c-ea05-4b67-accf-29c2ef7f6ee3
---
**근거** (노트 11.2절)

- **design이 T-Box와 ODD 편집 권한을 갖는다.** 어휘와 경계의 변경은 설계
  판단이고, 구현 역할이 만지면 모든 청크의 가정이 딛고 선 바닥이 조용히
  움직인다.
- **V&V가 검증 역할 `artifact`(RW)와 `annotation`(W)을 갖는다.** V&V KB 쓰기가
  개발 역할과 분리되어야 만든 쪽이 판정 기준을 고치는 일이 구조적으로 막힌다
  (Part VIII). 개발 산출물 쪽은 읽기와 logical 기준 참조에 그친다.
- **write 권한이 겹치지 않는다** — `decision`은 orchestrator·design,
  `artifact`는 developer, `annotation`은 V&V. 이 비겹침이 10.6절 입력 검증의
  검사 항목이다. claim은 제안만 하고 할당하지 않는다.
- 유저 결정 C4 — 이 저장소는 이 카탈로그의 **부분집합**만 쓰고 developer가
  design을 겸한다. 부분집합 사용은 프로젝트 재량이며, 카탈로그 자체는 아홉
  역할로 남는다(겸임하더라도 write 비겹침 검사는 겸임된 역할 쌍에 적용된다).
