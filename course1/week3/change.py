# Uses python3
import sys


def get_change(m):
    t, r = m // 10, m % 10
    f, r = r // 5, r % 5
    return t + f + r


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
