from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        first = strs[0]
        longest_prefix = None
        for i in range(1, len(strs)):
            prefix, cur = '', strs[i]
            shorter = first if len(first) <= len(cur) else cur
            for j in range(len(shorter)):
                if j == 0 and first[j] != cur[j]:
                    return ''
                elif j + 1 > len(prefix) and first[j] == cur[j]:
                    prefix += first[j]
            if not longest_prefix or len(prefix) < len(longest_prefix):
                longest_prefix = prefix
        return longest_prefix

    def longestCommonPrefix_faster(selfs, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]  # Doesn't matter which string we chose
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix


if __name__ == '__main__':
    soln = Solution()
    strs1 = ['flower', 'flow', 'flight']
    strs2 = ['dog', 'racecar', 'car']
    strs3 = ['flower', 'flow', 'car']
    strs4 = []
    strs5 = ['flower']
    assert soln.longestCommonPrefix(strs1) == 'fl'
    assert soln.longestCommonPrefix(strs2) == ''
    assert soln.longestCommonPrefix(strs3) == ''
    assert soln.longestCommonPrefix(strs4) == ''
    assert soln.longestCommonPrefix(strs5) == 'flower'
    assert soln.longestCommonPrefix_faster(strs1) == 'fl'
    assert soln.longestCommonPrefix_faster(strs2) == ''
    assert soln.longestCommonPrefix_faster(strs3) == ''
    assert soln.longestCommonPrefix_faster(strs4) == ''
    assert soln.longestCommonPrefix_faster(strs5) == 'flower'
