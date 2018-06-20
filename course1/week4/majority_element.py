# Uses python3
import sys

def get_majority_element(a, left, right):
    count = {}
    for value in a:
        if value in count.keys():
            count[value] += 1
        else:
            count[value] = 1
    total = len(a)
    for c in count.values():
        if c / total > 0.5:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
