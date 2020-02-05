from typing import List


class Solution:
    # This is the O(n^2) solution. It can be solved in linear time but it's pretty tricky.
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n
        for booking in bookings:
            start, end, seats = booking
            for i in range(start - 1, end):
                flights[i] += seats
        return flights


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    # bookings = [[2, 2, 30], [2, 2, 45]]
    # n = 2
    # bookings = [[3, 3, 5], [1, 3, 20], [1, 2, 15]]
    # n = 3

    print(Solution().corpFlightBookings(bookings, n))
