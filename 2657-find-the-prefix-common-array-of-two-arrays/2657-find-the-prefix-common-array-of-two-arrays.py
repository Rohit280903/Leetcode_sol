class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        a = set()
        b = set()
        for i in range(len(A)):
             a.add(A[i])
             b.add(B[i])
             C.append(len(a & b))
        return C