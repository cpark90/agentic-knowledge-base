---
id: https://agentic-knowledge-base.dev/id/chunk/fe6b6284-362e-4830-9f28-3b8991ad565a
type: decision
level: logical
title_ko: 지식의 가정이 그 ODD 위의 명제라 ODD가 다르면 판정이 성립하지 않는다
former_title_ko: ["청크의 가정이 그 ODD 위의 명제라 ODD가 다르면 판정이 성립하지 않는다", "지식 항목의 가정이 그 ODD 위의 명제라 ODD가 다르면 판정이 성립하지 않는다"]
title: A chunk's assumptions are propositions over its own ODD, so judgement fails under another
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-01T05:42:48+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8dbf8cd0-81dd-478f-b73e-3aeea905768f
---
**근거** (노트 12.7절)

- 지식의 가정은 **그 프로젝트 ODD 조건 위의 명제**다. 다른 ODD로 옮기면 가정의
  판정 자체가 성립하지 않으므로, 옮겨진 지식은 근거 없는 문장이 된다.
- 온톨로지 코어를 수정하지 않는 이유 — 코어가 프로젝트마다 갈라지면 프로젝트를
  넘는 것이 아무것도 남지 않는다. 확장은 모듈로만 한다.
- 일반화로 올라간 제약은 이미 온톨로지 공리이므로 별도 이관 절차가 없다.
  **이것이 일반화(6.3절)가 지식에서 멈추지 않고 온톨로지까지 닿아야 하는
  이유다** — 어휘와 공리로 올라간 것만 다음 프로젝트에서 쓸 수 있다.

**개정** (Q-0075#Q172-a, 2026-11-01) — 다음 프로젝트 `smartbelley_vnv`가 이 저장소를 Bazel 모듈 의존으로 쓰기로 했다. 코어가 한 곳에 있어야 "코어 수정 금지"가 기계로 지켜지고, 복사하면 두 사본이 표류하는데 그것을 잡을 수단이 없다. 2026-10-31 시험 의존 모듈 실측에서 막힌 자리는 아홉이었다. 그중 일곱(명령 문자열의 도구 라벨, verify 질의 고정 경로와 질의 0개의 거짓 통과, 어휘 파일 이름 고정, 작업 트리 상대의 코어 경로, `--residency` 기본값, IRI 이름공간 고정)을 고쳤다. 남은 둘은 생성 BUILD의 `//defs` 전제와 V&V 판정의 `kb/vv` 접두이고, 의존 저장소가 BUILD를 손으로 쓰고 같은 배치를 따르면 닿지 않는다. 손질 뒤 시험 의존 모듈에서 게이트가 의존 저장소의 요구를 실제로 판정했고(출처 없는 본문을 shacl이 거부했다), 질의 도구가 이 모듈의 코어를 runfiles에서 찾았다. 이름공간 기본값을 `kb_lib`이 아니라 `chunk2kg`에 둔 것은 head 액션과 `odd2kg`가 rdflib 없이 돌아 `kb_lib`을 불러올 수 없기 때문이다.
