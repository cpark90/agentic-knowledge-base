---
iri: https://agentic-knowledge-base.dev/id/chunk-d0027
plane: decision
level: concrete
label_ko: 산출물 접미사가 성격과 축 위치를 알린다
label_en: Filename suffix announces artifact kind and axis position
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 파일명이 그 파일의 성격을 알려주도록 접미사를 고정한다.

| 접미사 | 산출물 | 축 위의 위치 |
|---|---|---|
| `-ontology` | 어휘와 공리. 개체 없음 | 없음 — 기반 |
| `-rules` | 형식화. 추론 규칙, 어휘와 분리 | 없음 — 기반 |
| `-space` | 설계 공간. 후보 링크 집합 | abstract, logical |
| `-kg` | 지식그래프. 어휘의 개체(ABox) | concrete |
| `-odd` | 프로젝트의 운영 조건 명세 | concrete (확정된 경계) |
| (확장자) | 실행 산출물 — 코드·하네스·설정 | executable |

**근거** (노트 0.2절)
- 접미사만 보고 그 파일이 어휘를 담는지 개체를 담는지, 후보를 담는지
  확정을 담는지 판정할 수 있어야 스코프와 검사 게이트를 파일 단위로 건다.
- 어휘(`-ontology`)와 추론 규칙(`-rules`)을 분리하는 이유는 둘의 갱신
  주기와 판정 방식이 다르기 때문이다. 둘 다 축 위에 있지 않다(0.1절).
- **청크는 고유 접미사가 없다.** head·provenance·pubinfo는 `-kg`에, 본문은
  plane별 위치에 가므로 파일명은 본문의 확장자를 따른다(4.3절).
- **functional 단계는 별도 파일이 아니다.** 어휘 자체를 서술적으로 쓴 것이
  functional이므로 온톨로지 파일 안의 주석·라벨로 존재한다.
