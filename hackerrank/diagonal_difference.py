# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    l2r, r2l = 0, 0
    n = len(arr[0])  # Problem constraints mandate the array is a square
    for i in range(n):
        l2r += arr[i][i]
        r2l += arr[i][n - 1 - i]
    return abs(l2r - r2l)


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]

    assert diagonalDifference(arr) == 2
