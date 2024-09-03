# https://neetcode.io/problems/two-integer-sum-ii
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.
#
# Return the indices (1-indexed) of two numbers, [index1, index2], such that
# they add up to a given target number target and index1 < index2. Note that
# index1 and index2 cannot be equal, therefore you may not use the same element
# twice.
#
# There will always be exactly one valid solution.
#
# Your solution must use O(1) additional space.
#
# Example 1:
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1,
# index2 = 2. We return [1, 2].
#
# Constraints:
#
# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000

# Intuition:
# Start with the full array. Let L be the leftmost element, R the rightmost.
#
# If L + R = target: We're done
#
# If L + R > target: The rightmost element is too big, because it exceeds the
# target, even when combined with the smallest available element. Since no
# element can be smaller than L, this proves that the rightmost element is
# useless and must be removed.
#
# If L + R < target: The leftmost element is too small, because it is smaller
# than the target, even when combined with the biggest available element.
# Therefore, it must be removed.
#
# Once you removed the leftmost or the rightmost, the algorithm starts over on
# the remaining array.
def two_sum(nums: list[int], tgt: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s > tgt:
            r -= 1
        elif s < tgt:
            l += 1
        else:
            return [l + 1, r + 1]


def two_sum_bruteforce(nums: list[int], tgt: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == tgt:
                return [i + 1, j + 1]


def test1():
    nums = [1, 2, 3, 4]
    tgt = 3
    assert two_sum(nums, tgt) == [1, 2]


def test2():
    nums = [2, 3, 4, 6, 9]
    tgt = 9
    assert two_sum(nums, tgt) == [2, 4]
