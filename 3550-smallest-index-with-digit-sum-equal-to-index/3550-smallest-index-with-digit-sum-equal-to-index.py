class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            total = 0
            elem = str(nums[i])
            for j in elem:
                total += int(j)
            if total == i:
                return i
        return -1
