def is_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == c ** 2


# This is slowwww :(, but works
def triplet_product(n):
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if is_triplet(a, b, c):
                    print(a, b, c)
                    if sum((a, b, c)) == n:
                        return a * b * c
    return None


if __name__ == '__main__':
    print(triplet_product(1000))
