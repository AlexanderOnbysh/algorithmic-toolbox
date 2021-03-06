# Uses python3
import sys


def pisano(modulo):
    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):  # 1
        buffer = (previous + current) % modulo  # 2
        previous = current
        current = buffer

        result += 1

    return result


def fibonacci(number, modulo):
    if number < 2:
        return number

    results = [1, 1]
    for _ in range(number - 2):
        results.append((results[-1] + results[-2]) % modulo)

    return results[-1]


def get_fibonacci_huge_naive(n, m):
    return fibonacci(n % pisano(m), m)


def fibonacci_sum(n):
    if n <= 1:
        return n
    answer = get_fibonacci_huge_naive(n + 2, 10) - 1
    return 9 if answer == -1 else answer


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
