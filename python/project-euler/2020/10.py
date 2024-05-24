def sieve(n):
    a = [True] * n
    for i in range(2, int(n ** 0.5)):
        if a[i]:
            for j in range(i ** 2, n, i):
                a[j] = False

    return [i for i in range(len(a)) if a[i] and i > 1]


if __name__ == '__main__':
    print(sum(sieve(2000000)))
