class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        maxWindow = 0
        res = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            maxWindow = max(maxWindow, window[s[r]])
            if (r - l + 1) - maxWindow > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
            

