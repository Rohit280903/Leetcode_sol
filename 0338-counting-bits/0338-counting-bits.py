class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = [0]
        # for i in range(1, n+1):
        #     temp = bin(i)
        #     temp = temp.split('1')
        #     res.append(len(temp)-1)
        # return res
        ans = [0] * (n+1)
        for idx in range(1, n+1):
            ans[idx] = ans[idx//2] + (idx%2)
        return ans