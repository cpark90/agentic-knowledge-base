#!/usr/bin/env python3
"""하네스 채널 스크립트의 동작 시험 — 임시 채널에서 프로토콜의 흐름과 거부 규칙을 실제 실행으로 본다.

채널·유저 디렉토리는 `AKB_CHANNEL_DIR`·`AKB_USER_DIR` 로 `TEST_TMPDIR` 아래에 둔다 — 저장소의 채널 실물에는 쓰지
않는다. 스크립트는 호스트 `bash` 로 돌린다. 프로토콜 원본은 harness/README.md 다.

보는 것은 다음과 같다.
1. send → inbox → read-msg → mark 의 정상 흐름과 done 의 archive 이동, id 의 전역 단조 증가.
2. send 의 거부 — 방향(task 는 interpreter → orchestrator, result·status 는 orchestrator → interpreter), type 어휘, answer·result 의
   re 필수와 대상 type, task 의 필수 절 여섯, 실재하지 않는 source. 거부된 send 는 번호를 쓰지 않는다.
3. mark 의 거부 — result 없는 task, answer 없는 question 의 done.
4. inbox.sh 의 종료 코드 0 (메시지가 있을 때와 없을 때 모두).
5. watch.sh 가 이미 있는 new 메시지를 바로 감지해 0 으로 끝나고, 없으면 시간 초과로 2 로 끝난다.
6. 옛 이름 hci 는 interpreter 와 같은 역할이다 — send 는 받아 interpreter 로 적고, inbox·watch 는 같은 수신함을 읽으며,
   watch 는 같은 PID 파일을 쓴다.
7. send 의 발신 전 검사 — 한글 이름 없는 백틱 결정 slug 나 경어를 담은 본문은 거부되고 수신함에 파일이 생기지 않으며 번호도
   쓰지 않는다. 같은 slug 옆에 한글 이름을 적은 본문은 보내진다. 검사는 runfiles 의 //harness:channel_send_check 가 한다.

사용: bazel test //harness:scripts_test · python3 harness/scripts_test.py
"""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent / "scripts"
REPO = Path(__file__).resolve().parent.parent
TASK_BODY = "## 배경\n시험\n## 목표\n시험\n## 완료조건\n- [ ] 시험\n## 제약\n없음\n## 파급효과\n없음\n## 확인 못 한 것\n없음\n"


