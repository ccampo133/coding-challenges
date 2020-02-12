#!/bin/python3

import os


def gradingStudents(grades):
    return [round_grade(grade) for grade in grades]


def round_grade(grade):
    if grade < 38:
        return grade
    next_multiple = grade + (5 - (grade % 5))
    return next_multiple if next_multiple - grade < 3 else grade


if __name__ == '__main__':

    print(round_grade(67))

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
