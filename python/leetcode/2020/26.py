from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count, prev = 0, None
        for i in range(len(nums)):
            cur = nums[i]
            if prev is not None and cur == prev:
                count += 1
            nums[i - count] = cur
            prev = cur
        return len(nums) - count


if __name__ == '__main__':
    soln = Solution()
    a1, e1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]
    a2, e2 = [0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]
    a3, e3 = [1, 1, 2], [1, 2]
    a4, e4 = [1, 2], [1, 2]
    a5, e5 = [1], [1]
    a6, e6 = [1, 2, 2], [1, 2]
    a7, e7 = [1, 2, 3, 3, 4], [1, 2, 3, 4]
    assert e1 == a1[:soln.removeDuplicates(a1)]
    assert e2 == a2[:soln.removeDuplicates(a2)]
    assert e3 == a3[:soln.removeDuplicates(a3)]
    assert e4 == a4[:soln.removeDuplicates(a4)]
    assert e5 == a5[:soln.removeDuplicates(a5)]
    assert e6 == a6[:soln.removeDuplicates(a6)]
    assert e7 == a7[:soln.removeDuplicates(a7)]
