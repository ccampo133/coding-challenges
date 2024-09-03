# https://neetcode.io/problems/anagram-groups
# Anagram Groups
# Given an array of strings strs, group all anagrams together into sublists. You
# may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another
# string, but the order of the characters can be different.
#
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]
#
# Constraints:
#
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

def group_anagrams(strs: list[str]):
    groups = {}
    for s in strs:
        ss = "".join(sorted(s))
        if ss not in groups:
            groups[ss] = []
        groups[ss].append(s)
    return groups.values()


def group_anagrams_hash(strs: list[str]):
    groups = {}
    for s in strs:
        counts = [0] * 26  # 26 possible lowercase letters
        for c in s:
            counts[ord(c) - ord("a")] += 1
        # You can use tuples as keys in Python. This is a 26-length tuple where
        # each index represents the number of occurrences of that letter, e.g.
        # (0, 1, 1, 2 ...) represents (a=0, b=1, c=2, ...). In another language,
        # it might make more sense to use a hash key like 'a0b1c1d2...'.
        key = tuple(counts)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return groups.values()


def test1():
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    got = group_anagrams(strs)
    want = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    assert want == got
