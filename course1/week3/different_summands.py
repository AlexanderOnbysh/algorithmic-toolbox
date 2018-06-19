# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1
    while n != 0:
        add = i if n - i > i else n
        summands.append(add)
        n -= add
        i += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
