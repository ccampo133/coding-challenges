# https://neetcode.io/problems/design-word-search-data-structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Design a data structure that supports adding new words and searching for
# existing words.
#
# Implement the WordDictionary class:
#
# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots can
# be matched with any letter.
#
# Example 1:
# Input:
# ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may",
# "search", "say", "search", "day", "search", ".ay", "search", "b.."]
#
# Output:
# [null, null, null, null, false, true, true, true]
#
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("day");
# wordDictionary.addWord("bay");
# wordDictionary.addWord("may");
# wordDictionary.search("say"); // return false
# wordDictionary.search("day"); // return true
# wordDictionary.search(".ay"); // return true
# wordDictionary.search("b.."); // return true
# Constraints:
#
# 1 <= word.length <= 20
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
class Node:
    def __init__(self, terminal: bool = False):
        self.chars: dict[chr, Node] = {}
        self.terminal: bool = terminal


class WordDictionary:

    def __init__(self):
        self.root: Node = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Node()
            cur = cur.chars[c]
        cur.terminal = True

    def search(self, word: str) -> bool:
        def search(word: str, root: Node):
            cur = root
            for i, c in enumerate(word):
                if c == ".":
                    for node in cur.chars.values():
                        if search(word[i + 1:], node):
                            return True
                    return False
                else:
                    if c not in cur.chars:
                        return False
                    cur = cur.chars[c]
            return cur.terminal

        return search(word, self.root)


def test1():
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    assert not d.search("pad")
    assert d.search("bad")
    assert d.search(".ad")
    assert d.search("b..")
    assert d.search("...")
    assert d.search("..d")
    assert not d.search("..c")
