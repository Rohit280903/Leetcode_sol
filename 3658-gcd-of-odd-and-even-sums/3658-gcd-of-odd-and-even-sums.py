class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o = n * (2 + (n-1)*2) // 2
        e = n * (4 + (n-1)*2) // 2
        return gcd(o,e)