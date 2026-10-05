# FY.md — 고정물 둘째 규범 문서 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 3개: `kb/dev/decision/fx-a/conventions.md` · `kb/dev/norm/fy/head.md` · `kb/dev/norm/fy/one.md` · 절 1 · 규약 줄 1
- 질의: `kb/dev/norm/fy/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/fy/` 의 절 청크와 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

고정물 둘째 문서의 도입문이다. 이 문서는 첫 문서가 싣는 줄을 다시 싣는다.

## §0. 공유

이 절은 첫 문서의 세부 절이 싣는 줄을 다시 싣는다. 서로 다른 문서가 같은 줄을 한 번씩 싣는 것은 이중 소비가 아니다.

- **[지킴]** 다른 결정을 링크로 함께 가리킨다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md), [`fx-b`](kb/dev/decision/fx-b/conclusion.md)).

<!-- 인용 끝 -->

