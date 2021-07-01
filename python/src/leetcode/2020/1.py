from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
