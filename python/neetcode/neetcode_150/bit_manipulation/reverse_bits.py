# https://neetcode.io/problems/reverse-bits
# Reverse Bits
# Given a 32-bit unsigned integer n, reverse the bits of the binary
# representation of n and return the result.
#
# Example 1:
# Input: n = 00000000000000000000000000010101
# Output:    2818572288 (10101000000000000000000000000000)
# Explanation: Reversing 00000000000000000000000000010101, which represents the
# unsigned integer 21, gives us 10101000000000000000000000000000 which
# represents the unsigned integer 2818572288.

def rev(n: int) -> int:
    res = 0
    for i in range(31):
        res = (res + ((n >> i) & 1)) << 1
    res += (n >> 31) & 1
    return res


def test1():
    n = 0b10101
    assert rev(n) == 0b10101000000000000000000000000000


def test2():
    n = 0b11111111111111111111111111111101
    assert rev(n) == 0b10111111111111111111111111111111


def test3():
    n = 0b01001
    assert rev(n) == 0b10010000000000000000000000000000
