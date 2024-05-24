package top_interview_150

// Given an integer array nums sorted in non-decreasing order, remove the
// duplicates in-place such that each unique element appears only once. The
// relative order of the elements should be kept the same. Then return the
// number of unique elements in nums.
//
// Consider the number of unique elements of nums to be k, to get accepted, you
// need to do the following things:
//
//  1. Change the array nums such that the first k elements of nums contain the
//     unique elements in the order they were present in nums initially. The
//     remaining elements of nums are not important as well as the size of nums.
//  2. Return k.
//
// Custom judge:
//
// The judge will test your solution with the following code:
//
//	int[] nums = [...]; // Input array
//	int[] expectedNums = [...]; // The expected answer with correct length
//
//	int k = removeDuplicates(nums); // Calls your implementation
//
//	assert k == expectedNums.length;
//	for (int i = 0; i < k; i++) {
//	    assert nums[i] == expectedNums[i];
//	}
//
// If all assertions pass, then your solution will be accepted.
//
// Ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
func removeDuplicates(nums []int) int {
	i := 0
	for j := 1; j < len(nums); j++ {
		val := nums[i]
		cur := nums[j]
		if cur != val {
			i++
			nums[i] = cur
		}
	}
	return i + 1
}
