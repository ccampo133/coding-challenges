# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            nums[i - j] = nums[i]
            if nums[i] == val:
                j += 1
        return len(nums) - j


if __name__ == '__main__':
    soln = Solution()
    nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
    val1 = 2
    res1 = soln.removeElement(nums1, val1)
    assert res1 == 5
    assert nums1[:res1] == [0, 1, 3, 0, 4]

    nums2 = [3, 2, 2, 3]
    val2 = 3
    res2 = soln.removeElement(nums2, val2)
    assert res2 == 2
    assert nums2[:res2] == [2, 2]
