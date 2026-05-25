class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for elem in nums:
            for ch in str(elem):
                ans.append(int(ch))
        return ans
