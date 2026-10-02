---
name: judge
description: 게이트 밖에서 등록된 판정 질문을 청크에 물어 값과 확신도를 받고 판정 로그·결과 주석을 남길 때 쓴다. 판정자는 외부 서비스가 아니라 세션 판정자다 — 응답은 `--responses`로 오프라인 입력한다.
---

# judge — 판정자 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/judge.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

판정자 — 등록된 판정 질문을 청크에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-session-agreement — 질문 형·척도·임계 셋 자체는 옛 결정 p8-judge-calibration-binding·p8-judge-question-form 그대로다).

## 언제 쓰는가

게이트 밖에서 등록된 판정 질문을 청크에 물어 값과 확신도를 받고 판정 로그·결과 주석을 남길 때 쓴다. 판정자는 외부 서비스가 아니라 세션 판정자다 — 응답은 `--responses`로 오프라인 입력한다.

## 명령

```bash
bazel run //tools:judge -- --list
bazel run //tools:judge -- --question labelRepresentsBody --responses r1.json --record <청크 파일…>
bazel run //tools:judge -- --question bodyHasOneClaim --responses r1.json --responses r2.json --decoys key.json --into /tmp/judge <청크 파일…>
```

## 원본

- 절차: [`docs/method.md` 11. 검증 — V&V 층으로](../../../docs/method.md#11-검증--vv-층으로)
- 도구: `tools/judge.py` (`bazel run //tools:judge`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>]
[--record] [--into <디렉토리>] <청크 파일…>
python3 tools/judge.py --question labelRepresentsBody --responses r1.json --responses r2.json --decoys key.json
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
