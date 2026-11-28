---
name: host-prerequisites
description: 새 호스트에서는 send.sh 가 bazel 과 C 컴파일러(gcc) 없이 멈춘다 — 2026-11-28 straw-field-1 이전 때의 경위
metadata:
  type: project
---

2026-11-28 프로젝트를 `straw-field-1`(Ubuntu 24.04.5)로 옮긴 뒤(Q194·Q196) `send.sh` 가 두 번 멈췄다. 첫째는 `bazel` 이 없어서, 둘째는 rules_cc 자동 구성이 "Cannot find gcc or CC" 로 실패해서였다. 유저가 Q197-a 로 bazelisk 를 `/usr/local/bin/bazel` 에, 이어 `build-essential` 을 설치했다.

**Why:** `send.sh` 는 발신 전에 `bazel build //harness:channel_send_check` 를 하므로 툴체인이 없으면 메시지가 하나도 나가지 않는다. 시스템 설치는 interpreter 의 파일 수정 경계 밖이다.

**How to apply:** 새 호스트에서 세션을 시작하면 `which bazel gcc` 를 먼저 본다. 없으면 질문지로 유저 설치(명령 제시, `!` 접두)를 권한다. `/usr/local/bin` 은 떠 있는 세션의 PATH 에 들어 있어 재기동이 필요 없다. [[session-start-cycle]]
