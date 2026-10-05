---
id: https://agentic-knowledge-base.dev/id/chunk/c67dfe43-f624-4e13-a813-64f0733fbfd6
type: artifact
level: executable
title_ko: 절 link-targets (tools/chunk2kg.py)
title: section link-targets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
composite: {id: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2, title_ko: 절 복합체 link-targets (tools/chunk2kg.py), title: section composite link-targets in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c67dfe43-f624-4e13-a813-64f0733fbfd6, https://agentic-knowledge-base.dev/id/chunk/583a95ea-746e-4243-a6d9-108c18a3c9d8, https://agentic-knowledge-base.dev/id/chunk/dae11730-e07f-47c6-becd-61b72a819b12, https://agentic-knowledge-base.dev/id/chunk/4dcdeb22-0819-48a5-96a4-72da225a3003, https://agentic-knowledge-base.dev/id/chunk/1b8a9132-b68b-46c7-a14e-55e7048494e2, https://agentic-knowledge-base.dev/id/chunk/8a9578b7-a0d9-4b0a-951e-aed33d8b8825, https://agentic-knowledge-base.dev/id/chunk/e40d0ed3-5060-4b0e-9dd9-d76acde18c0e], part_of: https://agentic-knowledge-base.dev/id/composite/067a8c81-640e-4b58-8235-c18119d80f2e}
---
**절** — `tools/chunk2kg.py` 의 절 `link-targets` 다. 링크의 방출과 정체성

**정의** — `link_targets` · `check_restored` · `link_hash` · `spec_cycles` · `work_id` · `emit_links` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 링크의 방출과 정체성 ────────────────────
# frontmatter 의 **링크 키**와 링크 IRI 의 규칙 — 이 절이 방출하는 것이다.
#   refines:      이 항목이 정제하는 상위 항목 IRI 목록 (선택, 수직 링크 9.2절)
#   supersedes:   이 항목이 대체하는 항목 IRI 목록 (선택)
#   serves·verifies·derivesFrom·satisfies·constrains·allocates·generates·overlapsWith: 그 밖의 링크 키(LINK_KEYS) — 대상 IRI 목록 (선택).
#                 모든 링크 키는 직접 트리플(agt:<key>)과 링크 개체(agt:Link, emit_links) 둘로 나간다. verifies 의 주어는 kb/vv 청크뿐 (defs/kb.bzl).
#                 overlapsWith 는 relatedTo 족의 약한 잎이다 — 추적 매트릭스에 칸이 없어 어느 잎도 이름을 주지 못하는 관계의 자리이고,
#                 Bazel deps 가 되지 않는다(gen_build.LINKS 밖) 대신 링크 개체와 복원 표시를 받는다 (overlap-ontology)
#   restored:     복원 링크의 표시 — 같은 청크의 링크 키(LINK_KEYS) 어딘가에 대상으로 있는 IRI 목록 (선택, p10-restored-link-marking).
#                 그 (주어, 링크 키, 대상)의 agt:Link 개체에 증거가 두 줄 붙는다 — 확정 기록 constructionRecord(사람이 frontmatter 에 적은
#                 편집 시점 기록; 9.11절 규칙 "구축(+) 또는 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제한다)와
#                 후보의 출처 proposal(도구·에이전트가 제안하고 사람이 확정). 구축 링크는 constructionRecord 한 줄뿐이므로 proposal 의 유무가
#                 복원의 표지다. linkState 는 그대로 confirmed 다 — frontmatter 에 적힌 것은 확정이다. 링크 대상에 없는 IRI 는
#                 `FAIL [restored] <파일>: 복원 표시 <IRI> 가 링크 대상에 없다` 로 거부. 복원 비율(metrics·audit)은 증거 종류로 센다 (kb_lib.link_origins)
#   specializationOf: 분할로 생긴 조각이 원 청크를 가리키는 단일 IRI (선택, p10-split-keeps-work-identity) → prov:specializationOf (PROV-O).
#                 청크 uuid 는 work-id 다: 분할 시 조각 하나가 원 uuid 를 승계하고 나머지는 새 uuid + 이 키로 잇는다. 자기 자신은 거부.
#                 대상 실재는 validate dangling, 같은 plane·살아 있음·사슬 비순환은 validate check_specialization(FAIL [specialization])이
#                 판정한다. 순환은 이 도구도 뿌리를 계산할 수 없으므로 같은 게이트 id 로 거부한다
#   링크 IRI:     id/link/<sha256(뿌리(출발)|종류|뿌리(도착))[:12]> — 양 끝은 specializationOf 사슬을 따라 올라간 뿌리 uuid(work-id)다.
#                 그래서 조각을 가리키는 링크와 원본을 가리키던 링크가 같은 개체가 되어 증거·이력이 이어진다. 뿌리는 묶음 전체를 알아야
#                 계산되므로 --fragment 는 원 IRI 로 해시하고 --merge(와 단일 실행)가 rebase_links 로 다시 계산해 같은 IRI 의 링크·증거
#                 블록을 하나로 합친다(양 끝·증거의 합집합). 증거 IRI 는 같은 해시에 접미(-proposal)다
#   coUpdatesWith: 같은 내용을 담아 함께 갱신되어야 하는 청크 IRI 목록 (선택, relatedTo 족 — 안전율 중복의 표시)













LINK_PREFIX = f"{ID_BASE}link/"
EVIDENCE_PREFIX = f"{ID_BASE}evidence/"
_SPEC_LINE = re.compile(r"^    prov:specializationOf <([^>]+)>", re.MULTILINE)
```
<!-- 인용 끝 -->
