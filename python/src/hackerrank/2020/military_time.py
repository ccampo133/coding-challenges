def timeConversion(s):
    ampm = s[-2:]
    hr = s[:2]
    if ampm == 'AM':
        return s[:-2] if hr != '12' else '00' + s[2:-2]
    return s[:-2] if hr == '12' else str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    s1 = '07:05:45PM'
    assert timeConversion(s1) == '19:05:45'

    s2 = '07:05:45AM'
    assert timeConversion(s2) == '07:05:45'

    s3 = '12:06:21PM'
    assert timeConversion(s3) == '12:06:21'

    s4 = '12:06:21AM'
    assert timeConversion(s4) == '00:06:21'
