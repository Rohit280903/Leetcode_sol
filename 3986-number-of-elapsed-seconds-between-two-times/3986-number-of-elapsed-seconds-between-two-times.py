class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st = startTime.split(':')
        et = endTime.split(':')
        ss = 0
        es = 0
        for i in range(len(st)):
            if i == 0:
                ss += (int(st[i]) * 3600)
                es += (int(et[i]) * 3600)
            elif i == 1:
                ss += (int(st[i]) * 60)
                es += (int(et[i]) * 60)
            else:
                ss += int(st[i])
                es += int(et[i])
        return es - ss