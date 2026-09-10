세 층의 역할
층	담당	못 하는 것
OKF	지식의 원본. 마크다운 + YAML 프론트매터, git으로 버전 관리, 사람과 에이전트가 모두 읽음. verified: human / generated: agent 트러스트 티어	관계의 의미, 일관성 검증, 파생물 관리
온톨로지 (PROV-O + SHACL)	관계에 이름 붙이기(supersedes, dependsOn, contradicts), 근거 연쇄 표현, 스키마 제약 검증, SPARQL 의미 질의	증분 컴파일, 캐시, CI에서의 강제
Bazel	원본→그래프 변환, 파생물(요약·인덱스·컨텍스트 번들) 자동 무효화, 검증을 테스트로 실행, 가시성으로 경계 강제	의미 검색, 다양한 엣지 타입
세 층을 잇는 세 가지 접점

Bazel 라벨을 앵커로. 결정 기록이 파일 경로 대신 //src/auth:server 같은 라벨을 참조합니다. 경로는 리팩터링에 깨지지만 라벨은 살아남고, bazel query로 영향 범위를 뽑을 수 있습니다. 작업(Beads) → 타깃(Bazel) → 결정(OKF)이 하나의 그래프로 이어지는 연결점입니다.

프론트매터를 트리플로. OKF의 type은 rdf:type이고 링크는 관계입니다. Bazel 액션이 각 파일을 Turtle로 변환하고, 바뀐 파일만 다시 변환됩니다. 온톨로지를 따로 관리하는 게 아니라 OKF에서 컴파일해 내는 겁니다.

TBox/ABox 분리를 권한 경계로. 스키마(무엇이 Decision이고 무엇이 필요한가)는 사람만 수정합니다. 인스턴스(실제 결정과 사실)는 에이전트가 쓰되 SHACL 제약을 통과해야 빌드됩니다. 시험지는 에이전트 손 밖에, 답안만 쓸 수 있는 구조입니다. OKF 트러스트 티어와 PROV-O의 Person/SoftwareAgent 구분이 여기서 같은 걸 가리킵니다.

파이프라인
OKF 마크다운 (git)
  │ Bazel: frontmatter → Turtle (바뀐 것만)
  ▼
프로젝트 그래프 (.ttl)
  │ Bazel test: SHACL 검증 — 실패하면 빌드 실패
  │ Bazel: 규칙 몇 개를 SPARQL UPDATE로 물질화 (retracted → atRisk 전파)
  ▼
Oxigraph (임베디드 SPARQL, 빌드 산출물)
  │ MCP 도구로 노출
  ▼
워커 세션 — SessionStart 훅이 SPARQL CONSTRUCT 결과를 컨텍스트로 로드

이 구조에서 워커가 받는 지식은 사람의 요약이 아니라 그래프에서 기계적으로 도출된 부분그래프입니다. 요약 릴레이에서 규칙이 빠지는 문제가 개입할 자리가 없습니다.

검증되는 것

bazel test 한 번에 잡히는 것들입니다.

인용한 코드 타깃이 존재하는가
전제 결정이 retracted인데 이 결정이 active인가
verified: human 파일을 에이전트 커밋이 건드렸는가
superseded 결정이 여전히 active 코드를 constrains 하는가
Decision에 Evidence를 인용하는 Rationale이 있는가

지식 테스트 통과율이 곧 지식 그래프의 건전성 지표가 됩니다.

시작 순서
OKF 포맷으로 결정 기록을 시작. 프론트매터에 depends_on, anchors, verified만 넣습니다.
프론트매터에서 BUILD를 생성하는 Gazelle 확장 하나. 손으로 쓰면 못 버팁니다.
PROV-O 그대로 + 프로젝트 클래스 5개(Decision, Constraint, Evidence, Ruling, Target)로 스키마 고정.
SHACL shape 다섯 개로 위 검증 목록 구현.
실제로 쿼리하게 된 관계만 추가.
주의

과잉 설계가 가장 큰 위험입니다. 클래스와 필드가 늘수록 아무도 채우지 않는 칸이 늘고, Yegge의 450개 산출물이 됩니다. 실제로 쿼리하는 관계만 살아남게 하세요.

OWL 추론은 쓰지 마세요. 열린 세계 가정과 속도 문제가 있고 에이전트가 의미론을 틀립니다. 검증은 SHACL, 추론은 단순 규칙 물질화로 충분합니다.

에이전트에게 스키마를 맡기지 마세요. Turtle과 SPARQL은 잘 쓰지만 온톨로지 설계는 못합니다. 인스턴스 작성으로 역할을 제한하세요.
