class Solution:
    # O(nm) - Brute Force
    # Note that a KMP implementation will do this in O(n)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
        return -1


if __name__ == '__main__':
    soln = Solution()

    haystack = 'hello'
    needle = 'll'
    res = soln.strStr(haystack, needle)
    assert res == 2

    haystack2 = 'aaaaa'
    needle2 = 'baa'
    res = soln.strStr(haystack2, needle2)
    assert res == -1

    haystack3 = 'hello darkness my old friend'
    needle3 = 'dark'
    res = soln.strStr(haystack3, needle3)
    assert res == 6

    haystack4 = 'foo bar baz'
    needle4 = ''
    res = soln.strStr(haystack4, needle4)
    assert res == 0

    haystack5 = 'aaa'
    needle5 = 'aaaa'
    res = soln.strStr(haystack5, needle5)
    assert res == -1

    haystack6 = 'mississippi'
    needle6 = 'issipi'
    res = soln.strStr(haystack6, needle6)
    assert res == -1

    haystack7 = 'a'
    needle7 = 'a'
    res = soln.strStr(haystack7, needle7)
    assert res == 0
