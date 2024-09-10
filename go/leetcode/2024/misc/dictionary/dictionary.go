package dictionary

// https://leetcode.com/problems/design-add-and-search-words-data-structure/

type node struct {
	chars  map[rune]*node
	isWord bool
}

func newNode() *node {
	return &node{chars: make(map[rune]*node)}
}

type WordDictionary struct {
	root *node
}

func Constructor() WordDictionary {
	return WordDictionary{root: newNode()}
}

func (d *WordDictionary) AddWord(word string) {
	cur := d.root
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

func (d *WordDictionary) Search(word string) bool {
	return search(d.root, word)
}

func search(root *node, word string) bool {
	cur := root
	for i, c := range word {
		if c == '.' {
			for _, n := range cur.chars {
				if search(n, word[i + 1:]) {
					return true
				}
			}
			return false
		} else {
			n, ok := cur.chars[c]
			if !ok {
				return false
			}
			cur = n
		}
	}
	return cur.isWord
}
