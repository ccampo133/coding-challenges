def is_permutation_of_palindrome(s):
    # Remove whitespace and normalize case
    # O(n)
    s = s.replace(' ', '').lower()

    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    # Even length strings must have an even count of ALL characters
    # O(n)
    if len(s) % 2 == 0:
        for c in counts:
            if counts[c] % 2 != 0:
                return False
        return True

    # Odd length strings must have an even count of all characters except ONE
    # O(n)
    num_odd = 0
    for c in counts:
        if counts[c] % 2 != 0 and num_odd >= 1:
            return False
        elif counts[c] % 2 != 0:
            num_odd += 1
    return True


if __name__ == '__main__':
    s = 'tawc towoa'
    print(is_permutation_of_palindrome(s))
