# https://neetcode.io/problems/is-palindrome
# Is Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward. It is also
# case-insensitive and ignores all non-alphanumeric characters.
#
# Example 1:
#
# Input: s = "Was it a car or a cat I saw?"
#
# Output: true
# Explanation: After considering only alphanumerical characters we have
# "wasitacaroracatisaw", which is a palindrome.
#
# Example 2:
#
# Input: s = "tab a cat"
#
# Output: false
# Explanation: "tabacat" is not a palindrome.
#
# Constraints:
#
# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        c1, c2 = s[i], s[j]
        if not is_alphanum(c1):
            i += 1
        elif not is_alphanum(c2):
            j -= 1
        elif c1.lower() != c2.lower():
            return False
        else:
            i += 1
            j -= 1
    return True


def is_alphanum(c):
    return '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z'
