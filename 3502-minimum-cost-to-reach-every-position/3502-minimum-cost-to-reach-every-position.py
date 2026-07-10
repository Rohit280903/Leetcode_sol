class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = [cost[0]]
        for i in range(1, len(cost)):
            res.append(min(res[i-1], cost[i]))
        return res