class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c in closed:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if closed[c] != prev:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


if __name__ == '__main__':
    soln = Solution()
    s1 = '()'
    s2 = '()[]{}'
    s3 = '(]'
    s4 = '([)]'
    s5 = '{[]}'
    assert soln.isValid(s1)
    assert soln.isValid(s2)
    assert not soln.isValid(s3)
    assert not soln.isValid(s4)
    assert soln.isValid(s5)
