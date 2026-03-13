class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        profit = 0
        while s < len(prices):
            curr_profit = prices[s] - prices[b]
            if prices[b] < prices[s]:
                profit = max(curr_profit, profit)
            else:
                b = s
            s += 1
        return profit