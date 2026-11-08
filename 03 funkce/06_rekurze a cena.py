def faktorial(n):
    if n > 1:
        return n * faktorial(n-1)
    else:
        return 1



def fib(n): 
    if n == 1:
        return 1, 1
    if n == 0:
        return 0, 1

    hodnota1, volani1 = fib(n-1)
    hodnota2, volani2 = fib(n-2)
    return hodnota1 + hodnota2, 1 + volani1 + volani2

def fib_iter(n):
    if n == 1:
        return 1, 1
    if n == 0:
        return 0, 1
    a = 0
    b = 1
    i = 1
    for _ in range(2, n+1):
        i += 1
        c = a+b
        a = b
        b = c
    return b, i

def fib_memo(n, memo = {}):
    if n in memo:
        return memo[n]

    if n == 1:
        return 1
    if n == 0:
        return 0

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


print(faktorial(5))
print(f"hodnota = {fib(10)[0]}, volání = {fib(10)[1]}")
print(f"hodnota = {fib(20)[0]}, volání = {fib(20)[1]}")
print(f"hodnota = {fib(25)[0]}, volání = {fib(25)[1]}")
print("---- n = 30 -----")
print(f"rek: hodnota = {fib(30)[0]}, volání = {fib(30)[1]}")
print(f"iter: hodnota = {fib_iter(30)[0]}, iterace = {fib_iter(30)[1]}")
print(f"memo: hodnota = {fib_memo(30)}")
