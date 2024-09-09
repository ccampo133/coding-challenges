# https://neetcode.io/problems/products-of-array-discluding-self
# https://leetcode.com/problems/product-of-array-except-self
# Products of Array Excluding Self
# Given an integer array nums, return an array output where output[i] is the
# product of all the elements of nums except nums[i].
#
# Each product is guaranteed to fit in a 32-bit integer.
#
# Follow-up: Could you solve it in O(n) time without using the division
# operation?
#
# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
#
# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]
#
# Constraints:
#
# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

def prod_divide(nums: list[int]) -> list[int]:
    p = nums[0]
    for i in range(1, len(nums)):
        p *= nums[i]
    res = []
    for n in nums:
        res.append(p // n)
    return res


def prod(nums: list[int]) -> list[int]:
    res = [1] * (len(nums))
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
