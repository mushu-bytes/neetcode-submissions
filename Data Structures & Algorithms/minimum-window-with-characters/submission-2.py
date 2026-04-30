class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for c in t:
            target[c] = 1 + target.get(c, 0)
        
        have, need = 0, len(t)
        res = s + t
        curr = {} # letter : count
        l = 0
        for r in range(len(s)):
            # skip irrelevants
            if s[r] not in target:
                continue
            if s[r] in target and not curr:
                # first valid char
                l = r

            curr[s[r]] = 1 + curr.get(s[r], 0)
            if curr[s[r]] <= target[s[r]]:
                have += 1
            print(have, need)
            while curr[s[r]] > target[s[r]] and have >= need:
                if s[l] in target:
                    curr[s[l]] -= 1
                l += 1

            while s[l] not in curr and l < r:
                l += 1

            if curr == target and len(res) > (r - l + 1):
                res = s[l : r + 1]

        if res == s + t:
            res = ""
        return res


