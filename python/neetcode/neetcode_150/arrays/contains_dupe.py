# https://neetcode.io/problems/duplicate-integer
# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false

# time: O(n2)
# space: O(1)
def contains_dupe(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False


# time: O(n)
# space: O(n)
def contains_dupe_set(nums):
    s = set()
    for n in nums:
        if n in s:
            return True
        s.add(n)
    return False


# time: O(nlogn)
# space: O(1)
def contains_dupe_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def test_contains_dupe1():
    nums = [1, 2, 3, 4]
    assert not contains_dupe(nums)
    assert not contains_dupe_set(nums)
    assert not contains_dupe_sort(nums)


def test_contains_dupe2():
    nums = [1, 2, 3, 3]
    assert contains_dupe(nums)
    assert contains_dupe_set(nums)
    assert contains_dupe_sort(nums)


def test_contains_dupe3():
    nums = [2, 1, 3, 6, 5, 1, 8]
    assert contains_dupe(nums)
    assert contains_dupe_set(nums)
    assert contains_dupe_sort(nums)
