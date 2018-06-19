# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    ratio = [v / w for v, w in zip(values, weights)]
    s = sorted(zip(ratio, values, weights), reverse=True)
    total_value = 0
    capacity_left = capacity
    for ratio, value, weight in s:
        take = min(capacity_left, weight)
        capacity_left -= take
        total_value += take / weight * value

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
