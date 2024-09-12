package add_two_ll

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test1(t *testing.T) {
	l1 := FromSlice([]int{2, 4, 3})
	l2 := FromSlice([]int{5, 6, 4})
	got := addTwoNumbers(l1, l2)
	require.Equal(t, []int{7, 0, 8}, got.ToSlice())
}

func Test2(t *testing.T) {
	l1 := FromSlice([]int{0})
	l2 := FromSlice([]int{0})
	got := addTwoNumbers(l1, l2)
	require.Equal(t, []int{0}, got.ToSlice())
}

func Test3(t *testing.T) {
	l1 := FromSlice([]int{9, 9, 9, 9, 9, 9, 9})
	l2 := FromSlice([]int{9, 9, 9, 9})
	got := addTwoNumbers(l1, l2)
	require.Equal(t, []int{8, 9, 9, 9, 0, 0, 0, 1}, got.ToSlice())
}
