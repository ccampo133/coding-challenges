# https://neetcode.io/problems/string-encode-and-decode
# https://leetcode.com/problems/encode-and-decode-strings/description/
# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The
# encoded string is then decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]
#
# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
#
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

# encode returns a message in the form <header>#<msg>. The forms of `header` and
# `msg` is as follows:
# header: <len(strs)>#<len of each str>, where # a the delimiter.
# msg: The list `strs` concatenated into a single string.
#
# For example, the input ["hello", "world!"] would be returned as
# 2#5#6#helloworld!
def encode(strs: list[str]) -> str:
    hdr = f"{len(strs)}#"
    msg = ""
    for s in strs:
        hdr += f"{len(s)}#"
        msg += s
    return hdr + msg


# decode takes an encoded string, encoded with the scheme described in `encode`,
# and decodes it to return the original input list. For example, the encoded
# message 2#5#6#helloworld! would be returned as ["hello", "world!"]
def decode(s: str) -> list[str]:
    i = 0
    c = ""
    while c != "#":
        c = s[i]
        i += 1
    n = int(s[:i - 1])
    lens = [0] * n
    for j in range(n):
        c = ""
        start = i
        while c != "#":
            c = s[i]
            i += 1
        lens[j] = int(s[start:i - 1])
    msg = [""] * n
    for j, l in enumerate(lens):
        msg[j] = s[i:i + l]
        i += l
    return msg


def test1():
    strs = ["neet", "code", "love", "you"]
    msg = "4#4#4#4#3#neetcodeloveyou"
    assert encode(strs) == msg
    assert decode(msg) == strs


def test2():
    strs = ["we", "say", ":", "yes"]
    msg = "4#2#3#1#3#wesay:yes"
    assert encode(strs) == msg
    assert decode(msg) == strs
