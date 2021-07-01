# O(a log a + b log b) where a = len(s1) and b = len(s2)
# This breaks down to O(n log n) when s1 and s2 have the same length
def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)


def is_permutation_linear(s1, s2):
    counts = {'s1': {}, 's2': {}}

    def incr_dict(d, k):
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

    for c in s1:
        incr_dict(counts['s1'], c)

    for c in s2:
        incr_dict(counts['s2'], c)

    if len(counts['s1']) != len(counts['s2']):
        return False

    for key in counts['s1']:
        if key not in counts['s2']:
            return False
        if counts['s1'][key] != counts['s2'][key]:
            return False

    return True


# This is more space efficient than the above version (one dict vs two)
# but uses the same concept to solve the problem
def is_permutation_linear2(s1, s2):
    counts = {}
    for c in s1:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    for c in s2:
        if c in counts:
            counts[c] -= 1
        else:
            return False

    for c in counts:
        if counts[c] != 0:
            return False
    return True


if __name__ == '__main__':
    s1 = 'abcdeff'
    s2 = 'defbacf'
    print(is_permutation(s1, s2))  # True
    print(is_permutation_linear(s1, s2))
    print(is_permutation_linear2(s1, s2))
