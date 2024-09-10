package trie

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test1(t *testing.T) {
	trie := Constructor()
	trie.Insert("dog")
	require.True(t, trie.Search("dog"))
	require.False(t, trie.Search("do"))
	require.True(t, trie.StartsWith("do"))
	trie.Insert("do")
	require.True(t, trie.Search("do"))
}

func Test2(t *testing.T) {
	trie := Constructor()
	trie.Insert("apple")
	require.True(t, trie.Search("apple"))
	require.False(t, trie.Search("app"))
	require.True(t, trie.StartsWith("app"))
	trie.Insert("app")
	require.True(t, trie.Search("app"))
}
