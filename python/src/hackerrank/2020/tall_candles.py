# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(ar):
    cur_max, count = 0, 0
    for n in ar:
        if n > cur_max:
            cur_max = n
            count = 1
        elif n == cur_max:
            count += 1
    return count


if __name__ == '__main__':
    vals = [3, 2, 1, 3]
    assert birthdayCakeCandles(vals) == 2
