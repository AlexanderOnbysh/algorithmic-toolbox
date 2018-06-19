# Uses python3
import sys


def pisano(modulo):
    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):
        buffer = (previous + current) % modulo
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


def get_fibonacci_huge(n, m):
    return fibonacci(n % pisano(m), m)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
