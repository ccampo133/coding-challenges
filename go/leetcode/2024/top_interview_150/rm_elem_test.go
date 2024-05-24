package top_interview_150

import (
	"slices"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRemoveElement(t *testing.T) {
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	val := 2
	got := removeElement(nums, val)
	want := 5
	require.Equal(t, want, got)
	slices.Sort(nums[:got])
	wantNums := []int{0, 0, 1, 3, 4}
	require.Equal(t, wantNums, nums[:got])
}
