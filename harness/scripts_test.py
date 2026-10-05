#!/usr/bin/env python3
"""하네스 채널 스크립트의 동작 시험 — 임시 채널에서 프로토콜의 흐름과 거부 규칙을 실제 실행으로 본다.

채널·유저 디렉토리는 `AKB_CHANNEL_DIR`·`AKB_USER_DIR` 로 `TEST_TMPDIR` 아래에 둔다 — 저장소의 채널 실물에는 쓰지
않는다. 스크립트는 호스트 `bash` 로 돌린다. 프로토콜 원본은 harness/README.md 다.

보는 것은 다음과 같다.
1. send → inbox → read-msg → mark 의 정상 흐름과 done 의 archive 이동, id 의 전역 단조 증가.
2. send 의 거부 — 방향(task 는 hci → orchestrator, result·status 는 orchestrator → hci), type 어휘, answer·result 의
   re 필수와 대상 type, task 의 필수 절 여섯, 실재하지 않는 source. 거부된 send 는 번호를 쓰지 않는다.
3. mark 의 거부 — result 없는 task, answer 없는 question 의 done.
4. inbox.sh 의 종료 코드 0 (메시지가 있을 때와 없을 때 모두).
5. watch.sh 가 이미 있는 new 메시지를 바로 감지해 0 으로 끝나고, 없으면 시간 초과로 2 로 끝난다.

사용: bazel test //harness:scripts_test · python3 harness/scripts_test.py
"""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent / "scripts"
TASK_BODY = "## 배경\n시험\n## 목표\n시험\n## 완료조건\n- [ ] 시험\n## 제약\n없음\n## 파급효과\n없음\n## 확인 못 한 것\n없음\n"


