class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] % 2:
            flag = True
        else:
            flag = False

        for i in range(1, len(nums)):
            if nums[i] % 2:
                if flag == True:
                    return False
                else:
                    flag = True
            else:
                if flag == False:
                    return False
                else:
                    flag = False
        return True
