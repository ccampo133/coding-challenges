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

        return sgn * rev if rev <= 2 ** 31 - 1 else 0

    # This is more efficient according to LeetCode ¯\_(ツ)_/¯
    def reverse_string(self, x: int) -> int:
        sgn = self.sign(x)
        rev = int(str(sgn * x)[::-1])  # Convert to a string, reverse it, then convert back to an int
        return sgn * rev if rev <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    x = -1234567890
    solution = Solution().reverse(x)
    assert solution == -987654321
    print(solution)
    print(Solution().reverse_string(x))
