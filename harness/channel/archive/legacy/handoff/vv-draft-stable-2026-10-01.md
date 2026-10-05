---
from: hci
source: vv-draft-stable-2026-10-01.md
verdict: apply
status: closed
---

# V&V 21건의 stable 전이 (2026-10-01 승인)

유저 답: *"1."* — **검증 목표 8 · 합격 기준 8 · 시나리오 5(세 청크 복합체) 전부 stable.**

## 파급효과

- **정지 규칙이 규범이 된다.** `verification-round-stop-rule` 이 stable 이면 orchestrator 는 두 라운드 정체 시 반드시 멈추고 채널로 되돌린다. 2026-09-29·30 의 정지는 관측이었고 이제부터는 규칙이다.
- 감사 보고서의 "승인된 목표" 분모가 바뀐다 — 검증 목표 41 전부가 stable 이 된다.
- 상태 전이는 frontmatter 한 줄씩 21건이고 본문·링크·IRI 는 그대로다. 도장(`verified`)은 쓰기 권한 역할(vnv)이 `endorse` 로 붙인다.
- 닿지 않는 것: 케이스·검증기·판정 주석(이미 stable 이거나 도구 생성). 관측 수단 미확정 둘(P17·P20)은 이 전이와 무관하게 남는다.

## 반영 계획

1. **vnv — 상태 전이 21.** `kb/vv/goal/` 8 · `kb/vv/criteria/` 8 · `kb/vv/scenario/` 5 복합체(15 청크)의 `status: draft → stable`. 복합체는 세 청크를 함께 올린다 — 부분만 stable 인 복합체를 만들지 않는다.
2. **vnv — 도장.** `bazel run //tools:endorse` 로 21건에 `verified` 를 붙인다. 근거는 이 승인이다.
3. **orchestrator — 규범 반영.** 정지 규칙을 `AGENTS.md` 의 작업 절 또는 `docs/method.md` 의 검증 절에 한 문장으로 적는다 — "연속 두 라운드에서 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않고 채널로 되돌린다". 목표 청크가 원본이고 문서는 인용이다.
4. **vnv — 감사 확인.** `bazel build //kg:audit` 의 "위험에서 파생된 목표" 절이 전이를 반영하는지 본다.

**검색 키워드**: `draft` · `stable` · `verification-round-stop-rule` · `정지 규칙` · `라운드` · `endorse` · `위험에서 파생`.

## 확인 못 한 것

- 시나리오 복합체 5 의 세 청크가 전부 draft 인지(16 파일 중 하나는 `risk-grade-scale` 척도다). vnv 가 전이 전에 센다.
- 정지 규칙의 "신규 결함 수"의 정의처. 목표 본문이 적었는지, 감사의 라운드 표가 그 수를 어떻게 세는지 확인하지 않았다.

## 판정

`apply` 다. 승인된 입력의 산출이고 하나는 이미 작동했다. 복합체를 통째로 올리는 것이 유일한 주의점이다.

## 반영 확인 (hci, 2026-10-02)

인수 기록으로 돌아왔다 — 31 파일(목표 8 · 기준 8 · 시나리오 5 부류 × 3 청크) stable + vnv 도장. 정지 규칙의 규범 문장은 `docs/method.md` §11 에 들어갔다.
`risk-grade-scale` 1건은 승인 목록 밖이라 `draft` 로 남았고 별도 항목으로 올렸다.
