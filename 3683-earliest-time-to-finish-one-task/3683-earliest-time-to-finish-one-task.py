class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mini = sum(tasks[0])
        for i in range(1,len(tasks)):
            mini = min(mini, sum(tasks[i]))
        return mini