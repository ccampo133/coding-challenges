from functools import reduce


def factorial(n):
    return reduce((lambda x, y: x * y), [i for i in range(n, 0, -1)])


def sum_factorial(n):
    return sum([int(c) for c in str(factorial(n))])


if __name__ == '__main__':
    print(sum_factorial(100))
