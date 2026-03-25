class Solution:
    def climbStairs(self, n , helper = {}):
        if (n ==0) or (n==1):
            return 1
        if n in helper:
            return helper[n]
        helper[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return helper[n]
        