class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        repeat = -1
        for row in grid:
            for elem in row:
                if elem not in seen:
                    seen.add(elem)
                else:
                    repeat = elem
        for i in range(1, n*n + 1):
            if i not in seen:
                miss = i
        return [repeat,miss]