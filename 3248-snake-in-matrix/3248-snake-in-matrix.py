class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        num = 0
        for ch in commands:
            match ch:
                case "RIGHT":
                    num += 1
                case "LEFT":
                    num -= 1
                case "DOWN":
                    num += n
                case "UP":
                    num -= n
        return num
