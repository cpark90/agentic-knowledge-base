---
id: https://agentic-knowledge-base.dev/id/chunk/227b4c18-cbe1-4ea2-85a4-0690c1f1e126
type: norm
level: logical
title_ko: docs/rules.md 절 — 파일 형식과 head 생성
title: docs/rules.md section — File format and head generation
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
heading: 파일 형식과 head 생성
depth: 3
---
head 메타데이터는 파일 안의 frontmatter에 있고, `bazel-bin/kg/chunks-kg.ttl`은 거기서 **생성**된다.
손으로 쓰지 않는다. `tokenCount`·`assertionLocation`이 파일에서 계산되므로 어긋날 수 없다.

```markdown
---
id: https://agentic-knowledge-base.dev/id/chunk/<uuid4>    # 필수 — uuid 영속 IRI (OKF 확장 키 id; 경로 = 주소, uuid = 정체성)
type: decision             # 필수 (OKF). requirement|decision|contract|schema|artifact|annotation|memory
level: concrete            # 필수. functional|abstract|logical|concrete|executable
title_ko: Bazel 하네스 채택  # 필수 (OKF 확장 키)
title: Adopt Bazel harness    # 필수 (OKF title)
status: stable             # 필수 (OKF). draft|stable|suspect|invalidated|deprecated
generated: {by: claude/fable-5, at: 2026-09-01T17:34:48+09:00}   # 필수 (OKF)
verified: [{by: human:cpark, at: 2026-09-07T10:00:00+09:00}]     # 선택 (OKF)
assumes: [<가정 IRI>, ...]      # 선택
sources: [{resource: <출처 IRI>}, ...]   # 선택 — OKF v0.2 sources: 객체 목록(resource 필수, id·title·author 선택) → prov:wasDerivedFrom. 도입 3단계부터 하네스가 읽기 집합으로 채움
refines: [<IRI>, ...]           # 선택 — 결정→요구 등
supersedes: [<IRI>, ...]        # 선택 — 시간축 대체
restored: [<IRI>, ...]          # 선택 — 위 링크 키의 대상 중 사후에 이은(복원) 것. 증거에 proposal 이 더해진다
specializationOf: <IRI>         # 선택 — 분할로 생긴 조각이 원 청크(같은 plane)를 가리킨다. 링크 IRI 는 뿌리 uuid 로 계산
part_of: <복합체 IRI>            # 선택 — 복합체의 부분일 때
composite: {id: ..., title_ko: ..., title: ..., ordered: [...], part_of: <상위 복합체 IRI>}  # 복합체 선언 — 대표 부분에서 한 번만.
                                # `part_of`는 선언된 **복합체**가 다른 복합체의 부분임을 적는다 (중첩, p4-composite-as-part-of)
---
본문 — 토큰 상한 이하(저작 산문 1,092 · 인용 2,856; frontmatter와 앞뒤 빈 줄은 세지 않는다)
```

IRI는 uuid로 영속이고, 내용 버전은 `chunk2kg`가 본문의 sha256 앞 12자를
`agt:contentHash`로 계산해 붙인다. 같은 IRI에서 내용이 바뀌었는지를 해시 비교로
안다 (노트 9.9절, 유저 결정 Q1).

**이 형식은 [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
번들이다.** 번들은 마크다운 + YAML 프론트매터이고, `type`만 필수이며, 소비자는 알 수 없는 키를 견딘다.
`id`·`title_ko`·`level`·`assumes` 등은 확장 키로 남고 외부 도구도 이 저장소를 읽을 수 있다
(필드 사상은 [`pe-three-layer-binding`](../../decision/pe-three-layer-binding/conclusion.md)).
예약 파일명 `index.md`·`log.md`는 **생성물로만** 둔다. 생성 명령은 `bazel build //kb/dev:index`다 (유저 결정 Q4).
