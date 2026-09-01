# 에이전트 lane — 타 에이전트 → hci

hci를 제외한 에이전트가 **유저 피드백이 필요할 때 / 문제가 생겼을 때 / 특이사항이
생겼을 때** 항목을 남기는 곳. 유저에게 직접 묻지 않는다 — hci가 이 lane을 스캔해
검토하고 유저에게 전달한다. 규약 원본: [`../README.md`](../README.md).

- 파일명: `{발신역할}-{주제-kebab}.md` (예: `developer-shacl-ambiguity.md`)
- 작성·수정은 **자기 항목만**. 다른 항목·유저 lane은 읽기 전용.
- 작성은 `.wip.md` → 완료 시 rename.

```markdown
---
from: developer      # 발신 역할
kind: decision       # decision(결정 필요) | problem(문제) | notice(특이사항)
status: open         # open → relayed(hci) → answered(hci) → closed(발신자)
targets: []          # 관련 지식 (선택)
---

# (제목)

(배경 + 필요한 결정/전달 내용 + 선택지가 있으면 선택지)

## 답
(hci가 유저의 답을 채움)
```
