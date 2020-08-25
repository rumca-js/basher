
import basher

b = basher.BashCtx()

if b.run("dir", True) == 0 and b.run("dir /b", True) == 0:
    print("Success\n")

    print(b.stdoutstack)
    print(b.stderrstack)
else:
    print("An error\n")

    print("Last output")
    print(b.stdoutstack[-1])
    print("Last error")
    print(b.stderrstack[-1])
    print()

    print("Whole std output stack")
    print(b.stdoutstack)
    print()

    print("Whole std error stack")
    print(b.stderrstack)
    print()
