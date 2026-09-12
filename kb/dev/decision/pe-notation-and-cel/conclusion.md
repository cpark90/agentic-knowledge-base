---
id: https://agentic-knowledge-base.dev/id/chunk/52882515-946a-4d03-a4a2-938489b1a203
type: decision
level: concrete
title_ko: 수준별 본문 표기는 정해져 있고 판정식은 네 곳 전부 CEL 하나다
title: Per-level body notation is fixed, and every judgement expression in all four places is CEL
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249, https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
composite: {id: https://agentic-knowledge-base.dev/id/composite/ffcf1fe8-be2a-4a21-b532-ff6f7bb4b727, title_ko: 수준별 표기와 CEL, title: Per-level notation and CEL}
part_of: https://agentic-knowledge-base.dev/id/composite/ffcf1fe8-be2a-4a21-b532-ff6f7bb4b727
---
**결론** — 수준별 본문 표기 (노트 부록 E.3):

| level | 개발 KB | V&V KB |
|---|---|---|
| functional | EARS 문장 | 검증 목표 산문 |
| abstract | 변수 선언 YAML + plane별 표기 (IDL / 결론·근거·대안) | `scenario` parameter + actor |
| logical | 범위·제약 YAML + CEL / `schema`는 JSON Schema 자체 | `keep(범위)` + 기준 청크(CEL) + `cover()` |
| concrete | 값 레코드 + 표본 근거 | `keep(고정값)` — 생성 결과 |
| executable | 앵커 (소스에서 추출한 stub) | 검증기 앵커 + 계산 필드 |

판정식은 네 곳(ODD 판정 방법·가정·합격 기준·후보 제약) 전부 **CEL** 하나. OpenODD 식과 `keep()`은 표준 표기를 쓰되 실행 시 CEL로 변환된다. 이 저장소: CEL 평가기는 도입 5단계 (유저 결정 Q9).

외부 조사로 채운 세부 (cel-spec langdef, cel-go, 2026-09-11) — CEL은 메모리 안전·부작용 없음·종료 보장·강타입이며 같은 환경에서 결정론적으로 값 또는 오류를 낸다. `when`의 세 값 중 "판정 불가"는 cel-go의 **부분 평가**(`PartialVars`·`OptTrackState`)로 미지 속성을 잔여 식(residual AST)으로 남기는 것에 대응한다 — 어떤 ODD 속성이 빠져 판정 불가인지가 잔여 식으로 드러난다.
