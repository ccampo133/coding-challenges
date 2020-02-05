# This isn't necessary to this solution, but helpful for testing
def sieve(n):
    a = [True] * n
    for i in range(2, int(n ** 0.5)):
        if a[i]:
            for j in range(i ** 2, n, i):
                a[j] = False

    return [i for i in range(len(a)) if a[i] and i > 1]


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def get_nth_prime(n):
    count, i = 0, 1
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


if __name__ == '__main__':
    print(get_nth_prime(10001))
