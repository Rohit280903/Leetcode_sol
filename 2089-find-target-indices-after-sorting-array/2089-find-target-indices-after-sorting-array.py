class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = []
        i = 0
        while(i<len(nums)):
            if nums[i] == target:
                l.append(i)
            i += 1
        return l