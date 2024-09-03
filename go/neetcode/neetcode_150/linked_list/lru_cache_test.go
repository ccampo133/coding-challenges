package linked_list

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestLRUCache_1(t *testing.T) {
	c := Constructor(2)
	c.Put(1, 1)
	c.Put(2, 2)
	got := c.Get(1)
	require.Equal(t, 1, got)
	c.Put(3, 3)
	got = c.Get(2)
	require.Equal(t, -1, got)
	c.Put(4, 4)
	got = c.Get(1)
	require.Equal(t, -1, got)
	got = c.Get(3)
	require.Equal(t, 3, got)
	got = c.Get(4)
	require.Equal(t, 4, got)
}
