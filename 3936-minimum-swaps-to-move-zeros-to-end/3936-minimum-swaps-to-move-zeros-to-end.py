class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        cnt = 0
        for elem in nums:
            if elem == 0:
                cnt += 1
        swap = 0
        n = len(nums) - 1
        while cnt > 0:
            if nums[n] == 0:
                cnt -= 1
                n -= 1
            else:
                cnt -= 1
                n -= 1
                swap += 1
        return swap