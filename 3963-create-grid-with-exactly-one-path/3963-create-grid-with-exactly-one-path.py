class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for i in range(m):
            path = ""
            for j in range(n):
                if i == 0:
                    path += "."
                elif j == n -1:
                    path += "."
                else:
                    path += "#"
            res.append(path)
        return res
                 