---
from: hci
status: approved
targets: [kb/dev/decision/p8-two-verification-targets/conclusion.md, defs/kb.bzl, kb/dev/requirement/r-025-verify-product-and-agent.md, kb/vv/goal/agent-and-product-verified.md]
---

# 에이전트 검증의 `verifies` 도착점 — 결정과 규칙이 어긋난다 (2026-09-22 중계)

원본: [`agents/orchestrator-agent-verification-target-2026-09-21.md`](agents/orchestrator-agent-verification-target-2026-09-21.md)

## 질문

에이전트 검증의 `verifies`는 무엇을 가리키는가. **결정은 하네스·스코프 개체라 하고 규칙은 개발 KB 청크만 허용한다.**
요구 `r-025`(제품과 에이전트 둘 다 검증한다)가 성립하려면 둘 중 하나를 고쳐야 한다.

어려운 이유는 양쪽 다 확정이고 성격이 다르다는 데 있다. 규칙을 넓히면 **검사 약화라 유저 승인 사항**이고, 결정을 좁히면
"검증 대상 둘"이라는 설계의 한 줄이 바뀐다.

## 이미 정해진 것

- `p8-two-verification-targets/conclusion.md` 끝줄 — "제품 검증은 `decision`·`contract`의 logical 기준을, 에이전트 검증은 **하네스·스코프 개체**를 검증한다". hci가 원문을 확인했다.
- `defs/kb.bzl:73-79` — `verifies`의 주어는 V&V KB 청크뿐이고 **대상은 개발 KB 청크**이며 수준이 같아야 한다. 세 검사가 분석 시점에 `fail()`로 막는다. hci가 코드를 확인했다.
- 하네스·스코프 개체(`kg/catalog-kg.ttl`의 `id:h-akb`·`id:scope-*`)는 청크가 아니라 A-Box 개체다. `ChunkInfo`가 없어 지금 규칙의 대상이 될 수 없다.
- 검사를 약화하는 변경은 유저 승인 사항이다(`STYLEGUIDE.md` §2·§7).

## 현재 상태 (실측 2026-09-21~22)

- `r-025`는 **사람 확인**으로 분류돼 목표와 기준만 있고 케이스가 없다(`kb/vv/goal/agent-and-product-verified.md`). 에이전트 쪽 사슬은 **0**이다.
- `audit` 검증 현황 — 검증 대응물 있는 요구 **35/35**, 사슬 목표 33, 케이스까지 이어진 목표 **28**. 차이 5 중 하나가 이 항목이다.
- 에이전트 검증의 판정 수단 가운데 **산출물 품질은 이미 게이트가 잰다**(`writer`·`endorse`·`gendoc`). **인지능력의 판정 수단은 저장소에 없다.**

## 답이 가르는 것

- **규칙을 넓히면** `verifies` 대상에 A-Box 개체가 들어온다. `defs/kb.bzl`이 청크 타깃 외에 IRI를 알아야 하고, 개체에는 수준이 없어 수준 일치 검사를 적용할 수 없다. TIM의 `verifies` 칸이 하나 는다.
- **결정을 좁히면** 에이전트 검증도 개발 KB 청크를 도착점으로 삼는다. 역할·스코프를 정한 결정이나 요구 `r-019`(읽기·쓰기 집합 기록)가 그 자리다. 검증 대상 둘이라는 구분은 남고 도착점 종류만 하나가 된다.
- **두면** `r-025`는 영구히 사람 확인이고, 케이스까지 이어진 목표 비율의 상한이 100% 아래에 고정된다.

## 선택지

1. **결정을 좁힌다** (orchestrator 권장). 도착점을 개발 KB 청크로 한다. 규칙은 그대로다. 비용: 결정 하나 개정(orchestrator, `supersedes`로 잇는다) + 에이전트 쪽 사슬 저작(vnv). 근거는 산출물 품질 게이트가 이미 그 자리를 잰다는 실측이다.
2. **규칙을 넓힌다.** 카탈로그 개체를 `verifies` 대상으로 허용한다. 비용: `defs/kb.bzl` 개정과 **검사 약화 승인** + 개체 참조 방식 설계 + 수준 검사의 예외. 인지능력 판정 수단이 생기면 필요해지는 형태다.
3. **지금은 둔다.** `r-025`를 사람 확인으로 유지하고 인지능력 판정 수단이 생길 때 다시 본다. 비용: 케이스 이어진 비율의 상한 고정.

## 답
1.
이 답과는 별개로 이 저장소의 하네스도 저장소에서 다루는 내용이 개선됨에 따라 진보된 지식들을 반영하여 개선해야함.
