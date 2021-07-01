class Solution(object):
    def sign(self, x):
        return -1 if x < 0 else 1

    def reverse_math(self, x):
        """
        :type x: int
        :rtype: int
        """
        sgn = self.sign(x)
        x *= sgn

        rev = 0
        while x // 10 > 0:
            digit = x % 10
            rev = 10 * rev + digit
            x //= 10

        result = sgn * (10 * rev + (x % 10))

        if result > (2 ** 31 - 1) or result < -2 ** 31:
            return 0

        return result

    def reverse_string(self, x):
        """
        :type x: int
        :rtype: int
        """
        sgn = self.sign(x)
        x *= sgn

        rev = int(str(x)[::-1])

        return sgn * rev if rev <= 2 ** 31 - 1 else 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.reverse_math(x)


if __name__ == '__main__':
    soln = Solution()

    x = 321
    res = soln.reverse(x)
    print(res)

    x = -123
    res = soln.reverse(x)
    print(res)

    x = 120
    res = soln.reverse(x)
    print(res)

    x = 0
    res = soln.reverse(x)
    print(res)
