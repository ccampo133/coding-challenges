# The naive way - work back to front
def urlify(s):
    # Count the end spaces
    ws_count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            ws_count += 1
        else:
            break

    # Replace characters
    new_str = ''
    for i in range(len(s) - ws_count):
        if s[i] == ' ':
            new_str += '%20'
        else:
            new_str += s[i]

    return new_str


def urlify_pythonic(s):
    return s.rstrip().replace(' ', '%20')


if __name__ == '__main__':
    s = 'Mr John Smith   '
    print(urlify(s))
    print(urlify_pythonic(s))
