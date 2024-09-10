package dictionary

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test1(t *testing.T) {
	d := Constructor()
	d.AddWord("bad")
	d.AddWord("dad")
	d.AddWord("mad")
	require.False(t, d.Search("pad"))
	require.True(t, d.Search("bad"))
	require.True(t, d.Search(".ad"))
	require.True(t, d.Search("b.."))
	require.True(t, d.Search("..."))
	require.True(t, d.Search("..d"))
	require.False(t, d.Search("..c"))
}


func Test2(t *testing.T) {
	d := Constructor()
	d.AddWord("fooo")
	require.False(t, d.Search("foo"))
	require.False(t, d.Search("..."))
	require.True(t, d.Search("...o"))
	require.True(t, d.Search("...."))
	require.True(t, d.Search("...o"))
}


func Test3(t *testing.T) {
	d := Constructor()
	d.AddWord("a")
	d.AddWord("a")
	require.True(t, d.Search("."))
	require.True(t, d.Search("a"))
	require.False(t, d.Search("aa"))
	require.True(t, d.Search("a"))
	require.False(t, d.Search(".a"))
	require.False(t, d.Search("a."))
}
