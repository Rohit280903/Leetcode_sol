class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        i = 0
        while i < len(nums) :
            if nums[i] in freq:
                if freq[nums[i]] >= k:
                    nums.remove(nums[i])
                else:
                    freq[nums[i]] += 1
                    i += 1
            else:
                freq[nums[i]] = 1
                i += 1
        return nums