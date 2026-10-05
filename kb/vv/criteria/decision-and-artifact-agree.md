---
id: https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee
type: contract
level: logical
title_ko: 결정 결론의 내용 해시가 바뀌면 그것을 충족하는 링크가 재판정 대상이 된다
title: When the content hash of a decision conclusion changes, the links that satisfy it become re-judgement targets
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:18:12+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-04T23:20:47+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a]
---
**합격 기준** — 기준 종류는 불변식이다. 결정 결론 `d`의 `agt:contentHash`가 리비전 사이에 바뀌었으면 `d`를 대상으로 하는 확정 링크 전부가 `suspect`로 유도되거나 재판정 기록을 갖는 것이 합격이다.

**판정식**

- 실행. 표본 리비전 창은 합성 변이다(유저 답 Q38-c). `python3 tools/revalidate.py --base-files <base 결론> <base 산출물> --head-files <head 결론> <head 산출물>`이 git·`bazel query` 없이 스냅숏 둘을 비교한다. head 결론 파일 이름은 `conclusion.md`여야 결정 결론으로 인식된다(`DECISION_PART_FILES`).
- 음성. 결론 본문 한 문장만 다른 쌍(`defs/tests/revalidate/{base,head}/`)에서 종료 1, `(바뀐 끝이 결정 결론인 것 1)`, 링크 개체 행 `| 도착 | suspect |`가 나오지 않으면 불합격이다. 케이스는 `decision-conclusion-mutation-equivalence-2`다.
- 통제. 같은 쌍을 base=head로 주면 종료 0과 `재판정 링크 개체 0`이다. 케이스는 `decision-conclusion-mutation-equivalence-1`이고 둘 다 논리 시나리오 `decision-conclusion-mutation`에서 생성된다.
- 실측 2026-10-04에 변이 쌍은 변경 청크 1 · 재판정 대상 1 · 링크 개체 1(바뀐 끝이 결정 결론인 것 1)이고 통제 쌍은 전부 0이다. 두 케이스 모두 `vv_run`에서 pass이고 고정물 시험 `//defs/tests:revalidate_fixture_{dirs,files,same,partial}_test`가 같은 판정을 `bazel test`에서 한다. 공허 합격이 아니다.
- 라벨 쪽은 현상 `agt:labelRot`(P14)이다. 라벨이 본문을 대표하는지는 세션 판정자 질문 `agt:labelRepresentsBody`의 값 분포로 잰다. 첫 측정(2026-09-30)은 실표본 60건 중 값 1이 6 = 10.0%이고 값 일치는 58/60 = 96.7%이며 값 2를 받은 미끼는 0/10이다.

**등급** — A다. 링크 재판정의 판정은 생성된 케이스 둘과 고정물 시험이 하고 사람 판단이 없다. 라벨 부패의 측정은 판정자의 값이라 게이트 밖이고 이 등급의 근거가 아니다.
