# https://neetcode.io/problems/number-of-one-bits
# https://leetcode.com/problems/number-of-1-bits/
# Number of One Bits
# You are given an unsigned integer n. Return the number of 1 bits in its
# binary representation.
#
# You may assume n is a non-negative integer which fits within 32-bits.
#
# Example 1:
# Input: n = 00000000000000000000000000010111
# Output: 4

# Example 2:
# Input: n = 01111111111111111111111111111101
#
# Output: 30
def hamming_weight(n: int):
    tot = 0
    while n > 0:
        tot += n & 1
        n >>= 1
    return tot
