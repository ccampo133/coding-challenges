def n_divisors(n):
    num_divisors, sqrt = 0, int(n ** 0.5)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            num_divisors += 2

    if sqrt * sqrt == n:
        num_divisors -= 1

    return num_divisors


def triangle_n_divisors(n):
    num, i = 0, 1
    while n_divisors(num) < n:
        num += i
        i += 1
    return num


if __name__ == '__main__':
    print(triangle_n_divisors(500))
