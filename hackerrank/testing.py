# https://www.hackerrank.com/challenges/30-testing/problem


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [15, 54, 13, 76, 1, 4, 5, 3, 2, 9, 27, 87, 91, 10, 11, 7, 12, 99]

    @staticmethod
    def get_expected_result():
        return 4


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [1, 2, 3, 0, 4, 0, 5]

    @staticmethod
    def get_expected_result():
        return 3


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


if __name__ == '__main__':
    TestWithEmptyArray()
    TestWithUniqueValues()
    TestiWithExactyTwoDifferentMinimums()
    print("OK")
