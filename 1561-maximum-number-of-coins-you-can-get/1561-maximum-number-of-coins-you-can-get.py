class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) // 3
        k = 1
        res = 0
        while k <= i:
            res += piles[-2*k]
            k += 1
        return res

