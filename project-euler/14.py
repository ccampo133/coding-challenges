def collatz_func(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def sequence(start):
    seq, i = [], start
    while i != 1:
        seq.append(i)
        i = collatz_func(i)
    seq.append(1)
    return seq


def longest_chain(max_start):
    max_len, num = 0, max_start
    for i in range(max_start, 0, -1):
        seq = sequence(i)
        if len(seq) > max_len:
            max_len = len(seq)
            num = i
    return num


if __name__ == '__main__':
    print(longest_chain(1000000))
