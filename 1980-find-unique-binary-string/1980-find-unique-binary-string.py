class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        r = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                r += "0"
            else:
                r += "1"
        return r