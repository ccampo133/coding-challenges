# This solution is basically the same as #7, but it explicitly
# asks you do solve it without converting the input number to
# a string.
class Solution:
    def sign(self, x: int) -> int:
        return -1 if x < 0 else 1

    def reverse(self, x: int) -> int:
        sgn = self.sign(x)
        x *= sgn
        rev = 0
        while x != 0:
            rev = (10 * rev) + x % 10
            x //= 10
        return rev

    def isPalindrome(self, x: int) -> bool:
        return False if self.sign(x) == -1 else self.reverse(x) == x
