class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = 0
        prev = 0
        for elem in requests:
            time += abs(elem-prev)
            prev = elem
        return time