class ChannelScripts(unittest.TestCase):
    def setUp(self):
        base = os.environ.get("TEST_TMPDIR") or tempfile.gettempdir()
        self.root = Path(tempfile.mkdtemp(prefix="channel-", dir=base))
        self.chan, self.user = self.root / "channel", self.root / "user"
        for d in ("to_orchestrator", "to_interpreter", "archive/legacy"):
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
        r = self.send("interpreter", "orchestrator", "task", "시험 지시", TASK_BODY, SOURCE="Q-0001")
        self.assertEqual(r.returncode, 0, r.stderr)
        msg = self.chan / "to_orchestrator/0001.md"
        text = msg.read_text(encoding="utf-8")
        for line in ("id: 0001", "from: interpreter", "to: orchestrator", "type: task", "status: new", "source: Q-0001"):
            self.assertIn(line + "\n", text)
        r = self.run_sh("inbox.sh", "orchestrator")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0001", r.stdout)
        r = self.run_sh("read-msg.sh", "1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("subject: 시험 지시", r.stdout)
        self.assertEqual(self.run_sh("mark.sh", "0001", "in_progress").returncode, 0)
        self.assertIn("status: in_progress\n", msg.read_text(encoding="utf-8"))
        r = self.send("orchestrator", "interpreter", "result", "완료", "수행 요약", RE="0001")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((self.chan / "to_interpreter/0002.md").exists())
        r = self.run_sh("mark.sh", "1", "done")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(msg.exists())
        self.assertIn("status: done\n", (self.chan / "archive/0001.md").read_text(encoding="utf-8"))
        self.assertEqual(self.seq(), 2)
        self.assertEqual(sorted(p.name for p in self.chan.rglob("*.tmp")), [])

    def test_send_rejects(self):
        self.assertEqual(self.send("interpreter", "orchestrator", "task", "지시", TASK_BODY).returncode, 0)
        self.assertEqual(self.send("orchestrator", "interpreter", "question", "질문", RE="0001").returncode, 0)
        bad = [
            (("orchestrator", "interpreter", "task", "역방향 task"), TASK_BODY, {}),
            (("interpreter", "orchestrator", "result", "역방향 result"), "본문", {"RE": "0001"}),
            (("interpreter", "orchestrator", "status", "역방향 status"), "본문", {}),
            (("interpreter", "orchestrator", "memo", "어휘 밖 type"), "본문", {}),
            (("interpreter", "hci", "ack", "같은 역할"), "본문", {}),
            (("orchestrator", "interpreter", "result", "re 없는 result"), "본문", {}),
            (("interpreter", "orchestrator", "answer", "re 없는 answer"), "본문", {}),
            (("interpreter", "orchestrator", "answer", "task 에 answer"), "본문", {"RE": "0001"}),
            (("orchestrator", "interpreter", "result", "question 에 result"), "본문", {"RE": "0002"}),
            (("orchestrator", "interpreter", "result", "없는 re"), "본문", {"RE": "0099"}),
            (("interpreter", "orchestrator", "task", "절 없는 task"), "## 배경\n만\n", {}),
            (("interpreter", "orchestrator", "knowledge", "없는 source"), "본문", {"SOURCE": "Q-0099"}),
        ]
        for args, body, env in bad:
            with self.subTest(args[3]):
                r = self.send(*args, body=body, **env)
                self.assertNotEqual(r.returncode, 0, r.stdout)
                self.assertIn("오류:", r.stderr)
        self.assertEqual(self.seq(), 2)  # 거부된 send 는 번호를 쓰지 않는다
        r = self.send("interpreter", "orchestrator", "answer", "답", RE="2", SOURCE="Q-0001")
        self.assertEqual(r.returncode, 0, r.stderr)

    def decision_slug(self):
        """발신 전 검사의 이름 원천에서 결정 기록 하나의 slug 를 고른다 — 시험이 특정 결정에 묶이지 않게 한다."""
        rf = os.environ.get("RUNFILES_DIR") or os.environ.get("TEST_SRCDIR")
        main = Path(rf) / "_main" if rf else REPO / "bazel-bin/harness/channel_send_check.runfiles/_main"
        args = (main / "harness/channel_send_check.args").read_text(encoding="utf-8").split("\n")
        return next(a for a in args if a.startswith("kb/dev/decision/") and a.endswith("/conclusion.md")).split("/")[3]

    def test_send_prechecks_message(self):
        slug = self.decision_slug()
        inbox = self.chan / "to_interpreter"
        r = self.send("orchestrator", "interpreter", "knowledge", "이름 없는 slug", f"결정 `{slug}` 를 따른다.\n")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("발신 전 검사가 FAIL", r.stderr)
        self.assertIn(f"`{slug}`(slug) 옆에 한글 이름이 없다", r.stderr)
        r2 = self.send("orchestrator", "interpreter", "knowledge", "경어", "확인했습니다.\n")
        self.assertEqual(r2.returncode, 1, r2.stdout + r2.stderr)
        self.assertIn("경어", r2.stderr)
        self.assertEqual(sorted(p.name for p in inbox.iterdir()), [])  # 거부된 메시지는 수신함에 남지 않는다
        self.assertEqual(self.seq(), 0)  # 거부된 send 는 번호를 쓰지 않는다
        name = r.stderr.split("그대로 적는다: ", 1)[1].splitlines()[0].split(" 또는 ")[0].strip('"')  # 검사가 요구한 한글 이름
        r = self.send("orchestrator", "interpreter", "knowledge", "이름 있는 slug", f"결정 `{slug}`({name})를 따른다.\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        text = (inbox / "0001.md").read_text(encoding="utf-8")
        self.assertIn("id: 0001\n", text)
        self.assertIn(f"`{slug}`({name})", text)
        self.assertEqual(self.seq(), 1)

    def test_mark_requires_reply(self):
        self.send("interpreter", "orchestrator", "task", "지시", TASK_BODY)
        r = self.run_sh("mark.sh", "0001", "done")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("result", r.stderr)
        self.assertTrue((self.chan / "to_orchestrator/0001.md").exists())
        self.send("orchestrator", "interpreter", "question", "질문")
        r = self.run_sh("mark.sh", "0002", "done")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("answer", r.stderr)
        self.assertNotEqual(self.run_sh("mark.sh", "0001", "finished").returncode, 0)
        self.assertNotEqual(self.run_sh("mark.sh", "0042", "read").returncode, 0)

    def test_inbox_exit_zero(self):
        r = self.run_sh("inbox.sh", "interpreter")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("비었다", r.stdout)
        self.send("orchestrator", "interpreter", "status", "진행")
        r = self.run_sh("inbox.sh", "interpreter")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0001", r.stdout)
        self.assertNotEqual(self.run_sh("inbox.sh", "developer").returncode, 0)

    def test_watch(self):
        r = self.run_sh("watch.sh", "interpreter", "1", "2")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.send("orchestrator", "interpreter", "status", "진행")
        r = self.run_sh("watch.sh", "interpreter", "1", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("0001", r.stdout)

    def test_old_name_hci(self):
        r = self.send("hci", "orchestrator", "task", "옛 이름 지시", TASK_BODY)
        self.assertEqual(r.returncode, 0, r.stderr)
        text = (self.chan / "to_orchestrator/0001.md").read_text(encoding="utf-8")
        self.assertIn("from: interpreter\n", text)
        r = self.send("orchestrator", "hci", "status", "진행")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("to: interpreter\n", (self.chan / "to_interpreter/0002.md").read_text(encoding="utf-8"))
        self.assertNotEqual(self.send("hci", "interpreter", "ack", "같은 역할").returncode, 0)
        r = self.run_sh("inbox.sh", "hci")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("0002", r.stdout)
        r = self.run_sh("watch.sh", "hci", "1", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("interpreter 수신함", r.stdout)
        self.assertEqual(self.run_sh("mark.sh", "0002", "read").returncode, 0)  # new 가 없어야 감시가 기다린다
        pid = self.root / ".watch-interpreter.pid"  # 별칭은 정규 이름의 PID 파일을 쓴다 — 감시는 역할마다 하나다
        w = subprocess.Popen(["bash", str(SCRIPTS / "watch.sh"), "interpreter", "1", "30"], env=self.env,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            for _ in range(50):
                if pid.exists():
                    break
                subprocess.run(["sleep", "0.1"])
            r = self.run_sh("watch.sh", "hci", "1", "2")
            self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
            self.assertFalse((self.root / ".watch-hci.pid").exists())
        finally:
            w.terminate()
            w.wait(timeout=10)

    def test_reset_keeps_legacy(self):
        self.send("orchestrator", "interpreter", "status", "진행")
        r = self.run_sh("reset.sh", FORCE="1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse((self.chan / "to_interpreter/0001.md").exists())
        self.assertFalse((self.chan / ".seq").exists())
        self.assertTrue((self.chan / "archive/legacy/old.md").exists())
        self.assertTrue((self.user / "Q-0001.md").exists())


if __name__ == "__main__":
    unittest.main()
