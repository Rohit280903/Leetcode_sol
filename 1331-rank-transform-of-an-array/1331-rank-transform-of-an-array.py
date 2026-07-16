class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = sorted(arr)
        d = {}
        j = 1
        for i in range(len(n)):
            if n[i] not in d: 
                d[n[i]] = j
                j += 1
        ans = []
        for elem in arr:
            ans.append(d[elem])
        return ans