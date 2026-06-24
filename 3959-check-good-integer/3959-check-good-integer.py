class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n = str(n)
        digitSum = 0
        squareSum = 0
        for elem in n:
            digitSum += int(elem)
            squareSum += (int(elem) ** 2)
        return squareSum - digitSum >= 50