# https://www.hackerrank.com/challenges/30-binary-numbers/problem
#
# Given a base-10 integer n, convert it to binary (base-2). Then find and print
# the base-10 integer denoting the maximum number of consecutive 1's in n's
# binary representation.


# Converting to string - not as efficient as bit shifting
def count_ones_strings(n: int) -> int:
    b = bin(n)
    max_count, cur_count = 0, 0
    for i in range(2, len(b)):  # skip the 0b
        if b[i] == '1':
            cur_count += 1
        else:
            if cur_count > max_count:
                max_count = cur_count
            cur_count = 0
    return cur_count if cur_count > max_count else max_count


# Bit-shifting is efficient -  O(log n)
def count_ones_shift(n: int) -> int:
    max_count, cur_count = 0, 0
    while n != 0:
        if n & 1 == 1:
            cur_count += 1
        else:
            if cur_count > max_count:
                max_count = cur_count
            cur_count = 0
        n >>= 1
    return cur_count if cur_count > max_count else max_count


if __name__ == '__main__':
    # 1021 = 0b1111111101 -- 8 consecutive ones
    assert count_ones_shift(1021) == 8
