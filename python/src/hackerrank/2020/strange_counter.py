# https://www.hackerrank.com/challenges/strange-code/problem

def strangeCounter(t):
    k = 3
    while t > k:
        t -= k
        k *= 2
    return k - t + 1


if __name__ == '__main__':
    t0 = 6
    assert strangeCounter(t0) == 4
