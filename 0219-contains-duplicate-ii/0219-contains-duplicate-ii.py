class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # last_seen = {}
        # for i, num in enumerate(nums):
        #     if num in last_seen and i - last_seen[num] <= k:
        #         return True
        #     last_seen[num] = i
        # return False

        if len(nums) == len(set(nums)):
            return False
        else:
            for i in range(len(nums)):
                if nums[i] in nums[i+1 : i+k+1]:
                    return True
            return False