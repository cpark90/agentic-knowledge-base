---
id: https://agentic-knowledge-base.dev/id/chunk/d89395fa-c7f4-4ba5-a820-82d384627845
type: artifact
level: executable
title_ko: 절 -fm-id (tools/metrics.py)
title: section -fm-id in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ff0be03b-b931-485c-bbb4-98c897dd6133
composite: {id: https://agentic-knowledge-base.dev/id/composite/ff0be03b-b931-485c-bbb4-98c897dd6133, title_ko: 절 복합체 -fm-id (tools/metrics.py), title: section composite -fm-id in tools/metrics.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d89395fa-c7f4-4ba5-a820-82d384627845, https://agentic-knowledge-base.dev/id/chunk/030c7af0-5dd1-4541-87a2-47f630beb3cd], part_of: https://agentic-knowledge-base.dev/id/composite/c6d68e53-8445-4ac7-a4d6-7d59dd3b3ca6}
---
**절** — `tools/metrics.py` 의 절 `-fm-id` 다. 선언 청크와 복합체

**정의** — `composite_declarers` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 선언 청크와 복합체 ────────────────────
# 복합체는 청크가 아니고 그 링크·가정은 선언 청크(frontmatter `composite:` 를 가진 청크)가 갖는다 — 파일 복합체의
# 선언 청크는 파일 청크(`module.md`)이고 그 청크는 복합체의 부분이 아니다 (p7-code-links-on-file-composite "선언 청크 =
# 파일 청크"). 그래프에는 선언 관계의 트리플이 없다 — chunk2kg 는 `composite:` 를 복합체 개체(라벨·`agt:hasDirectPart`·
# 순서)로만 방출한다. 그래서 연결 성분과 후방 추적은 선언을 청크 본문(`--bodies`)의 frontmatter 에서 읽어 선언 청크와
# 복합체를 한 노드로 본다 (유저 결정 Q49-a). 지표의 회계이고 검사가 아니다. 결정·규범·시나리오 복합체의 선언 청크는
# 이미 자기 복합체의 부분이라 이 합침은 그들에게 아무것도 바꾸지 않는다
_FM_ID = re.compile(r"^id:\s*(\S+)\s*$", re.M)
_FM_COMPOSITE = re.compile(r"^composite:\s*\{\s*id:\s*([^,\s}]+)", re.M)
```
<!-- 인용 끝 -->
