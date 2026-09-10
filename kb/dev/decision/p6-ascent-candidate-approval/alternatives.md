---
id: https://agentic-knowledge-base.dev/id/chunk/2224512f-ee1f-423a-bc09-7807e5d944f7
type: decision
level: logical
title_ko: 상승 트리거 자동화 후보 넷 — 초기에는 유저 지정만 쓴다
title: Four candidate ascent triggers - only user tagging is used at first
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b3bb3bde-43af-4fad-8e67-3a52dd7a2fa9
---
**대안** `[안]` — 상승의 트리거를 자동화하는 후보 넷 (노트 6.11절, 미확정).

- **반복** — 같은 결함 요인이 N회 이상 관측 → 요인 청크를 `defect` 어휘 후보로
- **무효화 빈도** — 같은 가정이 M회 이상 깨짐 → 가정을 ODD 속성 후보로 (범위 재검토)
- **배제 반복** — 같은 후보가 같은 제약으로 K회 이상 기각 → 제약을 온톨로지 공리 후보로
- **유저 지정** — 유저가 관측 청크에 "일반화" 태그 → 즉시 후보

`[?]` N·M·K의 초기값은 정하지 않았다. 실행 기록이 쌓이기 전에는 넷 중 **유저 지정만** 쓴다 — 임계값을 근거 없이 고르면 잡음이 어휘로 올라가고, 그 오염은 6.3절 상승의 되돌리기 비용을 그대로 문다.
