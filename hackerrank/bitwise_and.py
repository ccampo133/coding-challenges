# https://www.hackerrank.com/challenges/30-bitwise-and/problem

# O(n^2)
def max_bitwise_and(n, k):
    cur_max = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            res = i & j
            if k > res > cur_max:
                cur_max = res
    return cur_max


# O(1)
# This one is very tricky and I admittedly didn't get it without reading the discussions
def max_bitwise_and_constant(n, k):
    return k - 1 if ((k - 1) | k) <= n else k - 2


if __name__ == '__main__':
    # t, vals = int(input()), []
    # for t_itr in range(t):
    #     vals.append(map(int, input().split()))

    vals = [
        (5, 2),
        (8, 5),
        (2, 2),
    ]
    for val in vals:
        print(max_bitwise_and_constant(*val))
