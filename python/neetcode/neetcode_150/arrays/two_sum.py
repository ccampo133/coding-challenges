# https://neetcode.io/problems/two-integer-sum
# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i
# and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that
# satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
#
# Input:
# nums = [3,4,5,6], target = 7
#
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
#
# Input: nums = [4,5,6], target = 10
#
# Output: [0,2]
# Example 3:
#
# Input: nums = [5,5], target = 10
#
# Output: [0,1]
# Constraints:
#
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# time: O(n2)
# space: O(1)
def two_sum_slow(nums, tgt):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == tgt:
                return [i, j]


# time: O(n)
# space: O(n)
def two_sum_fast(nums, tgt):
    m = {}
    for i, n in enumerate(nums):
        d = tgt - n
        if d in m:
            return [i, m[d]]
        m[n] = i
