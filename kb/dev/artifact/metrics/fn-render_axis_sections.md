---
id: https://agentic-knowledge-base.dev/id/chunk/8539f11f-8398-42c3-91a0-b7ae377c9927
type: artifact
level: executable
title_ko: 함수 render_axis_sections (tools/metrics.py)
title: function render_axis_sections in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/453be329-3277-4ed7-a036-50df02988fed
---
**함수** — `render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line, link_ents, with_ev, origins, extracted_n, built_n, restored_total, tim_filled, TIM, BUDGET, role_rows, scope_bad)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line, link_ents, with_ev, origins, extracted_n, built_n, restored_total, tim_filled, TIM, BUDGET, role_rows, scope_bad):
    o = []
    o += ["", "## 세 축 대리 — 1·3·5단계 (14.1 정정본: 의미 보존 · 구체화 · 유기적 연결)", "",
          f"- 연결: 저작된 지식의 연결 성분 **{components}**개 (살아 있는 청크 {len(live)} 중 관측·주석 {len(live) - len(authored)}건을 뺀 {len(authored)}개가 링크·복합체로 이어진 덩어리. 목표 1)",
          f"- 연결: level×level `refines` 매트릭스 채움 {pct(len(filled), 4)} — " + (", ".join(f"{a_}→{b_}" for a_, b_ in filled) or "없음") + " (목표 4/4 = 100.0%)",
          f"- 구체화: level을 한 단계씩 내려가지 않는 `refines` **{len(skips)}**건 (목표 0; 지금은 concrete→functional 직행이 구조적으로 허용됨 — abstract·logical 결정이 생기면 0이어야 한다)",
          f"- 구체화: 수준 허용표 위반 **{len(residency_bad)}**건 (목표 0)",
          cov_line,
          "- 의미 보존: 라벨 대표성은 실험 — 이 도구 밖"]
    o += ["", "## 3단계 대리 — 링크 구축 (14.1 정정본: 근거 · 한 단계씩 · 매트릭스 · 복원 비율)", "",
          f"- 의미 보존: 링크 개체 **{len(link_ents)}** (확정 {origins['confirmed']} · 후보 {origins['candidates']}) 중 증거 기록이 있는 것 **{pct(len(with_ev), len(link_ents))}** (목표 100.0%; 증거 종류 분포는 `audit` 링크 근거 절)",
          f"- 의미 보존: 구축 비율 — 확정 링크 개체 중 구축(구축 기록 증거뿐) {built_n} vs 복원 {restored_total}(구축 기록 아닌 증거 `proposal` 을 가진 링크 개체 — frontmatter `restored:` 표시) → 복원 비율 **{pct(restored_total, built_n + restored_total)}** (목표 20% 미만; 후보는 `bazel build //kg:link_candidates`, 확정은 `restored:` — p10-restored-link-marking)",
          f"- 의미 보존: 후보 링크 개체(`agt:CandidateLink`, linkState candidate — 본문 추출, 증거는 구축 기록) **{origins['candidates']}** — " + (" · ".join(f"`{k}` {v}" for k, v in sorted(origins['candidate_kinds'].items())) or "없음") + "; 본문 식별자 추출 직접 트리플 " + " · ".join(f"`{k}` {v}" for k, v in extracted_n.items()) + " (`usesConcept` 는 대상이 온톨로지 용어라 링크 치역 밖 — 후보 개체 없음; p10-extracted-references-are-candidates)",
          f"- 연결: plane×plane 매트릭스 — TIM 허용 칸 채움 **{pct(len(tim_filled), len(TIM))}** ({', '.join(f'{k}:{a_}→{b_}' for k, a_, b_ in tim_filled) or '없음'}); 빈 칸은 contract·schema·artifact·V&V 항목이 생겨야 찬다",
          "- 구체화: `refines` 한 단계씩 — 위 세 축 절의 건너뜀 수 참조"]
    o += ["", "## 2단계 대리 — ODD와 스코프", "",
          f"- 정의: 여기의 예산 준수율은 **앵커마다** 센다 — 스코프 안 청크 하나를 앵커로 잡고 그 1홉 이웃의 라벨과 본문을 펼친 줄 수가 "
          f"{BUDGET}줄 이하인 앵커의 비율이다. `bazel build //kg:workset` 의 예산 판정은 **문서 전체**(앵커 없이 스코프 전체의 라벨 목록)를 재므로 "
          "두 수치는 같은 이름이되 다른 것을 센다",
          "- 구체화: 역할·앵커별 작업 집합(스코프 안 청크를 앵커로, 1홉 이웃 라벨 + 본문 펼침)이 예산 안인 비율: " + " · ".join(role_rows),
          f"- 구체화: ODD × plane 권한에서 파생되지 않은 스코프 **{len(scope_bad)}**건" + (f" — {', '.join(scope_bad)}" if scope_bad else "") + " (목표 0; 2026-09-26부터 게이트 `catalog` 가 같은 규칙을 강제하므로 이 수치는 그 게이트의 관측이다)",
          "- 연결: ODD 밖 참조는 게이트(odd-ref)가 0으로 강제. 첫 모니터링 이탈은 `bazel run //tools:odd_check`"]
    return o
```
<!-- 인용 끝 -->