class ChannelScripts(unittest.TestCase):
    def setUp(self):
        base = os.environ.get("TEST_TMPDIR") or tempfile.gettempdir()
        self.root = Path(tempfile.mkdtemp(prefix="channel-", dir=base))
        self.chan, self.user = self.root / "channel", self.root / "user"
        for d in ("to_orchestrator", "to_hci", "archive/legacy"):
            (self.chan / d).mkdir(parents=True)
        (self.user / "archive").mkdir(parents=True)
        (self.user / "Q-0001.md").write_text("---\nid: Q-0001\nstatus: answered\nsubject: 시험\ncreated: 2026-10-03\n---\n답: 권장\n",
                                             encoding="utf-8")
        (self.chan / "archive/legacy/old.md").write_text("옛 기록\n", encoding="utf-8")
        self.env = dict(os.environ, AKB_CHANNEL_DIR=str(self.chan), AKB_USER_DIR=str(self.user))

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def run_sh(self, script, *args, stdin="", **env):
        e = dict(self.env, **env)
        return subprocess.run(["bash", str(SCRIPTS / script), *args], input=stdin, env=e,
                              capture_output=True, text=True, timeout=60)

    def send(self, frm, to, typ, subject, body="본문", **env):
        return self.run_sh("send.sh", frm, to, typ, subject, stdin=body, **env)

    def seq(self):
        f = self.chan / ".seq"
        return int(f.read_text()) if f.exists() else 0

    def test_flow(self):
        r = self.send("hci", "orchestrator", "task", "시험 지시", TASK_BODY, SOURCE="Q-0001")
        self.assertEqual(r.returncode, 0, r.stderr)
        msg = self.chan / "to_orchestrator/0001.md"
        text = msg.read_text(encoding="utf-8")
        for line in ("id: 0001", "from: hci", "to: orchestrator", "type: task", "status: new", "source: Q-0001"):
            self.assertIn(line + "\n", text)
        r = self.run_sh("inbox.sh", "orchestrator")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0001", r.stdout)
        r = self.run_sh("read-msg.sh", "1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("subject: 시험 지시", r.stdout)
        self.assertEqual(self.run_sh("mark.sh", "0001", "in_progress").returncode, 0)
        self.assertIn("status: in_progress\n", msg.read_text(encoding="utf-8"))
        r = self.send("orchestrator", "hci", "result", "완료", "수행 요약", RE="0001")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((self.chan / "to_hci/0002.md").exists())
        r = self.run_sh("mark.sh", "1", "done")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(msg.exists())
        self.assertIn("status: done\n", (self.chan / "archive/0001.md").read_text(encoding="utf-8"))
        self.assertEqual(self.seq(), 2)
        self.assertEqual(sorted(p.name for p in self.chan.rglob("*.tmp")), [])

    def test_send_rejects(self):
        self.assertEqual(self.send("hci", "orchestrator", "task", "지시", TASK_BODY).returncode, 0)
        self.assertEqual(self.send("orchestrator", "hci", "question", "질문", RE="0001").returncode, 0)
        bad = [
            (("orchestrator", "hci", "task", "역방향 task"), TASK_BODY, {}),
            (("hci", "orchestrator", "result", "역방향 result"), "본문", {"RE": "0001"}),
            (("hci", "orchestrator", "status", "역방향 status"), "본문", {}),
            (("hci", "orchestrator", "memo", "어휘 밖 type"), "본문", {}),
            (("hci", "hci", "ack", "같은 역할"), "본문", {}),
            (("orchestrator", "hci", "result", "re 없는 result"), "본문", {}),
            (("hci", "orchestrator", "answer", "re 없는 answer"), "본문", {}),
            (("hci", "orchestrator", "answer", "task 에 answer"), "본문", {"RE": "0001"}),
            (("orchestrator", "hci", "result", "question 에 result"), "본문", {"RE": "0002"}),
            (("orchestrator", "hci", "result", "없는 re"), "본문", {"RE": "0099"}),
            (("hci", "orchestrator", "task", "절 없는 task"), "## 배경\n만\n", {}),
            (("hci", "orchestrator", "knowledge", "없는 source"), "본문", {"SOURCE": "Q-0099"}),
        ]
        for args, body, env in bad:
            with self.subTest(args[3]):
                r = self.send(*args, body=body, **env)
                self.assertNotEqual(r.returncode, 0, r.stdout)
                self.assertIn("오류:", r.stderr)
        self.assertEqual(self.seq(), 2)  # 거부된 send 는 번호를 쓰지 않는다
        r = self.send("hci", "orchestrator", "answer", "답", RE="2", SOURCE="Q-0001")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_mark_requires_reply(self):
        self.send("hci", "orchestrator", "task", "지시", TASK_BODY)
        r = self.run_sh("mark.sh", "0001", "done")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("result", r.stderr)
        self.assertTrue((self.chan / "to_orchestrator/0001.md").exists())
        self.send("orchestrator", "hci", "question", "질문")
        r = self.run_sh("mark.sh", "0002", "done")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("answer", r.stderr)
        self.assertNotEqual(self.run_sh("mark.sh", "0001", "finished").returncode, 0)
        self.assertNotEqual(self.run_sh("mark.sh", "0042", "read").returncode, 0)

    def test_inbox_exit_zero(self):
        r = self.run_sh("inbox.sh", "hci")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("비었다", r.stdout)
        self.send("orchestrator", "hci", "status", "진행")
        r = self.run_sh("inbox.sh", "hci")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0001", r.stdout)
        self.assertNotEqual(self.run_sh("inbox.sh", "developer").returncode, 0)

    def test_watch(self):
        r = self.run_sh("watch.sh", "hci", "1", "2")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.send("orchestrator", "hci", "status", "진행")
        r = self.run_sh("watch.sh", "hci", "1", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("0001", r.stdout)

    def test_reset_keeps_legacy(self):
        self.send("orchestrator", "hci", "status", "진행")
        r = self.run_sh("reset.sh", FORCE="1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse((self.chan / "to_hci/0001.md").exists())
        self.assertFalse((self.chan / ".seq").exists())
        self.assertTrue((self.chan / "archive/legacy/old.md").exists())
        self.assertTrue((self.user / "Q-0001.md").exists())


if __name__ == "__main__":
    unittest.main()
