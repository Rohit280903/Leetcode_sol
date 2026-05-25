class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) - 1 == len(set(nums)):
            nums.sort()
            if nums[-1] == nums[-2] and nums[-1] == len(set(nums)):
                return True
        return False
