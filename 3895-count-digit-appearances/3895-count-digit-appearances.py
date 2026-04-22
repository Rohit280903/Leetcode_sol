class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # cnt = 0
        # for elem in nums:
        #     elem = str(elem)
        #     for n in elem:
        #         if n == str(digit):
        #             cnt += 1
        # return cnt
        nums="".join(map(str,nums))
        return nums.count(str(digit))