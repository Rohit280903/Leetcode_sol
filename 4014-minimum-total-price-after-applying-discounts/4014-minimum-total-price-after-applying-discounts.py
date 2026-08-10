class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        res = 0.00
        discounts.sort(reverse = True)
        prices.sort(reverse = True)
        for i in range(len(prices)):
            if i < len(discounts):
                res += (prices[i] *(100 - discounts[i]) / 100)
            else:
                res += prices[i]
        return res