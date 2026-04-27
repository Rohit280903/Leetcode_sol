class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = []
        for m in matrix:
            result.append(sum(m))
        return result