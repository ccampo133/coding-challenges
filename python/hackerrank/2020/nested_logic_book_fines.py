#  https://www.hackerrank.com/challenges/30-nested-logic/problem

# Can use the date class for this, but it somewhat defeats the spirit of the problem.
def calc_fine(d_ex: int, m_ex: int, y_ex: int, d_act: int, m_act: int, y_act: int) -> int:
    if y_act < y_ex:
        return 0

    if y_act == y_ex:
        if m_act < m_ex:
            return 0
        if m_act == m_ex:
            if d_act <= d_ex:
                return 0
            return 15 * (d_act - d_ex)
        return 500 * (m_act - m_ex)
    return 10000


if __name__ == '__main__':
    d_act, m_act, y_act = map(int, input().split(' '))
    d_ex, m_ex, y_ex = map(int, input().split(' '))
    # d_act, m_act, y_act = 9, 6, 2015
    # d_ex, m_ex, y_ex = 6, 6, 2015
    print(calc_fine(d_ex, m_ex, y_ex, d_act, m_act, y_act))
