# https://neetcode.io/problems/buy-and-sell-crypto
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Buy and Sell Crypto
# You are given an integer array prices where prices[i] is the price of NeetCoin
# on the ith day.
#
# You may choose a single day to buy one NeetCoin and choose a different day in
# the future to sell it.
#
# Return the maximum profit you can achieve. You may choose to not make any
# transactions, in which case the profit would be 0.
#
# Example 1:
#
# Input: prices = [10,1,5,6,7,1]
#
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
#
# Example 2:
#
# Input: prices = [10,8,7,5,2]
#
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.
#
# Constraints:
#
# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

# time: O(n2)
# space: O(1)
def max_profit_slow(prices):
    profit = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i, len(prices)):
            sell = prices[j]
            diff = sell - buy
            profit = max(profit, diff)
    return profit


# time: O(n)
def max_profit_fast(prices):
    if len(prices) < 2:
        return 0
    profit, buy = 0, 0
    for sell in range(1, len(prices)):
        p1, p2 = prices[buy], prices[sell]
        if p2 < p1:
            buy = sell
        else:
            diff = p2 - p1
            profit = max(profit, diff)
    return profit


def test_max_profit():
    prices = [2, 1, 2, 1, 0, 1, 2]
    want = 2
    assert max_profit_slow(prices) == want
    assert max_profit_fast(prices) == want


def test_max_profit2():
    prices = [7, 1, 2, 12, 0]
    want = 11
    assert max_profit_slow(prices) == want
    assert max_profit_fast(prices) == want
