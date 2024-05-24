package top_interview_150

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRemoveDuplicates(t *testing.T) {
	nums := []int{1, 1, 2}
	got := removeDuplicates(nums)
	want := 2
	require.Equal(t, want, got)
	wantNums := []int{1, 2}
	require.Equal(t, wantNums, nums[:got])
}

func TestRemoveDuplicates_2(t *testing.T) {
	nums := []int{0,0,1,1,1,2,2,3,3,4}
	got := removeDuplicates(nums)
	want := 5
	require.Equal(t, want, got)
	wantNums := []int{0,1,2,3,4}
	require.Equal(t, wantNums, nums[:got])
}
