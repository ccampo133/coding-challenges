# https://neetcode.io/problems/counting-bits
# https://leetcode.com/problems/counting-bits
# Counting Bits
# Given an integer n, count the number of 1's in the binary representation of
# every number in the range [0, n].
#
# Return an array output where output[i] is the number of 1's in the binary
# representation of i.
#
# Example 1:
# Input: n = 4
# Output: [0,1,1,2,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
#
# Constraints:
#
# 0 <= n <= 1000
def hamming_weight(n: int):
    tot = 0
    while n > 0:
        tot += n & 1
        n >>= 1
    return tot


# O(n log n)
def count_bits(n: int) -> list[int]:
    res = []
    for i in range(n + 1):
        w = hamming_weight(i)
        res.append(w)
    return res


# The O(n) solution is a non-intuitive dynamic programming solution.
# TODO: come back to this.


def test1():
    n = 4
    assert count_bits(n) == [0, 1, 1, 2, 1]
