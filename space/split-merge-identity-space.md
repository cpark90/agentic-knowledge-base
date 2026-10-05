---
id: https://agentic-knowledge-base.dev/id/chunk/6fec9aaa-ca14-42fe-98d4-64bc8d15dbe8
type: agt:Space
level: logical
title_ko: 분할·병합에서 IRI를 어떻게 잇는가
title: How the IRI carries through a split or merge
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 항목을 분할·병합하면 "같은 것"인가 "새 것"인가. 정체성이 끊기면 그 IRI를 끝으로 하는 링크와 가정이 전부 고아가 된다. 언제 IRI를 유지하고 언제 새 IRI를 만드는지의 판정 기준이 변수였다. 요구 `r-012`(변경은 링크를 재판정 대상으로 만든다)에서 이 기준으로 가는 `refines`다. 같은 미결의 다른 변수인 신생의 강제 장치와 버전 IRI는 공간 `https://agentic-knowledge-base.dev/id/chunk/dda51e76-7054-460b-ba4d-3bd4c14d4e6f`가 맡는다.

이미 정해진 것 — 개체는 endurant이고 정체성은 IRI이며 변화는 `prov:wasRevisionOf` 연쇄다(`p2-temporal-identity`). 삭제하지 않고 폐기한다(`p0-deprecate-not-delete`). 확정은 `p10-split-keeps-work-identity`의 결론이다(유저 결정 Q57-a). 분할은 라벨을 잇는 조각 하나가 uuid를 승계하고 나머지는 `specializationOf`로 원본을 가리킨다. 병합은 한 uuid를 승계하고 나머지는 deprecated로 두어 승계 청크가 `supersedes`로 가리킨다. 개정은 uuid를 유지한다. 링크 IRI는 뿌리 uuid로 계산한다. 미결을 적던 당시의 안은 분할·병합이 새 IRI를 만들고 옛 IRI를 `prov:wasDerivedFrom`으로 잇는 것이었다(옛 d-0002·d-0077). `p4-chunk-split-and-merge`는 그 IRI 문장을 `p10-split-keeps-work-identity` 참조로 바꿨다(Q57-a·Q58-a). 옛 안은 청크로 존재하지 않아 후보로 세우지 않는다.

현재 상태(2026-10-06 실측) — 지속 IRI는 `id/chunk/<uuid>`이고 옛 결정 IRI(`chunk-d0001` 꼴)는 head 그래프에 158개가 남는다. 파일명(라벨 슬러그)과 IRI가 분리되어 개명과 이동은 IRI를 깨지 않는다. `specializationOf`를 가진 분할 조각은 시나리오 6개이고 `specialization` 게이트가 그 사슬을 검사한다. head 그래프의 `prov:wasRevisionOf` 트리플은 0이다. `p4-chunk-iri-is-the-anchor`의 결론은 아직 분할·병합이 `prov:wasDerivedFrom`으로 옛 IRI와 이어진다고 적는다.

답이 가르는 것 — 분할 순간 링크의 증거·확인 주체·시각이 이어지는지가 갈린다. 토큰 상한이 분할을 강제하므로 이 손실은 예외가 아니라 정상 경로다(`p10-split-keeps-work-identity`의 근거).

선택지 — 확정 후보는 `p10-split-keeps-work-identity`의 결론 하나다. 그 결론은 head에서 `r-012`를 refines한다. 미결의 선택지 A·B·C는 신생을 막는 강제 장치의 선택지라 공간 `https://agentic-knowledge-base.dev/id/chunk/dda51e76-7054-460b-ba4d-3bd4c14d4e6f`의 후보다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd
  kind: refines
status: resolved
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/57fc48aa-6091-4ee7-9763-13ddab8ac8b1
    state: confirmed
    evidence: [{kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/57fc48aa-6091-4ee7-9763-13ddab8ac8b1}]
```
