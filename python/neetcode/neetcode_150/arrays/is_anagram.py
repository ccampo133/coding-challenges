# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of
# each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another
# string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
# Constraints:
#
# s and t consist of lowercase English letters.

# time: O(N)
# space: O(N)
def is_anagram_map(s1, s2):
    if len(s1) != len(s2):
        return False
    m1, m2 = {}, {}
    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]
        if c1 not in m1:
            m1[c1] = 0
        if c2 not in m2:
            m2[c2] = 0
        m1[c1] += 1
        m2[c2] += 1
    for c in s1:
        if c not in m2 or m1[c] != m2[c]:
            return False
    return True


# time: O(nlogn)
# space: O(1)
def is_anagram_sorted(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def test_is_anagram1():
    s = "racecar"
    t = "carrace"
    assert is_anagram_map(s, t)
    assert is_anagram_sorted(s, t)


def test_is_anagram2():
    s = "foo"
    t = "off"
    assert not is_anagram_map(s, t)
    assert not is_anagram_sorted(s, t)
