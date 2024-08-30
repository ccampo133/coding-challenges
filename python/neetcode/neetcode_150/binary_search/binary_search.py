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

# first stab at this, w/o having written it in a while
def search_recur(nums, tgt):
    print("foo")
    if len(nums) == 1:
        if nums[0] == tgt:
            return 0
        return -1
    mid = len(nums) // 2
    left = nums[:mid]
    l = search_recur(left, tgt)
    if l != -1:
        return l
    right = nums[mid:]
    r = search_recur(right, tgt)
    if r != -1:
        return mid + r
    return -1


def search(nums, tgt):
    l, r = 0, len(nums) - 1
    while l <= r:
        print("foo")
        mid = (l + r) // 2
        if nums[mid] < tgt:
            l = mid + 1
        elif nums[mid] > tgt:
            r = mid - 1
        else:
            return mid
    return -1

def test1():
    nums = [-1, 0, 2, 4, 6, 8]
    tgt = 4
    assert search(nums, tgt) == 3


def test2():
    nums = [-1, 0, 2, 4, 6, 8]
    tgt = 3
    assert search(nums, tgt) == -1


def test3():
    nums = [-1, 0, 3, 5, 9, 12]
    tgt = 9
    assert search(nums, tgt) == 4


def test4():
    nums = [-1, 0, 3, 5, 9, 12]
    tgt = -1
    assert search(nums, tgt) == 0
