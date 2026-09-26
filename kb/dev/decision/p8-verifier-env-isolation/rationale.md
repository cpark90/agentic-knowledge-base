---
id: https://agentic-knowledge-base.dev/id/chunk/82790ce1-27f0-4673-b99d-3ce99e02b308
type: decision
level: logical
title_ko: 실행기를 부르는 방식이 판정을 바꾸면 재현이 성립하지 않는다
title: If how the runner is invoked changes the verdict, reproducibility does not hold
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T12:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/2a051063-7217-4597-b03f-4a4346e85b0e
---
**근거** — 2026-09-23 실측이 결함을 드러냈다. `bazel run //tools:vv_run`의 파이썬 스텁이 `PYTHONSAFEPATH=1`을 두고 하위 프로세스가 그것을 물려받아, 케이스가 부르는 `python3 tools/validate.py`가 `import kb_lib`에서 `ModuleNotFoundError`로 죽었다. 같은 케이스가 `python3 tools/vv_run.py`로는 통과했다. **실행기를 부르는 방식이 케이스의 판정을 바꾸고 있었다.**

요구 `reproducible-runs`는 실행이 같은 리비전과 seed에서 재현된다고 정한다. 재현의 전제는 실행 환경이 기록된 것에서만 온다는 것이다. 실행기가 자기 문맥을 하위 프로세스에 흘리면 그 문맥은 기록되지 않고 재현되지도 않는다.

이 결함은 같은 원인의 두 번째 사례다. 첫째는 `bazel run //tools:<검증기>`가 작업 디렉토리를 runfiles 트리로 두어 상대 경로가 자극에 닿지 못한 것이다. 둘 다 **bazel의 실행 문맥이 검증기에게 보이는 것**이 원인이고, 그래서 대책도 하나다 — 문맥을 걷어낸다.

거짓 통과가 건너뜀보다 나쁜 까닭은 판정의 성격에 있다. 건너뜀은 "판정하지 않았다"를 정직하게 적고 감사가 그것을 센다. 거짓 통과는 판정했다고 적으면서 다른 것을 판정한 것이라 감사가 볼 수 없다. `verification-means-trust`가 재려는 것이 바로 이 차이다.
