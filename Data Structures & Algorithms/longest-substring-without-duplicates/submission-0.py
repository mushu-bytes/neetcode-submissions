class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, len(seen))
            print(l, r)
        return maxLen
