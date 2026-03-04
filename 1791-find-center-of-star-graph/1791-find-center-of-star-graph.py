class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b=edges[0]
        c,d=edges[1]

        if a==c or a==d:
            return a
        return b
        
        
        
        
        # d = {}
        # for elem in edges:
        #     for i in range(2):
        #         if elem[i] in d:
        #             d[elem[i]] = d[elem[i]] + 1
        #         else:
        #             d[elem[i]] = 1
        # d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        # return next(iter(d))
        # return list(d.keys())[0]