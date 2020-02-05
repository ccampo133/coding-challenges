# See: https://en.wikipedia.org/wiki/Primality_test#Simple_methods
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


# This is slow, but correct
def largest_prime_factor(n):
    factor = 0
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            if i >= factor:
                factor = i

    if factor == 0:
        return None

    return factor


# See: https://en.wikipedia.org/wiki/Trial_division
def largest_prime_factor_fast(n):
    p, factor = 2, n
    while p * p <= factor:
        if factor % p == 0:
            factor //= p
        else:
            p += 2 if p > 2 else 1
    return factor


if __name__ == '__main__':
    print(largest_prime_factor_fast(600851475143))
