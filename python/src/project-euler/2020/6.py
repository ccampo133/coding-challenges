def sum_of_squares(n):
    return sum([i ** 2 for i in range(1, n + 1)])


def square_of_sum(n):
    return sum([i for i in range(1, n + 1)]) ** 2


if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_squares(100))
