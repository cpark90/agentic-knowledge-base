---
id: https://agentic-knowledge-base.dev/id/chunk/4b460cbc-fe23-48fd-8ac3-daf8351c98c9
type: contract
level: logical
title_ko: 같은 이름의 지표는 도구가 달라도 같은 값이고 union이 다르면 그 차가 수로 적힌다
title: A same-named metric holds one value across tools and any union gap is written as a number
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/91d72e63-e72e-4803-aaf3-281a81994a31]
---
**합격 기준** — 기준 종류는 **불변식**이다. 같은 리비전에서 도구 `t`가 내는 수치 `m(t, 이름)`에 대해 이름이 같은 두 도구의 값이 같고, 읽는 union이 달라 값이 갈리면 그 차 `|n(t1) − n(t2)|`와 차의 출처 파일이 머리에 적히는 것이 합격이다.

**판정식**

- 실행. `bazel build //kg:metrics //kg:link_candidates //kg:audit` 뒤 `grep -o "트리플 [0-9]*" bazel-bin/kg/metrics.md bazel-bin/kg/link-candidates.md bazel-bin/kg/audit.md`로 세 값을 뽑는다.
- 음성. 세 값이 다르고 어느 머리도 차를 수로 적지 않으면 불합격이다. 실측 2026-09-29에 28749 · 28678 · 30293이고 `28749 − 28678 = 71`은 ODD 그래프 `bazel-bin/kb/odd/project-odd.ttl`의 트리플 수와 같고 `30293 − 28749 = 1544`는 온톨로지 모듈의 몫이다. 세 머리 어디에도 71도 1544도 없으므로 지금은 **불합격**이다.
- 양성. 이름이 같은 다른 수치는 갈리지 않는다. `살아 있는 청크`는 `metrics`·`link_candidates`·`audit` 세 곳 모두 808이다. 불변식이 깨진 자리는 `트리플` 하나다.
- 고칠 것은 도구다. 값을 맞추려고 union을 바꾸면 도구의 질의가 달라지므로, 차를 지우는 대신 각 머리가 자기 union의 구성과 차를 수로 적는 쪽이 이 기준을 만족시킨다.

**등급** — B다. 세 수치의 추출과 비교가 전부 기계 판정이고 명령이 지금 돌아 값이 나온다. A가 아닌 까닭은 차의 출처를 파일로 귀속시키는 마지막 단계가 아직 사람의 대조라는 것이다.

미확정: 차를 적을 자리가 머리의 `입력` 줄인지 별도 절인지 정해지지 않았다. 규약의 원본은 `kb_lib`의 생성 문서 머리이므로 그 결정이 서면 이 기준에 판정 문구를 적는다.
