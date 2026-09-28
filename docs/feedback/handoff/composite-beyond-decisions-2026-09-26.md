---
from: hci
source: composite-beyond-decisions-2026-09-26.md
verdict: apply
status: open
---

# 결정 밖의 복합체 — 도구를 고친다 (2026-09-26 승인)

유저 답: *"1."* — **도구를 고친다.** `kb_chunk` 단위 청크끼리 복합체를 만들 수 있게 한다. 결정을 좁히지 않는다.

## 파급효과

- 결정 `p4-all-knowledge-is-composite` 의 표가 **전부 성립할 수 있게 된다** — 요구의 관심사별 복합체, 합격 기준의 기준 집합, 시나리오의 세 청크, 검증기의 케이스 열.
- 생성 복합체 246 중 결정 242 뿐인 상태가 풀린다. 손으로 쓴 `kg/composite-kg.ttl` 의 42건과 생성물이 갈리는 문제도 여기서 정리된다.
- `artifact` plane 3(검증기)이 첫 대상이다. 복합체가 서면 `co:List` 순서가 tangle 의 입력이 된다.
- 생성 BUILD 가 바뀐다 — 새 규칙이 묶음을 선언하므로 `//:build_drift_test` 가 재생성을 요구한다.

## 반영 계획

1. **developer — 묶음 규칙.** `defs/kb.bzl` 에 `kb_composite`(또는 `kb_chunk` 의 묶음 인자)를 만든다. 한 액션이 여러 청크 파일을 받아 `chunk2kg --fragment` 에 함께 넘긴다 — 지금 실패의 원인이 **파일 하나 = 묶음 하나**라는 가정이다.
2. **developer — `chunk2kg`.** 묶음 안에서 `part_of` 대상 복합체가 선언되는지 보는 검사를 유지하되, 묶음의 단위를 파일이 아니라 **액션의 입력 집합**으로 읽는다.
3. **developer — `gen_build`.** 복합체를 가진 청크 묶음을 새 규칙으로 생성한다. 결정(`kb_decision`)과 같은 형식이다.
4. **vnv — 검증기 복합체.** `artifact` 3을 `co:List` 로 묶고 부분의 plane·level 동질성을 확인한다.
5. **orchestrator — 손 기록의 정리.** `kg/composite-kg.ttl` 의 42건 가운데 생성 경로로 옮길 수 있는 것을 옮기고, 남는 것(요구의 관심사 묶음 등)은 그 이유를 배너에 적는다.

**검색 키워드**: `복합체` · `composite` · `part_of` · `hasDirectPart` · `co:List` · `fragment` · `kb_decision`.

## 확인 못 한 것

- 새 규칙이 `kb_decision` 과 통합될 수 있는지. 결정은 세 청크 고정이고 일반 복합체는 가변이라 별 규칙이 자연스러울 수 있다.
- 부분의 plane·level 동질성 예외(결정 복합체)가 일반 복합체에도 필요한지. `composite-heterogeneous.rq` 가 지금 결정만 예외로 둔다.
- 손으로 쓴 42건 중 몇 건이 옮겨지는지.

## 판정

`apply` 다. 답이 명확하고, 규칙이 지식의 모양을 제한하던 상태를 푸는 쪽이다 — 2026-09-26 의 정의문 판정("규칙은 실행 자리를 이름 짓는다")과 같은 방향이다.
