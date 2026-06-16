import asyncio
import os
import sys
from typing import Optional, Tuple
from helpers import runtime
from plugins._code_execution.helpers import tty_session
from plugins._code_execution.helpers.shell_ssh import clean_string


class LocalInteractiveSession:
    def __init__(self, cwd: str|None = None):
        self.cwd = cwd
        self.session = None

    async def connect(self):
        env = os.environ.copy()
        env["GIT_PAGER"] = "cat"
        env["PAGER"] = "cat"
        self.session = tty_session.TTYSession(runtime.get_terminal_executable(), cwd=self.cwd, env=env)
        await self.session.start()
        await self.session.read_full_until_idle(idle_timeout=1, total_timeout=1)

    async def close(self):
        if self.session:
            session = self.session
            self.session = None
            try:
                await session.close()
            except Exception:
                try:
                    session.kill()
                except Exception:
                    pass

    async def send_command(self, command: str):
        if not self.session:
            raise RuntimeError("Session not connected")
        await self.session.send(command)

    async def read_output(self, timeout=1, reset_full_output=False):
        if not self.session:
            raise RuntimeError("Session not connected")
        return await self.session.read_output(timeout=timeout, reset_full_output=reset_full_output)