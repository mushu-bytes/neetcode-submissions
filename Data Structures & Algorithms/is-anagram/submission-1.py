class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = [0 for i in range(26)]
        tcount = [0 for i in range(26)]

        for c in s:
            scount[ord(c) - ord("a")] += 1
        for c in t:
            tcount[ord(c) - ord("a")] += 1
        
        return tuple(scount) == tuple(tcount)