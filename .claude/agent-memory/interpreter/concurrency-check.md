# 분담 보고를 받으면 동시 한도를 대조한다 (2026-10-25)

- 한도: `kg/catalog-kg.ttl`의 역할별 `agt:maxConcurrent`(최대 동시 수)는 각 1(hci는 0)이고, ODD `id:cond-concurrent-agents`(동시 에이전트 수)는 0~5다. ODD의 기계 검사(cmd)는 카탈로그 합만 보므로 실제 동시 dispatch 초과를 잡지 못한다.
- 사건: status 0305(작업자 다섯 — fork 둘·developer 둘·vnv)를 hci가 knowledge 0306으로 지적했고, orchestrator가 (1) 한도 안으로 줄였다(0307). 앞선 위반 둘도 확인됐다 — 0287의 6a(developer 둘)와 0262의 판정자 세션 20개 동시.
- 규칙: fork와 판정자 세션도 dispatch이므로 센다(0307). status·task의 분담 문장에 "둘, 동시"나 세션 수가 나오면 역할별 1과 전체 5를 대조하고, 넘으면 knowledge로 넘긴다. 한도를 바꾸는 것은 ODD 개정이라 유저 승인이다.
