package top_interview_150

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRemoveDuplicates2(t *testing.T) {
	nums := []int{1, 1, 2}
	got := removeDuplicates2(nums)
	want := 3
	require.Equal(t, want, got)
	wantNums := []int{1, 1, 2}
	require.Equal(t, wantNums, nums[:got])
}

func TestRemoveDuplicates2_2(t *testing.T) {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	got := removeDuplicates2(nums)
	want := 9
	require.Equal(t, want, got)
	wantNums := []int{0, 0, 1, 1, 2, 2, 3, 3, 4}
	require.Equal(t, wantNums, nums[:got])
}

func TestRemoveDuplicates2_3(t *testing.T) {
	nums := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	got := removeDuplicates2(nums)
	want := 7
	require.Equal(t, want, got)
	wantNums := []int{0, 0, 1, 1, 2, 3, 3}
	require.Equal(t, wantNums, nums[:got])
}
