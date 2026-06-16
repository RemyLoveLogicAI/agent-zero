import os
import platform
import select
import subprocess
import time
import sys
from typing import Optional, Tuple
from helpers import runtime
from plugins._code_execution.helpers import tty_session
from plugins._code_execution.helpers.shell_ssh import clean_string

class LocalInteractiveSession:
    def __init__(self, cwd: str|None = None):
        self.session: tty_session.TTYSession|None = None
        self.full_output = ''
        self.cwd = cwd

    async def connect(self):
        env = os.environ.copy()
        env["GIT_PAGER"] = "cat"
        env["PAGER"] = "cat"
        self.session = tty_session.TTYSession(
            runtime.get_terminal_executable(), cwd=self.cwd, env=env
        )
        await self.session.start()
        await self.session.read_full_until_idle(idle_timeout=1, total_timeout=1)