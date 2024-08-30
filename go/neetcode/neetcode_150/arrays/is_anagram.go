package arrays

import (
	"slices"
)

// Is Anagram
// Given two strings s and t, return true if the two strings are anagrams of
// each other, otherwise return false.
//
// An anagram is a string that contains the exact same characters as another
// string, but the order of the characters can be different.
//
// Example 1:
//
// Input: s = "racecar", t = "carrace"
//
// Output: true
// Example 2:
//
// Input: s = "jar", t = "jam"
//
// Output: false
// Constraints:
//
// s and t consist of lowercase English letters.

// Time: O(N + M)
// Space: O(N + M)
func IsAnagram(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	runes1, runes2 := []rune(s1), []rune(s2)
	set1 := make(map[rune]int, len(runes1))
	set2 := make(map[rune]int, len(runes2))
	for i := 0; i < len(runes1); i++ {
		set1[runes1[i]] += 1
		set2[runes2[i]] += 1
	}
	for _, c := range runes2 {
		if set1[c] != set2[c] {
			return false
		}
	}
	return true
}

// Time: O(NlogN + MlogM)
// Space: O(1)
func IsAnagramSort(s1, s2 string) bool {
	runes1, runes2 := []rune(s1), []rune(s2)
	slices.Sort(runes1)
	slices.Sort(runes2)
	return string(runes1) == string(runes2)
}
