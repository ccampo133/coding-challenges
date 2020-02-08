# https://www.hackerrank.com/challenges/simple-array-sum/problem

import os


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return sum(ar)


# Here's how to do it by hand (no builtins)
def sum_linear(ar):
    cur_sum = 0
    for elem in ar:
        cur_sum += ar
    return cur_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
