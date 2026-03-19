class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # else:
        #     return -1
        left = 0
        right = sum(nums)
        for i,num in enumerate(nums):
            left += num
            if left == right:
                return i
            right -= num
        return -1 