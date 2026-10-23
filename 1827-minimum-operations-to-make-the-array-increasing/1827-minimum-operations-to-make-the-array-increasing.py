class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        if nums == sorted(nums) and len(nums) == len(set(nums)):
            return res
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                res += (prev - nums[i] + 1)
                prev += 1
            else:
                prev = nums[i] 
        return res
