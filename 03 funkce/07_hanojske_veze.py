def hanoi(n, source, target, helper):
    if n == 0:
        return 0
    tahy1 = hanoi(n-1, source, helper, target)

    print(f"{source} --> {target}")
    tahy_stred = 1

    tahy2 = hanoi(n-1, helper, target, source)

    return tahy1 + tahy_stred + tahy2


n = 10
print(hanoi(n, "A", "C", "B"))
print((2**n)-1)