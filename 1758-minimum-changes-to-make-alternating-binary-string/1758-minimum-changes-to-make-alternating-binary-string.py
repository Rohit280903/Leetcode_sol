class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            if int(s[i]) != i%2:
                ans += 1
        return min(ans, n-ans)