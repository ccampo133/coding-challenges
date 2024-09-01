# https://neetcode.io/problems/meeting-schedule
# Meeting Schedule
# Given an array of meeting time interval objects consisting of start and end
# times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a
# person could add all meetings to their schedule without any conflicts.
#
# Example 1:
#
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation:
#
# (0,30) and (5,10) will conflict
# (0,30) and (15,20) will conflict

# Example 2:
# Input: intervals = [(5,8),(9,15)]
# Output: true
# Note:
#
# (0,8),(8,10) is not considered a conflict at 8
#
# Constraints:
#
# 0 <= intervals.length <= 500
# 0 <= intervals[i].start < intervals[i].end <= 1,000,000
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def is_not_conflict(intervals: list[Interval]):
    if len(intervals) <= 1:
        return True
    # The intervals aren't guaranteed to be sorted.
    intervals.sort(key=lambda i: i.start)
    prev = intervals[0]
    for interval in intervals[1:]:
        if interval.start < prev.end:
            return False
        # The only other case here would be if interval.end < prev.end. We don't
        # need to check that because interval.end is guaranteed to be greater
        # than interval.start.
        prev = interval
    return True


def test1():
    intervals = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20),
    ]
    assert not is_not_conflict(intervals)


def test2():
    intervals = [
        Interval(5, 8),
        Interval(9, 15),
    ]
    assert is_not_conflict(intervals)

def test3():
    intervals = [
        Interval(5, 10),
        Interval(0, 4),
    ]
    assert is_not_conflict(intervals)
