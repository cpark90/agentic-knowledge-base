issue (non-blocking): 빈 칸 `satisfies`:artifact→decision 은 실제 누락이다 — 코드의 `refines` 가 사다리를 잇지만 충족 주장의 자리는 비어 있다

대상: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946

본문: `p10-link-types` 는 `satisfies` 를 contract·artifact → decision 의 수평 링크로 두고, `p9-evidence-ledger` 는 검증기의 통과·실패가 그 `satisfies` 후보의 증거 기록에 (+)(−)로 적힌다고 정한다. 개발 산출물 파일 복합체는 `p7-code-links-on-file-composite` 에 따라 결정을 `refines` 하고 그 결정은 `satisfies` 를 고르지 않았으며(대안 표에 없다) `satisfies:` 키를 쓴 개발 청크는 0 이다. 그래서 실행 증거가 개발 KB 로 흘러드는 유일한 경로가 받을 링크가 없고 검증 목표 `decision-and-artifact-agree` 의 첫째·둘째 관측(충족 링크의 `suspect` 유도, 증거 극성 (−))이 대상 0 의 공허 상태다. 유일하게 찬 이웃 칸 `satisfies`:contract→decision 은 V&V 기준 `agent-catalog-complete` 가 개발 결정을 가리키는 KB 간 링크라 이 칸의 대체가 아니다.

제안: 등록부의 파일 복합체에 `satisfies` 를 `refines` 와 함께 둘지, `refines` 가 충족 주장을 겸한다고 결정하고 TIM 의 이 칸을 지울지를 orchestrator 가 정한다. 개발 쪽 수정은 developer 몫이다.

해소: 열림
