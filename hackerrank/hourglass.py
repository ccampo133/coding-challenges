# https://www.hackerrank.com/challenges/30-2d-arrays/problem
def max_hourglass_sum(a):
    h, w = len(a), len(a[0])
    max_sum = None
    for row in range(h - 2):
        for col in range(w - 2):
            hg_sum = a[row][col] + a[row][col + 1] + a[row][col + 2] \
                     + a[row + 1][col + 1] \
                     + a[row + 2][col] + a[row + 2][col + 1] + a[row + 2][col + 2]
            if max_sum is None or hg_sum > max_sum:
                max_sum = hg_sum
    return max_sum


if __name__ == '__main__':
    a1 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    res1 = max_hourglass_sum(a1)
    assert res1 == 19

    a2 = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]
    res2 = max_hourglass_sum(a2)
    assert res2 == -6
