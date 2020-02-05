def get_range(n):
    return range(10 ** (n - 1), 10 ** n)


def reverse_number(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    return rev


def is_palindrome(n):
    return n == reverse_number(n)


def largest_palindrome(n):
    palindrome = 0
    for i in get_range(n):
        for j in get_range(n):
            product = i * j
            if is_palindrome(product) and product > palindrome:
                palindrome = product
    return palindrome


if __name__ == '__main__':
    print(largest_palindrome(3))
