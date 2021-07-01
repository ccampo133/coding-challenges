# https://leetcode.com/discuss/interview-question/352459
# This is a worst-case quadratic time solution - O((n - k + 1) * k) = O(nk - k^2)
def max_sub_array(a, k):
    cur_max = []
    for i in range(len(a) - k + 1):
        # cur_max = max(cur_max, a[i:i + k])  # Using Python's 'max' function
        cur_max = max_array(cur_max, a[i:i + k])  # Array slicing time complexity is O(k)
    return cur_max


# O(n) worst case
def max_array(a1, a2):
    # Arrays are assumed to be the same length. If not, return the longest:
    if len(a1) != len(a2):
        return a1 if len(a1) > len(a2) else a2

    for i in range(len(a1)):  # len(a1) == len(a2)
        if a1[i] > a2[i]:
            return a1
        elif a2[i] > a1[i]:
            return a2
    return a1  # arrays are equivalent - return the first one


# O(n) solution
def max_sub_array_linear(a, k):
    cur_max, start = 0, 0  # This is safe because elements of a are guaranteed to be positive
    for i in range(len(a) - k + 1):
        if a[i] > cur_max:
            cur_max, start = a[i], i
    return a[start: start + k]


if __name__ == '__main__':
    a = [1, 4, 3, 2, 5, 9, 9, 2, 4, 5, 8, 7, 1, 1]
    res1 = max_sub_array(a, 4)
    res2 = max_sub_array_linear(a, 4)
    print(res1, res2)
    assert res1 == res2 == [9, 1, 2, 4]
