class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = x
        sum = 0
        while y > 0:
            sum += (y % 10)
            y //= 10
        if x % sum == 0:
            return sum
        else:
            return -1