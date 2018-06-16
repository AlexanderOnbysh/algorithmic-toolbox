# python3


def max_pairwise_product(numbers):
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)
    return first_max * second_max

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
