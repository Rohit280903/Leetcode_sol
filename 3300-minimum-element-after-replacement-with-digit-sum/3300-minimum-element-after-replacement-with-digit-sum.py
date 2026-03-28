class Solution:
    def minElement(self, nums: List[int]) -> int:
        j = 0
        for elem in nums:
            res = 0
            elem = str(elem)
            for i in elem:
                res += int(i)
            nums[j] = res
            j += 1
        print(nums)
        return min(nums)