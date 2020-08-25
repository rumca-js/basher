"""
@brief This module allows to run shell scripts more easily.

b = basher.BashCtx()

if b.run("dir", True) == 0 and b.run("dir /b", True) == 0:
    print("Success. Print last output")
    print(b.stdoutstack[-1])
    print(b.stderrstack[-1])
"""
import subprocess


class EmptyProcess(object):
    pass


class BashCtx(object):

    def __init__(self):
        self.stdoutstack = []
        self.stderrstack = []
        self.USE_SHELL = False

    def run(self, command, thisshell = None):
        shell_setting = self.USE_SHELL

        if thisshell is not None:
            shell_setting = thisshell

        procout = None
        try:
            procout = subprocess.run(command, shell=shell_setting, capture_output=True)
        except Exception as E:
            procout = EmptyProcess()
            procout.returncode = -1
            procout.stdout = str(E)
            procout.stderr = str(E)

        if procout is not None:
            self.stdoutstack.append(procout.stdout)
            self.stderrstack.append(procout.stderr)

            return procout.returncode

    def clean_stacks(self):
        self.stdoutstack.clear()
        self.stderrstack.clear()
