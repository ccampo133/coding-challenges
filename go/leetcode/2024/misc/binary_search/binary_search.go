package binary_search

// https://leetcode.com/problems/binary-search/description/

func search(nums []int, target int) int {
	l, r := 0, len(nums) - 1
	for l <= r {
		mid := (l + r) / 2
		val := nums[mid]
		if val < target {
			l = mid + 1
		} else if val > target {
			r = mid - 1
		} else {
			return mid
		}
	}
	return -1
}
