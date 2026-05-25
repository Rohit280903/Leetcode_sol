class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums) + 1
        flag = 0
        temp = nums[0]
        for i in range(1,n):
            if nums[i%len(nums)] < temp:
                flag += 1
            temp = nums[i%len(nums)]
        if flag > 1:
            return False
        else:
            return True