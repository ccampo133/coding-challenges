def divisors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors


def are_amicable(a, b, da, db):
    return a == db and b == da


# This is slow... O(n ** 2)
def compute(n):
    # Cache the divisors so we can use them later more efficiently (memoization)
    div_sums = {}
    for i in range(n):
        div_sums[i] = sum(divisors(i))

    total = 0
    for i in range(n):
        for j in range(n):
            if i != j and are_amicable(i, j, div_sums[i], div_sums[j]):
                total += i + j
    return total // 2


if __name__ == '__main__':
    print(compute(10000))
