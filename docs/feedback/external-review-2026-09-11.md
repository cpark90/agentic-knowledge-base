---
from: hci
status: approved
targets: [docs/references.md, docs/glossary.md, docs/roadmap.md]
---

# 진행 검토와 외부 조사 보충 (2026-09-11)

유저 요청: "현재까지 진행된 내용 검토하고 세부적인 내용 외부에서 조사해서 채워줘."

## 1. 진행 검토 — 2026-09-10 계획(0~7)과 그 뒤

| 단계 | 상태 | 남은 것 |
|---|---|---|
| 0~1 답 기록·번호 동기화 | 완료 | — |
| 2 대안 청크 | 완료 182/182 | 대안 필수 shape(그래프에 역할이 없어 규약) |
| 3 v4·v5 델타 재도출 | 완료 결정 +37, 요구 +7 | 부록 B 사례는 `[확정]` 없음 — 도입 시 사례 프로젝트로 |
| 3′ 링크 어휘 개정 | 완료 (`when`·증거 기록·`serves`) | 링크 개체 0 — 3단계 |
| 4 OKF 필드 정렬 | 완료 + **오늘 정정**: `sources`를 객체 목록으로 | `log.md` 생성기, `stale_after` 활용 |
| 5 `kb/{ontology,odd}`·OpenODD | 완료 | 모듈 YAML 키 원문 대조(원문 페이지 404), 택소노미를 형 있는 속성 트리로 |
| 6 문서 세 층 | 완료 | — |
| 7 1단계 측정 | 부분 — 세 축으로 재정의, 고아율 0%, 예산 이내 5/5, 의미 보존 대리 3/5 | 확정 문장 커버리지, 라벨 대표성 실험 |
| 통과 조건 세 축 | 채택·반영 (노트 14.1, 결정, roadmap, metrics) | 연결 성분 6→1, 매트릭스 0/4 — 3·5단계 산출 |
| 용어 정규화 | 완료 337 파일, 용어집 | 아래 미확인 3건 |

`metrics` 최신: 청크 733(살아 있는 607), 고아율 0%, 연결 성분 6, `refines` 매트릭스 0/4, 한 단계 건너뜀 332, 사람 검토 0.

## 2. 외부 조사 — 무엇을 확인했고 무엇을 고쳤나

상세 표는 [`references.md` §1.1](../references.md)에 있다 (출처 URL 포함). 요약:

**정정한 것 (저장소가 틀렸던 것)**
- OKF v0.2 `sources`는 IRI 목록이 아니라 **객체 목록**(`resource` 필수, `id`·`title`·`author`…). 프런트매터 735 파일과 `chunk2kg`·`rules.md`를 고쳤다. 게이트 PASS.
- ODC 한정자는 missing·incorrect 둘이 아니라 **extraneous 포함 셋**. 노트 8.17과 결정 `p8-odc-qualifier-and-dimensions`에 보충.
- PyYAML "부채"는 기술 제약이 아니라 **잠금 정책의 선택** — rules_python은 sdist 빌드를 지원한다. `open-questions`·`tools.md`·`kb_yaml.py` 정정.
- 용어 정규화의 조사 부산물 "코어을" 13곳 → "코어를".

**확인한 것 (저장소가 맞았던 것)** — OKF `generated`/`verified`/`status`/행위자/예약 파일/미지 키; OpenODD의 INCLUDE·EXCLUDE × AND/OR와 다섯 식, `unknown` 리터럴, 택소노미 YAML `TAXONOMY:`; OpenSCENARIO `keep`·`do serial/parallel`·`cover(expr, event, target)`; CEL의 무부작용·종료·결정론; EARS 다섯 패턴; ISO 29148 검증 방법 4종과 전방/후방 추적성; ISO 34503 최상위 3범주; LinkML 생성기; ISO 15026-2 주장·논증·증거; ISO 25964 통제 어휘; 42010 뷰; LEDGER의 노드·엣지 4종·검색 4단계·검사 3종·수치; LARGER의 노드·엣지·앵커·K-hop; GoF 국문판 "복합체".

**채운 세부** — 결정 6건에 한 문단씩(`pe-three-layer-binding`·`pe-odd-is-openodd`·`pe-scenario-is-openscenario`·`pe-notation-and-cel`·`p7-dev-plane-substance`·`p6-assumption-verification-methods`), `dependency-graph-design.md`에 LEDGER·LARGER 검증 절, 용어집에 출처·확인 표기.

**미확인으로 남긴 것** — 역량 질문의 국문 정역, ISTQB 국문 "합격 판정 기준" 표기, ISO 34503 국문 명칭과 "ODD exit" 표기, OpenODD 모듈 YAML 키 이름. 용어집·references에 미확인으로 표시했다.

## 3. 검토에서 드러난 것 — 판단이 필요한 둘

1. **OpenODD 정합의 깊이** — 지금 `project-odd.yml`은 OpenODD의 의미론(INCLUDE ∧ ¬EXCLUDE, 다섯 식, unknown)을 따르되 키 이름은 적응이고, 조건 값이 자유 문장(`equal: "Bazel 9.2.0 + …"`)이라 범주 리터럴이 아니다. 도입 2단계(`odd_check`)에서 원문 키와 형 있는 택소노미로 맞출지, 지금 맞출지.
2. **PyYAML** — 정책을 바꿔 sdist 해시로 잠그면 `kb_yaml.py`를 지울 수 있다. 네트워크가 필요하다(ODD `cond-network` 허용 범위). 할지 말지.

## 답
**유저(2026-09-11): "1은 지금 맞추고 2도 진행해줘"** — hci 반영(담당 역할 인수 대기): ODD 문서를 OpenODD YAML 매핑 모양으로 재작성(범주 리터럴·수치 식·확장 키 대문자), 생성기 재작성; `pyyaml==6.0.2` 잠금(relock.sh가 플랫폼 휠에 sdist 해시 병기), `kb_yaml.py` 삭제.

인수: orchestrator 2026-09-11 — 청크·도구·문서 변경을 검토했다(요구 7건 전문, 결정 표본, 온톨로지 폐기 표기, 게이트 구조 검사). endorse 로 verified 부여.

인수: orchestrator 2026-09-12 (채널 점검) — 판단 둘 다 반영 완료 상태 확인: 1 OpenODD YAML 매핑 재작성(`kb/odd/project-odd.yml`·`odd2kg`·`taxonomy`), 2 PyYAML 해시 고정(`pyyaml==6.0.2`, `kb_yaml.py` 삭제 2026-09-11). 이 항목에서 남는 수행은 없다 — 유저 태깅 대기(`open`).
