class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i % 2 ==0:
                    if mat[i][(j+k)%len(mat[i])] != mat[i][j]:
                        return False
                else:
                    if mat[i][(j-k)%len(mat[i])] != mat[i][j]:
                        return False
        return True