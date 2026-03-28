class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum, digit_sum = 0, 0
        for elem in nums:
            elem_sum += elem
        for elem in nums:
            elem = str(elem)
            for i in elem:
                digit_sum += int(i)
        return abs(elem_sum - digit_sum) 
