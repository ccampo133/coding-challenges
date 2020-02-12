# https://www.hackerrank.com/challenges/apple-and-orange/problem

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    n_apples = count_fruit(s, t, a, apples)
    n_oranges = count_fruit(s, t, b, oranges)
    print(n_apples)
    print(n_oranges)


def count_fruit(s, t, x, fruit):
    n = 0
    for d in fruit:
        pos = x + d
        if t >= pos >= s:
            n += 1
    return n


if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
