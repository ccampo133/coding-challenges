package arrays

import "sort"

// Given an integer array nums, return true if any value appears more than once
// in the array, otherwise return false.
//
// Example 1:
//
// Input: nums = [1, 2, 3, 3]
//
// Output: true
// Example 2:
//
// Input: nums = [1, 2, 3, 4]
//
// Output: false

func ContainsDupe(nums []int) bool {
	for i, n := range nums {
		for j, m := range nums {
			if i != j && n == m {
				return true
			}
		}
	}
	return false
}

func ContainsDupeSort(nums []int) bool {
	// A sorted slice will have duplicates adjacent to each other, e.g.
	// [1, 2, 2, 2, 3, 4]. Therefore, checking if any adjacent pairs match is
	// sufficient.
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			return true
		}
	}
	return false
}

func ContainsDupeSet(nums []int) bool {
	set := make(map[int]struct{})
	for _, n := range nums {
		if _, ok := set[n]; ok {
			return true
		}
		set[n] = struct{}{}
	}
	return false
}
