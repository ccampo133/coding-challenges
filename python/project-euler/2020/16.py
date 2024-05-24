# O(log n)
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


# O(s) where s = number of digits in 2**n
def compute(n):
    val = 2 ** n
    val_str = str(val)
    digits = [int(c) for c in val_str]
    return sum(digits)


# O(log 2**n) == O(n)
def compute2(n):
    return sum_digits(2 ** n)


if __name__ == '__main__':
    print(compute(1000))
    print(compute2(1000))
