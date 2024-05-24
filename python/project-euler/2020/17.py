num_to_word = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def number_to_word(n):
    if 20 >= n > 0:
        return num_to_word[n]

    # 21 - 99
    if n < 100:
        n_ten = n // 10
        n_one = n - (n_ten * 10)
        return f'{num_to_word[n_ten * 10]} {num_to_word[n_one]}'

    # 101 - 999
    if n < 1000:
        n_hundred = n // 100
        n_ten = (n // 10) - (n_hundred * 10)
        n_one = n - (n_hundred * 100) - (n_ten * 10)

        word = f'{num_to_word[n_hundred]} hundred'
        if n_ten == 0 and n_one == 0:
            return word
        elif n_ten == 0 and n_one > 0:
            word += f' and {num_to_word[n_one]}'
        elif n_ten == 1 and n_one > 0:
            word += f' and {num_to_word[10 * n_ten + n_one]}'
        else:
            word += f' and {num_to_word[n_ten * 10]} {num_to_word[n_one]}'

        return word

    # 1000
    if n == 100 or n == 1000:
        return f'one {num_to_word[n]}'

    # We don't support anything else :\
    return None


def count_number_chars(n):
    word = number_to_word(n)
    return len(word.replace(' ', ''))


def compute():
    total = 0
    for i in range(1, 1001):
        print(number_to_word(i))
        total += count_number_chars(i)
    return total


if __name__ == '__main__':
    print(compute())
