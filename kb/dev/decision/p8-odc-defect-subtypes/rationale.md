---
id: https://agentic-knowledge-base.dev/id/chunk/f015e7f7-e974-44a3-aec0-6f24a96e5a30
type: decision
level: logical
title_ko: 수정 행위로 정의된 배타적 유형이라야 분포 진단이 성립한다
title: Only mutually exclusive types defined by the fix make distribution diagnosis work
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc
---
**근거** (노트 8.17절) — ODC를 쓰는 이유는 유형이 배타적이고 **수정 행위로 정의되어 있어** 분류가 판단에 덜 흔들리기 때문이다. 자체 분류를 새로 만들면 같은 결함이 세션마다 다른 유형으로 기록되어 분포 진단이 무의미해진다 (있는 어휘를 쓴다 — r-017과 같은 이유).

- 고유 유형을 더하는 자리가 인지와 상호작용인 이유 — ODC는 코드 결함의 분류라 "입력을 잘못 읽음"과 "메시지를 오해함"에 대응하는 유형이 없다. 실행 요인은 ODC 여덟 유형이 그대로 덮는다.
- 인지 요인의 하위 넷이 서로 다른 고칠 곳을 지목한다 — 오독은 표현·프롬프트, 누락은 스코프, 낡음은 무효화 전파(6.10절), 오인은 어휘 밖 지식의 거부(r-017)다.
