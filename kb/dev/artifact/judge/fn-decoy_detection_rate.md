---
id: https://agentic-knowledge-base.dev/id/chunk/f804ba0b-8ec8-42b5-b53e-733d51e50546
type: artifact
level: executable
title_ko: 함수 decoy_detection_rate (tools/judge.py)
title: function decoy_detection_rate in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/48ed45d6-a852-4def-9baa-eee654691bc7, https://agentic-knowledge-base.dev/id/chunk/a2001d9e-7d53-4d25-b643-9825bd271d97]
part_of: https://agentic-knowledge-base.dev/id/composite/25ad6efd-997a-44a7-b5c4-dc61c13b63ed
---
**함수** — `decoy_detection_rate(items, q, resp_sets)` 다. 미끼 검출률의 (검출 수, 응답 있는 미끼 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decoy_detection_rate(items: list[dict], q: dict, resp_sets: list[dict]) -> tuple[int, int]:
    """미끼 검출률의 (검출 수, 응답 있는 미끼 수).

    검출 = **"척도의 최고값(적합)이 아니다"**다(orchestrator 결정, 2026-09-30 vnv 결함 보고 ③) — 판별력의 뜻이
    "미끼를 적합으로 통과시키지 않는가"이기 때문이다. 이전 판(최저 척도값과 같아야 검출)은 "부분"으로 답한
    판별도 놓쳤다. 척도의 상황 문장 자체는 그대로다 — 척도는 상황으로 적는다(질문 온톨로지, p8-judge-calibration-binding).
    score 형만 잰다 — noul·choice 는 질문마다 "적합"의 뜻이 달라 일반화하지 않는다(9.3절 판별력)."""
    if q["form"] != "score" or not q["scale"]:
        return 0, 0
    full_fit = str(_leading_int(max(q["scale"], key=_leading_int)))
    hit = seen = 0
    for it in items:
        fp = kb_lib.label_fingerprint(it)
        for data in resp_sets:
            for r in data.get("responses", []):
                if r.get("fingerprint") == fp:
                    seen += 1
                    if str(r.get("value")) != full_fit:
                        hit += 1
    return hit, seen
```
<!-- 인용 끝 -->
