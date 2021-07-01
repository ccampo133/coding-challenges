class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        items = {}
        for i in range(len(nums)):
            n = nums[i]
            items[target - n] = i

        for i in range(len(nums)):
            n = nums[i]
            if n in items and items[n] != i:
                j = items[n]
                return [i, j]


if __name__ == '__main__':
    soln = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    nums = [3, 2, 4]
    target = 6

    res = soln.twoSum(nums, target)

    print(res)