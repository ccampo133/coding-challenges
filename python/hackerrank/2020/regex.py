# https://www.hackerrank.com/challenges/30-regex-patterns/problem

import re


def search_gmail(data: list):
    return sorted([row['first_name'] for row in data if re.search('@gmail.com', row['email_id']) is not None])


if __name__ == '__main__':
    data = []

    # vals = [
    #     ('riya', 'riya@gmail.com'),
    #     ('julia', 'julia@julia.me'),
    #     ('julia', 'sjulia@gmail.com'),
    #     ('julia', 'julia@gmail.com'),
    #     ('samantha', 'samantha@gmail.com'),
    #     ('tanya', 'tanya@gmail.com')
    # ]

    vals = [
        ('riya', 'riya@gmail.com'),
        ('julia', 'julia@julia.me'),
        ('julia', 'sjulia@gmail.com'),
        ('julia', 'julia@gmail.com'),
        ('samantha', 'samantha@gmail.com'),
        ('tanya', 'tanya@gmail.com'),
        ('riya', 'ariya@gmail.com'),
        ('julia', 'bjulia@julia.me'),
        ('julia', 'csjulia@gmail.com'),
        ('julia', 'djulia@gmail.com'),
        ('samantha', 'esamantha@gmail.com'),
        ('tanya', 'ftanya@gmail.com'),
        ('riya', 'riya@live.com'),
        ('julia', 'julia@live.com'),
        ('julia', 'sjulia@live.com'),
        ('julia', 'julia@live.com'),
        ('samantha', 'samantha@live.com'),
        ('tanya', 'tanya@live.com'),
        ('riya', 'ariya@live.com'),
        ('julia', 'bjulia@live.com'),
        ('julia', 'csjulia@live.com'),
        ('julia', 'djulia@live.com'),
        ('samantha', 'esamantha@live.com'),
        ('tanya', 'ftanya@live.com'),
        ('riya', 'gmail@riya.com'),
        ('priya', 'priya@gmail.com'),
        ('preeti', 'preeti@gmail.com'),
        ('alice', 'alice@alicegmail.com'),
        ('alice', 'alice@gmail.com'),
        ('alice', 'gmail.alice@gmail.com')
    ]
    n = len(vals)

    # n = int(input())
    for i in range(n):
        # first_name, email_id = input().split()
        first_name, email_id = vals[i]
        data.append({'first_name': first_name, 'email_id': email_id})

    results = search_gmail(data)
    for name in results:
        print(name)
