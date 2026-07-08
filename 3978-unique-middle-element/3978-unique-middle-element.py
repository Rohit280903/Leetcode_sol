class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = nums[len(nums) // 2]
        res = 0
        for elem in nums:
            if n == elem:
                res += 1
        return res == 1