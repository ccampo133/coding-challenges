# https://www.hackerrank.com/challenges/plus-minus/problem

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for n in arr:
        if n < 0:
            neg += 1
        elif n > 0:
            pos += 1
        else:
            zero += 1

    print(round(pos / len(arr), 6))
    print(round(neg / len(arr), 6))
    print(round(zero / len(arr), 6))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
