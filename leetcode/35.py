# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    # O(n)
    # Since the data are sorted, we can do this in O(log n) with binary search (see below)
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i

    def binary_search_iterative(self, nums: List[int], left: int, right: int, target: int):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

    def binary_search_recursive(self, nums: List[int], left: int, right: int, target: int):
        if left > right:
            return left
        mid = (left + right) // 2
        if nums[mid] < target:
            return self.binary_search_recursive(nums, mid + 1, right, target)
        if nums[mid] > target:
            return self.binary_search_recursive(nums, left, mid - 1, target)
        return mid

    # O(log n)
    def searchInsert_binary(self, nums: List[int], target: int) -> int:
        # return self.binary_search_iterative(nums, 0, len(nums) - 1, target)
        return self.binary_search_recursive(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    soln = Solution()

    a, t = [1, 3, 5, 6], 5
    assert soln.searchInsert(a, t) == 2
    assert soln.searchInsert_binary(a, t) == 2

    a, t = [1, 3, 5, 6], 2
    assert soln.searchInsert(a, t) == 1
    assert soln.searchInsert_binary(a, t) == 1

    a, t = [1, 3, 5, 6], 7
    assert soln.searchInsert(a, t) == 4
    assert soln.searchInsert_binary(a, t) == 4

    a, t = [1, 3, 5, 6], 0
    assert soln.searchInsert(a, t) == 0
    assert soln.searchInsert_binary(a, t) == 0
