---
id: https://agentic-knowledge-base.dev/id/chunk/b1b61b11-010b-4e6f-926c-0af3d670c455
type: decision
level: logical
title_ko: 검토된 plane 후보 — ui만 남고 나머지는 하위 클래스나 다른 장치로 흡수
title: Reviewed plane candidates: only ui remains, the rest are absorbed
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ab95f777-16da-41c6-8b1d-5f51f1484840
---
**대안** — 검토된 후보와 판정 (5.5절).

| 후보 | 판정 |
|---|---|
| 테스트 코드 | 실행·테스트 = `artifact` 하위 클래스 |
| 빌드·배포 스크립트 | 실행 = `artifact` 하위 클래스 |
| 인프라 정의 (IaC) | 실행 + 환경 상태 대조 = `artifact` 하위 클래스. 환경 상태는 ODD 환경 조건과 대조 |
| 설정 파일 | 스키마 검사 = `schema` 하위 클래스 |
| 운영 지표 | 관측 = `memory` 하위 클래스 |
| 데이터 (픽스처·마이그레이션·샘플셋) | 스키마 검사 + 통계적 검증(분포·결측). `schema` 하위 클래스로 시작하되 통계 검증이 주가 되면 plane 후보 |
| 대응 절차 (runbook) | 절차 실행 성공 = `decision` 하위 클래스 `agt:Runbook`. 판정은 실행 기록으로 |
| 인시던트·사후분석 | 관측은 `memory`, 결론은 `decision` — 두 plane의 복합체 |
| 보안·라이선스·규제 정책 | plane이 아님. ODD 조건 또는 온톨로지 공리 |
| 용어집 | plane이 아님. 온톨로지 자체 |
| 요구사항 | 이해관계자 합의 — 기존과 다름. **승격됨** |

`[안]` **화면 설계(레이아웃·흐름)** — 시각·사용성 판정, 즉 사람의 인지 평가로
기존 어디와도 다르므로 plane 후보 `ui`. 판정 도구가 없으므로 `decision`처럼
유저 승인이 조건이 된다. **미확정으로 남는다.**
