# https://neetcode.io/problems/missing-number
# Missing Number
# Given an array nums containing n integers in the range [0, n] without any
# duplicates, return the single number in the range that is missing from nums.
#
# Follow-up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
#
# Example 1:
# Input: nums = [1,2,3]
# Output: 0
# Explanation: Since there are 3 numbers, the range is [0,3]. The missing number
# is 0 since it does not appear in nums.
#
# Example 2:
# Input: nums = [0,2]
# Output: 1
# Constraints:
#
# 1 <= nums.length <= 1000

# O(n) time and O(n) space
def missingno(nums: list[int]) -> int:
    s = set()
    for num in nums:
        s.add(num)
    for i in range(len(nums) + 1):
        if i not in s:
            return i


# O(n) time and O(1) space
def missingno_sum(nums: list[int]) -> int:
    missing = 0
    # This is equivalent to doing sum([0...n]) - sum(nums), where n = len(nums)
    for i, num in enumerate(nums):
        missing += (i + 1) - num
    return missing


# There's an XOR solution too which is probably why this is classified under bit
# manipulation. That is really esoteric IMO. Anyway, here it is:
def missingno_xor(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


# This is basically the same as the set answer, except it uses a bit string
# as a set. Each bit is mapped
def missingno_bit(nums):
    # Creates a bit string of len(nums) + 1 w/ all zeros except the left-most
    # bit, which we can ignore
    s = 2 ** (len(nums) + 1)
    for n in nums:
        s = s | (1 << n) # Set's the nth bit to 1 (0-indexed)
    for i in range(len(nums) + 1):
        # Check each bit. If it's zero, it means that bit (and hence number)
        # is missing.
        if (s >> i) & 1 == 0:
            return i
    # This should never happen.
    return -1


def test1():
    nums = [3, 0, 1]
    assert missingno_bit(nums) == 2

def test2():
    nums = [0, 1]
    assert missingno_bit(nums) == 2
