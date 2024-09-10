package inmemfs

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_Example1(t *testing.T) {
	fs := Constructor()
	ls := fs.Ls("/")
	require.Empty(t, ls)
	fs.Mkdir("/a/b/c")
	fs.AddContentToFile("/a/b/c/d", "hello")
	ls = fs.Ls("/")
	require.Equal(t, []string{"a"}, ls)
	content := fs.ReadContentFromFile("/a/b/c/d")
	require.Equal(t, "hello", content)
}

func Test_Example2(t *testing.T) {
	fs := Constructor()
	ls := fs.Ls("/")
	require.Empty(t, ls)
	fs.Mkdir("/a")
	fs.Mkdir("/b")
	fs.Mkdir("/c")
	fs.AddContentToFile("/a/foo", "foo")
	fs.AddContentToFile("/a/foo", "bar")
	fs.AddContentToFile("/a/bar", "bar")
	ls = fs.Ls("/")
	require.Equal(t, []string{"a", "b", "c"}, ls)
	content := fs.ReadContentFromFile("/a/foo")
	require.Equal(t, "foobar", content)
	content = fs.ReadContentFromFile("/a/bar")
	require.Equal(t, "bar", content)
}

func Test_Example3(t *testing.T) {
	fs := Constructor()
	fs.Mkdir("/goowmfn")
	ls := fs.Ls("/goowmfn")
	require.Empty(t, ls)
	ls = fs.Ls("/")
	require.Equal(t, []string{"goowmfn"}, ls)
	fs.Mkdir("/z")
	ls = fs.Ls("/")
	require.Equal(t, []string{"goowmfn", "z"}, ls)
	ls = fs.Ls("/")
	require.Equal(t, []string{"goowmfn", "z"}, ls)
	fs.AddContentToFile("/goowmfn/c", "shetopcy")
	ls = fs.Ls("/z")
	require.Empty(t, ls)
	ls = fs.Ls("/goowmfn/c")
	require.Equal(t, []string{"c"}, ls)
	ls = fs.Ls("/goowmfn")
	require.Equal(t, []string{"c"}, ls)
}
