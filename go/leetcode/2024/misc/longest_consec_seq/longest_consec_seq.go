package longest_consec_seq

// https://leetcode.com/problems/longest-consecutive-sequence/description/

func longestConsecutive(nums []int) int {
	set := make(map[int]bool)
	for _, num := range nums {
		set[num] = true
	}
	res := 0
	for _, num := range nums {
		if !set[num - 1] {
			count := 1
			for set[num + count] {
				count++
			}
			if count > res {
				res = count
			}
		}
	}
	return res
}
