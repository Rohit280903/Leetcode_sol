# class Solution:
#     def subarraySum(self, nums: List[int]) -> int:
#         res = 0
#         for i in range(len(nums)):
#             start = max(0, i - nums[i])
#             for j in range(start, i+1):
#                 res += nums[j]
#         return res
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            j = i - nums[i] - 1
            nums[i] += nums[i - 1]
            res += nums[i] - (0 if j < 0 else nums[j])
        return res
    