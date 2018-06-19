# Uses python3
import sys


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(a % b, b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
