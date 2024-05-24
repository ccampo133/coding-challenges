def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n, fib, total = 0, 0, 0
    while fib < 4e6:
        fib = fibonacci(n)
        if fib % 2 == 0:
            total += fib
        n += 1
    print(total)
