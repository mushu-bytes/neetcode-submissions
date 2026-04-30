class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for c in t:
            target[c] = 1 + target.get(c, 0)
    
        curr = {}
        have, need = 0, len(t)
        l = 0
        resLen = float('inf')
        res = ""
        for r in range(len(s)):
            curr[s[r]] = 1 + curr.get(s[r], 0)
            if s[r] in target and curr[s[r]] <= target[s[r]]:
                have += 1
            while have == need:
                if resLen > (r - l + 1):
                    res = s[l: r + 1]
                    resLen = (r - l + 1)

                curr[s[l]] -= 1
                if s[l] in target and curr[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        return res
            


