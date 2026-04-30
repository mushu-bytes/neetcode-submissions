class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        majorChar = s[0]
        maxWindow = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] > window[majorChar]:
                majorChar = s[r]
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow
            

