# Validate Parentheses
# You are given a string s consisting of the following characters: '(', ')',
# '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
#
# Input: s = "[]"
#
# Output: true
# Example 2:
#
# Input: s = "([{}])"
#
# Output: true
# Example 3:
#
# Input: s = "[(])"
#
# Output: false
# Explanation: The brackets are not closed in the correct order.
#
# Constraints:
#
# 1 <= s.length <= 1000

open_parens = {
    '}': '{',
    ')': '(',
    ']': '['
}


def is_valid(s):
    stk = []
    for c in s:
        if is_open(c):  # alternatively: if c not in open_parens
            stk.append(c)
        else:
            if len(stk) == 0:
                return False
            last = stk.pop()
            if last != open_parens[c]:
                return False
    return len(stk) == 0


def is_open(c):
    return c == '(' or c == '[' or c == '{'


def test_is_valid1():
    s = '[]'
    assert is_valid(s)


def test_is_valid2():
    s = '([{}])'
    assert is_valid(s)


def test_is_valid3():
    s = '[(])'
    assert not is_valid(s)


def test_is_valid4():
    s = '(){}[]'
    assert is_valid(s)


def test_is_valid5():
    s = '(){}[]}'
    assert not is_valid(s)


def test_is_valid6():
    s = '(('
    assert not is_valid(s)


def test_is_valid7():
    s = '))'
    assert not is_valid(s)


def test_is_valid8():
    s = ']'
    assert not is_valid(s)
