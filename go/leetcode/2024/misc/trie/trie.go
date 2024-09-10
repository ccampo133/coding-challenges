package trie

// https://neetcode.io/problems/implement-prefix-tree
// https://leetcode.com/problems/implement-trie-prefix-tree/description/
// Implement Prefix Tree`
// A prefix tree (also known as a trie) is a tree data structure used to
// efficiently store and retrieve keys in a set of strings. Some applications of
// this data structure include auto-complete and spell checker systems.
//
// Implement the PrefixTree class:
//
// PrefixTree() Initializes the prefix tree object.
// void insert(String word) Inserts the string word into the prefix tree.
// boolean search(String word) Returns true if the string word is in the prefix
// tree (i.e., was inserted before), and false otherwise.
// boolean startsWith(String prefix) Returns true if there is a previously
// inserted string word that has the prefix prefix, and false otherwise.
//
// Example 1:
// Input:
// ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do",
// "insert", "do", "search", "do"]
// Output:
// [null, null, true, false, true, null, true]
//
// Explanation:
// PrefixTree prefixTree = new PrefixTree();
// prefixTree.insert("dog");
// prefixTree.search("dog");    // return true
// prefixTree.search("do");     // return false
// prefixTree.startsWith("do"); // return true
// prefixTree.insert("do");
// prefixTree.search("do");     // return true
// Constraints:
//
// 1 <= word.length, prefix.length <= 1000
// word and prefix are made up of lowercase English letters.

type node struct {
	chars  map[rune]*node
	isWord bool
}

func newNode() *node {
	return &node{chars: make(map[rune]*node)}
}

type Trie struct {
	root *node
}

func Constructor() Trie {
	return Trie{root: newNode()}
}

func (t *Trie) Insert(word string) {
	cur := t.root
	for _, c := range word {
		n, ok := cur.chars[c]
		if !ok {
			n = newNode()
			cur.chars[c] = n
		}
		cur = n
	}
	cur.isWord = true
}

func (t *Trie) Search(word string) bool {
	cur := t.root
	for _, c := range word {
		n, ok := cur.chars[c]
		if !ok {
			return false
		}
		cur = n
	}
	return cur.isWord
}

func (t *Trie) StartsWith(prefix string) bool {
	cur := t.root
	for _, c := range prefix {
		n, ok := cur.chars[c]
		if !ok {
			return false
		}
		cur = n
	}
	return true
}
