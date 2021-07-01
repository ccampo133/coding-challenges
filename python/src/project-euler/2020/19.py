def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def get_end_day(month, year):
    if month == 2 and is_leap_year(year):
        return 29
    if month == 2:
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def compute():
    dow = 0
    sundays = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            end_day = get_end_day(month, year)
            for day in range(1, end_day + 1):
                dow += 1
                if dow % 7 == 0 and day == 1 and year > 1900:
                    sundays += 1
    return sundays


if __name__ == '__main__':
    print(compute())
