class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, 0
        n = len(colors)
        for i in range(n-1):
            if colors[i] != colors[-1]:
                left = n -1 - i
                break

        for j in range(n-1, 0, -1):
            if colors[0] != colors[j]:
                right = j
                break
        return max(left, right)

