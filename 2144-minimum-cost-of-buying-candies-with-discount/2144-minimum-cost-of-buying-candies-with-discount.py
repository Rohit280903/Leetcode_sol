class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        res = 0
        cnt = 0
        for i in range(len(cost)):
            if cnt == 2:
                cnt = 0
            else:
                res += cost[i]
                cnt += 1
        return res 