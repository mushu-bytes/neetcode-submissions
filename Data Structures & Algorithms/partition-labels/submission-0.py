class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counter = {}
        for c in s:
            counter[c] = 1 + counter.get(c, 0)
        substring = set()
        count = 0

        for i in range(len(s)):
            substring.add(s[i])
            count += 1
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                substring.remove(s[i])
            if not substring:
                res.append(count)
                count = 0

        return res