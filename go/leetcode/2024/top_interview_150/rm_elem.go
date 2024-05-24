package top_interview_150

// Given an integer array nums and an integer val, remove all occurrences of val
// in nums in-place. The order of the elements may be changed. Then return the
// number of elements in nums which are not equal to val.
//
// Consider the number of elements in nums which are not equal to val be k, to
// get accepted, you need to do the following things:
//
// 1. Change the array nums such that the first k elements of nums contain the
//	  elements which are not equal to val. The remaining elements of nums are
//	  not important as well as the size of nums.
// 2. Return k.
//
// Custom judge:
//
// The judge will test your solution with the following code:
//
//   int[] nums = [...]; // Input array
//   int val = ...; // Value to remove
//   int[] expectedNums = [...]; // The expected answer with correct length.
//                               // It is sorted with no values equaling val.
//
//   int k = removeElement(nums, val); // Calls your implementation
//
//   assert k == expectedNums.length;
//   sort(nums, 0, k); // Sort the first k elements of nums
//   for (int i = 0; i < actualLength; i++) {
//       assert nums[i] == expectedNums[i];
//   }
//
// If all assertions pass, then your solution will be accepted.
//
// Ref: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
func removeElement(nums []int, val int) int {
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}
