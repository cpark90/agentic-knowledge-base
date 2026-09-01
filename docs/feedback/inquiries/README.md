# 조사 lane — hci → 타 에이전트

유저의 조사 요청("구현된 내용이 어떻게 되어 있는가")을 hci가 조사 질문으로 구체화해
남기는 곳. 담당 에이전트(주로 inspection)가 사이클마다 `status: open`을 스캔해
조사하고 같은 파일에 답을 채운다. 규약 원본: [`../README.md`](../README.md).

- 파일명: `{주제-kebab}.md`
- 답에는 **결론 + 근거**(`file:line` 또는 청크 IRI)를 적는다. 불명확하면 추측으로
  채우지 않고 한계를 명시한다.
- 상태: `open`(hci 작성) → `answered`(담당 에이전트가 답 완성) → `closed`(hci가
  유저 lane으로 중계·소비 후 태깅) → 담당 에이전트가 다음 사이클에 제거.

```markdown
---
from: hci
assignee: inspection   # 담당 역할
status: open           # open → answered → closed
---

# (조사 질문)

(무엇을 왜 알아야 하는지 + 조사 범위)

## 답
(담당 에이전트가 채움 — 결론 + 근거)
```
