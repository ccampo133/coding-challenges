# https://www.hackerrank.com/challenges/happy-ladybugs/problem
# This one was tricky - I had to look at the discussion for a hint

# O(n)
# This solution is predicated on the following conditions:
#   A board can only be made happy IFF
#     1. There is at least one empty space and no color has count 1
#     2. There are no empty spaces and the board is already happy.
def happyLadybugs(b):
    counts = {}
    for c in b:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    # No empty spaces - check if the board is 'happy'
    if '_' not in counts:
        return 'YES' if len(b) != 1 and is_happy(b) else 'NO'

    # There is at least one empty space, so ensure no 'colors'
    # have a single count. If they do, the board can never be
    # 'happy' and we can return instantly.
    for c in counts:
        if c != '_' and counts[c] == 1:
            return 'NO'

    # If we've made it this far, the board can be happy with some series of moves
    return 'YES'


# This only works for boards that don't have empty spaces (i.e. no underscores)
def is_happy(s):
    for i in range(len(s)):
        if i == len(s) - 1:
            return s[i] == s[i - 1]
        if s[i - 1] != s[i] and s[i + 1] != s[i]:
            return False
    return True


if __name__ == '__main__':
    b1 = 'AABBC'
    b2 = 'AABBC_C'
    b3 = '_'
    b4 = 'DD__FQ_QQF'
    b5 = 'AABCBC'
    b6 = 'G'
    b7 = 'GR'
    b8 = '_GR_'
    b9 = '_R_G_'
    b10 = 'R_R_R'
    b11 = 'RRGGBBXX'
    b12 = 'RRGGBBXY'

    assert happyLadybugs(b1) == 'NO'
    assert happyLadybugs(b2) == 'YES'
    assert happyLadybugs(b3) == 'YES'
    assert happyLadybugs(b4) == 'YES'
    assert happyLadybugs(b5) == 'NO'
    assert happyLadybugs(b5) == 'NO'
    assert happyLadybugs(b6) == 'NO'
    assert happyLadybugs(b7) == 'NO'
    assert happyLadybugs(b8) == 'NO'
    assert happyLadybugs(b9) == 'NO'
    assert happyLadybugs(b10) == 'YES'
    assert happyLadybugs(b11) == 'YES'
    assert happyLadybugs(b12) == 'NO'
