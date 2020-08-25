# Overview

This script allows to write shell scripts more easily.

Other nice alternatives:
[Pysh](https://github.com/yunabe/pysh)

# Use

This is an example code for Windows.

```
b = basher.BashCtx()

if b.run(r"python.exe --version", False) == 0 and b.run("dir", True) == 0 and b.run("dir /b", True) == 0:
    print("Success. Print last output")
    print(b.stdoutstack[-1])
    print(b.stderrstack[-1])
```

# TODO
make setuptool out of this.
