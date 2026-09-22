---
from: orchestrator
kind: notice
status: open
targets: [kb/dev/decision/p12-generated-document-header/, kb/dev/decision/p12-generated-document-form/, kb/dev/decision/p12-generated-documents-are-gated/, docs/roadmap.md]
---

# 연결 성분 6 → 4 — 원인을 갈라 고칠 수 있는 둘을 이었다 (2026-09-22)

유저 항목 [`connected-components-observations-2026-09-19`](../connected-components-observations-2026-09-19.md)이 "관측이 연결 성분을 늘린다"로 열려 있다. 그 판단을 기다리는 동안 성분의 내역을 실측해 **관측이 아닌 것**을 갈라냈다.

## 실측 (2026-09-22, 살아 있는 청크 753)

계산의 정의는 `tools/metrics.py:104-116`이다. 간선은 `LINKS` 15종과 `agt:hasDirectPart`와 복합체 형제이고 방향을 무시한다. `deprecated`와 청크가 아닌 대상은 간선이 되지 않는다.

| 성분 | 크기 | 정체 | 원인 |
|---|---|---|---|
| 1 | 733 | 본체 | 해당 없음 |
| 2 | 10 | `r-028` + p12 생성문서 형식·게이트 묶음 | 새 요구가 본체의 어떤 요구와도 이어지지 않았다 |
| 3 | 7 | `r-027` + p12 머리 블록 묶음 | 같은 원인 |
| 4·5·6 | 각 1 | 관측 — `kb/vv/run/` 2 · `kb/dev/memory/` 1 | `assumes`의 대상이 가정 개체(청크 아님)라 간선이 되지 않는다 |

2026-09-13에 성분 1이었던 것은 그 시점 그래프에 memory plane이 없었기 때문이다. 같은 커밋(`18840a8`)이 "Close adoption stage 1 (one connected component)"라는 제목으로 memory를 그래프에 처음 넣고 관측 1건을 커밋했다.

## 반영

성분 2·3은 2026-09-21에 orchestrator가 만든 것이고 링크 하나씩이면 붙는다. 결정 셋(`p12-generated-document-header`·`p12-generated-document-form`·`p12-generated-documents-are-gated`)의 결론에 `serves → documents-are-generated`(`973f5595`)를 더했다. `serves`는 TIM 허용 칸 `("serves","decision","requirement")`에 있고 수준·KB 규칙을 통과한다. 사후에 잇는 링크이므로 `restored`로 표시해 복원 비율에 정직하게 센다.

**성분 6 → 4.** `bazel test //...` PASS.

`docs/roadmap.md`의 1단계 칸이 "연결 성분 5(목표 1)"와 "연결 성분 1 ○ … **1단계 통과**"를 동시에 적고 있었다. 수치가 세 번 낡았고 서로 모순이라 `d-0075`대로 생성물 인용으로 바꿨다.

## 유저 판단 항목에 넘기는 근거

남은 셋은 구조적이다. hci가 유저 lane 항목에 덧붙일 실측이다.

- **TIM 15칸 중 `memory`를 출발·도착으로 갖는 칸이 0개다**(`tools/kb_lib.py:529-534`). 관측이 어떤 링크를 갖든 매트릭스 밖 칸이 된다.
- 관측은 `process:vv_run`·`process:assume_check`의 생성물이고 append-only다(`r-026`). 사람이 사후에 frontmatter를 고치는 길이 없고 **생성기가 링크를 계산해야 한다.**
- 항목의 선택지 2(본문 인용으로 잇기)는 **추출기 수정이 전제다.** `cites`는 frontmatter 링크 키 9종에 없고 본문 추출은 `d-NNNN` 정규식 하나뿐이다(`tools/extract_refs.py:56`). 실행 기록이 본문 표에 적은 케이스 이름은 링크가 되지 않는다.
- 구조 규칙만 보면 `kb/vv/run/`의 실행 기록이 개발 KB의 concrete 청크를 `verifies`할 수 있고 판정 관측은 `refines`·`serves`가 가능하다. 그러나 위 두 제약이 남는다.
- 같은 관측 3건이 CQ20 후방 추적의 잔여이기도 하다(682/685 = 99.6%). 연결 성분과 후방 추적이 같은 답으로 닫힌다.

부수로 확인한 것 하나. `-space` 청크 2개는 `//kg:metrics`의 입력이 아니라 성분 계산 밖이다(`kg/BUILD.bazel`의 `data` 넷에 `//space:design_space`가 없다). 넣으면 두 개체가 `agt:lineCount`를 가져 청크로 세어지고 성분이 8로 는다. `-space`는 청크가 아니라 A-Box이므로 지금 배치가 맞다.
