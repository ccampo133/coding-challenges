# https://neetcode.io/problems/binary-search
# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order,
# and an integer target.
#
# Implement a function to search for target within nums. If it exists, then
# return its index, otherwise, return -1.
#
# Your solution must run in O(logn) time.
#
# Example 1:
#
# Input: nums = [-1,0,2,4,6,8], target = 4
#
# [-1, 0, 2]  [4, 6, 8]  mid = 3
# [-1, 0,] [2]  mid = 1   [4, 6]  [8]  mid = 1
# [-1] [0] mid = 1

# Output: 3
# Example 2:
#
# Input: nums = [-1,0,2,4,6,8], target = 3
#
# Output: -1
# Constraints:
#
# 1 <= nums.length <= 10000.
# -10000 < nums[i], target < 10000


def search(nums, tgt):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < tgt:
            l = mid + 1
        elif nums[mid] > tgt:
            r = mid - 1
        else:
            return mid
    return -1
