package longest_consec_seq

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test1(t *testing.T) {
	nums := []int{100, 4, 200, 1, 3, 2}
	require.Equal(t, 4, longestConsecutive(nums))
}

func Test2(t *testing.T) {
	nums := []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}
	require.Equal(t, 9, longestConsecutive(nums))
}
