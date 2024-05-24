package top_interview_150

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMerge(t *testing.T) {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)

	want := []int{1, 2, 2, 3, 5, 6}
	require.Equal(t, want, nums1)
}

func TestMerge_2(t *testing.T) {
	nums1 := []int{4, 5, 6, 0, 0, 0}
	nums2 := []int{1, 2, 3}
	merge(nums1, 3, nums2, 3)

	want := []int{1, 2, 3, 4, 5, 6}
	require.Equal(t, want, nums1)
}

func TestMerge_3(t *testing.T) {
	nums1 := []int{0}
	nums2 := []int{1}
	merge(nums1, 0, nums2, 1)

	want := []int{1}
	require.Equal(t, want, nums1)
}
