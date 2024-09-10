package remove_nth_node

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRemoveNthFromEnd1(t *testing.T) {
	head := NewList([]int{1, 2, 3, 4, 5})
	head2 := NewList([]int{1, 2, 3, 4, 5})
	n := 2
	got := removeNthFromEnd(head, n)
	got2 := removeNthFromEndTwoPasses(head2, n)
	want := []int{1, 2, 3, 5}
	require.Equal(t, want, got.ToSlice())
	require.Equal(t, want, got2.ToSlice())
}

func TestRemoveNthFromEnd2(t *testing.T) {
	head := NewList([]int{1})
	head2 := NewList([]int{1})
	n := 1
	got := removeNthFromEnd(head, n)
	got2 := removeNthFromEndTwoPasses(head2, n)
	want := []int{}
	require.Equal(t, want, got.ToSlice())
	require.Equal(t, want, got2.ToSlice())
}

func TestRemoveNthFromEnd3(t *testing.T) {
	head := NewList([]int{1, 2})
	head2 := NewList([]int{1, 2})
	n := 1
	got := removeNthFromEnd(head, n)
	got2 := removeNthFromEndTwoPasses(head2, n)
	want := []int{1}
	require.Equal(t, want, got.ToSlice())
	require.Equal(t, want, got2.ToSlice())
}
