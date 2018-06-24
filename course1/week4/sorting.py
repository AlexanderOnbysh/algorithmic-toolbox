# Uses python3
import sys


def partition3(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    return partition3([x for x in a if x < pivot]) + \
           [x for x in a if x == pivot] + \
           partition3([x for x in a if x > pivot])


def randomized_quick_sort(a):
    return partition3(a)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort(a)
    for x in a:
        print(x, end=' ')
