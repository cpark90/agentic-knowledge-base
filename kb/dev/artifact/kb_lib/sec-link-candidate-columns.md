---
id: https://agentic-knowledge-base.dev/id/chunk/cf9e740e-2c3d-44e8-9d49-d75654ff849e
type: artifact
level: executable
title_ko: 절 link-candidate-columns (tools/kb_lib.py)
title: section link-candidate-columns in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/940cfa49-d6bf-444b-93a1-ee4441b63501
composite: {id: https://agentic-knowledge-base.dev/id/composite/940cfa49-d6bf-444b-93a1-ee4441b63501, title_ko: 절 복합체 link-candidate-columns (tools/kb_lib.py), title: section composite link-candidate-columns in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/cf9e740e-2c3d-44e8-9d49-d75654ff849e, https://agentic-knowledge-base.dev/id/chunk/8c071cee-5922-4176-a0d9-848167ee9316, https://agentic-knowledge-base.dev/id/chunk/13c498a5-52b6-4be6-a555-4099859edbbf, https://agentic-knowledge-base.dev/id/chunk/9ba49f50-c949-45ae-816e-d24210ec8af6], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `link-candidate-columns` 다. 쌍 판정의 해시값과 링크 후보 뷰의 판정 넷

**정의** — `judged_class` · `pair_fingerprint` · `pair_record_fingerprint` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 쌍 판정의 해시값과 링크 후보 뷰의 판정 넷 ────────────────────
# 링크 후보 뷰(tools/link.py)의 후보 표 열 — 쌍 판정지(`label_sample.py --pair-sheet`)가 이 열 이름으로 표를 되읽는다
LINK_CANDIDATE_COLUMNS = ("#", "앵커 (ko)", "앵커 파일", "링크 종류", "대상 (ko)", "대상 IRI", "근거 종류",
                          "근거 값 (인용 식별자 / 테스트 케이스 슬러그 / 공유 개념 수 / 승계: 원본 / 판정 극성)", "판정자 값",
                          "판정 (채택 / 기각)")
# 동시 편집이 첫 근거인 후보의 판정 넷 — 판정 증거(agt:judgement)의 극성으로 가른다. 사람 확인 큐에는 일치(+,+) 전부와 일치(−,−)의
# 표본이 오른다 (task 0303, Q165-c)
JUDGED_AGREE_YES, JUDGED_AGREE_NO, JUDGED_DISAGREE, JUDGED_NONE = "일치(+,+)", "일치(−,−)", "불일치", "판정 없음"
# 일치(−,−) 표본 — 쌍마다 sha256(시드 ∣ 앵커 IRI ∣ 대상 IRI ∣ 링크 종류)으로 순위를 매겨 가장 작은 크기만큼 큐에 올린다. 사람이 표본에서
# 성립하는 링크를 찾으면 판정자가 놓친 비율의 재료다. 표본 밖 일치(−,−)는 큐 밖 절에 후보로 남는다 (task 0303, Q165-c)
JUDGED_NO_SAMPLE_SEED = "20261025"
JUDGED_NO_SAMPLE_SIZE = 20
JUDGED_NO_SAMPLE_MARK = "표본(−,−)"
```
<!-- 인용 끝 -->
