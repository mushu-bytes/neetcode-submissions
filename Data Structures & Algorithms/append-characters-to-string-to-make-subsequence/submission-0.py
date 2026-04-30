class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for j in range(len(s)):
            if i < len(t) and t[i] == s[j]:
                i += 1
        return len(t) - i