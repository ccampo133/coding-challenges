# https://neetcode.io/problems/top-k-elements-in-list
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent
# elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]
#
# Constraints:
#
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
# O(n log n)
def top_freq(nums: list[int], k: int):
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    sorted_counts = sorted(counts.items(), key=lambda i: i[1], reverse=True)
    res = []
    for i in range(k):
        res.append(sorted_counts[i][0])
    return res

# O(n) - this is a clever bucket sort algorithm.
def top_freq_bucket(nums: list[int], k: int):
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    buckets = [[] for _ in range(len(nums))]
    for num, count in counts.items():
        buckets[count - 1].append(num)
    res = []
    for i in range(len(nums), 0, -1):
        bucket = buckets[i - 1]
        for num in bucket:
            res.append(num)
            if len(res) == k:
                return res
    return res


def test1():
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    assert top_freq(nums, k) == [3, 2]
    assert top_freq_bucket(nums, k) == [3, 2]


def test2():
    nums = [7, 7]
    k = 1
    assert top_freq(nums, k) == [7]
    assert top_freq_bucket(nums, k) == [7]

def test3():
    nums = [1]
    k = 1
    assert top_freq(nums, k) == [1]
    assert top_freq_bucket(nums, k) == [1]
