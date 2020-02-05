# This is fairly slow - can be optimized... but it works at least.
def divisible(start, stop):
    n, rng = 1, range(stop, start - 1, -1)  # Starting from greatest to least is slightly faster
    while not is_evenly_divisible(n, rng):
        n += 1
    return n


def is_evenly_divisible(n, rng):
    for i in rng:
        if n % i > 0:
            return False
    return True


if __name__ == '__main__':
    print(divisible(1, 20))
