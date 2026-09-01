---
iri: https://agentic-knowledge-base.dev/id/chunk-d0039
plane: decision
level: concrete
label_ko: 편향마다 구조적 완화 장치를 고정한다
label_en: Each bias is bound to a structural mitigation
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 1.2절의 성질 각각에 이 체계의 어느 장치가 대응하는지를 표로
고정한다. 완화는 프롬프트가 아니라 자료구조·규칙·체계 밖 판정으로 한다.

**근거** (노트 1.5절) — 편향 / 발현 / 구조적 완화
- **학습자료 종속** — 낯선 이름을 아는 것으로 오인 → 0.3절 접두어,
  온톨로지 밖 어휘 거부
- **과도한 순응** — 근거 없이 후보 하나를 고름 → Part VII, 후보가 여럿인
  상태가 정상
- **최신성 편향** — 마지막으로 본 청크를 과대평가 → 5.3절 라벨 목록이
  순서를 갖지 않음. 순서는 구성체가 결정
- **첫 정보 고착** — 처음 읽은 결정에 묶임 → 후보 링크가 남아 있는 한
  재검토 가능
- **확인 편향** — 자기 결정과 일치하는 증거만 봄 → `verifies` 링크가 없는
  결정이 커버리지 지표에서 드러남
- **자기 검토 실패** — 자기 출력을 검증했다고 믿음 → 검사 게이트는 에이전트
  밖. 규칙과 shape가 판정
