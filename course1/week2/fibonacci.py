# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    x0, x1 = 0, 1
    for _ in range(n - 1):
        x0, x1 = x1, x0 + x1
    return x1

n = int(input())
print(calc_fib(n))
