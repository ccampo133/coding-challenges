# https://neetcode.io/problems/implement-prefix-tree
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Implement Prefix Tree
# A prefix tree (also known as a trie) is a tree data structure used to
# efficiently store and retrieve keys in a set of strings. Some applications of
# this data structure include auto-complete and spell checker systems.
#
# Implement the PrefixTree class:
#
# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix
# tree (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
# Example 1:
# Input:
# ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do",
# "insert", "do", "search", "do"]
# Output:
# [null, null, true, false, true, null, true]
#
# Explanation:
# PrefixTree prefixTree = new PrefixTree();
# prefixTree.insert("dog");
# prefixTree.search("dog");    // return true
# prefixTree.search("do");     // return false
# prefixTree.startsWith("do"); // return true
# prefixTree.insert("do");
# prefixTree.search("do");     // return true
# Constraints:
#
# 1 <= word.length, prefix.length <= 1000
# word and prefix are made up of lowercase English letters.

class Node:
    def __init__(self, terminal: bool = False):
        self.chars: dict[chr, Node] = {}
        self.terminal: bool = terminal


class PrefixTree:
    def __init__(self):
        self.root: Node = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Node()
            cur = cur.chars[c]
        cur.terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return cur.terminal

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return True


def test1():
    trie = PrefixTree()
    trie.insert("dog")
    assert trie.search("dog")
    assert not trie.search("do")
    assert trie.startsWith("do")
    trie.insert("do")
    assert trie.search("do")


def test2():
    trie = PrefixTree()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
