# 미해결·결정 요청 항목의 최소 구조 (유저 피드백에서 나온 교훈)

2026-09-02 유저: "한문장의 짧은 질문으로는 해당 항목에 대한 내용파악이 힘든것같아."
docs/open-questions.md의 한 줄 항목으로는 답을 받을 수 없었다. 유저에게 판단을 요청하는 질문의 형식은
`harness/user/README.md`가 원본이다(2026-10-03 부터 그 자리는 질문지 `harness/user/Q-<번호>.md`다). 여기에 다시 적지 않는다.

**이름 검사(2026-10-24, result 0246, Q103 답의 3번).** 2026-10-24T08:20:24 뒤에 보내는 메시지와 2026-10-25부터 만드는 질문지에서,
백틱 안의 결정 slug·`agt:` 어휘·`id:` 개체가 KB 항목으로 풀리면 **같은 줄에 그 한글 이름을 정확히** 적어야 한다(`channel_lint`의 하위 검사 `names`).
결정의 이름은 결정 기록의 `title_ko`다 — `kb/dev/decision/<slug>/conclusion.md`의 `composite: {…, title_ko: …}` 필드이고, 결론 자체의 `title_ko`가 아니다.
찾는 명령: `grep -o 'composite: {[^}]*}' kb/dev/decision/<slug>/conclusion.md | grep -o 'title_ko: [^,}]*'`. 어휘와 개체는 온톨로지·그래프의 `@ko` 라벨이다.
빠뜨리면 `//harness:channel_lint_test`가 바른 이름을 보여 주며 거부한다. 경로·명령·게이트 id는 대상이 아니다. 인용 블록 줄에도 걸린다(실제로 막히면 orchestrator가 뺀다).

라벨 한 줄은 인덱스다 — 내용이 아니다. 질문지에서 지식은 한글 이름과 경로로 가리키고(IRI만 적지 않는다, Q104-a 2026-10-23),
본문 수치는 반드시 실측(`ls|wc`, `grep -c`, awk)한다 — 문서의 수치는 낡아 있다.
반영됨(2026-09-04, 2026-10-03 개정): `AGENTS.md` 소통 규칙 · `STYLEGUIDE.md` §8 · `harness/user/README.md`.
`docs/open-questions.md`와 `docs/open-questions/` 디렉토리는 없어졌다. 미결은 설계 공간(`space/*-space.md`)과 뷰 `//kg:open`에 산다(Q54-a).
