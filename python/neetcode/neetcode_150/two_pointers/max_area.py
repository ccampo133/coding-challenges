# https://neetcode.io/problems/max-water-container
# https://leetcode.com/problems/container-with-most-water/description/
# Max Water Container
# You are given an integer array heights where heights[i] represents the height
# of the ith bar.
#
# You may choose any two bars to form a container. Return the maximum amount o
# water a container can store.
#
# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36
#
# Example 2:
# Input: height = [2,2,2]
# Output: 4
#
# Constraints:
#
# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

def max_area(h: list[int]) -> int:
    l, r = 0, len(h) - 1
    res = 0
    while l < r:
        hl, hr = h[l], h[r]
        a = (r - l) * min(hl, hr)
        res = max(res, a)
        if hl < hr:
            l += 1
        elif hr <= hl:
            r -= 1
    return res


def test1():
    h = [1,7,2,5,4,7,3,6]
    assert max_area(h) == 36


def test2():
    h = [2,2,2]
    assert max_area(h) == 4
