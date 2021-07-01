class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = [c.lower() for c in s if c.isalnum()]
        rev = chars[::-1]

        return chars == rev


if __name__ == '__main__':
    soln = Solution()

    s = "A man, a plan, a canal: Panama"
    res = soln.isPalindrome(s)
    print(res)  # True

    s = "race a car"
    res = soln.isPalindrome(s)
    print(res)  # False

    s = "RaCeCaR"
    res = soln.isPalindrome(s)
    print(res)  # True
