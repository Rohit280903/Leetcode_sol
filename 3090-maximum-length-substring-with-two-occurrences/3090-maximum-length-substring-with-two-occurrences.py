class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = {}
        i = res = 0
        for j, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1
            while cnt[c] > 2:
                cnt[s[i]] -= 1
                i += 1
            res = max(res, j-i+1)
        return res