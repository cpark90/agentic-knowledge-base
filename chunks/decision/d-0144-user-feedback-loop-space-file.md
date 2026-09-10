---
id: https://agentic-knowledge-base.dev/id/chunk-d0144
type: decision
level: concrete
title_ko: 사용자 피드백 루프와 -space 파일 형식
title: User feedback loop and the -space file format
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 유저는 적은 선택지 중 고르지 않는다. **리포트를 받고 거기에
피드백을 입력해 결정한다.** logical 단계의 `-space` 파일이 그대로 리포트이며,
체계가 그것을 **유저가 읽고 편집 가능한 형태로 노출**하는 것이 유일한 UI
요구다.

**근거** (노트 10.2, 11.5절)
- 결정할 항목과 배경 = `-space`의 변수·도메인·제약, 선택지 = 도메인,
  결정의 기록 = concrete 배정 + `refines` 링크, 완결 판정 = 후보 링크가
  하나 남음.
- **완결된 피드백만 채널을 통과한다.** 후보가 하나로 좁혀지기 전의 편집은
  피드백 디렉토리 안에 머문다.
- 파일 형식은 유저가 온톨로지 문법을 몰라도 되게 한다 — 제목 + 청크 앵커,
  배경 한 줄, 후보 체크박스 목록, 메모 칸.

```
## 인증 방식                          [d-17-space]
배경: 외부 클라이언트가 존재하므로 API key는 배제됨.
후보 (남은 것 위주로 편집하세요)
  [x] OAuth2   — 운영 경험 있음
  [ ] mTLS     — 인증서 관리 부담
  [-] API key  — 배제됨 (외부 클라이언트)
메모:
```

`[x]`가 하나만 남으면 완결이고, 체계가 이 파일을 후보 링크 상태로 되읽는다.
