# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

# Trial division
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    n, nums = int(input()), []
    for i in range(n):
        nums.append(int(input()))

    # nums = [5, 97, 98, 3]
    # nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008,
    #         1000000009]
    # nums = [1000000006]
    for num in nums:
        print('Prime' if is_prime(num) else 'Not prime')
