def is_one_edit(s1, s2):
    # Difference of two or more characters - instant fail. Can use abs()
    # here, but would rather not for the purposes of this exercise
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False

    # Find the shorter string - it will only be one char shorter by this point
    shortest = s1 if len(s1) < len(s2) else s2
    mismatched = 1 if len(s1) != len(s2) else 0
    for i in range(len(shortest)):
        if s1[i] != s2[i]:
            mismatched += 1
        if mismatched > 1:
            return False

    return True


if __name__ == '__main__':
    s1 = 'pale'
    s2 = 'pale'
    print(is_one_edit(s1, s2))
