class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # elem_sum, digit_sum = 0, 0
        # for elem in nums:
        #     elem_sum += elem
        # for elem in nums:
        #     elem = str(elem)
        #     for i in elem:
        #         digit_sum += int(i)
        # return abs(elem_sum - digit_sum) 
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num > 0:
                digit_sum += num % 10 #take last digit
                num //= 10 #remove last digit
        return abs(element_sum - digit_sum)