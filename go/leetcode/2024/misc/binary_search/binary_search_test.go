package binary_search

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test1(t *testing.T) {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9
	require.Equal(t, 4, search(nums, target))
}

func Test2(t *testing.T) {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 2
	require.Equal(t, -1, search(nums, target))
}

func Test3(t *testing.T) {
	nums := []int{5}
	target := 5
	require.Equal(t, 0, search(nums, target))
}
