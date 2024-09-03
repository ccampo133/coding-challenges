# https://neetcode.io/problems/three-integer-sum
# https://leetcode.com/problems/3sum/description/
# Three Integer Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k
# are all distinct.
#
# The output should not contain any duplicate triplets. You may return the
# output and the triplets in any order.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
#
# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5
#
# Ref: https://en.wikipedia.org/wiki/3SUM

def three_sum(nums: list[int]):
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue
        two_sums = two_sum(nums[i + 1:], -1 * n)
        for elem in two_sums:
            j, k = elem
            res.append([n, nums[i + j + 1], nums[i + k + 1]])
    return res


def two_sum(nums: list[int], tgt: int) -> list[list[int]]:
    l, r = 0, len(nums) - 1
    res = []
    while l < r:
        s = nums[l] + nums[r]
        if s > tgt:
            r -= 1
        elif s < tgt:
            l += 1
        else:
            res.append([l, r])
            r -= 1
            l += 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
    return res


def test1():
    nums = [-1, 0, 1, 2, -1, -4]
    assert three_sum(nums) == [[-1, -1, 2], [-1, 0, 1]]


def test2():
    nums = [-2, 0, 0, 2, 2]
    assert three_sum(nums) == [[-2, 0, 2]]
