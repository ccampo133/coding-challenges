# O(n)
def has_all_uniq_chars_with_set(s):
    return len(s) == len(set(s))


# O(n**2)
def has_all_uniq_chars(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                return False
    return True


# O(n log n + n) == O(n log n)
def has_all_uniq_chars_sorted(s):
    # This is O(n log n)
    sorted_s = sorted(s)

    # This is O(n)
    for i in range(len(sorted_s)):
        if i > 0 and sorted_s[i] == sorted_s[i - 1]:
            return False
    return True


if __name__ == '__main__':
    uniq = 'abcdefg hijklmnop'
    print(has_all_uniq_chars_with_set(uniq))  # True
    print(has_all_uniq_chars(uniq))
    print(has_all_uniq_chars_sorted(uniq))

    non_uniq = 'aabcd   efg'
    print(has_all_uniq_chars_with_set(non_uniq))  # False
    print(has_all_uniq_chars(non_uniq))
    print(has_all_uniq_chars_sorted(non_uniq))
